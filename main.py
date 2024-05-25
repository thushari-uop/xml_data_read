import logging
import xml.etree.ElementTree as ET
import psycopg2
import sys
import multiprocessing 
from multiprocessing import Pool
from multiprocessing import Pool
from config import get_predefined_tag_string, get_predefined_temp_table_name, get_predefined_cur_table_name, get_histry_table_name, connection_string, setup_logging
from xml_processing import get_file_names, has_repeated_immediate_child_tags, parallelProcess
from db_operations import create_table_and_insert_data, table_exists, execute_query_from_dic, row_count_of_table, row_count_of_distinct_rows, drop_table, histry_update, current_table_update, ensure_columns_exist
from utilities.table_update_query import sql_temp_table_update_queries, required_columns_dict
from utilities.table_create_query import sql_temp_table_create_queries


# Set the encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')


if __name__ == "__main__":
    setup_logging()
    logging.info('Main program started')

    print("Read Data from XML")

    folder_path = input("Enter the folder path containing XML files: ")
    table_name = input("Enter the table name to store data: ")
    tag = get_predefined_tag_string(table_name)
    temp_table = get_predefined_temp_table_name(table_name)
    current_table = get_predefined_cur_table_name(table_name)
    histry_table = get_histry_table_name(table_name)

    # Get the list of XML files from the specified folder
    file_list = get_file_names(folder_path)

    Final_List=[]
    for file in file_list:
        try:
            xml_file = f'{folder_path}\\{str(file)}'
            print(xml_file)
            tree = ET.parse(xml_file)
            root1 = tree.getroot()

            # Flist=[]
            target_list=[tag for tag in root1 if has_repeated_immediate_child_tags(tag)]
            target_tag1 = root1.find(tag)#(target_list[0])
            path1 = 'Root'
        
            ######################################################################
            multi_process_tags = [tag for tag in target_tag1 if len(list(tag)) > 0]
            
            # multi-process manager
            manager = multiprocessing.Manager()
            result_list = manager.list()  # shared list to store result of each process

            # list to hold process
            
            # creating processes
            repeatTags=manager.list()#fot the repeated tags
            processes = [(root1, tag, f'{str(root1.tag)}_{target_tag1.tag}', result_list, repeatTags) for tag in multi_process_tags]

            #pool of 20 processes
            with Pool(20) as pool:
                pool.starmap(parallelProcess, processes)
        
            # print(result_list)

            for sublist in result_list:
                for item in sublist:
                    if item not in Final_List:
                        Final_List.append(item)
                                        
            logging.info('%s processed', file)

        except Exception as e:
            logging.error('%s not processed', file)
            print(f"Error processing XML file: {file}")

    try:
        with psycopg2.connect(connection_string) as conn:
            with conn.cursor() as cursor:

                create_table_and_insert_data(cursor, Final_List, table_name)
                required_columns = required_columns_dict[table_name]
                ensure_columns_exist(cursor, table_name, required_columns)

                old_cur_table_row_count = 0

                old_temp_table_row_count = 0
                cur_temp_table_row_count = 0
                distinct_row_count = 0

                # get current table row count
                if table_exists(cursor, (current_table)):
                    old_cur_table_row_count = row_count_of_table(cursor, current_table)
                else:
                    old_cur_table_row_count = 0

                # read data to temp table
                if table_exists(cursor, (temp_table)):
                    old_temp_table_row_count = row_count_of_table(cursor, temp_table)
                    execute_query_from_dic(cursor, sql_temp_table_update_queries, (table_name))
                    cur_temp_table_row_count = row_count_of_table(cursor, temp_table)
                    # print("Temporary Table Update!")
                else:
                    execute_query_from_dic(cursor, sql_temp_table_create_queries, (table_name))
                    # print(f"Create {table_name} table and insert data!")
                    cur_temp_table_row_count = row_count_of_table(cursor, temp_table)

                # After the Read the XML files and insert data into tables
                if(cur_temp_table_row_count != None):
                    # Display Summary
                    print(f"\nPrevious row count of \t{temp_table} table: {old_temp_table_row_count}")
                    print(f"Current row count of \t{temp_table} table: {cur_temp_table_row_count}")
                    print(f"Pending row count to add {current_table} table: {row_count_of_distinct_rows(cursor,temp_table)}")

                    
                    print(f"\nOptions")
                    print(f"\t1.Add read data to current table")
                    print(f"\t2.Update Histry Table and Add read data to current table")
                    print(f"\t3.Exit")

                    input_option = input("Your Option? :")

                    if input_option == '1' or input_option == '2':
                        if table_exists(cursor, current_table):
                            if input_option == '1':
                                current_table_update(cursor,temp_table, current_table)
                                    
                            elif input_option == '2':
                                histry_update(cursor, table_name)
                                current_table_update(cursor,temp_table, current_table)
                                    
                        else:
                            input_permision = input(f"\nCurrent {current_table} table does not exist. \nDo you want to create and update current table from read data (Yes/No)?\n").lower()
                            # Create and Update current table
                            if(input_permision == "yes"): 
                                cursor.execute(f"CREATE TABLE {current_table} AS SELECT DISTINCT * FROM {temp_table};")
                                drop_table(cursor,temp_table)
                                print(f"The table {current_table} Create and Updated Successfully!")
                            elif(input_permision == "no"):
                                print("Exit") 
                            else:
                                print("\n Invalid Input.")

                    elif input_option == '3':
                        print("Exit.")
                            
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                                
            conn.commit()

        logging.info('Main program started')

    except psycopg2.Error as e:
        print("Error:", e)

# D:\\XML_DATA_READ\\xml_files\\New folder
# requirements_release_wise
import psycopg2
from utilities.table_update_query import sql_history_update_queries
from utilities.table_create_query import sql_history_table_create_queries
from config import get_histry_table_name

def flatten_keys(dataset):
    flattened_dataset = {}
    for key, value in dataset.items():
        if isinstance(value, dict):
            # Recursively flatten nested dictionaries
            flattened_subkeys = flatten_keys(value)
            for subkey, subvalue in flattened_subkeys.items():
                flattened_dataset[f"{key}_{subkey}"] = subvalue
        else:
            flattened_dataset[key] = value
    return flattened_dataset


def get_column_name(key):
    # Split the key by underscores and get the last three parts
    parts = key.split('_')[-4:]
    # Join the last three parts to form the column name
    return '_'.join(parts)


def create_table_and_insert_data(cursor, datasets, table_name):
    if not datasets:
        print("No datasets provided.")
        return 
    
    # Find the dict object with the highest number of keys
    max_keys_dataset = max(datasets, key=lambda x: len(x.keys()))
    
    # Get flattened column names from the dict object with the highest number of keys
    flattened_keys = flatten_keys(max_keys_dataset)
    
    # Extract column names with last three values from each key
    column_names = [get_column_name(key) for key in flattened_keys.keys()]
    
    # to catch data types
    column_types = {}
    for column in column_names:
        if column.endswith('Id'):
            column_types[column] = 'INT'
        elif column.endswith('Date'):
            column_types[column] = 'TIMESTAMP'
        else:
            column_types[column] = 'VARCHAR'
    
    # Create table based on flattened column names and types
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'"{name}" {type}' for name, type in column_types.items()])})"
    cursor.execute(create_table_query)
    
    # Insert data from all datasets
    for dataset in datasets:
        # Flatten keys for the current dataset
        flattened_dataset = flatten_keys(dataset)
        
        # Construct INSERT query with all column names
        insert_query = f"INSERT INTO {table_name} ({', '.join([f'"{column}"' for column in column_names])}) VALUES ({', '.join(['%s' for _ in column_names])})"
        
        # Replace 'NULL' with None for missing values
        values = [flattened_dataset.get(key) for key in flattened_keys.keys()]
        
        # Execute INSERT query with corresponding values
        cursor.execute(insert_query, tuple(values))
  

#######################################

# check weather table exist
def table_exists(cursor, table_name):
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    return cursor.fetchone()[0]


# execute query from dictionary
def execute_query_from_dic(cursor, queries_dict, query_key, *params):
    try:
        query = queries_dict.get(query_key)
        if query:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
        else:
            print("Error: Query key not found.")
    except psycopg2.Error as e:
        print("Error:", e)


# get row count of table
def row_count_of_table(cursor, table_name):
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        # Fetch the count
        return cursor.fetchone()[0]
    except psycopg2.Error as e:
        print("Error:", e)


# get distinct row count of table
def row_count_of_distinct_rows(cursor, table_name):
    try:
        cursor.execute(f"SELECT COUNT(*) FROM (SELECT DISTINCT * FROM {table_name}) AS distinct_rows;")
        # Fetch the count
        return cursor.fetchone()[0]
    except psycopg2.Error as e:
        print("Error:", e)


# Function to compare two tables and get the differences
def compare_tables(cursor, table1, table2, columns):
    try:
        select_query = f"SELECT {', '.join(columns)} FROM {table2} EXCEPT SELECT {', '.join(columns)} FROM {table1}"
        cursor.execute(select_query)
        differences = cursor.fetchall()
        return differences
    except psycopg2.Error as e:
        print("Error:", e)
 

 # Function to get the column names of a table


def get_table_columns(cursor, table_name):
    try:
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = [row[0] for row in cursor.fetchall()]
        return columns
    except psycopg2.Error as e:
        print("Error:", e)


# Replace current table with data from duplicate table
def replace_table(cursor, cur_table, dup_table):
    try:
        cursor.execute(f"DELETE FROM {cur_table};")
        cursor.execute(f"INSERT INTO {cur_table} SELECT * FROM {dup_table};")
        print(f"Successfully Updated the {cur_table} table!")
    except psycopg2.Error as e:
        print("Error:", e)


# Drop table
def drop_table(cursor, table_name):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    except psycopg2.Error as e:
        print(f"Error dropping tables: {e}")


# update histry table
def histry_update(cursor, table_name):
    try:
        # update the history table
        version = input("\nUpdated Version ? : ")
        if table_exists(cursor, get_histry_table_name(table_name)):
            execute_query_from_dic(cursor, sql_history_update_queries, table_name, version)
            print("Successfully moved current data to history table.")
        else:
            print("History table does not exist.")
            his_table_res = input("Do you need to create History table & update with current data? (Yes/No) : ").lower()
            if his_table_res == "yes":
                execute_query_from_dic(cursor, sql_history_table_create_queries, table_name)
                execute_query_from_dic(cursor, sql_history_update_queries, table_name, version)
                print("Successfully moved current data to history table.")
            elif his_table_res == "no":
                print("Program terminated.")
            else:
                print("Invalid input. Program terminated.")
                                
    except psycopg2.Error as e:
        print(f"Error in Update Histry: {e}")


# update current table
def current_table_update(cursor, temp_table, current_table):
    try:
        # duplicate table name
        dup_table = f"dup_{current_table}"
        # create duplicate table from current table
        cursor.execute(f"CREATE TABLE {dup_table} AS SELECT * FROM {current_table};")

        columns = get_table_columns(cursor, temp_table)

        # get differencess between temp_table and dup_table
        differences = compare_tables(cursor, dup_table, temp_table, columns)
        if differences:
            # Add difference row from tem_table to dup_table
            for row in differences:
                insert_query = f"INSERT INTO {dup_table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in columns])})"
                cursor.execute(insert_query, row)

            # print the summary of details
            print(f"\n-----------------SUMMARY-----------------")
            print(f"\nBefor update, current table row count  : {row_count_of_table(cursor, current_table)} ")
            print(f"\nAfter update, current table row count  : {row_count_of_table(cursor, dup_table)} ")
            print(f"\nTotal row count of temporary table     : {row_count_of_table(cursor, temp_table)} ")
            print(f"\nDistinct row count of temporary table  : {row_count_of_distinct_rows(cursor, temp_table)} ")

            # get user input and confirm the process
            confirm = input(f"\nDo you confirm the update (Yes/No)? ").lower()
            if(confirm == "yes"):
                # Update the current table
                replace_table(cursor, current_table, dup_table)
                drop_table(cursor,dup_table)
                drop_table(cursor, temp_table)
            elif(confirm == "no"):
                drop_table(cursor, dup_table)
                print(f"The table {current_table} not update.")
        else:
            drop_table(cursor, dup_table)
            print("Already include data in the Current Table.")
            # continue
    except psycopg2.Error as e:
        print(f"Error updating current tables: {e}")


# check the all columns exist
def ensure_columns_exist(cursor, table_name, required_columns):
    for column in required_columns:
        if column.endswith('Id'):
            column_type = 'INT'
        elif column.endswith('Date'):
            column_type = 'TIMESTAMP'
        else:
            column_type = 'VARCHAR'

        cursor.execute(f"""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                            WHERE table_name='{table_name}' AND column_name='{column}') THEN
                ALTER TABLE {table_name} ADD COLUMN "{column}" {column_type};
            END IF;
        END$$;
        """)

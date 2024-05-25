import logging

# connection string
connection_string = "dbname='A_Testing' user='postgres' host='localhost' password='4321'"

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler("access.log"),
            logging.StreamHandler()  # Also log to console
        ]
    )
    # Create a separate file handler for error messages
    error_handler = logging.FileHandler("error.log")
    error_handler.setLevel(logging.ERROR) 
    error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S') 
    error_handler.setFormatter(error_formatter)

    # Add the error handler to the root logger
    logging.getLogger('').addHandler(error_handler)

# Dictionary mappings
def get_predefined_tag_string(table_name):
    predefined_tag_string = {
        #"table_name": "tage_name"
        "incident_release_wise": "IncidentData",
        "requirements_release_wise": "RequirementData",
        "requirements_components_wise": "RequirementData",
        "test_case_release_wise": "TestCaseData",
        "test_run_release_wise": "TestRunData",
        "test_set_release_wise": "TestSetData"
    }
    # Get the Tag name using provided table_name exists in the dictionary
    if table_name in predefined_tag_string:
        return predefined_tag_string[table_name]
    else:
        return "Incorect Table Name '{}'.".format(table_name)


def get_predefined_temp_table_name(table_name):
    predefined_temp_table_name = {
        #"table_name": "temp_table"
        "incident_release_wise": "temp_incident_release_wise",
        "requirements_release_wise": "temp_requirements_release_wise",
        "requirements_components_wise": "temp_requirements_components_wise",
        "test_case_release_wise": "temp_test_case_release_wise",
        "test_run_release_wise": "temp_test_run_release_wise",
        "test_set_release_wise": "temp_test_set_release_wise"
    }
    # Get the Tag name using provided table_name exists in the dictionary
    if table_name in predefined_temp_table_name:
        return predefined_temp_table_name[table_name]
    else:
        return "Incorect Table Name '{}'.".format(table_name)
    

def get_predefined_cur_table_name(table_name):   
    predefined_table_name = {
        #"table_name": "current_table_name"
        "incident_release_wise": "incident_release_wise_updated",
        "requirements_release_wise": "requirements_release_wise_updated",
        "requirements_components_wise": "requirements_components_wise_updated",
        "test_case_release_wise": "test_case_release_wise_updated",
        "test_run_release_wise": "test_run_release_wise_updated",
        "test_set_release_wise": "test_set_release_wise_updated"
    }
    # Get the Tag name using provided table_name exists in the dictionary
    if table_name in predefined_table_name:
        return predefined_table_name[table_name]
    else:
        return "Incorect Table Name '{}'.".format(table_name)


def get_histry_table_name(table_name):
    predifine_histry_table_name = {
        #"table_name": "histry_table_name"
        "incident_release_wise": "histry_incident_release_wise",
        "requirements_release_wise": "histry_requirements_release_wise",
        "requirements_components_wise": "histry_requirements_components_wise",
        "test_case_release_wise": "histry_test_case_release_wise",
        "test_run_release_wise": "histry_test_run_release_wise",
        "test_set_release_wise": "histry_test_set_release_wise"
    }
    if table_name in predifine_histry_table_name:
        return predifine_histry_table_name[table_name]




 
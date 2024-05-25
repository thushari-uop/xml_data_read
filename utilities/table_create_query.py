sql_temp_table_create_queries = {
	'incident_release_wise': """
	                        -- SQL query for temp_incident_release_wise create
                            BEGIN;
	                        CREATE TABLE temp_incident_release_wise AS SELECT DISTINCT
                                "Report_IncidentData_Incident_IncidentId" AS incident_id,
                                "Report_IncidentData_Incident_SeverityId" AS severity_id,
                                "Report_IncidentData_Incident_DetectedReleaseId" AS detected_release_id,
                                "Report_IncidentData_Incident_PriorityId" AS priority_id,
                                "Report_IncidentData_Incident_ProjectId" AS project_id,
                                "Report_IncidentData_Incident_IncidentStatusId" AS status_id,
                                "Report_IncidentData_Incident_IncidentTypeId" AS type_id,
                                "Report_IncidentData_Incident_OpenerId" AS opener_id,
                                "Report_IncidentData_Incident_OwnerId" AS owner_id,
                                "Report_IncidentData_Incident_Name" AS incident_name,
                                "Report_IncidentData_Incident_ResolvedReleaseId" AS resolved_release_id,
                                "Report_IncidentData_Incident_Description" AS description,
                                "Report_IncidentData_Incident_VerifiedReleaseId" AS verified_release_id,
                                "Report_IncidentData_Incident_CreationDate" AS creation_date,
                                "Report_IncidentData_Incident_LastUpdateDate" AS last_update_date,
                                "Report_IncidentData_Incident_IsAttachments" AS is_attachments,
                                "Report_IncidentData_Incident_CompletionPercent" AS completion_percent,
                                "Report_IncidentData_Incident_IsDeleted" AS is_deleted,
                                "Report_IncidentData_Incident_ComponentIds" AS component_ids,
                                "Report_IncidentData_Incident_PriorityName" AS priority_name,
                                "Report_IncidentData_Incident_PriorityColor" AS priority_color,
                                "Report_IncidentData_Incident_SeverityName" AS severity_name,
                                "Report_IncidentData_Incident_SeverityColor" AS severity_color,
                                "Report_IncidentData_Incident_IncidentStatusName" AS status_name,
                                "Report_IncidentData_Incident_IncidentStatusIsOpenStatus" AS is_open_status,
                                "Report_IncidentData_Incident_IncidentTypeName" AS type_name,
                                "Report_IncidentData_Incident_OpenerName" AS opener_name,
                                "Report_IncidentData_Incident_OwnerName" AS owner_name,
                                "Report_IncidentData_Incident_DetectedReleaseVersionNumber" AS detected_release_version_number,
                                "Report_IncidentData_Incident_ResolvedReleaseVersionNumber" AS resolved_release_version_number,
                                "Report_IncidentData_Incident_VerifiedReleaseVersionNumber" AS verified_release_version_number,
                                "Report_IncidentData_Incident_ProjectIsActive" AS project_is_active,
                                "Report_IncidentData_Incident_ProjectGroupId" AS project_group_id,
                                "Report_IncidentData_Incident_IncidentTypeIsIssue" AS incident_type_is_issue,
                                "Report_IncidentData_Incident_IncidentTypeIsRisk" AS incident_type_is_risk,
                                "Report_IncidentData_Incident_ProjectName" AS project_name,
                                "IncidentData_Incident_Custom_02" AS custom_02,
                                "IncidentData_Incident_Custom_04" AS custom_04,
                                "IncidentData_Incident_Custom_08" AS custom_08,
                                "IncidentData_Incident_Custom_11" AS custom_11,
                                "IncidentData_Incident_Custom_12" AS custom_12,
                                "IncidentData_Incident_Custom_13" AS custom_13,
                                "IncidentData_Incident_Custom_14" AS custom_14,
                                "IncidentData_Incident_Custom_15" AS custom_15,
                                "IncidentData_Incident_Custom_16" AS custom_16,
                                "Report_IncidentData_Incident_ConcurrencyDate" AS concurrency_date,
                                "Report_IncidentData_Incident_ArtifactPrefix" AS artifact_prefix,
                                "Report_IncidentData_Incident_ArtifactType" AS artifact_type,
                                "Report_IncidentData_Incident_ArtifactToken" AS artifact_token,
                                "Report_IncidentData_Incident_ArtifactId" AS incident_artifact_id,
                                "Report_IncidentData_Incident_Properties" AS properties,
                                "Report_IncidentData_Incident_ComponentNames" AS component_names,
                                "Incident_CustomProperties_CustomProperty_Alias" AS custom_property_alias,
                                "Incident_CustomProperties_CustomProperty_Name" AS custom_property_name,
                                "Incident_CustomProperties_CustomProperty_Type" AS custom_property_type,
                                "Incident_IncidentResolutions_IncidentResolution_IncidentResolut" AS incident_resolution_resolut,
                                "Incident_IncidentResolutions_IncidentResolution_IncidentId" AS incident_resolution_id,
                                "Incident_IncidentResolutions_IncidentResolution_CreatorId" AS incident_resolution_creator_id,
                                "Incident_IncidentResolutions_IncidentResolution_Resolution" AS incident_resolution_resolution,
                                "Incident_IncidentResolutions_IncidentResolution_CreationDate" AS incident_resolution_creation_date,
                                "Incident_IncidentResolutions_IncidentResolution_Incident" AS incident_resolution_incident,
                                "Incident_IncidentResolutions_IncidentResolution_Creator" AS incident_resolution_creator,
                                "Incident_IncidentResolutions_IncidentResolution_CreatorName" AS incident_resolution_creator_name,
                                "Incident_IncidentResolutions_IncidentResolution_Properties" AS incident_resolution_properties,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactLinkId" AS artifact_link_id,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactId" AS artifact_id,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactTypeId" AS artifact_type_id,
                                "Incident_ArtifactLinks_ArtifactLink_CreatorId" AS artifact_creator_id,
                                "Incident_ArtifactLinks_ArtifactLink_CreationDate" AS artifact_creation_date,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactName" AS artifact_name,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactTypeName" AS artifact_type_name,
                                "Incident_ArtifactLinks_ArtifactLink_CreatorName" AS artifact_creator_name,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactLinkTypeId" AS artifact_link_type_id,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactLinkTypeName" AS artifact_link_type_name,
                                "Incident_ArtifactLinks_ArtifactLink_ArtifactStatusName" AS artifact_status_name,
                                "Incident_ArtifactLinks_ArtifactLink_ProjectId" AS artifact_project_id,
                                "Incident_ArtifactLinks_ArtifactLink_Properties" AS artifact_properties
                            FROM incident_release_wise;
                            DROP TABLE incident_release_wise;
                            COMMIT;
	                        """,
                               
    'requirements_release_wise': """
                            -- SQL query for temp_requirements_release_wise create
                            BEGIN;
                            CREATE TABLE temp_requirements_release_wise AS SELECT DISTINCT
                                "Report_RequirementData_Requirement_RequirementId" AS requirement_id,
                                "Report_RequirementData_Requirement_AuthorId" AS author_id,
                                "Report_RequirementData_Requirement_ReleaseId" AS release_id,
                                "Report_RequirementData_Requirement_ProjectId" AS project_id,
                                "Report_RequirementData_Requirement_RequirementTypeId" AS requirement_type_id,
                                "Report_RequirementData_Requirement_RequirementStatusId" AS requirement_status_id,
                                "Report_RequirementData_Requirement_ComponentId" AS component_id,
                                "Report_RequirementData_Requirement_ImportanceId" AS importance_id,
                                "Report_RequirementData_Requirement_Name" AS requirement_name,
                                "Report_RequirementData_Requirement_CreationDate" AS creation_date,
                                "Report_RequirementData_Requirement_IndentLevel" AS indent_level,
                                "Report_RequirementData_Requirement_Description" AS description,
                                "Report_RequirementData_Requirement_LastUpdateDate" AS last_update_date,
                                "Report_RequirementData_Requirement_IsSummary" AS is_summary,
                                "Report_RequirementData_Requirement_IsAttachments" AS is_attachments,
                                "Report_RequirementData_Requirement_CoverageCountTotal" AS coverage_count_total,
                                "Report_RequirementData_Requirement_CoverageCountPassed" AS coverage_count_passed,
                                "Report_RequirementData_Requirement_CoverageCountFailed" AS coverage_count_failed,
                                "Report_RequirementData_Requirement_CoverageCountCaution" AS coverage_count_caution,
                                "Report_RequirementData_Requirement_CoverageCountBlocked" AS coverage_count_blocked,
                                "Report_RequirementData_Requirement_TaskCount"  AS task_count,
                                "Report_RequirementData_Requirement_TaskPercentOnTime" AS task_percent_on_time,
                                "Report_RequirementData_Requirement_TaskPercentLateFinish" AS task_percent_late_finish,
                                "Report_RequirementData_Requirement_TaskPercentNotStart" AS task_percent_not_start,
                                "Report_RequirementData_Requirement_TaskPercentLateStart" AS task_percent_late_start,
                                "Report_RequirementData_Requirement_IsDeleted" AS is_deleted,
                                "Report_RequirementData_Requirement_ConcurrencyDate" AS concurrency_date,
                                "Report_RequirementData_Requirement_RequirementStatusName" AS requirement_status_name,
                                "Report_RequirementData_Requirement_RequirementTypeName" AS requirement_type_name,
                                "Report_RequirementData_Requirement_ComponentName" AS component_name,
                                "Report_RequirementData_Requirement_AuthorName" AS author_name,
                                "Report_RequirementData_Requirement_ImportanceName" AS importance_name,
                                "Report_RequirementData_Requirement_ReleaseVersionNumber" AS release_version_number,
                                "Report_RequirementData_Requirement_IsExpanded" AS is_expanded,
                                "Report_RequirementData_Requirement_IsVisible" AS is_visible,
                                "Report_RequirementData_Requirement_ProjectName" AS project_name,
                                "Report_RequirementData_Requirement_ProjectIsActive" AS project_is_active,
                                "Report_RequirementData_Requirement_Rank" AS requirement_rank,
                                "Report_RequirementData_Requirement_RequirementTypeIsSteps" AS requirement_type_is_steps,
                                "Report_RequirementData_Requirement_ImportanceColor" AS importance_color,
                                "Report_RequirementData_Requirement_ImportanceScore" AS importance_score,
                                "Report_RequirementData_Requirement_ArtifactPrefix" AS artifact_prefix,
                                "Report_RequirementData_Requirement_ArtifactType" AS artifact_type,
                                "Report_RequirementData_Requirement_ArtifactToken" AS artifact_token,
                                "Report_RequirementData_Requirement_ArtifactId" AS artifact_id,
                                "Report_RequirementData_Requirement_ParentIndentLevel" AS parent_indent_level,
                                "Report_RequirementData_Requirement_Properties" AS properties
                            FROM requirements_release_wise;
                            DROP TABLE requirements_release_wise;
                            COMMIT;
                            """,  

    'requirements_components_wise': """
                            -- SQL query for temp_requirements_components_wise create
                            BEGIN; 
                            CREATE TABLE temp_requirements_components_wise AS SELECT DISTINCT
                                "Report_RequirementData_Requirement_RequirementId" AS requirement_id,
                                "Report_RequirementData_Requirement_Name" AS requirement_name,
                                "Report_RequirementData_Requirement_AuthorId" AS author_id,
                                "Report_RequirementData_Requirement_ReleaseId" AS release_id,
                                "Report_RequirementData_Requirement_ProjectId" AS project_id,
                                "Report_RequirementData_Requirement_RequirementTypeId" AS requirement_type_id,
                                "Report_RequirementData_Requirement_RequirementStatusId" AS requirement_status_id,
                                "Report_RequirementData_Requirement_ComponentId" AS component_id,
                                "Report_RequirementData_Requirement_ImportanceId" AS importance_id,
                                "Report_RequirementData_Requirement_CreationDate" AS creation_date,
                                "Report_RequirementData_Requirement_IndentLevel" AS indent_level,
                                "Report_RequirementData_Requirement_Description" AS description,
                                "Report_RequirementData_Requirement_LastUpdateDate" AS last_update_date,
                                "Report_RequirementData_Requirement_IsSummary" AS is_summary,
                                "Report_RequirementData_Requirement_IsAttachments" AS is_attachments,
                                "Report_RequirementData_Requirement_CoverageCountTotal" AS coverage_count_total,
                                "Report_RequirementData_Requirement_CoverageCountPassed" AS coverage_count_passed,
                                "Report_RequirementData_Requirement_CoverageCountFailed" AS coverage_count_failed,
                                "Report_RequirementData_Requirement_CoverageCountCaution" AS coverage_count_caution,
                                "Report_RequirementData_Requirement_CoverageCountBlocked" AS coverage_count_blocked,
                                "Report_RequirementData_Requirement_TaskCount" AS task_count,
                                "Report_RequirementData_Requirement_TaskPercentOnTime" AS task_percent_on_time,
                                "Report_RequirementData_Requirement_TaskPercentLateFinish" AS task_percent_late_finish,
                                "Report_RequirementData_Requirement_TaskPercentNotStart" AS task_percent_not_start,
                                "Report_RequirementData_Requirement_TaskPercentLateStart" AS task_percent_late_start,
                                "Report_RequirementData_Requirement_IsDeleted" AS is_deleted,
                                "Report_RequirementData_Requirement_ConcurrencyDate" AS concurrency_date,
                                "Report_RequirementData_Requirement_RequirementStatusName" AS requirement_status_name,
                                "Report_RequirementData_Requirement_RequirementTypeName" AS requirement_type_name,
                                "Report_RequirementData_Requirement_ComponentName" AS component_name,
                                "Report_RequirementData_Requirement_AuthorName" AS author_name,
                                "Report_RequirementData_Requirement_ImportanceName" AS importance_name,
                                "Report_RequirementData_Requirement_ReleaseVersionNumber" AS release_version_number,
                                "Report_RequirementData_Requirement_IsExpanded" AS is_expanded,
                                "Report_RequirementData_Requirement_IsVisible" AS is_visible,
                                "Report_RequirementData_Requirement_ProjectName" AS project_name,
                                "Report_RequirementData_Requirement_ProjectIsActive" AS project_is_active,
                                "Report_RequirementData_Requirement_Rank" AS requirement_rank,
                                "Report_RequirementData_Requirement_RequirementTypeIsSteps" AS requirement_type_is_steps,
                                "Report_RequirementData_Requirement_ImportanceColor" AS importance_color,
                                "Report_RequirementData_Requirement_ImportanceScore" AS importance_score,
                                "Report_RequirementData_Requirement_ArtifactPrefix" AS artifact_prefix,
                                "Report_RequirementData_Requirement_ArtifactType" AS artifact_type,
                                "Report_RequirementData_Requirement_ArtifactToken" AS artifact_token,
                                "Report_RequirementData_Requirement_ArtifactId" AS artifact_id,
                                "Report_RequirementData_Requirement_ParentIndentLevel" AS parent_indent_level,
                                "Report_RequirementData_Requirement_Properties" AS properties,
                                "Requirement_TestCases_TestCase_TestCaseId" AS test_case_id
                            FROM requirements_components_wise;
                            DROP TABLE requirements_components_wise;
                            COMMIT;
                            """,

    'test_case_release_wise': """
                            -- SQL query for temp_test_case_release_wise create 
                            BEGIN; 
                            CREATE TABLE temp_table AS SELECT
                                "Report_TestCaseData_TestCaseFolder_TestCaseFolderId" AS test_case_folder_Id,
                                "Report_TestCaseData_TestCaseFolder_ParentTestCaseFolderId" AS parent_test_case_folder_Id,
                                "Report_TestCaseData_TestCaseFolder_ProjectId" AS test_case_folder_project_id,
                                "Report_TestCaseData_TestCaseFolder_Name" AS test_case_folder_name,
                                "Report_TestCaseData_TestCaseFolder_Description" AS test_case_folder_description,
                                "Report_TestCaseData_TestCaseFolder_ExecutionDate" AS test_case_folder_execution_date,
                                "Report_TestCaseData_TestCaseFolder_LastUpdateDate" AS test_case_folder_last_update_date,
                                "Report_TestCaseData_TestCaseFolder_EstimatedDuration" AS test_case_folder_estimated_duration,
                                "Report_TestCaseData_TestCaseFolder_ActualDuration" AS test_case_folder_actual_duration,
                                "Report_TestCaseData_TestCaseFolder_CountPassed" AS test_case_folder_count_passed,
                                "Report_TestCaseData_TestCaseFolder_CountFailed" AS test_case_folder_count_failed,
                                "Report_TestCaseData_TestCaseFolder_CountBlocked" AS test_case_folder_count_blocked,
                                "Report_TestCaseData_TestCaseFolder_CountCaution" AS test_case_folder_count_caution,
                                "Report_TestCaseData_TestCaseFolder_CountNotRun" AS test_case_folder_count_not_run,
                                "Report_TestCaseData_TestCaseFolder_CountNotApplicable" AS test_case_folder_count_not_applicable,
                                "Report_TestCaseData_TestCaseFolder_ArtifactPrefix" AS test_case_folder_artifact_prefix,
                                "Report_TestCaseData_TestCaseFolder_ArtifactType" AS test_case_folder_artifact_type,
                                "Report_TestCaseData_TestCaseFolder_ArtifactToken" AS test_case_folder_artifact_token,
                                "Report_TestCaseData_TestCaseFolder_ArtifactId" AS test_case_folder_artifact_id,
                                "Report_TestCaseData_TestCaseFolder_ExecutionStatusId" AS test_case_folder_execution_status_id,
                                "Report_TestCaseData_TestCaseFolder_TestCaseCount" AS test_case_folder_test_case_count,
                                "Report_TestCaseData_TestCaseFolder_Properties" AS test_case_folder_properties,
                                "Report_TestCaseData_TestCaseFolder_IndentLevel" AS test_case_folder_indent_level,
                                "TestCaseFolder_TestCases_TestCase_TestCaseId" AS test_case_id,
                                "TestCaseFolder_TestCases_TestCase_TestCasePriorityId" AS test_case_priority_id,
                                "TestCaseFolder_TestCases_TestCase_ProjectId" AS test_case_project_id,
                                "TestCaseFolder_TestCases_TestCase_AuthorId" AS test_case_author_id,
                                "TestCaseFolder_TestCases_TestCase_TestCaseStatusId" AS test_case_status_id,
                                "TestCaseFolder_TestCases_TestCase_TestCaseTypeId" AS test_case_type_id,
                                "TestCaseFolder_TestCases_TestCase_TestCaseFolderId" AS test_case_test_case_folder_id,
                                "TestCaseFolder_TestCases_TestCase_Name" AS test_case_name,
                                "TestCaseFolder_TestCases_TestCase_OwnerId" AS test_case_owner_id,
                                "TestCaseFolder_TestCases_TestCase_Description" AS test_case_description,
                                "TestCaseFolder_TestCases_TestCase_CreationDate" AS test_case_creation_date,
                                "TestCaseFolder_TestCases_TestCase_LastUpdateDate" AS test_case_last_update_date,
                                "TestCaseFolder_TestCases_TestCase_IsAttachments" AS test_case_is_attachments,
                                "TestCaseFolder_TestCases_TestCase_IsTestSteps" AS test_case_is_test_steps,
                                "TestCaseFolder_TestCases_TestCase_IsDeleted" AS test_case_is_deleted,
                                "TestCaseFolder_TestCases_TestCase_ConcurrencyDate" AS test_case_concurrency_date,
                                "TestCaseFolder_TestCases_TestCase_ComponentIds" AS test_case_component_ids,
                                "TestCaseFolder_TestCases_TestCase_ExecutionStatusId" AS test_case_execution_status_id,
                                "TestCaseFolder_TestCases_TestCase_ExecutionDate" AS test_case_execution_date,
                                "TestCaseFolder_TestCases_TestCase_ActualDuration" AS test_case_actual_duration,
                                "TestCaseFolder_TestCases_TestCase_ReleaseId" AS test_case_release_id,
                                "TestCaseFolder_TestCases_TestCase_ExecutionStatusName" AS test_case_execution_status_name,
                                "TestCaseFolder_TestCases_TestCase_TestCasePriorityName" AS test_case_priority_name,
                                "TestCaseFolder_TestCases_TestCase_AuthorName" AS test_case_author_name,
                                "TestCaseFolder_TestCases_TestCase_OwnerName" AS test_case_owner_name,
                                "TestCaseFolder_TestCases_TestCase_TestCaseStatusName" AS test_case_status_name,
                                "TestCaseFolder_TestCases_TestCase_TestCaseTypeName" AS test_case_type_name,
                                "TestCaseFolder_TestCases_TestCase_TestCasePriorityColor" AS test_case_priority_color,
                                "TestCaseFolder_TestCases_TestCase_ArtifactPrefix" AS test_case_artifact_prefix,
                                "TestCaseFolder_TestCases_TestCase_ArtifactType" AS test_case_artifact_type,
                                "TestCaseFolder_TestCases_TestCase_ArtifactToken" AS test_case_artifact_token,
                                "TestCaseFolder_TestCases_TestCase_ArtifactId" AS test_case_artifact_id,
                                "TestCaseFolder_TestCases_TestCase_IsActive" AS test_case_is_active,
                                "TestCaseFolder_TestCases_TestCase_Properties" AS test_case_properties,
                                "TestCaseFolder_TestCases_TestCase_ComponentNames" AS test_case_component_names,
                                "TestCase_Requirements_Requirement_RequirementId" AS requirement_id
                            FROM test_case_release_wise;
                            CREATE TABLE temp_test_case_release_wise AS SELECT DISTINCT * FROM temp_table WHERE requirement_id IS NOT NULL;
                            DROP TABLE test_case_release_wise, temp_table;
                            COMMIT;
                            """, 
                                                
	'test_run_release_wise': """
                            -- SQL query for temp_test_run_release_wise create 
                            BEGIN; 
                            CREATE TABLE temp_table AS SELECT
                                "Report_TestRunData_TestRun_TestRunId" AS test_run_id,
                                "Report_TestRunData_TestRun_TestCaseId" AS test_case_id,
                                "Report_TestRunData_TestRun_TestRunTypeId" AS test_run_type_id,
                                "Report_TestRunData_TestRun_ReleaseId" AS release_id,
                                "Report_TestRunData_TestRun_TestSetId" AS test_set_id,
                                "Report_TestRunData_TestRun_TestSetTestCaseId" AS test_set_test_case_id,
                                "Report_TestRunData_TestRun_TesterId" AS tester_id,
                                "Report_TestRunData_TestRun_TestRunsPendingId" AS test_runs_pending_id,
                                "Report_TestRunData_TestRun_ExecutionStatusId" AS execution_status_id,
                                "Report_TestRunData_TestRun_StartDate" AS start_date,
                                "Report_TestRunData_TestRun_Name" AS test_run_name,
                                "Report_TestRunData_TestRun_Description" AS description,
                                "Report_TestRunData_TestRun_EndDate" AS end_date,
                                "Report_TestRunData_TestRun_ActualDuration" AS actual_duration,
                                "Report_TestRunData_TestRun_IsAttachments" AS is_attachments,
                                "Report_TestRunData_TestRun_IsDeleted" AS is_deleted,
                                "Report_TestRunData_TestRun_ConcurrencyDate" AS concurrency_date,
                                "Report_TestRunData_TestRun_ExecutionStatusName" AS execution_status_name,
                                "Report_TestRunData_TestRun_TesterName" AS tester_name,
                                "Report_TestRunData_TestRun_ReleaseName" AS release_name,
                                "Report_TestRunData_TestRun_ReleaseVersionNumber" AS release_version_number,
                                "Report_TestRunData_TestRun_TestSetName" AS test_set_name,
                                "Report_TestRunData_TestRun_TestRunTypeName" AS test_run_type_name,
                                "Report_TestRunData_TestRun_ProjectId" AS project_id,
                                "Report_TestRunData_TestRun_ChangeSetId" AS change_set_id,
                                "Report_TestRunData_TestRun_ArtifactPrefix" AS artifact_prefix,
                                "Report_TestRunData_TestRun_ArtifactType" AS artifact_type,
                                "Report_TestRunData_TestRun_ArtifactToken" AS artifact_token,
                                "Report_TestRunData_TestRun_ArtifactId" AS artifact_id,
                                "Report_TestRunData_TestRun_Properties" AS properties
                            FROM test_run_release_wise;
                            CREATE TABLE temp_test_run_release_wise AS SELECT DISTINCT * FROM temp_table WHERE test_case_id IS NOT NULL;
                            DROP TABLE test_run_release_wise, temp_table;
                            COMMIT;
                            """,

    # 'test_set_release_wise': """
    #                         -- SQL query for test_set_release_wise_updated 
                             
    #                          """,
	
}


sql_history_table_create_queries = {
    'incident_release_wise': """
                                CREATE TABLE histry_incident_release_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM incident_release_wise_updated 
                                WITH NO DATA;
                                """,
    'requirements_release_wise': """
                                CREATE TABLE histry_requirements_release_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM requirements_release_wise_updated 
                                WITH NO DATA;
                                """,
    'requirements_components_wise': """
                                CREATE TABLE histry_requirements_components_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM requirements_components_wise_updated 
                                WITH NO DATA;
                                """,
    'test_case_release_wise': """
                                CREATE TABLE histry_test_case_release_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM test_case_release_wise_updated 
                                WITH NO DATA;
                                """,
    'test_run_release_wise': """
                                CREATE TABLE histry_test_run_release_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM test_run_release_wise_updated 
                                WITH NO DATA;
                                """,
    'test_set_release_wise': """
                                CREATE TABLE histry_test_set_release_wise AS 
                                SELECT *, NULL::VARCHAR AS updated_version, NULL::TIMESTAMP AS updated_date_time 
                                FROM test_set_release_wise_updated 
                                WITH NO DATA;
                                """
}
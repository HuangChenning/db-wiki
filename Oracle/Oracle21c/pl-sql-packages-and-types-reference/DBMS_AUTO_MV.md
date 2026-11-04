---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AUTO_MV.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 33 DBMS\_AUTO\_MV

`DBMS_AUTO_MV` contains subprograms for configuring automatic materialized views.

This chapter contains the following topics:

- Using DBMS\_AUTO\_MV
- Summary of DBMS\_AUTO\_MV Subprograms

### 33.1 Using DBMS\_AUTO\_MV

The `DBMS_AUTO_MV` package contains functions and procedures to manage automatic materialized views.

This package is owned by `SYS`, so `EXECUTE` package privilege is required by non- `SYS` users. Grant `EXECUTE` privilege on the package to the users.

### 33.2 Summary of DBMS\_AUTO\_MV Subprograms

This table lists the `DBMS_AUTO_MV` package subprograms and briefly describes them.

Table 33-1 DBMS\_AUTO\_MV Package Subprograms

| Subprogram | Description |
| --- | --- |
| `CONFIGURE Procedure` | Enables, disables, and configures the various parameters of the automatic materialized view feature. |
| `DROP_AUTO_MVS Procedure` | Drops automatic materialized views that were created. This routine can only be executed by DBA. |
| `RECOMMEND Function` | This function allows a user to manually generate automatic materialized view recommendations for SQL statements in a given SQL tuning set |
| `REFRESH Procedure` | This procedure allows a user to manually refresh all stale automatic materialized views in the system unconditionally. |
| `REPORT_ACTIVITY Function` | This function generates a report on the automatic materialized view activities and usage for a specified time duration. The report can be generated in text, HTML, or XML formats as specified by the argument type. |
| `REPORT_LAST_ACTIVITY Function` | This function generates a report on the most recent automatic materialized view activities and usage. The report can be generated in text, HTML, or XML formats as specified by the argument type. |

#### 33.2.1 CONFIGURE Procedure

This procedure enables, disables, and configures the various parameters of the automatic materialized view feature.

Syntax

```
DBMS_AUTO_MV.CONFIGURE (
   parameter   IN VARCHAR2,
   value      IN VARCHAR2,
   allow      IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 33-2 CONFIGURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `parameter` | The name of the parameter to be modified. Parameter names are not case sensitive. |
| `value` | The value of the specified parameter. |
| `allow` | This parameter allows or disallows various schemas or app modules. It is applicable only for the `AUTO_MV_SCHEMA` and `AUTO_MV_APP_MODULE` parameters. |

Parameters

Table 33-3 CONFIGURE Parameters Names

| Parameter | Description |
| --- | --- |
| `AUTO_MV_MODE` | Enables, disables, or engages report-only mode.  Possible values are:  - `OFF`: No recommendations are made. This is the default value. - `REPORT ONLY`: This mode generates recommendations and stores them in the internal repository so they are available to the DBA through `DBA_AUTO_MV_ANALYSIS_RECOMMENDATIONS`. - `IMPLEMENT`: This mode generates, verifies, and publishes recommendations, or drops them. |
| `AUTO_MV_MAINT_TASK` | Activates and deactivated automatic maintenance of materialized views.  - `ENABLE`: Activates automatic maintenance of materialized views. - `DISABLE`: Deactivates the automatic maintenance of materialized views. If automatic maintenance of materialized views is in progress, it finishes the maintenance. This is the default value. - `CLEANUP_AND_DISABLE`: Drops all automatic materialized views, and deactivates automatic maintenance of materialized views. If automatic materialized views maintenance is in progress, it finishes the maintenance before the task is deactivated. |
| `AUTO_MV_SPACE_BUDGET` | Specifies the amount of space budget available for implementing automatic materialized views. The total space value is the sum of currently space used by all user tables (i.e. not system tables). The calculation does not include user access structures (like indexes or materialized views). Possible values are:  - `Budget in percent`: A positive number ending with `%` symbol designating the percentage of currently utilized space for all user tables. - `Budget in GB`: A positive integer ending with GB that indicates the absolute space limit for automatic materialized views. For example, 10GB indicates 10 Gigabytes. The minimum value is 1GB but no maximum value.  The default budget is `10%` of the total size of user tables. |
| `AUTO_MV_DEFAULT_TABLESPACE` | Specifies the tablespace to place automatic materialized views. Possible values are:  - `Tablespace name`: A valid Oracle tablespace name to be used when creating new automatic materialized views. Quoted identifiers are supported. - `NULL`: A new automatic materialized view is created in the default tablespace of the owner of parent object. If automatic materialized view has more than one parent object, such as materialized views defined on multiple base tables, the default tablespace of the owner of largest base table is selected. This is the default value.  If the value is changed dynamically, it takes effect the next time automatic materialized views recommendations are implemented. |
| `AUTO_MV_TEMP_TABLESPACE` | Specifies the temporary tablespace while creating or refreshing automatic materialized views. Possible values are:  - `Tablespace name`: A valid Oracle temp tablespace name to be used when creating new automatic materialized views and the data needs to be spilled to temp. - `NULL`: The temp table space assigned to the owner of the largest parent object of the automatic materialized views. This is the default value.  If the value is changed dynamically, it takes effect the next time recommendations are implemented. |
| `AUTO_MV_RETENTION` | Specifies the number of days automatic materialized views exists without being utilized by a query. When the expiry period is reached, the materialized view is dropped.  `Positive integer`: An integer between `1` and `373`. The default value is `33` days. |
| `AUTO_MV_ANALYZE_REPORT_RETENTION` | Specifies the maximum number of days to retain analysis and recommendation history.  `Positive integer`: An integer value between `0` and `90`. Value `0` implies that history is not maintained. The default value is `31`.  The history of analysis and verification is retained in the `DBA_AUTO_MV_*` dictionary tables. |
| `AUTO_MV_ANALYZE_WORKLOAD_WINDOW` | Specifies the maximum number of hours to make recommendations.  `Positive integer`: An integer value between `1` and `8760`. The default value is `24`. |
| `AUTO_MV_ANALYZE_WORKLOAD_MIN_TIME` | Specifies the minimum time in seconds for a query to be considered for automatic materialized views recommendation. Queries below this threshold are not considered for recommendations.  `Positive value`: An integer value between `0` and `3600` (1 hour). The default value is `120` (2 minutes). |
| `AUTO_MV_SCHEMA` | Specifies the schemas to include or exclude from creation of automatic materialized views.  Possible values are:  - `TRUE`: Adds the specified schema to the inclusion list. - `FALSE`: Adds the specified schema to the exclusion list. - `NULL`: Removes the specified schema from the list to which it is currently added.  If both the lists (the inclusion list and the exclusion list) contain at least one schema, then all the schemas can use automatic materialized views, except the schemas listed in the exclusion list. |
| `AUTO_MV_APP_MODULE` | Specifies application modules to include or exclude from creation of automatic materialized views. Possible values are:  - `TRUE`: Adds the specified application module to the inclusion list. - `FALSE`: Adds the specified application module to the exclusion list. - `NULL`: Removes the specified application module from the list to which it is currently added.  Initially, the inclusion list and the exclusion list are empty and we can create automatic materialized views under all application modules when automatic automatic materialized views are enabled for a database. |
| `AUTO_MV_VERIFY_REPORT_RETENTION` | Specifies the maximum number of days to retain the verification history.  `Positive value`: An integer value between `0` and `90` for the number of days the history of analysis and verification is retained in the `DBA_AUTO_MV_*` dictionary tables. Value `0` implies that history is not maintained. The default value is `31`. |
| `AUTO_MV_MAINT_REPORT_RETENTION` | Specifies the maximum number of days to retain history of automatic materialized view maintenance.  `Positive integer`: An integer value between `0` and `90` for the number of days the history of automatic materialized view refreshes is retained in the `DBA_AUTO_MV_REFRESH_*` dictionary tables. Value 0 means no history is maintained. The default value is `31`. |

Example

```
begin
   dbms_auto_mv.configure ('AUTO_MV_SPACE_BUDGET',  '50%');
end;
begin
   dbms_auto_mv.configure ('AUTO_MV_SCHEMA',  'SH', FALSE);
   dbms_auto_mv.configure ('AUTO_MV_SCHEMA',  'SCOTT');
end;
/
```

#### 33.2.2 DROP\_AUTO\_MVS Procedure

This procedure drops automatic materialized views that were created. This routine can only be executed by DBA.

Syntax

```
DBMS_AUTO_MV.DROP_AUTO_MVS (
   owner            IN VARCHAR2,
   mv_name          IN VARCHAR2,
   allow_recreate   IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 33-4 DROP\_AUTO\_MVS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `OWNER` | Specifies the name of the owner of the automatic materialized views.  If `OWNER` is explicity specified and `MV_NAME` is set to null, all automatic materialized views which the user has privileges are dropped.  If `OWNER` is explicity specified and `MV_NAME` is set to null, all automatic materialized views with the given `OWNER` are dropped.  Dropped automatic materialized views are not recreated automatically by the system as default. |
| `MV_NAME` | The name of the automatic materialized views. |
| `ALLOW_RECREATE` | Enables or disables the automatic creation of dropped automatic materialized views.  `FALSE` disables the automatic creation of dropped automatic materialized views. This is default.  `TRUE` enables the automatic creation of dropped automatic materialized views. |

Examples

```
begin
   dbms_auto_mv.DROP_AUTO_MVS ('SH');
end;
/

begin
   dbms_auto_mv.DROP_AUTO_MVS ('SH', 'AUTO_MV$$_G2MKPB9SA1FB7');
end;
/
```

#### 33.2.3 RECOMMEND Function

This function allows a user to manually generate automatic materialized view recommendations for SQL statements in a given SQL tuning set

Syntax

```
DBMS_AUTO_MV.RECOMMEND (
   sts_owner             IN  VARCHAR2  DEFAULT 'SYS',
   sts_name              IN  VARCHAR2  DEFAULT 'SYS_AUTO_STS',
   workload_start_time   IN  TIMESTAMP DEFAULT NULL,
   workload_end_time     IN  TIMESTAMP DEFAULT NULL,
   automv_mode           IN  VARCHAR2  DEFAULT 'REPORT ONLY')
RETURN VARCHAR2;
```

Parameters

Table 33-5 RECOMMEND Function Parameters

| Parameter | Description |
| --- | --- |
| `sts_owner` | The name of the owner of the SQL tuning set. The default value is `SYS`. |
| `sts_name` | The name of the SQL tuning set. The default value is `SYS_AUTO_STS`. |
| `workload_start_time` | The start time of the workload window.  The value `NULL` means that the default is chosen. The default is `SYSDATE` minus the number of hours defined by `AUTO_MV_ANALYZE_WORKLOAD_WINDOW`. |
| `workload_end_time` | The end time of the workload window. |
| `automv_mode` | When `AUTOMV_MODE` is set to `REPORT                     ONLY`, which is the default mode, the function will only output the recommendations. If this parameter is set to `IMPLEMENT`, then the recommended automatic materialized views will be verified and implemented. |

Return Value

The execution name (`execution_name`) to be used in `DBA_AUTO_MV%` catalog views.

Examples

In the following examples, the default SQL tuning set, `SYS_AUTO_STS` is used. Make sure that `SYS_AUTO_STS` contains the required workload to generate the automatic materialized views.

Example 1: Generate and report recommendations using `SYS_AUTO_STS` for the past 24 hours. Note that the default behavior of this function is `REPORT ONLY`, so no automatic materialized view will be implemented.

```
var exec_name varchar2(200);
begin
    :exec_name := dbms_auto_mv.recommend();
end;
/

SELECT * FROM DBA_AUTO_MV_ANALYSIS_RECOMMENDATIONS 
        WHERE exec_name = :exec_name;
```

Example 2: Generate and publish recommendations using `SYS_AUTO_STS` for the past 24 hours.

```
var exec_name varchar2(200);
begin
    :exec_name := dbms_auto_mv.recommend(automv_mode=>'IMPLEMENT');
end;
/
```

#### 33.2.4 REFRESH Procedure

This procedure allows a user to manually refresh all stale automatic materialized views in the system unconditionally.

Syntax

```
DBMS_AUTO_MV.REFRESH ();
```

Example

```
begin
    dbms_auto_mv.refresh();
end;
/
```

#### 33.2.5 REPORT\_ACTIVITY Function

This function generates a report on the automatic materialized view activities and usage for a specified time duration. The report can be generated in text, HTML, or XML formats as specified by the argument type.

Syntax

```
DBMS_AUTO_MV.REPORT_ACTIVITY (
   activity_start        IN  TIMESTAMP WITH TIME ZONE DEFAULT SYSTIMESTAMP -1,
   activity_end          IN  TIMESTAMP WITH TIME ZONE DEFAULT SYSTIMESTAMP,
   type                  IN  VARCHAR2  DEFAULT 'TEXT',
   section               IN  VARCHAR2  DEFAULT 'ALL',
   level                 IN  VARCHAR2  DEFAULT 'TYPICAL')
RETURN CLOB;
```

Parameters

Table 33-6 REPORT\_ACTIVITY Function Parameters

| Parameter | Description |
| --- | --- |
| `activity_start` | The start time for report generation. |
| `activity_end` | The end time for report generation. |
| `type` | The format type in which the report needs to be generated. The possible values are: - TEXT - HTML - XML  The default value is `TEXT`. |
| `section` | The section can be a combination of the following: - `SUMMARY` - `MV_DETAILS` - `QUERY_DETAILS` - `VERIFICATION_DETAILS` - `ALL`  The default value is `ALL`.  You can generate a specific combination of report by using `+` or `-` operators. For example, when section is specified as `SUMMARY+MV_DETAILS`, the generated report will contain only the summary and the details about the automatic materialized view. |
| `level` | The level can be either `BASIC`, `TYPICAL`, or `ALL`. When the level is set to `BASIC`, a minimum set of information regarding the most recent automatic materialized view activity is reported. On the other hand, when the level is set to `ALL`, a detailed report is generated.  The default value is `TYPICAL`. |

Return Value

This functions returns the report as a `CLOB`.

Examples

Example 1: The following call to `REPORT_ACTIVITY()` generates an HTML output for all the automatic materialized view activities:

```
select dbms_auto_mv.report_activity(type => 'HTML') from dual;
```

#### 33.2.6 REPORT\_LAST\_ACTIVITY Function

This function generates a report on the most recent automatic materialized view activities and usage. The report can be generated in text, HTML, or XML formats as specified by the argument type.

Syntax

```
DBMS_AUTO_MV.REPORT_LAST_ACTIVITY (
   type                  IN  VARCHAR2  DEFAULT 'TEXT',
   section               IN  VARCHAR2  DEFAULT 'ALL',
   level                 IN  VARCHAR2  DEFAULT 'TYPICAL')
RETURN CLOB;
```

Parameters

Table 33-7 REPORT\_LAST\_ACTIVITY Function Parameters

| Parameter | Description |
| --- | --- |
| `type` | The format type in which the report needs to be generated. The possible values are: - TEXT - HTML - XML  The default value is `TEXT`. |
| `section` | The section can be a combination of the following: - `SUMMARY` - `MV_DETAILS` - `QUERY_DETAILS` - `VERIFICATION_DETAILS` - `ALL`  The default value is `ALL`.  You can generate a specific combination of report by using `+` or `-` operators. For example, when section is specified as `SUMMARY+MV_DETAILS`, the generated report will contain only the summary and the details about the automatic materialized view. |
| `level` | The level can be either `BASIC`, `TYPICAL`, or `ALL`. When the level is set to `BASIC`, a minimum set of information regarding the most recent automatic materialized view activity is reported. On the other hand, when the level is set to `ALL`, a detailed report is generated.  The default value is `TYPICAL`. |

Return Value

This functions returns the report as a `CLOB`.

Examples

Example 1: The following call to `REPORT_LAST_ACTIVITY()` generates a `TEXT` output:

```
select dbms_auto_mv.report_last_activity('TEXT', 'ALL', 'TYPICAL') from dual;
```

Example 2: The following call to `REPORT_LAST_ACTIVITY()` generates an XML output:

```
select dbms_auto_mv.report_last_activity('XML', 'ALL', 'TYPICAL') from dual;
```

Example 3: The following call to REPORT\_LAST\_ACTIVITY() generates an HTML output:

```
select dbms_auto_mv.report_last_activity('HTML', 'ALL', 'TYPICAL') from dual;
```
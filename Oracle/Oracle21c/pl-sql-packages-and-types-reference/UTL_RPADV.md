---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_RPADV.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 279 UTL\_RPADV

The `UTL_RPADV` package provides subprograms to collect and analyze statistics for the Oracle Replication components in a distributed database environment. This package uses the Oracle Replication Performance Advisor to gather statistics.

This chapter contains the following topic:

### 279.1 UTL\_RPADV Overview

This package enables you to collect and analyze statistics about the performance or Oracle Replication components. You can either collect statistics on demand or you can create a monitoring job that continually monitors Oracle Replication performance.

When this package is used on an Oracle Database 11g Release 2 (11.2) database, it can monitor Oracle Database 10g Release 2 (10.2) and later databases. It cannot monitor databases before release 10.2.

### 279.2 DBMS\_COMPARISON Security Model

Security on this package can be controlled by either granting `EXECUTE` on this package to selected users or roles, or by granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an Oracle Replication administrator and connect as the Oracle Replication administrator when using this package.

### 279.3 UTL\_RPADV Operational Notes

To use this package, you must connect to an Oracle database as an Oracle Replication administrator and run the `utlrpadv.sql` script in the `rdbms/admin` directory in `ORACLE_HOME`.

The `utlrpadv.sql` script creates the following tables:

- STREAMS$\_PA\_COMPONENT Table
- STREAMS$\_PA\_COMPONENT\_LINK Table
- STREAMS$\_PA\_COMPONENT\_PROP Table
- STREAMS$\_PA\_COMPONENT\_STAT Table
- STREAMS$\_PA\_CONTROL Table
- STREAMS$\_PA\_DATABASE Table
- STREAMS$\_PA\_DATABASE\_PROP Table
- STREAMS$\_PA\_MONITORING Table
- STREAMS$\_PA\_PATH\_BOTTLENECK Table
- STREAMS$\_PA\_PATH\_STAT Table
- STREAMS$\_PA\_SHOW\_COMP\_STAT Table
- STREAMS$\_PA\_SHOW\_PATH\_STAT Table

The Oracle Replication Performance Advisor populates these tables when it is run.

STREAMS$\_PA\_COMPONENT Table

The `STREAMS$_PA_COMPONENT` table displays information about the Oracle Replication components at each database.

Table 279-1 STREAMS$\_PA\_COMPONENT Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT` `NULL` | Identification number assigned to the component by the Oracle Replication Performance Advisor |
| `COMPONENT_NAME` | `VARCHAR2(194)` |  | Name of the component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Name of the database that contains the component |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the component  The following types are possible:  - `CAPTURE` for a capture process - `PROPAGATION` `SENDER` for a propagation sender - `PROPAGATION` `RECEIVER` for a propagation receiver - `APPLY` for an apply process - `QUEUE` for a queue |
| `COMPONENT_CHANGED_TIME` | `DATE` |  | Time when the component was last changed |

STREAMS$\_PA\_COMPONENT\_LINK Table

The `STREAMS$_PA_COMPONENT_LINK` table displays information about how information flows between Oracle Replication components.

Table 279-2 STREAMS$\_PA\_COMPONENT\_LINK Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH_ID` | `NUMBER` | `NOT` `NULL` | Identification number assigned to the path by the Oracle Replication Performance Advisor |
| `PATH_KEY` | `VARCHAR2(4000)` |  | Unique key assigned to the path by the Oracle Replication Performance Advisor |
| `SOURCE_COMPONENT_ID` | `NUMBER` | `NOT` `NULL` | Source component ID for the path  The path starts with this component. |
| `DESTINATION_COMPONENT_ID` | `NUMBER` | `NOT` `NULL` | Destination component ID for the path  The path ends with this component. |
| `POSITION` | `NUMBER` |  | Position of the component in the path |

STREAMS$\_PA\_COMPONENT\_PROP Table

The `STREAMS$_PA_COMPONENT_PROP` table displays information about capture processes and apply processes necessary for analysis by the Replication Performance Advisor.

Table 279-3 STREAMS$\_PA\_COMPONENT\_PROP Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT` `NULL` | Identification number assigned to the component by the Oracle Replication Performance Advisor |
| `PROP_NAME` | `VARCHAR2(30)` |  | Property name  For a capture process, the component properties include the following:  - `SOURCE_DATABASE` - The source database for the changes captured by the capture process - `PARALLELISM` - The setting for the `parallelism` capture process parameter - `OPTIMIZATION_MODE` - Indicates whether the capture process uses combined capture and apply (greater than zero) or does not use combined capture and apply (0)  For an apply process, the component properties include the following:  - `SOURCE_DATABASE` - The source database for the messages applied by the apply process - `PARALLELISM` - The setting for the `parallelism` apply process parameter - `APPLY_CAPTURED` - Indicates whether the apply process applies captured messages (YES) persistent messages (NO) - `MESSAGE_DELIVERY_MODE` - Either buffered or persistent |
| `PROP_VALUE` | `VARCHAR2(30)` |  | Property value |

STREAMS$\_PA\_COMPONENT\_STAT Table

The `STREAMS$_PA_COMPONENT_STAT` table displays performance statistics and session statistics about each Oracle Replication component.

Table 279-4 STREAMS$\_PA\_COMPONENT\_STAT Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was run for the advisor run ID |
| `COMPONENT_ID` | `NUMBER` |  | Identification number assigned to the component by the Oracle Replication Performance Advisor |
| `STATISTIC_TIME` | `DATE` |  | Time when the statistic was recorded |
| `STATISTIC_NAME` | `VARCHAR2(64)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `NUMBER` |  | Value recorded for the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(64)` |  | Unit of measurement for the statistic |
| `SUB_COMPONENT_TYPE` | `VARCHAR2(64)` |  | Type of the subcomponent  Only capture processes and apply processes have subcomponents.  The following capture process subcomponent types are possible:  - `LOGMINER` `READER` for a builder server of a capture process - `LOGMINER` `PREPARER` for a preparer server of a capture process - `LOGMINER` `BUILDER` for a reader server of a capture process - `CAPTURE` `SESSION` for a capture process session  The following apply process subcomponent types are possible:  - `PROPAGATION SENDER+RECEIVER` for sending LCRs from a capture process directly to an apply process in a combined capture and apply configuration in which both the capture process and apply process run on a single database - `APPLY` `READER` for a reader server of an apply process - `APPLY` `COORDINATOR` for a coordinator process of an apply process - `APPLY` `SERVER` for a reader server of an apply process |
| `SESSION_ID` | `NUMBER` |  | Identification number of the session for the component. Query the `V$SESSION` view for information about the session. |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number of the session for the component. Query the `V$SESSION` view for information about the session. |

STREAMS$\_PA\_CONTROL Table

The `STREAMS$_PA_CONTROL` table displays the parameters set for the `COLLECT_STATS` procedure in this package. The parameters control the monitoring behavior.

Table 279-5 STREAMS$\_PA\_CONTROL Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was last run |
| `PARAM_NAME` | `VARCHAR2(30)` |  | The name of the parameter |
| `PARAM_VALUE` | `VARCHAR2(4000)` |  | The value set for the parameter |
| `PARAM_UNIT` | `VARCHAR2(30)` |  | The unit of the parameter |

STREAMS$\_PA\_DATABASE Table

The `STREAMS$_PA_DATABASE` table displays information about each database that contains Oracle Replication components.

Table 279-6 STREAMS$\_PA\_DATABASE Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GLOBAL_NAME` | `VARCHAR2(128)` | `NOT` `NULL` | Global name of the database analyzed by the Oracle Replication Performance Advisor |
| `LAST_QUERIED` | `DATE` |  | The time when the Performance Advisor successfully collected information from a database in its last run |
| `ERROR_NUMBER` | `NUMBER` |  | The error number of the error encountered when the database was last queried |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | The error message of the error encountered when the database was last queried |

STREAMS$\_PA\_DATABASE\_PROP Table

The `STREAMS$_PA_DATABASE_PROP` table displays Oracle Replication database property information necessary for analysis by the Replication Performance Advisor.

Table 279-7 STREAMS$\_PA\_DATABASE\_PROP Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GLOBAL_NAME` | `VARCHAR2(128)` | `NOT` `NULL` | Global name of the database analyzed by the Oracle Replication Performance Advisor |
| `PROP_NAME` | `VARCHAR2(30)` |  | Property name  The database properties include the following:  - `VERSION` - `COMPATIBILITY` - `MANAGEMENT_PACK_ACCESS` - `DB_UNIQUE_NAME` |
| `PROP_VALUE` | `VARCHAR2(30)` |  | Property value |

STREAMS$\_PA\_MONITORING Table

The `STREAMS$_PA_MONITORING` table displays information about each monitoring job running in a database.

Table 279-8 STREAMS$\_PA\_MONITORING Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_NAME` | `VARCHAR2(30)` | `NOT` `NULL` | Name of the monitoring job |
| `CLIENT_NAME` | `VARCHAR2(30)` |  | Name of the client that submitted the job  See Also: " Full Monitoring Job Names " |
| `QUERY_USER_NAME` | `VARCHAR2(30)` |  | User granted privileges to view the monitoring results |
| `SHOW_STATS_TABLE` | `VARCHAR2(30)` |  | Name of the table used by the `SHOW_STATS` procedure to display statistics |
| `STARTED_TIME` | `TIMESTAMP` |  | Time the monitoring job started |
| `STOPPED_TIME` | `TIMESTAMP` |  | Time the monitoring job last stopped |
| `ALTERED_TIME` | `TIMESTAMP` |  | Time the monitoring job was last altered |
| `STATE` | `VARCHAR2(30)` |  | State of the monitoring job, either `ENABLED` or `STOPPED` |

STREAMS$\_PA\_PATH\_BOTTLENECK Table

The `STREAMS$_PA_PATH_BOTTLENECK` table displays information about Oracle Replication components that might be slowing down the flow of messages.

Table 279-9 STREAMS$\_PA\_PATH\_BOTTLENECK Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was last run |
| `ADVISOR_RUN_REASON` | `VARCHAR2(4000)` |  | Reason for the bottleneck |
| `PATH_ID` | `NUMBER` |  | Identification number assigned to the path by the Oracle Replication Performance Advisor |
| `PATH_KEY` | `VARCHAR2(4000)` |  | Unique key assigned to the path by the Oracle Replication Performance Advisor |
| `COMPONENT_ID` | `NUMBER` |  | Identification number assigned to the component by the Oracle Replication Performance Advisor |
| `TOP_SESSION_ID` | `NUMBER` |  | Session ID of the top component. Query the `V$SESSION` view for information about the session. |
| `TOP_SESSION_SERIAL#` | `NUMBER` |  | Session serial number of the top component. Query the `V$SESSION` view for information about the session. |
| `ACTION_NAME` | `VARCHAR2(32)` |  | Action name for the top session |
| `BOTTLENECK_IDENTIFIED` | `VARCHAR2(30)` |  | Whether a bottleneck was identified |

STREAMS$\_PA\_PATH\_STAT Table

The `STREAMS$_PA_PATH_STAT` table displays performance statistics about each stream path.

Table 279-10 STREAMS$\_PA\_PATH\_STAT Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was run for the advisor run ID |
| `PATH_ID` | `NUMBER` |  | Identification number assigned to the path by the Oracle Replication Performance Advisor |
| `PATH_KEY` | `VARCHAR2(4000)` |  | Unique key assigned to the path by the Oracle Replication Performance Advisor |
| `STATISTIC_TIME` | `DATE` |  | Time when the statistic was recorded |
| `STATISTIC_NAME` | `VARCHAR2(64)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `NUMBER` |  | Value recorded for the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(64)` |  | Unit of measurement for the statistic |

STREAMS$\_PA\_SHOW\_COMP\_STAT Table

The `STREAMS$_PA_SHOW_COMP_STAT` table displays statistics for Oracle Replication components.

Table 279-11 STREAMS$\_PA\_SHOW\_COMP\_STAT Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was last run |
| `PATH_ID` | `NUMBER` |  | Identification number assigned to the path by the Oracle Replication Performance Advisor |
| `POSITION` | `NUMBER` |  | Position of the component in the path |
| `COMPONENT_ID` | `NUMBER` |  | Identification number assigned to the component by the Oracle Replication Performance Advisor |
| `COMPONENT_NAME` | `VARCHAR2(194)` |  | Name of the component |
| `COMPONENT_TYPE` | `VARCHAR2(30)` |  | Type of the component  The following types are possible:  - `CAPTURE` for a capture process - `PROPAGATION` `SENDER` for a propagation sender - `PROPAGATION` `RECEIVER` for a propagation receiver - `APPLY` for an apply process - `QUEUE` for a queue |
| `SUB_COMPONENT_TYPE` | `VARCHAR2(30)` |  | Type of the subcomponent  Only capture processes and apply processes have subcomponents.  The following capture process subcomponent types are possible:  - `LOGMINER` `READER` for a builder server of a capture process - `LOGMINER` `PREPARER` for a preparer server of a capture process - `LOGMINER` `BUILDER` for a reader server of a capture process - `CAPTURE` `SESSION` for a capture process session  The following apply process subcomponent types are possible:  - `PROPAGATION SENDER+RECEIVER` for sending LCRs from a capture process directly to an apply process in a combined capture and apply configuration in which both the capture process and apply process run on a single database - `APPLY` `READER` for a reader server of an apply process - `APPLY` `COORDINATOR` for a coordinator process of an apply process - `APPLY` `SERVER` for a reader server of an apply process |
| `SESSION_ID` | `NUMBER` |  | Identification number of the session for the component. Query the `V$SESSION` view for information about the session. |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number of the session for the component. Query the `V$SESSION` view for information about the session. |
| `STATISTIC_ALIAS` | `VARCHAR2(30)` |  | Name of the statistic |
| `STATISTIC_NAME` | `VARCHAR2(128)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `NUMBER` |  | Value recorded for the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(128)` |  | Unit of measurement for the statistic |

STREAMS$\_PA\_SHOW\_PATH\_STAT Table

The `STREAMS$_PA_SHOW_PATH_STAT` table displays statistics for the stream paths in an Oracle Replication configuration. A monitoring job uses this table as the default table for the statistics collected for stream paths.

Table 279-12 STREAMS$\_PA\_SHOW\_PATH\_STAT Table

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH_ID` | `NUMBER` |  | Identification number assigned to the path by the Oracle Replication Performance Advisor |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Identification number of the Oracle Replication Performance Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time when the Oracle Replication Performance Advisor was last run |
| `SETTING` | `VARCHAR2(2000)` |  | Setting for the Oracle Replication Performance Advisor Run |
| `STATISTICS` | `VARCHAR2(4000)` |  | Component-level statistics |
| `SESSION_STATISTICS` | `VARCHAR2(4000)` |  | Session-level statistics |
| `OPTIMIZATION` | `NUMBER` |  | Whether the path uses the combined capture and apply optimization  0 (zero) means that the path does not use the combined capture and apply optimization.  1 means that the path uses the combined capture and apply optimization. |

### 279.4 Summary of UTL\_RPADV Subprograms

This table lists the `UTL_RPADV` subprograms and briefly describes them.

Table 279-13 UTL\_RPADV Package Subprograms

| Subprogram | Description |
| --- | --- |
| ALTER\_MONITORING Procedure | Alters the monitoring job submitted by the current user. |
| COLLECT\_STATS Procedure | Uses the Oracle Replication Performance Advisor to gather statistics about the Oracle Replication components and subcomponents in a distributed database environment. |
| IS\_MONITORING Function | Checks whether a monitoring job is currently running. |
| SHOW\_STATS Procedure | Generates output that includes the statistics gathered by the `COLLECT_STATS` procedure. |
| SHOW\_STATS\_HTML Procedure | Generates HTML output that includes the statistics gathered by the `COLLECT_STATS` procedure. |
| START\_MONITORING Procedure | Starts a monitoring job. |
| STOP\_MONITORING Procedure | Stops a monitoring job. |

#### 279.4.1 ALTER\_MONITORING Procedure

This procedure alters the monitoring job submitted by the current user.

Syntax

```
UTL_RPADV.ALTER_MONITORING(
   interval                      IN NUMBER  DEFAULT NULL,
   top_event_threshold           IN NUMBER  DEFAULT NULL,
   bottleneck_idle_threshold     IN NUMBER  DEFAULT NULL,
   bottleneck_flowctrl_threshold IN NUMBER  DEFAULT NULL,
   retention_time                IN NUMBER  DEFAULT NULL);
```

Parameters

Table 279-14 ALTER\_MONITORING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `interval` | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds.  If `NULL`, then the current value is not changed. |
| `top_event_threshold` | A percentage that determines whether a top wait event statistic is collected.  The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if `15` is specified, then only wait events with a value larger than 15% are collected.  If `NULL`, then the current value is not changed. |
| `bottleneck_idle_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `IDLE` percentage.  The `IDLE` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis.  If `NULL`, then the current value is not changed. |
| `bottleneck_flowctrl_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `FLOW` `CONTROL` percentage.  The `FLOW` `CONTROL` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis.  If `NULL`, then the current value is not changed. |
| `retention_time` | The number of hours to retain monitoring results.  If `NULL`, then the current value is not changed. |

Exceptions

Table 279-15 ALTER\_MONITORING Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-20113` | no active monitoring job found |

#### 279.4.2 COLLECT\_STATS Procedure

This procedure uses the Oracle Replication Performance Advisor to gather statistics about the Oracle Replication components and subcomponents in a distributed database environment.

Note:

This procedure commits.

Syntax

```
UTL_RPADV.COLLECT_STATS(
   interval                      IN NUMBER  DEFAULT 60,
   num_runs                      IN NUMBER  DEFAULT 10,
   comp_stat_table             IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_COMP_STAT',
   path_stat_table             IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_PATH_STAT',
   top_event_threshold           IN NUMBER  DEFAULT 15,
   bottleneck_idle_threshold     IN NUMBER  DEFAULT 50,
   bottleneck_flowctrl_threshold IN NUMBER  DEFAULT 50);
```

Parameters

Table 279-16 COLLECT\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `interval` | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds. |
| `num_runs` | The number of times that the Oracle Replication Performance Advisor is run by the procedure. |
| `comp_stat_table` | The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as `[schema_name.]object_name`. If the schema is not specified, then the current user is the default.  The procedure creates the specified table if it does not exist.  Oracle recommends that you use the default table `STREAMS$_ADVISOR_COMP_STAT`.  See " Usage Notes " for more information about this parameter. |
| `path_stat_table` | The name of the table that stores the statistics collected for stream paths. Specify the table name as `[schema_name.]object_name`. If the schema is not specified, then the current user is the default.  The procedure creates the specified table if it does not exist.  Oracle recommends that you use the default table `STREAMS$_ADVISOR_PATH_STAT`.  See " Usage Notes " for more information about this parameter. |
| `top_event_threshold` | A percentage that determines whether a top wait event statistic is collected.  The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if `15` is specified, then only wait events with a value larger than 15% are collected. |
| `bottleneck_idle_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `IDLE` percentage.  The `IDLE` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. |
| `bottleneck_flowctrl_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `FLOW` `CONTROL` percentage.  The `FLOW` `CONTROL` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. |

Usage Notes

The table specified in the `path_stat_table` parameter stores stream path statistics. This table also concatenates the component and subcomponent statistics stored in the table specified in the `comp_stat_table` parameter. The `SHOW_STATS` procedure in this package shows only the statistics stored in the table specified in the `path_stat_table` parameter.

#### 279.4.3 IS\_MONITORING Function

This function checks whether a monitoring job is currently running. This function either returns `TRUE` if a monitoring job is currently running or `FALSE` if a monitoring job is not currently running.

A monitoring job is submitted using the `START_MONITORING` procedure.

See Also:

" START\_MONITORING Procedure "

Syntax

```
UTL_RPADV.IS_MONITORING(
   job_name    IN VARCHAR2  DEFAULT 'STREAMS$_MONITORING_JOB',
   client_name IN VARCHAR2  DEFAULT NULL) 
RETURN BOOLEAN;
```

Parameters

Table 279-17 IS\_MONITORING Function Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | The name of the job for which to check. |
| `client_name` | The name of the client that submitted the job. |

#### 279.4.4 SHOW\_STATS Procedure

This procedure generates output that includes the statistics gathered by the `COLLECT_STATS` and `START_MONITORING` procedures.

The output is formatted so that it can be imported into a spreadsheet for analysis.

Note:

This procedure does not commit.

See Also:

- " COLLECT\_STATS Procedure "
- " START\_MONITORING Procedure "

Syntax

```
UTL_RPADV.SHOW_STATS(
   path_stat_table IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_PATH_STAT',
   path_id           IN NUMBER    DEFAULT NULL,
   bgn_run_id        IN NUMBER    DEFAULT -1,
   end_run_id        IN NUMBER    DEFAULT -10,
   show_path_id      IN BOOLEAN   DEFAULT TRUE,
   show_run_id       IN BOOLEAN   DEFAULT TRUE,
   show_run_time     IN BOOLEAN   DEFAULT TRUE,
   show_optimization IN BOOLEAN   DEFAULT TRUE,
   show_setting      IN BOOLEAN   DEFAULT FALSE,
   show_stat         IN BOOLEAN   DEFAULT TRUE,
   show_sess         IN BOOLEAN   DEFAULT FALSE,
   show_legend       IN BOOLEAN   DEFAULT TRUE);
```

Parameters

Table 279-18 SHOW\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `path_stat_table` | The name of the table that contains the stream path statistics. Specify the table name as `[schema_name.]object_name`. If the schema is not specified, then the current user is the default.  When you gather statistics using the `COLLECT_STATS` procedure, this table is specified in the `path_stat_table` parameter in the `COLLECT_STATS` procedure. The default table is `STREAMS$_ADVISOR_PATH_STAT`.  When you gather statistics using the `START_MONITORING` procedure, you can determine the name for this table by querying the `SHOW_STATS_TABLE` column in the `STREAMS$_PA_MONITORING` view. The default table for a monitoring job is `STREAMS$_PA_SHOW_PATH_STAT`. |
| `path_id` | A stream path ID.  If non- `NULL`, then the procedure shows output for the specified stream path only.  If `NULL`, then the procedure shows output for all active stream paths. |
| `bgn_run_id` | The first Oracle Replication Performance Advisor run ID to show in the range of runs.  See " Usage Notes " for more information about this parameter. |
| `end_run_id` | The last Oracle Replication Performance Advisor run ID to show in the range of runs.  See " Usage Notes " for more information about this parameter. |
| `show_path_id` | If `TRUE`, then the path ID for each stream path is included in the output.  If `FALSE`, then the path ID for each stream path is not included in the output. |
| `show_run_id` | If `TRUE`, then the Oracle Replication Performance Advisor run ID is included in the output.  If `FALSE`, then the Oracle Replication Performance Advisor run ID is not included in the output. |
| `show_run_time` | If `TRUE`, then the Oracle Replication Performance Advisor run time is included in the output.  If `FALSE`, then the Oracle Replication Performance Advisor run time is not included in the output. |
| `show_optimization` | If `TRUE`, then path output includes information pertaining to the combined capture and apply optimization.  If `FALSE`, then path output does not include information pertaining to the combined capture and apply optimization. |
| `show_setting` | If `TRUE`, then the settings for the threshold parameters are included in the output. The threshold parameters are the `top_event_threshold`, `bottleneck_idle_threshold`, and `bottleneck_flowctrl_threshold` parameters in the `COLLECT_STATS` procedure.  If `FALSE`, then the settings for the threshold parameters are not included in the output. |
| `show_stat` | If `TRUE`, then the component-level and subcomponent-level statistics are included in the output. These components include capture processes, queues, propagation senders, propagation receivers, and apply processes. The subcomponents are the subcomponents for capture processes and apply processes.  If `FALSE`, then the component-level and subcomponent-level statistics are not included in the output. |
| `show_sess` | If `TRUE`, then the session-level statistics are included in the output. Session-level statistics include `IDLE`, `FLOW` `CONTROL`, and `EVENT` statistics.  If `FALSE`, then the session-level statistics are not included in the output. |
| `show_legend` | If `TRUE`, then the legend is included in the output. The legend describes the abbreviations used in the output.  If `FALSE`, then the legend is not included in the output. |

Usage Notes

Use the `bgn_run_id` and `end_run_id` together to specify the range of Oracle Replication Performance Advisor runs to display. Positive numbers show statistics from an earlier run forward. Negative numbers show statistics from a later run backward.

For example, if `bgn_run_id` is set to `1` and `end_run_id` is set to `10`, then the procedure shows statistics for the first ten Oracle Replication Performance Advisor runs.

However, if `bgn_run_id` is set to `-1` and `end_run_id` is set to `-10`, then the procedure shows statistics for the last ten Oracle Replication Performance Advisor runs.

#### 279.4.5 SHOW\_STATS\_HTML Procedure

This procedure generates HTML output that includes the statistics gathered by the `COLLECT_STATS` and `START_MONITORING` procedures.

Note:

This procedure does not commit.

See Also:

- " COLLECT\_STATS Procedure "
- " START\_MONITORING Procedure "

Syntax

```
UTL_RPADV.SHOW_STATS_HTML(
   directory       IN VARCHAR2,
   reportname      IN VARCHAR2  DEFAULT 'RPADVREPORT.HTML',
   comp_stat_table IN VARCHAR2  DEFAULT 'STREAMS$_ADVISOR_COMP_STAT',
   path_id         IN NUMBER    DEFAULT NULL,
   bgn_run_id      IN NUMBER    DEFAULT -1,
   end_run_id      IN NUMBER    DEFAULT -10,
   detailed        IN BOOLEAN   DEFAULT TRUE);
```

Parameters

Table 279-19 SHOW\_STATS\_HTML Procedure Parameters

| Parameter | Description |
| --- | --- |
| `directory` | The directory object for the directory on the local computer system into which the generated HTML report is placed  The specified directory object must be created using the SQL statement `CREATE` `DIRECTORY`, and the user who invokes the procedure must have `READ` and `WRITE` privilege on each one. |
| `reportname` | The name of the HTML report |
| `comp_stat_table` | The name of the table that stores the statistics collected for Oracle Replication components and subcomponents. Specify the table name as `[schema_name.]object_name`. If the schema is not specified, then the current user is the default.  When you gather statistics using the `COLLECT_STATS` procedure, this table is specified in the `comp_stat_table` parameter in the `COLLECT_STATS` procedure. The default table is `STREAMS$_ADVISOR_COMP_STAT`.  When you gather statistics using the `START_MONITORING` procedure, you can determine the name for this table by querying the `SHOW_STATS_TABLE` column in the `STREAMS$_PA_MONITORING` view. The default table for a monitoring job is `STREAMS$_PA_SHOW_PATH_STAT`.  Oracle recommends that you start a monitoring job with the `START_MONITORING` procedure in this package and use the appropriate the `STREAMS$_PA_SHOW_PATH_STAT` table. |
| `path_id` | A stream path ID.  If non- `NULL`, then the procedure shows output for the specified stream path only.  If `NULL`, then the procedure shows output for all active stream paths. |
| `bgn_run_id` | The first Oracle Replication Performance Advisor run ID to show in the range of runs.  See " Usage Notes " for more information about this parameter. |
| `end_run_id` | The last Oracle Replication Performance Advisor run ID to show in the range of runs.  See " Usage Notes " for more information about this parameter. |
| `detailed` | If `TRUE`, then the procedure generates component-level statistics.  If `FALSE`, then the procedure does not generate component-level statistics. |

Usage Notes

Use the `bgn_run_id` and `end_run_id` together to specify the range of Oracle Replication Performance Advisor runs to display. Positive numbers show statistics from an earlier run forward. Negative numbers show statistics from a later run backward.

For example, if `bgn_run_id` is set to `1` and `end_run_id` is set to `10`, then the procedure shows statistics for the first ten Oracle Replication Performance Advisor runs.

However, if `bgn_run_id` is set to `-1` and `end_run_id` is set to `-10`, then the procedure shows statistics for the last ten Oracle Replication Performance Advisor runs.

#### 279.4.6 START\_MONITORING Procedure

This procedure starts a monitoring job.

This procedure runs the `COLLECT_STATS` procedure to gather statistics about the Oracle Replication components and subcomponents in a distributed database environment.

Note:

This procedure commits.

See Also:

- " COLLECT\_STATS Procedure "

Syntax

```
UTL_RPADV.START_MONITORING(
   job_name                      IN VARCHAR2  DEFAULT 'STREAMS$_MONITORING_JOB',
   client_name                   IN VARCHAR2  DEFAULT NULL,
   query_user_name               IN VARCHAR2  DEFAULT NULL,
   interval                      IN NUMBER    DEFAULT 60,
   top_event_threshold           IN NUMBER    DEFAULT 15,
   bottleneck_idle_threshold     IN NUMBER    DEFAULT 50,
   bottleneck_flowctrl_threshold IN NUMBER    DEFAULT 50,
   retention_time                IN NUMBER    DEFAULT 24);
```

Parameters

Table 279-20 START\_MONITORING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | The name of the monitoring job to create. |
| `client_name` | The name of the client. |
| `query_user_name` | The user who will query the result tables.  This procedure grants privileges to the specified user to enable the user to query the result tables. |
| `interval` | The amount of time, in seconds, between each Performance Advisor run. The maximum is 3600 seconds.  The specified interval is used for the interval parameter in the `COLLECT_STATS` procedure. |
| `top_event_threshold` | A percentage that determines whether a top wait event statistic is collected.  The percentage for a wait event must be greater than the value specified in this parameter for the procedure to collect the wait event statistic. For example, if `15` is specified, then only wait events with a value larger than 15% are collected. |
| `bottleneck_idle_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `IDLE` percentage.  The `IDLE` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are idle 50% of the time or less are eligible for bottleneck analysis. |
| `bottleneck_flowctrl_threshold` | A percentage that determines whether an Oracle Replication component session is eligible for bottleneck analysis based on its `FLOW` `CONTROL` percentage.  The `FLOW` `CONTROL` percentage must be less than or equal to the value specified in this parameter for the Oracle Replication component session to be eligible for bottleneck analysis. For example, if `50` is specified, then only components that are paused for flow control 50% of the time or less are eligible for bottleneck analysis. |
| `retention_time` | The number of hours to retain monitoring results. |

Exceptions

Table 279-21 START\_MONITORING Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-20111` | cannot start monitoring due to active EM monitoring job  Stop the Oracle Enterprise Manager (EM) monitoring job, and run the `START_MONITORING` procedure again. |
| `ORA-20112` | cannot start monitoring due to active Replication monitoring job  Stop the Replication monitoring job, and run the `START_MONITORING` procedure again. |

Usage Notes

The following are usage notes for the `START_MONITORING` procedure:

- Requirements for the User Running the Procedure
- Full Monitoring Job Names
- Restrictions on Monitoring Jobs

Requirements for the User Running the Procedure

The user who runs the `START_MONITORING` procedure must meet the following requirements:

- The user must have access to a database link to each database that contains Oracle Replication components.
- The user must have been granted privileges using the `DBMS_XSTREAM_AUTH.GRANT_ADMIN_PRIVILEGE` procedure, and each database link must connect to a user at the remote database that has been granted privileges using the `DBMS_XSTREAM_AUTH.GRANT_ADMIN_PRIVILEGE` procedure.

Full Monitoring Job Names

When you submit a monitoring job, the client name and job name are concatenated to form the full monitoring job name. You specify the client name using the `client_name` parameter and the job name using the `job_name` parameter when you run the `START_MONITORING` procedure. The client name for a monitoring job submitted by Oracle Enterprise Manager is always `EM`.

The following table show examples of full monitoring job names:

| Setting for client\_name Parameter | Setting for job\_name parameter | Full Monitoring Job Name |
| --- | --- | --- |
| `NULL` | `STREAMS$_MONITORING_JOB` | `STREAMS$_MONITORING_JOB` |
| `EM` | `STREAMS$_MONITORING_JOB` | `EMSTREAMS$_MONITORING_JOB` |
| `strm` | `STREAMS$_MONITORING_JOB` | `strmSTREAMS$_MONITORING_JOB` |
| `strm` | `mjob1` | `strmmjob1` |

Restrictions on Monitoring Jobs

The following restrictions apply to monitoring jobs:

- The limit for the length of the full monitoring job name is 30 bytes.
- Two monitoring jobs cannot have the same full monitoring job name, even if the monitoring jobs were submitted by different schemas. The name check is not case-sensitive. For example, `strmSTREAMS$_MONITORING_JOB` and `STRMSTREAMS$_MONITORING_JOB` are considered to be the same name.
- Oracle Enterprise Manager can have at most one monitoring job for each database.
- Each schema can have at most one monitoring job.

#### 279.4.7 STOP\_MONITORING Procedure

This procedure stops a monitoring job that was submitted by the current user.

Syntax

```
UTL_RPADV.STOP_MONITORING(
   purge IN BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 279-22 STOP\_MONITORING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `purge` | If `TRUE`, then the procedure purges information about the monitoring job from the result tables.  If `FALSE`, then the procedure retains information about the monitoring job in the result tables. |
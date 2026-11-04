---
title: DBMS_WORKLOAD_REPLAY
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_replay.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 161 DBMS\_WORKLOAD\_REPLAY

The `DBMS_WORKLOAD_REPLAY` package provides an interface to replay a workload capture.

See Also:

[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm) for more information about database replay

This chapter contains the following topics:

- Using DBMS\_WORKLOAD\_REPLAY
- Summary of DBMS\_WORKLOAD\_REPLAY Subprograms

---

## Using DBMS\_WORKLOAD\_REPLAY

- Overview
- Security Model

---

### Overview

The `DBMS_WORKLOAD_REPLAY` package provides an interface to replay a workload capture that was originally created by way of the [DBMS\_WORKLOAD\_CAPTURE](d_workload_capture.md) package. Typically, the `DBMS_WORKLOAD_CAPTURE` package is used in the production system to capture a production workload, and the `DBMS_WORKLOAD_REPLAY` package is subsequently used in a test system to replay the captured production workload for testing purposes.

---

### Security Model

The following code describes the minimum set of privileges required to

- Create directory objects
- Operate the interface provided by the `DBMS_WORKLOAD_CAPTURE` and `DBMS_WORKLOAD_REPLAY` packages
- Act as a replay client user (wrc `someuser` / `somepassword` or wrc `USER=someuser` `PASSWORD=somepassword`)
```
DROP USER rom1 CASCADE;
CREATE USER rom1 IDENTIFIED BY rom1;
 
GRANT EXECUTE ON DBMS_WORKLOAD_CAPTURE TO rom1;
GRANT EXECUTE ON DBMS_WORKLOAD_REPLAY TO rom1;
 
GRANT CREATE SESSION TO rom1;
GRANT CREATE ANY DIRECTORY TO rom1;
GRANT SELECT_CATALOG_ROLE TO rom1;
GRANT BECOME USER TO rom1;
```

Appropriate OS permissions are required to access and manipulate files and directories on both the capture and replay system. The Oracle process(es) and the OS user performing the capture or replay must be able to access and manipulate at least one common directory accessible from the host where the instance is running.

The replay client is a multithreaded program (an executable named `wrc` located in the `$ORACLE_HOME/bin` directory) where each thread submits a workload from a captured session. The OS user performing the replay must be able to execute `wrc` on hosts that are used for the replay clients and be able to access the file system appropriately to be able to copy the capture to the replay clients' hosts if required.

---

## Summary of DBMS\_WORKLOAD\_REPLAY Subprograms

This table lists the package subprograms in alphabetical order.

Table 161-1 DBMS\_WORKLOAD\_REPLAY Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_CAPTURE Function | Adds the given capture to the current schedule |
| ADD\_FILTER Procedure | Adds a filter to replay only a subset of the captured workload |
| ADD\_SCHEDULE\_ORDERING Function | Adds a schedule order between two captures |
| BEGIN\_REPLAY\_SCHEDULE Procedure | Initiates the creation of a reusable replay schedule |
| CALIBRATE Function | Operates on a processed workload capture directory to estimate the number of hosts and workload replay clients needed to faithfully replay the given workload |
| CANCEL\_REPLAY Procedure | Cancels the workload replay in progress |
| COMPARE\_PERIOD\_REPORT Procedure | Generates a report comparing a replay to its capture or to another replay of the same capture |
| COMPARE\_SQLSET\_REPORT Function | Generates a report comparing a sqlset captured during replay to one captured during workload capture or to one captured during another replay of the same capture |
| CREATE\_FILTER\_SET Procedure | Uses the replay filters added to create a set of filters to use against the replay in `replay_dir` |
| DELETE\_FILTER Procedure | Deletes the named filter |
| DELETE\_REPLAY\_INFO Procedure | Deletes the rows in `DBA_WORKLOAD_REPLAYS` that corresponds to the given workload replay ID |
| END\_REPLAY\_SCHEDULE Procedure | Wraps up the creation of the current schedule |
| EXPORT\_AWR Procedure | Exports the Automatic Workload Repository (AWR) snapshots associated with a given replay ID |
| GENERATE\_CAPTURE\_SUBSET Procedure | Creates a new capture from an existing workload capture |
| GET\_DIVERGING\_STATEMENT Function | Exports the Automatic Workload Repository (AWR) snapshots associated with a given replay ID |
| GET\_REPLAY\_DIRECTORY Function | Returns the current replay directory set by the SET\_REPLAY\_DIRECTORY Procedure. |
| GET\_REPLAY\_INFO Function | Retrieves information about the workload capture and the history of all the workload replay attempts from the related directory |
| GET\_REPLAY\_TIMEOUT Procedure | Retrieves the replay timeout setting |
| IMPORT\_AWR Function | Imports the Automatic Workload Repository (AWR) snapshots associated with a given replay ID |
| INITIALIZE\_CONSOLIDATED\_REPLAY Procedure | Puts the database state in `INIT` for a multiple-capture replay |
| INITIALIZE\_REPLAY Procedure | Initializes replay, and loads specific data produced during processing into the database |
| IS\_REPLAY\_PAUSED Function | Reports whether the replay is currently paused |
| PAUSE\_REPLAY Procedure | Pauses the in-progress workload replay |
| POPULATE\_DIVERGENCE Procedure | Precomputes the divergence information for the given call, stream, or the whole replay so that the GET\_DIVERGING\_STATEMENT Function returns as quickly as possible for the precomputed calls |
| PREPARE\_REPLAY Procedure | Puts the database in a special "Prepare" mode |
| PREPARE\_CONSOLIDATED\_REPLAY Procedure | Puts the database in a special "Prepare" mode for a multiple-capture replay |
| PROCESS\_CAPTURE Procedure | Processes the workload capture found in `capture_dir` in place |
| REMAP\_CONNECTION Procedure | Remaps the captured connection to a new one so that the user sessions can connect to the database in a desired way during workload replay |
| REMOVE\_CAPTURE Procedure | Removes the given capture from the current schedule |
| REMOVE\_SCHEDULE\_ORDERING Procedure | Removes an existing schedule order from the current replay schedule |
| REPORT Function | Generates a report on the given workload replay |
| RESUME\_REPLAY Procedure | Resumes a paused workload replay |
| REUSE\_REPLAY\_FILTER\_SET Procedure | Reuses filters in the specified filter set as if each were added using the ADD\_SCHEDULE\_ORDERING Function |
| SET\_ADVANCED\_PARAMETER Procedure | Sets an advanced parameter for replay besides the ones used with the PREPARE\_REPLAY Procedure |
| SET\_REPLAY\_DIRECTORY Procedure | Sets a directory that contains multiple workload captures as the current replay directory |
| SET\_REPLAY\_TIMEOUT Procedure | Sets the replay timeout setting |
| SET\_USER\_MAPPING Procedure | Sets a new schema or user name to be used during replay instead of the captured user |
| START\_CONSOLIDATED\_REPLAY Procedure | Starts the replay of a multiple-capture capture |
| START\_REPLAY Procedure | Starts the workload replay |
| USE\_FILTER\_SET Procedure | Uses the given filter set that has been created by calling the CREATE\_FILTER\_SET Procedure to filter the current replay |

---

### ADD\_CAPTURE Function

This function adds the given capture to the current schedule. The directory has to be a valid capture processed in the current database's version. It returns a unique ID that identifies this capture within this schedule.

Syntax

```
DBMS_WORKLOAD_REPLAY.ADD_CAPTURE (
   capture_dir_name      IN    VARCHAR2,
   start_delay_seconds   IN    NUMBER  DEFAULT 0,
   stop_replay           IN    BOOLEAN FALSE,
   take_begin_snapshot   IN    BOOLEAN TRUE,
   take_end_snapshot     IN    BOOLEAN TRUE,
   query_only            IN    BOOLEAN DEFAULT FALSE)
 RETURN NUMBER;

DBMS_WORKLOAD_REPLAY.ADD_CAPTURE (
   capture_dir_name      IN    VARCHAR2,
   start_delay_seconds   IN    NUMBER  DEFAULT 0,
   stop_replay           IN    BOOLEAN FALSE,
   take_begin_snapshot   IN    BOOLEAN TRUE,
   take_end_snapshot     IN    BOOLEAN TRUE,
   query_only            IN    VARCHAR2 DEFAULT 'N')
 RETURN NUMBER;
```

Parameters

Table 161-2 ADD\_CAPTURE Function Parameters

| Parameter | Description |
| --- | --- |
| `capture_dir_name` | Name of the OS directory containing the capture under the replay top-level directory |
| `start_delay_seconds` | Delay time in seconds before the replay of this capture starts |
| `stop_replay` | Stop the replay after it finishes |
| `take_begin_snapshot` | Take an AWR snapshot when the replay of this capture starts |
| `take_end_snapshot` | Take an AWR snapshot when the replay of this capture finishes |
| `query_only` | Replay only the read-only queries of this workload capture |

Usage Notes

The SET\_REPLAY\_DIRECTORY Procedure must have already been called.

---

### ADD\_FILTER Procedure

This procedure adds a filter to replay only a subset of the captured workload.

The procedure adds a new filter that is used in the next replay filter set created using the CREATE\_FILTER\_SET Procedure. This filter will be considered an " `INCLUSION` " or " `EXCLUSION` " filter depending on the argument passed to `CREATE_FILTER_SET` when creating the filter set.

Syntax

```
DBMS_WORKLOAD_REPLAY.ADD_FILTER (
   fname          IN VARCHAR2,
   fattribute     IN VARCHAR2,
   fvalue         IN VARCHAR2);

DBMS_WORKLOAD_REPLAY.ADD_FILTER (
   fname          IN VARCHAR2,
   fattribute     IN VARCHAR2,
   fvalue         IN NUMBER);
```

Parameters

Table 161-3 ADD\_FILTER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `fname` | (Mandatory) Name of the filter. Can be used to delete the filter later if it is not required. |
| `fattribute` | (Mandatory) Specifies the attribute on which the filter is defined as one of the following values of type `STRING`:  - `USER` - `MODULE` - `ACTION` - `PROGRAM` - `SERVICE` - `CONNECTION_STRING` |
| `fvalue` | (Mandatory) Specifies the value to which the given 'attribute' must be equal to for the filter to be considered active. Wildcards such as '%' are acceptable for all attributes that are of type `STRING`. Currently all the listed values of `fattribute` are of type `STRING`. `INSTANCE_NUMBER` is a `NUMBER` attribute. It is currently only supported for capture. |

---

### ADD\_SCHEDULE\_ORDERING Function

This function adds a schedule order between two captures. Together, `schedule_capture_id` and waitfor\_capture\_id form a schedule ordering that previously added by the ADD\_SCHEDULE\_ORDERING Function. The order is that replay of capture indicated by `schedule_capture_id` will not start unless the replay of capture indicated by `waiting_for_capture_id` finishes.

Syntax

```
DBMS_WORKLOAD_REPLAY.ADD_SCHEDULE_ORDERING (
   schedule_capture_id     IN VARCHAR2,
   waitfor_capture_id      IN VARCHAR2)
  RETURN NUMBER;
```

Parameters

Table 161-4 ADD\_SCHEDULE\_ORDERING Function Parameters

| Parameter | Description |
| --- | --- |
| `schedule_capture_id` | Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, its replay will not start until the replay of another capture specified by `waitfor_capture_id` runs to completion. |
| `waitfor_capture_id` | Points to a capture that has been added to the current replay schedule. According to the new schedule ordering added by this subprogram, the replay of capture specified by `schedule_capture_id` will not start until the replay of this capture runs to completion. |

Return Values

Returns a non-zero error code if the constraint cannot be added

Usage Notes

The two captures must have already been added to the replay schedule.

---

### BEGIN\_REPLAY\_SCHEDULE Procedure

This procedure initiates the creation of a reusable replay schedule.

Syntax

```
DBMS_WORKLOAD_REPLAY.BEGIN_REPLAY_SCHEDULE  (
   replay_dir_obj     IN     VARCHAR2,
   schedule_name      IN     VARCHAR2);
```

Parameters

Table 161-5 BEGIN\_REPLAY\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_dir_obj` | Directory object that points to the replay directory that contains all the capture directories involved in the schedule |
| `schedule_name` | Name of the schedule to be replayed |

Usage Notes

- Only one schedule can be in creation mode at a time. Calling the subprogram again before `end_replay_schedule` will raise an error.
- Prerequisites:
	- The workload capture was already processed using the PROCESS\_CAPTURE Procedure in the same database version.
		- The user must have copied the capture directory appropriately.
		- The database is not in replay mode.
		- The SET\_REPLAY\_DIRECTORY Procedure has already been called.

---

### CALIBRATE Function

This function operates on a processed workload capture directory to estimate the number of hosts and workload replay clients needed to faithfully replay the given workload. This function returns the results as an XML `CLOB`.

Syntax

```
DBMS_WORKLOAD_REPLAY.CALIBRATE (
   capture_dir          IN VARCHAR2,
   process_per_cpu      IN BINARY_INTEGER DEFAULT 4,
   threads_per_process  IN BINARY_INTEGER DEFAULT 50)
  RETURN CLOB;
```

Parameters

Table 161-6 CALIBRATE Function Parameters

| Parameter | Description |
| --- | --- |
| `capture_dir` | Name of the directory object that points to the (case sensitive) OS directory that contains processed capture data |
| `process_per_cpu` | Maximum number of processes allowed for each CPU (default is 4) |
| `threads_per_process` | Maximum number of threads allowed for each process (default is 50) |

Return Values

Returns a `CLOB` formatted as XML that contains:

- Information about the capture
- Current database version
- Input parameters to this function
- Number of CPUs and replay clients needed to replay the given workload
- Information about the sessions captured (total number and maximum concurrency)

Usage Notes

- Prerequisite: The input workload capture was already processed using the PROCESS\_CAPTURE Procedure in the same database version.
- This procedure will return the same results as the workload replay client in calibrate mode, which can be run as follows.
	```
	$ wrc mode=calibrate replaydir=
	```

---

### CANCEL\_REPLAY Procedure

This procedure cancels workload replay in progress. All the external replay clients (WRC) will automatically be notified to stop issuing the captured workload and exit.

Syntax

```
DBMS_WORKLOAD_REPLAY.CANCEL_REPLAY (
   error_msg    IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 161-7 CANCEL\_REPLAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `error_msg` | An optional reason for cancelling the replay can be passed which is recorded into `DBA_WORKLOAD_REPLAYS`.`ERROR_MESSAGE`. |

Usage Notes

Prerequisite: A call to the INITIALIZE\_REPLAY Procedure, or PREPARE\_REPLAY Procedure, or START\_REPLAY Procedure was already issued.

---

### COMPARE\_PERIOD\_REPORT Procedure

This procedure generates a report comparing a replay to its capture or to another replay of the same capture.

Syntax

```
DBMS_WORKLOAD_REPLAY.COMPARE_PERIOD_REPORT (
   replay_id1   IN   NUMBER,
   replay_id2   IN   NUMBER,
   format       IN   VARCHAR2,
   result       OUT  CLOB );
```

Parameters

Table 161-8 COMPARE\_PERIOD\_REPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_id1` | First ID of the workload replay whose report is requested |
| `replay_id2` | Second ID of the workload replay whose report is requested. If this is `NULL`, then the comparison is done with the capture. |
| `format` | Specifies the report format. Valid values are `DBMS_WORKLOAD_CAPTURE`.`TYPE_HTML` and `DBMS_WORKLOAD_CAPTURE`.`TYPE_XML`. |
| `result` | Output of the report (`CLOB`) |

---

### COMPARE\_SQLSET\_REPORT Function

This procedure generates a report comparing a sqlset captured during replay to one captured during workload capture or to one captured during another replay of the same capture.

Syntax

```
DBMS_WORKLOAD_REPLAY.COMPARE_SQLSET_REPORT (
   replay_id1    IN NUMBER,
   replay_id2    IN NUMBER,
   format        IN VARCHAR2,
   r_level       IN VARCHAR2 DEFAULT 'ALL',
   r_sections    IN VARCHAR2 DEFAULT 'ALL',
   result        OUT CLOB )
  RETURN VARCHAR2;
```

Parameters

Table 161-9 COMPARE\_SQLSET\_REPORT Function Parameters

| Parameter | Description |
| --- | --- |
| `replay_id1` | First ID of the workload replay after a change |
| `replay_id2` | Second ID of the workload replay before a change. If this is `NULL`, then the comparison is done with the capture. |
| `format` | Specifies the report format. Valid values are `DBMS_WORKLOAD_CAPTURE`.`TYPE_HTML`, `DBMS_WORKLOAD_CAPTURE`.`TYPE_XML` and `DBMS_WORKLOAD_CAPTURE.TYPE_TEXT`. |
| `r_level` | See `level` parameter in the [REPORT\_ANALYSIS\_TASK Function](d_sqlpa.md) in the [DBMS\_SQLPA](d_sqlpa.md) package |
| `r_sections` | See `section` parameter in the [REPORT\_ANALYSIS\_TASK Function](d_sqlpa.md) in the [DBMS\_SQLPA](d_sqlpa.md) package |
| `result` | Output of the report (`CLOB`) |

---

### CREATE\_FILTER\_SET Procedure

This procedure creates a new filter set for the replays at `replay_dir`. It includes all the replay filters that have already been added by the ADD\_FILTER Procedure. After the procedure has completed and replay initiated, the newly-created filter set can be used to filter the replay in `replay_dir` by calling the USE\_FILTER\_SET Procedure.

Syntax

```
DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET(
   replay_dir       IN  VARCHAR2,
   filter_set       IN  VARCHAR2,
   default_action   IN  VARCHAR2 DEFAULT 'INCLUDE');
```

Parameters

Table 161-10 CREATE\_FILTER\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_dir` | Object directory of the replay to be filtered |
| `filter_set` | Name of the filter set to create (to use in USE\_FILTER\_SET Procedure) |
| `default_action` | Can be either `INCLUDE` or `EXCLUDE`. Determines whether, by default, every captured call must be replayed or not. Also determines whether the workload filters specified must be considered as `INCLUSION` filters or `EXCLUSION` filters.)  If it is `INCLUDE`, then by default all captured calls are replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using the ADD\_SCHEDULE\_ORDERING Function are treated as `EXCLUSION` filters, and will determine the workload that will not be replayed.  If it is `EXCLUDE`, then by default no captured call to the database is replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using he ADD\_SCHEDULE\_ORDERING Function are treated as `INCLUSION` filters, and will determine the workload that is replayed.  Default: `INCLUDE` and all the filters specified are assumed to be `EXCLUSION` filters |

Usage Notes

This operation must be invoked when no replay is initialized, prepared, or in progress.

---

### DELETE\_FILTER Procedure

This procedure deletes the named filter.

Syntax

```
DBMS_WORKLOAD_REPLAY.DELETE_FILTER(
   fname    IN  VARCHAR2);
```

Parameters

Table 161-11 DELETE\_FILTER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `fname` | (Mandatory) Name of the filter that must be deleted |

---

### DELETE\_REPLAY\_INFO Procedure

This procedure deletes the rows in `DBA_WORKLOAD_REPLAYS` that correspond to the given workload replay ID.

Syntax

```
DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO (
   replay_id    IN  NUMBER);
```

Parameters

Table 161-12 DELETE\_REPLAY\_INFO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | (Mandatory) ID of the workload replay that must be deleted. Corresponds to `DBA_WORKLOAD_REPLAYS`.`ID` |

---

### END\_REPLAY\_SCHEDULE Procedure

This procedure wraps up the creation of the current schedule. The schedule is now saved and associated with the replay directory and can be used for a replay.

Syntax

```
DBMS_WORKLOAD_REPLAY.END_REPLAY_SCHEDULE;
```

Usage Notes

The BEGIN\_REPLAY\_SCHEDULE Procedure must have already been called.

---

### EXPORT\_AWR Procedure

This procedure exports the AWR snapshots associated with a stipulated replay ID.

Syntax

```
DBMS_WORKLOAD_REPLAY.EXPORT_AWR (
   replay_id    IN  NUMBER);
```

Parameters

Table 161-13 EXPORT\_AWR Function Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | (Mandatory) ID of the replay whose AWR snapshots are to be exported |

Usage Notes

- At the end of each replay, the corresponding AWR snapshots are automatically exported. Consequently, there is no need to do this manually after a workload replay is complete, unless the automatic `EXPORT_AWR` invocation failed.
- This procedure will work only if the corresponding workload replay was performed in the current database (meaning that the corresponding row in `DBA_WORKLOAD_REPLAYS` was not created by calling the GET\_REPLAY\_INFO Function) and the AWR snapshots that correspond to that replay time period are still available.

---

### GENERATE\_CAPTURE\_SUBSET Procedure

This procedure creates a new capture from an existing workload capture.

Syntax

```
DBMS_WORKLOAD_REPLAY.GENERATE_CAPTURE_SUBSET (
   input_capture_dir          IN   VARCHAR2,
   output_capture_dir         IN   VARCHAR2,
   new_capture_name           IN   VARCHAR2,
   begin_time                 IN   NUMBER,
   begin_include_incomplete   IN   BOOLEAN DEFAULT TRUE,
   end_time                   IN   NUMBER,
   end_include_incomplete     IN   BOOLEAN DEFAULT FALSE,
   parallel_level             IN   NUMBER DEFAULT NULL);
```

Parameters

Table 161-14 GENERATE\_CAPTURE\_SUBSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `input_capture_dir` | (Mandatory) Name of the directory object that points to an existing workload capture |
| `output_capture_dir` | (Mandatory) Name of the directory object that points to the new capture |
| `new_capture_name` | (Mandatory) Name of new capture |
| `begin_time` | Start of the time range - time offset in seconds from the start of a workload capture |
| `begin_include_incomplete` | Column to include incomplete calls caused by `begin_time` |
| `end_time` | End of the time range - time offset in seconds from the start of a workload capture. If `end_time` is zero or `end_time` is less or equal than `begin_time`, the time range is invalid. The new capture will use the whole duration of the input capture. |
| `end_include_incomplete` | Column to include incomplete calls caused by `end_time` |
| `parallel_level` | Number of Oracle processes used to process the input captures in a parallel fashion. The `NULL` default value will auto-compute the parallelism level based on number of CPUs, whereas a value of 1 will enforce serial execution. |

---

### GET\_DIVERGING\_STATEMENT Function

This function retrieves information about a diverging call, including the statement text, the SQL ID, and the binds. If the replay of a recorded user call has data or error divergence, it is a diverging call.

Syntax

```
DBMS_WORKLOAD_REPLAY.GET_DIVERGING_STATEMENT (
   replay_id    IN NUMBER,
   stream_id    IN NUMBER,
   call_counter IN NUMBER)
  RETURN CLOB;
```

Parameters

Table 161-15 GET\_DIVERGING\_STATEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | ID of the replay in which that call diverged |
| `stream_id` | Stream ID of the diverging call |
| `call_counter` | Call counter of the diverging call |

Usage Notes

- Returns a `CLOB` formatted as XML that contains:
	- SQL ID
		- SQL Text
		- Bind information: position, name and value
- This function will silently invoke the POPULATE\_DIVERGENCE Procedure to read the information from the capture files. Therefore, if divergence has not been populated, then the first call to this function for a particular diverging call might take longer, especially in very large captures.

---

### GET\_REPLAY\_DIRECTORY Function

This function returns the current replay directory set by the SET\_REPLAY\_DIRECTORY Procedure. It returns `NULL` if no replay directory has been set.

Syntax

```
DBMS_WORKLOAD_REPLAY.GET_REPLAY_DIRECTORY
   RETURN VARCHAR2;
```

---

### GET\_REPLAY\_INFO Function

This function retrieves information about the workload capture and the history of all the workload replay attempts from the stipulated directory.

Syntax

```
DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO (
   dir    IN VARCHAR2)
 RETURN NUMBER;
```

Parameters

Table 161-16 GET\_REPLAY\_INFO Function Parameters

| Parameter | Description |
| --- | --- |
| `dir` | (Mandatory) Name of the workload replay directory object (case sensitive). |

Return Values

The procedure returns the `CAPTURE_ID`, which can be associated with both `DBA_WORKLOAD_CAPTURES`.`ID` and `DBA_WORKLOAD_REPLAYS`.`CAPTURE_ID` to access the imported information.

Usage Notes

- The procedure first imports a row into `DBA_WORKLOAD_CAPTURES` which will contain information about the capture. It then imports a row for every replay attempt retrieved from the given replay directory into `DBA_WORKLOAD_REPLAYS`.
- The procedure will not insert new rows to `DBA_WORKLOAD_CAPTURES` and `DBA_WORKLOAD_REPLAYS` if these views already contain rows describing the capture and replay history present in the given directory.

---

### GET\_REPLAY\_TIMEOUT Procedure

This procedure gets the replay timeout setting.

Syntax

```
DBMS_WORKLOAD_REPLAY.GET_REPLAY_TIMEOUT (
   enabled       OUT  BOOLEAN, 
   min_delay     OUT  NUMBER,
   max_delay     OUT  NUMBER,
   delay_factor  OUT  NUMBER);
```

Parameters

Table 161-17 GET\_REPLAY\_TIMEOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `enabled` | `TRUE` if the timeout action is enabled, `FALSE` otherwise. |
| `min_delay` | Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than `min_delay`. |
| `max_delay` | Upper bound of call delay in minutes. The timeout action throws `ORA-15569` when the delay is more than `max_delay`. |
| `delay_factor` | Factor for the call delay that is between `min_delay` and `max_delay`. The timeout action throws `ORA-15569` when the current replay elapsed time is more than the product of capture elapsed time and `delay_factor`. |

Usage Notes

This procedure can be called anytime during replay.

---

### IMPORT\_AWR Function

This procedure imports the AWR snapshots from a given replay.

Syntax

```
DBMS_WORKLOAD_REPLAY.IMPORT_AWR (
   replay_id       IN   NUMBER,
   staging_schema  IN   VARCHAR2)
  RETURN NUMBER;
```

Parameters

Table 161-18 IMPORT\_AWR Function Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | (Mandatory) ID of the replay whose AWR snapshots must be imported |
| `staging_schema` | (Mandatory) Name of a valid schema in the current database which can be used as a staging area while importing the AWR snapshots from the replay directory to the `SYS` `AWR` schema. The `SYS` schema is not a valid input. |

Return Values

Returns the new randomly generated database ID that was used to import the AWR snapshots. The same value can be found in the `AWR_DBID` column in the `DBA_WORKLOAD_REPLAYS` view.

Usage Notes

- This procedure will work provided those AWR snapshots were exported earlier from the original replay system using the EXPORT\_AWR Procedure.
- `IMPORT_AWR` will fail if the `staging_schema` provided as input contains any tables with the same name as any of the AWR tables, such as `WRM$_SNAPSHOT` or `WRH$_PARAMETER`. Drop any such tables in the `staging_schema` before invoking `IMPORT_AWR`.

---

### INITIALIZE\_CONSOLIDATED\_REPLAY Procedure

This procedure puts the database state in `INIT` for a multiple-capture replay. It uses the `replay_dir` which has already been defined by the SET\_REPLAY\_DIRECTORY Procedure, pointing to a directory that contains all the capture directories involved in the schedule. It reads data about schedule `schedule_name` from the directory, and loads required connection data into the replay system.

Syntax

```
DBMS_WORKLOAD_REPLAY.INITIALIZE_CONSOLIDATED_REPLAY (
   replay_name        IN    VARCHAR2,
   schedule_name      IN    VARCHAR2);
```

Parameters

Table 161-19 INITIALIZE\_CONSOLIDATED\_REPLAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_name` | (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. |
| `schedule_name` | Name of the schedule to be replayed. It must have been created through the BEGIN\_REPLAY\_SCHEDULE Procedure for the replay directory `replay_dir`. |

Usage Notes

Prerequisites:

- Workload capture was already processed using the PROCESS\_CAPTURE Procedure in the same database version.
- Database state has been logically restored to what it was at the beginning of the original workload capture.
- The SET\_REPLAY\_DIRECTORY Procedure has been called.

---

### INITIALIZE\_REPLAY Procedure

This procedure puts the database state in `INIT` for `REPLAY` mode, and loads data into the replay system that is required before preparing for the replay (by executing the PAUSE\_REPLAY Procedure).

Syntax

```
DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY (
   replay_name     IN  VARCHAR2,
   replay_dir      IN  VARCHAR2);
```

Parameters

Table 161-20 INITIALIZE\_REPLAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_name` | (Mandatory) Name of the workload replay. Every replay of a processed workload capture can be given a name. |
| `replay_dir` | Name of the directory object that points to the OS directory (case sensitive) that contains processed capture data |

Usage Notes

- Prerequisites:
	- Workload capture was already processed using the PROCESS\_CAPTURE Procedure in the same database version.
		- Database state has been logically restored to what it was at the beginning of the original workload capture.
- The subprogram loads data into the replay system that is required before preparing for the replay by calling the PAUSE\_REPLAY Procedure.
	For instance, during capture the user may record the connection string each session used to connect to the server. The INITIALIZE\_REPLAY Procedure loads this data and allows the user to re-map the recorded connection string to new connection strings or service points.
	Elaborating on the example described in the PROCESS\_CAPTURE Procedure, the user could invoke the following:
	```
	DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY('replay foo #1', 'rec_dir');
	```
	This command will load up the connection map and by default will set all replay time connection strings to be equal to `NULL`. A `NULL` replay time connection string means that the workload replay clients (WRCs) will connect to the default host as determined by the replay client's runtime environment settings. The user can change a particular connection string to a new one (or a new service point) for replay by using the REMAP\_CONNECTION Procedure.

---

### IS\_REPLAY\_PAUSED Function

This function reports whether the replay is currently paused.

Syntax

```
DBMS_WORKLOAD_REPLAY.IS_REPLAY_PAUSED
   RETURN BOOLEAN;
```

Return Values

Returns `TRUE` if the PAUSE\_REPLAY Procedure has been called successfully and the RESUME\_REPLAY Procedure has not been called yet.

Usage Notes

A call to the START\_REPLAY Procedure must have already been issued as a prerequisite.

---

### PAUSE\_REPLAY Procedure

This procedure pauses the in-progress workload replay. All subsequent user calls from the replay clients will be stalled until either a call to the RESUME\_REPLAY Procedure is issued or the replay is cancelled.

Syntax

```
DBMS_WORKLOAD_REPLAY.PAUSE_REPLAY;
```

Usage Notes

- Prerequisite: A call to the START\_REPLAY Procedure must have already been issued.
- User calls that were already in-progress when this procedure was invoked are allowed to run to completion. Only subsequent user calls, when issued, are paused.

---

### POPULATE\_DIVERGENCE Procedure

This procedure precomputes the divergence information for the given call, stream, or the whole replay so that the GET\_DIVERGING\_STATEMENT Function returns as quickly as possible for the precomputed calls.

Syntax

```
DBMS_WORKLOAD_REPLAY.POPULATE_DIVERGENCE (
   replay_id    IN   NUMBER,
   stream_id    IN   NUMBER DEFAULT NULL,
   call_counter IN   NUMBER DEFAULT NULL);
```

Parameters

Table 161-21 POPULATE\_DIVERGENCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | ID of the replay |
| `stream_id` | Stream ID of the diverging call. If `NULL` is provided, then divergence information is precomputed for all diverging calls in the given replay. |
| `call_counter` | Call counter of the diverging call. If `NULL` is provided, then divergence information is precomputed for all diverging calls in the given stream. |

---

### PREPARE\_REPLAY Procedure

This procedure puts the database state in `PREPARE FOR REPLAY` mode.

Syntax

```
DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY (
   synchronization           IN BOOLEAN   DEFAULT TRUE,
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   scale_up_multiplier       IN NUMBER    DEFAULT 1,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);

DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY (
   synchronization           IN VARCHAR2  DEFAULT 'OBJECT_ID',
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   scale_up_multiplier       IN NUMBER    DEFAULT 1,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);
```

Parameters

Table 161-22 PREPARE\_REPLAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `synchronization` | Turns synchronization `ON` or `OFF` during workload replay.  - `OFF` - Workload replay runs asynchronously. - `SCN` - The `COMMIT` order observed during the original workload capture is preserved during replay. Every action that is replayed is executed only after all of its dependent `COMMIT` s (all `COMMIT` s that were issued before the given action in the original workload capture) have finished execution. - `OBJECT_ID` - This is the default, and uses a more advanced synchronization scheme. Every action that is replayed is executed only after the relevant `COMMIT` s have finished executing. The relevant `COMMIT` s are the ones that were issued before the given action in the original workload capture and that had modified at least one of the database objects the given action is referencing (either implicitly or explicitly). This `OBJECT_ID` scheme has the same logical property of making sure that any action will see the same data it saw during capture, but will allow more concurrency during replays for the actions that do not touch the same objects/tables.  For legacy reasons, there is a boolean version of this procedure:  - `TRUE` means `'OBJECT_ID'` - `FALSE` means `'OFF'` |
| `connect_time_scale` | Scales the time elapsed between the instant the workload capture was started and the session connects with the given value. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. `DEFAULT` `VALUE` is 100. See "Application of the connect\_time\_scale Parameter". |
| `think_time_scale` | Scales the time elapsed between two successive user calls from the same session. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. `DEFAULT` `VALUE` is 100. See "Application of the think\_time\_scale Parameter". |
| `think_time_auto_correct` | Auto corrects the think time between calls appropriately when a user call takes longer to complete during replay than during the original capture. `DEFAULT` is `TRUE` which is to reduce think time if replay goes slower than capture. See "Application of the think\_time\_auto\_correct Parameter" |
| `scale_up_multiplier` | Defines the number of times the query workload is scaled up during replay. Each captured session is replayed concurrently as many times as the value of the `scale_up_multiplier`. However, only one of the sessions in each set of identical replay sessions executes both queries and updates. The remaining sessions only execute queries. |
| `capture_sts` | If this parameter is `TRUE`, then a SQL tuning set capture is also started in parallel with workload replay. The resulting SQL tuning set can be exported using the EXPORT\_AWR Procedure along with the AWR data. Currently, parallel SQL tuning set (STS) capture is not supported in an Oracle RAC environment. So, this parameter has no effect in that context. The calling user must have the appropriate privileges (' `ADMINISTER SQL TUNING SET` '). The default value is `FALSE`. |
| `sts_cap_interval` | Specifies the capture interval of the SQL set capture from the cursor cache in seconds. The default value is 300. |

Usage Notes

- Prerequisites:
	- The database has been initialized for replay using the INITIALIZE\_REPLAY Procedure.
		- Any capture time connection strings that require remapping have been already done using the REMAP\_CONNECTION Procedure.
- One or more external replay clients (WRC) can be started once the `PREPARE_REPLAY` procedure has been executed.
- With regard to scale\_up\_multiplier:
	- One replay session (base session) of each set of identical sessions will replay every call from the capture as usual.
		- The remaining sessions (scale-up sessions) will only replay calls that are read-only. Thus, DDL, DML, and PL/SQL calls that modified the database is skipped. `SELECT` `FOR` `UPDATE` statements are also skipped.
		- Read-only calls from the scale-up are synchronized appropriately and obey the timings defined by `think_time_scale`, `connect_time_scale`, and `think_time_auto_correct`. Also, the queries are made to wait for the appropriate commits.
		- No replay data or error divergence records are generated for the scale-up sessions.
		- All base or scale-up sessions that replay the same capture file will connect from the same workload replay client.

Examples

Application of the connect\_time\_scale Parameter

If the following was observed during the original workload capture:

```
12:00 : Capture was started
12:10 : First session connect  (10m after)
12:30 : Second session connect (30m after)
12:42 : Third session connect  (42m after)
```

If the connect\_time\_scale is 50, then the session connects will happen as follows:

```
12:00 : Replay was started with 50% connect time scale
12:05 : First session connect  ( 5m after)
12:15 : Second session connect (15m after)
12:21 : Third session connect  (21m after)
```

If the connect\_time\_scale is 200, then the session connects will happen as follows:

```
12:00 : Replay was started with 200% connect time scale
12:20 : First session connect  (20m after)
13:00 : Second session connect (60m after)
13:24 : Third session connect  (84m after)
```

Application of the think\_time\_scale Parameter

If the following was observed during the original workload capture:

```
12:00 : User SCOTT connects
12:10 : First user call issued (10m after completion of prevcall)
12:14 : First user call completes in 4mins
12:30 : Second user call issued (16m after completion of prevcall)
12:40 : Second user call completes in 10m
12:42 : Third user call issued ( 2m after completion of prevcall)
12:50 : Third user call completes in 8m
```

If the think\_time\_scale is 50 during the workload replay, then the user calls will look something like below:

```
12:00 : User SCOTT connects
12:05 : First user call issued 5 mins (50% of 10m) after the completion of 
        previous call
12:10 : First user call completes in 5m (takes a minute longer)
12:18 : Second user call issued 8 mins (50% of 16m) after the completion of prev 
        call
12:25 : Second user call completes in 7m (takes 3 minutes less)
12:26 : Third user call issued 1 min  (50% of 2m) after the completion of prev 
        call
12:35 : Third user call completes in 9m (takes a minute longer)
```

Application of the think\_time\_auto\_correct Parameter

If the following was observed during the original workload capture:

```
12:00 : User SCOTT connects
12:10 : First user call issued (10m after completion of prevcall)
12:14 : First user call completes in 4m
12:30 : Second user call issued (16m after completion of prevcall)
12:40 : Second user call completes in 10m
12:42 : Third user call issued ( 2m after completion of prevcall)
12:50 : Third user call completes in 8m
```

If the think\_time\_scale is 100 and the think\_time\_auto\_correct is TRUE during the workload replay, then the user calls will look something like below:

```
12:00 : User SCOTT connects
12:10 : First user call issued 10 mins after the completion of prev call
12:15 : First user call completes in 5m (takes 1 minute longer)
12:30 : Second user call issued 15 mins (16m minus the extra time of 1m the prev 
        call took) after the completion of prev call
12:44 : Second user call completes in 14m (takes 4 minutes longer)
12:44 : Third user call issued immediately (2m minus the extra time of 4m the prev 
        call took) after the completion of prev call
12:52 : Third user call completes in 8m
```

---

### PREPARE\_CONSOLIDATED\_REPLAY Procedure

Similar to the PREPARE\_REPLAY Procedure, this procedure puts the database in a special "Prepare" mode for a multiple-capture replay. The difference is that this subprogram should be used only for consolidated replays.

Syntax

```
DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY (
   synchronization           IN BOOLEAN,
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);

DBMS_WORKLOAD_REPLAY.PREPARE_CONSOLIDATED_REPLAY (
   synchronization           IN VARCHAR2  DEFAULT 'OBJECT_ID',,
   connect_time_scale        IN NUMBER    DEFAULT 100,
   think_time_scale          IN NUMBER    DEFAULT 100,
   think_time_auto_correct   IN BOOLEAN   DEFAULT TRUE,
   capture_sts               IN BOOLEAN   DEFAULT FALSE,
   sts_cap_interval          IN NUMBER    DEFAULT 300);
```

Parameters

Table 161-23 PREPARE\_CONSOLIDATED\_REPLAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `synchronization` | Turns synchronization `ON` or `OFF` during workload replay. When synchronization is `ON`, the `COMMIT` order observed during the original workload capture is preserved during replay. Every action that is replayed is executed `ONLY` `AFTER` all of its dependent `COMMIT` s (all `COMMIT` s that were issued before the given action in the original workload capture) have finished execution. `DEFAULT` is `TRUE` which preserves commit order.  When synchronization is `OBJECT_ID`, a more advanced synchronization scheme is used. Every action that is replayed is executed only after the relevant `COMMIT` s have finished executing. The relevant `COMMIT` s are the ones that were issued before the given action in the original workload capture and that had modified at least one of the database objects the given action is referencing (either implicitly or explicitly). This OBJECT\_ID scheme has the same logical property of making sure that any action will see the same data it saw during capture, but will allow more concurrency during replays for the actions that do not touch the same objects/tables. `DEFAULT VALUE: SCN`, preserve commit order. For legacy reasons, there is a boolean version of this procedure:  - `TRUE` means `'SCN'` - `FALSE` means `'OFF'` |
| `connect_time_scale` | Scales the time elapsed between the instant the workload capture was started and the session connects with the given value. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. `DEFAULT` `VALUE` is 100. See "Application of the connect\_time\_scale Parameter". |
| `think_time_scale` | Scales the time elapsed between two successive user calls from the same session. The input is interpreted as a % value. Can potentially be used to increase or decrease the number of concurrent users during the workload replay. `DEFAULT` `VALUE` is 100. See "Application of the think\_time\_auto\_correct Parameter" |
| `think_time_auto_correct` | Auto corrects the think time between calls appropriately when user calls takes longer to complete during replay than during the original capture. `DEFAULT` is `TRUE` which is to reduce think time if replay goes slower than capture. See "Application of the think\_time\_auto\_correct Parameter" |
| `capture_sts` | If this parameter is `TRUE`, then a SQL tuning set capture is also started in parallel with workload replay. The resulting SQL tuning set can be exported using the EXPORT\_AWR Procedure along with the Automatic Workload Repository (AWR) data. Currently, parallel SQL tuning set (STS) capture is not supported in an Oracle RAC environment. So, this parameter has no effect in that context. The calling user must have the appropriate privileges (' `ADMINISTER SQL TUNING SET` '). The default value is `FALSE`. |
| `sts_cap_interval` | Specifies the capture interval of the SQL set capture from the cursor cache in seconds. The default value is 300. |

Usage Notes

A consolidated replay replays multiple captures in one replay. Each capture records different system change number (SCN) values. For this reason SCN-based sync is not supported for consolidated replays. Consolidated replays only support non-sync mode and the Object-ID based synchronization, and SCN-based synchronization is currently not supported.

---

### PROCESS\_CAPTURE Procedure

This procedure processes the workload capture found in `capture_dir` in place.

Syntax

```
DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE (
   capture_dir            IN   VARCHAR2,
   parallel_level         IN   NUMBER DEFAULT NULL);
```

Parameters

Table 161-24 PROCESS\_CAPTURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `catpure_dir` | (Mandatory) Name of the workload capture directory object (case sensitive). The directory object must point to a valid OS directory that has the appropriate permissions. New files are added to this directory. |
| `parallel_level` | Number of Oracle processes used to process the capture in parallel. The `NULL` default value will auto-compute the parallelism level, whereas a value of 1 will enforce serial execution. |

Usage Notes

- This subprogram analyzes the workload capture found in the `capture_dir` and creates new workload replay specific metadata files that are required to replay the given workload capture. It only creates new files and does not modify any files that were originally created during the workload capture. Therefore, this procedure can be run multiple times on the same capture directory, such as when the procedure encounters unexpected errors or is cancelled by the user.
- Once this procedure runs successfully, the capture\_dir can be used as input to the INITIALIZE\_REPLAY Procedure in order to replay the captured workload present in `capture_dir`.
- Before a workload capture can be replayed in a particular database version, the capture must be processed using `PROCESS_CAPTURE` in the same database version. Once created, a processed workload capture can be used to replay the captured workload multiple times in the same database version.
	For example, suppose workload "foo" was captured in `rec_dir` in Oracle database version 10.2.0.5. In order to replay the workload "foo" in version 11.1.0.1 the workload must be processed in version 11.1.0.1. The following procedure must be executed in an 11.1.0.1 database in order to process the capture directory `rec_dir`:
	```
	DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE('rec_dir');
	```
	Now, `rec_dir` contains a valid 11.1.0.1 processed workload capture that can be used to replay the workload "foo" in 11.1.0.1 databases as many times as required.

---

### REMAP\_CONNECTION Procedure

This procedure remaps the captured connection to a new one so that the user sessions can connect to the database in a desired way during workload replay.

Syntax

```
DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION (
   connection_id         IN  NUMBER,
   replay_connection     IN  VARCHAR2);

DBMS_WORKLOAD_REPLAY.REMAP_CONNECTION (
   capture_number        IN  VARCHAR2,
   connection_id         IN  NUMBER,
   replay_connection     IN  VARCHAR2);
```

Parameters

Table 161-25 REMAP\_CONNECTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `capture_number` | Pointing to a capture of the current replay schedule |
| `connection_id` | ID of the connection to be remapped. Corresponds to `DBA_WORKLOAD_CONNECTION_MAP`.`CONN_ID`. |
| `replay_connection` | New connection string to be used during replay |

Usage Notes

- Prior to calling `REMAP_CONNECTION` all replay connection strings are set to `NULL` by default. If a `replay_connection` is `NULL`, then the replay sessions will connect as determined by the replay client's runtime environment. For example, if the environment variable `TNS_ADMIN` is defined and the user does not call the REMAP\_CONNECTION Procedure, then the `wrc` executable will connect to the server specified in the tnsnames.ora file pointed to by `TNS_ADMIN`.
- A valid `replay_connection` must specify a connect identifier or a service point. See the [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/toc.htm) for ways to specify connect identifiers (such as net service names, database service names, and net service aliases) and naming methods that can be used to resolve a connect identifier to a connect descriptor.
- An error is returned if no row matches the given `connection_id`.
- Use the `DBA_WORKLOAD_CONNECTION_MAP` view to review all the connection strings that are used by the subsequent workload replay, and also to examine connection string remappings used for previous workload replays.

---

### REMOVE\_CAPTURE Procedure

This procedure removes the given capture from the current schedule.

Syntax

```
DBMS_WORKLOAD_REPLAY.REMOVE_CAPTURE (
   schedule_capture_number    IN     NUMBER);
```

Parameters

Table 161-26 REMOVE\_CAPTURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_capture_number` | Unique ID that identifies this capture within this schedule |

---

### REMOVE\_SCHEDULE\_ORDERING Procedure

This procedure removes an existing schedule order from the current replay schedule. Together, `schedule_capture_id` and `waitfor_capture_id` form a schedule ordering that previously added by the ADD\_SCHEDULE\_ORDERING Function (`schedule_capture_id`, `waitfor_capture_id`). The order is that replay of capture indicated by `schedule_capture_id` will not start unless the replay of capture indicated by `waiting_for_capture_id` finishes.

Syntax

```
DBMS_WORKLOAD_REPLAY.REMOVE_SCHEDULE_ORDERING (
   schedule_capture_id     IN         NUMBER,
   waitfor_capture_id      IN         NUMBER);
```

Parameters

Table 161-27 REMOVE\_SCHEDULE\_ORDERING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_capture_id` | Points to a capture that has been added to the current replay schedule (see procedure description). |
| `waitfor_capture_id` | Points to a capture that has been added to the current replay schedule. |

Usage Notes

Prerequisites:

- The BEGIN\_REPLAY\_SCHEDULE Procedure must have been called.
- The replay schedule order should have already been added using the ADD\_SCHEDULE\_ORDERING Function.

---

### REPORT Function

This function generates a report on the stipulated workload replay.

Syntax

```
DBMS_WORKLOAD_REPLAY.REPORT (
   replay_id          IN NUMBER,
   format             IN VARCHAR2)
  RETURN CLOB;
```

Parameters

Table 161-28 REPORT Function Parameters

| Parameter | Description |
| --- | --- |
| `replay_id` | (Mandatory) Specifies the ID of the workload replay whose report is requested. |
| `format` | (Mandatory) Specifies the report format. Valid values:  - HTML - Generates the HTML version of the report - XML - Generates the XML version of the report - TEXT - Generates the text version of the report |

Return Values

The report body in the desired format returned as a `CLOB`

---

### RESUME\_REPLAY Procedure

This procedure resumes a paused workload replay.

Syntax

```
DBMS_WORKLOAD_REPLAY.RESUME_REPLAY;
```

Usage Notes

Prerequisite: A call to the PAUSE\_REPLAY Procedure must have already been issued.

---

### REUSE\_REPLAY\_FILTER\_SET Procedure

This procedure reuses filters in the specified filter set as if each were added using the ADD\_SCHEDULE\_ORDERING Function. Each call adds one filter set, which is a collection of individual filters on various attributes. Also, a new filter rule can be added, and an existing filter can be deleted before invoking the CREATE\_FILTER\_SET Procedure to create a new filter set.

Syntax

```
DBMS_WORKLOAD_REPLAY.REUSE_REPLAY_FILTER_SET( 
   replay_dir  IN VARCHAR2,
   filter_set  IN VARCHAR2);
```

Parameters

Table 161-29 REUSE\_REPLAY\_FILTER\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_dir` | Capture ID of the existing filter set with which it is associated |
| `filter_set` | Name of the filter set to be reused |

---

### SET\_ADVANCED\_PARAMETER Procedure

This procedure sets an advanced parameter for replay besides the ones used with the PREPARE\_REPLAY Procedure. The advanced parameters control aspects of the replay that are more specialized. The advanced parameters are reset to their default values after the replay has finished.

Syntax

```
DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   VARCHAR2);

DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   NUMBER);

DBMS_WORKLOAD_REPLAY.SET_ADVANCED_PARAMETER( 
   pname    IN   VARCHAR2,
   pvalue   IN   BOOLEAN);
```

Parameters

Table 161-30 SET\_ADVANCED\_PARAMETER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Name of the parameter (case insensitive) |
| `pvalue` | Value of the parameter |

Usage Notes

The current parameters and values that can be used are:

```
'DO_NO_WAIT_COMMITS': (default: FALSE)
```

This parameter controls whether the `COMMIT` s issued by replay sessions is `NOWAIT`. The default value for this parameter is `FALSE`. In this case all the `COMMIT` s are issued with the mode they were captured (`wait`, `no-wait`, `batch`, `no-batch`). If the parameter is set to `TRUE`, then all `COMMIT` s are issued in `no-wait` mode. This is useful in cases where the replay is becoming noticeably slow because of a high volume of concurrent `COMMIT` s. Setting the parameter to `TRUE` will significantly decrease the waits on the `'log file sync'` event during the replay with respect to capture.

---

### SET\_REPLAY\_DIRECTORY Procedure

This procedure sets a directory that contains multiple workload captures as the current replay directory.

Syntax

```
DBMS_WORKLOAD_REPLAY.SET_REPLAY_DIRECTORY (
   replay_dir    IN    VARCHAR2);
```

Parameters

Table 161-31 SET\_REPLAY\_DIRECTORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `replay_dir` | Name of the OS directory containing the captures for a workload consolidation |

---

### SET\_REPLAY\_TIMEOUT Procedure

This procedure sets the replay timeout setting. The purpose is to abort user calls that might make the replay much slower or even cause a replay hang.

Syntax

```
DBMS_WORKLOAD_REPLAY.SET_REPLAY_TIMEOUT (
   enabled       OUT  BOOLEAN DEFAULT TRUE, 
   min_delay     OUT  NUMBER DEFAULT 10,
   max_delay     OUT  NUMBER DEFAULT 120,
   delay_factor  OUT  NUMBER DEFAULT 8);
```

Parameters

Table 161-32 SET\_REPLAY\_TIMEOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `enabled` | `TRUE` to enable the timeout action, and `FALSE` to disable. |
| `min_delay` | Lower bound of call delay in minutes. The replay action is activated only when the delay is equal to or more than `min_delay`. Default = 10. |
| `max_delay` | Upper bound of call delay in minutes. The timeout action throws `ORA-15569` when the delay is more than `max_delay`. Default = 120. |
| `delay_factor` | Factor for the call delay that is between `min_delay` and `max_delay`. The timeout action throws `ORA-15569` when the current replay elapsed time is more than the product of capture elapsed time and `delay_factor`. Default = 8. |

Usage Notes

- This procedure can be called anytime during replay.
- Call delay is defined as the difference between replay and capture if replay elapsed time is longer than call elapsed time.
- Once a replay timeout action is enabled, a user call will exit with `ORA-15569` if it has been delayed more than the condition specified by the replay action. The call and its error are reported as error divergence.
- Replay timeout operates as follows:
	- The timeout action has no effect if it is not enabled.
		- If the call delay in minutes is less than a lower bound specified by parameter `min_delay`, then the timeout action is non-operational.
		- If the delay in minutes is more than a upper bound specified by parameter `max_delay`, the timeout action will abort the user call and throw `ORA-15569`.
		- For delay that is between the lower bound and upper bound, the user call will abort with `ORA-15569` only when the current replay elapsed time is more than the product of capture elapsed time and parameter `delay_factor`.

---

### SET\_USER\_MAPPING Procedure

This procedure sets a new schema or user name to be used during replay instead of the captured user.

Syntax

```
DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING (
   schedule_cap_id      IN NUMBER,
   capture_user         IN VARCHAR2,
   replay_user          IN VARCHAR2);

DBMS_WORKLOAD_REPLAY.SET_USER_MAPPING (
   capture_user         IN VARCHAR2,
   replay_user          IN VARCHAR2);
```

Parameters

Table 161-33 SET\_USER\_MAPPING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_cap_id` | ID of the a capture in the schedule |
| `capture_user` | User name during the time of the workload capture |
| `replay_user` | User name to which captured user is remapped during replay. |

Usage Notes

- A `schedule_cap_id` of `NULL` is used for regular non-consolidate replay.
- The replay must be initialized but not prepared in order to use this subprogram.
- If `replay_user` is set to `NULL`, then the mapping is disabled.
- After multiple calls with the same `capture_user`, the last call always takes effect.
- To list all the mappings that will be in effect during the subsequent replay execute the following:
	```
	SELECT * FROM DBA_WORKLOAD_ACTIVE_USER_MAP
	```
- The overloaded version without the `schedule_cap_id` calls the one with the `schedule_cap_id` argument by passing in `NULL`.
- Mappings are stored in a table made public through the view `DBA_WORKLOAD_USER_MAP`. To remove old mappings execute
	```
	DELETE * FROM DBA_WORKLOAD_USER_MAP
	```

---

### START\_CONSOLIDATED\_REPLAY Procedure

This procedure starts the replay of a multiple-capture capture. It should be used only for consolidated replays.

Syntax

```
DBMS_WORKLOAD_REPLAY.START_CONSOLIDATED_REPLAY;
```

Usage Notes

Prerequisites:

- The call to the PREPARE\_REPLAY Procedure was already issued.
- A sufficient number of external replay clients (WRC) that can faithfully replay the captured workload already started. The status of such external replay clients can be monitored using `V$WORKLOAD_REPLAY_CLIENTS`.

---

### START\_REPLAY Procedure

This procedure starts the workload replay. All the external replay clients (WRC) that are currently connected to the replay database will automatically be notified, and those replay clients (WRC) will begin issuing the captured workload. It should only be used for consolidated replays.

Syntax

```
DBMS_WORKLOAD_REPLAY.START_REPLAY;
```

Usage Notes

- Prerequisites:
	- The call to the PREPARE\_REPLAY Procedure was already issued.
		- A sufficient number of external replay clients (WRC) that can faithfully replay the captured workload already started. The status of such external replay clients can be monitored using `V$WORKLOAD_REPLAY_CLIENTS`.
- Use the WRC's `CALIBRATE` mode to determine the number of replay clients that might be required to faithfully replay the captured workload. For example:
	```
	$ wrc mode=calibrate replaydir=.
	```

---

### USE\_FILTER\_SET Procedure

This procedure applies a filter set to a capture in the current replay schedule. The filter set must have been created by calling the CREATE\_FILTER\_SET Procedure.

Syntax

```
DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( 
   capture_number   IN    VARCHAR2,
   filter_set       IN    VARCHAR2);

DBMS_WORKLOAD_REPLAY.USE_FILTER_SET( 
   filter_set       IN    VARCHAR2);
```

Parameters

Table 161-34 USE\_FILTER\_SET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `capture_number` | Pointing to a capture of the current replay schedule |
| `filter_set` | Name of the filter set |

Usage Notes

The filter set must have been created by calling the CREATE\_FILTER\_SET Procedure.
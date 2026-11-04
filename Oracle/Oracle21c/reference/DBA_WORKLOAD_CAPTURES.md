---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_CAPTURES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.118 DBA\_WORKLOAD\_CAPTURES

`DBA_WORKLOAD_CAPTURES` displays all the workload captures that have been performed in the current database.

It also lists captures on which `DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO()` or `DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO()` have been called. Each row contains information about one workload capture.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` | `NOT NULL` | Internal key for the workload capture |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name for the workload capture |
| `DBID` | `NUMBER` | `NOT NULL` | ID of the database in which the workload was captured |
| `DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the database in which the workload was captured |
| `DBVERSION` | `VARCHAR2(17)` | `NOT NULL` | Version of the database in which the workload was captured |
| `PARALLEL` | `VARCHAR2(3)` |  | Indicates whether the database in which the workload was captured is an Oracle RAC database (`YES`) or a single instance database (`NO`) |
| `DIRECTORY` | `VARCHAR2(128)` | `NOT NULL` | Name of the directory object for workload capture |
| `STATUS` | `VARCHAR2(40)` | `NOT NULL` | Current status of the workload capture:  - `IN PROGRESS` - Workload capture is in progress - `COMPLETED` - Workload capture has completed successfully - `FAILED` - Workload capture was terminated due to errors encountered |
| `START_TIME` | `DATE` | `NOT NULL` | Datetime when the capture began |
| `END_TIME` | `DATE` |  | Datetime when the capture completed or failed; NULL if the capture is still in progress |
| `DURATION_SECS` | `NUMBER` |  | Duration of the workload capture (in seconds) |
| `START_SCN` | `NUMBER` | `NOT NULL` | Start SCN value for this capture |
| `END_SCN` | `NUMBER` |  | End SCN value for this capture; NULL if the capture is still in progress |
| `DEFAULT_ACTION` | `VARCHAR2(30)` | `NOT NULL` | Mode in which to apply workload capture filters:  - `INCLUDE` - All the capture filters are treated as EXCLUSION filters, determining the workload that will not be captured. - `EXCLUDE` - All the capture filters are treated as INCLUSION FILTERS, determining the workload that will be captured. |
| `FILTERS_USED` | `NUMBER` |  | Number of filters that were used for this capture |
| `CAPTURE_SIZE` | `NUMBER` |  | Total size of workload capture |
| `DBTIME` | `NUMBER` |  | Total amount of database time (in microseconds) that has been recorded in this workload capture |
| `DBTIME_TOTAL` | `NUMBER` |  | Total amount of database time (in microseconds) across the entire database during the workload capture, including the part of the workload that was not captured. |
| `USER_CALLS` | `NUMBER` |  | Total number of user calls that have been recorded in this workload capture |
| `USER_CALLS_TOTAL` | `NUMBER` |  | Total number of user calls across the entire database during the workload capture, including the part of the workload that was not captured. |
| `USER_CALLS_UNREPLAYABLE` | `NUMBER` |  | Total number of user calls that will not be replayed in a subsequent replay of this workload capture |
| `PLSQL_SUBCALL_SIZE` | `NUMBER` |  | Total size of workload capture for SQL executed from PL/SQL |
| `PLSQL_CALLS` | `NUMBER` |  | Total number of PL/SQL calls recorded in the workload capture |
| `PLSQL_SUBCALLS` | `NUMBER` |  | Total number of calls recorded in the workload capture for SQL executed from PL/SQL |
| `PLSQL_DBTIME` | `NUMBER` |  | Total amount of database time (in microseconds) from PL/SQL calls that have been recorded in the workload capture |
| `TRANSACTIONS` | `NUMBER` |  | Total number of transactions that have been recorded in this workload capture |
| `TRANSACTIONS_TOTAL` | `NUMBER` |  | Total number of transactions across the entire database during the workload capture, including the part of the workload that was not captured. |
| `CONNECTS` | `NUMBER` |  | Total number of session connects that have been recorded in this workload capture |
| `CONNECTS_TOTAL` | `NUMBER` |  | Total number of session connects across the entire database during the workload capture, including the part of the workload that was not captured |
| `ERRORS` | `NUMBER` |  | Total number of errors that have been recorded in this workload capture |
| `AWR_DBID` | `NUMBER` |  | Database ID of the AWR snapshots that correspond to this workload capture. For captures that were performed in the current database, this value is equal to the current database's DBID. For captures that were performed in other databases, this value will either be NULL or will be populated by `DBMS_WORKLOAD_CAPTURE.IMPORT_AWR()`. |
| `AWR_BEGIN_SNAP` | `NUMBER` |  | Begin snapshot ID of the AWR snapshots that correspond to this workload capture |
| `AWR_END_SNAP` | `NUMBER` |  | End snapshot ID of the AWR snapshots that correspond to this workload capture |
| `AWR_EXPORTED` | `VARCHAR2(12)` |  | Indicates whether the AWR snapshots that correspond to this workload capture have been exported using `DBMS_WORKLOAD_CAPTURE.EXPORT_AWR()` (`YES`) or not (`NO`), or whether AWR snapshots cannot be exported because the capture is still in progress, has run to completion successfully, or was done in a different database from which it was not exported (`NOT POSSIBLE`) |
| `ERROR_CODE` | `NUMBER` |  | Error code for this workload capture |
| `ERROR_MESSAGE` | `VARCHAR2(512)` |  | Error message for this workload capture |
| `DIR_PATH` | `VARCHAR2(4000)` | `NOT NULL` | Full directory path for the workload capture directory object |
| `DIR_PATH_SHARED` | `VARCHAR2(10)` | `NOT NULL` | Indicates whether the workload capture directory is shared by all the instances of the recording database (applicable only for Oracle RAC databases) |
| `LAST_PROCESSED_VERSION` | `VARCHAR2(128)` |  | Database version in which this capture was preprocessed using `DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE()` last; NULL if the capture has never been preprocessed |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of the SQL tuning set owner |
| `SQLSET_NAME` | `VARCHAR2(128)` |  | Name of the SQL tuning set for this workload capture |
| `PLSQL_MODE` | `VARCHAR2(12)` |  | Capture options for PL/SQL calls. Possible values:  - `TOP_LEVEL`: Top-level PL/SQL only - `EXTENDED`: Both top-level PL/SQL and SQL executed from PL/SQL |
| `ENCRYPTION` | `VARCHAR2(128)` |  | Indicates the encryption standard used for the given capture:  - NULL - Capture files are not encrypted - `AES128` – Capture files are encrypted using AES128 - `AES192` – Capture files are encrypted using AES192 - `AES256` – Capture files are encrypted using AES256 |
| `ENCRYPTION_VERIFIER` | `RAW(512)` |  | Data used internally for creating an encrypted capture |
| `PATCH_NAME` | `VARCHAR2(128)` |  | Database workload capture and replay patch name  This column is populated only for backports to Oracle Database 12c Release 1 (12.1) and earlier releases. |
| `STORAGE_TYPE` | `NUMBER(38)` |  | Describes where the captured workload is stored |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS207) for more information about the `DBMS_WORKLOAD_CAPTURE` package
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS208) for more information about the `DBMS_WORKLOAD_REPLAY` package
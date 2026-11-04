---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RMAN_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.182 V$RMAN\_STATUS

For on-going jobs, this view displays progress and status. The jobs which are in progress are stored only in memory while the finished jobs are stored in the controlfile.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the session which is running this RMAN operation |
| `RECID` | `NUMBER` | Record ID of the row in the controlfile |
| `STAMP` | `NUMBER` | Timestamp of the row (`RECID` + `STAMP` is unique) |
| `PARENT_RECID` | `NUMBER` | Record ID of the parent row of this row (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `ROW_LEVEL` - `1`) |
| `PARENT_STAMP` | `NUMBER` | Timestamp of the parent row of this row (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `ROW_LEVEL` - `1`) |
| `SESSION_RECID` | `NUMBER` | Record ID of the session (corresponding V$RMAN\_STATUS row with `ROW_LEVEL` = `0`) |
| `SESSION_STAMP` | `NUMBER` | Timestamp of the session (corresponding V$RMAN\_STATUS row with `ROW_LEVEL` = `0`) |
| `ROW_LEVEL` | `NUMBER` | Level of the row. The session has level `0`. |
| `ROW_TYPE` | `VARCHAR2(19)` | Type of the row:  - `SESSION` - `COMMAND` - `RECURSIVE OPERATION` |
| `COMMAND_ID` | `VARCHAR2(33)` | Command ID set by the RMAN `SET COMMAND ID` command. If not set, then RMAN will create a unique number. |
| `OPERATION` | `VARCHAR2(33)` | Name of the command in the execution explained by this row |
| `STATUS` | `VARCHAR2(23)` | Status of the operation:  - `RUNNING` - `RUNNING WITH WARNINGS` - `RUNNING WITH ERRORS` - `COMPLETED` - `COMPLETED WITH WARNINGS` - `COMPLETED WITH ERRORS` - `FAILED` |
| `MBYTES_PROCESSED` | `NUMBER` | Percentage of the job completed; null if not applicable for the operation |
| `START_TIME` | `DATE` | Start time of the job |
| `END_TIME` | `DATE` | End time of the job |
| `INPUT_BYTES` | `NUMBER` | Number of input bytes read |
| `OUTPUT_BYTES` | `NUMBER` | Number of output bytes written |
| `OPTIMIZED` | `VARCHAR2(3)` | YES, if backup optimization was applied during the backup job. Otherwise, NO. |
| `OBJECT_TYPE` | `VARCHAR2(13)` | Identifies types of objects backed up |
| `OUTPUT_DEVICE_TYPE` | `VARCHAR2(17)` | `DISK`, `SBT_TAPE`, or `*`. An `*` indicates that output was written to more than one device type. |
| `OSB_ALLOCATED` | `VARCHAR2(3)` | A value of `YES` means an Oracle Secure Backup channel was allocated during the specified operation identified by the `V$RMAN_STATUS` view. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-STANDBY_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.81 V$STANDBY\_LOG

Standby redo logs are similar to online redo logs, but standby redo logs are only used on a standby database that is receiving redo data from the primary database.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Log group number |
| `DBID` | `VARCHAR2(40)` | Database ID of the primary database to which the standby redo logfile is assigned. If the standby redo logfile is unassigned, the value `UNASSIGNED` will be displayed. |
| `THREAD#` | `NUMBER` | Log thread number |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `BYTES` | `NUMBER` | Size of the log (in bytes) |
| `BLOCKSIZE` | `NUMBER` | Block size of the logfile (512 or 4096) |
| `USED` | `NUMBER` | Number of bytes used in the log |
| `ARCHIVED` | `VARCHAR2(3)` | Archive status (`YES`) or (`NO`). See the `STATUS` column for further details. |
| `STATUS` | `VARCHAR2(10)` | Log status:  - `UNASSIGNED` - If `ARCHIVED` is `NO`, then the standby redo log has been archived and is again available. If `ARCHIVED` is `YES`, then the standby redo log has never been used and is available. - `ACTIVE` - If `ARCHIVED` is `NO`, then the standby redo log is complete and waiting to be archived. If `ARCHIVED` is `YES`, then the standby redo log is currently being written to and is therefore not ready to be archived. For a given thread, there should be only one such log. |
| `FIRST_CHANGE#` | `NUMBER` | Lowest SCN in the log |
| `FIRST_TIME` | `DATE` | Time of the first SCN in the log |
| `NEXT_CHANGE#` | `NUMBER` | All redo records contained within this log will have an SCN lower than `NEXT_CHANGE#`. Only filled in once the log is complete. Also the lowest SCN of any redo record in the next log. |
| `NEXT_TIME` | `DATE` | All redo records contained within this log will have a timestamp lower than `NEXT_TIME`. Only filled in once the log is complete. Also the lowest timestamp of any redo record in the next log. |
| `LAST_CHANGE#` | `NUMBER` | Redo in the standby redo log that recovery can possibly apply from the log has an SCN lower than `LAST_CHANGE#` |
| `LAST_TIME` | `DATE` | Timestamp of `LAST_CHANGE#` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
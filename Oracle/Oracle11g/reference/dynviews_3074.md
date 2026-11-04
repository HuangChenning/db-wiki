---
title: "V$STANDBY_LOG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3074.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$STANDBY_LOG` displays information about standby redo logs. Standby redo logs are similar to online redo logs, but standby redo logs are only used on a standby database that is receiving redo data from the primary database.

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
| `STATUS` | `VARCHAR2(10)` | Log status: - `UNASSIGNED` - If `ARCHIVED` is `NO`, then the standby redo log has been archived and is again available. If `ARCHIVED` is `YES`, then the standby redo log has never been used and is available. - `ACTIVE` - If `ARCHIVED` is `NO`, then the standby redo log is complete and waiting to be archived. If `ARCHIVED` is `YES`, then the standby redo log is currently being written to and is therefore not ready to be archived. For a given thread, there should be only one such log. |
| `FIRST_CHANGE#` | `NUMBER` | Lowest SCN in the log |
| `FIRST_TIME` | `DATE` | Time of the first SCN in the log |
| `NEXT_CHANGE#` | `NUMBER` | All redo records contained within this log will have an SCN lower than `NEXT_CHANGE#`. Only filled in once the log is complete. Also the lowest SCN of any redo record in the next log. |
| `NEXT_TIME` | `DATE` | All redo records contained within this log will have a timestamp lower than `NEXT_TIME`. Only filled in once the log is complete. Also the lowest timestamp of any redo record in the next log. |
| `LAST_CHANGE#` | `NUMBER` | Last change number made to this datafile. Set to `NULL` if the datafile is being changed. |
| `LAST_TIME` | `DATE` | Timestamp of the last change |
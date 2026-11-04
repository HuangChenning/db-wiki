---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_SESS_TIME_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_SESS_TIME_STATS` displays information about CPU and I/O time for interesting Streams sessions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SESSION_TYPE` | `VARCHAR2(64)` | `NOT NULL` | Type of session |
| `MIN_LOGON_TIME` | `DATE` |  | Minimum logon time |
| `SUM_CPU_TIME` | `NUMBER` |  | Total CPU time |
| `SUM_SYS_IO_WAIT` | `NUMBER` |  | Total system I/O wait time |
| `SUM_USER_IO_WAIT` | `NUMBER` |  | Total user I/O wait time |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `SESSION_MODULE` | `VARCHAR2(64)` | `NOT NULL` | Session module. Valid values:  - Streams - XStream - GoldenGate |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
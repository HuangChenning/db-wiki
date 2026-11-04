---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ROLLING_DATABASES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ROLLING_DATABASES` lists all the databases eligible for configuration with rolling operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RDBID` | `NUMBER` |  | Rolling operation database identifier |
| `DBID` | `NUMBER` |  | Oracle database identifier |
| `DBUN` | `VARCHAR2(128)` |  | Database unique name |
| `ROLE` | `VARCHAR2(8)` |  | Database role |
| `OPEN_MODE` | `VARCHAR2(15)` |  | Open mode information |
| `PARTICIPANT` | `VARCHAR2(3)` |  | Indicates whether the database is participating in the rolling operation (`YES`) or not (`NO`) |
| `VERSION` | `VARCHAR2(128)` |  | RDBMS version number |
| `ENGINE_STATUS` | `VARCHAR2(14)` |  | Running status of the MRP-recovery or LSP-apply process |
| `RAC` | `VARCHAR2(3)` |  | Indicates whether the database is an Oracle Real Application Clusters (Oracle RAC) database |
| `UPDATE_PROGRESS` | `VARCHAR2(11)` |  | Upgrade status of the system catalog |
| `PROD_RSCN` | `VARCHAR(40)` |  | Resetlogs SCN at which redo is currently being produced |
| `PROD_RID` | `VARCHAR(40)` |  | Resetlogs ID at which redo is currently being produced |
| `PROD_SCN` | `VARCHAR(40)` |  | Last SCN at which redo was produced |
| `REDO_SOURCE` | `VARCHAR2(128)` |  | Database unique name of the producer of redo being consumed |
| `CONS_RSCN` | `VARCHAR(40)` |  | Resetlogs SCN at which redo is currently being consumed |
| `CONS_RID` | `VARCHAR(40)` |  | Resetlogs ID at which redo is currently being consumed |
| `CONS_SCN` | `VARCHAR(40)` |  | Last SCN at which redo was consumed |
| `UPDATE_TIME` | `TIMESTAMP(6)` |  | Time of the last record update |

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB5214) for more information about rolling operations.
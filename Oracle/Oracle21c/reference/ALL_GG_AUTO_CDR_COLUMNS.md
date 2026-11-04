---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_GG_AUTO_CDR_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.198 ALL\_GG\_AUTO\_CDR\_COLUMNS

`ALL_GG_AUTO_CDR_COLUMNS` provides details about Oracle GoldenGate automatic conflict detection and resolution (CDR) columns owned by the current user.

Related View

`DBA_GG_AUTO_CDR_COLUMNS` provides details about all of the Oracle GoldenGate automatic CDR columns in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table name |
| `COLUMN_GROUP_NAME` | `VARCHAR2(128)` |  | Column group name |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Column name |
| `RESOLUTION_COLUMN` | `VARCHAR2(128)` |  | Timestamp resolution column |

See Also:

" [DBA\_GG\_AUTO\_CDR\_COLUMNS](DBA_GG_AUTO_CDR_COLUMNS.md) "
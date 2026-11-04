---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_GG_AUTO_CDR_COLUMN_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.197 ALL\_GG\_AUTO\_CDR\_COLUMN\_GROUPS

`ALL_GG_AUTO_CDR_COLUMN_GROUPS` provides details about Oracle GoldenGate automatic conflict detection and resolution (CDR) column groups owned by the current user.

Related View

`DBA_GG_AUTO_CDR_COLUMN_GROUPS` provides details about all of the Oracle GoldenGate automatic CDR column groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name |
| `COLUMN_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column group name |
| `RESOLUTION_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Timestamp resolution column |

See Also:

" [DBA\_GG\_AUTO\_CDR\_COLUMN\_GROUPS](DBA_GG_AUTO_CDR_COLUMN_GROUPS.md) "
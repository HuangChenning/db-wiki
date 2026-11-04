---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_GG_AUTO_CDR_COLUMN_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_GG_AUTO_CDR_COLUMN_GROUPS` provides details about Oracle GoldenGate automatic conflict detection and resolution (CDR) column groups owned by the current user.

Related View

`DBA_GG_AUTO_CDR_COLUMN_GROUPS` provides details about all of the Oracle GoldenGate automatic CDR column groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name |
| `COLUMN_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column group name |
| `RESOLUTION_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Timestamp resolution column |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_GG\_AUTO\_CDR\_COLUMN\_GROUPS](DBA_GG_AUTO_CDR_COLUMN_GROUPS.md) "
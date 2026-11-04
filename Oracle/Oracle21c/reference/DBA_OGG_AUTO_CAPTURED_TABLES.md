---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_OGG_AUTO_CAPTURED_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.215 DBA\_OGG\_AUTO\_CAPTURED\_TABLES

`DBA_OGG_AUTO_CAPTURED_TABLES` describes all tables in the database that are enabled for Oracle GoldenGate automatic capture.

Related View

`USER_OGG_AUTO_CAPTURED_TABLES` describes the tables owned by the current user that are enabled for Oracle GoldenGate automatic capture. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `ALLOW_NOVALIDATE_PK` | `VARCHAR2(3)` |  | Indicates whether a primary key constraint in `NOVALIDATE` mode can be used as a unique identifier for the table (`YES`) or not (`NO`) |

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [USER\_OGG\_AUTO\_CAPTURED\_TABLES](USER_OGG_AUTO_CAPTURED_TABLES.md) "
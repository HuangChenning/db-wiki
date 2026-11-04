---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_APPLY_TABLE_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.79 ALL\_APPLY\_TABLE\_COLUMNS

`ALL_APPLY_TABLE_COLUMNS` displays, for the tables accessible to the current user, information about the nonkey table columns for which apply process conflict detection has been stopped for update and delete operations.

Conflict detection for nonkey columns can be stopped using the `DBMS_APPLY_ADM.COMPARE_OLD_VALUES` procedure.

Related View

`DBA_APPLY_TABLE_COLUMNS` displays, for all tables in the database, information about the nonkey table columns for which apply process conflict detection has been stopped for update and delete operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `COMPARE_OLD_ON_DELETE` | `VARCHAR2(3)` |  | Indicates whether to Compare the old value of the column on deletes (`YES`) or not (`NO`) |
| `COMPARE_OLD_ON_UPDATE` | `VARCHAR2(3)` |  | Indicates whether to Compare the old value of the column on updates (`YES`) or not (`NO`) |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | For remote tables, name of the database link pointing to the remote database |

See Also:

- " [DBA\_APPLY\_TABLE\_COLUMNS](DBA_APPLY_TABLE_COLUMNS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS526) for more information about the `DBMS_APPLY_ADM.COMPARE_OLD_VALUES` procedure
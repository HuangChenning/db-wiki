---
title: ALL_APPLY_TABLE_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1015.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_TABLE_COLUMNS` displays, for the tables accessible to the current user, information about the nonkey table columns for which Oracle Streams apply processes do not detect conflicts for updates and deletes.

Conflict detection for nonkey columns can be stopped using the `DBMS_APPLY_ADM.COMPARE_OLD_VALUES` procedure.

Related View

`DBA_APPLY_TABLE_COLUMNS` displays, for all tables in the database, information about the nonkey table columns for which Oracle Streams apply processes do not detect conflicts for updates and deletes.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `COMPARE_OLD_ON_DELETE` | `VARCHAR2(3)` |  | Indicates whether to Compare the old value of the column on deletes (`YES`) or not (`NO`) |
| `COMPARE_OLD_ON_UPDATE` | `VARCHAR2(3)` |  | Indicates whether to Compare the old value of the column on updates (`YES`) or not (`NO`) |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | For remote tables, name of the database link pointing to the remote database |

See Also:

["DBA\_APPLY\_TABLE\_COLUMNS"](statviews_3063.md)
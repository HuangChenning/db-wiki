---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_UPDATABLE_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.136 ALL\_UPDATABLE\_COLUMNS

`ALL_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the current user, subject to appropriate privileges.

Related Views

- `DBA_UPDATABLE_COLUMNS` describes all columns in a join view that are updatable by the database administrator, subject to appropriate privileges.
- `USER_UPDATABLE_COLUMNS` describes all columns owned by the current user that are in a join view and are updatable by the current user, subject to appropriate privileges.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name |
| `UPDATABLE` | `VARCHAR2(3)` |  | Indicates whether the column is updatable (`YES`) or not (`NO`) <sup>Foot 1</sup> |
| `INSERTABLE ` | `VARCHAR2(3)` |  | Indicates whether the column is insertable (`YES`) or not (`NO`) |
| `DELETABLE` | `VARCHAR2(3)` |  | Indicates whether the column is deletable (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> Starting with Oracle Database 21c, there is a circumstance under which a column is updatable even if its `UPDATABLE` value is `NO` in this view. A column with a `NO` value can be updated if it is in a non-key-preserved table, the `UPDATE` operation updates only columns in that table, and the update is deterministic, that is, it updates each row only once. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT-GUID-8C983FA8-0E9B-4D2B-B819-28FD7F45F1FA) for more information.

Note:

The values shown in the `UPDATABLE`, `INSERTABLE`, and `DELETABLE` columns are not instantly updated when a DDL operation that would affect these attributes occurs on one of the tables referenced in the `FROM` clause of the view definition. For example, these columns are not instantly updated when a primary key or unique constraint is added to or removed from the non-key-preserved table. To remedy this situation, recompile the view using the `ALTER` `VIEW` `COMPILE` statement to ensure that the latest information is displayed.

See Also:

- " [DBA\_UPDATABLE\_COLUMNS](DBA_UPDATABLE_COLUMNS.md) "
- " [USER\_UPDATABLE\_COLUMNS](USER_UPDATABLE_COLUMNS.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1151) for information on updatable join views
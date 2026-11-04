---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_JOINGROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.138 DBA\_JOINGROUPS

`DBA_JOINGROUPS` describes join groups in the database. A join group is a user-created object that consists of two or more columns that can be meaningfully joined. The maximum number of columns that can be included in a join group is 255.

In certain queries, join groups enable the database to eliminate the performance overhead of decompressing and hashing column values. Join groups require an In-Memory column store (IM column store).

Related View

`USER_JOINGROUPS` describes join groups belonging to the user. This view does not display the `JOINGROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOINGROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Join group owner. This is the user that created the join group. |
| `JOINGROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | This is the user specified name of the join group. The join group name is specified when the join group is created as part of the `CREATE INMEMORY JOIN GROUP` statement. |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Table owner |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Column name |
| `FLAGS` | `VARCHAR2(6)` |  | Possible values:  - `MASTER`: Indicates which column in the join group is mastering the global dictionary. A join group is a group of columns sharing a global dictionary; the global dictionary is associated with one column and the other columns share the same dictionary. The column with which the global dictionary is associated is called the mastering column. - NULL: Indicates that the column is not mastering the global dictionary. |
| `GD_ADDRESS` | `RAW(8)` |  | The memory address of the global dictionary. Ideally, all the columns in one join group should have the same global dictionary address (that is, they share the same global structure). This might not always be the case (for example, a column might be added to a join group after it was populated into memory - in which case its `GD_ADDRESS` field will be NULL). In such cases, you should force re-populate the tables that are part of the join group and check the views after the repopulates complete. |

See Also:

- " [USER\_JOINGROUPS](USER_JOINGROUPS.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-3E5491C4-B345-4A8E-8B1B-8DC150C8A797) for an introduction to join groups
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-87CA7034-4F80-4D46-8EE1-5CC865C2D676) for information about creating a join group using the `CREATE INMEMORY JOIN GROUP` statement
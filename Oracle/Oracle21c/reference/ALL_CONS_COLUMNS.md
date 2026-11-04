---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CONS_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.138 ALL\_CONS\_COLUMNS

`ALL_CONS_COLUMNS` describes columns that are accessible to the current user and that are specified in constraints.

Related Views

- `DBA_CONS_COLUMNS` describes all columns in the database that are specified in constraints.
- `USER_CONS_COLUMNS` describes columns that are owned by the current user and that are specified in constraints.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the constraint definition |
| `CONSTRAINT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the constraint definition |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table with the constraint definition |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column or attribute of the object type column specified in the constraint definition  If you create a constraint on a user-defined `REF` column, the system creates the constraint on the attributes that make up the REF column. Therefore, the column names displayed in this view are the attribute names, with the `REF` column name as a prefix, in the following form: ``` "REF_name"."attribute" ``` |
| `POSITION` | `NUMBER` |  | Original position of the column or attribute in the definition of the object |

See Also:

- " [DBA\_CONS\_COLUMNS](DBA_CONS_COLUMNS.md) "
- " [USER\_CONS\_COLUMNS](USER_CONS_COLUMNS.md) "
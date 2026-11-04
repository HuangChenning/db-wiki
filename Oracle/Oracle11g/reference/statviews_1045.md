---
title: ALL_CONS_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1045.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CONS_COLUMNS` describes columns that are accessible to the current user and that are specified in constraints.

Related Views

- `DBA_CONS_COLUMNS` describes all columns in the database that are specified in constraints.
- `USER_CONS_COLUMNS` describes columns that are owned by the current user and that are specified in constraints.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the constraint definition |
| `CONSTRAINT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the constraint definition |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table with the constraint definition |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column or attribute of the object type column specified in the constraint definition |
|  |  |  | Note: If you create a constraint on a user-defined `REF` column, the system creates the constraint on the attributes that make up the REF column. Therefore, the column names displayed in this view are the attribute names, with the `REF` column name as a prefix, in the following form:  `"REF_name"."attribute"` |
| `POSITION` | `NUMBER` |  | Original position of the column or attribute in the definition of the object |
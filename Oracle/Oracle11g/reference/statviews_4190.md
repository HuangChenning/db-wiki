---
title: DBA_PUBLISHED_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4190.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_PUBLISHED_COLUMNS` describes all source table columns in the database which have been published for the source tables. This view is intended for use by Change Data Capture publishers.

Related View

`USER_PUBLISHED_COLUMNS` describes the source table columns owned by the current user which have been published for the source tables. This view does not display the `CHANGE_TABLE_SCHEMA` or `CHANGE_TABLE_NAME` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CHANGE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change set |
| `CHANGE_TABLE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Associated change table owner |
| `CHANGE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Associated change table name |
| `PUB_ID` | `NUMBER` | `NOT NULL` | Publication identifier |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Table owner in the source database |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Table name in the source database |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Column name |
| `DATA_TYPE` | `VARCHAR2(106)` |  | Column datatype |
| `DATA_LENGTH` | `NUMBER` | `NOT NULL` | Column length (in bytes) |
| `DATA_PRECISION` | `NUMBER` |  | Decimal precision for `NUMBER` datatypes; binary precision for `FLOAT` datatypes; NULL for all other datatypes |
| `DATA_SCALE` | `NUMBER` |  | Digits to the right of a decimal point in a number |
| `NULLABLE` | `VARCHAR2(1)` |  | Indicates whether NULLs are allowed (`Y`) or not (`N`) |

See Also:

["USER\_PUBLISHED\_COLUMNS"](statviews_5402.md)
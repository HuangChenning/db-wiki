---
title: ALL_IND_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1103.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_IND_COLUMNS` describes the columns of indexes on all tables accessible to the current user.

Related Views

- `DBA_IND_COLUMNS` describes the columns of indexes on all tables in the database.
- `USER_IND_COLUMNS` describes the columns of indexes owned by the current user and columns of indexes on tables owned by the current user. This view does not display the `INDEX_OWNER` or `TABLE_OWNER` columns.

Note:

For join indexes, the `TABLE_NAME` and `TABLE_OWNER` columns in this view may not match the `TABLE_NAME` and `TABLE_OWNER` columns you find in the `*_INDEXES` (and other similar) data dictionary views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the index |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table or cluster |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table or cluster |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name or attribute of the object type column |
|  |  |  | Note: If you create an index on a user-defined `REF` column, the system creates the index on the attributes that make up the `REF` column. Therefore, the column names displayed in this view are the attribute names, with the `REF` column name as a prefix, in the following form:  `"REF_name"."attribute"` |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Position of the column or attribute within the index |
| `COLUMN_LENGTH` | `NUMBER` | `NOT NULL` | Indexed length of the column |
| `CHAR_LENGTH` | `NUMBER` |  | Maximum codepoint length of the column |
| `DESCEND` | `VARCHAR2(4)` |  | Indicates whether the column is sorted in descending order (`DESC`) or ascending order (`ASC`) |
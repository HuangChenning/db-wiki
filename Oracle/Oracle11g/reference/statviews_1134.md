---
title: ALL_LOG_GROUP_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1134.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LOG_GROUP_COLUMNS` describes columns that are accessible to the current user and that are specified in log groups.

Related Views

- `DBA_LOG_GROUP_COLUMNS` describes all columns in the database that are specified in log groups.
- `USER_LOG_GROUP_COLUMNS` describes columns that are owned by the current user and that are specified in log groups.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the log group definition |
| `LOG_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the log group definition |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table in which the log group is defined |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column or attribute of the object type column specified in the log group definition |
| `POSITION` | `NUMBER` |  | Original position of the column or attribute in the definition of the object |
| `LOGGING_PROPERTY` | `VARCHAR2(6)` |  | Indicates whether the column or attribute would be supplementally logged (`LOG`) or not (`NO LOG`) |
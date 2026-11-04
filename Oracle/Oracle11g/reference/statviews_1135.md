---
title: ALL_LOG_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1135.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LOG_GROUPS` describes the log group definitions on the tables accessible to the current user.

Related Views

- `DBA_LOG_GROUPS` describes the log group definitions on all tables in the database.
- `USER_LOG_GROUPS` describes the log group definitions on the tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the log group definition |
| `LOG_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the log group definition |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table on which the log group is defined |
| `LOG_GROUP_TYPE` | `VARCHAR2(19)` |  | Type of the log group: |
| `ALWAYS` | `VARCHAR2(11)` |  | `Y` indicates the log group is logged any time a row is updated; `N` indicates the log group is logged any time a member column is updated |
| `GENERATED` | `VARCHAR2(14)` |  | Indicates whether the name of the supplemental log group was system generated (`GENERATED NAME`) or not (`USER NAME`) |
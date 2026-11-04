---
title: ALL_SQLSET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2070.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SQLSET` displays information about all SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET` displays information about all SQL tuning sets in the database.
- `USER_SQLSET` displays information about the SQL tuning sets owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL tuning set |
| `ID` | `NUMBER` | `NOT NULL` | SQL tuning set identifier |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the SQL tuning set |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the SQL tuning set |
| `CREATED` | `DATE` |  | Date the SQL tuning set was created |
| `LAST_MODIFIED` | `DATE` |  | Date the SQL tuning set was last modified |
| `STATEMENT_COUNT` | `NUMBER` |  | Number of statements in the SQL tuning set |
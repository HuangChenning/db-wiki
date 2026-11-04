---
title: ALL_SQLSET_REFERENCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2073.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SQLSET_REFERENCES` describes whether or not the SQL tuning sets accessible to the current user are active.

Related Views

- `DBA_SQLSET_REFERENCES` describes whether or not all SQL tuning sets in the database are active. A SQL tuning set cannot be dropped if it is referenced.
- `USER_SQLSET_REFERENCES` describes whether or not the SQL tuning sets owned by the current user are active.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL tuning set |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | Identifier of the SQL tuning set |
| `SQLSET_OWNER` | `VARCHAR2(30)` |  | Owner of the SQL tuning set |
| `ID` | `NUMBER` | `NOT NULL` | Reference identifier |
| `OWNER` | `VARCHAR2(30)` |  | User who registered to use the SQL tuning set |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the usage of the SQL tuning set |
| `CREATED` | `DATE` |  | Date the reference was created |
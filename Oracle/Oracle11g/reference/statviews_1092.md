---
title: ALL_EXTERNAL_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1092.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EXTERNAL_TABLES` describes the external tables accessible to the current user.

Related Views

- `DBA_EXTERNAL_TABLES` describes all external tables in the database.
- `USER_EXTERNAL_TABLES` describes the external tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the external table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the external table |
| `TYPE_OWNER` | `CHAR(3)` |  | Owner of the implementation type for the external table access driver |
| `TYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the implementation type for the external table access driver |
| `DEFAULT_DIRECTORY_OWNER` | `CHAR(3)` |  | Owner of the default directory for the external table |
| `DEFAULT_DIRECTORY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the default directory for the external table |
| `REJECT_LIMIT` | `VARCHAR2(40)` |  | Reject limit for the external table, or `UNLIMITED` |
| `ACCESS_TYPE` | `VARCHAR2(7)` |  | Type of access parameters for the external table: |
| `ACCESS_PARAMETERS` | `CLOB` |  | Access parameters for the external table |
| `PROPERTY` | `VARCHAR2(10)` |  | Property of the external table: |

See Also:

- ["DBA\_EXTERNAL\_TABLES"](statviews_3180.md)
- ["USER\_EXTERNAL\_TABLES"](statviews_5303.md)
---
title: ROLE_TAB_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5172.htm
tags:
  - oracle
  - 11g
  - reference
---

`ROLE_TAB_PRIVS` describes table privileges granted to roles. Information is provided only about roles to which the user has access.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the role |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of the column, if applicable |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Object privilege granted to the role |
| `GRANTABLE` | `VARCHAR2(3)` |  | `YES` if the role was granted with `ADMIN OPTION`; otherwise `NO` |
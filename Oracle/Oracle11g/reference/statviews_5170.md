---
title: ROLE_ROLE_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5170.htm
tags:
  - oracle
  - 11g
  - reference
---

`ROLE_ROLE_PRIVS` describes the roles granted to other roles. Information is provided only about roles to which the user has access.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the role |
| `GRANTED_ROLE` | `VARCHAR2(30)` | `NOT NULL` | Role that was granted |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Signifies that the role was granted with `ADMIN` option |
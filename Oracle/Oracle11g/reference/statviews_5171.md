---
title: ROLE_SYS_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5171.htm
tags:
  - oracle
  - 11g
  - reference
---

`ROLE_SYS_PRIVS` describes system privileges granted to roles. Information is provided only about roles to which the user has access.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the role |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | System privilege granted to the role |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |
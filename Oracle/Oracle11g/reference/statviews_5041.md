---
title: DBA_SYS_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5041.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SYS_PRIVS` describes system privileges granted to users and roles.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` | `NOT NULL` | Grantee name, user, or role receiving the grant |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | System privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |
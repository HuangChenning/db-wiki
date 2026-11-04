---
title: USER_SYS_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5473.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_SYS_PRIVS` describes system privileges granted to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` |  | Name of the user, or `PUBLIC` |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | System privilege |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN` option (`YES`) or not (`NO`) |
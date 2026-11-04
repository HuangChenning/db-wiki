---
title: USER_ROLE_PRIVS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5416.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_ROLE_PRIVS` describes the roles granted to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` |  | Name of the user, or `PUBLIC` |
| `GRANTED_ROLE` | `VARCHAR2(30)` |  | Name of the role granted to the user |
| `ADMIN_OPTION` | `VARCHAR2(3)` |  | Indicates whether the grant was with the `ADMIN OPTION` (`YES`) or not (`NO`) |
| `DEFAULT_ROLE` | `VARCHAR2(3)` |  | Indicates whether the role is designated as a `DEFAULT ROLE` for the user (`YES`) or not (`NO`) |
| `OS_GRANTED` | `VARCHAR2(3)` |  | Indicates whether the role was granted by the operating system (`YES`) or not (`NO`); occurs if the `OS_ROLES` initialization parameter is `true` |
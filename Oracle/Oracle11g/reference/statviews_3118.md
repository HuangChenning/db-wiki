---
title: DBA_CONNECT_ROLE_GRANTEES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3118.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_CONNECT_ROLE_GRANTEES` displays information about users who are granted the `CONNECT` privilege.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(30)` |  | User or schema to which the `CONNECT` role is granted |
| `PATH_OF_CONNECT_ROLE_GRANT` | `VARCHAR2(4000)` |  | The path of role inheritance through which the grantee is granted the `CONNECT` role |
| `ADMIN_OPT` | `VARCHAR2(3)` |  | Whether or not the grantee was granted the `ADMIN` option for the `CONNECT` role |
---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_CONNECT_ROLE_GRANTEES.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.215 DBA\_CONNECT\_ROLE\_GRANTEES

`DBA_CONNECT_ROLE_GRANTEES` displays information about users who are granted the `CONNECT` privilege.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` |  | User or schema to which the `CONNECT` role is granted |
| `PATH_OF_CONNECT_ROLE_GRANT` | `VARCHAR2(4000)` |  | The path of role inheritance through which the grantee is granted the `CONNECT` role |
| `ADMIN_OPT` | `VARCHAR2(3)` |  | Whether or not the grantee was granted the `ADMIN` option for the `CONNECT` role |
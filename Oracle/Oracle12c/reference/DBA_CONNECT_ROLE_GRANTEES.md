---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CONNECT_ROLE_GRANTEES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_CONNECT_ROLE_GRANTEES` displays information about users who are granted the `CONNECT` privilege.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTEE` | `VARCHAR2(128)` |  | User or schema to which the `CONNECT` role is granted |
| `PATH_OF_CONNECT_ROLE_GRANT` | `VARCHAR2(4000)` |  | The path of role inheritance through which the grantee is granted the `CONNECT` role |
| `ADMIN_OPT` | `VARCHAR2(3)` |  | Whether or not the grantee was granted the `ADMIN` option for the `CONNECT` role |
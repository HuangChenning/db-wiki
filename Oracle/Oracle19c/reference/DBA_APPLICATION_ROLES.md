---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_APPLICATION_ROLES.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.98 DBA\_APPLICATION\_ROLES

`DBA_APPLICATION_ROLES` describes all the roles that have authentication policy functions defined.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the application role |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema of the authorized package |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Name of the authorized package |
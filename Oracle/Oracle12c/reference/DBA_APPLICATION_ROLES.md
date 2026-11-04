---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APPLICATION_ROLES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APPLICATION_ROLES` describes all the roles that have authentication policy functions defined.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the application role |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema of the authorized package |
| `PACKAGE` | `VARCHAR2(128)` | `NOT NULL` | Name of the authorized package |
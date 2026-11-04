---
title: DBA_APPLICATION_ROLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3046.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLICATION_ROLES` describes all the roles that have authentication policy functions defined.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the application role |
| `SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Schema of the authorized package |
| `PACKAGE` | `VARCHAR2(30)` | `NOT NULL` | Name of the authorized package |
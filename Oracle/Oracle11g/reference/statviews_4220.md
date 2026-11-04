---
title: DBA_ROLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4220.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ROLES` describes all roles in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the role |
| `PASSWORD_REQUIRED` | `VARCHAR2(8)` |  | This column is deprecated in favor of the `AUTHENTICATION_TYPE` column |
| `AUTHENTICATION_TYPE` | `VARCHAR2(11)` |  | Indicates the authentication mechanism for the role: - `NONE` - `CREATE ROLE` `role1``;` - `EXTERNAL` - `CREATE ROLE` `role2` `IDENTIFIED EXTERNALLY;` - `GLOBAL` - `CREATE ROLE` `role3` `IDENTIFIED GLOBALLY;` - `APPLICATION` - `CREATE ROLE` `role4` `IDENTIFIED USING` `schema``.``package``;` - `PASSWORD` - `CREATE ROLE` `role5` `IDENTIFIED BY` `role5``;` |
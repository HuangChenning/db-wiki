---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.294 DBA\_ROLES

`DBA_ROLES` describes all roles in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ROLE ` | `VARCHAR2(128)` | `NOT NULL` | Name of the role |
| `ROLE_ID` | `NUMBER` | `NOT NULL` | ID number of the role |
| `PASSWORD_REQUIRED ` | `VARCHAR2(8)` |  | This column is deprecated in favor of the `AUTHENTICATION_TYPE` column |
| `AUTHENTICATION_TYPE` | `VARCHAR2(11)` |  | Indicates the authentication mechanism for the role:  - `NONE` - `CREATE ROLE ` `role1``;` - `EXTERNAL` - `CREATE ROLE ` `role2` ` IDENTIFIED EXTERNALLY;` - `GLOBAL` - `CREATE ROLE ` `role3` ` IDENTIFIED GLOBALLY;` - `APPLICATION` - `CREATE ROLE ` `role4` `  IDENTIFIED USING  ` `schema``.``package``;` - `PASSWORD` - `CREATE ROLE ` `role5` `  IDENTIFIED BY  ` `role5``;` |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether a given role is common. Possible values:  - `YES` if the role is common - `NO` if the role is local (not common) |
| `ORACLE_MAINTAINED` | `VARCHAR2(1)` |  | Denotes whether the role was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). A role for which this column has the value `Y` must not be changed in any way except by running an Oracle-supplied script. |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the role was inherited from another container (`YES`) or not (`NO`) |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether the role is a common role created by an implicit application (`YES`) or not (`NO`) |
| `EXTERNAL_NAME` | `VARCHAR2(4000)` |  | For a global role, the external name refers to the DN of a group from a directory service that is mapped to the global role. This is not applicable to a local role. |
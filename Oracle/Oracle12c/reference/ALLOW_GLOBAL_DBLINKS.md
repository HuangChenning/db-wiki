---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALLOW_GLOBAL_DBLINKS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALLOW_GLOBAL_DBLINKS` specifies whether LDAP lookup for database links is allowed for the database.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Syntax | `ALLOW_GLOBAL_DBLINKS = { FALSE \| TRUE }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The following values can be set:

- `FALSE`: LDAP lookup for a database link’s definition is not allowed for the database.
- `TRUE`: LDAP lookup for a database link’s definition is allowed for the database.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).
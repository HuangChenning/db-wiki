---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALLOW_GLOBAL_DBLINKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.10 ALLOW\_GLOBAL\_DBLINKS

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
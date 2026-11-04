---
title: DB_UNIQUE_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams070.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_UNIQUE_NAME =` `database_unique_name` |
| Default value | Database instances: the value of `DB_NAME`  Automatic Storage Management instances: `+ASM` |
| Modifiable | No |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

`DB_UNIQUE_NAME` specifies a globally unique name for the database. Databases with the same `DB_NAME` within the same `DB_DOMAIN` (for example, copies of a database created for reporting or a physical standby) must have a unique `DB_UNIQUE_NAME`. Every database's `DB_UNIQUE_NAME` must be unique within the enterprise.

The value of `DB_UNIQUE_NAME` can be up to 30 characters and is case insensitive. The following characters are valid in a database name: alphanumeric characters, underscore (\_), number sign (#), and dollar sign ($).

Note:

As part of their operations, some database tools or utilities create a string that uniquely identifies a database. The string may include the `DB_UNIQUE_NAME` for a database, and other identifying information for the database, such as the database SID. Oracle Database restricts some identifiers to 30 characters, so using a short `DB_UNIQUE_NAME` can help prevent `ORA-00972` "identifier is too long" messages from database tools and utilities that create a string that includes the `DB_UNIQUE_NAME`.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_arch_dest_param.htm#SBYDB01100) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on setting this parameter
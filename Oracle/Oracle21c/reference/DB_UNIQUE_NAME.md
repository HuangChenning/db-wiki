---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_UNIQUE_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.97 DB\_UNIQUE\_NAME

`DB_UNIQUE_NAME` specifies a globally unique name for the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_UNIQUE_NAME = ` `database_unique_name` |
| Default value | Database instances: the value of `DB_NAME`  Oracle Automatic Storage Management instances: `+ASM` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

Databases with the same `DB_NAME` within the same `DB_DOMAIN` (for example, copies of a database created for reporting or a physical standby) must have a unique `DB_UNIQUE_NAME`. Every database's `DB_UNIQUE_NAME` must be unique within the enterprise.

The value of `DB_UNIQUE_NAME` can be up to 30 characters and is case insensitive. The following characters are valid in a database name: alphanumeric characters, underscore (\_), number sign (#), and dollar sign ($).

Note:

`DB_UNIQUE_NAME` is used by several components within an Oracle instance to default file names or file paths, such as the default for the `DG_BROKER_CONFIG_FILE` n initialization parameter. In these cases, on UNIX platforms, the dollar sign ($) character will be removed from the path or file name, because the character is used by Oracle to define the start of an environment variable substitution within a path or file name.

Note:

As part of their operations, some database tools or utilities create a string that uniquely identifies a database. The string may include the `DB_UNIQUE_NAME` for a database, and other identifying information for the database, such as the database SID. Oracle Database restricts some identifiers to 30 characters, so using a short `DB_UNIQUE_NAME` can help prevent `ORA-00972` "identifier is too long" messages from database tools and utilities that create a string that includes the `DB_UNIQUE_NAME`.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB01100) and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11492) for more information on setting this parameter
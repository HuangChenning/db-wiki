---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.90 DB\_NAME

`DB_NAME` specifies a database identifier of up to 8 characters.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_NAME = ` `database_name` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance. Multiple instances must have the same value. |

This parameter must be specified and must correspond to the name specified in the `CREATE DATABASE` statement.

If you have multiple databases, the value of this parameter should match the Oracle instance identifier of each one to avoid confusion with other databases running on the system. The value of `DB_NAME` must be the same in both the standby and production initialization parameter files.

The database name specified in either the `STARTUP` command or the `ALTER DATABASE ... MOUNT` statement for each instance of the cluster database must correspond to the `DB_NAME` initialization parameter setting.

The following characters are valid in a database name: alphanumeric characters, underscore (\_), number sign (#), and dollar sign ($). No other characters are valid. The database name must start with an alphabetic character. Oracle removes double quotation marks before processing the database name. Therefore you cannot use double quotation marks to embed other characters in the name. The database name is case insensitive.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11101) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD7278) for more information on setting this parameter
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_PDB_FS_CONF.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.102 DBNEST\_PDB\_FS\_CONF

`DBNEST_PDB_FS_CONF` specifies the dbNest file system configuration file for a PDB.

Note:

This parameter is applicable only on Linux systems.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DBNEST_PDB_FS_CONF = 'pathname'` |
| Default value | None |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

A dbNest file system configuration file specifies directories to be mounted inside the nest for a PDB. These directories are mounted in addition to the default directories.

For `pathname`, specify the full operating system path for the file.

If you do not set this parameter, then only the default directories are mounted.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

[Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-BEE0A670-F46F-49DC-819B-6191361A6C8E) for information on dbNest file system configuration files
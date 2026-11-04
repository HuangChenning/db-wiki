---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CLONEDB_DIR.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.42 CLONEDB\_DIR

`CLONEDB_DIR` sets the directory path where CloneDB bitmap files should be created and accessed.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CLONEDB_DIR =` `string` |
| Default value | `$ORACLE_HOME/dbs` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | In an Oracle RAC environment, this parameter should be set to a shared location that is accessible from all the instances. |

By default the CloneDB bitmap file is created under the `$ORACLE_HOME/dbs` directory. This directory may not be in a shared location in an Oracle RAC environment, and therefore this parameter is provided to identify a shared location where CloneDB specific files can be created.

See Also:

" [CLONEDB](CLONEDB.md) "
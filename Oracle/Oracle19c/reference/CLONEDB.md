---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/CLONEDB.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.41 CLONEDB

`CLONEDB` should be set on Direct NFS Client CloneDB databases. When this parameter is set, the CloneDB database uses the database backup as the backing store for the datafiles.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value should be set for all instances. |

See Also:

- See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADMIN14023) for more information about cloning databases on network attached storage (NAS).
- " [CLONEDB\_DIR](CLONEDB_DIR.md) "
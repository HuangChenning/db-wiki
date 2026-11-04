---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NONCDB_COMPATIBLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.231 NONCDB\_COMPATIBLE

`NONCDB_COMPATIBLE` enables you to get behavior similar to a non-CDB when issuing SQL commands inside a PDB in a CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Set this parameter if you are using a single PDB in your CDB configuration and you have legacy code that causes `ORA-65040` when you run it in the PDB.

Values

- `TRUE`
	Indicates the behavior for SQL statements will be like a non-CDB although the statements are issued in a PDB in a CDB.
- `FALSE`
	Indicates the behavior will for SQL statements will be like a CDB. This is the default value of the parameter.

There are some statements (such as `ALTER DB BACKUP CONTROLFILE`) which can be issued in a non-CDB, but in a CDB they must be issued in the root (because they affect the whole CDB) and would result in an error if issued in a PDB.

Some `ALTER DATABASE` or `ALTER SYSTEM` statements are not permitted inside a PDB, and they will fail if `NONCDB_COMPATIBLE=FALSE` is set in `init.ora`. However, these statements will succeed if `NONCDB_COMPATIBLE=TRUE` is set.

See Also:

- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89234) for an introduction to PDBs and CDBs
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-A3459A8B-A36A-44D4-9FCD-75CA0E3D3252) for information about the initialization parameters that control the memory usage of PDBs
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13652) for information about the ALTER SYSTEM statements that can be run in a PDB.
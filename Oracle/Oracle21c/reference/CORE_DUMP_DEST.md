---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CORE_DUMP_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.57 CORE\_DUMP\_DEST

`CORE_DUMP_DEST` specifies the directory where Oracle dumps core files.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CORE_DUMP_DEST = ` `directory` |
| Default value | `ORACLE_HOME` `/DBS` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

`CORE_DUMP_DEST` is primarily a UNIX parameter and may not be supported on your platform.

Note:

This parameter is ignored by the new diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the `DIAGNOSTIC_DEST` initialization parameter.

See Also:

" [DIAGNOSTIC\_DEST](DIAGNOSTIC_DEST.md) "
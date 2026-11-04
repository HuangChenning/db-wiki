---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_PLUGGABLE_DATABASE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.125 ENABLE\_PLUGGABLE\_DATABASE

`ENABLE_PLUGGABLE_DATABASE` is a bootstrap initialization parameter to create a CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

This parameter enables a database in `NOMOUNT` startup mode to know that it is a CDB.

Note:

See [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89234) for more information about CDBs and PDBs.
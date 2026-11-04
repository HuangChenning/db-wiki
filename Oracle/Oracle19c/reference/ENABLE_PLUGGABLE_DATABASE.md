---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_PLUGGABLE_DATABASE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.121 ENABLE\_PLUGGABLE\_DATABASE

`ENABLE_PLUGGABLE_DATABASE` is a bootstrap initialization parameter to create a CDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

This parameter enables a database in `NOMOUNT` startup mode to know that it is a CDB.

This parameter must be set in `init.ora` before creating a CDB.

Note:

See [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=CNCPT89234) for more information about CDBs and PDBs.
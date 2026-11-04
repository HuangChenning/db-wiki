---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ENABLE_PLUGGABLE_DATABASE.html
tags:
  - oracle
  - 12c
  - reference
---

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

See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT89234) for more information about CDBs and PDBs.
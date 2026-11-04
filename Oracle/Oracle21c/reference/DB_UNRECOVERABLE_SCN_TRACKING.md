---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_UNRECOVERABLE_SCN_TRACKING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.98 DB\_UNRECOVERABLE\_SCN\_TRACKING

`DB_UNRECOVERABLE_SCN_TRACKING` enables or disables the tracking of unrecoverable (`NOLOGGING`) direct-path INSERT and direct-path load operations.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value |

When the value is set to `true`, updates are made to the controlfile that maintains the `V$DATAFILE`.`UNRECOVERABLE_CHANGE#` and `V$DATAFILE`.`UNRECOVERABLE_TIME` columns. When the value is set to `false`, updates are not made to the controlfile. Setting this parameter to `false` may improve performance of direct-path `NOLOGGING` operations.
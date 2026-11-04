---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DB_UNRECOVERABLE_SCN_TRACKING.html
tags:
  - oracle
  - 12c
  - reference
---

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
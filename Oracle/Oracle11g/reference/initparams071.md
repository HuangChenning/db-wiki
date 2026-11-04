---
title: DB_UNRECOVERABLE_SCN_TRACKING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams071.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value |

`DB_UNRECOVERABLE_SCN_TRACKING` enables or disables the tracking of unrecoverable (`NOLOGGING`) direct-path insert and load operations.

When the value is set to `true`, updates are made to the controlfile that maintains the `V$DATAFILE`.`UNRECOVERABLE_CHANGE#` and `V$DATAFILE`.`UNRECOVERABLE_TIME` columns. When the value is set to `false`, updates are not made to the controlfile. Setting this parameter to `false` may improve performance of direct-path `NOLOGGING` operations.

Note:

The `DB_UNRECOVERABLE_SCN_TRACKING` initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.2).
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LONG_MODULE_ACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.197 LONG\_MODULE\_ACTION

`LONG_MODULE_ACTION` enables the use of longer lengths for modules and actions.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | true |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Module length was 48 bytes and action length was 32 bytes in Oracle Database releases prior to Oracle Database 12c Release 2 (12.2.0.1).

Starting with Oracle Database 12c Release 2 (12.2.0.1):

- If `LONG_MODULE_ACTION` is set to `TRUE` (the default value), then the length of modules and actions will be 64 bytes each.
- If `LONG_MODULE_ACTION` is set to `FALSE`, then the length of modules will be 48 bytes, and the length of actions will be 32 bytes.
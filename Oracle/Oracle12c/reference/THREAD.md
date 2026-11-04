---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/THREAD.html
tags:
  - oracle
  - 12c
  - reference
---

`THREAD` has been superseded by the `INSTANCE_NAME` and `INSTANCE_NUMBER` parameters, and will be made obsolete in a future release of the Oracle Database.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to the maximum number of enabled threads |
| Basic | No |
| Oracle RAC | If specified, multiple instances must have different values. |

See Also:

" [INSTANCE\_NAME](INSTANCE_NAME.md) " and " [INSTANCE\_NUMBER](INSTANCE_NUMBER.md) "
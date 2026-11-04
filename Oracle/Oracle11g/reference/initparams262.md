---
title: TRANSACTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams262.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: (1.1 \* `SESSIONS`) |
| Modifiable | No |
| Range of values | 4 to 2 <sup>32</sup> |
| Oracle RAC | Multiple instances can have different values. |

`TRANSACTIONS` specifies how many rollback segments to online when `UNDO_MANAGEMENT` `=` `MANUAL`. The maximum number of concurrent transactions is now restricted by undo tablespace size (`UNDO_MANAGEMENT` `=` `AUTO`) or the number of online rollback segments (`UNDO_MANAGEMENT` `=` `MANUAL`).

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on setting this parameter
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for the relationship of this parameter to the number of rollback segments
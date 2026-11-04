---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DISTRIBUTED_LOCK_TIMEOUT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.113 DISTRIBUTED\_LOCK\_TIMEOUT

`DISTRIBUTED_LOCK_TIMEOUT` specifies the amount of time (in seconds) for distributed transactions to wait for locked resources.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `60` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 1 to 2 <sup>31</sup> - 1 |
| Basic | No |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT964) for more information on data concurrency
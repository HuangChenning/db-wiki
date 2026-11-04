---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DISTRIBUTED_LOCK_TIMEOUT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.111 DISTRIBUTED\_LOCK\_TIMEOUT

`DISTRIBUTED_LOCK_TIMEOUT` specifies the amount of time (in seconds) for distributed transactions to wait for locked resources.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `60` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to 2 <sup>31</sup> - 1 |
| Basic | No |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=CNCPT964) for more information on data concurrency
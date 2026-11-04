---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_DEEP_VECTORIZATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.152 INMEMORY\_DEEP\_VECTORIZATION

`INMEMORY_DEEP_VECTORIZATION` enables or disables the deep vectorization framework.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `TRUE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `TRUE \| FALSE` |
| Basic | No |

Deep vectorization can optimize complex SQL operations (such as joins) by pipelining physical operators inside each SQL operator and vectorizing them.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

[Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-55F66F65-1568-4B53-B79E-F841B94659CA) for information about deep vectorization
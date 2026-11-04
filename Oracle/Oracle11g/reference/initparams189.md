---
title: PARALLEL_MIN_TIME_THRESHOLD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams189.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_MIN_TIME_THRESHOLD = { AUTO \|` `integer` `}` |
| Default value | `AUTO` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`PARALLEL_MIN_TIME_THRESHOLD` specifies the minimum execution time a statement should have before the statement is considered for automatic degree of parallelism. By default, this is set to 10 seconds. Automatic degree of parallelism is only enabled if `PARALLEL_DEGREE_POLICY` is set to `AUTO` or `LIMITED`.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm) for information about automatic degree of parallelism
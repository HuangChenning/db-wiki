---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_MIN_PERCENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.272 PARALLEL\_MIN\_PERCENT

`PARALLEL_MIN_PERCENT` lets you specify the minimum percentage of the requested number of parallel execution processes required for parallel execution.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | No |
| Range of values | 0 to 100 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter controls the behavior for parallel operations when parallel statement queuing is not enabled (when `PARALLEL_DEGREE_POLICY` is set to `manual` or `limited`). It ensures that an operation always gets a minimum percentage of parallel execution servers or errors out. Setting this parameter ensures that parallel operations will not execute unless adequate resources are available. The default value of `0` means that no minimum percentage of processes has been set.

Consider the following settings:

```
PARALLEL_MIN_PERCENT = 50
PARALLEL_MIN_SERVERS = 5
PARALLEL_MAX_SERVERS = 10
```

If 8 of the 10 parallel execution processes are busy, only 2 processes are available. If you then request a query with a degree of parallelism of 8, the minimum 50% will not be met.

You can use this parameter with `PARALLEL_ADAPTIVE_MULTI_USER`. In a multi-user environment, an individual user or application can set `PARALLEL_MIN_PERCENT` to a minimum value until sufficient resources are available on the system and an acceptable degree of parallelism is returned.
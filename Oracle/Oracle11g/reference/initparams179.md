---
title: PARALLEL_AUTOMATIC_TUNING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams179.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |

Note:

The `PARALLEL_AUTOMATIC_TUNING` parameter is deprecated. It is retained for backward compatibility only.

When `PARALLEL_AUTOMATIC_TUNING` is set to `true`, Oracle determines the default values for parameters that control parallel execution. In addition to setting this parameter, you must specify the `PARALLEL` clause for the target tables in the system. Oracle then tunes all subsequent parallel operations automatically.

If you used parallel execution in a previous release and are now enabling `PARALLEL_AUTOMATIC_TUNING`, then you should reduce the amount of memory allocated from the shared pool to account for the decreased demand on that pool. This memory will now be allocated from the large pool, and will be computed automatically if `LARGE_POOL_SIZE` is not specified.

As part of the automatic tuning, Oracle will enable the `PARALLEL_ADAPTIVE_MULTI_USER` parameter. You can override any of the system-provided defaults if desired.
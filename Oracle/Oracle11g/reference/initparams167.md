---
title: OPTIMIZER_DYNAMIC_SAMPLING
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams167.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If `OPTIMIZER_FEATURES_ENABLE` is set to `10.0.0` or higher, then `2`  If `OPTIMIZER_FEATURES_ENABLE` is set to `9.2.0`, then `1`  If `OPTIMIZER_FEATURES_ENABLE` is set to `9.0.1` or lower, then `0` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `0` to `11` |
| Basic | No |

`OPTIMIZER_DYNAMIC_SAMPLING` controls both when the database gathers dynamic statistics, and the size of the sample that the optimizer uses to gather the statistics.

Note:

Dynamic statistics were called dynamic sampling in releases before Oracle Database 11g Release 2 (11.2.0.4).

When this parameter is set to `11`, the optimizer will use dynamic statistics to verify cardinality estimates for all SQL operators, and it will determine an internal time limit to spend verifying the estimates.

If the value of `OPTIMIZER_DYNAMIC_SAMPLING` is set to `11`, the `OPTIMIZER_FEATURES_ENABLE` setting has no effect on the `OPTIMIZER_DYNAMIC_SAMPLING` setting.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF30101) for more information on setting this parameter
---
title: OPTIMIZER_FEATURES_ENABLE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams168.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OPTIMIZER_FEATURES_ENABLE = { 8.0.0 \| 8.0.3 \| 8.0.4 \| 8.0.5 \| 8.0.6 \| 8.0.7 \| 8.1.0 \| 8.1.3 \| 8.1.4 \| 8.1.5 \| 8.1.6 \| 8.1.7 \| 9.0.0 \| 9.0.1 \| 9.2.0 \| 9.2.0.8 \| 10.1.0 \| 10.1.0.3 \| 10.1.0.4 \| 10.1.0.5 \| 10.2.0.1 \| 10.2.0.2 \| 10.2.0.3 \| 10.2.0.4 \| 10.2.0.5 \| 11.1.0.6 \| 11.1.0.7 \| 11.2.0.1 }` |
| Default value | `11.2.0.1` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`OPTIMIZER_FEATURES_ENABLE` acts as an umbrella parameter for enabling a series of optimizer features based on an Oracle release number.

For example, if you upgrade your database from release 10.1 to release 11.1, but you want to keep the release 10.1 optimizer behavior, you can do so by setting this parameter to `10.1.0`. At a later time, you can try the enhancements introduced in releases up to and including release 11.1 by setting the parameter to `11.1.0.6`.

Table 1-3 describes some of the optimizer features that are enabled when you set the `OPTIMIZER_FEATURES_ENABLE` parameter to a 9.0 release or a 9.2 release.

Table 1-4 describes some of the optimizer features that are enabled when you set the `OPTIMIZER_FEATURES_ENABLE` parameter to a 10.1 release or a 10.2 release.

Table 1-5 describes some of the optimizer features that are enabled when you set the `OPTIMIZER_FEATURES_ENABLE` parameter to a 11.1 release.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about the optimizer and for information about the features listed in the following tables

Table 1-3 Optimizer Features for Oracle9I Releases

| Features | 9.0.0 | 9.0.1 | 9.2.0 |
| --- | --- | --- | --- |
| Index fast full scan | X | X | X |
| Consideration of bitmap access to paths for tables with only B-tree indexes | X | X | X |
| Complex view merging | X | X | X |
| Peeking into user-defined bind variables | X | X | X |
| Index joins | X | X | X |

Table 1-4 Optimizer Features for Oracle Database 10g Releases

| Features | 10.1.0 | 10.1.0.3 | 10.1.0.4 | 10.1.0.5 | 10.2.0.1 | 10.2.0.2 |
| --- | --- | --- | --- | --- | --- | --- |
| Index fast full scan | X | X | X | X | X | X |
| Consideration of bitmap access to paths for tables with only B-tree indexes | X | X | X | X | X | X |
| Complex view merging | X | X | X | X | X | X |
| Peeking into user-defined bind variables | X | X | X | X | X | X |
| Index joins | X | X | X | X | X | X |
| Dynamic sampling | X | X | X | X | X | X |
| Query rewrite enables | X | X | X | X | X | X |
| Skip unusable indexes | X | X | X | X | X | X |
| Automatically compute index statistics as part of creation | X | X | X | X | X | X |
| Cost-based query transformations | X | X | X | X | X | X |
| Allow rewrites with multiple MVs and/or base tables |  |  |  |  | X | X |

Table 1-5 Optimizer Features for Oracle Database 11g Releases

| Features | 11.1.0.6 |
| --- | --- |
| Enhanced Bind Peeking | X |
| Use extended statistics to estimate selectivity | X |
| Use native implementation for full outer joins | X |
| Partition pruning using join filtering | X |
| Group by placement optimization | X |
| Null aware antijoins | X |
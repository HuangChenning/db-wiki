---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_ADAPTIVE_REPORTING_ONLY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.241 OPTIMIZER\_ADAPTIVE\_REPORTING\_ONLY

`OPTIMIZER_ADAPTIVE_REPORTING_ONLY` controls reporting-only mode for adaptive optimizations.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `FALSE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `TRUE \| FALSE` |
| Basic | No |

When `OPTIMIZER_ADAPTIVE_REPORTING_ONLY` is set to `FALSE`, reporting-only mode is off, and the adaptive optimizations are enabled as usual.

When `OPTIMIZER_ADAPTIVE_REPORTING_ONLY` is set to `TRUE`, adaptive optimizations run in reporting-only mode. With this setting, the information required for an adaptive optimization is gathered, but no action is taken to change the plan. For instance, an adaptive plan will always choose the default (optimizer-chosen) plan, but information is collected on what plan to adapt to in non-reporting mode. This information can be viewed in the adaptive plan report.

This parameter affects only adaptive optimizations that are enabled.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL221) for more information about adaptive plans and automatic reoptimization
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL257) for information on controlling adaptive optimization
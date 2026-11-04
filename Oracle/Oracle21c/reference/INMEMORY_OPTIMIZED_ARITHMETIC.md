---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_OPTIMIZED_ARITHMETIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.156 INMEMORY\_OPTIMIZED\_ARITHMETIC

`INMEMORY_OPTIMIZED_ARITHMETIC` encodes the `NUMBER` data type in in-memory tables compressed with `QUERY LOW` as a fixed-width native integer scaled by a common exponent.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_OPTIMIZED_ARITHMETIC = { ENABLE \| DISABLE }` |
| Default value | `DISABLE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Different values can be specified on different instances. |

The Oracle Database `NUMBER` format can incur a significant performance overhead when executing queries because arithmetic operations cannot be performed natively in hardware.

When `INMEMORY_OPTIMIZED_ARITHMETIC` is set to `ENABLE`, for tables compressed with `QUERY LOW`, `NUMBER` columns are encoded as a fixed-width native integer scaled by a common exponent. This In-Memory optimized number format enables fast calculations using SIMD hardware. By using SIMD vector processing, arithmetic operations, simple aggregations, and group-by aggregations can benefit significantly.

Not all row sources in the query processing engine have support for the In-Memory optimized number format. Therefore, the IM column store must store both the traditional Oracle Database `NUMBER` data type and the In-Memory optimized number type. This means that the acceleration in analytic query performance comes at a cost of increased space overhead.

When `INMEMORY_OPTIMIZED_ARITHMETIC` is set to `DISABLE` (the default), the database does not use the optimized encoding.

If `INMEMORY_OPTIMIZED_ARITHMETIC` is set to `ENABLE` and then to `DISABLE`, the optimized number format for existing IMCUs is not dropped immediately. Instead, as the IM column store repopulates IMCUs, the new IMCUs do not use the optimized encoding.
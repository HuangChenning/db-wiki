---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_MIN_DEGREE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.271 PARALLEL\_MIN\_DEGREE

`PARALLEL_MIN_DEGREE` controls the minimum degree of parallelism computed by automatic degree of parallelism.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_MIN_DEGREE = [ n \| CPU ]` |
| Default value | 1 |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | A different value can be set on different instances. |

The value of `PARALLEL_MIN_DEGREE` is either a number that corresponds to the lower bound on the degree of parallelism computed by automatic degree of parallelism, or the string value `CPU`, which is computed by the function `CPU_COUNT` \* `PARALLEL_THREADS_PER_CPU`.

The default value of `PARALLEL_MIN_DEGREE` is 1.

Note:

`PARALLEL_MIN_DEGREE` has no impact in either of these cases:

- When the value of `PARALLEL_MIN_DEGREE` is greater than the value of `CPU_COUNT`
- When the object is Oracle-owned, such as a dictionary table or view created on a dictionary table

See Also:

- " [PARALLEL\_DEGREE\_LIMIT](PARALLEL_DEGREE_LIMIT.md) "
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG1392) for information about how the optimizer automatically determines the degree of parallelism for a statement
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_DEGREE_POLICY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.266 PARALLEL\_DEGREE\_POLICY

`PARALLEL_DEGREE_POLICY` specifies whether automatic degree of parallelism, statement queuing, and in-memory parallel execution will be enabled.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_DEGREE_POLICY = { MANUAL \| LIMITED \| AUTO \| ADAPTIVE }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

Note:

Automatic degree of parallelism will be enabled regardless of the value of `PARALLEL_DEGREE_POLICY` if a `PARALLEL` hint is used at the SQL statement level.

- `MANUAL`
	Disables automatic degree of parallelism, statement queuing, and in-memory parallel execution. This reverts the behavior of parallel execution to what it was prior to Oracle Database 11g Release 2 (11.2). This is the default.
- `LIMITED`
	Enables automatic degree of parallelism for some statements but statement queuing and in-memory Parallel Execution are disabled. Automatic degree of parallelism is only applied to those statements that access tables or indexes decorated explicitly with the `DEFAULT` degree of parallelism using the `PARALLEL` clause. Statements that do not access any tables or indexes decorated with the `DEFAULT` degree of parallelism will retain the `MANUAL` behavior.
- `AUTO`
	Enables automatic degree of parallelism, statement queuing, and in-memory parallel execution.
- `ADAPTIVE`
	This value enables automatic degree of parallelism, statement queuing and in-memory parallel execution, similar to the `AUTO` value. In addition, performance feedback is enabled. Performance feedback helps to improve the degree of parallelism automatically chosen for repeated SQL statements. After the initial execution of a statement, the degree of parallelism chosen by the optimizer is compared to the degree of parallelism computed based on the actual execution performance. If they vary significantly, then the statement is marked for re-parse and the initial execution performance statistics (for example, CPU-time) are provided as feedback for subsequent executions. The optimizer uses the initial execution performance statistics to better determine a degree of parallelism for subsequent executions.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF50801) for information about `PARALLEL` hints
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG13911) for information about automatic degree of parallelism
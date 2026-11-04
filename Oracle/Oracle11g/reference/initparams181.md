---
title: PARALLEL_DEGREE_POLICY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams181.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_DEGREE_POLICY = { MANUAL \| LIMITED \| AUTO }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`PARALLEL_DEGREE_POLICY` specifies whether or not automatic degree of Parallelism, statement queuing, and in-memory parallel execution will be enabled.

Values:

Note:

Automatic degree of parallelism will be enabled regardless of the value of `PARALLEL_DEGREE_POLICY` if a `PARALLEL` hint is used at the SQL statement level.

- `MANUAL`
	Disables automatic degree of parallelism, statement queuing, and in-memory parallel execution. This reverts the behavior of parallel execution to what it was prior to Oracle Database 11g Release 2 (11.2). This is the default.
- `LIMITED`
	Enables automatic degree of parallelism for some statements but statement queuing and in-memory Parallel Execution are disabled. Automatic degree of parallelism is only applied to those statements that access tables or indexes decorated explicitly with the `DEFAULT` degree of parallelism using the `PARALLEL` clause. Statements that do not access any tables or indexes decorated with the `DEFAULT` degree of parallelism will retain the `MANUAL` behavior.
- `AUTO`
	Enables automatic degree of parallelism, statement queuing, and in-memory parallel execution.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements006.htm#SQLRF50801) for information about `PARALLEL` hints
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm) for information about automatic degree of parallelism, statement queuing, and in-memory parallel execution
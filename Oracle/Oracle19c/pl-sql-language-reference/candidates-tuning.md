---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/candidates-tuning.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Candidates for Tuning

The following kinds of PL/SQL code are very likely to benefit from tuning:

- Older code that does not take advantage of new PL/SQL language features.
	Tip:
	Before tuning older code, benchmark the current system and profile the older subprograms that your program invokes (see " [Profiling and Tracing PL/SQL Programs](profiling-and-tracing-pl-sql-programs.md) "). With the many automatic optimizations of the PL/SQL optimizer (described in " [PL/SQL Optimizer](pl-sql-optimizer.md) "), you might see performance improvements before doing any tuning.
- Older dynamic SQL statements written with the `DBMS_SQL` package.
	If you know at compile time the number and data types of the input and output variables of a dynamic SQL statement, then you can rewrite the statement in native dynamic SQL, which runs noticeably faster than equivalent code that uses the `DBMS_SQL` package (especially when it can be optimized by the compiler). For more information, see [PL/SQL Dynamic SQL](dynamic-sql.md).
- Code that spends much time processing SQL statements.
	See " [Tune SQL Statements](minimizing-cpu-overhead.md) ".
- Functions invoked in queries, which might run millions of times.
	See " [Tune Function Invocations in Queries](minimizing-cpu-overhead.md) ".
- Code that spends much time looping through query results.
	See " [Tune Loops](minimizing-cpu-overhead.md) ".
- Code that does many numeric computations.
	See " [Tune Computation-Intensive PL/SQL Code](minimizing-cpu-overhead.md) ".
- Code that spends much time processing PL/SQL statements (as opposed to issuing database definition language (DDL) statements that PL/SQL passes directly to SQL).
	See " [Compiling PL/SQL Units for Native Execution](compiling-pl-sql-units-native-execution.md) ".
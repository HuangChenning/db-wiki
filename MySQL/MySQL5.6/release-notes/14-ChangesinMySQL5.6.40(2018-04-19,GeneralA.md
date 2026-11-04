---
title: "Changes in MySQL 5.6.40 (2018-04-19, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=15"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Functionality Added or Changed
- Bugs Fixed

> Functionality Added or Changed

- If the server PID file is configured to be created in a world-writable location, the server now issues a

warning suggesting use of a more secure location. (Bug #26585560)

> Bugs Fixed

- NDB Cluster: MySQL NDB Cluster encountered race conditions compiling `lex_hash.h`. (Bug

#24931655, Bug #83477, Bug #27470071, Bug #89482)

- InnoDB: A `REPLACE` operation on a temporary table raised an assertion. (Bug #27225649, Bug

#27229072)

## MySQL 5.6 Release Notes

- InnoDB: A tablespace import operation on a server with a default row format of `REDUNDANT` raised an

assertion failure. (Bug #26960215)

- InnoDB: Evaluation of a subquery in a resolving function raised an assertion. (Bug #26909960)
- InnoDB: An online DDL operation that rebuilds the table raised an assertion when the last insert log

record to be applied was split across two pages. (Bug #26696448, Bug #87532)

- InnoDB: A `RENAME TABLE` operation that renamed the schema failed to rename full-text search

common auxiliary tables that were left behind when the full-text search index was removed previously,resulting in a assertion failure when attempting to drop the old schema. (Bug #26334149)

- Replication: A number of changes were made to the binary log decoding procedure to improve handling

of invalid or corrupted binary log entries. (Bug #24365972)

- An invalid input polygon for spatial functions could lead to undefined server behavior. Now the server

returns `NULL`. (Bug #27230859, Bug #88801)

- Adding a unique index to an `InnoDB` table on which multiple locks were held could raise an assertion.

(Bug #27216817)

- For some statements, the `FILE` privilege was not properly checked. (Bug #27160888)
- `ST_Touches()` could fail due to a missing null pointer check. (Bug #27081349)
- A multiple-insert statement on a table containing a `FULLTEXT` key and a `FTS_DOC_ID` column caused a

server error. (Bug #27041445, Bug #88267)References: This issue is a regression of: Bug #22679185.

- An `ALTER TABLE` operation attempted to set the `AUTO_INCREMENT` value for table in a discarded

tablespace. (Bug #26935001)

- Dropping an index from a system table could cause a server exit. (Bug #26881798)
- A server exit could result from simultaneous attempts by multiple threads to register and deregister

metadata Performance Schema objects. (Bug #26502135)

- The thread pool plugin logged too much information for failed connections. (Bug #26368725, Bug

#86863)

- For debug builds, using `KILL` to terminate a stored routine could raise an assertion. Thanks to Laurynas

Biveinis for the patch. (Bug #26040870, Bug #86260)

- MySQL client programs could exit unexpectedly if malformed client/server protocol packets were

received. (Bug #25471090)

- Incorrect handling by the `CONNECTION_CONTROL` plugin of an internal hash led to spurious messages in

the error log and eventual server exit. (Bug #25052009)

- Building MySQL using parallel compilation sometimes failed with an attempt to compile `sql_yacc.yy`

before `lex_token.h` had been created. (Bug #21680733, Bug #27470071, Bug #89482)

- On Windows, `sql_yacc.cc` and `sql_yacc.h` were generated twice during the build process. This can

lead to compilation failure if parallel processes are permitted. (Bug #19060850, Bug #27470071, Bug#89482)

- The `audit_log` plugin did not log placeholder values for prepared statements. (Bug #16617026)
- `NULLIF()` with a `TIMESTAMP` argument could produce truncated output. (Bug #12616286, Bug #61378)

## MySQL 5.6 Release Notes

- `MAX()` for `DATE` values smaller than year 100 produced incorrect results. (Bug #12546797, Bug #61100)
- Compilation could fail due to a missing dependency on `lex_token.h` for `sql_yacc.cc.o`. (Bug

#76235, Bug #20678411, Bug #27470071, Bug #89482)

- A `WHERE` condition of the form `column_value < ALL (select_expression)` did not always

evaluate as `TRUE` when the `select_expression` did not return any rows. (Bug #61799, Bug#12762381)

- The optimizer incorrectly optimized away a subquery selecting a `MIN()` or `MAX()` expression even when

the subquery was correlated with or depended on an outer reference. An example of such a query is shown here:

```
SELECT (
SELECT MIN(42) FROM t2 WHERE t2.pk = t1.pk
) AS scalar_subqry
FROM t1;
```

In this case, the optimizer reduced `SELECT MIN(42) FROM T2` to a constant value (42), and the correlation predicate `WHERE T2.pk = T1.pk` was never checked during query execution. (If the predicate were executed, it would not have qualifed any rows from the subquery, and would have evaluated as `NULL`.) (Bug #53485, Bug #11761032)

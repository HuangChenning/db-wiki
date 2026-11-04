---
title: "Changes in MySQL 5.6.33 (2016-09-06, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=31"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Compilation Notes

## MySQL 5.6 Release Notes

- Test Suite Notes
- Bugs Fixed

> Compilation Notes

- `CMake` support was added for compiling with Developer Studio 12.5. (Bug #82249, Bug #24303829, Bug

#81274, Bug #23212938)

> Test Suite Notes

- In `mysql-test-run.pl`, a limit of 50 was imposed on the number of workers for parallel testing, which

on systems with more than 50 CPUs resulted in exhaustion of unique thread IDs. The ID-exhaustion problem has been corrected, and the limit of 50 on number of workers has been lifted. Thanks to Daniel Black for the patch on which this change was based. Additionally, these changes were made:

- To avoid idle workers, the number of parallel workers now is limited to the number of tests.
- Previously, if `--parallel=auto` was given and the `MTR_MAX_PARALLEL` environment variable was

not set, a limit of 8 was imposed on the number of parallel workers. This limit has been lifted.

(Bug #22342399, Bug #79585)

> Bugs Fixed

- InnoDB: An operation that dropped and created a full-text search table raised an assertion. (Bug

#24315031)

- InnoDB: Accessing full-text search auxiliary tables while dropping the indexed table raised an assertion.

(Bug #24009272)

- InnoDB: An online DDL operation on a table with indexed `BLOB` columns raised an assertion during

logging of table modifications. (Bug #23760086)

- Replication: `mysqlbinlog --read-from-remote-server log1 log2` was opening a new

connection for `log2` without freeing the connection used for `log1`. Thanks to Laurynas Biveinis for the contribution. (Bug #81675, Bug #23540182)

- Replication: With `binlog_row_image=FULL`, when updating single tables temporary tables were

unnecessarily being used. The fix ensures single table update follows the same pattern as multi-table update. (Bug #79867, Bug #22510353)

- For `mysqld_safe`, the argument to `--malloc-lib` now must be one of the directories `/usr/lib`, /

`usr/lib64`, `/usr/lib/i386-linux-gnu`, or `/usr/lib/x86_64-linux-gnu`. In addition, the `--``mysqld` and `--mysqld-version` options are accepted only on the command line, not in option files.

(Bug #24464380)References: See also: Bug #24619033, Bug #82920.

- It was possible to write log files ending with `.ini` or `.cnf` that later could be parsed as option files. The

general query log and slow query log can no longer be written to a file ending with `.ini` or `.cnf`. (Bug#24388753)

- Privilege escalation was possible by exploiting the way `REPAIR TABLE` used temporary files. (Bug

#24388746)

- If the `basedir` system variable was set at server startup from the command line or option file, the value

was not normalized (on Windows, / was not replaced with \). (Bug #23747899, Bug #82125)

## MySQL 5.6 Release Notes

- In-place `ALTER TABLE` operations which when executed separately caused no table rebuild could when

combined into a single statement result in a table rebuild. (Bug #23475211, Bug #81587)

- A blank server name in `CREATE SERVER` statements produced a server exit rather than an error. (Bug

#23295288)

- A prepared statement that used a parameter in the select list of a derived table that was part of a join

could cause a server exit. (Bug #22392374, Bug #24380263)

- `MEDIUMINT` columns used in operations with long integer values could result in buffer overflow. (Bug

#19984392)

- A spurious `ER_NO_SUCH_TABLE` error could occur when attempting to execute a prepared `CREATE`

`TABLE ... SELECT` statement that used a temporary table in the `FROM` clause and called a stored function. The same error could occur for a nonprepared version of the statement if used in a stored procedure when the procedure was re-executed. (Bug #16672723, Bug #68972)

- `EINTR` handling in the client library has been fixed so that interrupted read and write calls are retried.

Previously, `EINTR` was ignored. (Bug #82019, Bug #23703570)

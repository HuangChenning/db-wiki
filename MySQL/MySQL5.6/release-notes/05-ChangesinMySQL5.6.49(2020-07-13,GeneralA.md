---
title: "Changes in MySQL 5.6.49 (2020-07-13, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=5"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Configuration Notes
- Security Notes
- Bugs Fixed

> Configuration Notes

- `tcmalloc` is no longer a permitted value for the `mysqld_safe` `--malloc-lib` option. (Bug

#31372027)

> Security Notes

- Incompatible Change: Access to the `INFORMATION_SCHEMA.FILES` table now requires the `PROCESS`

privilege.

This change affects users of the `mysqldump` command, which accesses tablespace information in the`FILES` table, and thus now requires the `PROCESS` privilege as well. Users who do not need to dump tablespace information can work around this requirement by invoking `mysqldump` with the `--no-``tablespaces` option. (Bug #30350829)

- The linked OpenSSL library for MySQL Server has been updated to version 1.1.1g. Issues fixed

in the new OpenSSL version are described at https://www.openssl.org/news/cl111.txt and https://www.openssl.org/news/vulnerabilities.html. (Bug #31296697)

> Bugs Fixed

- Partitioning: A query against a partitioned table, which used an `ORDER BY`, returned unordered results

under the following conditions:

- The table had a composite index with a prefix on one of the columns.
- The query's `WHERE` clause contained an equality condition on the prefixed column.
- The column with the prefix was the leftmost column in the index.
- The column used in the `ORDER BY` was the rightmost column in the index.

## MySQL 5.6 Release Notes

- The index was used for handling the `ORDER BY`.

Our thanks to Quanan Han for the suggestion. (Bug #84070, Bug #25207522)

- Replication: When a replication source server shuts down and restarts, its `MEMORY` tables become

empty. To replicate this effect to replicas, the first time that the source uses a given `MEMORY` table after startup, it notifies replicas that the table must be emptied by writing a `DELETE` statement for that table to the binary log. Previously, the generated `DELETE` statement was written to the binary log statement cache for the current session, which could result in it being logged together with other statements under the same GTID, or logged without `BEGIN` and `COMMIT` statements. Also, in some situations, the generated `DELETE` statement could consume the GTID intended for the transaction that triggered it. The generated `DELETE` statement is now logged with accompanying `BEGIN` and `COMMIT` statements, and the resulting transaction is flushed to the binary log immediately after it is written to the statement cache, so that it always receives its own GTID and is kept separate from other transactions. (Bug #30527929, Bug#25681518, Bug #77729)

- `mysql_store_result()` could fail to detect invalid data packets. (Bug #29921423)
- The server sometimes mistakenly removed a subquery with a `GROUP BY` when optimizing a query, even

in some cases when this subquery was used by an outer select. This could occur when the subquery also used an aggregate function. (Bug #28240054)

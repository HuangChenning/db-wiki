---
title: "10.5.3 Optimizing InnoDB Read-Only Transactions"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-performance-ro-txn.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 10.5.3 Optimizing InnoDB Read-Only Transactions

`InnoDB` can avoid the overhead associated with setting up the [transaction ID](glossary.md) (`TRX_ID` field) for transactions that are known to be read-only. A transaction ID is only needed for a [transaction](glossary.md) that might perform write operations or [locking reads](glossary.md) such as `SELECT ... FOR UPDATE`. Eliminating unnecessary transaction IDs reduces the size of internal data structures that are consulted each time a query or data change statement constructs a [read view](glossary.md).

`InnoDB` detects read-only transactions when:

- The transaction is started with the [`START TRANSACTION             READ ONLY`](commit.md) statement. In this case, attempting to make changes to the database (for `InnoDB`, `MyISAM`, or other types of tables) causes an error, and the transaction continues in read-only state:
	```
	ERROR 1792 (25006): Cannot execute statement in a READ ONLY transaction.
	```
	You can still make changes to session-specific temporary tables in a read-only transaction, or issue locking queries for them, because those changes and locks are not visible to any other transaction.
- The [`autocommit`](server-system-variables.md) setting is turned on, so that the transaction is guaranteed to be a single statement, and the single statement making up the transaction is a “non-locking” [`SELECT`](select.md) statement. That is, a `SELECT` that does not use a `FOR             UPDATE` or `LOCK IN SHARED MODE` clause.
- The transaction is started without the `READ             ONLY` option, but no updates or statements that explicitly lock rows have been executed yet. Until updates or explicit locks are required, a transaction stays in read-only mode.

Thus, for a read-intensive application such as a report generator, you can tune a sequence of `InnoDB` queries by grouping them inside [`START TRANSACTION READ         ONLY`](commit.md) and [`COMMIT`](commit.md), or by turning on the [`autocommit`](server-system-variables.md) setting before running the `SELECT` statements, or simply by avoiding any data change statements interspersed with the queries.

For information about [`START         TRANSACTION`](commit.md) and [`autocommit`](server-system-variables.md), see [Section 15.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”](commit.md).

Note

Transactions that qualify as auto-commit, non-locking, and read-only (AC-NL-RO) are kept out of certain internal `InnoDB` data structures and are therefore not listed in [`SHOW ENGINE           INNODB STATUS`](show-engine.md) output.
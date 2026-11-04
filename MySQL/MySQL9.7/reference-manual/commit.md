---
title: "15.3.1 START TRANSACTION, COMMIT, and ROLLBACK Statements"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/commit.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.3.1 START TRANSACTION, COMMIT, and ROLLBACK Statements

```
START TRANSACTION
    [transaction_characteristic [, transaction_characteristic] ...]

transaction_characteristic: {
    WITH CONSISTENT SNAPSHOT
  | READ WRITE
  | READ ONLY
}

BEGIN [WORK]
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
SET autocommit = {0 | 1}
```

These statements provide control over use of [transactions](glossary.md):

- `START TRANSACTION` or `BEGIN` start a new transaction.
- `COMMIT` commits the current transaction, making its changes permanent.
- `ROLLBACK` rolls back the current transaction, canceling its changes.
- `SET autocommit` disables or enables the default autocommit mode for the current session.

By default, MySQL runs with [autocommit](glossary.md) mode enabled. This means that, when not otherwise inside a transaction, each statement is atomic, as if it were surrounded by `START       TRANSACTION` and `COMMIT`. You cannot use `ROLLBACK` to undo the effect; however, if an error occurs during statement execution, the statement is rolled back.

To disable autocommit mode implicitly for a single series of statements, use the `START TRANSACTION` statement:

```
START TRANSACTION;
SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
UPDATE table2 SET summary=@A WHERE type=1;
COMMIT;
```

With `START TRANSACTION`, autocommit remains disabled until you end the transaction with `COMMIT` or `ROLLBACK`. The autocommit mode then reverts to its previous state.

`START TRANSACTION` permits several modifiers that control transaction characteristics. To specify multiple modifiers, separate them by commas.

- The `WITH CONSISTENT SNAPSHOT` modifier starts a [consistent read](glossary.md) for storage engines that are capable of it. This applies only to `InnoDB`. The effect is the same as issuing a `START TRANSACTION` followed by a [`SELECT`](select.md) from any `InnoDB` table. See [Section 17.7.2.3, “Consistent Nonlocking Reads”](innodb-consistent-read.md). The `WITH           CONSISTENT SNAPSHOT` modifier does not change the current transaction [isolation level](glossary.md), so it provides a consistent snapshot only if the current isolation level is one that permits a consistent read. The only isolation level that permits a consistent read is [`REPEATABLE READ`](innodb-transaction-isolation-levels.md). For all other isolation levels, the `WITH CONSISTENT           SNAPSHOT` clause is ignored. A warning is generated when the `WITH CONSISTENT SNAPSHOT` clause is ignored.
- The `READ WRITE` and `READ           ONLY` modifiers set the transaction access mode. They permit or prohibit changes to tables used in the transaction. The `READ ONLY` restriction prevents the transaction from modifying or locking both transactional and nontransactional tables that are visible to other transactions; the transaction can still modify or lock temporary tables.
	MySQL enables extra optimizations for queries on `InnoDB` tables when the transaction is known to be read-only. Specifying `READ ONLY` ensures these optimizations are applied in cases where the read-only status cannot be determined automatically. See [Section 10.5.3, “Optimizing InnoDB Read-Only Transactions”](innodb-performance-ro-txn.md) for more information.
	If no access mode is specified, the default mode applies. Unless the default has been changed, it is read/write. It is not permitted to specify both `READ WRITE` and `READ ONLY` in the same statement.
	In read-only mode, it remains possible to change tables created with the `TEMPORARY` keyword using DML statements. Changes made with DDL statements are not permitted, just as with permanent tables.
	For additional information about transaction access mode, including ways to change the default mode, see [Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md).
	If the [`read_only`](server-system-variables.md) system variable is enabled, explicitly starting a transaction with `START TRANSACTION READ WRITE` requires the [`CONNECTION_ADMIN`](privileges-provided.md) privilege (or the deprecated [`SUPER`](privileges-provided.md) privilege).

Important

Many APIs used for writing MySQL client applications (such as JDBC) provide their own methods for starting transactions that can (and sometimes should) be used instead of sending a `START TRANSACTION` statement from the client. See [Chapter 31, *Connectors and APIs*](connectors-apis.md), or the documentation for your API, for more information.

To disable autocommit mode explicitly, use the following statement:

```
SET autocommit=0;
```

After disabling autocommit mode by setting the [`autocommit`](server-system-variables.md) variable to zero, changes to transaction-safe tables (such as those for [`InnoDB`](innodb-storage-engine.md) or [`NDB`](mysql-cluster.md)) are not made permanent immediately. You must use `COMMIT` to store your changes to disk or `ROLLBACK` to ignore the changes.

[`autocommit`](server-system-variables.md) is a session variable and must be set for each session. To disable autocommit mode for each new connection, see the description of the [`autocommit`](server-system-variables.md) system variable at [Section 7.1.8, “Server System Variables”](server-system-variables.md).

`BEGIN` and `BEGIN WORK` are supported as aliases of `START TRANSACTION` for initiating a transaction. `START TRANSACTION` is standard SQL syntax, is the recommended way to start an ad-hoc transaction, and permits modifiers that `BEGIN` does not.

The `BEGIN` statement differs from the use of the `BEGIN` keyword that starts a [`BEGIN ... END`](begin-end.md) compound statement. The latter does not begin a transaction. See [Section 15.6.1, “BEGIN... END Compound Statement”](begin-end.md).

Note

Within all stored programs (stored procedures and functions, triggers, and events), the parser treats `BEGIN         [WORK]` as the beginning of a [`BEGIN ...         END`](begin-end.md) block. Begin a transaction in this context with `START         TRANSACTION` instead.

The optional `WORK` keyword is supported for `COMMIT` and `ROLLBACK`, as are the `CHAIN` and `RELEASE` clauses. `CHAIN` and `RELEASE` can be used for additional control over transaction completion. The value of the [`completion_type`](server-system-variables.md) system variable determines the default completion behavior. See [Section 7.1.8, “Server System Variables”](server-system-variables.md).

The `AND CHAIN` clause causes a new transaction to begin as soon as the current one ends, and the new transaction has the same isolation level as the just-terminated transaction. The new transaction also uses the same access mode (`READ       WRITE` or `READ ONLY`) as the just-terminated transaction. The `RELEASE` clause causes the server to disconnect the current client session after terminating the current transaction. Including the `NO` keyword suppresses `CHAIN` or `RELEASE` completion, which can be useful if the [`completion_type`](server-system-variables.md) system variable is set to cause chaining or release completion by default.

Beginning a transaction causes any pending transaction to be committed. See [Section 15.3.3, “Statements That Cause an Implicit Commit”](implicit-commit.md), for more information.

Beginning a transaction also causes table locks acquired with [`LOCK TABLES`](lock-tables.md) to be released, as though you had executed [`UNLOCK       TABLES`](lock-tables.md). Beginning a transaction does not release a global read lock acquired with [`FLUSH TABLES       WITH READ LOCK`](flush.md).

For best results, transactions should be performed using only tables managed by a single transaction-safe storage engine. Otherwise, the following problems can occur:

- If you use tables from more than one transaction-safe storage engine (such as `InnoDB`), and the transaction isolation level is not [`SERIALIZABLE`](innodb-transaction-isolation-levels.md), it is possible that when one transaction commits, another ongoing transaction that uses the same tables sees only some of the changes made by the first transaction. That is, the atomicity of transactions is not guaranteed with mixed engines and inconsistencies can result. (If mixed-engine transactions are infrequent, you can use [`SET           TRANSACTION ISOLATION LEVEL`](set-transaction.md) to set the isolation level to [`SERIALIZABLE`](innodb-transaction-isolation-levels.md) on a per-transaction basis as necessary.)
- If you use tables that are not transaction-safe within a transaction, changes to those tables are stored at once, regardless of the status of autocommit mode.
- If you issue a `ROLLBACK` statement after updating a nontransactional table within a transaction, an [`ER_WARNING_NOT_COMPLETE_ROLLBACK`](https://docs.oracle.com/cd/E17952_01/mysql-errors-9.7-en/server-error-reference.html#error_er_warning_not_complete_rollback) warning occurs. Changes to transaction-safe tables are rolled back, but not changes to nontransaction-safe tables.

Each transaction is stored in the binary log in one chunk, upon `COMMIT`. Transactions that are rolled back are not logged. (**Exception**: Modifications to nontransactional tables cannot be rolled back. If a transaction that is rolled back includes modifications to nontransactional tables, the entire transaction is logged with a `ROLLBACK` statement at the end to ensure that modifications to the nontransactional tables are replicated.) See [Section 7.4.4, “The Binary Log”](binary-log.md).

You can change the isolation level or access mode for transactions with the [`SET TRANSACTION`](set-transaction.md) statement. See [Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md).

Rolling back can be a slow operation that may occur implicitly without the user having explicitly asked for it (for example, when an error occurs). Because of this, [`SHOW       PROCESSLIST`](show-processlist.md) displays `Rolling back` in the `State` column for the session, not only for explicit rollbacks performed with the `ROLLBACK` statement but also for implicit rollbacks.

Note

In MySQL 9.7, `BEGIN`, `COMMIT`, and `ROLLBACK` are not affected by [`--replicate-do-db`](replication-options-replica.md) or [`--replicate-ignore-db`](replication-options-replica.md) rules.

When `InnoDB` performs a complete rollback of a transaction, all locks set by the transaction are released. If a single SQL statement within a transaction rolls back as a result of an error, such as a duplicate key error, locks set by the statement are preserved while the transaction remains active. This happens because `InnoDB` stores row locks in a format such that it cannot know afterward which lock was set by which statement.

If a [`SELECT`](select.md) statement within a transaction calls a stored function, and a statement within the stored function fails, that statement rolls back. If `ROLLBACK` is executed for the transaction subsequently, the entire transaction rolls back.
---
title: "17.7.5 Deadlocks in InnoDB"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-deadlocks.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.7.5 Deadlocks in InnoDB

A deadlock is a situation in which multiple transactions are unable to proceed because each transaction holds a lock that is needed by another one. Because all transactions involved are waiting for the same resource to become available, none of them ever releases the lock it holds.

A deadlock can occur when transactions lock rows in multiple tables (through statements such as [`UPDATE`](update.md) or [`SELECT ... FOR       UPDATE`](select.md)), but in the opposite order. A deadlock can also occur when such statements lock ranges of index records and gaps, with each transaction acquiring some locks but not others due to a timing issue. For a deadlock example, see [Section 17.7.5.1, “An InnoDB Deadlock Example”](innodb-deadlock-example.md).

To reduce the possibility of deadlocks, use transactions rather than [`LOCK TABLES`](lock-tables.md) statements; keep transactions that insert or update data small enough that they do not stay open for long periods of time; when different transactions update multiple tables or large ranges of rows, use the same order of operations (such as [`SELECT ... FOR       UPDATE`](select.md)) in each transaction; create indexes on the columns used in [`SELECT ...       FOR UPDATE`](select.md) and [`UPDATE ... WHERE`](update.md) statements. The possibility of deadlocks is not affected by the isolation level, because the isolation level changes the behavior of read operations, while deadlocks occur because of write operations. For more information about avoiding and recovering from deadlock conditions, see [Section 17.7.5.3, “How to Minimize and Handle Deadlocks”](innodb-deadlocks-handling.md).

When deadlock detection is enabled (the default) and a deadlock does occur, `InnoDB` detects the condition and rolls back one of the transactions (the victim). If deadlock detection is disabled using the [`innodb_deadlock_detect`](innodb-parameters.md) variable, `InnoDB` relies on the [`innodb_lock_wait_timeout`](innodb-parameters.md) setting to roll back transactions in case of a deadlock. Thus, even if your application logic is correct, you must still handle the case where a transaction must be retried. To view the last deadlock in an `InnoDB` user transaction, use [`SHOW ENGINE INNODB       STATUS`](show-engine.md). If frequent deadlocks highlight a problem with transaction structure or application error handling, enable [`innodb_print_all_deadlocks`](innodb-parameters.md) to print information about all deadlocks to the [**mysqld**](mysqld.md) error log. For more information about how deadlocks are automatically detected and handled, see [Section 17.7.5.2, “Deadlock Detection”](innodb-deadlock-detection.md).
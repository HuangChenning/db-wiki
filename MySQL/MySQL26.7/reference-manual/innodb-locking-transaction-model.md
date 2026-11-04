---
title: "MySQL :: MySQL 26.7 Reference Manual :: 17.7 InnoDB Locking and Transaction Model"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/innodb-locking-transaction-model.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 17.7 InnoDB Locking and Transaction Model

To implement a large-scale, busy, or highly reliable database application, to port substantial code from a different database system, or to tune MySQL performance, it is important to understand `InnoDB` locking and the `InnoDB` transaction model.

This section discusses several topics related to `InnoDB` locking and the `InnoDB` transaction model with which you should be familiar.

- [Section 17.7.1, “InnoDB Locking”](innodb-locking.md) describes lock types used by `InnoDB`.
- [Section 17.7.2, “InnoDB Transaction Model”](innodb-transaction-model.md) describes transaction isolation levels and the locking strategies used by each. It also discusses the use of [`autocommit`](server-system-variables.md), consistent non-locking reads, and locking reads.
- [Section 17.7.3, “Locks Set by Different SQL Statements in InnoDB”](innodb-locks-set.md) discusses specific types of locks set in `InnoDB` for various statements.
- [Section 17.7.4, “Phantom Rows”](innodb-next-key-locking.md) describes how `InnoDB` uses next-key locking to avoid phantom rows.
- [Section 17.7.5, “Deadlocks in InnoDB”](innodb-deadlocks.md) provides a deadlock example, discusses deadlock detection, and provides tips for minimizing and handling deadlocks in `InnoDB`.
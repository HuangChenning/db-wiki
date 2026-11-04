---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.11.2 Table Locking Issues"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/table-locking.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 10.11.2 Table Locking Issues

`InnoDB` tables use row-level locking so that multiple sessions and applications can read from and write to the same table simultaneously, without making each other wait or producing inconsistent results. For this storage engine, avoid using the [`LOCK TABLES`](lock-tables.md) statement, because it does not offer any extra protection, but instead reduces concurrency. The automatic row-level locking makes these tables suitable for your busiest databases with your most important data, while also simplifying application logic since you do not need to lock and unlock tables. Consequently, the `InnoDB` storage engine is the default in MySQL.

MySQL uses table locking (instead of page, row, or column locking) for all storage engines except `InnoDB`. The locking operations themselves do not have much overhead. But because only one session can write to a table at any one time, for best performance with these other storage engines, use them primarily for tables that are queried often and rarely inserted into or updated.

#### Performance Considerations Favoring InnoDB

When choosing whether to create a table using `InnoDB` or a different storage engine, keep in mind the following disadvantages of table locking:

- Table locking enables many sessions to read from a table at the same time, but if a session wants to write to a table, it must first get exclusive access, meaning it might have to wait for other sessions to finish with the table first. During the update, all other sessions that want to access this particular table must wait until the update is done.
- Table locking causes problems when a session is waiting because the disk is full and free space needs to become available before the session can proceed. In this case, all sessions that want to access the problem table are also put in a waiting state until more disk space is made available.
- A [`SELECT`](select.md) statement that takes a long time to run prevents other sessions from updating the table in the meantime, making the other sessions appear slow or unresponsive. While a session is waiting to get exclusive access to the table for updates, other sessions that issue [`SELECT`](select.md) statements queue up behind it, reducing concurrency even for read-only sessions.

#### Workarounds for Locking Performance Issues

The following items describe some ways to avoid or reduce contention caused by table locking:

- Consider switching the table to the `InnoDB` storage engine, either using `CREATE TABLE ... ENGINE=INNODB` during setup, or using `ALTER TABLE ...               ENGINE=INNODB` for an existing table. See [Chapter 17, *The InnoDB Storage Engine*](innodb-storage-engine.md) for more details about this storage engine.
- Optimize [`SELECT`](select.md) statements to run faster so that they lock tables for a shorter time. You might have to create some summary tables to do this.
- Start [**mysqld**](mysqld.md) with [`--low-priority-updates`](server-system-variables.md). For storage engines that use only table-level locking (such as `MyISAM`, `MEMORY`, and `MERGE`), this gives all statements that update (modify) a table lower priority than [`SELECT`](select.md) statements. In this case, the second [`SELECT`](select.md) statement in the preceding scenario would execute before the [`UPDATE`](update.md) statement, and would not wait for the first [`SELECT`](select.md) to finish.
- To specify that all updates issued in a specific connection should be done with low priority, set the [`low_priority_updates`](server-system-variables.md) server system variable equal to 1.
- To give a specific [`INSERT`](insert.md), [`UPDATE`](update.md), or [`DELETE`](delete.md) statement lower priority, use the `LOW_PRIORITY` attribute.
- To give a specific [`SELECT`](select.md) statement higher priority, use the `HIGH_PRIORITY` attribute. See [Section 15.2.13, “SELECT Statement”](select.md).
- Start [**mysqld**](mysqld.md) with a low value for the [`max_write_lock_count`](server-system-variables.md) system variable to force MySQL to temporarily elevate the priority of all [`SELECT`](select.md) statements that are waiting for a table after a specific number of write locks to the table occur (for example, for insert operations). This permits read locks after a certain number of write locks.
- If you have problems with mixed [`SELECT`](select.md) and [`DELETE`](delete.md) statements, the `LIMIT` option to [`DELETE`](delete.md) may help. See [Section 15.2.2, “DELETE Statement”](delete.md).
- Using `SQL_BUFFER_RESULT` with [`SELECT`](select.md) statements can help to make the duration of table locks shorter. See [Section 15.2.13, “SELECT Statement”](select.md).
- Splitting table contents into separate tables may help, by allowing queries to run against columns in one table, while updates are confined to columns in a different table.
- You could change the locking code in `mysys/thr_lock.c` to use a single queue. In this case, write locks and read locks would have the same priority, which might help some applications.
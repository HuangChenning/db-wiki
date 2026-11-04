---
title: "17.2 InnoDB and the ACID Model"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-acid.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

The [ACID](glossary.md) model is a set of database design principles that emphasize aspects of reliability that are important for business data and mission-critical applications. MySQL includes components such as the `InnoDB` storage engine that adhere closely to the ACID model so that data is not corrupted and results are not distorted by exceptional conditions such as software crashes and hardware malfunctions. When you rely on ACID-compliant features, you do not need to reinvent the wheel of consistency checking and crash recovery mechanisms. In cases where you have additional software safeguards, ultra-reliable hardware, or an application that can tolerate a small amount of data loss or inconsistency, you can adjust MySQL settings to trade some of the ACID reliability for greater performance or throughput.

The following sections discuss how MySQL features, in particular the `InnoDB` storage engine, interact with the categories of the ACID model:

- **A**: atomicity.
- **C**: consistency.
- **I:**: isolation.
- **D**: durability.

### Atomicity

The **atomicity** aspect of the ACID model mainly involves `InnoDB` [transactions](glossary.md). Related MySQL features include:

- The [`autocommit`](server-system-variables.md) setting.
- The [`COMMIT`](commit.md) statement.
- The [`ROLLBACK`](commit.md) statement.

### Consistency

The **consistency** aspect of the ACID model mainly involves internal `InnoDB` processing to protect data from crashes. Related MySQL features include:

- The `InnoDB` doublewrite buffer. See [Section 17.6.4, “Doublewrite Buffer”](innodb-doublewrite-buffer.md).
- `InnoDB` crash recovery. See [InnoDB Crash Recovery](innodb-recovery.md).

### Isolation

The **isolation** aspect of the ACID model mainly involves `InnoDB` [transactions](glossary.md), in particular the [isolation level](glossary.md) that applies to each transaction. Related MySQL features include:

- The [`autocommit`](server-system-variables.md) setting.
- Transaction isolation levels and the [`SET         TRANSACTION`](set-transaction.md) statement. See [Section 17.7.2.1, “Transaction Isolation Levels”](innodb-transaction-isolation-levels.md).
- The low-level details of `InnoDB` [locking](glossary.md). Details can be viewed in the `INFORMATION_SCHEMA` tables (see [Section 17.15.2, “InnoDB INFORMATION\_SCHEMA Transaction and Locking Information”](innodb-information-schema-transactions.md)) and Performance Schema [`data_locks`](performance-schema-data-locks-table.md) and [`data_lock_waits`](performance-schema-data-lock-waits-table.md) tables.

### Durability

The **durability** aspect of the ACID model involves MySQL software features interacting with your particular hardware configuration. Because of the many possibilities depending on the capabilities of your CPU, network, and storage devices, this aspect is the most complicated to provide concrete guidelines for. (And those guidelines might take the form of “buy new hardware”.) Related MySQL features include:

- The `InnoDB` doublewrite buffer. See [Section 17.6.4, “Doublewrite Buffer”](innodb-doublewrite-buffer.md).
- The [`innodb_flush_log_at_trx_commit`](innodb-parameters.md) variable.
- The [`sync_binlog`](replication-options-binary-log.md) variable.
- The [`innodb_file_per_table`](innodb-parameters.md) variable.
- The write buffer in a storage device, such as a disk drive, SSD, or RAID array.
- A battery-backed cache in a storage device.
- The operating system used to run MySQL, in particular its support for the `fsync()` system call.
- An uninterruptible power supply (UPS) protecting the electrical power to all computer servers and storage devices that run MySQL servers and store MySQL data.
- Your backup strategy, such as frequency and types of backups, and backup retention periods.
- For distributed or hosted data applications, the particular characteristics of the data centers where the hardware for the MySQL servers is located, and network connections between the data centers.
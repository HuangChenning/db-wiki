---
title: "MySQL :: MySQL 26.7 Reference Manual :: Transaction Isolation Level Index"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/dynindex-isolevel.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## Transaction Isolation Level Index

R | S

### READ COMMITTED

[Section 17.7.2.3, “Consistent Nonlocking Reads”](innodb-consistent-read.md)

[Section 25.4.3.6, “Defining NDB Cluster Data Nodes”](mysql-cluster-ndbd-definition.md)

[Section 25.2.6.1, “Differences Between the NDB and InnoDB Storage Engines”](mysql-cluster-ndb-innodb-engines.md)

[Section 20.3.2, “Group Replication Limitations”](group-replication-limitations.md)

[Section 17.7.5.3, “How to Minimize and Handle Deadlocks”](innodb-deadlocks-handling.md)

[Section 17.7.1, “InnoDB Locking”](innodb-locking.md)

[Section 25.2.7.3, “Limits Relating to Transaction Handling in NDB Cluster”](mysql-cluster-limitations-transactions.md)

[Section 17.7.3, “Locks Set by Different SQL Statements in InnoDB”](innodb-locks-set.md)

[Section A.1, “MySQL 26.7 FAQ: General”](faqs-general.md)

[Section A.10, “MySQL 26.7 FAQ: NDB Cluster”](faqs-mysql-cluster.md)

[Section 25.2.6.3, “NDB and InnoDB Feature Usage Summary”](mysql-cluster-ndb-innodb-usage.md)

[Section 10.5.2, “Optimizing InnoDB Transaction Management”](optimizing-innodb-transaction-management.md)

[Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md)

[Section 7.4.4.2, “Setting The Binary Log Format”](binary-log-setting.md)

[Section 29.12.7.1, “The events\_transactions\_current Table”](performance-schema-events-transactions-current-table.md)

[Section 17.7.2.1, “Transaction Isolation Levels”](innodb-transaction-isolation-levels.md)

### REPEATABLE READ

[Section 17.7.2.3, “Consistent Nonlocking Reads”](innodb-consistent-read.md)

[Section 20.3.2, “Group Replication Limitations”](group-replication-limitations.md)

[Section 17.7.1, “InnoDB Locking”](innodb-locking.md)

[Section 25.2.7.3, “Limits Relating to Transaction Handling in NDB Cluster”](mysql-cluster-limitations-transactions.md)

[Section 7.4.4.3, “Mixed Binary Logging Format”](binary-log-mixed.md)

[Section 6.5.4, “mysqldump — A Database Backup Program”](mysqldump.md)

[Section 10.5.2, “Optimizing InnoDB Transaction Management”](optimizing-innodb-transaction-management.md)

[Section 29.12.7, “Performance Schema Transaction Tables”](performance-schema-transaction-tables.md)

[Section 17.8.9, “Purge Configuration”](innodb-purge-configuration.md)

[Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md)

[Section 15.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”](commit.md)

[Section 29.12.7.1, “The events\_transactions\_current Table”](performance-schema-events-transactions-current-table.md)

[Section 17.7.2.1, “Transaction Isolation Levels”](innodb-transaction-isolation-levels.md)

[Section 15.3.8, “XA Transactions”](xa.md)

### SERIALIZABLE

[Section 8.2.3, “Grant Tables”](grant-tables.md)

[Section 20.3.2, “Group Replication Limitations”](group-replication-limitations.md)

[Section 17.7.1, “InnoDB Locking”](innodb-locking.md)

[Section 25.2.7.3, “Limits Relating to Transaction Handling in NDB Cluster”](mysql-cluster-limitations-transactions.md)

[Section 17.7.3, “Locks Set by Different SQL Statements in InnoDB”](innodb-locks-set.md)

[Section 7.4.4.3, “Mixed Binary Logging Format”](binary-log-mixed.md)

[Section 29.12.7, “Performance Schema Transaction Tables”](performance-schema-transaction-tables.md)

[Section 7.1.7, “Server Command Options”](server-options.md)

[Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md)

[Section 15.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”](commit.md)

[Section 29.12.7.1, “The events\_transactions\_current Table”](performance-schema-events-transactions-current-table.md)

[Section 17.7.2.1, “Transaction Isolation Levels”](innodb-transaction-isolation-levels.md)

[Section 15.3.8, “XA Transactions”](xa.md)
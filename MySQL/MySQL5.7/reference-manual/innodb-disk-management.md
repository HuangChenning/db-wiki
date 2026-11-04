---
title: "14.12 InnoDB Disk I/O and File Space Management"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-disk-management.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

As a DBA, you must manage disk I/O to keep the I/O subsystem from becoming saturated, and manage disk space to avoid filling up storage devices. The [ACID](glossary.md) design model requires a certain amount of I/O that might seem redundant, but helps to ensure data reliability. Within these constraints, `InnoDB` tries to optimize the database work and the organization of disk files to minimize the amount of disk I/O. Sometimes, I/O is postponed until the database is not busy, or until everything needs to be brought to a consistent state, such as during a database restart after a [fast shutdown](glossary.md).

This section discusses the main considerations for I/O and disk space with the default kind of MySQL tables (also known as `InnoDB` tables):

- Controlling the amount of background I/O used to improve query performance.
- Enabling or disabling features that provide extra durability at the expense of additional I/O.
- Organizing tables into many small files, a few larger files, or a combination of both.
- Balancing the size of redo log files against the I/O activity that occurs when the log files become full.
- How to reorganize a table for optimal query performance.
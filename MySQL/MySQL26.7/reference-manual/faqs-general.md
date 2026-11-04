---
title: "MySQL :: MySQL 26.7 Reference Manual :: A.1 MySQL 26.7 FAQ: General"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/faqs-general.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## A.1 MySQL 26.7 FAQ: General

A.1.1. Which version of MySQL is production-ready (GA)?

A.1.2. Why did MySQL version numbering skip versions 6 and 7 and go straight to 8.0?

A.1.3. Can MySQL do subqueries?

A.1.4. Can MySQL perform multiple-table inserts, updates, and deletes?

A.1.5. Does MySQL have Sequences?

A.1.6. Does MySQL have a NOW() function with fractions of seconds?

A.1.7. Does MySQL work with multi-core processors?

A.1.8. Why do I see multiple processes for mysqld?

A.1.9. Can MySQL perform ACID transactions?

| **A.1.1.** | Which version of MySQL is production-ready (GA)? |
| --- | --- |
|  | MySQL 26.10, 8.4, and 8.0 are actively supported for production use.  The MySQL 9 Innovation series began with the MySQL 9.0.0 release on 01 July 2024.  The MySQL 8.4 LTS series began with the MySQL 8.4.0 release on 30 April 2024.  The MySQL 8 Innovation series began with the MySQL 8.1.0 release on 18 July 2023. Active development ended on 2024-01-16 with the MySQL 8.3.0 release.  MySQL 8.0 achieved General Availability (GA) status with MySQL 8.0.11, which was released for production use on 19 April 2018. It became a bugfix series as of MySQL 8.0.34 with the introduction of the [Innovation and LTS release model](mysql-releases.md).  MySQL 5.7 achieved General Availability (GA) status with MySQL 5.7.9, which was released for production use on 21 October 2015. Active development for MySQL 5.7 ended on 25 October 2023 with the MySQL 5.7.44 release.  MySQL 5.6 achieved General Availability (GA) status with MySQL 5.6.10, which was released for production use on 5 February 2013. Active development for MySQL 5.6 has ended.  MySQL 5.5 achieved General Availability (GA) status with MySQL 5.5.8, which was released for production use on 3 December 2010. Active development for MySQL 5.5 has ended.  MySQL 5.1 achieved General Availability (GA) status with MySQL 5.1.30, which was released for production use on 14 November 2008. Active development for MySQL 5.1 has ended.  MySQL 5.0 achieved General Availability (GA) status with MySQL 5.0.15, which was released for production use on 19 October 2005. Active development for MySQL 5.0 has ended. |
| **A.1.2.** | Why did MySQL version numbering skip versions 6 and 7 and go straight to 8.0? |
|  | Due to the many new and important features we were introducing in this MySQL version, we decided to start a fresh new series. As the series numbers 6 and 7 had actually been used before by MySQL, we went to 8.0. |
| **A.1.3.** | Can MySQL do subqueries? |
|  | Yes. See [Section 15.2.15, “Subqueries”](subqueries.md). |
| **A.1.4.** | Can MySQL perform multiple-table inserts, updates, and deletes? |
|  | Yes. For the syntax required to perform multiple-table updates, see [Section 15.2.17, “UPDATE Statement”](update.md); for that required to perform multiple-table deletes, see [Section 15.2.2, “DELETE Statement”](delete.md).  A multiple-table insert can be accomplished using a trigger whose `FOR EACH ROW` clause contains multiple [`INSERT`](insert.md) statements within a `BEGIN ... END` block. See [Section 27.4, “Using Triggers”](triggers.md). |
| **A.1.5.** | Does MySQL have Sequences? |
|  | No. However, MySQL has an `AUTO_INCREMENT` system, which can also handle inserts in a multi-source replication setup. With the [`auto_increment_increment`](replication-options-source.md) and [`auto_increment_offset`](replication-options-source.md) system variables, you can set each server to generate auto-increment values that don't conflict with other servers. The [`auto_increment_increment`](replication-options-source.md) value should be greater than the number of servers, and each server should have a unique offset. |
| **A.1.6.** | Does MySQL have a [`NOW()`](date-and-time-functions.md) function with fractions of seconds? |
|  | Yes, see [Section 13.2.6, “Fractional Seconds in Time Values”](fractional-seconds.md). |
| **A.1.7.** | Does MySQL work with multi-core processors? |
|  | Yes. MySQL is fully multithreaded, and makes use of all CPUs made available to it. Not all CPUs may be available; modern operating systems should be able to utilize all underlying CPUs, but also make it possible to restrict a process to a specific CPU or sets of CPUs.  On Windows, there is currently a limit to the number of (logical) processors that [**mysqld**](mysqld.md) can use: a single processor group, which is limited to a maximum of 64 logical processors.  Use of multiple cores may be seen in these ways:  - A single core is usually used to service the commands issued from one session. - A few background threads make limited use of extra cores; for example, to keep background I/O tasks moving. - If the database is I/O-bound (indicated by CPU consumption less than capacity), adding more CPUs is futile. If the database is partitioned into an I/O-bound part and a CPU-bond part, adding CPUs may still be useful. |
| **A.1.8.** | Why do I see multiple processes for [**mysqld**](mysqld.md)? |
|  | [**mysqld**](mysqld.md) is a single-process program, not a multi-process program, and does not fork or launch other processes. However, [**mysqld**](mysqld.md) is multithreaded and some process-reporting system utilities display separate entries for each thread of multithreaded processes, which may lead to the appearance of multiple [**mysqld**](mysqld.md) processes when in fact there is only one. |
| **A.1.9.** | Can MySQL perform ACID transactions? |
|  | Yes. All current MySQL versions support transactions. The `InnoDB` storage engine offers full ACID transactions with row-level locking, multi-versioning, nonlocking repeatable reads, and all four SQL standard isolation levels.  The [`NDB`](mysql-cluster.md) storage engine supports the [`READ COMMITTED`](innodb-transaction-isolation-levels.md) transaction isolation level only. |
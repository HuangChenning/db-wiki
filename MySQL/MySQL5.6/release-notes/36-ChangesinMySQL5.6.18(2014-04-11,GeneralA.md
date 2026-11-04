---
title: "Changes in MySQL 5.6.18 (2014-04-11, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=85"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

A known limitation of this release:Note If you have `InnoDB` tables with full-text search indexes and you are upgrading from MySQL 5.6.10 to a MySQL version up to and including MySQL 5.6.18, the server will fail to start after the upgrade (Bug#72079). This bug is fixed in MySQL 5.6.19.

As a workaround, remove full-text search indexes prior to upgrading and rebuild full-text search indexes after the upgrade is completed.

- Security Notes
- Bugs Fixed

> Security Notes

- The MySQL 5.6 Commercial Server has been updated to use OpenSSL version 1.0.1g, which has been

publicly reported as not vulnerable to CVE-2014-0160. Please see Oracle Note #1645479.1 for further details.

The MySQL 5.6 Community Server is built using the yaSSL cryptographic software library instead of OpenSSL. Oracle-produced MySQL 5.6 Community Server binaries use `YaSSL` libraries which have been reported as not affected by CVE-2014-0160. Users of MySQL Server binaries produced by parties other than Oracle should seek a vulnerability assessment from their respective binary providers.

Since the only change in MySQL Server 5.6.18 is the inclusion of OpenSSL libraries publicly reported as unaffected by CVE-2014-0160, and since Oracle-produced MySQL Community builds do not include OpenSSL libraries known to be affected by CVE-2014-0160, Oracle is not producing builds for MySQL Community Server for version 5.6.18. This means that MySQL Community Server is skipping version

5.6.18. (Bug #18533200)

## MySQL 5.6 Release Notes

> Bugs Fixed

- Executing a correlated subquery on an `ARCHIVE` table which has an `AUTO_INCREMENT` column caused

the server to hang. (Bug #18065452)

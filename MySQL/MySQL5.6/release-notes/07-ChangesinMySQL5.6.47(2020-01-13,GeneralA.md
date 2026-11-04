---
title: "Changes in MySQL 5.6.47 (2020-01-13, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=7"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

> Bugs Fixed

- Replication: Under certain conditions, replication of conditional comments could fail. (Bug #28388217)
- Replication: When GTIDs are enabled on a replication master and slave, and the slave connects to

the master with the `MASTER_AUTO_POSITION=1` option set, the master must send the slave all the transactions that the slave has not already received, committed, or both. If any of the transactions that should be sent by the master have been already purged from the master's binary log, the master sends the error `ER_MASTER_HAS_PURGED_REQUIRED_GTIDS` (1789) to the slave, and replication does not start.

The message provided for the error `ER_MASTER_HAS_PURGED_REQUIRED_GTIDS` has been changed to provide advice on the correct action in this situation, which is for the slave to replicate the missing transactions from another source, or for the slave to be replaced by a new slave created from a more recent backup. The message advises that the master's binary log expiration period can be revised to avoid the situation in future. In addition, the master now identifies the GTIDs of the purged transactions and supplies them in its error log in the warning message `ER_FOUND_MISSING_GTIDS` (11809), so that you do not need to calculate the missing GTIDs manually. (Bug #26004541, Bug #29769293)

- With multiple sessions executing concurrent `INSERT ... ON DUPLICATE KEY UPDATE` statements

into a table with an `AUTO_INCREMENT` column but not specifying the `AUTO_INCREMENT` value, inserts could fail with a unique index violation. (Bug #30194841, Bug #96578)

- A `SELECT` using a `WHERE` condition of the form `A AND (B OR C [OR ...])` resulting in an impossible

range led to an unplanned exit of the server. (Bug #29770705)

- An incomplete connection packet could cause clients not to properly initialize the authentication plugin

name. (Bug #29630767)

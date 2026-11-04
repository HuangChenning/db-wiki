---
title: "Changes in MySQL 5.6.38 (2017-10-16, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=19"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Bugs Fixed

> Packaging Notes

- `mysqlcheck` was missing in the MySQL Server Docker image, which prevented `mysql_upgrade` from

running. (Bug #26400146, Bug #86968)

> Bugs Fixed

- InnoDB: Replication lag occurred on slave instances during large update operations on tables with many

partitions. (Bug #25687813, Bug #85352)

- InnoDB: A failure occurred during an end range comparison. (Bug #25669686)
- InnoDB: Enabling the `innodb_buffer_pool_load_now` setting failed in read-only mode. The event

that signals the buffer pool load thread was not initialized. (Bug #25586766)

- InnoDB: A long wait for a dictionary operation lock held by a full-text search synchronization operation

caused a server exit. (Bug #24938374, Bug #26376681, Bug #26376239)

- Partitioning: Queries involving `NULL` were not always handled correctly on tables that were partitioned

by `LIST`. (Bug #76418, Bug #20748521)References: See also: Bug #86255, Bug #26034430.

- Replication: When replicating a partitioned table with an index, on a replication slave where

`HASH_SCAN` was specified as part of the `slave_rows_search_algorithms` setting, the slave I/O thread sometimes stopped with an error `HA_ERR_KEY_NOT_FOUND`. (Bug #26137159)

- Replication: Replication clients no longer enable `LOCAL` capability for `LOAD DATA` statements, because

they do not use `LOAD DATA LOCAL` statements. (Bug #24763131)

- Replication: In case of a failure while creating multiple slave applier worker threads, some threads

would be left orphaned and their resources would not be collected. Thanks to Laurynas Biveinis for his contribution to fixing this bug. (Bug #24679056, Bug #82980)

- MSI packages for Windows failed to detect when Microsoft Visual C++ 2010 Redistributable Package

was installed. (Bug #26501092, Bug #87139)

- yaSSL could incorrectly perform TLS cipher negotiation. (Bug #26482173)
- The server failed to check the maximum path length for partition names. (Bug #26390632)
- Identifiers containing a mixt of backslashes and backticks could be parsed incorrectly. (Bug #26372491)
- Source packages for Debian platforms contained prebuilt debug binaries, causing build failures on any

architectures other than the one on which those binaries were built. (Bug #26186911)

- The `test` database was missing from MSI packages. (Bug #26168832)

## MySQL 5.6 Release Notes

- Uninstalling the `daemon_memcached` plugin caused a serious error. (Bug #25909540)
- Selecting from a view could yield different results with materialization enabled versus materialization

disabled. (Bug #25782811, Bug #85622)

- The Performance Schema failed to check the maximum host length for client connections. (Bug

#25510805)

- A server error occurred when a full text search result exceeded the

`innodb_ft_result_cache_limit` setting. The patch for this bug also backports a related patch (Bug#21140111). (Bug #25033538)

- If a stored function was considered a constant by the optimizer, calling it from a subquery in a `NOT IN`

condition in the `WHERE` clause could cause a server exit. (Bug #23577867)

- A `mysqldump` memory leak was fixed. Thanks to Yura Sorokin for the patch. (Bug #23531150, Bug

#81714)

- If a session rolled back to a savepoint and then was killed, the statements up to the point of the

savepoint could be committed. (Bug #22350047, Bug #79596)

- For clients that used Connector/Python and authenticated using the `sha256_password` plugin, the

server could handle connections incorrectly. (Bug #21421642)

- `NAME_CONST()` can return null if incorrect arguments are given. In some cases, this was not handled

and could cause a server exit. (Bug #19143243, Bug #26361149)

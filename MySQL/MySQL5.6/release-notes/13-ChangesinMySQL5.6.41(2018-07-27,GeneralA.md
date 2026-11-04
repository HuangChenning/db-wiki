---
title: "Changes in MySQL 5.6.41 (2018-07-27, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=13"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Security Notes
- Functionality Added or Changed
- Bugs Fixed

## MySQL 5.6 Release Notes

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version

1.0.2o. Issues fixed in the new OpenSSL version are described at http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #28025379)

> Functionality Added or Changed

- Previously, for the `--ssl-verify-server-cert` option, the client checked whether the host name

that it used for connecting matched the Common Name value in the certificate but not the Subject Alternative Name value. Now, if MySQL was built using OpenSSL 1.0.2 or higher, the client checks whether the host name matches either the Subject Alternative Name value or the Common Name value in the server certificate. Host name identity verification also works with certificates that specify the Common Name using wildcards. Thanks to Daniël van Eeden for a patch on which this change was based. (Bug #16211011, Bug #68052, Bug #27511233, Bug #89578)

> Bugs Fixed

- InnoDB: A schema mismatch error reported during an import tablespace operation failed to print

mismatched table flags in a readable format. (Bug #27542720)

- InnoDB: A DDL operation failed to wait for a `FULLTEXT` index optimization operation to finish. (Bug

#27326796)References: This issue is a regression of: Bug #24938374.

- InnoDB: A failing assertion occurred after initiating a `memcached` get operation. (Bug #26876594)
- InnoDB: A corrupt index ID encountered during a foreign key check raised an assertion. (Bug

#26654685)

- Replication: When a transaction larger than the binary log transaction cache size

(`binlog_cache_size`) was flushed to a temporary file during processing, and the flush failed due to a lack of space in the temporary directory, the flush error was not handled correctly. No message was written to the error log, and the binary log cache was not cleared after the transaction was rolled back.

Now, in this situation, the server takes an appropriate action based on the `binlog_error_action`setting (shut down the server or halt logging), and writes a message to the error log. When the transaction is rolled back, the server checks for flush errors and clears the binary log cache if any occurred. (Bug #27399620, Bug #89272)

- Replication: When GTIDs are in use for replication, replicated transactions that are filtered out on the

slave are persisted. If binary logging is enabled on the slave, the filtered-out transaction is written to the binary log as a `Gtid_log_event` followed by an empty transaction containing only `BEGIN` and`COMMIT` statements. If binary logging is disabled, the GTID of the filtered-out transaction is written to the `mysql.gtid_executed` table. This process ensures that there are no gaps in the set of executed GTIDs, and that the filtered-out transactions are not retrieved again if the slave reconnects to the master. Previously, this process was not done for `CREATE DATABASE`, `ALTER DATABASE`, and`DROP DATABASE` statements, but it is now carried out for those statements as well as for others. (Bug#27308751, Bug #88891)

- Replication: On a multithreaded slave, when a `STOP SLAVE` statement is executed on the slave,

followed by a `START SLAVE` statement, the error log can report a different position in the binary log for

## MySQL 5.6 Release Notes

the slave SQL thread when exiting, compared to the position reported for the slave SQL thread at the subsequent initialization.

For a multithreaded slave, the position reported for the SQL thread on exit is a low water mark, up to which the replication stream is consistent and has no gaps. Transactions appearing before the position are guaranteed to have committed, but transactions after the position may have committed or not.

However, this low water mark was being reported before the process to stop the worker threads was actually carried out, and the low water mark was subsequently updated by a checkpoint routine during that process. The timing of the log message has now been changed so that the final low water mark is reported as the position for the SQL thread on exit. (Bug #27300658)

- A heap overflow vulnerability in the MySQL client library was fixed. (Bug #27980823)
- An unencrypted connection could result from a client connection attempt specifying that an encrypted

connection was required, if the server was not configured to support SSL. (Bug #27759871)

- On Windows, if the Visual C++ Redistributable for Visual Studio had been removed, MySQL

uninstallation using the MSI installer failed. (Bug #27621546)

- A memory leak in the `pfs-t` unit test was fixed. Thanks to Yura Sorokin for the patch. (Bug #27440735,

Bug #89384)

- With `automatic_sp_privileges` enabled, the `EXECUTE` and `ALTER ROUTINE` privileges were not

correctly granted to routine creators. (Bug #27407480)

- Mishandling of internal privilege structures could cause a server exit. (Bug #27230925)
- The `UNION` of a user-defined variable and a `DECIMAL` column produced an incorrect result when using a

UTF8 character set. (Bug #27197235)

- `mysqldump` exited abnormally for large `--where` option values. (Bug #26171967, Bug #86496, Bug

#27510150)

- For `MyISAM` tables, particular sequences of `INSERT` and `DELETE` statements could cause table

corruption. (Bug #25541037)

- `FORCE INDEX` had no effect on a query that used `GROUP BY`, `ORDER BY`, and `LIMIT` together. (Bug

#90817, Bug #27998526)

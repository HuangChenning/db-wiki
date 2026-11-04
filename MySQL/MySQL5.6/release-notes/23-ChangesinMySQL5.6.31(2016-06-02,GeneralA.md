---
title: "Changes in MySQL 5.6.31 (2016-06-02, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=35"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Packaging Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> Packaging Notes

- `support-files/MacOSX/ReadMe.txt` is no longer included in MySQL distributions. (Bug #81038,

Bug #23088916)

- The `INSTALL-SOURCE` file had partly outdated information and has been removed from source

packages. (Binary packages are unaffected). (Bug #80680, Bug #23081064)

> Security Notes

- The linked OpenSSL library for the MySQL Commercial Server has been updated to version 1.0.1t. For a

description of issues fixed in this version, see http://www.openssl.org/news/vulnerabilities.html.

This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead. (Bug #23229564)

> Functionality Added or Changed

- A new `CMake` option, `WITH_SYMVER16`, if enabled, causes the `libmysqlclient` client library

to contain extra symbols to be compatible with `libmysqlclient` on RHEL/OEL 5, 6, 7, and Fedora releases. All symbols present in `libmysqlclient.so.16` are tagged with symver 16 in`libmsqlclient.so.18`, making those symbols have both symver 16 and 18. (Bug #22980983)

- The version of the `tcmalloc` library included in MySQL distributions was very old. It has been removed

and is no longer included with MySQL. (Bug #80994, Bug #23068660)

> Bugs Fixed

- InnoDB: MySQL failed to build on Fedora 24 using GCC 6. (Bug #23227804)

## MySQL 5.6 Release Notes

- InnoDB: Potential buffer overflow issues were corrected for the `InnoDB` `memcached` plugin. (Bug

#23187607)

- InnoDB: The full-text index cache was freed during a background index cache synchronization. (Bug

#22996488)

- InnoDB: A full-text index operation raised an assertion. (Bug #22963169)
- InnoDB: An `INSERT` operation on a table with a `FULLTEXT` index and `FTS_DOC_ID` column

failed because the inserted `FTS_DOC_ID` value exceeded the permitted gap between consecutive`FTS_DOC_ID` values. To avoid this problem, the permitted gap between the largest used `FTS_DOC_ID`value and new `FTS_DOC_ID` value was raised from 10000 to 65535. (Bug #22679185)

- InnoDB: With `innodb_autoinc_lock_mode=0`, multiple threads waiting for a table-level lock caused

an unexpected deadlock. (Bug #21983865, Bug #78761)

- InnoDB: A `FLUSH TABLES ... FOR EXPORT` operation appeared to stall. A loop in the

`ibuf_contract_in_background` function failed to exit. (Bug #21133329, Bug #77011)

- InnoDB: A full-text query raised an assertion. Under certain circumstances, DDL operations such as

`ALTER TABLE ... RENAME` caused full-text auxiliary tables to be removed on server restart. (Bug#13651665)

- Replication: In the `next_event()` function, which is called by a slave's SQL thread to read the next

even from the relay log, the SQL thread did not release the `relaylog.log_lock` it acquired when it ran into an error (for example, due to a closed relay log), causing all other threads waiting to acquire a lock on the relay log to hang. With this fix, the lock is released before the SQL thread leaves the function under the situation. (Bug #21697821)References: See also: Bug #20492319.

- Replication: When using row-based replication in a cascading or circular replication setup, where

a master is replicating to server 1 which is then replicating to server 2, merge tables were not being correctly applied on server 2. This could cause an unexpected halt on server 2 while server 1 was unaffected. (Bug #17018343)

- Replication: If a multithreaded replication slave running with `relay_log_recovery=1` stopped

unexpectedly, during restart the relay log recovery process could fail. This was due to transaction inconsistencies not being filled, see Handling an Unexpected Halt of a Replica Server. Prior to this fix,to recover from this situation required manually setting `relay_log_recovery=0`, starting the slave with `START SLAVE UNTIL SQL_AFTER_MTS_GAPS` to fix any transaction inconsistencies and then restarting the slave with `relay_log_recovery=1`. This process has now been automated, enabling relay log recovery of a multithreaded slave upon restart automatically. (Bug #77496, Bug #21507981)

- Microsoft Windows: On Windows, MySQL installation could result in MySQL being placed under `C:`

`\Program Files\Canon\Easy-WebPrint EX`. (Bug #14583183)References: See also: Bug #70918, Bug #68821, Bug #68227.

- Microsoft Windows: On Windows, MySQL installation failed if the `HKEY_LOCAL_MACHINE\SOFTWARE`

`\Microsoft\Windows\CurrentVersion\Uninstall\` registry key was present with a key/value pair of `"InstallLocation"` and `"\Hewlett-Packard\\"`. (Bug #74631, Bug #19949163)

- `INSERT` with `ON DUPLICATE KEY UPDATE` and `REPLACE` on a table with a foreign key constraint

defined failed with an incorrect `duplicate entry` error rather than a foreign key constraint violation error. (Bug #23135731)References: This issue is a regression of: Bug #78853, Bug #22037930.

## MySQL 5.6 Release Notes

- For debug builds, `CONCAT_WS()` could raise an assertion if there was nothing to append. (Bug

#22888420)

- Invoking Enterprise Encryption functions in multiple threads simultaneously could cause a server exit.

(Bug #22839278)

- Attempting to use Enterprise Encryption functions after creating and dropping them could cause a server

exit. (Bug #22669012)

- Setting `sort_buffer_size` to a very large value could cause some operations to fail with an out-of-

memory error. (Bug #22594514)

- An assertion could be raised when a deadlock occurred due to a `SELECT ... GROUP BY ... FOR`

`UPDATE` query executed using a Loose Index Scan. (Bug #22187476)

- Several potential buffer overflow issues were corrected. (Bug #21977380, Bug #23187436, Bug

#23202778, Bug #23195370, Bug #23202699)

- If the CA certificate as given to the `--ssl-ca` option had an invalid path, yaSSL returned

an error message different from OpenSSL. Now both return `SSL connection error:``SSL_CTX_set_default_verify_paths failed`. (Bug #21920657)

- Some string functions returned one or a combination of their parameters as their result. If one of the

parameters had a non-ASCII character set, the result string had the same character set, resulting in incorrect behavior when an ASCII string was expected. (Bug #18740222)

- On Fedora 24, upgrades using a Community MySQL Server RPM failed to replace an installed MariaDB

Galera server due to a change in the MariaDB package. (Bug #81390, Bug #23273818)

- MySQL did not compile under Solaris 12 using Sun Studio. To correct this, instances of

`__attribute__` were changed to `MY_ATTRIBUTE`. (Bug #80748, Bug #22932576)

- For a server compiled with `-DWITH_PERFSCHEMA_STORAGE_ENGINE=0`, a memory leak could occur for

buffered log messages used during server startup. (Bug #80089, Bug #22578574)

- For debug builds, merging a derived table into an outer query block could raise an assertion. (Bug

#79502, Bug #22305361, Bug #21139722)

- A null pointer dereference of a parser structure could occur during stored procedure name validation.

(Bug #79396, Bug #22286421)

- Using `CREATE USER` to create an account with the `mysql_native_password` or

`mysql_old_password` authentication plugin and using a clause of the form `IDENTIFIED WITH``plugin AS 'hash_string'` caused the account to be created without a password. (Bug #78033, Bug#21616496)

- Failure of `UNINSTALL PLUGIN` could lead to inaccurate or confusing errors for subsequent `INSTALL`

`PLUGIN` operations. (Bug #74977, Bug #20085672)

- `mysqld_multi` displayed misleading error messages when it was unable to execute

`my_print_defaults`. (Bug #74636, Bug #19920049)

- `mysqldump` failed silently with no error message when it encountered an error while executing `FLUSH`

`LOGS`. (Bug #71783, Bug #18284273)

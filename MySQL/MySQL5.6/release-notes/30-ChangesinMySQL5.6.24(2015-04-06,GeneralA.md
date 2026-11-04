---
title: "Changes in MySQL 5.6.24 (2015-04-06, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=58"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Deprecation and Removal Notes
- MySQL Enterprise Notes
- Functionality Added or Changed

## MySQL 5.6 Release Notes

- Bugs Fixed

> Deprecation and Removal Notes

- `ALTER TABLE` did not take advantage of fast alterations that might otherwise apply to the operation to

be performed, if the table contained temporal columns found to be in pre-5.6.4 format (`TIME`, `DATETIME`,and `TIMESTAMP` columns without support for fractional seconds precision). Instead, it upgraded the table by rebuilding it. Two new system variables enable control over upgrading such columns and provide information about them:

- `avoid_temporal_upgrade` controls whether `ALTER TABLE` implicitly upgrades temporal columns

found to be in pre-5.6.4 format. This variable is disabled by default. Enabling it causes `ALTER TABLE`not to rebuild temporal columns and thereby be able to take advantage of possible fast alterations.

- `show_old_temporals` controls whether `SHOW CREATE TABLE` output includes comments to

flag temporal columns found to be in pre-5.6.4 format. Output for the `COLUMN_TYPE` column of the`INFORMATION_SCHEMA.COLUMNS` table is affected similarly. This variable is disabled by default.

Both variables are deprecated and will be removed in a future MySQL version. (Bug #72997, Bug#18985760)

> MySQL Enterprise Notes

- MySQL Enterprise Edition now includes MySQL Enterprise Firewall, an application-level firewall that

enables database administrators to permit or deny SQL statement execution based on matching against whitelists of accepted statement patterns. This helps harden MySQL Server against attacks such as SQL injection or attempts to exploit applications by using them outside of their legitimate query workload characteristics.

Each MySQL account registered with the firewall has its own statement whitelist, enabling protection to be tailored per account. For a given account, the firewall can operate in recording or protecting mode,for training in the accepted statement patterns or protection against unacceptable statements. For more information, see MySQL Enterprise Firewall. (WL #7725)

> Functionality Added or Changed

- `CMake` support was updated to handle `CMake` version 3.1. (Bug #20344207)
- The server now includes its version number when it writes the initial “starting” message to the error log,

to make it easier to tell which server instance error log output applies to. This value is the same as that available from the `version` system variable. (Bug #74917, Bug #20052694)

- Statement digesting as done previously by the Performance Schema is now done at the SQL level

regardless of whether the Performance Schema is compiled in and is available to other aspects of server operation that could benefit from it. The default space available for digesting is 1024 bytes, but can be changed at server startup using the `max_digest_length` system variable. (WL #8354)References: See also: Bug #18304086, Bug #20015246.

> Bugs Fixed

- InnoDB: A `TRUNCATE TABLE` operation on a temporary table raised an assertion. The temporary table

object was incompletely constructed when reloaded from `SYS_TABLES`. (Bug #20527363, Bug #72080)

- InnoDB: A full-text phrase search returned an incorrect result. An empty string was handled incorrectly

when tokenizing a newly inserted row. (Bug #20465273, Bug #75755)

## MySQL 5.6 Release Notes

- InnoDB: Optimizing a `FULLTEXT` index raised an assertion. The last optimized word of a `FULLTEXT`

index is stored in the `CONFIG` table `value` column which is defined as CHAR(50). An assertion was raised when the last optimized word was greater than 50 characters in length. The `CONFIG` table `value`column is defined as CHAR(200) as of MySQL 5.6.24 and MySQL 5.7.6.

If your `innodb_ft_max_token_size` setting is greater than 50, it is recommended that you recreate existing `InnoDB` `FULLTEXT` indexes after upgrading to MySQL 5.6.24 or MySQL 5.7.6 to avoid this issue. `FULLTEXT` indexes created after upgrading to MySQL 5.6.24 or MySQL 5.7.6 are unaffected.

(Bug #20418326)

- InnoDB: An `InnoDB` `memcached` `extra_col_value[]` array was freed without checking the allocated

flag, causing a server exit. (Bug #20400373)

- InnoDB: A DML operation performed while a flushing operation was in progress raised a memcached-

related assertion. (Bug #20390277)

- InnoDB: The `memcached` `process_arithmetic_command` raised an assertion. The wrong error code

was returned for a nonexistent `decr` key. (Bug #20386835)

- InnoDB: The expiration time (`exptime`) defined using the `memcached` `set` command was ignored.

`InnoDB` `memcached` set the expiration time to an interval value instead of a system time value. (Bug#20381342, Bug #70055)

- InnoDB: An assertion was raised when the full-text search `fts_savepoint_release()` function

released a named transaction savepoint and all subsequent savepoints. Only the initial savepoint should be released. (Bug #20341916)

- InnoDB: A full-text search optimization operation raised an assertion. (Bug #20281800)
- InnoDB: Due to a regression introduced in MySQL 5.6.20, `mysqld stop` did not stop the `mysqld`

server process while the `InnoDB` `memcached` plugin was active. (Bug #20078646, Bug #74956)References: This issue is a regression of: Bug #18409840.

- InnoDB: An `ALTER TABLE ... RENAME` failure on a table with a `FULLTEXT` index raised an assertion.

(Bug #20043707)

- InnoDB: A severe error occurred during the log apply phase of an online `ALTER TABLE` operation

that was converting a table with a UTF-8 charset to `ROW_FORMAT=REDUNDANT`. (Bug #19843246, Bug#19895661, Bug #20219871)

- InnoDB: When dummy tables are created, the `autoinc_mutex` member of the of the `dict_table_t`

object was created unnecessarily. Similarly, the `zip_pad.mutex` object of `dict_index_t` object was created unnecessarily for dummy indexes. To avoid unnecessary mutex contention, `autoinc_mutex`and `zip_pad.mutex` objects are now allocated and initialized on the first lock attempt. (Bug#19788198, Bug #73361)

- InnoDB: An `ALTER TABLE ... RENAME` operation raised an invalid assertion. The assertion code

used an incorrect transaction object. (Bug #18523599)References: This issue is a regression of: Bug #17447500.

- InnoDB: A `memcached` `append` operation on an `INT` column caused a segmentation fault. `append`

operations on `INT` columns are not supported and are now blocked. (Bug #75200, Bug #20209756)

- Partitioning: A number of `ALTER TABLE` statements that attempted to add partitions, columns, or

indexes to a partitioned table while a write lock was in effect for this table were not handled correctly.

(Bug #74451, Bug #74478, Bug #74491, Bug #74560, Bug #74746, Bug #74841, Bug #74860, Bug

## MySQL 5.6 Release Notes

#74869, Bug #19856162, Bug #19864284, Bug #19873019, Bug #19891663, Bug #19990815, Bug#20026661, Bug #20031966, Bug #20033503, Bug #19827845)

- Replication: When replicating from a MySQL 5.7.6 or later server to a MySQL 5.6.23 or earlier server,

if the older version applier thread encountered an `Anonymous_gtid_log_event` it caused an assert. The fix ensures that these new log events added in MySQL 5.7.6 and later do not cause this problem with MySQL 5.6.24 and later slaves. If `gtid_mode` is `OFF` and the applier thread encounters a`Gtid_log_event`, the applier thread aborts with an error. If `gtid_mode` is `ON` and the applier thread encounters a `Anonymous_gtid_log_event`, the applier thread aborts with an error. (Bug #20436436)

- Replication: When the `automatic_sp_privileges` variable is set, the server automatically

grants the `EXECUTE` and `ALTER ROUTINE` privileges to the creator of a stored routine, if the user does not already have these privileges. When a privileged user creates a procedure with `DEFINER`as a non privileged user on a master, the current user is considered to be a privileged user and the`mysql.procs_priv` table is not updated. When such a statement was replicated to slave, the non-privileged `DEFINER` was considered as the current user on the slave and privileges were being allocated. This caused a difference in the privileges that were being allocated on the master and the slave. The fix ensures that creater of the stored routine is added to the binary log, and the slave now checks first if the user exists before granting privileges. To maintain compatibility with previous versions,the `DEFINER` is used when the `INVOKER` is not available. As part of this fix, anonymous users can be used to replicate from master to slave. (Bug #20049894)

- Replication: When using a slave configured to use a special character set such as UTF-16, UTF-32,

or UCS-2, the receiver (I/O) thread failed to connect. The fix ensures that in such a situation, if a slave's character set is not supported then default to using the `latin1` character set. (Bug #19855907)

- Replication: An internal problem with binary log group commit caused an incompatibility with the

`threadpool` plugin. (Bug #18845301)

- Replication: When `gtid_mode=ON` and `slave_net_timeout` was set to a low value, the slave I/O

thread could appear to hang. This was due to the slave heartbeat not being sent regularly enough when the dump thread found many events that could be skipped. The fix ensures that the heartbeat is sent correctly in such a situation. (Bug #74607, Bug #19975697)

- `CMake` failed to detect the OpenSSL version properly for recent versions of OpenSSL (the format of the

version string changed). (Bug #20756770)

- For execution of prepared statements, no check was made whether an audit log plugin returned an error,

so statement success could erroneously be returned. (Bug #20567900)

- Debian packages were missing some dependencies. (Bug #20561621)
- Following execution of a `GRANT ... WITH GRANT OPTION` statement, execution of a prepared

statement with a view could cause a server exit. (Bug #20030284)

- A user with a name of `event_scheduler` could view the Event Scheduler process list without the

`PROCESS` privilege. (Bug #20007583, Bug #20754369)

- Trying to create a user after dropping columns from the `mysql.user` table could result in a server exit.

(Bug #19910140)

- Ordering by a `GROUP_CONCAT()` result could cause a server exit. (Bug #19880368, Bug #20730220)
- A malformed `mysql.proc` table row could result in a server exit for `DROP DATABASE` of the database

associated with the `proc` row. (Bug #19875331)

- `SHOW GRANTS` after connecting using a proxy user could display the password hash of the proxied user.

(Bug #19817663)

## MySQL 5.6 Release Notes

- Large values of the `transaction_prealloc_size` system variable could cause the server to allocate

excessive amounts of memory. The maximum value has been adjusted down to 128K. A similar change was made for `transaction_alloc_block_size`. Transactions can still allocate more than 128K if necessary; this change reduces the amount that can be preallocated, as well as the maximum size of the incremental allocation blocks. (Bug #19770858, Bug #20730053)

- Certain queries on the `INFORMATION_SCHEMA.INNODB_FT_CONFIG` table could cause a server exit.

(Bug #19703520)

- A server exit could occur for queries that compared two rows using the `<=>` operator and the rows

belonged to different character sets. (Bug #19699237, Bug #20730155)

- Certain `InnoDB` errors caused stored function and trigger condition handlers to be ignored. (Bug

#19683834, Bug #20094067)

- The optimizer could raise an assertion due to incorrectly associating an incorrect field with a temporary

table. (Bug #19612819, Bug #20730129)

- Audit log filtering was not applied to connection events. (Bug #19509398)
- With `audit_log_connection_policy=ERRORS`, successful `COM_QUIT` events were errroneously

written to the audit log. With `audit_log_statement_policy=NONE`, no connection events were written to the audit log, regardless of the current `audit_log_connection_policy` setting. (Bug#19509373, Bug #21027210)

- The value of the `Audit_log_events` status variable did not equal the sum of the other audit log

counters. (Bug #19509336)

- The `Audit_log_events_filtered` status variable did not increment when audit log events were

filtered. (Bug #19509263)

- Many new features were added to the audit log plugin in MySQL 5.6.20, but the version number was not

increased. The version has been bumped to 1.1. (Bug #19502900)

- The server could exit due to an optimizer failure to allocate enough memory for resolving outer

references. (Bug #18782905, Bug #19892803)

- If the audit log file was found to be corrupt at server startup, an appropriate error message was not

always written. Also, if the plugin is loaded, it will be initialized regardless of whether the log was corrupt,except in the case that renaming the log file fails. (Bug #14584292)

- Creating a `FEDERATED` table with an `AUTO_INCREMENT` column using a `LIKE` clause results in a server

exit. (Bug #12671631)

- Corrections were made for a number of code issues that resulted in compiler warnings about array

bounds, possibly uninitialized variables, and variables being set but not used. (Bug #75735, Bug#20458574)

- `NULL` as an expression was not recognized as a literal for calculation of Performance Schema statement

digests. (Bug #74813, Bug #20015246)

- The `group_concat_max_len` system variable could be set to its maximum value at runtime, but not in

an option file. (Bug #74037, Bug #19670915)

- A server warning error message referred to the obsolete `table_cache` system variable rather than

to `table_open_cache`. Thanks to Daniël van Eeden for the patch to fix some of the instances. (Bug#73373, Bug #19285052, Bug #75081, Bug #20135780)

## MySQL 5.6 Release Notes

- In the `DIGEST_TEXT` column of Performance Schema statement events tables, references to system

variables of the form `@@var_name` were stored as `@ @ var_name`. (Bug #71634, Bug #18304086)

- If the `WITH_SSL` `CMake` option was specified with an incorrect path to the SSL installation or the path to

an unsupported (too old) SSL installation, the option was implicitly changed to the `bundled` value and yaSSL was used instead. Now `CMake` exits with an error so the user knows that the option value must be changed. (Bug #69744, Bug #17162055)

- `mysql_real_connect()` could close a file descriptor twice if the server was not running. (Bug #69423,

Bug #19226740)

- Notification of events for the general log were received by the audit log plugin only if the general query

log was enabled. Now notifications are posted regardless of whether the general query log is enabled.

(Bug #60782, Bug #12368204, Bug #20536590, Bug #75796, Bug #20479643)

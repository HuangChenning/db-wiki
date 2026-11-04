---
title: "Changes in MySQL 5.6.25 (2015-05-29, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=54"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- MySQL Enterprise Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> MySQL Enterprise Notes

- Previously, enabling the `mysql_firewall_trace` system variable caused MySQL Enterprise Firewall

to write a file named `firewall_trace.txt` in the data directory. That is no longer done. Now with`mysql_firewall_trace` enabled, for `PROTECTING` mode, the firewall writes rejected statements to the error log.

> Security Notes

- `my_print_defaults` now masks passwords. To display passwords in cleartext, use the new `--show`

option. (Bug #19953365, Bug #20903330)

> Functionality Added or Changed

- MySQL Enterprise Firewall operates on parser states and does not work well together with the query

cache, which circumvents the parser. MySQL Enterprise Firewall now checks whether the query cache is enabled. If so, it displays a message that the query cache must be disabled and does not load. (Bug#20913616)

## MySQL 5.6 Release Notes

- MySQL distributions now include an `innodb_stress` suite of test cases. Thanks to Mark Callaghan for

the contribution. (Bug #76347, Bug #20717127)

> Bugs Fixed

- InnoDB; Partitioning: The `CREATE_TIME` column of the `INFORMATION_SCHEMA.TABLES` table now

shows the correct table creation time for partitioned `InnoDB` tables. The `CREATE_TIME` column of the`INFORMATION_SCHEMA.PARTITIONS` table now shows the correct partition creation time for a partition of partitioned `InnoDB` tables.

The `UPDATE_TIME` column of the `INFORMATION_SCHEMA.TABLES` table now shows when a partitioned`InnoDB` table was last updated by an `INSERT`, `DELETE`, or `UPDATE`. The `UPDATE_TIME` column of the`INFORMATION_SCHEMA.PARTITIONS` table now shows when a partition of a partitioned `InnoDB` table was last updated. (Bug #69990, Bug #17299181)

- InnoDB: An assertion was raised on shutdown due to XA PREPARE transactions holding explicit locks.

(Bug #20816223, Bug #76567)

- InnoDB: The `innodb_checksum_algorithm` `strict_*` settings (`strict_none`, `strict_innodb`,

and `strict_crc32`) caused the server to halt when `InnoDB` encountered a valid but non-matching checksum. For example, with `innodb_checksum_algorithm=strict_crc32`, a valid `innodb`checksum would cause the server to halt. Now, instead of halting the server, `InnoDB` only prints an error message. (Bug #20568464)

- InnoDB: The `memcached` `set` command permitted a negative expire time value. Expire time is stored

internally as an unsigned integer. A negative value would be converted to a large number and accepted.

The maximum expire time value is now restricted to `INT_MAX32` to prevent negative expire time values.

(Bug #20478242, Bug #75790)

- InnoDB: Removal of a foreign key object from the data dictionary cache during error handling caused

the server to exit. (Bug #20442523)

- InnoDB: `SHOW ENGINE INNODB STATUS` output showed negative reservation and signal count values

due to a counter overflow error. (Bug #20417397)

- InnoDB: Failure to check the status of a cursor transaction read-only option before reusing the

cursor transaction for a write operation resulted in a server exit during a `memcached` workload. (Bug#20391552)

- InnoDB: MDL locks taken by `memcached` clients caused a MySQL Enterprise Backup `FLUSH TABLES`

`WITH READ LOCK` operation to hang. (Bug #20275612)

- InnoDB: Estimates that were too low for the size of merge chunks in the result sorting algorithm caused

a server exit. (Bug #20049521)

- InnoDB: For full-text searches, the optimizer could choose an index that does not produce correct

relevancy rankings. (Bug #74686, Bug #19950568)

- Partitioning: When creating a partitioned table, partition-level `DATA DIRECTORY` or `INDEX`

`DIRECTORY` option values that contained an excessive number of characters were handled incorrectly.

(Bug #20809045)

- Partitioning: Executing an `ALTER TABLE` on a partitioned table on which a write lock was in effect

could cause subsequent SQL statements on this table to fail. (Bug #74288, Bug #74634, Bug#19784790, Bug #19918805)References: See also: Bug #19856162, Bug #74451.

## MySQL 5.6 Release Notes

- Replication: Row unpacking did not function correctly in some cases when running the server with

`binlog_row_image` set to `minimal`. (Bug #20468712)

- Replication: When binary logging was enabled, using stored functions and triggers resulting in a long

running procedure that inserted many records caused the memory use to increase rapidly. This was due to memory being allocated per variable. The fix ensures that in such a situation, memory is allocated once and the same memory is reused. (Bug #75879, Bug #20531812)

- Replication: If an error was encountered while adding a GTID to the received GTID set, the log lock was

not being correctly released. This could cause a deadlock. (Bug #75781, Bug #20492319)

- Replication: A slave running MySQL 5.6.24 or earlier could not connect to a master running

MySQL 5.7.6 and later that had `gtid_mode=OFF_PERMISSIVE` or `gtid_mode=ON_PERMISSIVE`.

The fix ensures that a slave running MySQL 5.6.25 and later can connect to such a master as long as the slave's `gtid_mode` is compatible. In other words, a slave running MySQL 5.6.25 and later which has `gtid_mode=OFF` can connect to a master running MySQL 5.7.6 and later which has `gtid_mode=OFF_PERMISSIVE`, and a slave running MySQL 5.6.25 and later which has `gtid_mode=ON` can connect to a master running MySQL 5.7.6 and later which has`gtid_mode=ON_PERMISSIVE`. Other combinations are incompatible. (Bug #75769, Bug #20471216)

- Replication: If an error occurred when using a multithreaded slave, issuing a `CHANGE MASTER`

`TO` statement which resulted in an `ER_MTS_CHANGE_MASTER_CANT_RUN_WITH_GAPS`error, and then issuing `RESET SLAVE`, made it impossible to change master due to repeated`ER_MTS_CHANGE_MASTER_CANT_RUN_WITH_GAPS` errors. Running the debug version of `mysqld`caused an unexpected exit in this case. The fix ensures that the recovery process for multithreaded slaves avoids this. (Bug #75574, Bug #20411374)

- Replication: When using semisynchronous replication performance was degrading when the number

of threads increased beyond a certain threshold. To improve performance, now only the thread which is committing is responsible for deleting the active transaction node. All other operations do not touch this active transaction list. (Bug #75570, Bug #20574628)

- Replication: Using `mysqlbinlog` to process log events greater than 1.6GB failed with an out of

memory error. This was caused by an internal error converting the length variable. The fix upgrades the length variable to avoid overflow in both encoding and decoding functions. (Bug #74734, Bug#20350989)

- Replication: When `master_info_repository=TABLE` the receiver thread stores received event

information in a table. The memory used in the process of updating the table was not being freed correctly and this could lead to an out of memory error. The fix ensures that after an event is flushed to the relay log file by a receiver thread, the memory used is freed. (Bug #72885, Bug #19390463, Bug#69848, Bug #20124342)

- Replication: Using `mysqlbinlog` to replay a relay log which ended with `GTID_LOG_EVENT` could

cause the following error:

```
ERROR 1790 (HY000) @@SESSION.GTID_NEXT cannot be changed by a client that
owns a GTID. The client owns UUID:GTID. Ownership is released on COMMIT or
ROLLBACK.
```

If a relay log rotate happens (either through a receiver thread restart or after issuing the `ROTATE`command) exactly after writing a `GTID_LOG_EVENT`, when replaying such a relay log's end`ROTATE_EVENT`, it was mistakenly identified as being inside a transaction, whereas the transaction was actually started after `GTID_LOG_EVENT`. This caused `mysqlbinlog` to append `SET``@@SESSION.GTID_NEXT='AUTOMATIC'`, resulting in two `GTID_NEXT` statements one after the other.

The fix ensures that `mysqlbinlog` generates `SET @@SESSION.GTID_NEXT='AUTOMATIC'` only outside of a transaction and when there has not been a previous `GTID_LOG_EVENT`.

## MySQL 5.6 Release Notes

Similarly, using `mysqlbinlog` to concatenate and replay a relay log which contained a partial GTID transaction caused the above error. A relay log can contain a partial GTID transaction when`AUTO_POSITION` is enabled if a receiver thread is restarted when it is in the middle of transferring a transaction from a master. On restart the slave retrieves the full transaction again. In this case, the first relay log contains a partial GTID transaction and the second relay log contains the full GTID transaction again. When using `mysqlbinlog` to concatenate such a relay log, the partial transaction was not being correctly detected and therefore a `ROLLBACK` was not being correctly generated. The fix identifies partial GTID transactions using the format description event of the second relay log, ensuring that a `ROLLBACK`is correctly added. (Bug #70711, Bug #17650326)

- For small values of the `read_rnd_buffer_size` system variable, internal caching of temporary results

could fail and cause query execution failure. (Bug #20895852)

- The `normalize_statement()` function used by MySQL Enterprise Firewall could cause a server exit

for certain password-related statements. (Bug #20873209)

- A failed `FLUSH PRIVILEGES` statement followed by statements to create or drop accounts could cause

a server exit. (Bug #20857652)

- MySQL Enterprise Firewall debug code could leak memory. (Bug #20849157)
- `std::stringstream` code used by MySQL Enterprise Firewall could cause a server exit. (Bug

#20848536)

- `SHOW VARIABLES` mutexes were being locked twice, resulting in a server exit. (Bug #20788853)
- `ull2dec()` was modified to avoid a problem with GCC 5 in optimized mode. (Bug #20768820)
- Using GCC 5, debug builds failed due to compiler warnings. (Bug #20768717)
- The `mysql_firewall_max_query_size` system variable should be read only at runtime, but it was

possible to modify it. (Bug #20608993)

- MySQL Enterprise Firewall could leak memory in the unlikely event of failure to store information in an

`INFORMATION_SCHEMA` table. (Bug #20593257)

- Under certain conditions, the `libedit` command-line library could write outside an array boundary and

cause a client program crash. (Bug #20318154)

- `mysql_config_editor` could exit abnormally while encrypting passwords. (Bug #20294225)
- Host value matching for the grant tables could fail to use the most specific of values that contained

wildcard characters. (Bug #20181776)

- For MySQL distributions linked against yaSSL, a corrupt client key file could cause clients to exit. (Bug

#20168526)

- For join queries with a large number of tables, the server could exit converting the join to a semijoin.

(Bug #20109861)

- Deleting rows from `mysql.user` following by granting privileges to a new account could result in a

server exit. (Bug #20031475)

- Renaming the `mysql.procs_priv` table and executing `SHOW GRANTS` resulted in a server exit. (Bug

#20006361)

- Within a stored procedure, access to view columns after DDL or `FLUSH TABLES` statements in the

procedure could cause a server exit. (Bug #19897405)

## MySQL 5.6 Release Notes

- Execution of certain `BINLOG` statements while temporary tables were open by `HANDLER` statements

could cause a server exit. (Bug #19894987, Bug #20449914)

- For a prepared statement with an `ORDER BY` that refers by column number to a `GROUP_CONCAT()`

expression that has an outer reference, repeated statement execution could cause a server exit. (Bug#19814337)

- `CMake` configuration was adjusted to handle new warnings reported by Clang 3.5, using the -

`Wpointer-bool-conversion` and `-Wundefined-bool-conversion` compiler options. (Bug#19584183)

- Loading corrupt spatial data into a `MyISAM` table could cause the server to exit during index building.

(Bug #19573096)

- Specifying `--general_log_file=` (with an empty value) at server startup caused the server to fail

and exit. (Bug #19392264)

- `CMake` configuration was adjusted to handle warnings reported by Clang 3.3. (Bug #17486216)
- Some MySQL Enterprise Firewall diagnostic messages were written outside the control of the

`log_error_verbosity` system variable. (Bug #76612, Bug #20848331)

- The server rejected empty `COM_SHUTDOWN` packets. (Bug #76552, Bug #20810928)

References: This issue is a regression of: Bug #14525642.

- A `Provides` rule in RPM `.spec` files misspelled “mysql-embedded” as “mysql-emdedded”. (Bug

#76385, Bug #20734434)

- Inappropriate `-Werror` options could appear in `mysql_config --cflags` output. (Bug #76019, Bug

#20590904)

- Using a MySQL 5.6 version of `mysqladmin` to change the password for an account on a MySQL 5.7.6

installation resulted in an unusable account password. (Bug #76018, Bug #20590548)

- AddressSanitizer compilation errors were silenced. (Bug #75739, Bug #20459338, Bug #75740, Bug

#20459363)

- In the `threads` Performance Schema table, the `PROCESSLIST_STATE` and `PROCESSLIST_INFO`

values did not change for the `thread/sql/main` main thread instrument as the thread state changed.

(Bug #74517, Bug #19887143)

- Certain queries for the `INFORMATION_SCHEMA` `TABLES` and `COLUMNS` tables could lead to excessive

memory use when there were large numbers of empty `InnoDB` tables. (Bug #72322, Bug #18592390)

- Queries that included a `HAVING` clause based on nondeterministic functions could produce incorrect

results. (Bug #69638, Bug #17055185)

- For logging of prepared statements to the general query log, the `Execute` line was logged after

statement execution, not before. (Bug #69453, Bug #16953758, Bug #20536590)

- MySQL failed to compile using OpenSSL 0.9.8e. (Bug #68999, Bug #16861371)

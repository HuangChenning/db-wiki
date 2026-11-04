---
title: "Changes in MySQL 5.6.26 (2015-07-24, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=50"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

This release adds support for Debian 8 and Ubuntu 15.04.

- MySQL Enterprise Notes
- Performance Schema Notes
- Security Notes
- Functionality Added or Changed
- Bugs Fixed

> MySQL Enterprise Notes

- MySQL Enterprise Edition incorporates these changes for MySQL Enterprise Firewall:
- The firewall implements a `DETECTING` intrusion-detection mode. For accounts in this mode, the

firewall detects suspicious statements and writes them to the error log but does not deny access.

## MySQL 5.6 Release Notes

The new `Firewall_access_suspicious` status variable counts the number of such statements.

The `sp_set_firewall_mode()` stored procedure now synchronizes between in-memory rules and those in persistent storage for `DETECTING` mode, just as it does for `PROTECTING` mode.

- A new `sp_reload_firewall_rules()` stored procedure reloads the in-memory rules for a

registered account from the rules stored in the `mysql.firewall_whitelist` table, providing better control over firewall operation for individual accounts.

- A new `mysql_firewall_flush_status()` function resets firewall access-counter status variables.

To upgrade MySQL Enterprise Firewall if you have a version installed from a previous release, first uninstall the old version. Then install the new version and register your firewall configuration again. For instructions, see Installing or Uninstalling MySQL Enterprise Firewall. (WL #8510)

> Performance Schema Notes

- Current-event timing now provides more information. Previously, while a wait, stage, or statement

event was executing, the respective tables displayed the event with `TIMER_START` populated, but with

```
TIMER_END and TIMER_WAIT as NULL:
events_waits_current
events_stages_current
events_statements_current
```

To make it possible to determine how long a not-yet-completed event has been running, the timer columns now are set as follows:

- `TIMER_START` is populated (unchanged from previous behavior)
- `TIMER_END` is populated with the current timer value
- `TIMER_WAIT` is populated with the time elapsed so far (`TIMER_END` − `TIMER_START`)

To find events that have not yet completed (that is, have no `END_EVENT_ID`) and have taken longer than N picoseconds thus far, monitoring applications can use this expression in queries:

```
WHERE END_EVENT_ID IS NULL AND TIMER_WAIT > N
```

(Bug #75156, Bug #20889406)

> Security Notes

- Due to the LogJam issue (https://weakdh.org/), OpenSSL has changed the Diffie-Hellman key length

parameters for openssl-1.0.1n and up. OpenSSL has provided a detailed explanation at http://openssl.org/news/secadv_20150611.txt. To adopt this change in MySQL, the following modifications were made:

- The key length used in `vio/viosslfactories.c` for creating Diffie-Hellman keys has been

increased from 512 to 2,048 bits.

- The linked OpenSSL library for the MySQL Commercial Server has been updated from version 1.0.1m

to version 1.0.1p. Issues fixed in the new version are described at http://www.openssl.org/news/vulnerabilities.html. This change does not affect the Oracle-produced MySQL Community build of MySQL Server, which uses the yaSSL library instead.

(Bug #77275, Bug #21221862, Bug #18367167, Bug #21307471, Bug #21449838)

## MySQL 5.6 Release Notes

> Functionality Added or Changed

- Replication: When using a multithreaded slave, each worker thread has its own queue of transactions

to process. In previous MySQL versions, `STOP SLAVE` waited for all workers to process their entire queue. This logic has been changed so that `STOP SLAVE` first finds the newest transaction that was committed by any worker thread. Then, it waits for all workers to complete transactions older than that.

Newer transactions are not processed. The new logic allows `STOP SLAVE` to complete faster in case some worker queues contain multiple transactions. (Bug #75525, Bug #20369401)

- Previously, the `max_digest_length` system variable controlled the maximum digest length for all

server functions that computed statement digests. However, whereas the Performance Schema may need to maintain many digest values, other server functions such as MySQL Enterprise Firewall need only one digest per session. Increasing the `max_digest_length` value has little impact on total memory requirements for those functions, but can increase Performance Schema memory requirements significantly. To enable configuring digest length separately for the Performance Schema, its digest length is now controlled by the new `performance_schema_max_digest_length` system variable.

(Bug #20963147)

- Previously, changes to the `validate_password` plugin dictionary file (named by the

`validate_password_dictionary_file` system variable) while the server was running required a restart for the server to recognize the changes. Now `validate_password_dictionary_file` can be set at runtime and assigning a value causes the named file to be read without a restart.

In addition, two new status variables are available.

`validate_password_dictionary_file_last_parsed` indicates when the dictionary file was last read, and `validate_password_dictionary_file_words_count` indicates how many words it contains. (Bug #66697, Bug #14588145)

> Bugs Fixed

- InnoDB: The `ib_cursor_moveto` function did not accept a search tuple with fewer fields than are

defined for the index. (Bug #21121197, Bug #77083)

- InnoDB: The `ib_table_truncate` function failed to release a transaction, resulting in a hang on

server shutdown. (Bug #21121164, Bug #77084)

- InnoDB: The `ib_open_table_by_id` function passed an incorrect argument to

`dict_table_open_on_id`. (Bug #21121084, Bug #77100)

- InnoDB: On Unix-like platforms, `os_file_create_simple_no_error_handling_func` and

`os_file_create_func` opened files in different modes when `innodb_flush_method` was set to`O_DIRECT`. (Bug #21113036, Bug #76627)

- InnoDB: Opening a foreign key-referenced table with `foreign_key_checks` enabled resulted in an

error when the table or database name contained special characters. (Bug #21094069, Bug #77043)

- InnoDB: The `page_zip_verify_checksum` function returned false for a valid compressed page. (Bug

#21086723)

- InnoDB: An `ALTER TABLE ... IMPORT TABLESPACE` operation on a table with prefix index failed

with a schema mismatch error. (Bug #20977779, Bug #76877)

- InnoDB: A failure to load a change buffer bitmap page during a concurrent delete tablespace operation

caused a server exit. (Bug #20878735)

- InnoDB: An assertion was raised when `InnoDB` attempted to dereference a NULL foreign key object.

(Bug #20762798)

## MySQL 5.6 Release Notes

- InnoDB: Importing a tablespace with a full-text index resulted in an assertion when attempting to rebuild

the index. (Bug #20637494)

- InnoDB: After dropping a full-text search index, the hidden `FTS_DOC_ID` and `FTS_DOC_ID_INDEX`

columns prevented online DDL operations. (Bug #20590013, Bug #76012)

- InnoDB: The `InnoDB` `memcached` plugin handled unsigned NOT NULL integer columns incorrectly.

Thanks to Piotr Jurkiewicz for the patch. (Bug #20535517, Bug #75864)

- InnoDB: A `DROP DATABASE` operation raised an assertion. (Bug #19929435)
- InnoDB: An index record was not found on rollback due to inconsistencies in the `purge_node_t`

structure. The inconsistency resulted in warnings and error messages such as “error in sec index entry update”, “unable to purge a record”, and “tried to purge sec index entry not marked for deletion”. (Bug#19138298, Bug #70214, Bug #21126772, Bug #21065746)

- Partitioning: In certain cases, `ALTER TABLE ... REBUILD PARTITION` was not handled correctly

when executed on a locked table. (Bug #75677, Bug #20437706)

- Replication: When using GTIDs, a multithreaded slave which had `relay_log_recovery=1` and

that stopped unexpectedly could encounter a `relay-log-recovery cannot be executed when``the slave was stopped with an error or killed in MTS mode` error upon restart. The fix ensures that the relay log recovery process checks if GTIDs are in use or not. If GTIDs are in use, the multithreaded slave recovery process uses the GTID protocol to fill any unprocessed transactions. (Bug#73397, Bug #19316063)

- Replication: When two slaves with the same `server_uuid` were configured to replicate from a single

master, the I/O thread of the slaves kept reconnecting and generating new relay log files without new content. In such a situation, the master now generates an error which is sent to the slave. By receiving this error from the master, the slave I/O thread does not try to reconnect, avoiding this problem. (Bug#72581, Bug #18731252)

- Incorrect cost calculation for the semijoin Duplicate Weedout strategy could result in a server exit. (Bug

#21184091)

- MySQL Enterprise Firewall recorded prepared statements as they were received by the server, not as

normalized digests. (Bug #20929568)

- For MySQL Enterprise Firewall operation, `max_digest_length` had to be larger than

`mysql_firewall_max_query_size` or normalized statements were truncated. The`mysql_firewall_max_query_size` has been removed so that issue no longer applies, but`max_digest_length` should still be set large enough to avoid statement truncation. (Bug #20894024)

- Enabling MySQL Enterprise Firewall and binary logging could result in the server reading freed memory.

(Bug #20848324)

- For large values of `max_digest_length`, the Performance Schema could encounter an overflow error

when computing memory requirements, resulting in a server exit. (Bug #20738072)

- The Spencer `regex` library used for the `REGEXP` operator could be subject to heap overflow in some

circumstances. (Bug #20642505)

- A buffer-overflow error could occur for `mysqlslap` during option parsing. (Bug #20605441)
- An off-by-one error in string-copying code could result in a buffer overflow. (Bug #20359808)
- `GROUP BY` or `ORDER BY` on a `CHAR(0) NOT NULL` column could lead to a server exit. (Bug

#19660891)

## MySQL 5.6 Release Notes

- For some status variables that should monotonically increase, `SHOW GLOBAL STATUS` in one session

could show them as decreasing when other concurrent sessions changed user or disconnected. (Bug#18591145)

- An unnecessary `memset()` call invoked during Performance Schema digest operations has been

removed, which improves performance by reducing overhead. (Bug #77863, Bug #21528683)

- `mysql-systemd-start` failed if `datadir` was set in `/etc/my.cnf`. (Bug #77357, Bug #21262883)
- Compilation failed when building MySQL without the Performance Schema. (Bug #77292, Bug

#21229433)

- A call to the MySQL Enterprise Firewall `sp_set_firewall_mode()` stored procedure with an invalid

user name produced an error but added the user to the `firewall_users` table anyway. (Bug #76914,Bug #21021875)

- Identifiers in normalized statements were sometimes quoted and sometimes not, an inconsistency

that caused matching failure for statement digests and digest texts. This caused problems for MySQL Enterprise Firewall and for Performance Schema aggregation by digest. Identifiers now are quoted consistently. (Bug #76723, Bug #20896539)

- Ubuntu packages were missing dependencies for `killall` and `psmisc`. (Bug #76716, Bug #20893836)
- On OS X 10.10 (Yosemite), `mysqld` failed to start automatically. The startup item has been replaced

with a `launchd` job, which enables the preference pane check box for automatic startup to work again.

(Bug #74434, Bug #19858350)

- When choosing join order, the optimizer could incorrectly calculate the cost of a table scan and choose a

table scan over a more efficient `eq_ref` join. (Bug #71584, Bug #18194196)

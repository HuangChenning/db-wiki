---
title: "Changes in MySQL 5.6.0 (Not released, Milestone 4)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=288"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note This is a milestone release, for use at your own risk. Upgrades between milestone releases (or from a milestone release to a GA release) are not supported.

Significant development changes take place in milestone releases and you may encounter compatibility issues, such as data format changes that require attention in addition to the usual procedure of running `mysql_upgrade`. For example, you may find it necessary to dump your data with `mysqldump` before the upgrade and reload it afterward. (Making a backup before the upgrade is a prudent precaution in any case.)

- Deprecation and Removal Notes
- Performance Schema Notes
- Globally Unique Server IDs

## MySQL 5.6 Release Notes

- Functionality Added or Changed
- Bugs Fixed

> Deprecation and Removal Notes

- Replication: These unused and deprecated items have been removed: the `--init-rpl-role` and

`--rpl-recovery-rank` options, the `rpl_recovery_rank` system variable, and the `Rpl_status`status variable. (Bug #54649, Bug #11762095)References: See also: Bug #34437, Bug #11747900, Bug #34635, Bug #11747961.

- In MySQL 5.5, setting `optimizer_search_depth` to the deprecated value of 63 switched to the

algorithm used in MySQL 5.0.0 (and previous versions) for performing searches. The value of 63 is now treated as invalid. (WL #5369)

> Performance Schema Notes

- The Performance Schema now includes instrumentation for table input and output. Instrumented

operations include row-level accesses to persistent base tables or temporary tables. Operations that affect rows are fetch, insert, update, and delete. For a view, waits are associated with base tables referenced by the view. (WL #4895)

> Globally Unique Server IDs

- Replication: Globally unique IDs for MySQL servers were implemented. A UUID is now obtained

automatically when the MySQL server starts. The server first checks for a UUID written in the `auto.cnf`file (in the server's data directory), and uses this UUID if found. Otherwise, the server generates a new UUID and saves it to this file (and creates the file if it does not already exist). This UUID is available as the `server_uuid` system variable.

MySQL replication masters and slaves know each other's UUIDs. The value of a slave's UUID can be read in the output of `SHOW SLAVE HOSTS`. After a slave is started using `START SLAVE`, the value of the master's UUID is available on the slave in the output of `SHOW SLAVE STATUS`. (Bug #33815, Bug#11747723, WL #4677)References: See also: Bug #16927, Bug #11745543.

> Functionality Added or Changed

- Partitioning: It is now possible to exchange a partition of a partitioned table or a subpartition of a

subpartitioned table with a nonpartitioned table that otherwise has the same structure using the `ALTER``TABLE ... EXCHANGE PARTITION` statement. This can be used, for example, for importing and exporting partitions.

For more information and examples, see Exchanging Partitions and Subpartitions with Tables. (WL#4445)

- Replication: The `SHOW SLAVE STATUS` statement now has a `Master_Info_File` field indicating the

location of the `master.info` file. (Bug #50316, Bug #11758151)

- Replication: MySQL now supports delayed replication such that a slave server deliberately lags

behind the master by at least a specified amount of time. The default delay is 0 seconds. Use the new`MASTER_DELAY` option for `CHANGE MASTER TO` to set the delay to N seconds:

```
CHANGE MASTER TO MASTER_DELAY = N;
```

## MySQL 5.6 Release Notes

An event received from the master is not executed until at least N seconds later than its execution on the master.

`START SLAVE` and `STOP SLAVE` take effect immediately and ignore any delay. `RESET SLAVE` resets the delay to 0.

`SHOW SLAVE STATUS` has three new fields that provide information about the delay:

- `SQL_Delay`: The number of seconds that the slave must lag the master.

```
- SQL_Remaining_Delay: When Slave_SQL_Running_State is Waiting until
```

`MASTER_DELAY seconds after master executed event`, this field contains the number of seconds left of the delay. At other times, this field is `NULL`.

- `Slave_SQL_Running_State`: The state of the SQL thread (analogous to `Slave_IO_State`). The

value is identical to the `State` value of the SQL thread as displayed by `SHOW PROCESSLIST`.

When the slave SQL thread is waiting for the delay to elapse before executing an event, `SHOW``PROCESSLIST` displays its `State` value as `Waiting until MASTER_DELAY seconds after`

```
master executed event.
```

The `relay-log.info` file now contains the delay value, so the file format has changed. See Replication Metadata Repositories. In particular, the first line of the file now indicates how many lines are in the file. If you downgrade a slave server to a version older than MySQL 5.6, the older server will not read the file correctly. To address this, modify the file in a text editor to delete the initial line containing the number of lines.

The introduction of delayed replication entails these restrictions:

- Previously the `BINLOG` statement could execute all types of events. Now it can execute only format

description events and row events.

- The output from `mysqlbinlog --base64-output=ALWAYS` cannot be parsed. `ALWAYS` becomes

an invalid value for this option in 5.6.1.

For additional information, see Delayed Replication. (Bug #28760, Bug #11746794, WL #344)

- The Romansh locale `'rm_CH'` is now a permissible value for the `lc_time_names` system variable.

(Bug #50915, Bug #11758678, WL #5303)

- `mysqlbinlog` now has a `--binlog-row-event-max-size` option to enable large row events to be

read from binary log files. (Bug #49932)

- `mysqldump` now has an `--add-drop-trigger` option which adds a `DROP TRIGGER IF EXISTS`

statement before each dumped trigger definition. (Bug #34325, Bug #11747863)

- Vietnamese collations were added for the Unicode character sets. Those based on Unicode

Collation Algorithm 5.2.0 have names of the form `xxx_vietnamese_520_ci` (for example,`utf8_vietnamese_520_ci`). Those based on Unicode Collation Algorithm 4.0.0 have names of the form `xxx_vietnamese_ci` (for example, `utf8_vietnamese_ci`). These collations are the same as the corresponding `xxx_unicode_520_ci` and `xxx_unicode_ci` collations except for precomposed characters which are accented versions of “A”, “D”, “E”, “O”, and “U”. There is no change to ideographic characters derived from Chinese. There are no digraphs. (WL #3865)

- Unicode collation names now may include a version number to indicate the Unicode Collation Algorithm

(UCA) version on which the collation is based. Initial collations thus created use version UCA 5.2.0. For

## MySQL 5.6 Release Notes

example, `utf8_unicode_520_ci` is based on UCA 5.2.0. UCA-based Unicode collation names that do not include a version number are based on version 4.0.0.

`LOWER()` and `UPPER()` perform case folding according to the collation of their argument. A character that has uppercase and lowercase versions only in a Unicode version more recent than 4.0.0 will be converted by these functions only if the argument has a collation that uses a recent enough UCA version.

The LDML rules for creating user-defined collations are extended to permit an optional `version`attribute in `<collation>` tags to indicate the UCA version on which the collation is based. If the`version` attribute is omitted, its default value is `4.0.0`. See Adding a UCA Collation to a Unicode Character Set. (WL #2673)

- The Unicode character sets now have a `xxx_german2_ci` collation that provides DIN-2 (phone book)

ordering (for example, `utf8_german2_ci`). See Unicode Character Sets. (WL #4013)

- `mysqlbinlog` now has the capability to back up a binary log in its original binary format. When invoked

with the `--read-from-remote-server` and `--raw` options, `mysqlbinlog` connects to a server,requests the log files, and writes output files in the same format as the originals. See Using mysqlbinlog to Back Up Binary Log Files. (WL #4783)

- A new SQL function, `WEIGHT_STRING()`, returns the weight string for an input string. The weight string

represents the sorting and comparison value of the input string. See String Functions and Operators.

(WL #3716)

> Bugs Fixed

- Security Fix: A security bug was fixed. (Bug #49124)
- InnoDB: The server could crash on shutdown, if started with `--innodb-use-system-malloc=0`.

(Bug #55581, Bug #11762927)

- Replication: The internal flag indicating whether a user value was signed or unsigned

(`unsigned_flag`) could sometimes change between the time that the user value was recorded for logging purposes and the time that the value was actually written to the binary log, which could lead to inconsistency. Now `unsigned_flag` is copied when the user variable value is copied, and the copy of`unsigned_flag` is then used for logging. (Bug #51426, Bug #11759138)References: See also: Bug #49562, Bug #11757508.

- Microsoft Windows: On Windows, an IPv6 connection to the server could not be made using an IPv4

address or host name. (Bug #52381, Bug #11760016)

- Microsoft Windows: On Windows, the `my_rename()` function failed to check whether the source file

existed. (Bug #51861, Bug #11759540)

- Microsoft Windows: On Windows, `mysqlslap` crashed for attempts to connect using shared memory.

(Bug #31173, Bug #11747181, Bug #59107, Bug #11766072)

- The embedded server could crash when determining which directories to search for option files. (Bug

#55062, Bug #11762465)

- Performance Schema code was subject to a buffer overflow. (Bug #53363)
- Subquery execution for `EXPLAIN` could be done incorrectly and raise an assertion. (Bug #52317, Bug

#11759957)

## MySQL 5.6 Release Notes

- There was a mixup between `GROUP BY` and `ORDER BY` concerning which indexes should be considered

or permitted during query optimization. (Bug #52081, Bug #11759746)

- The `ref` column of `EXPLAIN` output for subquery lines could be missing information. (Bug #50257, Bug

#11758106)

- Passwords for `CREATE USER` statements were written to the binary log in cleartext rather than in

ciphertext. (Bug #50172)

- The `BLACKHOLE` storage engine failed to load on Solaris and OpenSolaris if DTrace probes had been

enabled. (Bug #47748, Bug #11755909)

- Some error messages included a literal `mysql` database name rather than a parameter for the database

name. (Bug #46792, Bug #11755079)

- In the `ER_TABLEACCESS_DENIED_ERROR` error message, the command name parameter could be

truncated. (Bug #45355, Bug #11753840)

- To forestall the occurrence of possible relocation errors in the future, `libmysys`, `libmystrings`, and

`libdbug` have been changed from normal libraries to “noinst” `libtool` helper libraries, and are no longer installed as separate libraries. (Bug #29791, Bug #11746931)

- A suboptimal query execution plan could be chosen when there were several possible `range` and `ref`

accesses. Now preference is given to the keys that match the most parts and choosing the best one among them. (Bug #26106, Bug #11746406)

- Searches for data on a partial index for a column using the `utf8` character set failed. (Bug #24858)
- For queries with `GROUP BY`, `FORCE INDEX` was not ignored as it should have been when it would result

in a more expensive query execution plan. (Bug #18144, Bug #11745649)

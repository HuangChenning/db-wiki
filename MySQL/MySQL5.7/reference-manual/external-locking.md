---
title: "8.11.5 External Locking"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/external-locking.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.11.5 External Locking

External locking is the use of file system locking to manage contention for [`MyISAM`](myisam-storage-engine.md) database tables by multiple processes. External locking is used in situations where a single process such as the MySQL server cannot be assumed to be the only process that requires access to tables. Here are some examples:

- If you run multiple servers that use the same database directory (not recommended), each server must have external locking enabled.
- If you use [**myisamchk**](myisamchk.md) to perform table maintenance operations on [`MyISAM`](myisam-storage-engine.md) tables, you must either ensure that the server is not running, or that the server has external locking enabled so that it locks table files as necessary to coordinate with [**myisamchk**](myisamchk.md) for access to the tables. The same is true for use of [**myisampack**](myisampack.md) to pack [`MyISAM`](myisam-storage-engine.md) tables.
	If the server is run with external locking enabled, you can use [**myisamchk**](myisamchk.md) at any time for read operations such a checking tables. In this case, if the server tries to update a table that [**myisamchk**](myisamchk.md) is using, the server waits for [**myisamchk**](myisamchk.md) to finish before it continues.
	If you use [**myisamchk**](myisamchk.md) for write operations such as repairing or optimizing tables, or if you use [**myisampack**](myisampack.md) to pack tables, you *must* always ensure that the [**mysqld**](mysqld.md) server is not using the table. If you do not stop [**mysqld**](mysqld.md), at least do a [**mysqladmin flush-tables**](mysqladmin.md) before you run [**myisamchk**](myisamchk.md). Your tables *may become corrupted* if the server and [**myisamchk**](myisamchk.md) access the tables simultaneously.

With external locking in effect, each process that requires access to a table acquires a file system lock for the table files before proceeding to access the table. If all necessary locks cannot be acquired, the process is blocked from accessing the table until the locks can be obtained (after the process that currently holds the locks releases them).

External locking affects server performance because the server must sometimes wait for other processes before it can access tables.

External locking is unnecessary if you run a single server to access a given data directory (which is the usual case) and if no other programs such as [**myisamchk**](myisamchk.md) need to modify tables while the server is running. If you only *read* tables with other programs, external locking is not required, although [**myisamchk**](myisamchk.md) might report warnings if the server changes tables while [**myisamchk**](myisamchk.md) is reading them.

With external locking disabled, to use [**myisamchk**](myisamchk.md), you must either stop the server while [**myisamchk**](myisamchk.md) executes or else lock and flush the tables before running [**myisamchk**](myisamchk.md). (See [Section 8.12.1, “System Factors”](system-optimization.md).) To avoid this requirement, use the [`CHECK TABLE`](check-table.md) and [`REPAIR TABLE`](repair-table.md) statements to check and repair [`MyISAM`](myisam-storage-engine.md) tables.

For [**mysqld**](mysqld.md), external locking is controlled by the value of the [`skip_external_locking`](server-system-variables.md) system variable. When this variable is enabled, external locking is disabled, and vice versa. External locking is disabled by default.

Use of external locking can be controlled at server startup by using the [`--external-locking`](server-options.md) or [`--skip-external-locking`](server-options.md) option.

If you do use external locking option to enable updates to [`MyISAM`](myisam-storage-engine.md) tables from many MySQL processes, you must ensure that the following conditions are satisfied:

- Do not use the query cache for queries that use tables that are updated by another process.
- Do not start the server with the [`delay_key_write`](server-system-variables.md) system variable set to `ALL` or use the `DELAY_KEY_WRITE=1` table option for any shared tables. Otherwise, index corruption can occur.

The easiest way to satisfy these conditions is to always use [`--external-locking`](server-options.md) together with [`--delay-key-write=OFF`](server-system-variables.md) and [`--query-cache-size=0`](server-system-variables.md). (This is not done by default because in many setups it is useful to have a mixture of the preceding options.)
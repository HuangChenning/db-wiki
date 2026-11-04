---
title: "25.5.14 ndb_index_stat — NDB Index Statistics Utility"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-index-stat.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.14 ndb\_index\_stat — NDB Index Statistics Utility

**ndb\_index\_stat** provides per-fragment statistical information about indexes on `NDB` tables. This includes cache version and age, number of index entries per partition, and memory consumption by indexes.

#### Usage

To obtain basic index statistics about a given [`NDB`](mysql-cluster.md) table, invoke **ndb\_index\_stat** as shown here, with the name of the table as the first argument and the name of the database containing this table specified immediately following it, using the `--database` (`-d`) option:

```
ndb_index_stat table -d database
```

In this example, we use **ndb\_index\_stat** to obtain such information about an `NDB` table named `mytable` in the `test` database:

```
$> ndb_index_stat -d test mytable
table:City index:PRIMARY fragCount:2
sampleVersion:3 loadTime:1399585986 sampleCount:1994 keyBytes:7976
query cache: valid:1 sampleCount:1994 totalBytes:27916
times in ms: save: 7.133 sort: 1.974 sort per sample: 0.000
```

`sampleVersion` is the version number of the cache from which the statistics data is taken. Running **ndb\_index\_stat** with the `--update` option causes sampleVersion to be incremented.

`loadTime` shows when the cache was last updated. This is expressed as seconds since the Unix Epoch.

`sampleCount` is the number of index entries found per partition. You can estimate the total number of entries by multiplying this by the number of fragments (shown as `fragCount`).

`sampleCount` can be compared with the cardinality of [`SHOW INDEX`](show-index.md) or [`INFORMATION_SCHEMA.STATISTICS`](information-schema-statistics-table.md), although the latter two provide a view of the table as a whole, while **ndb\_index\_stat** provides a per-fragment average.

`keyBytes` is the number of bytes used by the index. In this example, the primary key is an integer, which requires four bytes for each index, so `keyBytes` can be calculated in this case as shown here:

```
keyBytes = sampleCount * (4 bytes per index) = 1994 * 4 = 7976
```

This information can also be obtained using the corresponding column definitions from [`INFORMATION_SCHEMA.COLUMNS`](information-schema-columns-table.md) (this requires a MySQL Server and a MySQL client application).

`totalBytes` is the total memory consumed by all indexes on the table, in bytes.

Timings shown in the preceding examples are specific to each invocation of **ndb\_index\_stat**.

The `--verbose` option provides some additional output, as shown here:

```
$> ndb_index_stat -d test mytable --verbose
random seed 1337010518
connected
loop 1 of 1
table:mytable index:PRIMARY fragCount:4
sampleVersion:2 loadTime:1336751773 sampleCount:0 keyBytes:0
read stats
query cache created
query cache: valid:1 sampleCount:0 totalBytes:0
times in ms: save: 20.766 sort: 0.001
disconnected

$>
```

If the output from the program is empty, this may indicate that no statistics yet exist. To force them to be created (or updated if they already exist), invoke **ndb\_index\_stat** with the `--update` option, or execute [`ANALYZE TABLE`](analyze-table.md) on the table in the [**mysql**](mysql.md) client.

#### Options

The following table includes options that are specific to the NDB Cluster **ndb\_index\_stat** utility. Additional descriptions are listed following the table.

**Table 25.36 Command-line options used with the program ndb\_index\_stat**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | REMOVED: 8.0.31 |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 8.0) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --core-file                  ` | Write core file on error; used in debugging | REMOVED: 8.0.31 |
| `--database=name`,  `                  -d                 name  ` | Name of database containing table | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --delete                  ` | Delete index statistics for table, stopping any auto-update previously configured | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --dump                  ` | Print query cache | (Supported in all NDB releases based on MySQL 8.0) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --loops=#                  ` | Set the number of times to perform given command; default is 0 | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | REMOVED: 8.0.31 |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --query=#                  ` | Perform random range queries on first key attr (must be int unsigned) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-drop                  ` | Drop any statistics tables and events in NDB kernel (all statistics are lost) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-create                  ` | Create all statistics tables and events in NDB kernel, if none of them already exist | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-create-if-not-exist                  ` | Create any statistics tables and events in NDB kernel that do not already exist | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-create-if-not-valid                  ` | Create any statistics tables or events that do not already exist in the NDB kernel, after dropping any that are invalid | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-check                  ` | Verify that NDB system index statistics and event tables exist | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-skip-tables                  ` | Do not apply sys-\* options to tables | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --sys-skip-events                  ` | Do not apply sys-\* options to events | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --update                  ` | Update index statistics for table, restarting any auto-update previously configured | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--verbose`,  `                  -v                  ` | Turn on verbose output | (Supported in all NDB releases based on MySQL 8.0) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 8.0) |

- `--character-sets-dir`
	Directory containing character sets.
- `--connect-retries`
	| Command-Line Format | `--connect-retries=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `12` |
	| Minimum Value | `0` |
	| Maximum Value | `12` |
	Number of times to retry connection before giving up.
- `--connect-retry-delay`
	| Command-Line Format | `--connect-retry-delay=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `5` |
	| Minimum Value | `0` |
	| Maximum Value | `5` |
	Number of seconds to wait between attempts to contact management server.
- `--connect-string`
	| Command-Line Format | `--connect-string=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
- `--core-file`
	Write core file on error; used in debugging.
- ``--database=*`name`*``, ``-d *`name`*``
	| Command-Line Format | `--database=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	| Minimum Value |  |
	| Maximum Value |  |
	The name of the database that contains the table being queried.
- `--defaults-extra-file`
	| Command-Line Format | `--defaults-extra-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given file after global files are read.
- `--defaults-file`
	| Command-Line Format | `--defaults-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read default options from given file only.
- `--defaults-group-suffix`
	| Command-Line Format | `--defaults-group-suffix=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Also read groups with concat(group, suffix).
- `--delete`
	| Command-Line Format | `--delete` |
	| --- | --- |
	Delete the index statistics for the given table, stopping any auto-update that was previously configured.
- `--dump`
	| Command-Line Format | `--dump` |
	| --- | --- |
	Dump the contents of the query cache.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- ``--loops=*`#`*``
	| Command-Line Format | `--loops=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `MAX_INT` |
	Repeat commands this number of times (for use in testing).
- `--ndb-connectstring`
	| Command-Line Format | `--ndb-connectstring=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf.
- `--ndb-mgmd-host`
	| Command-Line Format | `--ndb-mgmd-host=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
- `--ndb-nodeid`
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Set node ID for this node, overriding any ID set by `--ndb-connectstring`.
- `--ndb-optimized-node-selection`
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- ``--query=*`#`*``
	| Command-Line Format | `--query=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `MAX_INT` |
	Perform random range queries on first key attribute (must be int unsigned).
- `--sys-drop`
	| Command-Line Format | `--sys-drop` |
	| --- | --- |
	Drop all statistics tables and events in the NDB kernel. *This causes all statistics to be lost*.
- `--sys-create`
	| Command-Line Format | `--sys-create` |
	| --- | --- |
	Create all statistics tables and events in the NDB kernel. This works only if none of them exist previously.
- `--sys-create-if-not-exist`
	| Command-Line Format | `--sys-create-if-not-exist` |
	| --- | --- |
	Create any NDB system statistics tables or events (or both) that do not already exist when the program is invoked.
- `--sys-create-if-not-valid`
	| Command-Line Format | `--sys-create-if-not-valid` |
	| --- | --- |
	Create any NDB system statistics tables or events that do not already exist, after dropping any that are invalid.
- `--sys-check`
	| Command-Line Format | `--sys-check` |
	| --- | --- |
	Verify that all required system statistics tables and events exist in the NDB kernel.
- `--sys-skip-tables`
	| Command-Line Format | `--sys-skip-tables` |
	| --- | --- |
	Do not apply any `--sys-*` options to any statistics tables.
- `--sys-skip-events`
	| Command-Line Format | `--sys-skip-events` |
	| --- | --- |
	Do not apply any `--sys-*` options to any events.
- `--update`
	| Command-Line Format | `--update` |
	| --- | --- |
	Update the index statistics for the given table, and restart any auto-update that was previously configured.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--verbose`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Turn on verbose output.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

**ndb\_index\_stat system options.** The following options are used to generate and update the statistics tables in the NDB kernel. None of these options can be mixed with statistics options (see ndb\_index\_stat statistics options).

**ndb\_index\_stat statistics options.** The options listed here are used to generate index statistics. They work with a given table and database. They cannot be mixed with system options (see ndb\_index\_stat system options).
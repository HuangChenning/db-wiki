---
title: "25.5.13 ndb_import — Import CSV Data Into NDB"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster-programs-ndb-import.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 25.5.13 ndb\_import — Import CSV Data Into NDB

**ndb\_import** imports CSV-formatted data, such as that produced by [**mysqldump**](mysqldump.md) [`--tab`](mysqldump.md), directly into `NDB` using the NDB API. **ndb\_import** requires a connection to an NDB management server ([**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md)) to function; it does not require a connection to a MySQL Server.

#### Usage

```
ndb_import db_name file_name options
```

**ndb\_import** requires two arguments. *`db_name`* is the name of the database where the table into which to import the data is found; *`file_name`* is the name of the CSV file from which to read the data; this must include the path to this file if it is not in the current directory. The name of the file must match that of the table; the file's extension, if any, is not taken into consideration. Options supported by **ndb\_import** include those for specifying field separators, escapes, and line terminators, and are described later in this section.

**ndb\_import** rejects any empty lines which it reads from the CSV file, except when importing a single column, in which case an empty value can be used as the column value. **ndb\_import** handles this in the same manner as a [`LOAD DATA`](load-data.md) statement does.

**ndb\_import** must be able to connect to an NDB Cluster management server; for this reason, there must be an unused `[api]` slot in the cluster `config.ini` file.

To duplicate an existing table that uses a different storage engine, such as [`InnoDB`](innodb-storage-engine.md), as an `NDB` table, use the [**mysql**](mysql.md) client to perform a [`SELECT INTO         OUTFILE`](select-into.md) statement to export the existing table to a CSV file, then to execute a [`CREATE TABLE         LIKE`](create-table-like.md) statement to create a new table having the same structure as the existing table, then perform [`ALTER TABLE ...         ENGINE=NDB`](alter-table.md) on the new table; after this, from the system shell, invoke **ndb\_import** to load the data into the new `NDB` table. For example, an existing `InnoDB` table named `myinnodb_table` in a database named `myinnodb` can be exported into an `NDB` table named `myndb_table` in a database named `myndb` as shown here, assuming that you are already logged in as a MySQL user with the appropriate privileges:

1. In the [**mysql**](mysql.md) client:
	```
	mysql> USE myinnodb;
	mysql> SELECT * INTO OUTFILE '/tmp/myndb_table.csv'
	     >  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '\\'
	     >  LINES TERMINATED BY '\n'
	     >  FROM myinnodbtable;
	mysql> CREATE DATABASE myndb;
	mysql> USE myndb;
	mysql> CREATE TABLE myndb_table LIKE myinnodb.myinnodb_table;
	mysql> ALTER TABLE myndb_table ENGINE=NDB;
	mysql> EXIT;
	Bye
	$>
	```
	Once the target database and table have been created, a running [**mysqld**](mysqld.md) is no longer required. You can stop it using [**mysqladmin shutdown**](mysqladmin.md) or another method before proceeding, if you wish.
2. In the system shell:
	```
	# if you are not already in the MySQL bin directory:
	$> cd path-to-mysql-bin-dir
	$> ndb_import myndb /tmp/myndb_table.csv --fields-optionally-enclosed-by='"' \
	    --fields-terminated-by="," --fields-escaped-by='\\'
	```
	The output should resemble what is shown here:
	```
	job-1 import myndb.myndb_table from /tmp/myndb_table.csv
	job-1 [running] import myndb.myndb_table from /tmp/myndb_table.csv
	job-1 [success] import myndb.myndb_table from /tmp/myndb_table.csv
	job-1 imported 19984 rows in 0h0m9s at 2277 rows/s
	jobs summary: defined: 1 run: 1 with success: 1 with failure: 0
	$>
	```

All options that can be used with **ndb\_import** are shown in the following table. Additional descriptions follow the table.

- `--abort-on-error`
	| Command-Line Format | `--abort-on-error` |
	| --- | --- |
	Dump core on any fatal error; used for debugging only.
- `--ai-increment` = *`#`*
	| Command-Line Format | `--ai-increment=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	For a table with a hidden primary key, specify the autoincrement increment, like the [`auto_increment_increment`](replication-options-source.md) system variable does in the MySQL Server.
- `--ai-offset` = *`#`*
	| Command-Line Format | `--ai-offset=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	For a table with hidden primary key, specify the autoincrement offset. Similar to the [`auto_increment_offset`](replication-options-source.md) system variable.
- `--ai-prefetch-sz` = *`#`*
	| Command-Line Format | `--ai-prefetch-sz=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1024` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	For a table with a hidden primary key, specify the number of autoincrement values that are prefetched. Behaves like the [`ndb_autoincrement_prefetch_sz`](mysql-cluster-options-variables.md) system variable does in the MySQL Server.
- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	Directory containing character sets.
- `--connections` = *`#`*
	| Command-Line Format | `--connections=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	Number of cluster connections to create.
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
- `--continue`
	| Command-Line Format | `--continue` |
	| --- | --- |
	When a job fails, continue to the next job.
- `--core-file`
	| Command-Line Format | `--core-file` |
	| --- | --- |
	Write core file on error; used in debugging.
- `--csvopt` = *`string`*
	| Command-Line Format | `--csvopt=opts` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Provides a shortcut method for setting typical CSV import options. The argument to this option is a string consisting of one or more of the following parameters:
	- `c`: Fields terminated by comma
	- `d`: Use defaults, except where overridden by another parameter
	- `n`: Lines terminated by `\n`
	- `q`: Fields optionally enclosed by double quote characters (`"`)
	- `r`: Line terminated by `\r`
	The order of parameters used in the argument to this option is handled such that the rightmost parameter always takes precedence over any potentially conflicting parameters which have already been used in the same argument value. This also applies to any duplicate instances of a given parameter.
	This option is intended for use in testing under conditions in which it is difficult to transmit escapes or quotation marks.
- `--db-workers` = *`#`*
	| Command-Line Format | `--db-workers=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `4` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	Number of threads, per data node, executing database operations.
- `--defaults-file`
	| Command-Line Format | `--defaults-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read default options from given file only.
- `--defaults-extra-file`
	| Command-Line Format | `--defaults-extra-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given file after global files are read.
- `--defaults-group-suffix`
	| Command-Line Format | `--defaults-group-suffix=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Also read groups with concat(group, suffix).
- `--errins-type` = *`name`*
	| Command-Line Format | `--errins-type=name` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `stopjob`  `stopall`  `sighup`  `sigint`  `list` |
	Error insert type; use `list` as the *`name`* value to obtain all possible values. This option is used for testing purposes only.
- `--errins-delay` = *`#`*
	| Command-Line Format | `--errins-delay=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1000` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | ms |
	Error insert delay in milliseconds; random variation is added. This option is used for testing purposes only.
- `--fields-enclosed-by` = *`char`*
	| Command-Line Format | `--fields-enclosed-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	This works in the same way as the `FIELDS ENCLOSED             BY` option does for the [`LOAD             DATA`](load-data.md) statement, specifying a character to be interpreted as quoting field values. For CSV input, this is the same as `--fields-optionally-enclosed-by`.
- `--fields-escaped-by` = *`name`*
	| Command-Line Format | `--fields-escaped-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `\` |
	Specify an escape character in the same way as the `FIELDS ESCAPED BY` option does for the SQL [`LOAD DATA`](load-data.md) statement.
- `--fields-optionally-enclosed-by` = *`char`*
	| Command-Line Format | `--fields-optionally-enclosed-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	This works in the same way as the `FIELDS OPTIONALLY             ENCLOSED BY` option does for the [`LOAD DATA`](load-data.md) statement, specifying a character to be interpreted as optionally quoting field values. For CSV input, this is the same as `--fields-enclosed-by`.
- `--fields-terminated-by` = *`char`*
	| Command-Line Format | `--fields-terminated-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `\t` |
	This works in the same way as the `FIELDS TERMINATED             BY` option does for the [`LOAD             DATA`](load-data.md) statement, specifying a character to be interpreted as the field separator.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- `--idlesleep` = *`#`*
	| Command-Line Format | `--idlesleep=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	| Unit | ms |
	Number of milliseconds to sleep waiting for more work to perform.
- `--idlespin` = *`#`*
	| Command-Line Format | `--idlespin=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	Number of times to retry before sleeping.
- `--ignore-lines` = *`#`*
	| Command-Line Format | `--ignore-lines=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	Cause ndb\_import to ignore the first *`#`* lines of the input file. This can be employed to skip a file header that does not contain any data.
- `--input-type` = *`name`*
	| Command-Line Format | `--input-type=name` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `csv` |
	| Valid Values | `random`  `csv` |
	Set the type of input type. The default is `csv`; `random` is intended for testing purposes only..
- `--input-workers` = *`#`*
	| Command-Line Format | `--input-workers=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `4` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	Set the number of threads processing input.
- `--keep-state`
	| Command-Line Format | `--keep-state` |
	| --- | --- |
	By default, ndb\_import removes all state files (except non-empty `*.rej` files) when it completes a job. Specify this option (nor argument is required) to force the program to retain all state files instead.
- `--lines-terminated-by` = *`name`*
	| Command-Line Format | `--lines-terminated-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `\n` |
	This works in the same way as the `LINES TERMINATED             BY` option does for the [`LOAD             DATA`](load-data.md) statement, specifying a character to be interpreted as end-of-line.
- `--log-level` = *`#`*
	| Command-Line Format | `--log-level=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `2` |
	Performs internal logging at the given level. This option is intended primarily for internal and development use.
	In debug builds of NDB only, the logging level can be set using this option to a maximum of 4.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Skips reading options from the login path file.
- `--max-rows` = *`#`*
	| Command-Line Format | `--max-rows=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Import only this number of input data rows; the default is 0, which imports all rows.
- `--missing-ai-column`
	| Command-Line Format | `--missing-ai-column='name'` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option can be employed when importing a single table, or multiple tables. When used, it indicates that the CSV file being imported does not contain any values for an `AUTO_INCREMENT` column, and that **ndb\_import** should supply them; if the option is used and the `AUTO_INCREMENT` column contains any values, the import operation cannot proceed.
- `--monitor` = *`#`*
	| Command-Line Format | `--monitor=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `2` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Periodically print the status of a running job if something has changed (status, rejected rows, temporary errors). Set to 0 to disable this reporting. Setting to 1 prints any change that is seen. Higher values reduce the frequency of this status reporting.
- `--ndb-connectstring`
	| Command-Line Format | `--ndb-connectstring=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Set connection string for connecting to [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md). Syntax: ``[nodeid=*`id`*;][host=]*`hostname`*[:*`port`*]``. Overrides entries in `NDB_CONNECTSTRING` and `my.cnf`.
- `--ndb-mgm-tls`
	| Command-Line Format | `--ndb-mgm-tls=level` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `relaxed` |
	| Valid Values | `relaxed`  `strict` |
	Sets the level of TLS support required to connect to the management server; one of `relaxed` or `strict`. `relaxed` (the default) means that a TLS connection is attempted, but success is not required; `strict` means that TLS is required to connect.
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
	| Command-Line Format | `--ndb-optimized-node-selection` |
	| --- | --- |
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--ndb-tls-search-path`
	| Command-Line Format | `--ndb-tls-search-path=list` |
	| --- | --- |
	| Type | Path name |
	| Default Value (Unix) | `$HOME/ndb-tls` |
	| Default Value (Windows) | `$HOMEDIR/ndb-tls` |
	Specify a list of directories to search for a CA file. On Unix platforms, the directory names are separated by colons (`:`); on Windows systems, the semicolon character (`;`) is used as the separator. A directory reference may be relative or absolute; it may contain one or more environment variables, each denoted by a prefixed dollar sign (`$`), and expanded prior to use.
	Searching begins with the leftmost named directory and proceeds from left to right until a file is found. An empty string denotes an empty search path, which causes all searches to fail. A string consisting of a single dot (`.`) indicates that the search path limited to the current working directory.
	If no search path is supplied, the compiled-in default value is used. This value depends on the platform used: On Windows, this is `\ndb-tls`; on other platforms (including Linux), it is `$HOME/ndb-tls`. This can be overridden by compiling NDB Cluster using [`-DWITH_NDB_TLS_SEARCH_PATH`](source-configuration-options.md).
- `--no-asynch`
	| Command-Line Format | `--no-asynch` |
	| --- | --- |
	Run database operations as batches, in single transactions.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--no-hint`
	| Command-Line Format | `--no-hint` |
	| --- | --- |
	Do not use distribution key hinting to select a data node.
- `--opbatch` = *`#`*
	| Command-Line Format | `--opbatch=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `256` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Set a limit on the number of operations (including blob operations), and thus the number of asynchronous transactions, per execution batch.
- `--opbytes` = *`#`*
	| Command-Line Format | `--opbytes=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Set a limit on the number of bytes per execution batch. Use 0 for no limit.
- `--output-type` = *`name`*
	| Command-Line Format | `--output-type=name` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `ndb` |
	| Valid Values | `null` |
	Set the output type. `ndb` is the default. `null` is used only for testing.
- `--output-workers` = *`#`*
	| Command-Line Format | `--output-workers=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `2` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	Set the number of threads processing output or relaying database operations.
- `--pagesize` = *`#`*
	| Command-Line Format | `--pagesize=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `4096` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Align I/O buffers to the given size.
- `--pagecnt` = *`#`*
	| Command-Line Format | `--pagecnt=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `64` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	Set the size of I/O buffers as multiple of page size. The CSV input worker allocates buffer that is doubled in size.
- `--polltimeout` = *`#`*
	| Command-Line Format | `--polltimeout=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1000` |
	| Minimum Value | `1` |
	| Maximum Value | `4294967295` |
	| Unit | ms |
	Set a timeout per poll for completed asynchronous transactions; polling continues until all polls are completed, or until an error occurs.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--rejects` = *`#`*
	| Command-Line Format | `--rejects=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	Limit the number of rejected rows (rows with permanent errors) in the data load. The default is 0, which means that any rejected row causes a fatal error. Any rows causing the limit to be exceeded are added to the `.rej` file.
	The limit imposed by this option is effective for the duration of the current run. A run restarted using `--resume` is considered a “new” run for this purpose.
- `--resume`
	| Command-Line Format | `--resume` |
	| --- | --- |
	If a job is aborted (due to a temporary db error or when interrupted by the user), resume with any rows not yet processed.
- `--rowbatch` = *`#`*
	| Command-Line Format | `--rowbatch=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | rows |
	Set a limit on the number of rows per row queue. Use 0 for no limit.
- `--rowbytes` = *`#`*
	| Command-Line Format | `--rowbytes=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `262144` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | bytes |
	Set a limit on the number of bytes per row queue. Use 0 for no limit.
- `--stats`
	| Command-Line Format | `--stats` |
	| --- | --- |
	Save information about options related to performance and other internal statistics in files named `*.sto` and `*.stt`. These files are always kept on successful completion (even if `--keep-state` is not also specified).
- `--state-dir` = *`name`*
	| Command-Line Format | `--state-dir=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `.` |
	Where to write the state files (``*`tbl_name`*.map``, ``*`tbl_name`*.rej``, ``*`tbl_name`*.res``, and ``*`tbl_name`*.stt``) produced by a run of the program; the default is the current directory.
- ``--table=*`name`*``
	| Command-Line Format | `--table=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `[input file base name]` |
	By default, **ndb\_import** attempts to import data into a table whose name is the base name of the CSV file from which the data is being read. You can override the choice of table name by specifying it with the `--table` option (short form `-t`).
- `--tempdelay` = *`#`*
	| Command-Line Format | `--tempdelay=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `10` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	| Unit | ms |
	Number of milliseconds to sleep between temporary errors.
- `--temperrors` = *`#`*
	| Command-Line Format | `--temperrors=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	Number of times a transaction can fail due to a temporary error, per execution batch. The default is 0, which means that any temporary error is fatal. Temporary errors do not cause any rows to be added to the `.rej` file.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose[=#]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Enable verbose output.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

As with [`LOAD DATA`](load-data.md), options for field and line formatting much match those used to create the CSV file, whether this was done using [`SELECT INTO ...         OUTFILE`](select-into.md), or by some other means. There is no equivalent to the [`LOAD DATA`](load-data.md) statement `STARTING WITH` option.
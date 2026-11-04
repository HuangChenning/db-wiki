---
title: "21.5.24 ndb_restore — Restore an NDB Cluster Backup"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-restore.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.24 ndb\_restore — Restore an NDB Cluster Backup

The NDB Cluster restoration program is implemented as a separate command-line utility **ndb\_restore**, which can normally be found in the MySQL `bin` directory. This program reads the files created as a result of the backup and inserts the stored information into the database.

Note

Beginning with NDB 7.5.15 and 7.6.11, this program no longer prints `NDBT_ProgramExit: ...` when it finishes its run. Applications depending on this behavior should be modified accordingly when upgrading from earlier releases.

**ndb\_restore** must be executed once for each of the backup files that were created by the [`START BACKUP`](mysql-cluster-backup-using-management-client.md) command used to create the backup (see [Section 21.6.8.2, “Using The NDB Cluster Management Client to Create a Backup”](mysql-cluster-backup-using-management-client.md)). This is equal to the number of data nodes in the cluster at the time that the backup was created.

Note

Before using **ndb\_restore**, it is recommended that the cluster be running in single user mode, unless you are restoring multiple data nodes in parallel. See [Section 21.6.6, “NDB Cluster Single User Mode”](mysql-cluster-single-user-mode.md), for more information.

Options that can be used with **ndb\_restore** are shown in the following table. Additional descriptions follow the table.

**Table 21.38 Command-line options used with the program ndb\_restore**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --allow-pk-changes[=0\|1]                  ` | Allow changes to set of columns making up table's primary key | ADDED: NDB 7.6.14 |
| `                  --append                  ` | Append data to tab-delimited file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --backup-path=path                  ` | Path to backup files directory | (Supported in all NDB releases based on MySQL 5.7) |
| `--backupid=#`,  `  -b                 #  ` | Restore from backup having this ID | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | (Supported in all NDB releases based on MySQL 5.7) |
| `--connect=connection_string`,  `  -c                 connection_string  ` | Alias for --connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 5.7) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --core-file                  ` | Write core file on error; used in debugging | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --disable-indexes                  ` | Causes indexes from backup to be ignored; may decrease time needed to restore data | (Supported in all NDB releases based on MySQL 5.7) |
| `--dont-ignore-systab-0`,  `                  -f                  ` | Do not ignore system table during restore; experimental only; not for production use | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --exclude-databases=list                  ` | List of one or more databases to exclude (includes those not named) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --exclude-intermediate-sql-tables[=TRUE\|FALSE]                  ` | Do not restore any intermediate tables (having names prefixed with '#sql-') that were left over from copying ALTER TABLE operations; specify FALSE to restore such tables | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --exclude-missing-columns                  ` | Causes columns from backup version of table that are missing from version of table in database to be ignored | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --exclude-missing-tables                  ` | Causes tables from backup that are missing from database to be ignored | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --exclude-tables=list                  ` | List of one or more tables to exclude (includes those in same database that are not named); each table reference must include database name | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --fields-enclosed-by=char                  ` | Fields are enclosed by this character | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --fields-optionally-enclosed-by                  ` | Fields are optionally enclosed by this character | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --fields-terminated-by=char                  ` | Fields are terminated by this character | (Supported in all NDB releases based on MySQL 5.7) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --hex                  ` | Print binary types in hexadecimal format | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ignore-extended-pk-updates[=0\|1]                  ` | Ignore log entries containing updates to columns now included in extended primary key | ADDED: NDB 7.6.14 |
| `                  --include-databases=list                  ` | List of one or more databases to restore (excludes those not named) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --include-tables=list                  ` | List of one or more tables to restore (excludes those in same database that are not named); each table reference must include database name | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --lines-terminated-by=char                  ` | Lines are terminated by this character | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 5.7) |
| `--lossy-conversions`,  `                  -L                  ` | Allow lossy conversions of column values (type demotions or changes in sign) when restoring data from backup | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --no-binlog                  ` | If mysqld is connected and using binary logging, do not log restored data | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 5.7) |
| `--no-restore-disk-objects`,  `                  -d                  ` | Do not restore objects relating to Disk Data | (Supported in all NDB releases based on MySQL 5.7) |
| `--no-upgrade`,  `                  -u                  ` | Do not upgrade array type for varsize attributes which do not already resize VAR data, and do not change column attributes | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-nodegroup-map=map`,  `                  -z                  ` | Specify node group map; unused, unsupported | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | (Supported in all NDB releases based on MySQL 5.7) |
| `--nodeid=#`,  `  -n                 #  ` | ID of node where backup was taken | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --num-slices=#                  ` | Number of slices to apply when restoring by slice | ADDED: NDB 7.6.13 |
| `--parallelism=#`,  `                  -p                 #  ` | Number of parallel transactions to use while restoring data | (Supported in all NDB releases based on MySQL 5.7) |
| `--preserve-trailing-spaces`,  `                  -P                  ` | Allow preservation of trailing spaces (including padding) when promoting fixed-width string types to variable-width types | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print                  ` | Print metadata, data, and log to stdout (equivalent to --print-meta --print-data --print-log) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-data                  ` | Print data to stdout | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-log                  ` | Print log to stdout | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-meta                  ` | Print metadata to stdout | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-sql-log                  ` | Write SQL log to stdout | ADDED: NDB 7.5.4 |
| `                  --progress-frequency=#                  ` | Print status of restore each given number of seconds | (Supported in all NDB releases based on MySQL 5.7) |
| `--promote-attributes`,  `                  -A                  ` | Allow attributes to be promoted when restoring data from backup | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --rebuild-indexes                  ` | Causes multithreaded rebuilding of ordered indexes found in backup; number of threads used is determined by setting BuildIndexThreads | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --remap-column=string                  ` | Apply offset to value of specified column using indicated function and arguments. Format is \[db\].\[tbl\].\[col\]:\[fn\]:\[args\]; see documentation for details | ADDED: NDB 7.6.14 |
| `--restore-data`,  `                  -r                  ` | Restore table data and logs into NDB Cluster using NDB API | (Supported in all NDB releases based on MySQL 5.7) |
| `--restore-epoch`,  `                  -e                  ` | Restore epoch info into status table; useful on replica cluster for starting replication; updates or inserts row in mysql.ndb\_apply\_status with ID 0 | (Supported in all NDB releases based on MySQL 5.7) |
| `--restore-meta`,  `                  -m                  ` | Restore metadata to NDB Cluster using NDB API | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --restore-privilege-tables                  ` | Restore MySQL privilege tables that were previously moved to NDB | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --rewrite-database=string                  ` | Restore to differently named database; format is olddb,newdb | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --skip-broken-objects                  ` | Ignore missing blob tables in backup file | (Supported in all NDB releases based on MySQL 5.7) |
| `--skip-table-check`,  `                  -s                  ` | Skip table structure check during restore | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --skip-unknown-objects                  ` | Causes schema objects not recognized by ndb\_restore to be ignored when restoring backup made from newer NDB version to older version | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --slice-id=#                  ` | Slice ID, when restoring by slices | ADDED: NDB 7.6.13 |
| `--tab=path`,  `  -T                 path  ` | Creates a tab-separated.txt file for each table in path provided | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --timestamp-printouts{=true\|false}                  ` | Prefix all info, error, and debug log messages with timestamps | ADDED: NDB 7.5.30, 5.7.41-ndb-7.6.26 |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --verbose=#                  ` | Level of verbosity in output | (Supported in all NDB releases based on MySQL 5.7) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 5.7) |

- `--allow-pk-changes`
	| Command-Line Format | `--allow-pk-changes[=0\|1]` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `1` |
	When this option is set to `1`, **ndb\_restore** allows the primary keys in a table definition to differ from that of the same table in the backup. This may be desirable when backing up and restoring between different schema versions with primary key changes on one or more tables, and it appears that performing the restore operation using ndb\_restore is simpler or mor efficient than issuing many [`ALTER TABLE`](alter-table.md) statements after restoring table schemas and data.
	The following changes in primary key definitions are supported by `--allow-pk-changes`:
	- **Extending the primary key**: A non-nullable column that exists in the table schema in the backup becomes part of the table's primary key in the database.
		Important
		When extending a table's primary key, any columns which become part of primary key must not be updated while the backup is being taken; any such updates discovered by **ndb\_restore** cause the restore operation to fail, even when no change in value takes place. In some cases, it may be possible to override this behavior using the `--ignore-extended-pk-updates` option; see the description of this option for more information.
	- **Contracting the primary key (1)**: A column that is already part of the table's primary key in the backup schema is no longer part of the primary key, but remains in the table.
	- **Contracting the primary key (2)**: A column that is already part of the table's primary key in the backup schema is removed from the table entirely.
	These differences can be combined with other schema differences supported by **ndb\_restore**, including changes to blob and text columns requiring the use of staging tables.
	Basic steps in a typical scenario using primary key schema changes are listed here:
	1. Restore table schemas using **ndb\_restore** `--restore-meta`
	2. Alter schema to that desired, or create it
	3. Back up the desired schema
	4. Run **ndb\_restore** `--disable-indexes` using the backup from the previous step, to drop indexes and constraints
	5. Run **ndb\_restore** `--allow-pk-changes` (possibly along with `--ignore-extended-pk-updates`, `--disable-indexes`, and possibly other options as needed) to restore all data
	6. Run **ndb\_restore** `--rebuild-indexes` using the backup made with the desired schema, to rebuild indexes and constraints
	When extending the primary key, it may be necessary for **ndb\_restore** to use a temporary secondary unique index during the restore operation to map from the old primary key to the new one. Such an index is created only when necessary to apply events from the backup log to a table which has an extended primary key. This index is named `NDB$RESTORE_PK_MAPPING`, and is created on each table requiring it; it can be shared, if necessary, by multiple instances of **ndb\_restore** instances running in parallel. (Running **ndb\_restore** `--rebuild-indexes` at the end of the restore process causes this index to be dropped.)
- `--append`
	| Command-Line Format | `--append` |
	| --- | --- |
	When used with the `--tab` and `--print-data` options, this causes the data to be appended to any existing files having the same names.
- `--backup-path` = *`dir_name`*
	| Command-Line Format | `--backup-path=path` |
	| --- | --- |
	| Type | Directory name |
	| Default Value | `./` |
	The path to the backup directory is required; this is supplied to **ndb\_restore** using the `--backup-path` option, and must include the subdirectory corresponding to the ID backup of the backup to be restored. For example, if the data node's [`DataDir`](mysql-cluster-ndbd-definition.md) is `/var/lib/mysql-cluster`, then the backup directory is `/var/lib/mysql-cluster/BACKUP`, and the backup files for the backup with the ID 3 can be found in `/var/lib/mysql-cluster/BACKUP/BACKUP-3`. The path may be absolute or relative to the directory in which the **ndb\_restore** executable is located, and may be optionally prefixed with `backup-path=`.
	It is possible to restore a backup to a database with a different configuration than it was created from. For example, suppose that a backup with backup ID `12`, created in a cluster with two storage nodes having the node IDs `2` and `3`, is to be restored to a cluster with four nodes. Then **ndb\_restore** must be run twice—once for each storage node in the cluster where the backup was taken. However, **ndb\_restore** cannot always restore backups made from a cluster running one version of MySQL to a cluster running a different MySQL version. See [Section 21.3.7, “Upgrading and Downgrading NDB Cluster”](mysql-cluster-upgrade-downgrade.md), for more information.
	Important
	It is not possible to restore a backup made from a newer version of NDB Cluster using an older version of **ndb\_restore**. You can restore a backup made from a newer version of MySQL to an older cluster, but you must use a copy of **ndb\_restore** from the newer NDB Cluster version to do so.
	For example, to restore a cluster backup taken from a cluster running NDB Cluster 7.6.36 to a cluster running NDB Cluster 7.5.36, you must use the **ndb\_restore** that comes with the NDB Cluster 7.6.36 distribution.
	For more rapid restoration, the data may be restored in parallel, provided that there is a sufficient number of cluster connections available. That is, when restoring to multiple nodes in parallel, you must have an `[api]` or `[mysqld]` section in the cluster `config.ini` file available for each concurrent **ndb\_restore** process. However, the data files must always be applied before the logs.
- `--backupid` = *`#`*, `-b`
	| Command-Line Format | `--backupid=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `none` |
	This option is used to specify the ID or sequence number of the backup, and is the same number shown by the management client in the ``Backup             *`backup_id`* completed`` message displayed upon completion of a backup. (See [Section 21.6.8.2, “Using The NDB Cluster Management Client to Create a Backup”](mysql-cluster-backup-using-management-client.md).)
	Important
	When restoring cluster backups, you must be sure to restore all data nodes from backups having the same backup ID. Using files from different backups can at best result in restoring the cluster to an inconsistent state, and may fail altogether.
	In NDB 7.5.13 and later, and in NDB 7.6.9 and later, this option is required.
- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	Directory containing character sets.
- `--connect`, `-c`
	| Command-Line Format | `--connect=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `localhost:1186` |
	Alias for `--ndb-connectstring`.
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
	| Command-Line Format | `--core-file` |
	| --- | --- |
	Write core file on error; used in debugging.
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
- `--disable-indexes`
	| Command-Line Format | `--disable-indexes` |
	| --- | --- |
	Disable restoration of indexes during restoration of the data from a native `NDB` backup. Afterwards, you can restore indexes for all tables at once with multithreaded building of indexes using `--rebuild-indexes`, which should be faster than rebuilding indexes concurrently for very large tables.
	Beginning with NDB 7.5.24 and NDB 7.6.20, this option also drops any foreign keys specified in the backup.
- `--dont-ignore-systab-0`, `-f`
	| Command-Line Format | `--dont-ignore-systab-0` |
	| --- | --- |
	Normally, when restoring table data and metadata, **ndb\_restore** ignores the copy of the [`NDB`](mysql-cluster.md) system table that is present in the backup. `--dont-ignore-systab-0` causes the system table to be restored. *This option is intended for experimental and development use only, and is not recommended in a production environment*.
- `--exclude-databases` = *`db-list`*
	| Command-Line Format | `--exclude-databases=list` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Comma-delimited list of one or more databases which should not be restored.
	This option is often used in combination with `--exclude-tables`; see that option's description for further information and examples.
- `--exclude-intermediate-sql-tables[`\= *`TRUE|FALSE]`*
	| Command-Line Format | `--exclude-intermediate-sql-tables[=TRUE\|FALSE]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	When performing copying [`ALTER             TABLE`](alter-table.md) operations, [**mysqld**](mysqld.md) creates intermediate tables (whose names are prefixed with `#sql-`). When `TRUE`, the `--exclude-intermediate-sql-tables` option keeps **ndb\_restore** from restoring such tables that may have been left over from these operations. This option is `TRUE` by default.
- `--exclude-missing-columns`
	| Command-Line Format | `--exclude-missing-columns` |
	| --- | --- |
	It is possible to restore only selected table columns using this option, which causes **ndb\_restore** to ignore any columns missing from tables being restored as compared to the versions of those tables found in the backup. This option applies to all tables being restored. If you wish to apply this option only to selected tables or databases, you can use it in combination with one or more of the `--include-*` or `--exclude-*` options described elsewhere in this section to do so, then restore data to the remaining tables using a complementary set of these options.
- `--exclude-missing-tables`
	| Command-Line Format | `--exclude-missing-tables` |
	| --- | --- |
	It is possible to restore only selected tables using this option, which causes **ndb\_restore** to ignore any tables from the backup that are not found in the target database.
- `--exclude-tables` = *`table-list`*
	| Command-Line Format | `--exclude-tables=list` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	List of one or more tables to exclude; each table reference must include the database name. Often used together with `--exclude-databases`.
	When `--exclude-databases` or `--exclude-tables` is used, only those databases or tables named by the option are excluded; all other databases and tables are restored by **ndb\_restore**.
	This table shows several invocations of **ndb\_restore** usng `--exclude-*` options (other options possibly required have been omitted for clarity), and the effects these options have on restoring from an NDB Cluster backup:
	**Table 21.39 Several invocations of ndb\_restore using --exclude-\* options, and the effects these options have on restoring from an NDB Cluster backup.**
	| Option | Result |
	| --- | --- |
	| `--exclude-databases=db1` | All tables in all databases except `db1` are restored; no tables in `db1` are restored |
	| `--exclude-databases=db1,db2` (or `--exclude-databases=db1` `--exclude-databases=db2`) | All tables in all databases except `db1` and `db2` are restored; no tables in `db1` or `db2` are restored |
	| `--exclude-tables=db1.t1` | All tables except `t1` in database `db1` are restored; all other tables in `db1` are restored; all tables in all other databases are restored |
	| `--exclude-tables=db1.t2,db2.t1` (or `--exclude-tables=db1.t2` `--exclude-tables=db2.t1)` | All tables in database `db1` except for `t2` and all tables in database `db2` except for table `t1` are restored; no other tables in `db1` or `db2` are restored; all tables in all other databases are restored |
	You can use these two options together. For example, the following causes all tables in all databases *except for* databases `db1` and `db2`, and tables `t1` and `t2` in database `db3`, to be restored:
	```
	$> ndb_restore [...] --exclude-databases=db1,db2 --exclude-tables=db3.t1,db3.t2
	```
	(Again, we have omitted other possibly necessary options in the interest of clarity and brevity from the example just shown.)
	You can use `--include-*` and `--exclude-*` options together, subject to the following rules:
	- The actions of all `--include-*` and `--exclude-*` options are cumulative.
	- All `--include-*` and `--exclude-*` options are evaluated in the order passed to ndb\_restore, from right to left.
	- In the event of conflicting options, the first (rightmost) option takes precedence. In other words, the first option (going from right to left) that matches against a given database or table “wins”.
	For example, the following set of options causes **ndb\_restore** to restore all tables from database `db1` except `db1.t1`, while restoring no other tables from any other databases:
	```
	--include-databases=db1 --exclude-tables=db1.t1
	```
	However, reversing the order of the options just given simply causes all tables from database `db1` to be restored (including `db1.t1`, but no tables from any other database), because the `--include-databases` option, being farthest to the right, is the first match against database `db1` and thus takes precedence over any other option that matches `db1` or any tables in `db1`:
	```
	--exclude-tables=db1.t1 --include-databases=db1
	```
- `--fields-enclosed-by` = *`char`*
	| Command-Line Format | `--fields-enclosed-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Each column value is enclosed by the string passed to this option (regardless of data type; see the description of `--fields-optionally-enclosed-by`).
- `--fields-optionally-enclosed-by`
	| Command-Line Format | `--fields-optionally-enclosed-by` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	The string passed to this option is used to enclose column values containing character data (such as [`CHAR`](char.md), [`VARCHAR`](char.md), [`BINARY`](binary-varbinary.md), [`TEXT`](blob.md), or [`ENUM`](enum.md)).
- `--fields-terminated-by` = *`char`*
	| Command-Line Format | `--fields-terminated-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `\t (tab)` |
	The string passed to this option is used to separate column values. The default value is a tab character (`\t`).
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- `--hex`
	| Command-Line Format | `--hex` |
	| --- | --- |
	If this option is used, all binary values are output in hexadecimal format.
- `--ignore-extended-pk-updates`
	| Command-Line Format | `--ignore-extended-pk-updates[=0\|1]` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `1` |
	When using the `--allow-pk-changes` option, columns which become part of a table's primary key must not be updated while the backup is being taken; such columns should keep the same values from the time values are inserted into them until the rows containing the values are deleted. If **ndb\_restore** encounters updates to these columns when restoring a backup, the restore fails. Because some applications may set values for all columns when updating a row, even when some column values are not changed, the backup may include log events appearing to update columns which are not in fact modified. In such cases you can set `--ignore-extended-pk-updates` to `1`, forcing **ndb\_restore** to ignore such updates.
	Important
	When causing these updates to be ignored, the user is responsible for ensuring that there are no updates to the values of any columns that become part of the primary key.
	For more information, see the description of `--allow-pk-changes`.
- `--include-databases` = *`db-list`*
	| Command-Line Format | `--include-databases=list` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Comma-delimited list of one or more databases to restore. Often used together with `--include-tables`; see the description of that option for further information and examples.
- `--include-tables` = *`table-list`*
	| Command-Line Format | `--include-tables=list` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Comma-delimited list of tables to restore; each table reference must include the database name.
	When `--include-databases` or `--include-tables` is used, only those databases or tables named by the option are restored; all other databases and tables are excluded by **ndb\_restore**, and are not restored.
	The following table shows several invocations of **ndb\_restore** using `--include-*` options (other options possibly required have been omitted for clarity), and the effects these have on restoring from an NDB Cluster backup:
	**Table 21.40 Several invocations of ndb\_restore using --include-\* options, and their effects on restoring from an NDB Cluster backup.**
	| Option | Result |
	| --- | --- |
	| `--include-databases=db1` | Only tables in database `db1` are restored; all tables in all other databases are ignored |
	| `--include-databases=db1,db2` (or `--include-databases=db1` `--include-databases=db2`) | Only tables in databases `db1` and `db2` are restored; all tables in all other databases are ignored |
	| `--include-tables=db1.t1` | Only table `t1` in database `db1` is restored; no other tables in `db1` or in any other database are restored |
	| `--include-tables=db1.t2,db2.t1` (or `--include-tables=db1.t2` `--include-tables=db2.t1`) | Only the table `t2` in database `db1` and the table `t1` in database `db2` are restored; no other tables in `db1`, `db2`, or any other database are restored |
	You can also use these two options together. For example, the following causes all tables in databases `db1` and `db2`, together with the tables `t1` and `t2` in database `db3`, to be restored (and no other databases or tables):
	```
	$> ndb_restore [...] --include-databases=db1,db2 --include-tables=db3.t1,db3.t2
	```
	(Again we have omitted other, possibly required, options in the example just shown.)
	It also possible to restore only selected databases, or selected tables from a single database, without any `--include-*` (or `--exclude-*`) options, using the syntax shown here:
	```
	ndb_restore other_options db_name,[db_name[,...] | tbl_name[,tbl_name][,...]]
	```
	In other words, you can specify either of the following to be restored:
	- All tables from one or more databases
	- One or more tables from a single database
- `--lines-terminated-by` = *`char`*
	| Command-Line Format | `--lines-terminated-by=char` |
	| --- | --- |
	| Type | String |
	| Default Value | `\n (linebreak)` |
	Specifies the string used to end each line of output. The default is a linefeed character (`\n`).
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--lossy-conversions`, `-L`
	| Command-Line Format | `--lossy-conversions` |
	| --- | --- |
	This option is intended to complement the `--promote-attributes` option. Using `--lossy-conversions` allows lossy conversions of column values (type demotions or changes in sign) when restoring data from backup. With some exceptions, the rules governing demotion are the same as for MySQL replication; see [Section 16.4.1.10.2, “Replication of Columns Having Different Data Types”](replication-features-differing-tables.md), for information about specific type conversions currently supported by attribute demotion.
	Beginning with NDB 7.5.23 and NDB 7.6.19, this option also makes it possible to restore a `NULL` column as `NOT NULL`. The column must not contain any `NULL` entries; otherwise **ndb\_restore** stops with an error.
	**ndb\_restore** reports any truncation of data that it performs during lossy conversions once per attribute and column.
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
- `--ndb-nodegroup-map` = *`map`*, `-z`
	| Command-Line Format | `--ndb-nodegroup-map=map` |
	| --- | --- |
	Intended for restoring a backup taken from one node group to a different node group, but never completely implemented; unsupported.
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
- `--no-binlog`
	| Command-Line Format | `--no-binlog` |
	| --- | --- |
	This option prevents any connected SQL nodes from writing data restored by **ndb\_restore** to their binary logs.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--no-restore-disk-objects`, `-d`
	| Command-Line Format | `--no-restore-disk-objects` |
	| --- | --- |
	This option stops **ndb\_restore** from restoring any NDB Cluster Disk Data objects, such as tablespaces and log file groups; see [Section 21.6.11, “NDB Cluster Disk Data Tables”](mysql-cluster-disk-data.md), for more information about these.
- `--no-upgrade`, `-u`
	| Command-Line Format | `--no-upgrade` |
	| --- | --- |
	When using **ndb\_restore** to restore a backup, [`VARCHAR`](char.md) columns created using the old fixed format are resized and recreated using the variable-width format now employed. This behavior can be overridden by specifying `--no-upgrade`.
- `--nodeid` = *`#`*, `-n`
	| Command-Line Format | `--nodeid=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `none` |
	Specify the node ID of the data node on which the backup was taken.
	When restoring to a cluster with different number of data nodes from that where the backup was taken, this information helps identify the correct set or sets of files to be restored to a given node. (In such cases, multiple files usually need to be restored to a single data node.) See [Section 21.5.24.2, “Restoring to a different number of data nodes”](ndb-restore-different-number-nodes.md), for additional information and examples.
	In NDB 7.5.13 and later, and in NDB 7.6.9 and later, this option is required.
- `--num-slices` = *`#`*
	| Command-Line Format | `--num-slices=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `1024` |
	When restoring a backup by slices, this option sets the number of slices into which to divide the backup. This allows multiple instances of **ndb\_restore** to restore disjoint subsets in parallel, potentially reducing the amount of time required to perform the restore operation.
	A *slice* is a subset of the data in a given backup; that is, it is a set of fragments having the same slice ID, specified using the `--slice-id` option. The two options must always be used together, and the value set by `--slice-id` must always be less than the number of slices.
	**ndb\_restore** encounters fragments and assigns each one a fragment counter. When restoring by slices, a slice ID is assigned to each fragment; this slice ID is in the range 0 to 1 less than the number of slices. For a table that is not a [`BLOB`](blob.md) table, the slice to which a given fragment belongs is determined using the formula shown here:
	```
	[slice_ID] = [fragment_counter] % [number_of_slices]
	```
	For a [`BLOB`](blob.md) table, a fragment counter is not used; the fragment number is used instead, along with the ID of the main table for the `BLOB` table (recall that `NDB` stores *`BLOB`* values in a separate table internally). In this case, the slice ID for a given fragment is calculated as shown here:
	```
	[slice_ID] =
	([main_table_ID] + [fragment_ID]) % [number_of_slices]
	```
	Thus, restoring by *`N`* slices means running *`N`* instances of **ndb\_restore**, all with ``--num-slices=*`N`*`` (along with any other necessary options) and one each with `--slice-id=1`, `--slice-id=2`, `--slice-id=3`, and so on through ``slice-id=*`N`*-1``.
- `--parallelism` = *`#`*, `-p`
	| Command-Line Format | `--parallelism=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `128` |
	| Minimum Value | `1` |
	| Maximum Value | `1024` |
	**ndb\_restore** uses single-row transactions to apply many rows concurrently. This parameter determines the number of parallel transactions (concurrent rows) that an instance of **ndb\_restore** tries to use. By default, this is 128; the minimum is 1, and the maximum is 1024.
	The work of performing the inserts is parallelized across the threads in the data nodes involved. This mechanism is employed for restoring bulk data from the `.Data` file—that is, the fuzzy snapshot of the data; it is not used for building or rebuilding indexes. The change log is applied serially; index drops and builds are DDL operations and handled separately. There is no thread-level parallelism on the client side of the restore.
- `--preserve-trailing-spaces`, `-P`
	| Command-Line Format | `--preserve-trailing-spaces` |
	| --- | --- |
	Cause trailing spaces to be preserved when promoting a fixed-width character data type to its variable-width equivalent—that is, when promoting a [`CHAR`](char.md) column value to [`VARCHAR`](char.md), or a `BINARY` column value to [`VARBINARY`](binary-varbinary.md). Otherwise, any trailing spaces are dropped from such column values when they are inserted into the new columns.
	Note
	Although you can promote [`CHAR`](char.md) columns to [`VARCHAR`](char.md) and `BINARY` columns to [`VARBINARY`](binary-varbinary.md), you cannot promote [`VARCHAR`](char.md) columns to [`CHAR`](char.md) or [`VARBINARY`](binary-varbinary.md) columns to `BINARY`.
- `--print`
	| Command-Line Format | `--print` |
	| --- | --- |
	Causes **ndb\_restore** to print all data, metadata, and logs to `stdout`. Equivalent to using the `--print-data`, `--print-meta`, and `--print-log` options together.
	Note
	Use of `--print` or any of the `--print_*` options is in effect performing a dry run. Including one or more of these options causes any output to be redirected to `stdout`; in such cases, **ndb\_restore** makes no attempt to restore data or metadata to an NDB Cluster.
- `--print-data`
	| Command-Line Format | `--print-data` |
	| --- | --- |
	Cause **ndb\_restore** to direct its output to `stdout`. Often used together with one or more of `--tab`, `--fields-enclosed-by`, `--fields-optionally-enclosed-by`, `--fields-terminated-by`, `--hex`, and `--append`.
	[`TEXT`](blob.md) and [`BLOB`](blob.md) column values are always truncated. Such values are truncated to the first 256 bytes in the output. This cannot currently be overridden when using `--print-data`.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--print-log`
	| Command-Line Format | `--print-log` |
	| --- | --- |
	Cause **ndb\_restore** to output its log to `stdout`.
- `--print-meta`
	| Command-Line Format | `--print-meta` |
	| --- | --- |
	Print all metadata to `stdout`.
- `print-sql-log`
	| Command-Line Format | `--print-sql-log` |
	| --- | --- |
	Log SQL statements to `stdout`. Use the option to enable; normally this behavior is disabled. The option checks before attempting to log whether all the tables being restored have explicitly defined primary keys; queries on a table having only the hidden primary key implemented by `NDB` cannot be converted to valid SQL.
	This option does not work with tables having [`BLOB`](blob.md) columns.
	The `--print-sql-log` option was added in NDB 7.5.4. (Bug #13511949)
- `--progress-frequency` = *`N`*
	| Command-Line Format | `--progress-frequency=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `65535` |
	Print a status report each *`N`* seconds while the backup is in progress. 0 (the default) causes no status reports to be printed. The maximum is 65535.
- `--promote-attributes`, `-A`
	| Command-Line Format | `--promote-attributes` |
	| --- | --- |
	**ndb\_restore** supports limited attribute promotion in much the same way that it is supported by MySQL replication; that is, data backed up from a column of a given type can generally be restored to a column using a “larger, similar” type. For example, data from a `CHAR(20)` column can be restored to a column declared as `VARCHAR(20)`, `VARCHAR(30)`, or `CHAR(30)`; data from a [`MEDIUMINT`](integer-types.md) column can be restored to a column of type [`INT`](integer-types.md) or [`BIGINT`](integer-types.md). See [Section 16.4.1.10.2, “Replication of Columns Having Different Data Types”](replication-features-differing-tables.md), for a table of type conversions currently supported by attribute promotion.
	Beginning with NDB 7.5.23 and NDB 7.6.19, this option also makes it possible to restore a `NOT NULL` column as `NULL`.
	Attribute promotion by **ndb\_restore** must be enabled explicitly, as follows:
	1. Prepare the table to which the backup is to be restored. **ndb\_restore** cannot be used to re-create the table with a different definition from the original; this means that you must either create the table manually, or alter the columns which you wish to promote using [`ALTER TABLE`](alter-table.md) after restoring the table metadata but before restoring the data.
	2. Invoke **ndb\_restore** with the `--promote-attributes` option (short form `-A`) when restoring the table data. Attribute promotion does not occur if this option is not used; instead, the restore operation fails with an error.
	When converting between character data types and `TEXT` or `BLOB`, only conversions between character types ([`CHAR`](char.md) and [`VARCHAR`](char.md)) and binary types ([`BINARY`](binary-varbinary.md) and [`VARBINARY`](binary-varbinary.md)) can be performed at the same time. For example, you cannot promote an [`INT`](integer-types.md) column to [`BIGINT`](integer-types.md) while promoting a `VARCHAR` column to `TEXT` in the same invocation of **ndb\_restore**.
	Converting between [`TEXT`](blob.md) columns using different character sets is not supported, and is expressly disallowed.
	When performing conversions of character or binary types to `TEXT` or `BLOB` with **ndb\_restore**, you may notice that it creates and uses one or more staging tables named ``*`table_name`*$ST*`node_id`*``. These tables are not needed afterwards, and are normally deleted by **ndb\_restore** following a successful restoration.
- `--rebuild-indexes`
	| Command-Line Format | `--rebuild-indexes` |
	| --- | --- |
	Enable multithreaded rebuilding of the ordered indexes while restoring a native `NDB` backup. The number of threads used for building ordered indexes by **ndb\_restore** with this option is controlled by the [`BuildIndexThreads`](mysql-cluster-ndbd-definition.md) data node configuration parameter and the number of LDMs.
	It is necessary to use this option only for the first run of **ndb\_restore**; this causes all ordered indexes to be rebuilt without using `--rebuild-indexes` again when restoring subsequent nodes. You should use this option prior to inserting new rows into the database; otherwise, it is possible for a row to be inserted that later causes a unique constraint violation when trying to rebuild the indexes.
	Building of ordered indices is parallelized with the number of LDMs by default. Offline index builds performed during node and system restarts can be made faster using the [`BuildIndexThreads`](mysql-cluster-ndbd-definition.md) data node configuration parameter; this parameter has no effect on dropping and rebuilding of indexes by **ndb\_restore**, which is performed online.
	Rebuilding of unique indexes uses disk write bandwidth for redo logging and local checkpointing. An insufficient amount of this bandwith can lead to redo buffer overload or log overload errors. In such cases you can run **ndb\_restore** `--rebuild-indexes` again; the process resumes at the point where the error occurred. You can also do this when you have encountered temporary errors. You can repeat execution of **ndb\_restore** `--rebuild-indexes` indefinitely; you may be able to stop such errors by reducing the value of `--parallelism`. If the problem is insufficient space, you can increase the size of the redo log ([`FragmentLogFileSize`](mysql-cluster-ndbd-definition.md) node configuration parameter), or you can increase the speed at which LCPs are performed ([`MaxDiskWriteSpeed`](mysql-cluster-ndbd-definition.md) and related parameters), in order to free space more quickly.
- ``--remap-column=*`db`*.*`tbl`*.*`col`*:*`fn`*:*`args`*``
	| Command-Line Format | `--remap-column=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	When used together with `--restore-data`, this option applies a function to the value of the indicated column. Values in the argument string are listed here:
	- *`db`*: Database name, following any renames performed by `--rewrite-database`.
	- *`tbl`*: Table name.
	- *`col`*: Name of the column to be updated. This column must be of type [`INT`](integer-types.md) or [`BIGINT`](integer-types.md). The column can also be but is not required to be `UNSIGNED`.
	- *`fn`*: Function name; currently, the only supported name is `offset`.
	- *`args`*: Arguments supplied to the function. Currently, only a single argument, the size of the offset to be added by the `offset` function, is supported. Negative values are supported. The size of the argument cannot exceed that of the signed variant of the column's type; for example, if *`col`* is an `INT` column, then the allowed range of the argument passed to the `offset` function is `-2147483648` to `2147483647` (see [Section 11.1.2, “Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT”](integer-types.md)).
		If applying the offset value to the column would cause an overflow or underflow, the restore operation fails. This could happen, for example, if the column is a `BIGINT`, and the option attempts to apply an offset value of 8 on a row in which the column value is 4294967291, since `4294967291 + 8                 = 4294967299 > 4294967295`.
	This option can be useful when you wish to merge data stored in multiple source instances of NDB Cluster (all using the same schema) into a single destination NDB Cluster, using NDB native backup (see [Section 21.6.8.2, “Using The NDB Cluster Management Client to Create a Backup”](mysql-cluster-backup-using-management-client.md)) and **ndb\_restore** to merge the data, where primary and unique key values are overlapping between source clusters, and it is necessary as part of the process to remap these values to ranges that do not overlap. It may also be necessary to preserve other relationships between tables. To fulfill such requirements, it is possible to use the option multiple times in the same invocation of **ndb\_restore** to remap columns of different tables, as shown here:
	```
	$> ndb_restore --restore-data --remap-column=hr.employee.id:offset:1000 \
	    --remap-column=hr.manager.id:offset:1000 --remap-column=hr.firstaiders.id:offset:1000
	```
	(Other options not shown here may also be used.)
	`--remap-column` can also be used to update multiple columns of the same table. Combinations of multiple tables and columns are possible. Different offset values can also be used for different columns of the same table, like this:
	```
	$> ndb_restore --restore-data --remap-column=hr.employee.salary:offset:10000 \
	    --remap-column=hr.employee.hours:offset:-10
	```
	When source backups contain duplicate tables which should not be merged, you can handle this by using `--exclude-tables`, `--exclude-databases`, or by some other means in your application.
	Information about the structure and other characteristics of tables to be merged can obtained using [`SHOW CREATE TABLE`](show-create-table.md); the [**ndb\_desc**](mysql-cluster-programs-ndb-desc.md) tool; and [`MAX()`](aggregate-functions.md), [`MIN()`](aggregate-functions.md), [`LAST_INSERT_ID()`](information-functions.md), and other MySQL functions.
	Replication of changes from merged to unmerged tables, or from unmerged to merged tables, in separate instances of NDB Cluster is not supported.
- `--restore-data`, `-r`
	| Command-Line Format | `--restore-data` |
	| --- | --- |
	Output [`NDB`](mysql-cluster.md) table data and logs.
- `--restore-epoch`, `-e`
	| Command-Line Format | `--restore-epoch` |
	| --- | --- |
	Add (or restore) epoch information to the cluster replication status table. This is useful for starting replication on an NDB replica cluster. When this option is used, the row in the `mysql.ndb_apply_status` having `0` in the `id` column is updated if it already exists; such a row is inserted if it does not already exist. (See [Section 21.7.9, “NDB Cluster Backups With NDB Cluster Replication”](mysql-cluster-replication-backups.md).)
- `--restore-meta`, `-m`
	| Command-Line Format | `--restore-meta` |
	| --- | --- |
	This option causes **ndb\_restore** to print [`NDB`](mysql-cluster.md) table metadata.
	The first time you run the **ndb\_restore** restoration program, you also need to restore the metadata. In other words, you must re-create the database tables—this can be done by running it with the `--restore-meta` (`-m`) option. Restoring the metadata need be done only on a single data node; this is sufficient to restore it to the entire cluster.
	In older versions of NDB Cluster, tables whose schemas were restored using this option used the same number of partitions as they did on the original cluster, even if it had a differing number of data nodes from the new cluster. In NDB 7.5.2 and later, when restoring metadata, this is no longer an issue; **ndb\_restore** now uses the default number of partitions for the target cluster, unless the number of local data manager threads is also changed from what it was for data nodes in the original cluster.
	Note
	The cluster should have an empty database when starting to restore a backup. (In other words, you should start the data nodes with [`--initial`](mysql-cluster-programs-ndbd.md) prior to performing the restore.)
- `--restore-privilege-tables`
	| Command-Line Format | `--restore-privilege-tables` |
	| --- | --- |
	**ndb\_restore** does not by default restore distributed MySQL privilege tables. This option causes **ndb\_restore** to restore the privilege tables.
	This works only if the privilege tables were converted to [`NDB`](mysql-cluster.md) before the backup was taken. For more information, see [Section 21.6.13, “Distributed Privileges Using Shared Grant Tables”](mysql-cluster-privilege-distribution.md).
- `--rewrite-database` = *`olddb,newdb`*
	| Command-Line Format | `--rewrite-database=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `none` |
	This option makes it possible to restore to a database having a different name from that used in the backup. For example, if a backup is made of a database named `products`, you can restore the data it contains to a database named `inventory`, use this option as shown here (omitting any other options that might be required):
	```
	$> ndb_restore --rewrite-database=product,inventory
	```
	The option can be employed multiple times in a single invocation of **ndb\_restore**. Thus it is possible to restore simultaneously from a database named `db1` to a database named `db2` and from a database named `db3` to one named `db4` using `--rewrite-database=db1,db2             --rewrite-database=db3,db4`. Other **ndb\_restore** options may be used between multiple occurrences of `--rewrite-database`.
	In the event of conflicts between multiple `--rewrite-database` options, the last `--rewrite-database` option used, reading from left to right, is the one that takes effect. For example, if `--rewrite-database=db1,db2             --rewrite-database=db1,db3` is used, only `--rewrite-database=db1,db3` is honored, and `--rewrite-database=db1,db2` is ignored. It is also possible to restore from multiple databases to a single database, so that `--rewrite-database=db1,db3             --rewrite-database=db2,db3` restores all tables and data from databases `db1` and `db2` into database `db3`.
	Important
	When restoring from multiple backup databases into a single target database using `--rewrite-database`, no check is made for collisions between table or other object names, and the order in which rows are restored is not guaranteed. This means that it is possible in such cases for rows to be overwritten and updates to be lost.
- `--skip-broken-objects`
	| Command-Line Format | `--skip-broken-objects` |
	| --- | --- |
	This option causes **ndb\_restore** to ignore corrupt tables while reading a native [`NDB`](mysql-cluster.md) backup, and to continue restoring any remaining tables (that are not also corrupted). Currently, the `--skip-broken-objects` option works only in the case of missing blob parts tables.
- `--skip-table-check`, `-s`
	| Command-Line Format | `--skip-table-check` |
	| --- | --- |
	It is possible to restore data without restoring table metadata. By default when doing this, **ndb\_restore** fails with an error if a mismatch is found between the table data and the table schema; this option overrides that behavior.
	Some of the restrictions on mismatches in column definitions when restoring data using **ndb\_restore** are relaxed; when one of these types of mismatches is encountered, **ndb\_restore** does not stop with an error as it did previously, but rather accepts the data and inserts it into the target table while issuing a warning to the user that this is being done. This behavior occurs whether or not either of the options `--skip-table-check` or `--promote-attributes` is in use. These differences in column definitions are of the following types:
	- Different `COLUMN_FORMAT` settings (`FIXED`, `DYNAMIC`, `DEFAULT`)
	- Different `STORAGE` settings (`MEMORY`, `DISK`)
	- Different default values
	- Different distribution key settings
- `--skip-unknown-objects`
	| Command-Line Format | `--skip-unknown-objects` |
	| --- | --- |
	This option causes **ndb\_restore** to ignore any schema objects it does not recognize while reading a native [`NDB`](mysql-cluster.md) backup. This can be used for restoring a backup made from a cluster running (for example) NDB 7.6 to a cluster running NDB Cluster 7.5.
- `--slice-id` = *`#`*
	| Command-Line Format | `--slice-id=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `1023` |
	When restoring by slices, this is the ID of the slice to restore. This option is always used together with `--num-slices`, and its value must be always less than that of `--num-slices`.
	For more information, see the description of the `--num-slices` elsewhere in this section.
- `--tab` = *`dir_name`*, `-T` *`dir_name`*
	| Command-Line Format | `--tab=path` |
	| --- | --- |
	| Type | Directory name |
	Causes `--print-data` to create dump files, one per table, each named ``*`tbl_name`*.txt``. It requires as its argument the path to the directory where the files should be saved; use `.` for the current directory.
- `--timestamp-printouts`
	| Command-Line Format | `--timestamp-printouts{=true\|false}` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Causes info, error, and debug log messages to be prefixed with timestamps.
	This option is disabled by default in NDB 7.5 and NDB 7.6. Set it explicitly to `true` to enable.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--verbose` = *`#`*
	| Command-Line Format | `--verbose=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Minimum Value | `0` |
	| Maximum Value | `255` |
	Sets the level for the verbosity of the output. The minimum is 0; the maximum is 255. The default value is 1.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

Typical options for this utility are shown here:

```
ndb_restore [-c connection_string] -n node_id -b backup_id \
      [-m] -r --backup-path=/path/to/backup/files
```

Normally, when restoring from an NDB Cluster backup, **ndb\_restore** requires at a minimum the `--nodeid` (short form: `-n`), `--backupid` (short form: `-b`), and `--backup-path` options. In addition, when **ndb\_restore** is used to restore any tables containing unique indexes, you must include `--disable-indexes` or `--rebuild-indexes`. (Bug #57782, Bug #11764893)

The `-c` option is used to specify a connection string which tells `ndb_restore` where to locate the cluster management server (see [Section 21.4.3.3, “NDB Cluster Connection Strings”](mysql-cluster-connection-strings.md)). If this option is not used, then **ndb\_restore** attempts to connect to a management server on `localhost:1186`. This utility acts as a cluster API node, and so requires a free connection “slot” to connect to the cluster management server. This means that there must be at least one `[api]` or `[mysqld]` section that can be used by it in the cluster `config.ini` file. It is a good idea to keep at least one empty `[api]` or `[mysqld]` section in `config.ini` that is not being used for a MySQL server or other application for this reason (see [Section 21.4.3.7, “Defining SQL and Other API Nodes in an NDB Cluster”](mysql-cluster-api-definition.md)).

You can verify that **ndb\_restore** is connected to the cluster by using the [`SHOW`](mysql-cluster-mgm-client-commands.md) command in the [**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md) management client. You can also accomplish this from a system shell, as shown here:

```
$> ndb_mgm -e "SHOW"
```

**Error reporting.** **ndb\_restore** reports both temporary and permanent errors. In the case of temporary errors, it may able to recover from them, and reports `Restore successful,           but encountered temporary error, please look at           configuration` in such cases.

Important

After using **ndb\_restore** to initialize an NDB Cluster for use in circular replication, binary logs on the SQL node acting as the replica are not automatically created, and you must cause them to be created manually. To cause the binary logs to be created, issue a [`SHOW TABLES`](show-tables.md) statement on that SQL node before running [`START           SLAVE`](start-slave.md). This is a known issue in NDB Cluster.
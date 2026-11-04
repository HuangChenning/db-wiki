---
title: "25.5.25 ndb_select_all — Print Rows from an NDB Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-select-all.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.25 ndb\_select\_all — Print Rows from an NDB Table

**ndb\_select\_all** prints all rows from an [`NDB`](mysql-cluster.md) table to `stdout`.

#### Usage

```
ndb_select_all -c connection_string tbl_name -d db_name [> file_name]
```

Options that can be used with **ndb\_select\_all** are shown in the following table. Additional descriptions follow the table.

**Table 25.46 Command-line options used with the program ndb\_select\_all**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | REMOVED: 8.0.31 |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 8.0) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --core-file                  ` | Write core file on error; used in debugging | REMOVED: 8.0.31 |
| `--database=name`,  `                  -d                 name  ` | Name of database in which table is found | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `--delimiter=char`,  `                  -D                 char  ` | Set column delimiter | (Supported in all NDB releases based on MySQL 8.0) |
| `--descending`,  `                  -z                  ` | Sort resultset in descending order (requires --order) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --disk                  ` | Print disk references (useful only for Disk Data tables having unindexed columns) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --gci                  ` | Include GCI in output | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --gci64                  ` | Include GCI and row epoch in output | (Supported in all NDB releases based on MySQL 8.0) |
| `--header[=value]`,  `                  -h                  ` | Print header (set to 0\|FALSE to disable headers in output) | (Supported in all NDB releases based on MySQL 8.0) |
| `--lock=#`,  `  -l                 #  ` | Lock type | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | REMOVED: 8.0.31 |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --nodata                  ` | Do not print table column data | (Supported in all NDB releases based on MySQL 8.0) |
| `--order=index`,  `  -o                 index  ` | Sort resultset according to index having this name | (Supported in all NDB releases based on MySQL 8.0) |
| `--parallelism=#`,  `                  -p                 #  ` | Degree of parallelism | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --rowid                  ` | Print row ID | (Supported in all NDB releases based on MySQL 8.0) |
| `--tupscan`,  `                  -t                  ` | Scan in tup order | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--useHexFormat`,  `                  -x                  ` | Output numbers in hexadecimal format | (Supported in all NDB releases based on MySQL 8.0) |
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
- ``--database=*`dbname`*``, `-d` *`dbname`*
	Name of the database in which the table is found. The default value is `TEST_DB`.
- `--descending`, `-z`
	Sorts the output in descending order. This option can be used only in conjunction with the `-o` (`--order`) option.
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
- ``--delimiter=*`character`*``, ``-D *`character`*``
	Causes the *`character`* to be used as a column delimiter. Only table data columns are separated by this delimiter.
	The default delimiter is the tab character.
- `--disk`
	Adds a disk reference column to the output. The column is nonempty only for Disk Data tables having nonindexed columns.
- `--gci`
	Adds a `GCI` column to the output showing the global checkpoint at which each row was last updated. See [Section 25.2, “NDB Cluster Overview”](mysql-cluster-overview.md), and [Section 25.6.3.2, “NDB Cluster Log Events”](mysql-cluster-log-events.md), for more information about checkpoints.
- `--gci64`
	Adds a `ROW$GCI64` column to the output showing the global checkpoint at which each row was last updated, as well as the number of the epoch in which this update occurred.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- ``--lock=*`lock_type`*``, ``-l *`lock_type`*``
	Employs a lock when reading the table. Possible values for *`lock_type`* are:
	- `0`: Read lock
	- `1`: Read lock with hold
	- `2`: Exclusive read lock
	There is no default value for this option.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--header=FALSE`
	Excludes column headers from the output.
- `--nodata`
	Causes any table data to be omitted.
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
- ``--order=*`index_name`*``, ``-o *`index_name`*``
	Orders the output according to the index named *`index_name`*.
	Note
	This is the name of an index, not of a column; the index must have been explicitly named when created.
- ``parallelism=*`#`*``, `-p` *`#`*
	Specifies the degree of parallelism.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--rowid`
	Adds a `ROWID` column providing information about the fragments in which rows are stored.
- `--tupscan`, `-t`
	Scan the table in the order of the tuples.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--useHexFormat` `-x`
	Causes all numeric values to be displayed in hexadecimal format. This does not affect the output of numerals contained in strings or datetime values.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

#### Sample Output

Output from a MySQL [`SELECT`](select.md) statement:

```
mysql> SELECT * FROM ctest1.fish;
+----+-----------+
| id | name      |
+----+-----------+
|  3 | shark     |
|  6 | puffer    |
|  2 | tuna      |
|  4 | manta ray |
|  5 | grouper   |
|  1 | guppy     |
+----+-----------+
6 rows in set (0.04 sec)
```

Output from the equivalent invocation of **ndb\_select\_all**:

```
$> ./ndb_select_all -c localhost fish -d ctest1
id      name
3       [shark]
6       [puffer]
2       [tuna]
4       [manta ray]
5       [grouper]
1       [guppy]
6 rows returned
```

All string values are enclosed by square brackets (`[`...`]`) in the output of **ndb\_select\_all**. For another example, consider the table created and populated as shown here:

```
CREATE TABLE dogs (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    breed VARCHAR(50) NOT NULL,
    PRIMARY KEY pk (id),
    KEY ix (name)
)
TABLESPACE ts STORAGE DISK
ENGINE=NDBCLUSTER;

INSERT INTO dogs VALUES
    ('', 'Lassie', 'collie'),
    ('', 'Scooby-Doo', 'Great Dane'),
    ('', 'Rin-Tin-Tin', 'Alsatian'),
    ('', 'Rosscoe', 'Mutt');
```

This demonstrates the use of several additional **ndb\_select\_all** options:

```
$> ./ndb_select_all -d ctest1 dogs -o ix -z --gci --disk
GCI     id name          breed        DISK_REF
834461  2  [Scooby-Doo]  [Great Dane] [ m_file_no: 0 m_page: 98 m_page_idx: 0 ]
834878  4  [Rosscoe]     [Mutt]       [ m_file_no: 0 m_page: 98 m_page_idx: 16 ]
834463  3  [Rin-Tin-Tin] [Alsatian]   [ m_file_no: 0 m_page: 34 m_page_idx: 0 ]
835657  1  [Lassie]      [Collie]     [ m_file_no: 0 m_page: 66 m_page_idx: 0 ]
4 rows returned
```
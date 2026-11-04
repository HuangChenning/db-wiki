---
title: "21.5.17 ndb_perror — Obtain NDB Error Message Information"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-perror.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.17 ndb\_perror — Obtain NDB Error Message Information

**ndb\_perror** shows information about an NDB error, given its error code. This includes the error message, the type of error, and whether the error is permanent or temporary. Added to the MySQL NDB Cluster distribution in NDB 7.6, it is intended as a drop-in replacement for [**perror**](perror.md) [`--ndb`](perror.md).

#### Usage

```
ndb_perror [options] error_code
```

**ndb\_perror** does not need to access a running NDB Cluster, or any nodes (including SQL nodes). To view information about a given NDB error, invoke the program, using the error code as an argument, like this:

```
$> ndb_perror 323
NDB error code 323: Invalid nodegroup id, nodegroup already existing: Permanent error: Application error
```

To display only the error message, invoke **ndb\_perror** with the `--silent` option (short form `-s`), as shown here:

```
$> ndb_perror -s 323
Invalid nodegroup id, nodegroup already existing: Permanent error: Application error
```

Like [**perror**](perror.md), **ndb\_perror** accepts multiple error codes:

```
$> ndb_perror 321 1001
NDB error code 321: Invalid nodegroup id: Permanent error: Application error
NDB error code 1001: Illegal connect string
```

Additional program options for **ndb\_perror** are described later in this section.

**ndb\_perror** replaces [**perror**](perror.md) `--ndb`, which is deprecated in NDB 7.6 and subject to removal in a future release of MySQL NDB Cluster. To make substitution easier in scripts and other applications that might depend on [**perror**](perror.md) for obtaining NDB error information, **ndb\_perror** supports its own “dummy” `--ndb` option, which does nothing.

The following table includes all options that are specific to the NDB Cluster program **ndb\_perror**. Additional descriptions follow the table.

**Table 21.36 Command-line options used with the program ndb\_perror**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 5.7) |
| `--help`,  `                  -?                  ` | Display help text | ADDED: NDB 7.6.4 |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb                  ` | For compatibility with applications depending on old versions of perror; does nothing | ADDED: NDB 7.6.4 |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `--silent`,  `                  -s                  ` | Show error message only | ADDED: NDB 7.6.4 |
| `--version`,  `                  -V                  ` | Print program version information and exit | ADDED: NDB 7.6.4 |
| `--verbose`,  `                  -v                  ` | Verbose output; disable with --silent | ADDED: NDB 7.6.4 |

#### Additional Options

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display program help text and exit.
- `--ndb`
	| Command-Line Format | `--ndb` |
	| --- | --- |
	For compatibility with applications depending on old versions of [**perror**](perror.md) that use that program's [`--ndb`](perror.md) option. The option when used with **ndb\_perror** does nothing, and is ignored by it.
- `--silent`, `-s`
	| Command-Line Format | `--silent` |
	| --- | --- |
	Show error message only.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Print program version information and exit.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose output; disable with `--silent`.
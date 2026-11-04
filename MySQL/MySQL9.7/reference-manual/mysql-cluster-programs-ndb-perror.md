---
title: "25.5.16 ndb_perror — Obtain NDB Error Message Information"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-programs-ndb-perror.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 25.5.16 ndb\_perror — Obtain NDB Error Message Information

**ndb\_perror** shows information about an NDB error, given its error code. This includes the error message, the type of error, and whether the error is permanent or temporary. This is intended as a drop-in replacement for [**perror**](perror.md) [`--ndb`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/perror.html#option_perror_ndb), which is no longer supported.

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

**ndb\_perror** replaces [**perror**](perror.md) `--ndb`, which is no longer supported by NDB Cluster. To make substitution easier in scripts and other applications that might depend on [**perror**](perror.md) for obtaining NDB error information, **ndb\_perror** supports its own “dummy” `--ndb` option, which does nothing.

The following table includes all options that are specific to the NDB Cluster program **ndb\_perror**. Additional descriptions follow the table.

#### Additional Options

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
- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display program help text and exit.
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
- `--ndb`
	| Command-Line Format | `--ndb` |
	| --- | --- |
	For compatibility with applications depending on old versions of [**perror**](perror.md) that use that program's [`--ndb`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/perror.html#option_perror_ndb) option. The option when used with **ndb\_perror** does nothing, and is ignored by it.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
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
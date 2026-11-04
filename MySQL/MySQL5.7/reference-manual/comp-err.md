---
title: "4.4.1 comp_err — Compile MySQL Error Message File"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/comp-err.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.4.1 comp\_err — Compile MySQL Error Message File

**comp\_err** creates the `errmsg.sys` file that is used by [**mysqld**](mysqld.md) to determine the error messages to display for different error codes. **comp\_err** normally is run automatically when MySQL is built. It compiles the `errmsg.sys` file from the text-format error information file located at `sql/share/errmsg-utf8.txt` in MySQL source distributions.

**comp\_err** also generates the `mysqld_error.h`, `mysqld_ername.h`, and `sql_state.h` header files.

For more information about how error messages are defined, see the [MySQL Internals Manual](https://dev.mysql.com/doc/internals/en).

Invoke **comp\_err** like this:

```
comp_err [options]
```

**comp\_err** supports the following options.

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Display a help message and exit.
- ``--charset=*`dir_name`*``, ``-C *`dir_name`*``
	| Command-Line Format | `--charset` |
	| --- | --- |
	| Type | String |
	| Default Value | `../share/charsets` |
	The character set directory. The default is `../sql/share/charsets`.
- ``--debug=*`debug_options`*``, ``-# *`debug_options`*``
	| Command-Line Format | `--debug=options` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:O,/tmp/comp_err.trace` |
	In debug builds, write a debugging log. A typical *`debug_options`* string is ``d:t:O,*`file_name`*``. The default is `d:t:O,/tmp/comp_err.trace`.
	For non-debug builds, this option is non-functional and causes the program to exit with an explanatory message.
	Note
	The short form of this option is `-#`, using a literal `#` character.
- `--debug-info`, `-T`
	| Command-Line Format | `--debug-info` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Print some debugging information when the program exits.
- ``--header-file=*`file_name`*``, ``-H *`file_name`*``
	| Command-Line Format | `--header-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `mysqld_error.h` |
	The name of the error header file. The default is `mysqld_error.h`.
- ``--in-file=*`file_name`*``, ``-F *`file_name`*``
	| Command-Line Format | `--in-file=path` |
	| --- | --- |
	| Type | File name |
	| Default Value | `[none]` |
	The name of the input file that defines error messages. The default is `../sql/share/errmsg-utf8.txt`.
- ``--name-file=*`file_name`*``, ``-N *`file_name`*``
	| Command-Line Format | `--name-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `mysqld_ername.h` |
	The name of the error name file. The default is `mysqld_ername.h`.
- ``--out-dir=*`dir_name`*``, ``-D *`dir_name`*``
	| Command-Line Format | `--out-dir=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `../share/` |
	The name of the output base directory. The default is `../sql/share/`.
- ``--out-file=*`file_name`*``, ``-O *`file_name`*``
	| Command-Line Format | `--out-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `errmsg.sys` |
	The name of the output file. The default is `errmsg.sys`.
- ``--state-file=*`file_name`*``, ``-S *`file_name`*``
	| Command-Line Format | `--state-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `sql_state.h` |
	The name for the SQLSTATE header file. The default is `sql_state.h`.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Display version information and exit.
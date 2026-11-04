---
title: "MySQL :: MySQL 26.10 Reference Manual :: 6.4.1 comp_err — Compile MySQL Error Message File"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/comp-err.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 6.4.1 comp\_err — Compile MySQL Error Message File

**comp\_err** creates the `errmsg.sys` file that is used by [**mysqld**](mysqld.md) to determine the error messages to display for different error codes. **comp\_err** normally is run automatically when MySQL is built. It compiles the `errmsg.sys` file from text-format error information in MySQL source distributions:

The error information comes from the `messages_to_error_log.txt` and `messages_to_clients.txt` files in the `share` directory.

For more information about defining error messages, see the comments within those files, along with the `errmsg_readme.txt` file.

**comp\_err** also generates the `mysqld_error.h`, `mysqld_ername.h`, and `mysqld_errmsg.h` header files.

Invoke **comp\_err** like this:

```svg
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
	Write a debugging log. A typical *`debug_options`* string is ``d:t:O,*`file_name`*``. The default is `d:t:O,/tmp/comp_err.trace`.
- `--debug-info`, `-T`
	| Command-Line Format | `--debug-info` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Print some debugging information when the program exits.
- ``--errmsg-file=*`file_name`*``, ``-H *`file_name`*``
	| Command-Line Format | `--errmsg-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `mysqld_errmsg.h` |
	The name of the error message file. The default is `mysqld_errmsg.h`.
- ``--header-file=*`file_name`*``, ``-H *`file_name`*``
	| Command-Line Format | `--header-file=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `mysqld_error.h` |
	The name of the error header file. The default is `mysqld_error.h`.
- ``--in-file-errlog=*`file_name`*``, ``-e *`file_name`*``
	| Command-Line Format | `--in-file-errlog` |
	| --- | --- |
	| Type | File name |
	| Default Value | `../share/messages_to_error_log.txt` |
	The name of the input file that defines error messages intended to be written to the error log. The default is `../share/messages_to_error_log.txt`.
- ``--in-file-toclient=*`file_name`*``, ``-c *`file_name`*``
	| Command-Line Format | `--in-file-toclient=path` |
	| --- | --- |
	| Type | File name |
	| Default Value | `../share/messages_to_clients.txt` |
	The name of the input file that defines error messages intended to be written to clients. The default is `../share/messages_to_clients.txt`.
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
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Display version information and exit.
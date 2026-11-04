---
title: "6.6.10 mysqldumpslow — Summarize Slow Query Log Files"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysqldumpslow.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.6.10 mysqldumpslow — Summarize Slow Query Log Files

The MySQL slow query log contains information about queries that take a long time to execute (see [Section 7.4.5, “The Slow Query Log”](slow-query-log.md)). **mysqldumpslow** parses MySQL slow query log files and summarizes their contents.

Normally, **mysqldumpslow** groups queries that are similar except for the particular values of number and string data values. It “abstracts” these values to `N` and `'S'` when displaying summary output. To modify value abstracting behavior, use the `-a` and `-n` options.

Invoke **mysqldumpslow** like this:

```
mysqldumpslow [options] [log_file ...]
```

Example output with no options given:

```
Reading mysql slow query log from /usr/local/mysql/data/mysqld80-slow.log
Count: 1  Time=4.32s (4s)  Lock=0.00s (0s)  Rows=0.0 (0), root[root]@localhost
 insert into t2 select * from t1

Count: 3  Time=2.53s (7s)  Lock=0.00s (0s)  Rows=0.0 (0), root[root]@localhost
 insert into t2 select * from t1 limit N

Count: 3  Time=2.13s (6s)  Lock=0.00s (0s)  Rows=0.0 (0), root[root]@localhost
 insert into t1 select * from t1
```

**mysqldumpslow** supports the following options.

**Table 6.24 mysqldumpslow Options**

| Option Name | Description |
| --- | --- |
| \-a | Do not abstract all numbers to N and strings to 'S' |
| \-n | Abstract numbers with at least the specified digits |
| \--debug | Write debugging information |
| \-g | Only consider statements that match the pattern |
| \--help | Display help message and exit |
| \-h | Host name of the server in the log file name |
| \-i | Name of the server instance |
| \-l | Do not subtract lock time from total time |
| \-r | Reverse the sort order |
| \-s | How to sort output |
| \-t | Display only first num queries |
| \--verbose | Verbose mode |

- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- `-a`
	Do not abstract all numbers to `N` and strings to `'S'`.
- `--debug`, `-d`
	| Command-Line Format | `--debug` |
	| --- | --- |
	Run in debug mode.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- ``-g *`pattern`*``
	| Type | String |
	| --- | --- |
	Consider only queries that match the (**grep** -style) pattern.
- ``-h *`host_name`*``
	| Type | String |
	| --- | --- |
	| Default Value | `*` |
	Host name of MySQL server for `*-slow.log` file name. The value can contain a wildcard. The default is `*` (match all).
- ``-i *`name`*``
	| Type | String |
	| --- | --- |
	Name of server instance (if using [**mysql.server**](mysql-server.md) startup script).
- `-l`
	Do not subtract lock time from total time.
- ``-n *`N`*``
	| Type | Numeric |
	| --- | --- |
	Abstract numbers with at least *`N`* digits within names.
- `-r`
	Reverse the sort order.
- ``-s *`sort_type`*``
	| Type | String |
	| --- | --- |
	| Default Value | `at` |
	How to sort the output. The value of *`sort_type`* should be chosen from the following list:
	- `t`, `at`: Sort by query time or average query time
	- `l`, `al`: Sort by lock time or average lock time
	- `r`, `ar`: Sort by rows sent or average rows sent
	- `c`: Sort by count
	By default, **mysqldumpslow** sorts by average query time (equivalent to `-s at`).
- ``-t *`N`*``
	| Type | Numeric |
	| --- | --- |
	Display only the first *`N`* queries in the output.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does.
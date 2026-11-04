---
title: "8.14.1 Accessing the Process List"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/processlist-access.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.14.1 Accessing the Process List

The following discussion enumerates the sources of process information, the privileges required to see process information, and describes the content of process list entries.

#### Sources of Process Information

Process information is available from these sources:

- The [`SHOW PROCESSLIST`](show-processlist.md) statement: [Section 13.7.5.29, “SHOW PROCESSLIST Statement”](show-processlist.md)
- The [**mysqladmin processlist**](mysqladmin.md) command: [Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md)
- The `INFORMATION_SCHEMA` [`PROCESSLIST`](information-schema-processlist-table.md) table: [Section 24.3.18, “The INFORMATION\_SCHEMA PROCESSLIST Table”](information-schema-processlist-table.md)
- The Performance Schema [`processlist`](performance-schema-processlist-table.md) table: [Section 25.12.16.3, “The processlist Table”](performance-schema-processlist-table.md)
- The Performance Schema [`threads`](performance-schema-threads-table.md) table columns with names having a prefix of `PROCESSLIST_`: [Section 25.12.16.4, “The threads Table”](performance-schema-threads-table.md)
- The `sys` schema [`processlist`](sys-processlist.md) and [`session`](sys-session.md) views: [Section 26.4.3.22, “The processlist and x$processlist Views”](sys-processlist.md), and [Section 26.4.3.33, “The session and x$session Views”](sys-session.md)

The [`threads`](performance-schema-threads-table.md) table compares to [`SHOW PROCESSLIST`](show-processlist.md), `INFORMATION_SCHEMA` [`PROCESSLIST`](information-schema-processlist-table.md), and [**mysqladmin processlist**](mysqladmin.md) as follows:

- Access to the [`threads`](performance-schema-threads-table.md) table does not require a mutex and has minimal impact on server performance. The other sources have negative performance consequences because they require a mutex.
	Note
	As of MySQL 5.7.39, an alternative implementation for [`SHOW PROCESSLIST`](show-processlist.md) is available based on the Performance Schema [`processlist`](performance-schema-processlist-table.md) table, which, like the [`threads`](performance-schema-threads-table.md) table, does not require a mutex and has better performance characteristics. For details, see [Section 25.12.16.3, “The processlist Table”](performance-schema-processlist-table.md).
- The [`threads`](performance-schema-threads-table.md) table displays background threads, which the other sources do not. It also provides additional information for each thread that the other sources do not, such as whether the thread is a foreground or background thread, and the location within the server associated with the thread. This means that the [`threads`](performance-schema-threads-table.md) table can be used to monitor thread activity the other sources cannot.
- You can enable or disable Performance Schema thread monitoring, as described in [Section 25.12.16.4, “The threads Table”](performance-schema-threads-table.md).

For these reasons, DBAs who perform server monitoring using one of the other thread information sources may wish to monitor using the [`threads`](performance-schema-threads-table.md) table instead.

The `sys` schema [`processlist`](sys-processlist.md) view presents information from the Performance Schema [`threads`](performance-schema-threads-table.md) table in a more accessible format. The `sys` schema [`session`](sys-session.md) view presents information about user sessions like the `sys` schema [`processlist`](sys-processlist.md) view, but with background processes filtered out.

#### Privileges Required to Access the Process List

For most sources of process information, if you have the [`PROCESS`](privileges-provided.md) privilege, you can see all threads, even those belonging to other users. Otherwise (without the [`PROCESS`](privileges-provided.md) privilege), nonanonymous users have access to information about their own threads but not threads for other users, and anonymous users have no access to thread information.

The Performance Schema [`threads`](performance-schema-threads-table.md) table also provides thread information, but table access uses a different privilege model. See [Section 25.12.16.4, “The threads Table”](performance-schema-threads-table.md).

#### Content of Process List Entries

Each process list entry contains several pieces of information. The following list describes them using the labels from [`SHOW PROCESSLIST`](show-processlist.md) output. Other process information sources use similar labels.

- `Id` is the connection identifier for the client associated with the thread.
- `User` and `Host` indicate the account associated with the thread.
- `db` is the default database for the thread, or `NULL` if none has been selected.
- `Command` and `State` indicate what the thread is doing.
	Most states correspond to very quick operations. If a thread stays in a given state for many seconds, there might be a problem that needs to be investigated.
	The following sections list the possible `Command` values, and `State` values grouped by category. The meaning for some of these values is self-evident. For others, additional description is provided.
	Note
	Applications that examine process list information should be aware that the commands and states are subject to change.
- `Time` indicates how long the thread has been in its current state. The thread's notion of the current time may be altered in some cases: The thread can change the time with [``SET               TIMESTAMP = *`value`*``](set-variable.md). For a replica SQL thread, the value is the number of seconds between the timestamp of the last replicated event and the real time of the replica host. See [Section 16.2.3, “Replication Threads”](replication-threads.md).
- `Info` indicates the statement the thread is executing, or `NULL` if it is executing no statement. For [`SHOW               PROCESSLIST`](show-processlist.md), this value contains only the first 100 characters of the statement. To see complete statements, use [`SHOW               FULL PROCESSLIST`](show-processlist.md) (or query a diffferent process information source).
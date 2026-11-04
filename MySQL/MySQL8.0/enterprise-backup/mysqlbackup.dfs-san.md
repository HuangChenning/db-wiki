---
title: "4.4 Making Backups with a Distributed File System (DFS) or Storage Access Network (SAN)"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.dfs-san.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

When system administrators attempt to set up MySQL and MySQL Enterprise Backup in an environment that uses a distributed file system (DFS) or a storage access network (SAN), the MySQL server, the server's data directory, MySQL Enterprise Backup, and the backup directory may end up existing on different physical servers. When that happens, the operations of **mysqlbackup** might be impacted. The operation most likely to be adversely affected is hot backup, the success of which depends on:

1. Each page of a data file is copied consistently, that is, all the bytes in the page correspond to the same LSN.
2. No copied page is older than the time that marks the beginning of the temporal duration the backup is supposed to cover.
3. The redo log is copied consistently, meaning a continuous segment of redo log is copied, and it includes all the changes from the beginning of the temporal period that the backup is to cover until the end of the backup operation. Each block of the copied redo log has to be consistent.

Condition 1 is easily achievable with most DFSs or SANs of reasonable performance. Condition 2 though can remain unfulfilled even when condition 1 has been satisfied: for example, **mysqlbackup** could copy all the pages of a tablespace correctly except for one page for which **mysqlbackup** has included an old version into the copy. If the LSN of that old version of the page is smaller than the LSN first seen by **mysqlbackup** at the beginning of the backup process, the resulting backup will be defective. This example shows that **mysqlbackup** may have problem performing a hot backup unless it can see the writes to the file system being executed in the correct order, that is, the order in which the server executed them.

Regarding condition 3, unlike data file pages, redo log blocks are written sequentially, which means condition 3 is easier to fulfill than conditions 1 and 2, especially when [using the redo log archiving feature](meb-redo-log-archiving.md) available on MySQL Server 8.0.17. However, if **mysqlbackup** reaches the highest LSN in the copied data file pages before encountering the end of the redo log, the backup fails. A failure occurs also if **mysqlbackup** reads a corrupted log block at any time during the copying of the redo log. Both these failures can occur if **mysqlbackup** does not see the same history of the file system states as the MySQL server does.

Therefore, to use **mysqlbackup** with a DFS or SAN, it is important to make sure that **mysqlbackup** sees all the writes to the file system in the same order as the MySQL server does. The condition is most likely to be satisfied when **mysqlbackup** and the MySQL server are running on the same server node, and it is unlikely to be always fulfilled when it is otherwise.
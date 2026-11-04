---
title: "8.12.1 System Factors"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/system-optimization.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.12.1 System Factors

Some system-level factors can affect performance in a major way:

- If you have enough RAM, you could remove all swap devices. Some operating systems use a swap device in some contexts even if you have free memory.
- Avoid external locking for [`MyISAM`](myisam-storage-engine.md) tables. The default is for external locking to be disabled. The [`--external-locking`](server-options.md) and [`--skip-external-locking`](server-options.md) options explicitly enable and disable external locking.
	Disabling external locking does not affect MySQL's functionality as long as you run only one server. Just remember to take down the server (or lock and flush the relevant tables) before you run [**myisamchk**](myisamchk.md). On some systems it is mandatory to disable external locking because it does not work, anyway.
	The only case in which you cannot disable external locking is when you run multiple MySQL *servers* (not clients) on the same data, or if you run [**myisamchk**](myisamchk.md) to check (not repair) a table without telling the server to flush and lock the tables first. Note that using multiple MySQL servers to access the same data concurrently is generally *not* recommended, except when using NDB Cluster.
	The [`LOCK TABLES`](lock-tables.md) and [`UNLOCK             TABLES`](lock-tables.md) statements use internal locking, so you can use them even if external locking is disabled.
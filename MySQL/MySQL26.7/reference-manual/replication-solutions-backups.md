---
title: "MySQL :: MySQL 26.7 Reference Manual :: 19.4.1 Using Replication for Backups"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/replication-solutions-backups.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 19.4.1 Using Replication for Backups

To use replication as a backup solution, replicate data from the source to a replica, and then back up the replica. The replica can be paused and shut down without affecting the running operation of the source, so you can produce an effective snapshot of “live” data that would otherwise require the source to be shut down.

How you back up a database depends on its size and whether you are backing up only the data, or the data and the replica state so that you can rebuild the replica in the event of failure. There are therefore two choices:

- If you are using replication as a solution to enable you to back up the data on the source, and the size of your database is not too large, the [**mysqldump**](mysqldump.md) tool may be suitable. See [Section 19.4.1.1, “Backing Up a Replica Using mysqldump”](replication-solutions-backups-mysqldump.md).
- For larger databases, where [**mysqldump**](mysqldump.md) would be impractical or inefficient, you can back up the raw data files instead. Using the raw data files option also means that you can back up the binary and relay logs that make it possible to re-create the replica in the event of a replica failure. For more information, see [Section 19.4.1.2, “Backing Up Raw Data from a Replica”](replication-solutions-backups-rawdata.md).

Another backup strategy, which can be used for either source or replica servers, is to put the server in a read-only state. The backup is performed against the read-only server, which then is changed back to its usual read/write operational status. See [Section 19.4.1.3, “Backing Up a Source or Replica by Making It Read Only”](replication-solutions-backups-read-only.md).
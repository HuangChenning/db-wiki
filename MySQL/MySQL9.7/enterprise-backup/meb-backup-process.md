---
title: "1.4 The Backup Process"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-backup-process.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

The following is a very brief outline of the steps performed by **mysqlbackup** when it creates a backup. It does not include every single step taken by **mysqlbackup**, and the description only represents a very general case—the process can look quite different, depending on the backup options you use (especially with some of the options described in [Section 20.10, “Performance / Scalability / Capacity Options”](backup-capacity-options.md) and [Section 20.16, “Options for Special Backup Types”](backup-special-options.md)).

In general, this is what happens when you run a backup operation with **mysqlbackup**:

1. The InnoDB data files, redo log, binary log, and relay log files (except for the log files currently in use) are being copied into the backup, while the database server operates as usual.
	The data and the structures of the InnoDB tables might have changed during this period; so, some of the following steps are for making sure those changes are captured in the backup.
2. A [backup lock](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/lock-instance-for-backup.html) is applied on the server instance. It blocks DDL operations (except for those on user-created temporary tables), but not DML operations (except for those not captured by the binary log, like administrative changes to the database) on InnoDB tables. Most read and write activities on the database are still allowed. With this lock applied, **mysqlbackup** scans for InnoDB tables that have been modified by DDL operations since step 1, and make changes to the backup accordingly.
3. A [``FLUSH           TABLES *`tbl_name [, tbl_name]`* ...           WITH READ LOCK``](https://docs.oracle.com/cd/E17952_01/mysql-enterprise-backup-9.7-en/flush-tables-with-read-lock-with-list) statement is applied on all non-InnoDB tables ( only on non-InnoDB tables that are to be included in the backup ), after which any non-InnoDB tables relevant to the backup are copied.
	This step is skipped if no user-created non-InnoDB tables exist on the database.
4. A brief blocking of logging activities on the server is applied, for **mysqlbackup** to collect logging-related information like the current InnoDB LSN, binary log position, GTID, replication source or replica status, and so on.
5. The read lock on the non-InnoDB tables is released.
6. Using information from step 4 above, the relevant portion of the binary or relay log file currently in use is copied. This ensures that all recent changes to the InnoDB tables since step 1 are captured in the backup, so they can be applied later to the [raw backup](glossary.md) data to bring the restored server to a consistent state.
7. The [backup lock](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/lock-instance-for-backup.html) on the server instance is released. The database now returns to its normal operations.
8. The redo log files not yet copied before, as well as all the metadata files for the backup, are copied or created.
9. The backup operation is completed, and **mysqlbackup** returns success.
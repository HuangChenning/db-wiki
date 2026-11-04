---
title: "8.2 Backing up and Restoring a Replica Database"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/advanced.replica-backup-restore.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

To backup a replica database, add the [`--replica-info`](backup-special-options.md) option to your backup command.

To restore the backup on a replica server, follow the same steps outlined in [Section 8.1, “Setting Up a New replica”](advanced.replica.md).

**Temporary tables on a replica.** MySQL Enterprise Backup does not include temporary tables inside a backup. As a result, for a replica server in a statement-based replication (SBR) or a mixed-based replication setup (see [Replication Formats](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/replication-formats.html) for details), any temporary tables still open at the end of the backup process will be missing in the restored replica server, making the replication state of the replica inconsistent, and any subsequent replicated statements that refer to the temporary tables will fail. To avoid the issue, after the hot backup phase of a replica backup in which **mysqlbackup** copies all the InnoDB tables, it enters into a loop, in which the following happens:

1. **mysqlbackup** waits until all temporary tables have been closed by the replication SQL thread. **mysqlbackup** tells if that is the case by checking if the variable [`Replica_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) is 0.
2. After [`Replica_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) is detected to be 0, **mysqlbackup** stops the replication SQL thread to prevent more changes to the tables on the replica.
3. To avoid the unexpected consequence by a race condition, after the replication SQL thread has been stopped, **mysqlbackup** checks once more if [`Replica_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) is still 0
	- If it is, **mysqlbackup** exits the loop and finishes the backup by asserting a read lock on all the non-InnoDB tables and copy them.
	- If it is not, new temporary tables have just been created and opened on the replica. **mysqlbackup** then restarts the replication SQL thread, so more updates can be made on the replica servers. **mysqlbackup** then goes back to step 1 of this loop

Besides the exit condition described in step (3) above (which is, there really are no more open temporary tables and **mysqlbackup** is ready to complete the backup), **mysqlbackup** will time out after staying in the above loop for too long to wait for all temporary tables to be closed. The duration **mysqlbackup** waits until it times out is specified by the [`--safe-replica-backup-timeout`](backup-special-options.md) option.

In addition, **mysqlbackup** also runs an initial check at the beginning of a replica backup to see if [`Replica_open_temp_tables`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/server-status-variables.html#statvar_Replica_open_temp_tables) becomes 0 within the duration set by [`--safe-replica-backup-timeout`](backup-special-options.md). See description for [`--safe-replica-backup-timeout`](backup-special-options.md) on details about the check.

Even though the issue described above with temporary tables does not exist for a row-based replication (RBR) setup (for which temporary tables are not replicated onto the replica), any replica backups still enter the same loop as described above, because the mode of replication could potentially be switched from RBR to statement-based replication (SBR) or mixed-mode replication at any time. User who are certain that SBR is not occurring for the replica can set [`--safe-replica-backup-timeout=0`](backup-special-options.md), which will prevent **mysqlbackup** from entering the above-mentioned loop.

Note

See the [limitation](bugs.backup.md) that applies when backing up a replica in [Appendix B, *Limitations of MySQL Enterprise Backup*](bugs.backup.md).
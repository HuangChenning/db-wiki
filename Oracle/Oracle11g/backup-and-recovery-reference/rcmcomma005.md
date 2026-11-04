---
title: Summary of RMAN Commands
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma005.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Table 1-2 provides a functional summary of RMAN commands that you can execute at the RMAN prompt, within a `RUN` command, or both. All commands from previous RMAN releases work with the current release, although some commands and options are now deprecated (see [Appendix A, "Deprecated RMAN Syntax"](obs_comm.md)). For command-line options for the RMAN client, refer to `RMAN`.

Table 1-2 Recovery Manager Commands

| Command | Purpose |
| --- | --- |
| `@ (at sign)` | Run a command file. |
| `@@ (double at sign)` | Run a command file in the same directory as another command file that is currently running. The `@@` command differs from the `@` command only when run from within a command file. |
| `ADVISE FAILURE` | Display repair options. |
| `ALLOCATE CHANNEL` | Establish a channel, which is a connection between RMAN and a database instance. |
| `ALLOCATE CHANNEL FOR MAINTENANCE` | Allocate a channel in preparation for issuing maintenance commands such as `DELETE`. |
| `ALTER DATABASE` | Mount or open a database. |
| `BACKUP` | Back up database files, copies of database files, archived logs, or backup sets. |
| `CATALOG` | Add information about file copies and user-managed backups to the repository. |
| `CHANGE` | Mark a backup piece, image copy, or archived redo log as having the status `UNAVAILABLE` or `AVAILABLE`; remove the repository record for a backup or copy; override the retention policy for a backup or copy; update the recovery catalog with the `DB_UNIQUE_NAME` for the target database. |
| `CONFIGURE` | Configure persistent RMAN settings. These settings apply to all RMAN sessions until explicitly changed or disabled. |
| `CONNECT` | Establish a connection between RMAN and a target, auxiliary, or recovery catalog database. |
| `CONVERT` | Convert data file formats for transporting tablespaces and databases across platforms. |
| `CREATE CATALOG` | Create the schema for the recovery catalog. |
| `CREATE SCRIPT` | Create a stored script and store it in the recovery catalog. |
| `CROSSCHECK` | Determine whether files managed by RMAN, such as archived logs, data file copies, and backup pieces, still exist on disk or tape. |
| `DELETE` | Delete backups and copies, remove references to them from the recovery catalog, and update their control file records to status `DELETED`. |
| `DELETE SCRIPT` | Delete a stored script from the recovery catalog. |
| `DROP CATALOG` | Remove the schema from the recovery catalog. |
| `DROP DATABASE` | Delete the target database from disk and unregisters it. |
| `DUPLICATE` | Use backups of the target database to create a duplicate database that you can use for testing purposes or to create a standby database. |
| `EXECUTE SCRIPT` | Run an RMAN stored script. |
| `EXIT` | Quit the RMAN executable. |
| `FLASHBACK DATABASE` | Return the database to its state at a previous time or SCN. |
| `GRANT` | Grant privileges to a recovery catalog user. |
| `HOST` | Invoke an operating system command-line subshell from within RMAN or run a specific operating system command. |
| `IMPORT CATALOG` | Imports the metadata from one recovery catalog into a different recovery catalog. |
| `LIST` | Produce a detailed listing of backup sets or copies. |
| `PRINT SCRIPT` | Display a stored script. |
| `QUIT` | Exit the RMAN executable. |
| `RECOVER` | Apply redo log files and incremental backups to data files or data blocks restored from backup or dataflow copies, to update them to a specified time. |
| `REGISTER DATABASE` | Register the target database in the recovery catalog. |
| `RELEASE CHANNEL` | Release a channel that was allocated with an `ALLOCATE CHANNEL` command or `ALLOCATE CHANNEL FOR MAINTENANCE` command. |
| `REPAIR FAILURE` | Repair one or more failures recorded in the automated diagnostic repository. |
| `REPLACE SCRIPT` | Replace an existing script stored in the recovery catalog. If the script does not exist, then `REPLACE` `SCRIPT` creates it. |
| `REPORT` | Perform detailed analyses of the content of the recovery catalog. |
| `RESET DATABASE` | Inform RMAN that the SQL statement `ALTER DATABASE OPEN RESETLOGS` has been executed and that a new incarnation of the target database has been created, or reset the target database to a prior incarnation. |
| `RESTORE` | Restore files from backup sets or from disk copies to the default or a new location. |
| `RESYNC CATALOG` | Perform a full resynchronization, which creates a snapshot control file and then copies any new or changed information from that snapshot control file to the recovery catalog. |
| `REVOKE` | Revoke privileges from a recovery catalog user. |
| `RMAN` | Start RMAN from the operating system command line. |
| `RUN` | Execute a sequence of one or more RMAN commands, which are one or more statements executed within the braces of `RUN`. |
| `SEND` | Send a vendor-specific quoted string to one or more specific channels. |
| `SET` | Set the value of various attributes that affect RMAN behavior for the duration of a RUN block or a session. |
| `SHOW` | Display the current `CONFIGURE` settings. |
| `SHUTDOWN` | Shut down the target database. This command is equivalent to the SQL\*Plus `SHUTDOWN` command. |
| `SPOOL` | Write RMAN output to a log file. |
| `SQL` | Execute a SQL statement from within Recovery Manager. |
| `STARTUP` | Start up the target database. This command is equivalent to the SQL\*Plus `STARTUP` command. |
| `SWITCH` | Specify that a data file copy is now the current data file, that is, the data file pointed to by the control file. This command is equivalent to the SQL statement `ALTER DATABASE RENAME FILE` as it applies to data files. |
| `TRANSPORT TABLESPACE` | Create transportable tablespace sets from backup for one or more tablespaces. |
| `UNREGISTER` | Unregister a database from the recovery catalog. |
| `UPGRADE CATALOG` | Upgrade the recovery catalog schema from an older version to the version required by the RMAN executable. |
| `VALIDATE` | Examine a backup set and report whether its data is intact. RMAN scans all of the backup pieces in the specified backup sets and looks at the checksums to verify that the contents can be successfully restored. |
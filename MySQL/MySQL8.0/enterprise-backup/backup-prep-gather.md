---
title: "4.1.1 Collect Database Information"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-prep-gather.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.1.1 Collect Database Information

Before backing up a particular database server for the first time, gather some information and use it to make some planning decisions, as outlined in the following table.

**Table 4.1 Information Needed to Back Up a Database**

| Information to Gather | Where to Find It | How to Use It |
| --- | --- | --- |
| Path to MySQL configuration file | Default system locations, hardcoded application default locations, or from the [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-file) option in the **mysqld** startup script. | The preferred way to convey database configuration information to **mysqlbackup** is to use the [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-file) option. When connection and data layout information is available from the configuration file, you no longer need to supply separately most of the information listed below. |
| MySQL port | MySQL configuration file or **mysqld** startup script. | Used to connect to the database instance during backup operations. Specified via the `--port` option of **mysqlbackup**. The specification is not needed if the information is available from the MySQL configuration file. |
| Path to MySQL data directory | MySQL configuration file or **mysqld** startup script. | Used to retrieve files from the database instance during backup operations, and to copy files back to the database instance during restore operations. Automatically retrieved from database connection. |
| ID and password of privileged MySQL user | You record this during installation of your own databases, or get it from the DBA when backing up databases you do not own. | Specified via the `--password` option of the **mysqlbackup**. Prompted at the terminal if the `--password` option is present without the password argument. |
| Path under which to store backup data or metadata, temporarily or permanently | You choose this. See [Section 4.1.3, “Designate a Location for the Backup Directory”](backup-prep-storage.md) for details. | In general, this directory has to be empty for **mysqlbackup** to write data into it. |
| Owner and permission information for backed-up files (for Linux, Unix, and OS X systems) | In the MySQL data directory. | If you perform the backup and restore using a different OS user than the one who runs the server, this information might become important. See [Section 4.2.1, “OS User for Running mysqlbackup”](mysqlbackup-os-user.md) for details. |
| *For release 8.0.29 and before:* Size of InnoDB redo log files | Calculated from the values of the [`innodb_log_file_size`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_log_file_size) and [`innodb_log_files_in_group`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_log_files_in_group) configuration variables (both system variables are deprecated since release 8.0.30). Use the technique explained for the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option. | Only needed if you perform incremental backups using the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option rather than the [`--incremental`](backup-incremental-options.md) option. The size of the InnoDB redo log and the rate of generation for redo data dictate how often you must perform incremental backups. |
| *For release 8.0.29 and before:* Rate at which redo data is generated | Calculated from the values of the InnoDB [logical sequence number](glossary.md) at different points in time. Use the technique explained in [Creating Incremental Backups Using Only the Redo Log](mysqlbackup.incremental.md). | Only needed if you perform incremental backups using the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option rather than the [`--incremental`](backup-incremental-options.md) option. The size of the InnoDB redo log and the rate of generation for redo data dictate how often you must perform incremental backups. |
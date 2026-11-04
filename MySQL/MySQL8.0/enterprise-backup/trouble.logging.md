---
title: "17.3 Using the MySQL Enterprise Backup Logs"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/trouble.logging.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

Besides the message output of MySQL Enterprise Backup to the `stderr` stream and the log file, progress and history of each backup are also logged into the `mysql.backup_progress` and `mysql.backup_history` tables on the backed-up servers (to skip updating the two tables, use the [`--no-history-logging`](backup-metadata-options.md) option with the backup command).

### backup\_progress Table

Each row in the `backup_progress` table records a state change or message from a running backup job. The `backup_progress` table has the following columns:

```
mysql> DESCRIBE mysql.backup_progress;
+---------------+---------------+------+-----+----------------------+--------------------------------------------------+
| Field         | Type          | Null | Key | Default              | Extra                                            |
+---------------+---------------+------+-----+----------------------+--------------------------------------------------+
| id            | int           | NO   | PRI | NULL                 | auto_increment                                   |
| backup_id     | bigint        | NO   | MUL | NULL                 |                                                  |
| tool_name     | varchar(4096) | NO   |     | NULL                 |                                                  |
| error_code    | int           | NO   |     | NULL                 |                                                  |
| error_message | varchar(4096) | NO   |     | NULL                 |                                                  |
| current_time  | timestamp(3)  | NO   |     | CURRENT_TIMESTAMP(3) | DEFAULT_GENERATED on update CURRENT_TIMESTAMP(3) |
| current_state | varchar(200)  | NO   |     | NULL                 |                                                  |
+---------------+---------------+------+-----+----------------------+--------------------------------------------------+
7 rows in set (0.00 sec)
```

*For MySQL Enterprise Backup 8.0.19 and later:* The `backup_progress` table is in InnoDB format.

*For MySQL Enterprise Backup 8.0.18 and earlier:* The `backup_progress` table is in CSV format. You can query the table with the **mysql** client, or parse the corresponding `.CSV` file with an application or script.

Here are some ways to make use of the information in the `backup_progress` table:

- Use the `backup_id` value to query all the information for different stages of a single backup operation, and to find the corresponding row in the `backup_history` table for the same backup (the row is written to the `backup_history` table only after the backup is finished).
- Check the `tool_name` column for the full **mysqlbackup** command that triggered the backup, including all the options used.
- Use the `error_code` and `error_message` values to track any errors that have occurred, and to see if the backup operation should be terminated because of any serious errors.
- Use the `current_time` and `current_state` values to track the progress of the operation. They also allow you to measure how long each stage of the backup takes, which helps you plan for your future backups.

### backup\_history Table

Each row in the `backup_history` table records the details of one completed backup produced by a **mysqlbackup** command. The `backup_history` table has the following columns:

```
mysql> mysql> DESCRIBE mysql.backup_history;
+---------------------------+---------------+------+-----+---------------------+-------+
| Field                     | Type          | Null | Key | Default             | Extra |
+---------------------------+---------------+------+-----+---------------------+-------+
| backup_id                 | bigint(20)    | NO   | PRI | NULL                |       |
| tool_name                 | varchar(4096) | NO   |     | NULL                |       |
| start_time                | timestamp     | NO   |     | 0000-00-00 00:00:00 |       |
| end_time                  | timestamp     | NO   |     | 0000-00-00 00:00:00 |       |
| binlog_pos                | bigint(20)    | NO   |     | NULL                |       |
| binlog_file               | varchar(255)  | NO   |     | NULL                |       |
| compression_level         | int(11)       | NO   |     | NULL                |       |
| engines                   | varchar(100)  | NO   |     | NULL                |       |
| innodb_data_file_path     | varchar(2048) | NO   |     | NULL                |       |
| start_lsn                 | bigint(20)    | NO   |     | NULL                |       |
| end_lsn                   | bigint(20)    | NO   |     | NULL                |       |
| backup_type               | varchar(50)   | NO   |     | NULL                |       |
| backup_format             | varchar(50)   | NO   |     | NULL                |       |
| mysql_data_dir            | varchar(2048) | NO   |     | NULL                |       |
| innodb_data_home_dir      | varchar(2048) | NO   |     | NULL                |       |
| innodb_log_group_home_dir | varchar(2048) | NO   |     | NULL                |       |
| backup_destination        | varchar(4096) | NO   |     | NULL                |       |
| lock_time                 | double(7,3)   | NO   |     | NULL                |       |
| exit_state                | varchar(10)   | NO   |     | NULL                |       |
| last_error                | varchar(4096) | NO   |     | NULL                |       |
| last_error_code           | int(11)       | NO   |     | NULL                |       |
| start_time_utc            | bigint(20)    | NO   |     | NULL                |       |
| end_time_utc              | bigint(20)    | NO   |     | NULL                |       |
| consistency_time_utc      | bigint(20)    | NO   |     | NULL                |       |
| meb_version               | varchar(20)   | NO   |     | 0.0.0               |       |
| server_uuid               | varchar(36)   | NO   |     | NULL                |       |
+---------------------------+---------------+------+-----+---------------------+-------+
26 rows in set (0.01 sec)
```

Warning

Because a successful backup is always recorded as such in the `backup_history` table, a failure in the [`apply-log`](backup-commands-update.md) phase of a [`backup-and-apply-log`](backup-commands-backup.md) command is not reflected in the `backup_history` table. It is always important to check the output of **mysqlbackup** to see if an operation is completed fully without an error.

Here is information on some columns of the `backup_history` table, and some ways to make use of the information:

- The `tool_name` column records the full **mysqlbackup** command that triggered the backup, including all the options used.
- You can use the `end_lsn` value of the latest backup as the starting LSN value for the next incremental backup by specifying it with the [`--start-lsn`](backup-incremental-options.md) option. (An alternative to specifying the start LSN value for an incremental backup is to use the [`--incremental-base`](backup-incremental-options.md) option).
- The `binlog_pos` column gives the position of the binary log up to where log events have been covered by the backup. Because the `backup_history` table used to be in the CSV format, which cannot register `NULL` values directly, if binary logging is not enabled, a value of `-1` is entered into the column; the same applies to other columns for the logging of `NULL` values.
- The value for `backup_type` is one of `FULL`, `PARTIAL`, `DIFFERENTIAL`, `INCREMENTAL` or `TTS`.
- The value for `backup_format` is one of `IMAGE` (for single-file backups) or `DIRECTORY` (for directory backups).
- Use the values that show the backup's settings such as `mysql_data_dir`, `innodb_data_home_dir`, and `backup_destination` to confirm that the backups are using the right source and destination directories.
- The value for `exit_state` is either `SUCCESS` or `FAILURE`. If the `exit_state` is `SUCCESS` and `last_error` is `'NO_ERROR'`, the backup operation has been successful; when it is not the case, see `last_error` and `last_error_code` for the latest error of the operation. To retrieve the full list of errors for that backup operation, go to the `backup_progress` table.
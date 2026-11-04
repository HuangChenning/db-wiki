---
title: "20.12 Progress Report Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-progress-report-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

There are two options for controlling the progress reporting function of **mysqlbackup**: `--show-progress` and `--progress-interval`:

- `--show-progress` `[={stderr|stdout|file:FILENAME|fifo:FIFONAME|table|variable}]`
	| Command-Line Format | `--show-progress[=destinations]` |
	| --- | --- |
	| Type | Enumeration |
	| Valid Values | `stderr`  `stdout`  `file:FILENAME`  `fifo:FIFONAME`  `table`  `variable` |
	The option instructs **mysqlbackup** to periodically output short progress reports known as progress indicators on its operation.
	The argument of the option controls the destination to which the progress indicators are sent:
	- `stderr`: Progress indicators are sent to the standard error stream. The report is embedded in a time-stamped **mysqlbackup** INFO message. For example:
		```
		130607 12:22:38 mysqlbackup: INFO: Progress: 191 of 191 MB; state: Completed
		```
	- `stdout`: Progress indicators are sent to the standard output stream. A single newline character is printed after each progress indicator.
	- `file:FILENAME`: Progress indicators are sent to a file. Each new progress report overwrites the file, and the file contains the most recent progress indicator followed by a single newline character.
	- `fifo:FIFONAME`: Progress indicators are sent to a file system FIFO. A single newline character is printed after each progress indicator.
		Warning
		If there is no process reading the FIFO, the **mysqlbackup** process hangs at the end of the execution.
	- `table`: Progress indicators are sent to the `mysql.backup_progress` table. This requires a connection to the MySQL server, and therefore, only works when backing up a running MySQL instance. **mysqlbackup** first adds one row of the progress report to the `mysql.backup_progress` table, and then updates the row afterwards with the latest progress indicator. The progress indicator is stored in the `current_status` column of the table.
	- `variable`: Progress indicators are sent to the system variable `backup_progress`.
		Warning
		The system variable `backup_progress` is not yet defined for the MySQL Server. Users need to create their own plugin to define the variable. See [The MySQL Plugin API](https://dev.mysql.com/doc/extending-mysql/9.7/en/plugin-api.html) for more information on user plugins.
	When there is no argument specified for `--show-progress`, progress indicators are sent to `stderr`.
	Progress can be reported to multiple destinations by specifying the `--show-progress` option several times on the command line. For example the following command line reports progress of the backup command to `stderr` and to a file called `meb_output`:
	```
	mysqlbackup --show-progress --show-progress=file:meb_output --backup-dir=/full-backup
	            backup
	```
	The progress indicators are short strings that indicate how far the execution of a **mysqlbackup** operation has progressed. A progress indicator consists of one or more meters that measure the progress of the operation. For example:
	```
	Progress: 100 of 1450 MB; state: Copying .ibd files
	```
	This shows that 100 megabytes of a total of 1450 megabytes have been copied or processed so far, and **mysqlbackup** is currently copying InnoDB data files (`.ibd` files).
	The progress indicator string begins with `Progress:`, followed by one or more meters measuring the progress. If multiple meters are present, they are separated by semicolons. The different types of meters include:
	- Total data meter: It is always the first meter in the progress indicator. It is in the format of:
		```
		DATA of TOTAL UNIT
		```
		*DATA* and *TOTAL* are unsigned decimal integers, and *UNIT* is either MB (megabytes), KB (kilobytes), or bytes (1MB=1024KB and 1KB=1024 bytes).
		The total data meter has two slightly different meanings depending on the **mysqlbackup** operation:
		- The amount of data copied or processed and the total amount of data to be copied or processed by the **mysqlbackup** operation. For example:
			```
			Progress: 200 of 1450 MB
			```
			When the operation is for, e.g., [`backup`](backup-commands-backup.md), the indicator means 200MB is copied of 1450MB. But when the operation is for, e.g.,
			                    [`                     validate`](backup-commands-validate.md) or [`incremental`](backup-incremental-options.md), it means 200MB is processed out of 1450MB.
		- Total amount of data copied or processed and an estimate for the total that will be copied by the end of the operation. The estimated total is updated as per the data on the server, as the execution of the command progresses.
			For some operations such as [`backup`](backup-commands-backup.md), it is not possible to know exactly at the start of the execution how much data will be copied or processed. Therefore, the total data meter shows the estimated amount of the total data for a backup. The estimate is updated during the execution of the command. For example:
			```
			Progress: 200 of 1450 MB
			```
			is followed by:
			```
			Progress: 200 of 1550 MB
			```
			when 100MB of data is added on the server.
			If the operation is successful, the final progress indicator shows the actual amount of data copied at the end of the operation.
	- Compression meter: It indicates the sliding average of the compression ratio, which is defined for each block of data that is compressed as `(orig_size -                 compressed_size) / orig_size`. For example:
		```
		compression: 40%
		```
		This means that after compression, the data takes 40% less space (calculated as an average over the last 10 data blocks).
		The compression meter is included in the progress indicator if the [`--compress`](backup-compression-options.md) option is enabled for the **mysqlbackup** operation. The value of the compression meter is undefined until at least 10 data blocks have been compressed. The undefined meter value is denoted by the '-' in the meter:
		```
		compression: -
		```
	- State meter: It is a short description of the major step the command is currently executing. For example:
		```
		state: Copying InnoDB data
		```
		```
		state: Waiting for locks
		```
		```
		state: Copying system tablespace
		```
		```
		state: Copying .ibd files
		```
		```
		state: Copying non-InnoDB data
		```
		```
		state: Completed
		```
	Here are some examples of progress indicators with different meters:
	```
	Progress: 300 of 1540 MB; state: Waiting for locks
	```
	```
	Progress: 400 of 1450 MB; state: Copying InnoDB data: compression: 30%
	```
	The exact set of meters included in the progress indicator depends on the command and the options used for it.
- `--progress-interval` = *`SECONDS`*
	| Command-Line Format | `--progress-interval=SECONDS` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `2` |
	| Minimum Value | `1` |
	| Maximum Value | `100000` |
	| Unit | second |
	Interval between progress reports in seconds. Default value is two seconds. The shortest interval is 1 second and the longest allowed interval is 100000 seconds.
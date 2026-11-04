---
title: "20.6 Compression Options"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-compression-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

For an overview on backup compression, see [Section 4.3.4, “Making a Compressed Backup”](backup.compressed.md).

- `--compress`
	Create backup in compressed format. For a regular backup, among all the storage engines supported by MySQL, only data files of the InnoDB format are compressed, and they bear the `.ibz` extension after the compression. Similarly, for a single-image backup, only data files of the InnoDB format inside the backup image are compressed. The binary log and relay log files are compressed and saved with the `.bz` extension when being included in a compressed backup.
	You cannot use the `--compress` option together with the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option.
	Default: compression is disabled.
- `--compress-method` = *`ALGORITHM`*
	| Command-Line Format | `--compress-method=ALGORITHM` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `lz4` |
	| Valid Values | `zlib`  `lz4`  `lzma`  `punch-hole`  `none` |
	Specifies the algorithm for backup compression, or enables support for InnoDB [transparent page compression](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-page-compression.html). The supported arguments for the option and the algorithms they represent are:
	- `lz4`: LZ4 r109. Out of the three compression algorithms that are supported, this is the most efficient one, typically taking the shortest backup and restore times with the lowest CPU cost. See [lz4—Extremely Fast Compression algorithm](http://code.google.com/p/lz4/) for more details, including a comparison with other compression algorithms.
	- `lzma`: LZMA 9.20. Out of the three supported compression algorithms, this typically provides the highest compression ratio; but it is also far more expensive in terms of CPU cost than the other two options. Thus we do not recommend this for active systems, but only for off-hour or inactive database servers, or where I/O rates are extremely low.
	- `zlib`: ZLIB v1.2.3. This is in between the other two supported compression algorithms in terms of both speed and compression ratio. ZLIB was the only compression algorithm available for MySQL Enterprise Backup versions prior to 3.10.
	- `punch-hole`: ( Enables support for [transparent page compression](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-page-compression.html) for InnoDB tables for directory backups, which means that when the target platform for the **mysqlbackup** backup or restore operation supports hole punching, **mysqlbackup** keeps the punched holes in the page-compressed InnoDB files it transfers.
		*Limitations*: The feature is NOT supported in the following cases, for which punched holes are removed from the InnoDB files:
		- For single-file backups.
		- For [TTS](glossary.md), incremental, compressed, or encrypted backups.
		- When a backup is not created in a file system (for example, when cloud storage is used to save the backup), or when the file system does not support sparse files.
		- For those pages of InnoDB data files that are modified by the redo log in an [`apply-log`](backup-commands-update.md) operation.
		When the feature is enabled but hole punching fails, **mysqlbackup** issues a warning message after the operation is completed; for example:
		```
		WARNING: "Punch hole" operation failed.
		```
		Or:
		```
		WARNING: InnoDB datafiles in the backup are larger than in the source because of missing sparse file support.
		```
		A backup can be taken with `--compress-method=punch-hole` and then be restored later without using the feature; the reverse is also true: a backup taken without using `--compress-method=punch-hole` can be restored later with the feature.
		Note
		`punch-hole` is a special argument with the `--compress-method` option for supporting transparent page compression. `--compress-method=punch-hole` is ignored when used together with any other **mysqlbackup** compression options.
	- `none`: No compression.
	Default: lz4. Explicitly specifying a value other than `punch-hole` for the option through a configuration file or command line automatically enables the `--compress` option.
- `--compress-level` = *`LEVEL`*
	| Command-Line Format | `--compress-level=LEVEL` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Minimum Value | `0` |
	| Maximum Value | `9` |
	Specifies the level of compression, ranging from “0” to “9”: “0 ”disables compression; “1” is fastest compression, and “9” is highest (and slowest) compression. The option is only meaningful for compression using the ZLIB or LZMA algorithm; it is ignored when any other algorithms are selected by the `--compress-method` option.
	Default: 1 (lowest and fastest compression). Explicitly specifying a non-zero value through a configuration file or command line automatically enables the `--compress` option.
- `--uncompress`
	When used with the [`extract`](backup-commands-single-file.md) operation, uncompresses files that are extracted from a compressed single-file backup (the option is not required *when the [`--src-entry`](backup-single-file-options.md) option is used*).
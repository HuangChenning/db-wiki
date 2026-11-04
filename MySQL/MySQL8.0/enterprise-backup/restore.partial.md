---
title: "5.1.4 Table-Level Recovery (TLR)"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.partial.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.4 Table-Level Recovery (TLR)

*For MySQL Enterprise Backup 8.0.20 and later:* Table-Level Recovery (TLR) allows selected tables (or schemas) to be restored from a backup (be it a full backup, a partial backup, or a backup created using [transportable tablespaces (TTS)](glossary.md)) using the [`--include-tables`](backup-partial-options.md) and [`--exclude-tables`](backup-partial-options.md) options. The feature is also known as *partial restore* in this manual. Here are some general requirements for performing a TLR or partial restore:

- The destination server must be running.
- The required parameters for connecting to the server (port number, socket name, etc.) are provided as command-line options for **mysqlbackup**, or are specified in the `[client]` section of a defaults file.
- The destination server must be using the same page size that was used on the server on which the backup was made.
- The [innodb\_file\_per\_table](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/glossary.html#glos_file_per_table) option must be enabled on the destination server.
- *For [non-TTS backups](glossary.md)*: The tables being restored must already exist on the destination server, in the same table definition.
- *For [TTS backups](glossary.md)*: The tables being restored must *not* already exist on the destination server.
- While it is *not* necessary to specify the [`--datadir`](server-repository-options.md) option when partially restoring a backup, *if* the option is specified, its value must match that of the target server, or the restore operation will fail (when restoring a TTS backup with release 8.0.16 or earlier, the [`--datadir`](server-repository-options.md) option is required).

Here are some limitations for a TLR or partial restore:

- Individual partitions cannot be selectively restored. Tables selected by the [`--include-tables`](backup-partial-options.md) and [`--exclude-tables`](backup-partial-options.md) options are always restored in full.
- Partial restores cannot be performed with incremental backups.
- Binary, relay, and undo logs are not restored.
- *For [non-TTS backups](glossary.md) only,* these additional limitations apply:
	- After partial restores, tables could contain changes from uncommitted transactions.
	- The auto-increment values of the restored tables for a partial restore might not be the same as they were at the end of the backup process.
	- Encrypted InnoDB tables cannot be included in a partial restore.

The following command restores the table `cats` in the `pets` schema from the backup:

**Example 5.7 Restoring A Selected Table from an Image Backup**

```
mysqlbackup --socket=/tmp/restoreserver.sock --include-tables="^pets\.cats" --backup-dir=/dba/backuptmp \
 --backup-image=/dba/my.mbi copy-back-and-apply-log
```

The following command restores all tables in the “sales” database from the backup, but excludes the table with the name “hardware”:

**Example 5.8 Restoring Selected Tables in a Schema from an Image Backup**

```
mysqlbackup --socket=/tmp/restoreserver.sock --include-tables="^sales\." \ 
  --exclude-tables="^sales\.hardware$" --backup-dir=/dba/backuptmp --backup-image=/dba/my.mbi \
  copy-back-and-apply-log
```

Also see [Section 5.1.5, “Restoring Backups Created with the `--use-tts` Option”](restore-use-tts.md) for additional information on partial restores using TTS backups.

Note

For MySQL Enterprise Backup 8.0.19 and before, partial restore is only supported for [TTS backups](glossary.md).
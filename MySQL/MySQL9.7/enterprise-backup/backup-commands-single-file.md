---
title: "19.5 Other Single-File Backup Operations"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-commands-single-file.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Besides the commands for creating and restoring single-file backups (namely, [`backup-to-image`](backup-commands-backup.md) and [`copy-back-and-apply-log`](backup-commands-restore.md)), **mysqlbackup** provides a number of other commands for you to work with single-file backups. They are explained below.

```
mysqlbackup [STD-OPTIONS]
            [--backup-image=IMAGE]
            [--backup-dir=PATH]
            [--src-entry=PATH] [--dst-entry=PATH]
            [--uncompress]
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            image-to-backup-dir

mysqlbackup [STD-OPTIONS]
            [--backup-dir=PATH] [--backup-image=IMAGE]
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            backup-dir-to-image

mysqlbackup [STD-OPTIONS]
            [--backup-image=IMAGE]
            [MESSAGE-LOGGING-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            list-image

mysqlbackup [STD-OPTIONS]
            [--backup-image=IMAGE]
            [--backup-dir=PATH]
            [--src-entry=PATH] [--dst-entry=PATH]
            [--uncompress]
            [MESSAGE-LOGGING-OPTIONS]
            [PROGRESS-REPORT-OPTIONS]
            [ENCRYPTION-OPTIONS]
            [CLOUD-STORAGE-OPTIONS]
            extract
```

- `image-to-backup-dir`
	It is an alias for the `extract` command; see the description below for `extract`.
	Note
	`image-to-backup-dir` only creates a [raw backup](glossary.md) directory, which is NOT ready to be restored by the [`copy-back`](backup-commands-restore.md) command. To become a [prepared backup](glossary.md), the backup directory has to go through an [apply-log operation](backup-commands-update.md), executed either by a stand-alone [`apply-log`](backup-commands-update.md) command or as a part of a [`copy-back-and-apply-log`](backup-commands-restore.md) command.
- `backup-dir-to-image`
	Packs an existing backup directory into a single file. The value for the `--backup-image` parameter should either be “ `-` ”(stands for standard output) or an absolute path outside of the `backup-dir` directory. Specify a [`--backup-image`](backup-repository-options.md) value of `-` (standard output) to stream an existing backup directory structure to a tape device or a command that transfers the backup to another server. For usage examples, see [Section 4.3.1, “Making a Single-File Backup”](meb-backup-single-file.md).
- `list-image`
	Display the contents of a single-file backup. Lists all files and directories in the image. For usage examples, see [Section 4.3.1, “Making a Single-File Backup”](meb-backup-single-file.md).
	Note
	The `list-image` operation can be performed on a cloud backup only if the cloud proxy supports HTTP range headers.
- `extract`
	Unpacks individual files or directories from a single-file backup. It is useful for troubleshooting, or for restorations that do not require the full set of backup data. The resulting file or directory goes into the current directory, or into the [backup directory](glossary.md), if specified with [`--backup-dir`](backup-repository-options.md); in either case, the destination directory must be empty. For usage examples, see [Section 4.3.1, “Making a Single-File Backup”](meb-backup-single-file.md).
	The [``--src-entry=*`string`*``](backup-single-file-options.md) option can be used for selective extraction of files or directories whose path names in the image contain the *`string`* specified with the option.
	Notes
	- Some items are always extracted from the backup; see the descriptions of [`--src-entry`](backup-single-file-options.md) for details.
	- The option is currently not supported for the extraction of cloud backups, which can only be extracted in full.
	Tip
	If you want to extract only from specific directories (for example, `datadir/meta`), add a slash at the end of the option value ([`` --src-entry=`meta/` ``](backup-single-file-options.md)); otherwise, any file or directory in the backup that contains the value in its pathname (including, for example,`datadir/pets/metabolism.ibd`) will also be extracted.
	The [``--dst-entry=*`path`*``](backup-single-file-options.md) option, along with [``--src-entry=*`path`*``](backup-single-file-options.md) option, can be used to extract files or directories into user-specified locations; see the description for the option for details.
	Use the [`--uncompress`](backup-compression-options.md) option to extract files from a compressed single-file backup (the `--uncompress` option is not required *when the [`--src-entry`](backup-single-file-options.md) is used*).
	The default destination for the extract is the current working directory. All the files with relative pathnames in the image are extracted to pathnames relative to the destination directory. If the image contains some entries with absolute pathnames, those entries are extracted to the same absolute pathnames on the local system even if the `--backup-dir` option is specified. The [`--dst-entry`](backup-single-file-options.md) option must be used to relocate an absolute pathname; see [Example 4.12, “Dealing with Absolute Path Names”](meb-backup-single-file.md).
	Important
	Even with all files extracted from the backup image, `extract` only creates a [raw backup](glossary.md) directory, which is NOT ready to be restored by the [`copy-back`](backup-commands-restore.md) command. To become a [prepared backup](glossary.md), the backup directory has to go through an [apply-log operation](backup-commands-update.md), executed either by a stand-alone [`apply-log`](backup-commands-update.md) command or as a part of a [`copy-back-and-apply-log`](backup-commands-restore.md) command.
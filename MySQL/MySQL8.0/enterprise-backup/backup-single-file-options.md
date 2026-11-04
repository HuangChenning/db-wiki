---
title: "20.9 Single-File Backup Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-single-file-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

These options are associated with single-file backups. You use them in combination with the **mysqlbackup** commands [`backup-to-image`](backup-commands-backup.md), [`image-to-backup-dir`](backup-commands-single-file.md), [`backup-dir-to-image`](backup-commands-single-file.md), [`copy-back-and-apply-log`](backup-commands-restore.md), [`list-image`](backup-commands-single-file.md), and [`extract`](backup-commands-single-file.md) (not all of the options are applicable to all these commands though). For usage examples, see [Section 4.3.1, “Making a Single-File Backup”](meb-backup-single-file.md).

- `--backup-image` = *`IMAGE`*
	See description of the option in [Section 20.4, “Backup Repository Options”](backup-repository-options.md)
- `--src-entry` = *`STRING`*
	| Command-Line Format | `--src-entry=STRING` |
	| --- | --- |
	| Type | Path name |
	Identifies files or directories whose pathnames contain the STRING to be extracted from a single-file backup. This option is used with the [`extract`](backup-commands-single-file.md) and [`image-to-backup-dir`](backup-commands-single-file.md) commands. Optionally, you can also specify the `--dst-entry` option to extract a file or directory to a location different from its original path name.
	For example: `src-entry=d1/f2` extracts only one file, `f2`, while `src-entry=d1/` extracts the entire directory tree for the `d1` folder (notice the slash (`/`) at the end of the argument, without which all files or folders containing the string `d1` in their pathnames will be extracted).
	Default: All entries are extracted.
	Notes
	- The following items are always extracted from the backup, irrespective of the value of `--src-entry` (and the locations of their extraction are unaffected by the `--dst-entry` option):
		- The file `backup-my.cnf`.
		- A `datadir` folder (which only contains items matched by the `--src-entry` option).
		- A `meta` folder, which contains the file `                       backup_variables.txt`, a log file for the extract operation, and also items matched by the `--src-entry` option.
	- The option is currently not supported for the [`extract`](backup-commands-single-file.md) command for cloud backups, which can only be extracted in full.
- `--dst-entry` = *`PATH`*
	| Command-Line Format | `--dst-entry=PATH` |
	| --- | --- |
	| Type | Path name |
	Used with single-file backups to extract a file or directory to a user-specified path. Use of this option requires specifying the `--src-entry` option. This option specifies the destination path for the entry selected from the backup image by `--src-entry`. The entry could point to a single file or single directory. For example, to retrieve the comments file from a backup image and store it as `/tmp/my-comments.txt`, use a command like the following:
	```
	mysqlbackup --src-entry=meta/comments.txt \
	  --dst-entry=/tmp/my-comments.txt \
	  --backup-image=/var/myimage.bki  extract
	```
	Similarly, to extract all the contents of the `datadir/pets/` directory in a single-file backup as `/pets-extracted/`, use a command like the following:
	```
	mysqlbackup --src-entry=datadir/pets/ \
	  --dst-entry=/pets-extracted/ \
	  --backup-image=/var/myimage.bki  extract
	```
	The specified path is a simple path name without any wildcard expansion or regular expressions.
	In case the argument for `--src-entry` matches multiple files or folders, they are all extracted into a folder whose pathname, relative to the destination folder, is given by the argument of `--dst-entry` (unless the argument specifies an absolute path).
	Default: Original pathnames are used to create files under the destination folder.
- `--sbt-database-name` = *`NAME`*
	| Command-Line Format | `--sbt-database-name=NAME` |
	| --- | --- |
	| Type | String |
	| Default Value | `MySQL` |
	For tape backups, this option can be used as a hint to the Media Management Software (MMS) for the selection of media and policies. This name has nothing to do with MySQL database names. It is a term used by the MMS. See [Section 4.3.1.2, “Backing Up to Tape”](meb-backup-tape.md) for usage details.
- `--sbt-lib-path` = *`PATH`*
	| Command-Line Format | `--sbt-lib-path=PATH` |
	| --- | --- |
	| Type | File name |
	Path name of the SBT library used by the software that manages tape backups. If this is not specified, operating system-specific search methods are used to locate `libobk.so` (UNIX) or `orasbt.dll` (Windows). See [Section 4.3.1.2, “Backing Up to Tape”](meb-backup-tape.md) for usage details.
- `--sbt-environment` = *`VAR`* = *`value`*,...
	| Command-Line Format | `--sbt-environment=VAR1=value1[,VAR2=value2[,...]] SBT API provider)` |
	| --- | --- |
	| Type | String |
	Passes product-specific environment variables to Oracle Secure Backup or another SBT-compliant backup management product, as an alternative to setting and unsetting environment variables before and after each **mysqlbackup** invocation.
	The parameter to this option is a comma-separated list of key-value pairs, using syntax similar to that of the RMAN tool for the Oracle Database. For example, `--sbt-environment=VAR1=val1,VAR2=val2,VAR3=val3`.
	Consult the documentation for your backup management product to see which of its features can be controlled through environment variables. For example, the Oracle Secure Backup product [defines environment variables](http://docs.oracle.com/cd/E14812_01/doc/doc.103/e12838/rman_params.htm) such as `OB_MEDIA_FAMILY`, `OB_DEVICE`, and `OB_RESOURCE_WAIT_TIME`. You might set such variables with the **mysqlbackup** by specifying an option such as `--sbt-environment="OB_MEDIA_FAMILY=my_mf,OB_DEVICE=my_tape"`.
	If the argument string contains any whitespace or special characters recognized by the command shell, enclose the entire argument string in quotation marks. To escape an equal sign or comma, use the `\` character. For example, `--sbt-environment="VAR1=multiple             words,VAR2=<angle_brackets>,VAR3=2+2\=4"`.
- `--disable-manifest`
	Disable generation of [manifest](glossary.md) files for a backup operation, which are `backup_create.xml` and `backup_content.xml` present in the `meta` subdirectory.
---
title: "4.3.1 Making a Single-File Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-backup-single-file.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.3.1 Making a Single-File Backup

To avoid having a large number of backup files to keep track, store, and transport, **mysqlbackup** conveniently creates backups in a single-file format. It can also pack an existing backup directory into a single file, unpack the single file back to a backup directory, list the contents of a single-file backup, verify the contents of a single-file backup against embedded checksums, or extract a single file into a directory tree. For the syntax of the relevant **mysqlbackup** options, see [Section 20.9, “Single-File Backup Options”](backup-single-file-options.md).

*Advanced:* While **mysqlbackup** can also create a directory backup (see description for the [`backup`](backup-commands-backup.md) command for details) instead of a single-file backup, the single-file format is preferable in most cases: a single-file backup is easier to handle and store, and certain functions of **mysqlbackup** are not supported for directory backups—for example, backup to cloud and backup to tape using the System Backup to Tape (SBT) API. Throughout the manual, directory backup is mostly treated as an advanced topic, and information and examples for directory backups are marked with the *Advanced* tag, like this paragraph.

Because the single-file backup can be streamed or piped to another process such as a tape backup or a command, you can use the technique to put the backup onto another storage device or server and avoid significant storage overhead on the original database server.

To create a single-file backup, use the [`backup-to-image`](backup-commands-backup.md) command. The following examples illustrate how to perform a single-file backup and other related operations.

**Example 4.1 Single-File Backup to Absolute Path**

This command creates a single backup image on the given absolute path. It still requires `--backup-dir`, which is used to hold temporary output, status, and metadata files.

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --backup-image=/backups/sales.mbi --backup-dir=/backup-tmp backup-to-image
```

**Example 4.2 Single-File Backup to Relative Path**

When a relative path instead of an absolute path was supplied with the [`--backup-image`](backup-repository-options.md) option, the path is taken to be relative to the [backup directory](glossary.md). Therefore, in this example, the resulting single-file backup is created as `/backups/sales.mbi`.

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --backup-image=sales.mbi --backup-dir=/backups backup-to-image
```

**Example 4.3 Single-File Backup to Standard Output**

The following command dumps the backup output to standard output. Again, the folder specified with the [`--backup-dir`](backup-repository-options.md) option is used as a temporary directory.

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --backup-dir=/backups --backup-image=- backup-to-image > /backup/mybackup.mbi
```

**Example 4.4 Convert Existing Backup Directory to Single Image**

The `backup-dir` directory is bundled into the `/backup/my.mbi` file.

```
mysqlbackup --backup-image=/backup/my.mbi --backup-dir=/var/mysql/backup backup-dir-to-image
```

**Example 4.5 Extract Existing Image to Backup Directory**

The image contents are unpacked into *`backup-dir`*.

```
mysqlbackup --backup-dir=/var/backup --backup-image=/backup/my.mbi image-to-backup-dir
```

**Example 4.6 List Single-File Backup Contents**

The image contents are listed, with each line indicating a file or directory entry.

```
mysqlbackup --backup-image=/backup/my.mbi list-image
```

**Example 4.7 Validate a Single-File Backup**

The following command verifies that the single-file backup is not corrupted, truncated, or damaged by validating the checksum value for each data page in the backup.

```
mysqlbackup --backup-image=/logs/fullimage.mi  validate
```

**Example 4.8 Extract Single-File Backup into Current Directory**

The following command extracts all contents from a single-file backup into the current working directory.

```
mysqlbackup --backup-image=/var/my.mbi extract
```

**Example 4.9 Extract Single-File Backup into a Backup Directory**

This command extracts all contents of a single-file backup into the directory specified with the [`--backup-dir`](backup-repository-options.md) option.

```
mysqlbackup --backup-image=/var/my.mbi --backup-dir=/var/backup extract
```

**Example 4.10 Selective Extract of Single File**

The following command extracts the single file `meta/comments.txt` from the backup image `my.mbi` into the local path`./meta/comments.txt`.

```
mysqlbackup --backup-image=/var/my.mbi \
  --src-entry=meta/comments.txt extract
```

The following command extracts the `meta/comments.txt` file from the backup image `my.mbi` into a specified path `/tmp/mycomments.txt` by using the [`--dst-entry`](backup-single-file-options.md) option.

```
mysqlbackup --backup-image=/var/my.mbi \
  --src-entry=meta/comments.txt \
  --dst-entry=/tmp/mycomments.txt extract
```

The following command dumps the contents of `meta/comments.txt` (which is inside the single-file backup `my.mbi`) to standard output.

```
mysqlbackup --backup-image=/var/my.mbi --src-entry=meta/comments.txt --dst-entry=- extract
```

**Example 4.11 Selective Extract of Single Directory**

The following command extracts a single directory `meta` from the backup image `my.mbi` into a local file system path `./meta`. All contents in the `meta` directory are extracted, including any subdirectories. (Notice the slash (`/`) at the end of the value `meta/` for [`--src-entry`](backup-single-file-options.md), without which all files or folders containing the string `meta` in their pathnames will be extracted.)

```
mysqlbackup --backup-image=/backup/my.mbi --src-entry=meta/ extract
```

**Example 4.12 Dealing with Absolute Path Names**

Since absolute pathnames are extracted to the same paths in local system, it could be a problem if you do not have write permission for that path. You can remap absolute paths as follows:

```
mysqlbackup --backup-image=/backup/my.mbi --src-entry=/ --dst-entry=/myroot extract
mysqlbackup --backup-image=/backup/my.mbi --src-entry=. extract
```

The first command extracts all absolute paths to `/myroot` directory in the local system. The second command extracts all relative paths to the current directory.
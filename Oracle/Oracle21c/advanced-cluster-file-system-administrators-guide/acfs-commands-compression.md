---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-compression.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of commands to manage Oracle ACFS compression.

Table 6-54 lists Oracle ACFS compression commands with brief descriptions. For an overview of Oracle ACFS compression, refer to [Oracle ACFS Compression](understand-acfs-admin.md).

For more information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Table 6-54 Summary of commands for Oracle ACFS compression

| Command | Description |
| --- | --- |
| acfsutil compress copy | Copies and compresses a file or files in a directory. |
| acfsutil compress info | Displays compression information about a file. |
| acfsutil compress off | Enables Oracle ACFS file compression. |
| acfsutil compress on | Disables Oracle ACFS file compression. |

### acfsutil compress copy

Purpose

Compresses and copies a file.

Syntax and Description

```
acfsutil compress copy -h
acfsutil compress copy [-v] [-f] {-c size source | [-n] {-r source | source [...]} 
                       target_dir
```

The following table contains the options available with the `acfsutil` `compress` `copy` command.

Table 6-55 Options for the acfsutil compress copy command

| Option | Description |
| --- | --- |
| `-v` | Specifies verbose mode. |
| `-f ` | Specifies to overwrite any existing copies. |
| `—c` `size source` | Copies a single source file and uses compression unit (CU) size for the copy.  The format of size is n `K`. The CU sizes supported are: `4K`, `8K`, `16K`, `32K`, `64K` and `128K` bytes. |
| `—n ` `source` | Specifies that copies created are not compressed. |
| `—r ` `source` | Specifies to recursively copy files and directories starting from a single source directory. |
| `source [...]` | Specifies source files to be copy. |
| `target_dir` | Specifies the target directory to copy into. |

The `acfsutil` `compress` `copy` command does not copy over an existing files unless the `-f` option is used. If `-f` is not used, the copy operation terminates when the first existing target is found.

The command does not copy to an Oracle ACFS file system which is capable of supporting compression if compression is disabled unless the `-n` option is specified.

Example 6-49 Using the acfsutil compress copy command

```
$ /sbin/acfsutil compress copy -v -f my_file1 my_file2 /my_target_directory
```

### acfsutil compress info

Purpose

Displays information about compressed files.

Syntax and Description

```
acfsutil compress info -h
acfsutil compress info pathname
```

The following table contains the options available with the `acfsutil` `compress` `info` command.

Table 6-56 Options for the acfsutil compress info command

| Option | Description |
| --- | --- |
| `pathname` | Specifies the pathname to a file. |

Example 6-50 Using the acfsutil compress info command

```
$ /sbin/acfsutil compress info /my_mount_point/testfile1

Compression Unit size: 8192
Disk storage used: ( 189.89 MB )
Disk storage saved: ( 810.20 MB )
Storage used is 18% of what the uncompressed file would use
```

### acfsutil compress off

Purpose

Disables Oracle ACFS compression.

Syntax and Description

```
acfsutil compress off -h
acfsutil compress off mount_point
```

The following table contains the options available with the `acfsutil` `compress` `off` command.

Table 6-57 Options for the acfsutil compress off command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

When running `acfsutil` `compress` `off`, the following apply:

- Files that are created after compression is disabled are created uncompressed.
- Any compressed files in the file system remain compressed.

You must have root or system administrator privileges to run this command.

Example 6-51 Using the acfsutil compress off command

```
$ /sbin/acfsutil compress off /my_mount_point
```

### acfsutil compress on

Purpose

Enables Oracle ACFS compression.

Syntax and Description

```
acfsutil compress on -h
acfsutil compress on [-a algorithm] mount_point
```

The following table contains the options available with the `acfsutil` `compress` `on` command.

Table 6-58 Options for the acfsutil compress on command

| Option | Description |
| --- | --- |
| `—a algorithm` | Specifies the default compression algorithm. Currently only `lzo` is available and that is the default algorithm used. |
| `mount_point` | Specifies the directory where the file system is mounted. |

Note:

Oracle ACFS compression is not supported on Oracle Database files. Oracle ACFS file systems which are intended to hold database files should not be compressed with Oracle ACFS compression.

When running `acfsutil` `compress` `on`, the following apply:

- Files created after compression is enabled are compressed by default.
- Any uncompressed files in the file system remain uncompressed.

You must have root or system administrator privileges to run this command.

Example 6-52 Using the acfsutil compress on command

```
$ /sbin/acfsutil compress on /my_mount_point
```
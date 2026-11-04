---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-tagging.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of the Oracle ACFS tagging commands.

Table 6-17 lists the Oracle ACFS tagging commands with brief descriptions.

On Solaris, `acfsutil` `tag` commands can set tag names on symbolic link files, but backup and restore utilities do not save the tag names that are explicitly set on the symbolic link files. Also, symbolic link files lose explicitly set tag names if they have been moved, copied, tarred, or paxed.

Table 6-17 Summary of commands for Oracle ACFS tagging

| Command | Description |
| --- | --- |
| acfsutil tag info | Displays the tags for directories or files in Oracle ACFS file systems. |
| acfsutil tag set | Adds a tag to directories or files in an Oracle ACFS file system. |
| acfsutil tag unset | Removes a tag or all tag names from directories or files in an Oracle ACFS file system. |

See Also:

- [Oracle ACFS Tagging](understand-acfs-admin.md) for an overview of Oracle ACFS tagging
- [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md) for information about running Oracle ACFS `acfsutil` commands
- [Oracle ACFS Tagging Generic Application Programming Interface](acfs-advanced-topics.md) for information about Oracle ACFS tagging application programming interfaces (APIs)

### acfsutil tag info

Purpose

Displays the tag names for tagged directories or file names in Oracle ACFS file systems.

Syntax and Description

```
acfsutil tag info -h
acfsutil tag info [-r] [-c -t tagname] path [path ...]
acfsutil tag info [-c -t tagname]
```

`acfsutil` `tag` `info` `-h` displays help text and exits.

Table 6-18 contains the options available with the `acfsutil` `tag` `info` command.

Table 6-18 Options for the acfsutil tag info command

| Option | Description |
| --- | --- |
| `-t` `tagname` | Specifies the tag name string to display. Enclose the string in quotes if the string contains a space. |
| `path` | Specifies the path name to one or more files or directories. |
| `-r` | Specifies recursive action on a specified path. |
| `-c` | Specifies case-insensitive partial matching on the tag name. |

The `acfsutil` `tag` `info` command can recursively apply the operation to all child files and subdirectories if the `-r` option is included with specified directory path names.

If no path names are specified, the `acfsutil` `tag` `info` command searches all Oracle ACFS mount points for tagged files.

Only the paths of tagged files in an Oracle ACFS file system are displayed. If the `-t` `tagname` option is included, only paths of files with a tag name exactly matching the specified `tagname` are displayed. If the `-c` option is included, then `tagname` can be a case-insensitive substring of a tag name for a successful match. For example, the `acfsutil` `tag` `info` `-c` `-t` `AG` command would display path names of files with tag names such as `tag1`, `ag`, or `AG`.

Any user may use this command to display tag info on a directory to which the user has read access.

Examples

The following example show the use of the `acfsutil` `tag` `info` command.

Example 6-16 Using the acfsutil tag info command

```
$ /sbin/acfsutil tag info -r /acfsmounts/acfs1/myrepfiles/
```

### acfsutil tag set

Purpose

Adds the given tag to the specified files or directories in an Oracle ACFS file system

Syntax and Description

```
acfsutil tag set -h
acfsutil tag set [-v] [-r] tagname path [path ...]
```

`acfsutil` `tag` `set` `-h` displays help text and exits.

Table 6-19 contains the options available with the `acfsutil` `tag` `set` command.

Table 6-19 Options for the acfsutil tag set command

| Option | Description |
| --- | --- |
| `tagname` | Specifies a tag name string. Enclose the string in quotes if the string contains a space.  The tag string can be composed of ASCII characters that include: a-b, A-Z, 0-9, the space character, the hyphen, and the underscore. The maximum length of a tag name is 32 characters.  `all` is a reserved tag name and cannot be set on any file or directory. |
| `path` | Specifies the path string to one or more files or directories. |
| `-r` | Specifies recursive action on the specified path. |
| `-v` | Displays the progress of the operation. |

The command can recursively apply the operation to all child files and subdirectories for the specified directory path names.

When adding a tag name to a file or directory, the existing tags on that file or directory remain unchanged. New files that are created after a directory is assigned a tag implicitly inherit tags from their parent directories. Existing files in the directory do not inherit the new tag; these files must be explicitly assigned the tag. Renaming a file or moving a file to a subdirectory within the same file system does not cause the file to inherit tag names from the new parent directory. Moving a file between file systems uses a copy operation and the newly created file does inherit the tag names of the parent directory.

There is no fixed maximum number of tag names for an Oracle ACFS file system or for each file and directory. However, the number of tag names is limited by the tag names that fit in up to 64 KB of special metadata storage for each file and directory. This metadata also contains information to manage the extended attributes. Longer tag names reduce the total of tag names that can be set on a file or directory. For example, if all tag names were 4 bytes long, then it is possible to hold approximately 1730 tag names, assuming no other extended attribute information is present.

Any user who has the privilege to modify the target file or directory may run this command.

Examples

The following example show the use of the `acfsutil` `tag` `set` command.

Example 6-17 Using the acfsutil tag set command

```
$ /sbin/acfsutil tag set repl_grp1 -r /acfsmounts/acfs1/myrepfiles/*.dat
```

### acfsutil tag unset

Purpose

Removes the given tag name or all tag names from the specified file or directory.

Syntax and Description

```
acfsutil tag unset -h
acfsutil tag unset [-v] [-r] {all | tagname} path [path ...]
```

`acfsutil` `tag` `unset` `-h` displays help text and exits.

Table 6-20 contains the options available with the `acfsutil` `tag` `unset` command.

Table 6-20 Options for the acfsutil tag unset command

| Option | Description |
| --- | --- |
| `all` | Specifies to remove all tags in the path string. |
| `tagname` | Specifies a tag name string. Enclose the string in quotes if the string contains a space. |
| `path` | Specifies the path string to one or more files or directories. |
| `-r` | Specifies recursive action on the specified path. |
| `-v` | Displays the progress of the operation. |

The command can recursively apply the operation to all child files and subdirectories for the specified directory path names.

When removing a tag name from a file or directory, other existing tags on that file or directory remain unchanged.

Any user who has privilege to modify the target file or directory may run this command.

Examples

The following example show the use of the `acfsutil` `tag` `unset` command.

Example 6-18 Using the acfsutil tag unset command

```
$ /sbin/acfsutil tag unset repl_grp1 -r
     /acfsmounts/acfs1/myrepfiles/*.log
```
---
title: Oracle ACFS Command-Line Tools for Tagging
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util006.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-25 contains a summary of the commands for Oracle ACFS tagging.

You can run `acfsutil` `help` on all platforms to display help text. You can run `acfsutil` `version` on all platforms to display the Oracle ACFS version.

When the options are entered with commands on a Windows platform, use `/` instead of `-` with the option. For example, you can display help for `acfsutil` on a Linux platform with `acfsutil` `-h`. On a Windows platform, use `acfsutil` `/h`.

Note that a mount point on a Windows operating system can be a drive letter or a directory including the drive letter.

Table 13-25 Summary of commands for Oracle ACFS tagging

| Command | Description |
| --- | --- |
| acfsutil tag info | Displays the tags for directories or files in Oracle ACFS file systems. |
| acfsutil tag set | Adds a tag to directories or files in an Oracle ACFS file system. |
| acfsutil tag unset | Removes a tag or all tag names from directories or files in an Oracle ACFS file system. |

## acfsutil tag info

Purpose

Displays the tag names for tagged directories or file names in Oracle ACFS file systems.

Syntax and Description

  
`acfsutil` `tag` `info` `-h`  
`acfsutil` `tag` `info` \[`-r`\] \[`-t` `tagname`\] `path` \[`path`...\]  
`acfsutil` `tag` `info` \[`-t` `tagname`\]  

`acfsutil` `tag` `info` `-h` displays help text and exits.

Table 13-26 contains the options available with the `acfsutil` `tag` `info` command.

Table 13-26 Options for the acfsutil tag info command

| Option | Description |
| --- | --- |
| `-t` `tagname` | Specifies the tag name string to display. Enclose the string in quotes if the string contains a space. |
| `path` | Specifies the path name to one or more files or directories. |
| `-r` | Specifies recursive action on a specified path. |

The `acfsutil` `tag` `info` command can recursively apply the operation to all child files and subdirectories if the `-r` option is included with specified directory path names.

If no path names are specified, the `acfsutil` `tag` `info` command searches all Oracle ACFS mount points for tagged files.

Only the paths of tagged files in an Oracle ACFS file system are displayed. If the `-t` `tagname` option is included, only tag names matching `tagname` are displayed.

Any user may use this command to display tag info on a directory that the user has read access privileges.

Examples

The following example show the use of the `acfsutil` `tag` `info` command.

Example 13-21 Using the acfsutil tag info command

```
$ /sbin/acfsutil tag info -r /u01/app/acfsmounts/myacfs/myrepfiles/
```

## acfsutil tag set

Purpose

Adds the given tag to the specified files or directories in an Oracle ACFS file system

Syntax and Description

  
`acfsutil` `tag` `set` `-h`  
`acfsutil` `tag` `set` \[`-v`\] \[`-r`\] `tagname` `path` \[`path`...\]  

`acfsutil` `tag` `set` `-h` displays help text and exits.

Table 13-27 contains the options available with the `acfsutil` `tag` `set` command.

Table 13-27 Options for the acfsutil tag set command

| Option | Description |
| --- | --- |
| `tagname` | Specifies a tag name string. Enclose the string in quotes if the string contains a space.  The tag string can be composed of ASCII characters that include: a-b, A-Z, 0-9, the space character, the hyphen, and the underscore. The maximum length of a tag name is 32 characters.  `all` is a reserved tag name and cannot be set on any file or directory. |
| `path` | Specifies the path string to one or more files or directories. |
| `-r` | Specifies recursive action on the specified path. |
| `-v` | Displays the progress of the operation. |

The command can recursively apply the operation to all child files and subdirectories for the specified directory path names.

When adding a tag name to a file or directory, the existing tags on that file or directory remain unchanged. New files that are created after a directory is assigned a tag implicitly inherit tags from their parent directories. Existing files in the directory do not inherit the new tag; these files must be explicitly assigned the tag. Renaming a file or moving a file to a subdirectory within the same file system does not cause the file to inherit tag names from the new parent directory. Moving a file between file systems uses a copy operation and the newly created file does inherit the tag names of the parent directory.

Any user who has the privilege to modify the target file or directory may run this command.

Examples

The following example show the use of the `acfsutil` `tag` `set` command.

Example 13-22 Using the acfsutil tag set command

```
$ /sbin/acfsutil tag set repl_grp1 -r /u01/app/acfsmounts/myacfs/myrepfiles/*.dat
```

## acfsutil tag unset

Purpose

Removes the given tag name or all tag names from the specified file or directory.

Syntax and Description

  
`acfsutil` `tag` `unset` `-h`  
`acfsutil` `tag` `unset` \[`-v`\] \[`-r`\] { `all` | `tagname` } `path` \[`path`...\]  

`acfsutil` `tag` `unset` `-h` displays help text and exits.

Table 13-28 contains the options available with the `acfsutil` `tag` `unset` command.

Table 13-28 Options for the acfsutil tag unset command

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

Example 13-23 Using the acfsutil tag unset command

```
$ /sbin/acfsutil tag unset repl_grp1 -r
     /u01/app/acfsmounts/myacfs/myrepfiles/*.log
```
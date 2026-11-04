---
title: ASMCMD File Management Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util003.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD file management commands.

Table 12-16 provides a summary of the file management commands.

Table 12-16 Summary of ASMCMD file management commands

| Command | Description |
| --- | --- |
| cd | Changes the current directory to the specified directory. |
| cp | Enables you to copy files between disk groups, and between a disk group and the operating system. |
| du | Displays the total disk space occupied by files in the specified Oracle ASM directory and all of its subdirectories, recursively. |
| find | Lists the paths of all occurrences of the specified name (with wildcards) under the specified directory. |
| ls | Lists the contents of an Oracle ASM directory, the attributes of the specified file, or the names and attributes of all disk groups. |
| lsof | Lists the open files. |
| mkalias | Creates an alias for system-generated filenames. |
| mkdir | Creates Oracle ASM directories. |
| pwd | Displays the path of the current Oracle ASM directory. |
| rm | Deletes the specified Oracle ASM files or directories. |
| rmalias | Deletes the specified alias, retaining the file that the alias points to. |

## cd

Purpose

Changes the current directory to the specified directory.

Syntax and Description

`cd` \[`dir`\]

Table 12-17 lists the options for the `cd` command.

Table 12-17 Options for the cd command

| Option | Description |
| --- | --- |
| `dir` | Name of the directory. |

`dir` can be specified as either an absolute path or a relative path, including the `.` and `..` pseudo-directories. `dir` can contain wildcard characters. See ["Wildcard Characters"](asm_util001.md).

Examples

The following are examples of the `cd` command changing into various directories.

Example 12-19 Using the ASMCMD cd command

```
ASMCMD [+data/hr] > cd +data/orcl

ASMCMD [+data/orcl] > cd DATAFILE

ASMCMD [+data/orcl/DATAFILE] >cd ..
```

## cp

Purpose

Enables you to copy files between Oracle ASM disk groups and between a disk group and the operating system.

Syntax and Description

  
`cp` `src_file` \[`rem_connect_str``:`\] `tgt_file`  
`cp` \[`rem_connect_str``:`\] `src_file` `tgt_file`  

Table 12-18 lists the syntax options for the `cp` command.

Table 12-18 Options for the cp command

| Option | Description |
| --- | --- |
| `rem_connect_str` | Specifies the connection string for a remote instance. |
| `src_file` | Name of the source file to copy. |
| `tgt_file` | A user alias for the created target file name or an alias directory name. |

`cp` cannot copy files between two remote instances. The local Oracle ASM instance must be either the source or the target of the operation.

You can use the `cp` command to:

- Copy files from a disk group to the operating system
- Copy files from a disk group to a disk group
- Copy files from the operating system to a disk group

Some file types cannot be the source or destination of the `cp` command. These file types include OCR and OCR backup file types. To back up, copy, or move an Oracle ASM SPFILE, use the `spbackup`, `spcopy`, or `spmove` commands.

`rem_connect_str` is not required for a local instance copy, which is the default case. For a remote instance copy, you must specify the connect string and Oracle ASM prompts for a password in a non-echoing prompt. The `rem_connect_str` is in the form:

`user` `@` `host` `[.``port_number``].``SID`

`user`, `host`, and `SID` are required in the `rem_connect_str` parameter. The default port number is `1521`.

The connection privilege (`SYSASM` or `SYSDBA`) is determined by the use of the `--privilege` option when starting ASMCMD. For more information, refer to ["Specifying the Type of Connection"](asm_util001.md).

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about connection strings

`src_file` must be either a fully qualified file name or an Oracle ASM alias.

The `cp` command performs a bit-wise copy. There is no data transformation.

Examples

The following are examples of the `cp` command. The first example shows a copy of a file in the `data` disk group to a file on the operating system. The second example shows a copy of a file on the operating system to the `data` disk group. The third example shows how to copy a file in the `data` disk group to a remote server. If the password is not included in the command line, you are prompted to enter the password.

Example 12-20 Using the ASMCMD cp command

```
ASMCMD [+] > cp +data/orcl/datafile/EXAMPLE.265.691577295 /mybackups/example.bak
copying +data/orcl/datafile/EXAMPLE.265.691577295 -> /mybackups/example.bak

ASMCMD [+] >  cp /mybackups/examples.bak  +data/orcl/datafile/myexamples.bak
copying /mybackups/examples.bak -> +data/orcl/datafile/myexamples.bak

ASMCMD [+] > cp +data/orcl/datafile/EXAMPLE.265.691577295 sys@myserver.+ASM:/scratch/backup/myexamples.bak
Enter Password:
```

## du

Purpose

Displays the total space used for files in the specified directory and in the entire directory tree under the directory.

Syntax and Description

`du` \[`--suppressheader`\] `[``dir``]`

Table 12-19 lists the syntax options for the `du` command.

Table 12-19 Options for the du command

| Option | Description |
| --- | --- |
| `dir` | Name of the directory. |
| `--suppressheader` | Suppresses column headings from the output. |

If you do not specify `dir`, then information about the current directory is displayed. `dir` can contain wildcard characters. See ["Wildcard Characters"](asm_util001.md).

The following two values are displayed, both in units of megabytes.

- `Used_MB` - This value does not include mirroring.
- `Mirror_used_MB` - This value includes mirroring.

For example, if a normal redundancy disk group contains 100 MB of data and each file in the disk group is 2-way mirrored, then `Used_MB` is 100 MB and `Mirror_used_MB` is roughly 200 MB.

Example

The following is an example of the `du` command. The example shows disk space used in the `orcl` directory in the `data` disk group, including all of the directories under the `orcl` directory.

Example 12-21 Using the ASMCMD du command

```
ASMCMD [+] > du data/orcl
Used_MB      Mirror_used_MB
   1756                3519
```

## find

Purpose

Displays the absolute paths of all occurrences of the specified name pattern (with wildcards) in a specified directory and its subdirectories.

Syntax and Description

`find` `[--type` `type``]` `dir` `pattern`

Table 12-20 lists the syntax options for the `find` command.

Table 12-20 Options for the find command

| Option | Description |
| --- | --- |
| `--type` `type` | Type of target to find. |
| `dir` | Directory name where you want to start searching. |
| `pattern` | Name of a target or a wildcard pattern. |

This command searches the specified directory and all subdirectories under it in the directory tree for the supplied `pattern`. The value used for `pattern` can be a directory name or a filename, and can include wildcard characters. See ["Wildcard Characters"](asm_util001.md).

The ASMCMD `find` command is case insensitive.

In the output of the command, directory names are suffixed with the slash character (/) to distinguish them from filenames.

Use the `--type` flag to find all the files of a particular type (specified as `type`). For example, you can search for control files by specifying `type` as `CONTROLFILE`. Valid values for `type` are listed in [Table 7-1, "File types supported by Oracle ASM"](asmfiles.md). These are type values from the `type` column of the `V$ASM_FILE` view.

Examples

The following are examples of the `find` command. The first example searches the `data` disk group for files that begin with `undo`. The second example returns the absolute path of all the control files (`--type` `CONTROLFILE`) in the `+data/orcl` directory.

Example 12-22 Using the ASMCMD find command

```
ASMCMD [+] > find +data undo*
+data/ORCL/DATAFILE/UNDOTBS1.258.691577151

ASMCMD [+] >  find --type CONTROLFILE +data/orcl *
+data/orcl/CONTROLFILE/Current.260.691577263
```

## ls

Purpose

Lists the contents of an Oracle ASM directory, the attributes of the specified file, or the names and attributes of all disk groups.

Syntax and Description

  
`ls` \[`--suppressheader`\] \[`-lsdtLg`\]\[`--absolutepath`\]\[`--reverse`\]  
 \[`--permission`\]\[`pattern``]`  
  

Table 12-21 lists the syntax options for the `ls` command.

Table 12-21 Options for the ls command

| Option | Description |
| --- | --- |
| (none) | Displays only filenames and directory names. |
| `-l` | Displays extended file information, including striping and redundancy information and whether the file was system-generated (indicated by `Y` under the `SYS` column) or user-created (as with an alias, indicated by `N` under the `SYS` column). When used in the " `ls -l +` " command, displays directory information.  Not all possible file attributes or disk group attributes are included. To view the complete set of column values for a file or a disk group, query the `V$ASM_FILE` and `V$ASM_DISKGROUP` views. |
| `-s` | Displays file space information. |
| `-d` | If the value for the `pattern` argument is a directory, then `ls` displays information about that directory, rather than the directory contents. Typically used with another flag, such as the `-l` flag. |
| `--reverse` | Reverses the sort order of the listing. |
| `-t` | Sorts the listing by timestamp (latest first) instead of by name. |
| `-L` | If the value for the `pattern` argument is an alias, then ASMCMD displays information about the file that it references. Typically used with another flag, such as the `-l` flag. |
| `--absolutepath` | For each listed file, displays the absolute path of the alias that references it, if any. |
| `-g` | `GV$ASM_DISKGROUP.INST_ID` is included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `--permission` | Shows the permissions of a file (`V$ASM_FILE.permission`, `V$ASM_FILE.owner`, `V$ASM_FILE.usergroup`, `V$ASM_ALIAS.name`). |
| `pattern` | Name of a file, directory, or a pattern. |

Command options enable you to modify and customize the output of the command. Table 12-21 lists the options and their descriptions. For disk group information, this command queries the `V$ASM_DISKGROUP_STAT` view by default. If you specify all of the options, then the command shows a union of their attributes, with duplicates removed. If you enter `ls` `+`, the top level directory structure is displayed.

`pattern` can be a file name, directory name, or a pattern including wildcard characters. See ["Wildcard Characters"](asm_util001.md).

- If `pattern` is a directory name, then `ls` lists the contents of the directory and depending on flag settings, `ls` also lists information about each directory member. Directories are listed with a trailing slash (/) to distinguish them from files.
- If the value that you enter for `pattern` is a file name, then `ls` lists the file and depending on the flag settings, `ls` also lists information about the file. The file must be located in the current directory if the file name is specified with a relative path.

Examples

The following are examples of the `ls` command that display various information about directories and the contents of the directories.

Example 12-23 Using the ASMCMD ls command

```
ASMCMD [+] > ls +data/orcl/datafile
EXAMPLE.265.691577295
SYSAUX.257.691577149
SYSTEM.256.691577149
UNDOTBS1.258.691577151
USERS.259.691577151

ASMCMD [+] > ls -lt +data/orcl/datafile
Type      Redund  Striped  Time             Sys  Name
DATAFILE  MIRROR  COARSE   JUL 13 08:00:00  Y    EXAMPLE.265.691577295
DATAFILE  MIRROR  COARSE   JUL 13 05:00:00  Y    SYSAUX.257.691577149
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    USERS.259.691577151
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    UNDOTBS1.258.691577151
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    SYSTEM.256.691577149

ASMCMD [+] > ls -l +data/orcl/datafile/sy*
Type      Redund  Striped  Time             Sys  Name
DATAFILE  MIRROR  COARSE   JUL 13 05:00:00  Y    SYSAUX.257.691577149
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    SYSTEM.256.691577149

ASMCMD [+] > ls -s  +data/orcl/datafile
Block_Size  Blocks      Bytes       Space  Name
      8192   12801  104865792   214958080  EXAMPLE.265.691577295
      8192   88321  723525632  1452277760  SYSAUX.257.691577149
      8192   88321  723525632  1452277760  SYSTEM.256.691577149
      8192    7681   62922752   131072000  UNDOTBS1.258.691577151
      8192     641    5251072    12582912  USERS.259.691577151

ASMCMD [+] > ls --permission  +data/orcl/datafile
User  Group  Permission  Name
              rw-rw-rw-  EXAMPLE.265.691577295
              rw-rw-rw-  SYSAUX.257.691577149
              rw-rw-rw-  SYSTEM.256.691577149
              rw-rw-rw-  UNDOTBS1.258.691577151
              rw-rw-rw-  USERS.259.691577151
```

## lsof

Purpose

Lists the open files of the local clients.

Syntax and Description

  
`lsof` \[`--suppressheader`\] { `-G` `diskgroup` | `--dbname` `db` | `-C` `instance` }  

Table 12-22 lists the syntax options for the `lsof` command.

Table 12-22 Options for the lsof command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headings. |
| `-G` `diskgroup` | List files only from the specified disk group. |
| `--dbname` `db` | List files only from the specified database. |
| `-C` `instance` | List files only from the specified instance. |

Example

The following are examples of the `lsof` command. The first example lists the open files for the `data` disk group. The second example lists the open files for the Oracle ASM instance.

Example 12-24 Using the ASMCMD lsof command

```
ASMCMD [+] > lsof -G data
DB_Name  Instance_Name  Path                                          
orcl     orcl           +data/orcl/controlfile/current.260.691577263  
orcl     orcl           +data/orcl/datafile/example.265.691577295     
orcl     orcl           +data/orcl/datafile/sysaux.257.691577149      
orcl     orcl           +data/orcl/datafile/system.256.691577149      
orcl     orcl           +data/orcl/datafile/undotbs1.258.691577151    
orcl     orcl           +data/orcl/datafile/users.259.691577151       
orcl     orcl           +data/orcl/onlinelog/group_1.261.691577267    
orcl     orcl           +data/orcl/onlinelog/group_2.262.691577271    
orcl     orcl           +data/orcl/onlinelog/group_3.263.691577275    
orcl     orcl           +data/orcl/tempfile/temp.264.691577287 

ASMCMD [+] > lsof -C +ASM 
DB_Name  Instance_Name  Path
asmvol   +ASM           +data/VOLUME1.271.679226013
asmvol   +ASM           +data/VOLUME2.272.679227351
```

## mkalias

Purpose

Creates an alias for the specified system-generated filename.

Syntax and Description

`mkalias` `file` `alias`

Table 12-23 lists the syntax options for the `mkalias` command.

Table 12-23 Options for the mkalias command

| Option | Description |
| --- | --- |
| `file` | System-generated file name. |
| `alias` | Alias for the file name. |

`alias` must be in the same disk group as the system-generated file. Only one alias is permitted for each Oracle ASM file.

Example

The following example creates the `sysaux.f` alias for the fully qualified filename `+data/orcl/DATAFILE/SYSAUX.257.721811945`. Following the `mkalias` command, `ls` `--absolutepath` is run to check the results.

Example 12-25 Using the ASMCMD mkalias command

```
ASMCMD [+data/orcl/datafile] > mkalias SYSAUX.257.721811945 sysaux.f

ASMCMD [+data/orcl/datafile] > ls --absolutepath
none => EXAMPLE.265.721812093
+DATA/ORCL/DATAFILE/sysaux.f => SYSAUX.257.721811945
none => SYSTEM.256.721811945
none => UNDOTBS1.258.721811945
none => USERS.259.721811947
sysaux.f
```

## mkdir

Purpose

Creates Oracle ASM directories under the current directory.

Syntax and Description

`mkdir` `dir` \[`dir`...\]

Table 12-24 lists the syntax options for the `mkdir` command.

Table 12-24 Options for the mkdir command

| Option | Description |
| --- | --- |
| `dir` | Directory name to create. |

The directory from which `mkdir` is run can be a system-created or user-created directory. You cannot create a directory at the root (+) level.

Example

The following is an example of the `mkdir` command. The example creates the directories `subdir1` and `subdir2` at the disk group level in the disk group `data`.

Example 12-26 Using the ASMCMD mkdir command

```
ASMCMD [+data] > mkdir subdir1 subdir2

ASMCMD [+data] > ls
ASM/
ORCL/
subdir1/
subdir2/
```

## pwd

Purpose

Displays the absolute path of the current directory.

Syntax and Description

`pwd`

Example

The following is an example of the `pwd` command. The example displays the current directory.

Example 12-27 Using the ASMCMD pwd command

```
ASMCMD [+data/orcl/datafile] > pwd
+data/orcl/datafile
```

## rm

Purpose

Deletes the specified Oracle ASM files and directories.

Syntax and Description

`rm [-f|-r]` `pattern` \[`pattern`...\]

Table 12-25 lists the syntax options for the `rm` command.

Table 12-25 Options for the rm command

| Option | Description |
| --- | --- |
| `-r` | Recursively deletes files and subdirectories. |
| `-f` | Forces the deletion of files and subdirectories. |
| `pattern` | Name of a file, directory, or wildcard pattern. |

If `pattern` is a file or alias, then the `rm` command can delete the file or alias only if it is not currently in use. If `pattern` is a directory, then the `rm` command can delete it only if it is empty (unless the `-r` flag is used) and it is not a system-generated directory. If `pattern` is an alias, then the `rm` command deletes both the alias and the file to which the alias refers. To delete only an alias and retain the file that the alias references, use the `rmalias` command.

Note:

When you delete all of the files in a system-created directory, the directory is removed. If the parent directories are empty, all of the parent directories are also removed.

`pattern` can contain wildcard characters. See ["Wildcard Characters"](asm_util001.md).

If you use a wildcard, the `rm` command deletes all of the matches except nonempty directories, unless you use the `-r` flag. To recursively delete, use the `-r` flag. With `-r` option you can delete a nonempty directory, including all files and directories in it and in the entire directory tree underneath it. If you use the `-r` flag or a wildcard character, then the `rm` command prompts you to confirm the deletion before proceeding, unless you specify the `-f` flag.If a wildcard character matches an alias or a system-generated file that has an alias, then both the alias and the system-generated file that it references are deleted. When using the `-r` flag to delete an alias that matches a wildcard pattern, either the alias or the system-generated file that has an alias must be present in the directory in which you run the `rm` command.

For example, if you have a user alias, `+data/dir1/file.alias` that points to `+data/orcl/DATAFILE/System.256.146589651`, then running the `rm -r +data/dir1` command removes the `+data/dir1/file.alias` and `+data/orcl/DATAFILE/System.256.146589651`.

Example

The following are examples of the `rm` command. The first example deletes the `myexamples.bak` file. The second example removes the `subdir2` directory and its contents.

Example 12-28 Using the ASMCMD rm command

```
ASMCMD [+data/orcl/datafile] > rm myexamples.bak

ASMCMD [+data] > rm -r subdir2
You may delete multiple files and/or directories. 
Are you sure? (y/n) y
```

## rmalias

Purpose

Removes the specified aliases, retaining the files that the aliases reference.

Syntax and Description

`rmalias [-r]` `alias` \[`alias`...\]

Table 12-26 lists the syntax options for the `rmalias` command.

Table 12-26 Options for the rmalias command

| Option | Description |
| --- | --- |
| `-r` | Recursively removes aliases. |
| `alias` | Alias for the file name or directory. |

The `-r` flag enables you to remove all of the aliases in the current directory and in the entire directory tree beneath the current directory. If any user-created directories become empty after deleting aliases, they are also deleted. Files and directories created by the system are not deleted.

Example

The following is an example of the `rmalias` command. The example deletes the alias `sysaux.f`, retaining the data file that it references.

Example 12-29 Using the ASMCMD rmalias command

```
ASMCMD [+data/orcl/datafile] > rmalias sysaux.f
```
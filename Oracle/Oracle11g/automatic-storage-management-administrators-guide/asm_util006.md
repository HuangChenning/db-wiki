---
title: ASMCMD File Access Control Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util006.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD Oracle ASM File Access Control commands. For information about Oracle ASM File Access Control, see ["Managing Oracle ASM File Access Control for Disk Groups"](asmdiskgrps.md).

Table 12-53 provides a summary of ASMCMD Oracle ASM File Access Control commands.

Table 12-53 Summary of ASMCMD file access control commands

| Command | Description |
| --- | --- |
| chgrp | Changes the user group of a file or list of files. |
| chmod | Changes permissions of a file or list of files. |
| chown | Changes the owner of a file or list of files. |
| groups | Lists the user groups to which a user belongs. |
| grpmod | Adds or removes users from an existing user group. |
| lsgrp | Lists user groups. |
| lsusr | Lists users in a disk group. |
| mkgrp | Creates a new user group. |
| mkusr | Adds a user to disk group. |
| passwd | Changes the password of a user. |
| rmgrp | Deletes a user group. |
| rmusr | Deletes a user from a disk group. |

## chgrp

Purpose

Changes the user group of a file or list of files.

Syntax and Description

  
`chgrp` `usergroup` `file` \[`file`...\]  

Table 12-54 lists the syntax options for the `chgrp` command.

Table 12-54 Options for the chgrp command

| Option | Description |
| --- | --- |
| `usergroup` | Name of the user group. |
| `file` | Name of a file. |

Only the file owner or the Oracle ASM administrator can use this command. If the user is the file owner, then the user must also be either the owner or a member of the group for this command to succeed.

This command accepts a file name or multiple file names separated by spaces.

Examples

The following are examples of the `chgrp` command that change the Oracle ASM user group of the specified files.

Example 12-56 Using the ASMCMD chgrp command

```
ASMCMD [+] > chgrp asm_data +data/orcl/controlfile/Current.260.684924747

ASMCMD [+fra/orcl/archivelog/flashback] > chgrp asm_fra log_7.264.684968167 log_8.265.684972027
```

## chmod

Purpose

Changes permissions of a file or list of files.

Syntax and Description

  
`chmod` `mode` `file` \[`file`...\]  

`mode` can be one of the following forms:

- { `ugo` | `ug` | `uo` | `go` | `u` | `g` | `o` | `a` } { `+` | `-` } { `r` | `w` | `rw` }
	`a` specifies permissions for all users, `u` specifies permissions for the owner of the file, `g` specifies the group permissions, and `o` specifies permissions for other users.
- { `0` | `4` | `6` } { `0` | `4` | `6` } { `0` | `4` | `6` }
	The first digit specifies `owner` permissions, the second digit specifies `group` permissions, and the third digit specifies `other` permissions.

Table 12-55 lists the syntax options for the `chmod` command.

Table 12-55 Options for the chmod command

| Option | Description |
| --- | --- |
| `6` | Read write permissions |
| `4` | Read only permissions |
| `0` | No permissions |
| `u` | Owner permissions, used with `r` or `w` |
| `g` | Group permissions, used with `r` or `w` |
| `o` | Other user permissions, used with `r` or `w` |
| `a` | All user permissions, used with `r` or `w` |
| `+` | Add a permission, used with `r` or `w` |
| `-` | Removes a permission, used with `r` or `w` |
| `r` | Read permission |
| `w` | Write permission |
| `file` | Name of a file |

This command accepts a file name or multiple file names separated by spaces. The specified files must be closed.

You can only set file permissions to read-write, read-only, and no permissions. You cannot set file permissions to write-only.

To view the permissions on a file, use the ASMCMD `ls` command with the `--permission` option. See ["ls"](asm_util003.md).

Examples

The following are examples of the `chmod` command that change the permissions of the specified files.

Example 12-57 Using the ASMCMD chmod command

```
ASMCMD [+fra/orcl/archivelog/flashback] > chmod ug+rw log_7.264.684968167 log_8.265.684972027

ASMCMD [+fra/orcl/archivelog/flashback] > chmod 640 log_7.264.684968167 log_8.265.684972027

ASMCMD [+] > ls --permission +fra/orcl/archivelog/flashback
User      Group      Permission  Name
grid      asm_fra     rw-r-----  log_7.264.684968167
grid      asm_fra     rw-r-----  log_8.265.684972027
```

## chown

Purpose

Changes the owner of a file or list of files.

Syntax and Description

  
`chown` `user` `[``:``usergroup` `]` `file` \[`file`...\]  

Table 12-56 lists the syntax options for the `chown` command.

Table 12-56 Options for the chown command

| Option | Description |
| --- | --- |
| `user` | The name of the user that becomes the new owner. |
| `usergroup` | Name of the user group to which the user belongs. |
| `file` | Name of a file. |

`user` typically refers to the user that owns the database instance home. Oracle ASM File Access Control uses the operating system (OS) name to identify a database.

This command accepts a file name or multiple file names separated by spaces. The specified files must be closed.

Only the Oracle ASM administrator can use this command.

Examples

The following are examples of the `chown` command that change the owner of the specified files to the `oracle1` operating system user.

Example 12-58 Using the ASMCMD chown command

```
ASMCMD [+fra/orcl/archivelog/flashback] > chown oracle1 log_7.264.684968167 log_8.265.684972027

ASMCMD [+fra/orcl/archivelog/flashback] > chown oracle1:asm_fra log_9.264.687650269
```

## groups

Purpose

Lists all the user groups to which the specified user belongs.

Syntax and Description

  
`groups` `diskgroup` `user`  

Table 12-57 lists the syntax options for the `groups` command.

Table 12-57 Options for the groups command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user belongs. |
| `user` | Name of the user. |

Examples

The following is an example of the `groups` command that displays the user groups of the `data` disk group to which the `oracle1` user belongs.

Example 12-59 Using the ASMCMD groups command

```
ASMCMD [+] > groups data oracle1
asm_data
```

## grpmod

Purpose

Adds or removes operating system (OS) users to and from an existing Oracle ASM user group.

Syntax and Description

  
`grpmod` { `--add` `|` `--delete` } `diskgroup` `usergroup` `user` `[``user`...\]  

Table 12-58 lists the syntax options for the `grpmod` command.

Table 12-58 Options for the grpmod command

| Option | Description |
| --- | --- |
| `--add` | Specifies to add users to the user group. |
| `--delete` | Specifies to delete users from the user group. |
| `diskgroup` | Name of the disk group to which the user group belongs. |
| `usergroup` | Name of the user group. |
| `user` | Name of the user to add or remove from the user group. |

Only the owner of the user group can use this command. The command requires the SYSASM privilege to run.

This command accepts an operating system user name or multiple user names separated by spaces. The operating system users are typically owners of a database instance home.

Examples

The following are examples of the `grpmod` command. The first example adds the `oracle1` and `oracle2` users to the `asm_fra` user group of the `fra` disk group. The second example removes the `oracle2` user from the `asm_data` user group of the `data` disk group.

Example 12-60 Using the ASMCMD grpmod command

```
ASMCMD [+] > grpmod –-add fra asm_fra oracle1 oracle2

ASMCMD [+] > grpmod –-delete data asm_data oracle2
```

## lsgrp

Purpose

Lists all Oracle ASM user groups or only groups that match a specified pattern.

Syntax and Description

  
`lsgrp` \[`--suppressheader`\] `[-a]` \[ `-G` `diskgroup` \] \[ `pattern` `]`  

Table 12-59 lists the syntax options for the `lsgrp` command.

Table 12-59 Options for the lsgrp command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headings. |
| `-a` | Lists all columns. |
| `-G` `diskgroup` | Limits the results to the specified disk group name. |
| `pattern` | Displays the user groups that match the pattern expression. |

Examples

The following are examples of the `lsgrp` command. The first example displays a subset of information about the user groups whose name matches the `asm%` pattern. The second example displays all information about all the user groups.

Example 12-61 Using the ASMCMD lsgrp command

```
ASMCMD [+] > lsgrp asm%
DG_Name  Grp_Name   Owner
FRA      asm_fra    grid
DATA     asm_data   grid

ASMCMD [+] > lsgrp -a
DG_Name  Grp_Name   Owner     Members
FRA      asm_fra    grid      oracle1
DATA     asm_data   grid      oracle1 oracle2
```

## lsusr

Purpose

Lists Oracle ASM users in a disk group.

Syntax and Description

  
`lsusr` \[`--suppressheader`\] `[-a]` \[`-G` `diskgroup` \] \[ `pattern` \]  

Table 12-60 lists the syntax options for the `lsusr` command.

Table 12-60 Options for the lsusr command

| Option | Description |
| --- | --- |
| `-a` | List all users and the disk groups to which the users belong. |
| `--suppressheader` | Suppresses column headings. |
| `-G` `diskgroup` | Limits the results to the specified disk group name. |
| `pattern` | Displays the users that match the pattern expression. |

Examples

The following is an example of the `lsusr` command. The example lists users in the `data` disk group and also shows the operating system Id assigned to the user.

Example 12-62 Using the ASMCMD lsusr command

```
ASMCMD [+] > lsusr -G data
User_Num OS_ID OS_Name 
3        1001  grid
1        1021  oracle1
2        1022  oracle2
```

## mkgrp

Purpose

Creates a new Oracle ASM user group.

Syntax and Description

  
`mkgrp` `diskgroup` `usergroup` `[``user``]` `[``user`...\]  

Table 12-61 lists the syntax options for the `mkgrp` command.

Table 12-61 Options for the mkgrp command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user group is added. |
| `usergroup` | Name of the user group to add. 30 is the maximum number of characters. |
| `user` | Name of the database user to add to the user group. |

You can optionally specify a list of users to be included as members of the new user group.

Examples

The following is an example of the `mkgrp` command. This example creates the `asm_data` user group in the `data` disk group and adds the `oracle1` and `oracle2` users to the user group.

Example 12-63 Using the ASMCMD mkgrp command

```
ASMCMD [+] > mkgrp data asm_data oracle1 oracle2
```

## mkusr

Purpose

Adds an operating system (OS) user to a disk group.

Syntax and Description

  
`mkusr` `diskgroup` `user`  

Table 12-62 lists the syntax options for the `mkusr` command.

Table 12-62 Options for the mkusr command

| Option | Description |
| --- | --- |
| `diskgroup` | Specifies the name of the disk group to which the user is to be added. |
| `user` | Name of the user to add. |

The user to be added must be a valid operating system user. Only a user authenticated as `SYSASM` can run this command.

Examples

The following are examples of the `mkusr` command. The first example adds the `oracle1` user to the `data` disk group. The second example adds the `oracle2` user to the `fra` disk group.

Example 12-64 Using the ASMCMD mkusr command

```
ASMCMD [+] > mkusr data oracle1

ASMCMD [+] > mkusr fra oracle2
```

## passwd

Purpose

Changes the password of a user.

Syntax and Description

  
`passwd` `user`  

Table 12-63 lists the syntax options for the `passwd` command.

Table 12-63 Options for the passwd command

| Option | Description |
| --- | --- |
| `user` | Name of the user. |

An error is raised if the user does not exist in the Oracle ASM password file. The user is first prompted for the current password, then the new password. The command requires the SYSASM privilege to run.

Examples

The following is an example of the `passwd` command that changes the password of the `oracle2` user.

Example 12-65 Using the ASMCMD passwd command

```
ASMCMD [+] > passwd oracle2
Enter old password (optional): 
Enter new password: ******
```

## rmgrp

Purpose

Removes a user group from a disk group.

Syntax and Description

  
`rmgrp` `diskgroup` `usergroup`  

Table 12-64 lists the syntax options for the `rmgrp` command.

Table 12-64 Options for the rmgrp command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user group belongs. |
| `usergroup` | Name of the user group to delete. |

Removing a group might leave some files without a valid user group. To ensure that those files have a valid group, explicitly update those files to a valid user group. See "chgrp".

The command must be run by the owner of the user group and also requires the SYSASM privilege to run.

Examples

The following is an example of the `rmgrp` command that removes the `asm_data` user group from the `data` disk group.

Example 12-66 Using the ASMCMD rmgrp command

```
ASMCMD [+] > rmgrp data asm_data
```

## rmusr

Purpose

Deletes an operating system (OS) user from a disk group.

Syntax and Description

  
`rmusr` \[`-r`\] `diskgroup` `user`  

Table 12-65 lists the syntax options for the `rmusr` command.

Table 12-65 Options for the rmusr command

| Option | Description |
| --- | --- |
| `-r` | Removes all files in the disk group that the user owns at the same time that the user is removed. |
| `diskgroup` | Specifies the name of the disk group from which the user is to be deleted. |
| `user` | Name of the user to delete. |

The command requires the SYSASM privilege to run.

Examples

The following is an example of the `rmusr` command that removes the `oracle2` user from the `data` disk group.

Example 12-67 Using the ASMCMD rmusr command

```
ASMCMD [+] > rmusr data oracle2
```
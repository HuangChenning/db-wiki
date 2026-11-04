---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asmcmd-instance-commands.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic provides a summary of the ASMCMD instance management commands.

Some commands in this section affect the Grid Plug and Play (GPnP) profile, which is a resource in a clustered configuration. In an Oracle Restart configuration, the profile is actually located in a resource attribute, not the Grid Plug and Play (GPnP) profile. However, the functionality of the commands is the same for both configurations.

Note:

After a change has been made to the location of the password file, the following SQL statement should be executed to flush the password file metadata cache.

```
SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE
```

The location of the password file can be changed by running `orapwd`, or the ASMCMD `pwcopy`, `pwcreate`, `pwdelete`, `pwmove`, or `pwset` command.

See Also:

[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

Table 10-18 lists the Oracle ASM instance management commands with brief descriptions.

Table 10-18 Summary of ASMCMD instance management commands

| Command | Description |
| --- | --- |
| dsget | Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| dsset | Sets the disk discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| lsct | Lists information about current Oracle ASM clients. |
| lsop | Lists the current operations on a disk group or Oracle ASM instance. |
| lspwusr | Lists the users from an Oracle ASM password file. |
| orapwusr | Adds, drops, or changes an Oracle ASM password user. |
| pwcopy | Copies a password file to the specified location. |
| pwcreate | Creates a password file at the specified location. |
| pwdelete | Deletes a password file at the specified location. |
| pwget | Returns the location of the password file. |
| pwmove | Moves the location of the password file. |
| pwset | Sets the location of the password file. |
| showclustermode | Displays the current mode of the Oracle ASM cluster. |
| showclusterstate | Displays the current state of the cluster. |
| showpatches | Lists the patches applied to the Oracle Grid Infrastructure home. |
| showversion | Displays the Oracle ASM cluster release and software patch levels. |
| shutdown | Shuts down an instance. |
| spbackup | Backs up an Oracle ASM SPFILE. |
| spcopy | Copies an Oracle ASM SPFILE. |
| spget | Retrieves the location of the Oracle ASM SPFILE. |
| spmove | Moves an Oracle ASM SPFILE. |
| spset | Sets the location of the Oracle ASM SPFILE. |
| startup | Starts up an instance. |

### dsget

Purpose

Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients.

Syntax and Description

```
dsget [ --normal | --parameter | --profile [-f] ]
```

The syntax options for the `dsget` command are described in Table 10-19.

Table 10-19 Options for the dsget command

| Option | Description |
| --- | --- |
| `--normal` | Retrieves the discovery string from the Grid Plug and Play (GPnP) profile and the one that is set in the Oracle ASM instance. It returns one row each for the profile and parameter setting. This is the default setting. |
| `--parameter` | Retrieves the `ASM_DISKSTRING` parameter setting of the Oracle ASM instance. |
| `--profile` \[`-f`\] | Retrieves the discovery string from the GPnP profile. If `-f` is specified with `--profile`, `dsget` retrieves the discovery string from the local GPnP profile. |

Example

The following example uses `dsget` to retrieve the current discovery diskstring value from the GPnP profile and the `ASM_DISKSTRING` parameter.

Example 10-25 Using the ASMCMD dsget command

```
ASMCMD [+] > dsget
profile: /devices1/disk*
parameter: /devices2/disk*
```

### dsset

Purpose

Sets the discovery diskstring value that is used by the Oracle ASM instance and its clients.

The specified diskstring must be valid for existing mounted disk groups. The updated value takes effect immediately.

Syntax and Description

```
dsset [ --normal | --parameter | --profile [-f] ] diskstring
```

The syntax options for the `dsset` command are described in Table 10-20.

Table 10-20 Options for the dsset command

| Option | Description |
| --- | --- |
| `--normal` | Sets the discovery string in the Grid Plug and Play (GPnP) profile and in the Oracle ASM instance. The update occurs after the Oracle ASM instance has successfully validated that the specified discovery string has discovered all the necessary disk groups and voting files. This command fails if the instance is not using a server parameter file (SPFILE).  This is the default setting. |
| `--parameter` | Specifies that the diskstring is updated in memory after validating that the discovery diskstring discovers all the current mounted disk groups and voting files. The diskstring is not persistently recorded in either the SPFILE or the GPnP profile. |
| `--profile` \[`-f`\] | Specifies the discovery diskstring that is pushed to the GPnP profile without any validation by the Oracle ASM instance, ensuring that the instance can discover all the required disk groups. The update is guaranteed to be propagated to all the nodes that are part of the cluster.  If `-f` is specified with `--profile`, the specified diskstring is pushed to the local GPnP profile without any synchronization with other nodes in the cluster. This command option updates only the local profile file. This option should only be used for recovery. The command fails if the Oracle Clusterware stack is running. |
| `diskstring` | Specifies the value for the discovery diskstring. |

For information about disk discovery and the discovery diskstring, see [Oracle ASM Disk Discovery](asm-disk-discovery.md).

Example

The following example uses `dsset` to set the current value of the discovery diskstring in the GPnP profile.

Example 10-26 Using the ASMCMD dsset command

```
ASMCMD [+] > dsset /devices1/disk*,/devices2/disk*
```

### lsct

Purpose

Lists information about current Oracle ASM clients from the `V$ASM_CLIENT` view. A client, such as Oracle Database or Oracle ASM Dynamic Volume Manager (Oracle ADVM), uses disk groups that are managed by the Oracle ASM instance to which ASMCMD is currently connected.

Syntax and Description

```
lsct [--suppressheader] [-g] disk_group
```

The following table lists the options for the `lsct` command.

Table 10-21 Options for the lsct command

| Option | Description |
| --- | --- |
| `-g` | Selects from the `GV$ASM_CLIENT` view. `GV$ASM_CLIENT.INST_ID` is included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `disk_group` | Specifies the disk group. |

Client information is only listed for the specified disk group.

Example

The following example displays information about the clients that are accessing the `data` disk group.

Example 10-27 Using the ASMCMD lsct command

```
ASMCMD [+] > lsct data
DB_Name  Status    Software_Version  Compatible_version  Instance_Name  Disk_Group
+ASM     CONNECTED       19.0.0.0.0          19.0.0.0.0  +ASM           DATA
asmvol   CONNECTED       19.0.0.0.0          19.0.0.0.0  +ASM           DATA
orcl     CONNECTED       19.0.0.0.0          19.0.0.0.0  orcl           DATA
```

### lsop

Purpose

Lists the current operations on a disk group in an Oracle ASM instance.

Syntax and Description

```
lsop
```

`lsop` displays information from the `V$ASM_OPERATION` view.

Example

The following are examples of the `lsop` command. The examples list operations on the disk groups of the current Oracle ASM instance.

Example 10-28 Using the ASMCMD lsop command

```
ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power
DATA        REBAL    WAIT   2   

ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power  
FRA         REBAL    REAP   3
```

### lspwusr

Purpose

List the users from the local Oracle ASM password file.

Syntax and Description

```
lspwusr [--suppressheader]
```

Table 10-22 lists the options for the `lspwusr` command.

Table 10-22 Options for the lspwusr command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headers from the output. |

Examples

The following is an example of the `lspwusr` example. The example lists the current users in the local Oracle ASM password file.

Example 10-29 Using the ASMCMD lspwusr command

```
ASMCMD [+] > lspwusr
Username sysdba sysoper sysasm 
     SYS   TRUE    TRUE   TRUE 
 ASMSNMP   TRUE   FALSE  FALSE
```

### orapwusr

Purpose

Add, drop, or modify an Oracle ASM password file user.

Syntax and Description

```
orapwusr { --add | --modify | --delete | grant {sysasm|sysdba|sysoper} | 
           --revoke {sysasm|sysdba|sysoper} } user
```

Table 10-23 lists the options for the `orapwusr` command.

Table 10-23 Options for the orapwusr command

| Option | Description |
| --- | --- |
| `--add` | Adds a user to the password file. Also prompts for a password. |
| `--modify` | Changes the password for the specified user. |
| `--delete` | Drops a user from the password file. |
| `--grant` `role` | Sets the role for the user. The options are `sysasm`, `sysdba`, and `sysoper`. |
| `--revoke` `role` | Removes the role for the user. The options are `sysasm`, `sysdba`, and `sysoper`. |
| `user` | Name of the user to add, drop, or modify. |

`orapwusr` attempts to update passwords on all nodes in a cluster. This command requires the SYSASM privilege to run. A user logged in as SYSDBA cannot change its password using this command.

Examples

The following is an example of the `orapwusr` command. This example adds the `hruser` to the Oracle ASM password file.

Example 10-30 Using the ASMCMD orapwusr command

```
ASMCMD [+] > orapwusr --add hruser
```

### pwcopy

Purpose

Copies an Oracle ASM or database instance password file to the specified location.

Syntax and Description

```
pwcopy [--asm |--dbuniquename string] source  destination [-f]
```

Table 10-24 lists the options for the `pwcopy` command.

Table 10-24 Options for the pwcopy command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `source` | The `source` value identifies the location where the existing password file is located. |
| `destination` | The `destination` value identifies the location where you want to copy the password file. |
| `-f` | The `—f` option enables the password file to be copied without any checks. |

`pwcopy` copies a password file from one disk group to another, from the operating system to a disk group, or from a disk group to the operating system. If the `—f` option is specified, then the password file can be copied to the same disk group.

Either `–-asm` or - `-dbuniquename` is required to identify a CRSD resource. When either `–-asm` or - `-dbuniquename` is included in the `pwcopy` command, the target file is set to the current password file.

The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be copied.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example copies an Oracle ASM password file in one disk group to a different disk group. Because the `pwcopy` command includes the `--asm` option, the target file (`+fra/orapwasm_new`) is set to the current password file.

Example 10-31 Using the ASMCMD pwcopy command

```
ASMCMD [+] > pwcopy --asm +DATA/orapwasm +FRA/orapwasm_new
copying +DATA/orapwasm -> +FRA/orapwasm_new
```

### pwcreate

Purpose

Note:

Do not use `pwcreate` to create a new Oracle ASM password file when Oracle ASM is configured in a cluster. If the Oracle ASM password file is inaccessible in a cluster configuration, you must restore the password file using an available backup rather than create a new file. For articles about recreating a shared Oracle ASM password file in a cluster, such as document 1929673.1, refer to articles at [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)).

Creates an Oracle ASM or Oracle Database instance password file at the specified location.

Syntax and Description

```
pwcreate { --asm  |--dbuniquename string } [-f] [--format format] file_path [sys_password]
```

Table 10-25 lists the options for the `pwcreate` command.

Table 10-25 Options for the pwcreate command

| Option | Description |
| --- | --- |
| `--asm` | Associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | Specifies the Oracle Database unique name associated with the password file. |
| `-f` | Forces a deletion of the existing password file and creates a new password file. |
| `--format` `format` | Specifies the format in which the password is created. Values are `12` and `12.2`. If not specified, then `12.2` is the default value. |
| `file_path` | Specifies the location where the password file is created. |
| `sys_password` | Specifies the initial `SYS` password. If this option is omitted, then the you are prompted for the password. |

`pwcreate` creates a password file in the disk group specified by `file_path`. The initial `SYS` password is specified by `sys_password`.

Either `–-asm` or - `-dbuniquename` is required. The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be located.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

For additional information, refer to [Managing a Shared Password File in a Disk Group](authenticate-access-asm-instance.md).

Example

The following example creates an Oracle Database password file in an Oracle ASM disk group.

Example 10-32 Using the ASMCMD pwcreate command

```
ASMCMD [+] > pwcreate –-dbuniquename orcl '+data/ORCL/orapwdb'
Enter password for SYS:
```

### pwdelete

Purpose

Deletes an Oracle ASM or database instance password file.

Syntax and Description

```
pwdelete { --asm |--dbuniquename string | file_path }
```

Table 10-26 lists the options for the `pwdelete` command.

Table 10-26 Options for the pwdelete command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `file_path` | The `file_path` value identifies the location where the password file is located. |

`pwdelete` deletes the specified password file. Either `–-asm` or - `-dbuniquename` is required to identify a CRSD resource and to remove the password location from the CRSD resource.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example deletes the specified password file from a disk group.

Example 10-33 Using the ASMCMD pwdelete command

```
ASMCMD [+] > pwdelete +FRA/orapwasm_bak
```

### pwget

Purpose

Returns the location of the password file for the Oracle ASM or database instance.

Syntax and Description

```
pwget { --asm | --dbuniquename string }
```

Table 10-27 lists the options for the `pwget` command.

Table 10-27 Options for the pwget command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |

`pwget` returns the location of the password file for the Oracle ASM instance identified by `–-asm` or the database instance identified by - `-dbuniquename`.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example returns the location of the Oracle ASM password file.

Example 10-34 Using the ASMCMD pwget command

```
ASMCMD [+] > pwget --asm
+DATA/orapwasm
```

### pwmove

Purpose

Moves an Oracle ASM or database instance password file to the specified location.

Syntax and Description

```
pwmove { --asm | --dbuniquename string } source  destination [-f]
```

Table 10-28 lists the options for the `pwmove` command.

Table 10-28 Options for the pwmove command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `source` | The `source` value identifies the location where the existing password file is located. |
| `destination` | The `destination` value identifies the location where you want to move the password file. |
| `-f` | The `—f` option clears the password file for any associated resource and the new file is registered. |

`pwmove` moves a password file from one disk group to another, from the operating system to a disk group, or from a disk group to the operating system. If the `—f` option is specified, then a password file can be moved to a file in the same disk group.

Either `–-asm` or - `-dbuniquename` is required to identify a CRSD resource.

The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be moved.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example moves a password file from one disk group to another disk group.

Example 10-35 Using the ASMCMD pwmove command

```
ASMCMD [+] > pwmove --asm +FRA/orapwasm_bak +DATA/orapwasm
moving +FRA/orapwasm_bak -> +DATA/orapwasm
```

### pwset

Purpose

Sets the location of the password file for an Oracle ASM or database instance.

Syntax and Description

```
pwset { --asm  | --dbuniquename string } file_path
```

Table 10-29 lists the options for the `pwset` command.

Table 10-29 Options for the pwset command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `file_path` | The `file_path` value identifies the location where the password file is located. |

`pwset` sets the location of the password file for an Oracle ASM or database instance to the value specified by `file_path`. Either - `-dbuniquename` or `–-asm` is required to identify a CRSD resource.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example sets the location of the Oracle ASM password file in a disk group.

Example 10-36 Using the ASMCMD pwset command

```
ASMCMD [+] > pwset --asm +DATA/orapwasm
```

### showclustermode

Purpose

Displays the current mode of the Oracle ASM cluster.

Syntax and Description

```
showclustermode
```

`showclustermode` displays the mode that the Oracle ASM cluster is currently in. The possible return values are ASM cluster: Flex mode enabled or ASM cluster: Flex mode disabled.

Example

The following example shows the use of the `showclustermode` command.

Example 10-37 Using the ASMCMD showclustermode command

```
ASMCMD [+] > showclustermode
ASM cluster : Flex mode disabled
```

### showclusterstate

Purpose

Displays the current state of the cluster.

Syntax and Description

```
showclusterstate
```

`showclusterstate` displays the state that the Oracle ASM cluster is currently in. The possible values returned are Normal, In Rolling Patch, or In Rolling Upgrade mode.

Example

This example shows the use of the `showclusterstate` command.

Example 10-38 Using the ASMCMD showclusterstate command

```
ASMCMD [+] > showclusterstate
```

### showpatches

Purpose

Lists the patches applied on the Oracle Grid Infrastructure home.

Syntax and Description

```
showpatches [-l]
```

The following table lists the options for the `showpatches` command.

Table 10-30 Options for the showpathches command

| Option | Description |
| --- | --- |
| `—l` | Displays all details about the patches. |

`showpatches` lists the patches that have been applied to the Oracle Grid Infrastructure home.

Example

This example shows the use of the `showpatches` command.

Example 10-39 Using the ASMCMD showpatches command

```
ASMCMD [+] > showpatches -l
Oracle ASM release patch level is [0] and no patches have been applied on the local node. The release patch string is [18.1.0.0.0].
```

### showversion

Purpose

Displays the patch levels of the Oracle ASM cluster release and software.

Syntax and Description

```
showversion [[[--releasepatch] [--softwarepatch]] | [--active]]
```

The following table lists the options for the `showversion` command.

Table 10-31 Options for the showversion command

| Option | Description |
| --- | --- |
| `--releasepatch` | Displays the cluster level patch version.  Use `asmcmd` `showversion` `--active` instead. |
| `--softwarepatch` | Displays the patch level on the local node.  Use `asmcmd` `showpatches` `-l` instead. |
| `--active` | Displays the active version and active patch level |

`showversion` displays the Oracle ASM cluster release and software patch levels. The release and software patch options may differ depending whether the Oracle ASM or Oracle Grid Infrastructure home is being patched.

Note:

The `releasepatch` and `softwarepatch` options may be different when the Oracle Grid Infrastructure or Oracle ASM home is being patched. When in normal mode, the options should be same. When there is no Oracle ASM instance connected, release patch information is not displayed.

Example

This example shows the use of the `showversion` command.

Example 10-40 Using the ASMCMD showversion command

```
ASMCMD [+] > showversion --active
Oracle ASM active version on the cluster is [19.0.0.0.0]. The cluster upgrade state is [NORMAL]. The cluster active patch level is [0].
```

### shutdown

Purpose

Shuts down an instance.

Syntax and Description

```
shutdown [--target target_instance] [--normal | --abort|--immediate ]
```

Table 10-32 lists the options for the `shutdown` command.

Table 10-32 Options for the shutdown command

| Option | Description |
| --- | --- |
| `--target target_instance` | Specify the target instance. The value of `target_instance` could be either Oracle ASM (`ASM`), IOServer (`IOS`), or Oracle ASM proxy (`APX`) instance. |
| `--normal` | Shut down normal. This is the default action. |
| `--abort` | Shut down stopping all existing operations. |
| `--immediate` | Shut down immediately. |

The default target instance is determined by the `ORACLE_SID` environmental variable. The default action is a normal shutdown.

Oracle strongly recommends that you shut down all database instances that use the Oracle ASM instance and dismount all file systems mounted on Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes before attempting to shut down the Oracle ASM instance with the `--abort` option.

For more information about shutting down an Oracle ASM instance, see " [About Shutting Down an Oracle ASM Instance](admin-asm-instance.md) ".

Example

The following are examples of the `shutdown` command. The first example performs a shut down of the Oracle ASM instance with normal action. The second example performs a shut down with immediate action. The third example performs a shut down that stops all existing operations.

Example 10-41 Using the ASMCMD shutdown command

```
ASMCMD [+] > shutdown --target ASM --normal

ASMCMD [+] > shutdown --target ASM --immediate

ASMCMD [+] > shutdown --target ASM --abort
```

### spbackup

Purpose

Backs up an Oracle ASM SPFILE to a backup file.

Syntax and Description

```
spbackup source destination
```

Table 10-33 lists the options for the `spbackup` command.

Table 10-33 Options for the spbackup command

| Option | Description |
| --- | --- |
| `source` | Specifies the source file name. |
| `destination` | Specifies the destination file. |

`spbackup` should be used when you want to make single or multiple backups of an SPFILE in the same or a different disk group without creating an SPFILE in the target disk group.

Note the following about the use of `spbackup`:

- `spbackup` can back up an Oracle ASM SPFILE from a disk group to a disk group or to an operating system file.
- `spbackup` can back up an Oracle ASM SPFILE from an operating system file to a disk group.
- `spbackup` can back up an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.
- `spbackup` can make multiple backups of an Oracle ASM SPFILE in the same disk group.

`spbackup` does not affect the GPnP profile. The backup file that is created is not a special file type and is not identified as an SPFILE. This backup file cannot be copied with `spcopy`. To copy this backup file to and from a disk group, use the ASMCMD `cp` command.

To make a copy of a backup file in a disk group that is identified as an SPFILE file:

1. Use the ASMCMD `cp` command to copy the backup file from the disk group to an operating system file. See " [cp](asmcmd-file-commands.md) ".
2. Use the ASMCMD spcopy command to copy the operating system file to a disk group. See " spcopy ".

Example

The following are examples of the `spbackup` command. The first example backs up the SPFILE in the `data` disk group. The second example backs up the SPFILE from the `data` disk group to the `fra` disk group.

Example 10-42 Using the ASMCMD spbackup command

```
ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +DATA/spfileBackASM.bak

ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +FRA/spfileBackASM.bak
```

### spcopy

Purpose

Copies an Oracle ASM SPFILE from the source location to an SPFILE in the destination location.

Syntax and Description

```
spcopy [-u] source destination
```

Table 10-34 lists the options for the `spcopy` command.

Table 10-34 Options for the spcopy command

| Option | Description |
| --- | --- |
| `-u` | Updates the Grid Plug and Play (GPnP) profile. |
| `source` | Specifies the source file name. |
| `destination` | Specifies the destination. |

Note the following about the use of `spcopy`:

- `spcopy` can copy an Oracle ASM SPFILE from a disk group to a different disk group or to an operating system file.
- `spcopy` can copy an Oracle ASM SPFILE from an operating system file to a disk group.
- `spcopy` can copy an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.
- `spcopy` cannot make multiple copies of an Oracle ASM SPFILE in the same disk group. You can use `spbackup` for that purpose.

To update the GPnP profile, include the `-u` option with `spcopy`. You can also use `spset` to update the GPnP profile if `spcopy` is run without the `-u` option.

After copying the SPFILE and updating the GPnP profile, you must restart the instance with the SPFILE in the new location to use that SPFILE. When the Oracle ASM instance is running with the SPFILE in the new location, you can remove the source SPFILE.

To copy an Oracle ASM SPFILE into a disk group using `spcopy`, the `COMPATIBLE.ASM` attribute must be set to `11.2` or greater in the target disk group.

Example

The following are examples of the `spcopy` command. The first example copies the Oracle ASM SPFILE from the `data` disk group to the `fra` disk group. The second example copies the Oracle ASM SPFILE from the `data` disk group to an operating system location. The third example copies an Oracle ASM SPFILE from an operating system location to the `data` disk group and updates the GPnP profile with the `-u` option.

Example 10-43 Using the ASMCMD spcopy command

```
ASMCMD> spcopy  +DATA/asm/asmparameterfile/registry.253.721810181
                +FRA/spfileCopyASM.ora

ASMCMD> spcopy +DATA/asm/asmparameterfile/registry.253.721810181
                $ORACLE_HOME/dbs/spfileCopyASM.ora

ASMCMD> spcopy -u /oracle/product/11.2.0/grid/dbs/spfileTestASM.ora
                  +DATA/ASM/spfileCopyASM.ora
```

See Also:

- spset for information about using the ASMCMD `spset` command
- [About Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File](init-params-asm-instance.md) for information about copying and moving an Oracle ASM instance initialization parameter file after upgrading
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01315) for information about creating a server parameter file with the `CREATE SPFILE` SQL statement

### spget

Purpose

Retrieves the location of the Oracle ASM SPFILE from the Grid Plug and Play (GPnP) profile.

Syntax and Description

```
spget
```

The location retrieved by `spget` is the location in the GPnP profile, but not always the location of the SPFILE currently used. For example, the location could have been recently updated by `spset` or `spcopy` with the `-u` option on an Oracle ASM instance that has not been restarted. After the next restart of the Oracle ASM, this location points to the Oracle ASM SPFILE currently being used.

Example

The following is an example of the `spget` command that retrieves and displays the location of the SPFILE from the GPnP profile.

Example 10-44 Using the ASMCMD spget command

```
ASMCMD [+] > spget
+DATA/ASM/ASMPARAMETERFILE/registry.253.813507611
```

### spmove

Purpose

Moves an Oracle ASM SPFILE from source to destination and automatically updates the GPnP profile.

Syntax and Description

```
spmove source destination
```

Table 10-35 lists the options for the `spmove` command.

Table 10-35 Options for the spmove command

| Option | Description |
| --- | --- |
| `source` | Specifies the source file. |
| `destination` | Specifies the destination file. |

Note the following about the use of `spmove`:

- `spmove` can move an Oracle ASM SPFILE when the open instance is using a PFILE or a different SPFILE. After moving the SPFILE, you must restart the instance with the SPFILE in the new location to use that SPFILE.
- `spmove` cannot move an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.

For information about copying and moving an Oracle ASM instance initialization parameter file after upgrading, see " [About Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File](init-params-asm-instance.md) ".

To use `spmove` to move an Oracle ASM SPFILE into a disk group, the disk group attribute `COMPATIBLE.ASM` must be set to `11.2` or greater.

Example

The following are examples of the `spmove` command. The first example moves an Oracle ASM SPFILE from the `data` disk group to an operating system location. The second example moves an SPFILE from an operating system location to the `data` disk group.

Example 10-45 Using the ASMCMD spmove command

```
ASMCMD> spmove +DATA/spfileASM.ora
               /oracle/product/11.2.0/grid/dbs/spfileMoveASM.ora

ASMCMD> spmove /oracle/product/11.2.0/grid/dbs/spfile+ASM.ora
               +DATA/ASM/spfileMoveASM.ora
```

### spset

Purpose

Sets the location of the Oracle ASM SPFILE in the Grid Plug and Play (GPnP) profile.

Syntax and Description

```
spset location
```

Table 10-36 lists the options for the `spset` command.

Table 10-36 Options for the spset command

| Option | Description |
| --- | --- |
| `location` | Specifies the location of the Oracle ASM SPFILE. The location is the full path to the SPFILE. |

Example

The following is an example of the `spset` command that sets the location of the Oracle ASM SPFILE command in the `data` disk group.

Example 10-46 Using the ASMCMD spset command

```
ASMCMD> spset +DATA/asm/asmparameterfile/asmspfile.ora
```

### startup

Purpose

Starts up the default instance.

Syntax and Description

```
startup [--mount] [--nomount] [--restrict] [ --pfile pfile ]
```

Table 10-37 lists the options for the `startup` command.

Table 10-37 Options for the startup command

| Option | Description |
| --- | --- |
| `--mount` | Specifies a mount operation. This is the default action. |
| `--nomount` | Specifies no mount operation. |
| `--restrict` | Specifies restricted mode. |
| `--pfile` `pfile` | Oracle ASM initialization parameter file. |

This command starts up an instance specified by the `ORACLE_SID` environmental variable. The variable could be set to the Oracle ASM, IOServer, or APX proxy instance.

The default action for an Oracle ASM instance is a startup that mounts disk groups and enables Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes.

Example

The following is an example of the `startup` command that starts the Oracle ASM instance (`ORACLE_SID=+ASM`) without mounting disk groups and uses the `asm_init.ora` initialization parameter file.

Example 10-47 Using the ASMCMD startup command

```
ASMCMD> startup --nomount --pfile asm_init.ora
```

See Also:

- [About Mounting Disk Groups at Startup](admin-asm-instance.md) for information about disk groups that are mounted at startup time
- [About Starting Up an Oracle ASM Instance](admin-asm-instance.md) for more information about starting up an Oracle ASM instance
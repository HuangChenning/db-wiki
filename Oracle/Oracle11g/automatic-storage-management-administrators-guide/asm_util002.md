---
title: ASMCMD Instance Management Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util002.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD Oracle ASM instance management commands.

Some commands in this section affect the Grid Plug and Play (GPnP) profile, which is a resource in a clustered configuration. In an Oracle Restart configuration, the profile is actually located in a resource attribute, not the Grid Plug and Play (GPnP) profile. However, the functionality of the commands is the same for both configurations.

Table 12-4 provides a summary of the Oracle ASM instance management commands.

Table 12-4 Summary of ASMCMD instance management commands

| Command | Description |
| --- | --- |
| dsget | Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| dsset | Sets the disk discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| lsct | Lists information about current Oracle ASM clients. |
| lsop | Lists the current operations on a disk group or Oracle ASM instance. |
| lspwusr | Lists the users from an Oracle ASM password file. |
| orapwusr | Adds, drops, or changes an Oracle ASM password user. |
| shutdown | Shuts down an Oracle ASM instance. |
| spbackup | Backs up an Oracle ASM SPFILE. |
| spcopy | Copies an Oracle ASM SPFILE. |
| spget | Retrieves the location of the Oracle ASM SPFILE. |
| spmove | Moves an Oracle ASM SPFILE. |
| spset | Sets the location of the Oracle ASM SPFILE. |
| startup | Starts up an Oracle ASM instance. |

## dsget

Purpose

Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients.

Syntax and Description

`dsget` \[ `--normal` | `--parameter` | `--profile` \[`-f`\] \]

The syntax options for the `dsget` command are described in Table 12-5.

Table 12-5 Options for the dsget command

| Option | Description |
| --- | --- |
| `--normal` | Retrieves the discovery string from the Grid Plug and Play (GPnP) profile and the one that is set in the Oracle ASM instance. It returns one row each for the profile and parameter setting. This is the default setting. |
| `--parameter` | Retrieves the `ASM_DISKSTRING` parameter setting of the Oracle ASM instance. |
| `--profile` \[`-f`\] | Retrieves the discovery string from the GPnP profile. If `-f` is specified with `--profile`, `dsget` retrieves the discovery string from the local GPnP profile. |

Example

The following example uses `dsget` to retrieve the current discovery diskstring value from the GPnP profile and the `ASM_DISKSTRING` parameter.

Example 12-6 Using the ASMCMD dsget command

```
ASMCMD [+] > dsget
profile: /devices/disk*
parameter: /devices/disk*
```

## dsset

Purpose

Sets the discovery diskstring value that is used by the Oracle ASM instance and its clients.

The specified diskstring must be valid for existing mounted disk groups. The updated value takes effect immediately.

Syntax and Description

`dsset` \[ `--normal` | `--parameter` | `--profile` \[`-f`\] \] `diskstring`

The syntax options for the `dsset` command are described in Table 12-6.

Table 12-6 Options for the dsset command

| Option | Description |
| --- | --- |
| `--normal` | Sets the discovery string in the Grid Plug and Play (GPnP) profile and in the Oracle ASM instance. The update occurs after the Oracle ASM instance has successfully validated that the specified discovery string has discovered all the necessary disk groups and voting files. This command fails if the instance is not using a server parameter file (SPFILE).  This is the default setting. |
| `--parameter` | Specifies that the diskstring is updated in memory after validating that the discovery diskstring discovers all the current mounted disk groups and voting files. The diskstring is not persistently recorded in either the SPFILE or the GPnP profile. |
| `--profile` \[`-f`\] | Specifies the discovery diskstring that is pushed to the GPnP profile without any validation by the Oracle ASM instance, ensuring that the instance can discover all the required disk groups. The update is guaranteed to be propagated to all the nodes that are part of the cluster.  If `-f` is specified with `--profile`, the specified diskstring is pushed to the local GPnP profile without any synchronization with other nodes in the cluster. This command option updates only the local profile file. This option should only be used for recovery. The command fails if the Oracle Clusterware stack is running. |
| `diskstring` | Specifies the value for the discovery diskstring. |

For information about disk discovery and the discovery diskstring, see ["Oracle ASM Disk Discovery"](asmdiskgrps.md).

Example

The following example uses `dsset` to set the current value of the discovery diskstring in the GPnP profile.

Example 12-7 Using the ASMCMD dsset command

```
ASMCMD [+] > dsset /devices/disk*
```

## lsct

Purpose

Lists information about current Oracle ASM clients from the `V$ASM_CLIENT` view. A client, such as Oracle Database or Oracle ASM Dynamic Volume Manager (Oracle ADVM), uses disk groups that are managed by the Oracle ASM instance to which ASMCMD is currently connected.

Syntax and Description

`lsct` \[`--suppressheader`\] \[`-g`\] \[`diskgroup`\]

Table 12-7 lists the options for the `lsct` command.

Table 12-7 Options for the lsct command

| Option | Description |
| --- | --- |
| (none) | Displays information about current clients from the `V$ASM_CLIENT` view. |
| `-g` | Selects from the `GV$ASM_CLIENT` view. `GV$ASM_CLIENT.INST_ID` is included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `diskgroup` | Specifies the disk group. |

If `diskgroup` is specified, then only information about that disk group is listed.

Example

The following example displays information about the clients that are accessing the `data` disk group.

Example 12-8 Using the ASMCMD lsct command

```
ASMCMD [+] > lsct data
DB_Name  Status    Software_Version Compatible_version  Instance_Name  Disk_Group
+ASM     CONNECTED       11.2.0.2.0         11.2.0.0.0  +ASM           DATA
asmvol   CONNECTED       11.2.0.2.0         11.2.0.0.0  +ASM           DATA
orcl     CONNECTED       11.2.0.2.0         11.2.0.0.0  orcl           DATA
```

## lsop

Purpose

Lists the current operations on a disk group in an Oracle ASM instance.

Syntax and Description

  
`lsop`  

`lsop` displays information from the `V$ASM_OPERATION` view.

Example

The following are examples of the `lsop` command. The examples list operations on the disk groups of the current Oracle ASM instance.

Example 12-9 Using the ASMCMD lsop command

```
ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power
DATA        REBAL    WAIT   2   

ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power  
FRA         REBAL    REAP   3
```

## lspwusr

Purpose

List the users from the local Oracle ASM password file.

Syntax and Description

  
`lspwusr` \[`--suppressheader`\]  

Table 12-8 lists the options for the `lspwusr` command.

Table 12-8 Options for the lspwusr command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headers from the output. |

Examples

The following is an example of the `lspwusr` example. The example lists the current users in the local Oracle ASM password file.

Example 12-10 Using the ASMCMD lspwusr command

```
ASMCMD [+] > lspwusr
Username sysdba sysoper sysasm 
     SYS   TRUE    TRUE   TRUE 
 ASMSNMP   TRUE   FALSE  FALSE
```

## orapwusr

Purpose

Add, drop, or modify an Oracle ASM password file user.

Syntax and Description

  
`orapwusr` { { { `--add` | `--modify` \[`--password`\] }  
\[`--privilege` { `sysasm` | `sysdba` | `sysoper` } \] } | `--delete` } `user`  

Table 12-9 lists the options for the `orapwusr` command.

Table 12-9 Options for the orapwusr command

| Option | Description |
| --- | --- |
| `--add` | Adds a user to the password file. Also prompts for a password. |
| `--modify` | Changes a user in the password file. |
| `--password` | Prompts for and then changes the password of a user. |
| `--privilege` `role` | Sets the role for the user. The options are `sysasm`, `sysdba`, and `sysoper`. |
| `--delete` | Drops a user from the password file. |
| `user` | Name of the user to add, drop, or modify. |

`orapwusr` attempts to update passwords on all nodes in a cluster. The command requires the SYSASM privilege to run. A user logged in as SYSDBA cannot change its password using this command.

Examples

The following is an example of the `orapwusr` command. This example adds the `hruser` to the Oracle ASM password file with the role of the user set to SYSDBA.

Example 12-11 Using the ASMCMD orapwusr command

```
ASMCMD [+] > orapwusr --add --privilege sysdba hruser
```

## shutdown

Purpose

Shuts down an Oracle ASM instance.

Syntax and Description

  
`shutdown` \[`--normal` | `--abort` | `--immediate` \]  

Table 12-10 lists the options for the `shutdown` command.

Table 12-10 Options for the shutdown command

| Option | Description |
| --- | --- |
| `--normal` | Shut down normal. |
| `--abort` | Shut down aborting all existing operations. |
| `--immediate` | Shut down immediately. |

The default action is a normal shutdown if an option is not specified.

Oracle strongly recommends that you shut down all database instances that use the Oracle ASM instance and dismount all file systems mounted on Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes before attempting to shut down the Oracle ASM instance with the abort (`--abort`) option.

For more information about shutting down an Oracle ASM instance, see ["Shutting Down an Oracle ASM Instance"](asminst.md).

Example

The following are examples of the `shutdown` command. The first example performs a shut down of the Oracle ASM instance with normal action. The second example performs a shut down with immediate action. The third example performs a shut down that aborts all existing operations.

Example 12-12 Using the ASMCMD shutdown command

```
ASMCMD [+] > shutdown --normal

ASMCMD [+] > shutdown --immediate

ASMCMD [+] > shutdown --abort
```

## spbackup

Purpose

Backs ups an Oracle ASM SPFILE to a backup file.

Syntax and Description

  
`spbackup` `source` `destination`  

Table 12-11 lists the options for the `spbackup` command.

Table 12-11 Options for the spbackup command

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

1. Use the ASMCMD `cp` command to copy the backup file from the disk group to an operating system file. See ["cp"](asm_util003.md).
2. Use the ASMCMD spcopy command to copy the operating system file to a disk group. See "spcopy".

Example

The following are examples of the `spbackup` command. The first example backs up the SPFILE in the `data` disk group. The second example backs up the SPFILE from the `data` disk group to the `fra` disk group.

Example 12-13 Using the ASMCMD spbackup command

```
ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +DATA/spfileBackASM.bak

ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +FRA/spfileBackASM.bak
```

## spcopy

Purpose

Copies an Oracle ASM SPFILE from the source location to an SPFILE in the destination location.

Syntax and Description

  
`spcopy` \[`-u`\] `source` `destination`  

Table 12-12 lists the options for the `spcopy` command.

Table 12-12 Options for the spcopy command

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

To update the GPnP profile, include the `-u` option with `spcopy`. You can also use `spset` to update the GPnP profile if `spcopy` is run without the `-u` option. See "spset". For information about copying and moving an Oracle ASM instance initialization parameter file after upgrading, see ["Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File"](asminst.md).

After copying the SPFILE and updating the GPnP profile, you must restart the instance with the SPFILE in the new location to use that SPFILE. When the Oracle ASM instance is running with the SPFILE in the new location, you can remove the source SPFILE.

To copy an Oracle ASM SPFILE into a disk group using `spcopy`, the `COMPATIBLE.ASM` attribute must be set to 11.2 or greater in the target disk group.

See Also:

The `CREATE SPFILE` SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) for information about creating a server parameter file

Example

The following are examples of the `spcopy` command. The first example copies the Oracle ASM SPFILE from the `data` disk group to the `fra` disk group. The second example copies the Oracle ASM SPFILE from the `data` disk group to an operating system location. The third example copies an Oracle ASM SPFILE from an operating system location to the `data` disk group and updates the GPnP profile with the `-u` option.

Example 12-14 Using the ASMCMD spcopy command

```
ASMCMD> spcopy  +DATA/asm/asmparameterfile/registry.253.721810181
                +FRA/spfileCopyASM.ora

ASMCMD> spcopy +DATA/asm/asmparameterfile/registry.253.721810181
                $ORACLE_HOME/dbs/spfileCopyASM.ora

ASMCMD> spcopy -u /u01/oracle/product/11.2.0/grid/dbs/spfileTestASM.ora
                  +DATA/ASM/spfileCopyASM.ora
```

## spget

Purpose

Retrieves the location of the Oracle ASM SPFILE from the Grid Plug and Play (GPnP) profile.

Syntax and Description

  
`spget`  

The location retrieved by `spget` is the location in the GPnP profile, but not always the location of the SPFILE currently used. For example, the location could have been recently updated by `spset` or `spcopy` with the `-u` option on an Oracle ASM instance that has not been restarted. After the next restart of the Oracle ASM, this location points to the Oracle ASM SPFILE currently being used.

Example

The following is an example of the `spget` command that retrieves and displays the location of the SPFILE from the GPnP profile.

Example 12-15 Using the ASMCMD spget command

```
ASMCMD [+] > spget
+DATA/asm/asmparameterfile/registry.253.691575633
```

## spmove

Purpose

Moves an Oracle ASM SPFILE from source to destination and automatically updates the GPnP profile.

Syntax and Description

  
`spmove` `source` `destination`  

Table 12-13 lists the options for the `spmove` command.

Table 12-13 Options for the spmove command

| Option | Description |
| --- | --- |
| `source` | Specifies the source file. |
| `destination` | Specifies the destination file. |

Note the following about the use of `spmove`:

- `spmove` can move an Oracle ASM SPFILE when the open instance is using a PFILE or a different SPFILE. After moving the SPFILE, you must restart the instance with the SPFILE in the new location to use that SPFILE.
- `spmove` cannot move an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.

For information about copying and moving an Oracle ASM instance initialization parameter file after upgrading, see ["Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File"](asminst.md).

To use `spmove` to move an Oracle ASM SPFILE into a disk group, the disk group attribute `COMPATIBLE.ASM` must be set to 11.2 or greater.

Example

The following are examples of the `spmove` command. The first example moves an Oracle ASM SPFILE from the `data` disk group to an operating system location. The second example moves an SPFILE from an operating system location to the `data` disk group.

Example 12-16 Using the ASMCMD spmove command

```
ASMCMD> spmove +DATA/spfileASM.ora
               /u01/oracle/product/11.2.0/grid/dbs/spfileMoveASM.ora

ASMCMD> spmove /u01/oracle/product/11.2.0/grid/dbs/spfile+ASM.ora
               +DATA/ASM/spfileMoveASM.ora
```

## spset

Purpose

Sets the location of the Oracle ASM SPFILE in the Grid Plug and Play (GPnP) profile.

Syntax and Description

  
`spset` `location`  

Table 12-14 lists the options for the `spset` command.

Table 12-14 Options for the spset command

| Option | Description |
| --- | --- |
| `location` | Specifies the location of the Oracle ASM SPFILE. The location is the full path to the SPFILE. |

Example

The following is an example of the `spset` command that sets the location of the Oracle ASM SPFILE command in the `data` disk group.

Example 12-17 Using the ASMCMD spset command

```
ASMCMD> spset +DATA/asm/asmparameterfile/asmspfile.ora
```

## startup

Purpose

Starts up an Oracle ASM instance.

Syntax and Description

  
`startup` \[`--nomount`\] \[`--restrict`\] \[ `--pfile` `pfile` \]  

Table 12-15 lists the options for the `startup` command.

Table 12-15 Options for the startup command

| Option | Description |
| --- | --- |
| `--nomount` | Specifies no mount operation. |
| `--restrict` | Specifies restricted mode. |
| `--pfile` `pfile` | Oracle ASM initialization parameter file. |

The default action is a startup that mounts disk groups and enables Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes. For information about disk groups that are mounted at startup time, see ["About Mounting Disk Groups at Startup"](asminst.md).

For more information about starting up an Oracle ASM instance, see ["Starting Up an Oracle ASM Instance"](asminst.md).

Example

The following is an example of the `startup` command that starts the Oracle ASM instance without mounting disk groups and uses the `asm_init.ora` initialization parameter file.

Example 12-18 Using the ASMCMD startup command

```
ASMCMD> startup --nomount --pfile asm_init.ora
```
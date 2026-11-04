---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/manage-asm-asmca.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle ASM Configuration Assistant (ASMCA) provides utilities for managing Oracle ASM.

Oracle ASM Configuration Assistant (ASMCA) supports installing and configuring Oracle ASM instances, Oracle ASM disk groups, Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes, and Oracle Advanced Cluster File System (Oracle ACFS) file systems. In addition, you can use the ASMCA command-line interface.

This chapter discusses the following topics:

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-48112752-FEBD-4321-9A09-0F44CD9D9BDC) for information about managing Oracle ACFS and Oracle ADVM with ASMCA

Note:

Some ASMCA functionality and menu options are only available in specific environments, such as an Oracle RAC configuration. For details about a specific ASMCA page, access the online help provided with the Help button.

### Getting Started With the ASMCA GUI Tool

To start ASMCA, enter `asmca` at a command prompt inside the Oracle Grid Infrastructure home. For example:

`$` `asmca`

The GUI tool displays and attempts to connect to the Oracle ASM instance identified with the Oracle system identifier (SID) set to `+ASM`.

If ASMCA detects an Oracle ASM instance that is not running, then ASMCA prompts whether you want to start the instance.

To start the command-line ASMCA, see ASMCA Command-Line Interface.

Note:

Some ASMCA functionality and menu options are only available in specific environments, such as an Oracle RAC configuration. For details about a specific ASMCA page, access the online help provided with the Help button.

### Managing Instances and Disk Groups With ASMCA

This section contains the following topics:

- Creating Oracle ASM Instances with ASMCA
- Managing Disk Groups with ASMCA

Note:

Some ASMCA functionality and menu options are only available in specific environments, such as an Oracle RAC configuration. For details about a specific ASMCA page, access the online help provided with the Help button.

Note:

On Solaris and AIX, if you shut down the database instance using the `SHUTDOWN                     ABORT` command, volume device files are not removed.

#### Creating Oracle ASM Instances with ASMCA

Oracle ASM Configuration Assistant enables you to create an Oracle ASM instance if the Oracle ASM instance is not found on the host.

On the Create ASM page, you enter the `SYS` password for the administrator of the Oracle ASM instance and the password for the `ASMSNMP` user that can monitor this Oracle ASM instance. `ASMSNMP` is a less privileged user that is primarily used to monitor Oracle ASM instances.

You can select the listener with which to register this Oracle ASM instance. Click ASM Parameters to update the initialization parameters for the Oracle ASM instance.

When you can click ASM Parameters in the Create ASM page, you can update initialization parameters for an Oracle ASM instance on the Oracle ASM Configuration Assistant page.

See Also:

- [Initialization Parameters for Oracle ASM Instances](init-params-asm-instance.md) for information about Oracle ASM instance initialization parameters
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installing Oracle ASM
- [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=GINST) for information about reviewing database accounts and passwords

#### Managing Disk Groups with ASMCA

Oracle ASM Configuration Assistant enables you to configure or create Oracle ASM disk groups with the Configure ASM Disk Groups tab.

The disk group tab displays selected details about the disk group, such as name, size, free space, usable space, redundancy level, and state of the disk group.

You can right click a selected disk group in the screen to display the configuration options menu. The menu options enable you to:

- Add disks to and drop disks from the disk group
- Add, drop, and list quota groups.
- Add, drop, and move file groups.
- Edit the disk group attributes
- Manage templates for the disk group
- Create an Oracle ACFS file system on the disk group for database use
- Mount and dismount the disk group
- Drop the disk group
- Drop and clear Oracle ASM Filter Driver labels.

There are additional options for creating a disk group, mounting all disk groups, and dismounting all disk groups.

Oracle ASM Configuration Assistant enables you to create an Oracle ASM disk group by clicking Create on the Oracle ASM Configuration Assistant disk group page.

On the Create Disk Group page, you can enter a name for the disk group, select the redundancy level, change the disk discovery path to locate disks in a different directory, identify the disks to be in the disk group, enter a name for a failure group, and specify if the failure group is a quorum type.

A quorum failure group is a special type of failure group and disks in these failure groups do not contain user data and a quorum failure group is not considered when determining redundancy requirements with respect to user storage. However, a quorum failure group counts when mounting a disk group.

If Oracle ASM Filter Driver has been configured for your system, you can add Oracle ASM Filter Driver labels to disks or clear Oracle ASM Filter Driver labels from disks.

You can choose to show advanced options when creating a disk group. The advanced options section enables you to set additional options, such as disk group compatibility settings and allocation unit (AU) size. When you are finished with the create disk group specifications, click OK.

Note:

The disk group compatibility settings can only be advanced. You cannot revert to a lower compatibility setting after you advance the disk group compatibility settings.

Note:

The values for Free (GB) and Usable (GB) space are `0` if the disk group type is `FLEX` or `EXTEND`. The `0` value in this case means no value is given, not a zero amount in for Free (GB) and Usable (GB) space.

See Also:

- [Storing Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups](create-diskgroups.md) for information about quorum failure groups
- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASM Filter Driver
- [Disk Group Compatibility](diskgroup-compatibility.md) and [Overview of Disk Group Compatibility](diskgroup-compatibility.md) for information about disk group compatibility attributes and advancing disk group compatibility
- [Oracle ASM Disk Discovery](asm-disk-discovery.md) and [ASM\_DISKSTRING](init-params-asm-instance.md) for information about disk discovery
- [Administering Oracle ASM Disk Groups](admin-asm-diskgroups.md) for more information about managing disk groups
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN30171) for descriptions of disk group information displayed in the `V$ASM_DISKGROUP` view

### ASMCA Command-Line Interface

The ASMCA command-line interface provides non-GUI support for configuring Oracle ASM instances, Oracle ASM disk groups, volumes, and Oracle ACFS.

- Running ASMCA Command-Line
- ASMCA Commands for Instances and Disk Groups

#### Running ASMCA Command-Line

The syntax for running the ASMCA command-line tool is:

```
asmca -silent command_name [options]
```

Table 9-1 contains the options available with the `asmca` command-line tool.

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-48112752-FEBD-4321-9A09-0F44CD9D9BDC) for information about managing Oracle ACFS and Oracle ADVM with ASMCA commands

Table 9-1 Options for the ASMCA command-line tool

| Option | Description |
| --- | --- |
| `-silent` | Specifies to run `asmca` in command-line mode. |
| `command_name` | Specifies the command to run. The command can be any of the following:  - `-configureASM` - `-configureParameter` - `-createDiskGroup` - `-editDiskGroupAttributes` - `-addDisk` - `-createFileGroups` - `-dropFileGroups` - `—createQuotaGroups` - `-dropQuotaGroups` - `-createVolume` - `-createACFS` - `-createACFSSnapshot` - `-dropACFSSnapshot`  See ASMCA Commands for Instances and Disk Groups. |
| `options` | Specifies the options to run for a command. The options vary by command. See the individual commands described in ASMCA Commands for Instances and Disk Groups for the available options.  The following list describes the options that are common for multiple commands.  - `-help` 	Displays help for running ASMCA in silent mode. - `-asmsnmpPassword` `asmsnmp_password` 	The Oracle ASM monitor user (`ASMSNMP`) password. This is optional and only required when creating and migrating an Oracle ASM instance. - `-sysAsmPassword` `sysasm_password` 	The `SYSASM` password for Oracle ASM instance. This option is required. |

The following is an example of the `-help` option.

```
$ asmca -help
asmca [-silent] [-sysAsmPassword <SYS user password>] [-asmsnmpPassword <ASMSNMP password>] {<command> <options>}
Please refer to the manual for details.
You can enter one of the following commands:
...
```

#### ASMCA Commands for Instances and Disk Groups

This section describes the commands that can be run with ASMCA command-line to manage Oracle ASM objects.

- Configure an Oracle ASM Instance
- Configure Parameters for a Specified Instance
- Create a Disk Group
- Add a Disk to a Disk Group
- Edit Oracle ASM Disk Group Attributes
- Create Oracle ASM File Groups
- Drop Oracle ASM File Groups
- Create Oracle ASM Quota Groups
- Drop Oracle ASM Quota Groups

##### Configure an Oracle ASM Instance

\- `configureASM` configures or creates an Oracle ASM instance.

Syntax

```
asmca -silent
     -configureASM
       [-sysAsmPassword sysasm_password ]
       [-asmsnmpPassword asm_monitor_password ] 
       [ { -param paramname=paramvalue , ... } ]
       [ { -diskString discovery_path
        { -diskGroupName diskgroup
         { -disk disk_path [-diskName disk]  |
          -diskList disk_list 
              [-diskSize disk_size_MB] 
              [-failuregroup failure_group] 
              [-force|-noforce] 
              [-quorum|-noquorum]  }
       [-redundancy { HIGH | NORMAL | EXTERNAL } ] } ]
       [-au_size value]
       [-compatible.asm value ]
       [-compatible.rdbms value ]
       [-compatible.advm value ] }
       { -executeRootScript {MANUAL|ROOT|SUDO} |
         [-rootPassword root_password ] |
         [-sudoUser sudo_user] [-sudoUserPassword sudo_user_password] }
       [-asmNetworks asm_network]
```

Table 9-2 contains the options available with the - `configureASM` command.

Table 9-2 Options for the -configureASM command

| Option | Description |
| --- | --- |
| `-param` `paramname` `=` `paramvalue`,... | Specifies a list of initialization parameters with values for the Oracle ASM instance. |
| `-diskString` `discovery_path` | Specifies the Oracle ASM discovery string for locating disks. |
| `-diskGroupName` `diskgroup` | Specifies the name of the Oracle ASM disk group to create. |
| `-disk` `disk_path` | Specifies the full path of the disk device. |
| `-diskName` `disk` | Specifies a user-supplied disk name. |
| `-diskList` `disk_list` | Specifies a comma-delimited list of disk names to be added to the disk group. |
| `-diskSize` `disk_size_MB` | Specifies the size of the disk to use for Oracle ASM storage. |
| `-failuregroup` `failure_group` | Specifies the failure group name. |
| `-force` \| `-noforce` | Specifies where to force the use of the disk. |
| `-quorum` \| `-noquorum` | Specifies a quorum or standard failure group. |
| `-redundancy` { `HIGH` \| `NORMAL` \| `EXTERNAL` } | Specifies the redundancy setting for the Oracle ASM disk group. |
| `-au_size` | Specifies the allocation unit size (1,2,4,8,16,32,64) |
| `-compatible.asm` | Specifies the attribute setting. |
| `-compatible.rdbms` | Specifies the attribute setting. |
| `-compatible.advm` | Specifies the attribute setting. |
| `-executeRootScript {MANUAL\|ROOT\|SUDO}` | Executes the root script.  Specify `MANUAL` for a manual run, `ROOT` for the `root` password, or `SUDO` for the `sudo` password. |
| `-rootPassword root_password` | Specifies the password of the `root` user. |
| `-sudoUser sudo_user -sudoUserPassword sudo_user_password` | Runs `sudo` as the specified user with the specified password. |
| `-asmNetworks asm_network` | Specifies a comma separated list of Oracle ASM networks. Each network is specified in the form "interface\_name/subnet".  If not specified, then the existing private network is used as the Oracle ASM network. |

The following are additional parameters used for an Oracle Flex ASM configuration when Oracle Cluster Registry (OCR) is in Network Attached Storage (NAS): `-executeRootScript`, `-rootPassword`, `-sudoUser -sudoUserPassword`, and `-asmNetworks`

For additional options that are common to multiple commands, see Table 9-1.

Examples

To configure an Oracle ASM instance:

Example 9-1 Using asmca -silent -configureASM

```
asmca -silent
        -configureASM
          -diskString '/devices/disk*'
          –sysAsmPassword my_sysasm_password
          -asmsnmpPassword my_asmsnmp_passwd
```

##### Configure Parameters for a Specified Instance

`-configureParameter` modifies the parameters of the specified target instance.

Syntax

```
asmca -silent
          -configureParameter [-target {ASM|IOS|APX|ALL} ] 
          [{-param paramname=paramvalue , ... }]
          [-sysAsmPassword sysasm_password ]
```

Table 9-3 contains the options available with the - `configureParameter` command.

Table 9-3 Options for the -configureParameter command

| Option | Description |
| --- | --- |
| `-target {ASM\|IOS\|APX\|ALL}` | Specifies the target instance of the command. If no target is specified, the default is the Oracle ASM instance. |
| `-param` `paramname` `=` `paramvalue`,... | Specifies a list of initialization parameters with values for the Oracle ASM instance. |

For additional options that are common to multiple commands, see Table 9-1.

Examples

To configure parameters for a specified target instance:

Example 9-2 Using asmca -silent -configureParameter

```
asmca -silent
        -configureParameter 
            –param 
            asm_power_limit=3
        –sysAsmPassword my_sysasm_password
```

##### Create a Disk Group

\- `createDiskGroup` creates disk groups in an Oracle ASM instance.

Syntax

```
asmca -silent
     -createDiskGroup
       [ -diskString discovery_path ]
       { -diskGroupName diskgroup
         { -disk disk_path [-diskName disk]  |
          -diskList disk_list 
              [-diskSize disk_size_MB] 
              [-failuregroup failure_group] 
              [-force|-noforce] 
              [-quorum|-noquorum]  }
       [ -redundancy { HIGH | NORMAL | EXTERNAL } ] } ]
       [-au_size value]
       [-compatible.asm value ]
       [-compatible.rdbms value ]
       [-compatible.advm value ] }
       [-sysAsmPassword sysasm_password ]
```

Table 9-4 contains the options available with the - `createDiskGroup` command.

Table 9-4 Options for the -createDiskGroup command

| Option | Description |
| --- | --- |
| `-diskString` `discovery_path` | Specifies the Oracle ASM discovery string for locating disks. |
| `-diskGroupName` `diskgroup` | Specifies the name of the Oracle ASM disk group to create. |
| `-disk` `disk_path` | Specifies the full path of the disk device. |
| `-diskName` `disk` | Specifies a user-supplied disk name. |
| `-diskList` `disk_list` | Specifies a comma-delimited list of disk names to be added to the disk group. |
| `-diskSize` `disk_size_MB` | Specifies the size of the disk to use for Oracle ASM storage. |
| `-failuregroup` `failure_group` | Specifies the failure group name. |
| `-force` \| `-noforce` | Specifies where to force the use of the disk. |
| `-quorum` \| `-noquorum` | Specifies a quorum or standard failure group. |
| `-redundancy` { `HIGH` \| `NORMAL` \| `EXTERNAL` } | Specifies the redundancy setting for the Oracle ASM disk group. |
| `-au_size` | Specifies the allocation unit size (1,2,4,8,16,32,64) |
| `-compatible.asm` | Specifies the attribute setting. |
| `-compatible.rdbms` | Specifies the attribute setting. |
| `-compatible.advm` | Specifies the attribute setting. |

For additional options that are common to multiple commands, see Table 9-1.

For information about disk group compatibility attributes, see [Disk Group Compatibility](diskgroup-compatibility.md).

Examples

To create disk groups in an Oracle ASM instance:

Example 9-3 Using asmca -silent -createDiskGroup

```
$ asmca -silent -createDiskGroup
       -diskGroupName mynewdg
           -disk '/devices/diske*'
           -disk '/devices/diskk*'
       -redundancy NORMAL
       -au_size 64
       -compatible.asm '19.0.0.0.0'
       -compatible.rdbms '19.0.0.0.0'
       -compatible.advm '19.0.0.0.0'

DiskGroup mynewdg created successfully.
```

##### Edit Oracle ASM Disk Group Attributes

`-editDiskGroupAttributes` updates the Oracle ASM disk group attributes.

Syntax and Description

```
-editDiskGroupAttributes
      (-diskGroupName disk_group)
      (-attribute value)
```

The following table contains the options available with the `—editDiskGroupAttributes` command.

Table 9-5 Options for the -editDiskGroupAttributes command

| Option | Description |
| --- | --- |
| `-diskGroupName` `diskgroup` | Specifies the name of the Oracle ASM disk group to create. |
| `-attribute` `value` | Specifies the name and assigned value of an attribute. |

##### Add a Disk to a Disk Group

\- `addDisk` add disks to an existing disk group in an Oracle ASM instance.

Syntax

```
asmca -silent 
        -addDisk
         [ -diskString discovery_path ]
           {-diskGroupName diskgroup
            {-disk disk_path [-diskName disk]  |
             -diskList disk_list 
                [-diskSize disk_size_MB] 
                [-failuregroup failure_group] 
                [-force|-noforce] 
                [-quorum|-noquorum]  }
         [-sysAsmPassword sysasm_password ]
```

Table 9-6 contains the options available with the - `addDisk` command.

Table 9-6 Options for the -addDisk command

| Option | Description |
| --- | --- |
| `-diskString` `discovery_path` | Specifies the Oracle ASM discovery string for locating disks. |
| `-diskGroupName` `diskgroup` | Specifies the name of the Oracle ASM disk group to update. |
| `-diskList` `disk_list` | Specifies a comma-delimited list of disk names to be added to the disk group. |
| `-diskSize` `disk_size_MB` | Specifies the size of the disk to use for Oracle ASM storage. |
| `-failuregroup` `failure_group` | Specifies the failure group name. |
| `-force` \| `-noforce` | Specifies where to force the use of the disk. |
| `-quorum` \| `-noquorum` | Specifies a quorum or standard failure group. |

For additional options that are common to multiple commands, see Table 9-1.

Examples

To add disks to an existing disk group:

Example 9-4 Using asmca -silent -addDisk

```
asmca -silent
        -addDisk
          -diskGroupName mynewdg 
             -disk '/devices/diskl1'
             -disk '/devices/diskl2'

Disks added successfully to diskgroup mynewdg.
```

##### Create Oracle ASM File Groups

`-createFileGroups` creates Oracle ASM file groups.

Syntax and Description

```
-createFileGroups
     (-diskGroupName disk_group)
     (-fileGroupNames file_group_name_list)
     (-fileGroupUsages file_group_usages_list)
     (-fileGroupUsageIDs file_group_usagesID_list)
```

The following table contains the options available with the `—createFileGroups` command.

Table 9-7 Options for the -createFileGroups command

| Option | Description |
| --- | --- |
| `-diskGroupName` `disk_group` | Specifies the name of the Oracle ASM disk group. |
| `-fileGroupNames` `file_group_name_list` | Specifies a comma-delimited list of file group names to be added to the disk group. |
| `-fileGroupUsages` `file_group_usages_list` | Specifies a comma-delimited list of file group usage strings to be processed. |
| `-fileGroupUsagesIDs` `file_group_usagesID_list` | Specifies a comma-delimited list of file group usage IDs to be processed. |

##### Drop Oracle ASM File Groups

`-dropFileGroups` drops Oracle ASM file groups.

Syntax and Description

```
-dropFileGroups
      (-diskGroupName disk_group)
      (-fileGroupNames file_group_name_list)
```

The following table contains the options available with the `—dropFileGroups` command.

Table 9-8 Options for the -dropFileGroups command

| Option | Description |
| --- | --- |
| `-diskGroupName` `disk_group` | Specifies the name of the Oracle ASM disk group to create. |
| `-fileGroupNames` `file_group_name_list` | Specifies a comma-delimited list of file group names to be dropped. |

##### Create Oracle ASM Quota Groups

`—createQuotaGroups` creates Oracle ASM quota groups.

Syntax and Description

```
-createQuotaGroups
      (-diskGroupName disk_group)
      (-quotaGroupNames quota_group_name_list)
      (-quotaGroupSizes quota_group_size_list)
```

The following table contains the options available with the `—createQuotaGroups` command.

Table 9-9 Options for the -createQuotaGroups command

| Option | Description |
| --- | --- |
| `-diskGroupName` `disk_group` | Specifies the name of the Oracle ASM disk group. |
| `-quotaGroupNames` `quota_group_name_list` | Specifies a comma-delimited list of quota group names to be added to the disk group. |
| `-quotaGroupSizes` `quota_group_size_list` | Specifies a comma-delimited list of quota group sizes to be processed. |

##### Drop Oracle ASM Quota Groups

`-dropQuotaGroups` drops Oracle ASM quota groups.

Syntax and Description

```
-dropQuotaGroups
      (-diskGroupName disk_group)
      (-quotaGroupNames quota_group_names_list)
```

The following table contains the options available with the `—dropQuotaGroups` command.

Table 9-10 Options for the -dropQuotaGroups command

| Option | Description |
| --- | --- |
| `-diskGroupName` `disk_group` | Specifies the name of the Oracle ASM disk group. |
| `-quotaGroupNames` `quota_group_name_list` | Specifies a comma-delimited list of quota group names to be dropped. |
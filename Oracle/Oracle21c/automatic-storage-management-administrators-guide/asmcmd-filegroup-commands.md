---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asmcmd-filegroup-commands.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic provides a summary of the ASMCMD commands that enable you to manage Oracle ASM file groups and quota groups.

The following table lists the ASMCMD file group and quota group commands with brief descriptions.

Table 10-93 Summary of ASMCMD file group commands

| Command | Description |
| --- | --- |
| chfg | Modifies a file group in a disk group based on an XML configuration file or script. |
| chqg | Modifies a quota group in the disk group. |
| lsfg | List file groups in a disk group. |
| lsqg | Lists the quota groups in a disk group. |
| mkfg | Creates a file group in a disk group based on an XML configuration file or script. |
| mkqg | Adds a quota group to the disk group. |
| mvfg | Moves a file group in a disk group to the specified quota group. |
| mvfile | Moves a file to the specified file group in the same disk group where the file is stored. |
| rmfg | Removes an existing file group from a disk group. |
| rmqg | Drops a quota group from a disk group. |

See Also:

- [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md) for more information about Oracle file groups
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003) for information about the `V$ASM` views that contain file group and quota group information.
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for information about administering Oracle ASM file groups and quota groups with SQL statements

### chfg

Purpose

Changes the attributes of a file group in a disk group based on an XML configuration file or script.

Syntax and Description

```
chfg { config_file.xml | 'contents_of_xml_script' }
```

The following table lists the options for the `chfg` command.

Table 10-94 Options for the chfg command

| Option | Description |
| --- | --- |
| `config_file.xml` | Name of the XML file that contains the changes for the file group. `chfg` searches for the XML file in the current working directory of ASMCMD unless a path is specified |
| `contents_of_xml_script.xml` | The contents of an XML script enclosed in single quotes. |

The root element of the XML configuration file or script is the `<file_group>` tag and has these attributes:

- `name`: file group name
- `dg`: disk group name to which the file group belongs

You can set properties using these tag:

- `name`: property name
- `value`: property value
- `file_type`: property file type (optional)
- `template`: Oracle ASM template name (optional)

The following is an example of an XML configuration file for `chfg`. The configuration file alters a file group named `filegroup1` on disk group `dg_data1`. The file group is associated with quota group `quotagroup1`.

```
<filegroup name="filegroup1" dg="dg_data1">
  <p name="quota_group" value="quotagroup1"/>
</filegroup>
```

For information about Oracle ASM File Groups, refer to [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md).

Example

The following examples show the use of the `chfg` command using an XML configuration file and an XML script.

Example 10-105 Using the chfg command

```
ASMCMD [+] > chfg config_file.xml

ASMCMD [+] > chfg '<filegroup name="filegroup1" dg="dg_data1"> 
                  <p name="redundancy" value="high"/> 
                  </filegroup>'
```

### chqg

Purpose

Modifies a quota group in the disk group.

Syntax and Description

```
chqg -G disk_group quota_group property value
```

The following table lists the options for the `chqg` command.

Table 10-95 Options for the chqg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |
| `property` | Specifies the name of the property. |
| `value` | Specifies the value of the property. |

The `chqg` command modifies the specified property in the specified quota group of the specified disk group. For information about Oracle ASM File and Quota Groups, refer to " [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md) ".

The following are examples of the `chqg` command. The first example modifies the `quota` property of the quota group `quota_grp1` in the `data` disk group. The second example modifies the `quota` property of the quota group `quota_grp2` in the `data` disk group.

Example 10-106 Using the chqg command

```
ASMCMD [+] > chqg -G data quota_grp1 quota 200G

ASMCMD [+] > chqg -G data quota_grp2 quota UNLIMITED
```

### lsfg

Purpose

List file groups in a disk group.

Syntax and Description

```
lsfg [-G disk_group] [--filegroup file_group] [--suppressheader]
```

The following table lists the options for the `lsfg` command.

Table 10-96 Options for the lsfg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `—filegroupfile_group` | Specifies the file group. |
| `—suppressheader` | Suppresses the headers in the output of the command. |

If the disk group option is specified, then `lsfg` returns only information about file groups in the specified disk group. If the file group option is specified, then `lsfg` returns only information about that file group.

The information about file groups is retrieved from `V$ASM_FILEGROUP` and `V$ASM_FILEGROUP_PROPERTY` views.

The following example shows the use of the `lsfg` command. The first command in the example displays the properties of the file group `FG1` in the `DATA` disk group. The second command lists all the file groups and their properties in the `DATA` disk group.

Example 10-107 Using the lsfg command

```
ASMCMD [+] > lsfg -G DATA
File Group         Disk Group  Quota Group  Used Quota MB  Client Name  Client Type  
DEFAULT_FILEGROUP  DATA        GENERIC      0                                        
VOLUME1            DATA        GENERIC      3123           VOLUME1      VOLUME       
ORCL               DATA        GENERIC      5488           ORCL         DATABASE

ASMCMD [+] > lsfg -G DATA --filegroup ORCL
File Group  Disk Group  Property           Value       File Type                  
ORCL        DATA        PRIORITY           MEDIUM                                 
ORCL        DATA        STRIPING           COARSE      CONTAINER                  
ORCL        DATA        REDUNDANCY         HIGH        CONTROLFILE                
ORCL        DATA        STRIPING           FINE        CONTROLFILE                
ORCL        DATA        REDUNDANCY         MIRROR      DATAFILE                   
ORCL        DATA        STRIPING           COARSE      DATAFILE   
...
```

### lsqg

Purpose

Lists the quota groups in a disk group.

Syntax and Description

```
lsqg [-G disk_group] [--quotagroup quota_group] [--suppressheader]
```

The following table lists the options for the `lsqg` command.

Table 10-97 Options for the lsqg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `—quotagroupquota_group` | Specifies the quota group. |
| `—suppressheader` | Suppresses the headers in the output of the command. |

If the disk group option is specified, then `lsqg` returns only information about quota groups in the specified disk group. If the quota group option is specified, then `lsqg` returns only information about that quota group.

The information about file groups is retrieved from `V$ASM_QUOTAGROUP` view.

The following example shows the use of the `lsqg` command. The first command in the example displays the properties of the file group `QG1` in the `DATA` disk group. The second command lists all the quota groups and their properties in the `DATA` disk group. The third command lists all the quota groups with name `QG1` in all the disk groups mounted by the current Oracle ASM instance. The fourth command lists all the quota groups in all the disk groups mounted by the current Oracle ASM instance.

Example 10-108 Using the lsqg command

```
ASMCMD [+] > lsqg -G DATA --quotagroup QG1
Used_Quota_MB  Quota_Limit_MB
100            200

ASMCMD [+] > lsqg -G DATA
Quotagroup_Num  Quotagroup_Name  Used_Quota_MB  Quota_Limit_MB
1               GENERIC          12357          262143
2               QG1              100            200
3               QG2              400            420

ASMCMD [+] > lsqg --quotagroup QG1
Group_Num  Quotagroup_Num  Used_Quota_MB  Quota_Limit_MB
1          2               100            200
3          5               821            1024

ASMCMD [+] > lsqg
Group_Num  Quotagroup_Num  Quotagroup_Name  Used_Quota_MB  Quota_Limit_MB
1          1               GENERIC          12357          262143
1          2               QG1              100            200
1          3               QG2              400            420
2          1               GENERIC          54000          262143
3          1               GENERIC          11             262143
3          5               QG1              821            1024
```

### mkfg

Purpose

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

Creates a file group in a disk group based on an XML configuration file or script.

Syntax and Description

```
mkfg { config_file.xml | 'contents_of_xml_script' }
```

The following table lists the options for the `mkfg` command.

Table 10-98 Options for the mkfg command

| Option | Description |
| --- | --- |
| `config_file.xml` | Name of the XML file that contains the configuration information for the file group. `mkfg` searches for the XML file in the current working directory of ASMCMD unless a path is specified |
| `contents_of_xml_script.xml` | The contents of an XML script enclosed in single quotes. |

The root element of the XML configuration file or script is the `<file_group>` tag and has these attributes:

- `name`: file group name
- `dg`: disk group name to which the file group belongs
- `client_type`: database, cluster, volume
- `client_name`: database, CDB, PDB, cluster or volume name

You can set properties using these tag:

- `name`: property name
- `value`: property value
- `file_type`: property file type (optional)
- `template`: Oracle ASM template name (optional)

The following is an example of an XML configuration file for `mkfg`. The configuration file creates a file group named `filegroup1` on disk group `dg_data1` for a database named `sample`. The file group is associated with quota group `quotagroup1`. The files in this file group have the redundancy set to mirror, except for the control file, which has a high redundancy. All other attributes are set to the default value.

```
<filegroup name="filegroup1" dg="dg_data1" client_type="database" client_name="sample">
  <p name="redundancy" value="mirror"/>
  <p name="redundancy" value="high" file_type="controlfile"/>
  <p name="quota_group" value="quotagroup1"/>
</filegroup>
```

For information about Oracle ASM File Groups, refer to " [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md) ".

Example

The following examples show the use of the `mkfg` command using an XML configuration file and an XML script.

Example 10-109 Using the mkfg command

```
ASMCMD [+] > mkfg config_file.xml

ASMCMD [+] > mkfg '<filegroup name="filegroup1" dg="dg_data1" client_type="database" client_name="sample"> 
                   </filegroup>'
```

### mkqg

Purpose

Adds a quota group to the disk group.

Syntax and Description

```
mkqg -G disk_group quota_group [property] [value]
```

The following table lists the options for the `chqg` command.

Table 10-99 Options for the mkqg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |
| `property` | Specifies the name of the property. |
| `value` | Specifies the value of the property. |

The `mkqg` command adds the specified quota group with an optional the specified property to the specified disk group. For information about Oracle ASM file and quota groups, refer to " [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md) ".

The following are examples of the `mkqg` command. The first example adds the quota group `quota_grp1` to the `data` disk group without specifying a property. The second example adds the quota group `quota_grp2` to the `data` disk group while specifying the `quota` property.

Example 10-110 Using the mkqg command

```
ASMCMD [+] > mkqg -G data quota_grp1

ASMCMD [+] > mkqg -G data quota_grp2 quota 100G
```

### mvfg

Purpose

Moves a file group in a disk group to the specified quota group.

Syntax and Description

```
mvfg -G disk_group --filegroup file_group quota_group
```

The following table lists the options for the `mvfg` command.

Table 10-100 Options for the mvfg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `—filegroupfile_group` | Specifies the file group. |
| `quota_group` | Specifies the quota group. |

The following is an example of the `mvfg` command. In the example, the file group `FG1` in the `DATA` disk group is moved to the quota group `QG1`

Example 10-111 Using the mvfg command

```
ASMCMD [+] > mvfg -G DATA --filegroup FG1 QG1
```

### mvfile

Purpose

Moves a file to the specified file group in the same disk group where the file is stored.

Syntax and Description

```
mvfile file_name --filegroup file_group
```

The following table lists the options for the `mvfile` command.

Table 10-101 Options for the mvfile command

| Option | Description |
| --- | --- |
| `file_name` | Specifies the file to be moved. |
| `—filegroup file_group` | Specifies the file group name. |

The following `mvfile` commands move the specified Oracle ASM file to the named file group.

Example 10-112 Using the mvfile command

```
ASMCMD [+] > mvfile +data/orcl/controlfile/Current.260.684924747 --filegroup FG1

ASMCMD [+fra/orcl/archivelog/flashback] > mvfile log_7.264.684968167 --filegroup FG1
```

### rmfg

Purpose

Removes an existing file group from a disk group.

Syntax and Description

```
rmfg [-r] disk_group file_group
```

The following table lists the options for the `rmfg` command.

Table 10-102 Options for the rmfg command

| Option | Description |
| --- | --- |
| `-r ` | Specifies a recursive operation. |
| `disk_group` | Specifies the disk group. |
| `file_group` | Specifies the file group. |

The `-r` option specifies a recursive removal, including contents. All files in the disk group that the file group contains are removed at the same time that the file group is removed. You must specify this option to remove a file group that contains any files. If you omit this option and the file group is not empty, then ASMCMD returns an error and does not remove the file group.

The following example shows the use of the `rmfg` command. The first command in the example removes file group `FG1` from the `DATA1` disk group. The second command removes file group `FG2`, and its contents, from the `DATA2` disk group.

Example 10-113 Using the rmfg command

```
ASMCMD [+] > rmfg DATA1 FG1
ASMCMD [+] > rmfg -r DATA2 FG2
```

### rmqg

Purpose

Removes a quota group from a disk group.

Syntax and Description

```
rmqg -G disk_group quota_group
```

The following table lists the options for the `rmqg` command.

Table 10-103 Options for the rmqg command

| Option | Description |
| --- | --- |
| `-G disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |

The following example shows the use of the `rmqg` command. The command in the example removes quota group `QG1` from the `DATA` disk group.

Example 10-114 Using the rmqg command

```
ASMCMD [+] > rmqg -G DATA QG1
```
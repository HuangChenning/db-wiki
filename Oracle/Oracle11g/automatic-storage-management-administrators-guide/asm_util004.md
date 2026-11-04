---
title: ASMCMD Disk Group Management Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util004.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD disk group management commands.

Table 12-27 provides a summary of the disk group management commands.

Table 12-27 Summary of ASMCMD Disk group management commands

| Command | Description |
| --- | --- |
| chdg | Changes a disk group (add, drop, or rebalance). |
| chkdg | Checks or repairs a disk group. |
| dropdg | Drops a disk group. |
| iostat | Displays I/O statistics for disks. |
| lsattr | Lists the attributes of a disk group. |
| lsdg | Lists disk groups and their information. |
| lsdsk | Lists disks Oracle ASM disks. |
| lsod | Lists open devices. |
| md\_backup | Creates a backup of the metadata of mounted disk groups. |
| md\_restore | Restores disk groups from a backup of the metadata. |
| mkdg | Creates a disk group. |
| mount | Mounts a disk group. |
| offline | Offlines a disk or a failure group. |
| online | Onlines a disk or a failure group. |
| rebal | Rebalances a disk group. |
| remap | Relocates data in a range of physical blocks on a disk. |
| setattr | Sets attributes in a disk group. |
| umount | Dismounts a disk group. |

## chdg

Purpose

Changes a disk group (adds disks, drops disks, resizes disks, or rebalances a disk group) based on an XML configuration file.

Syntax and Description

  
`chdg` { `config_file``.xml` | `'` `contents_of_xml_file` `'` }  

Table 12-28 lists the syntax options for the `chdg` command.

Table 12-28 Options for the chdg command

| Option | Description |
| --- | --- |
| `config_file` | Name of the XML file that contains the changes for the disk group. `chdg` searches for the XML file in the directory where ASMCMD was started unless a path is specified.  For examples of the valid tags and XML configuration file, see Example 12-30 and Example 12-31. |
| `contents_of_xml_file` | The XML script enclosed in single quotations. |

`chdg` modifies a disk group based on an XML configuration file. The modification includes adding or deleting disks from an existing disk group, and the setting rebalance power level. The power level can be set to the same values as the `ASM_POWER_LIMIT` initialization parameter. For information about the initialization parameter, see ["ASM\_POWER\_LIMIT"](asminst.md).

When adding disks to a disk group, the diskstring must be specified in a format similar to the `ASM_DISKSTRING` initialization parameter. For information about the initialization parameter, see ["ASM\_DISKSTRING"](asminst.md).

The failure groups are optional parameters. The default causes every disk to belong to a its own failure group. For information about failure groups, see ["Oracle ASM Failure Groups"](asmdiskgrps.md).

Dropping disks from a disk group can be performed through this operation. An individual disk can be referenced by its Oracle ASM disk name. A set of disks that belong to a failure group can be specified by the failure group name. For information about dropping disks, see ["Dropping Disks from Disk Groups"](asmdiskgrps.md).

You can resize a disk inside a disk group with `chdg`. The resize operation fails if there is not enough space for storing data after the resize. For information about resizing disks, see ["Resizing Disks in Disk Groups"](asmdiskgrps.md).

Example 12-30 shows the basic structure and the valid tags with their respective attributes for the `chdg` XML configuration file.

Example 12-30 Tags for the chdg XML configuration template

```
<chdg> update disk clause (add/delete disks/failure groups)
      name         disk group to change
      power        power to perform rebalance
 
<add>  items to add are placed here
</add>

<drop> items to drop are placed here
</drop>

<fg>  failure group
      name         failure group name
</fg>

<dsk> disk
      name         disk name
      string       disk path
      size         size of the disk to add
      force        true specifies to use the force option
</dsk>

</chdg>
```

For information about creating a disk group with ASMCMD `mkdg`, see "mkdg". For information about altering disk groups, see ["Altering Disk Groups"](asmdiskgrps.md).

Example

The following is an example of an XML configuration file for `chdg`. This XML file alters the disk group named `data`. The failure group `fg1` is dropped and the disk `data_0001` is also dropped. The `/dev/disk5` disk is added to failure group `fg2`. The rebalance power level is set to `3`.

Example 12-31 chdg sample XML configuration file

```
<chdg name="data" power="3">
  <drop>
    <fg name="fg1"></fg>
    <dsk name="data_0001"/>
  </drop>
  <add>
    <fg name="fg2">
      <dsk string="/dev/disk5"/>
    </fg>
  </add>
</chdg>
```

The following are examples of the `chdg` command with the configuration file or configuration information on the command line.

Example 12-32 Using the ASMCMD chdg command

```
ASMCMD [+] > chdg data_config.xml

ASMCMD [+] > chdg '<chdg name="data" power="3">
        <drop><fg name="fg1"></fg><dsk name="data_0001"/></drop>
        <add><fg name="fg2"><dsk string="/dev/disk5"/></fg></add></chdg>'
```

## chkdg

Purpose

Checks or repairs the metadata of a disk group.

Syntax and Description

  
`chkdg` \[`--repair`\] `diskgroup`  

Table 12-29 lists the syntax options for the `chkdg` command.

Table 12-29 Options for the chkdg command

| Option | Description |
| --- | --- |
| `--repair` | Repairs the disk group. |
| `diskgroup` | Name of disk group to check or repair. |

`chkdg` checks the metadata of a disk group for errors and optionally repairs the errors.

Example

The following is an example of the `chkdg` command used to check and repair the `data` disk group.

Example 12-33 Using the ASMCMD chkdg command

```
ASMCMD [+] > chkdg --repair data
```

## dropdg

Purpose

Drops a disk group.

Syntax and Description

  
`dropdg` \[`-r` `-f`\] \[`-r`\] `diskgroup`  

Table 12-30 lists the syntax options for the `dropdg` command.

Table 12-30 Options for the dropdg command

| Option | Description |
| --- | --- |
| `-f` | Force the operation. Only applicable if the disk group cannot be mounted. |
| `-r` | Recursive, include contents. |
| `diskgroup` | Name of disk group to drop. |

`dropdg` drops an existing disk group. The disk group should not be mounted on multiple nodes.

Example

These are examples of the use of `dropdg`. The first example forces the drop of the disk group `data`, including any data in the disk group. The second example drops the disk group `fra`, including any data in the disk group.

Example 12-34 Using the ASMCMD dropdg command

```
ASMCMD [+] > dropdg -r -f data

ASMCMD [+] > dropdg -r fra
```

## iostat

Purpose

Displays I/O statistics for Oracle ASM disks in mounted disk groups.

Syntax and Description

  
`iostat` \[`--suppressheader`\] \[`-et`\] \[`--io`\] \[`--region`\]  
 \[`-G` `diskgroup`\] \[`interval`\]  

`iostat` lists disk group statistics using the `V$ASM_DISK_IOSTAT` view.

Table 12-31 lists the syntax options for the `iostat` command.

Table 12-31 Options for the iostat command

| Option | Description |
| --- | --- |
| `-e` | Displays error statistics (Read\_Err, Write\_Err). |
| `-G` `diskgroup` | Displays statistics for the disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `--io` | Displays information in number of I/Os, instead of bytes. |
| `-t` | Displays time statistics (Read\_Time, Write\_Time). |
| `--region` | Displays information for cold and hot disk regions (Cold\_Reads, Cold\_Writes, Hot\_Reads, Hot\_Writes). |
| `interval` | Refreshes the statistics display based on the interval value (seconds). Use Ctrl-C to stop the interval display. |

Table 12-32 shows the statistics for a disk group. To view the complete set of statistics for a disk group, use the `V$ASM_DISK_IOSTAT` view.

Table 12-32 Attribute descriptions for iostat command output

| Attribute Name | Description |
| --- | --- |
| Group\_Name | Name of the disk group. |
| Dsk\_Name | Name of the disk. |
| Reads | Number of bytes read from the disk. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Writes | Number of bytes written to the disk. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Cold\_Reads | Number of bytes read from the cold disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Cold\_Writes | Number of bytes written from the cold disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Hot\_Reads | Number of bytes read from the hot disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Hot\_Writes | Number of bytes written to the hot disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Read\_Err | Number of failed I/O read requests for the disk. |
| Write\_Err | Number of failed I/O write requests for the disk. |
| Read\_Time | I/O time (in hundredths of a second) for read requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (0 if set to `FALSE`). |
| Write\_Time | I/O time (in hundredths of a second) for write requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (0 if set to `FALSE`). |

If a refresh interval is not specified, the number displayed represents the total number of bytes or I/Os. If a refresh interval is specified, then the value displayed (bytes or I/Os) is the difference between the previous and current values, not the total value.

Example

The following are examples of the `iostat` command. The first example displays disk I/O statistics for the `data` disk group in total number of bytes. The second example displays disk I/O statistics for the `data` disk group in total number of I/O operations.

Example 12-35 Using the ASMCMD iostat command

```
ASMCMD [+] > iostat -G data
Group_Name  Dsk_Name   Reads       Writes     
DATA        DATA_0000  180488192   473707520  
DATA        DATA_0001  1089585152  469538816  
DATA        DATA_0002  191648256   489570304  
DATA        DATA_0003  175724032   424845824  
DATA        DATA_0004  183421952   781429248  
DATA        DATA_0005  1102540800  855269888  
DATA        DATA_0006  171290624   447662592  
DATA        DATA_0007  172281856   361337344  
DATA        DATA_0008  173225472   390840320  
DATA        DATA_0009  288497152   838680576  
DATA        DATA_0010  196657152   375764480  
DATA        DATA_0011  436420096   356003840  

ASMCMD [+] > iostat --io -G data
Group_Name  Dsk_Name   Reads  Writes  
DATA        DATA_0000  2801   34918   
DATA        DATA_0001  58301  35700   
DATA        DATA_0002  3320   36345   
DATA        DATA_0003  2816   10629   
DATA        DATA_0004  2883   34850   
DATA        DATA_0005  59306  38097   
DATA        DATA_0006  2151   10129   
DATA        DATA_0007  2686   10376   
DATA        DATA_0008  2105   8955    
DATA        DATA_0009  9121   36713   
DATA        DATA_0010  3557   8596    
DATA        DATA_0011  17458  9269
```

## lsattr

Purpose

Lists the attributes of a disk group.

Syntax and Description

  
`lsattr` \[`--suppressheader`\]\[`-G` `diskgroup` \] \[`-lm`\] \[`pattern`\]  

Table 12-33 lists the syntax options for the `lsattr` command.

Table 12-33 Options for the lsattr command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `-l` | Display names with values. |
| `-m` | Displays additional information, such as the RO and Sys columns. |
| `pattern` | Display the attributes that contain pattern expression. |

Information about disk group attributes is retrieved from the `V$ASM_ATTRIBUTE` view. For information about disk group attributes, see ["Disk Group Attributes"](asmdiskgrps.md).

The RO (read-only) column identifies those attributes that can only be set when a disk group is created. The Sys column identifies those attributes that are system-created.

To display information about the disk group template attributes, see ["lstmpl"](asm_util005.md).

To set disk group attributes, see "setattr".

Example

The following are examples of the `lsattr` command. The first displays information about all attributes for the `data` disk group. The second example displays only those attributes with names containing the string `compat` for the `fra` disk group. Note the use of both the `%` and `*` wildcard characters on Linux.

Example 12-36 Using the ASMCMD lsattr command

```
ASMCMD [+] > lsattr -G data -l
Name                     Value       
access_control.enabled   FALSE       
access_control.umask     066         
au_size                  1048576     
cell.smart_scan_capable  FALSE       
compatible.advm          11.2.0.0.0  
compatible.asm           11.2.0.0.0  
compatible.rdbms         11.2.0.0.0  
disk_repair_time         3.6h        
sector_size              512

ASMCMD [+] > lsattr -G fra -l %compat*
Name              Value       
compatible.asm    11.2.0.0.0  
compatible.rdbms  10.1.0.0.0
```

## lsdg

Purpose

Lists mounted disk groups and their information. `lsdg` queries `V$ASM_DISKGROUP_STAT` by default. If the `--discovery` flag is specified, the `V$ASM_DISKGROUP` is queried instead. The output also includes notification of any current rebalance operation for a disk group. If a disk group is specified, then `lsdg` returns only information about that disk group.

Syntax and Description

`lsdg` \[`--suppressheader`\] \[`-g`\] \[`--discovery`\] \[`pattern``]`

Table 12-34 lists the options for the `lsdg` command.

Table 12-34 Options for the lsdg command

| Option | Description |
| --- | --- |
| (none) | Displays the disk group attributes listed in Table 12-35. |
| `--discovery` | Selects from `V$ASM_DISKGROUP`, or from `GV$ASM_DISKGROUP` if the -g flag is also specified. This option is always enabled if the Oracle ASM instance is version 10.1 or earlier. This flag is disregarded if `lsdg` is running in non-connected mode. |
| `-g` | Selects from `GV$ASM_DISKGROUP_STAT`, or from `GV$ASM_DISKGROUP` if the `--discovery` flag is also specified. `GV$ASM_DISKGROUP.INST_ID` is included in the output. The `REBAL` column of the `GV$ASM_OPERATION` view is also included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `pattern` | Returns only information about the specified disk group or disk groups that match the supplied pattern. See ["Wildcard Characters"](asm_util001.md). |

Table 12-35 shows the attributes for each disk group. To view the complete set of attributes for a disk group, use the `V$ASM_DISKGROUP_STAT` or `V$ASM_DISKGROUP` view.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1027.htm#REFRN30171) for descriptions of disk group information displayed in the `V$ASM_DISKGROUP` view

Table 12-35 Attribute descriptions for lsdg command output

| Attribute Name | Description |
| --- | --- |
| State | State of the disk group. Values include `BROKEN`, `CONNECTED`, `DISMOUNTED`, `MOUNTED`, `QUIESCING`, and `UNKNOWN`. |
| Type | Disk group redundancy (`NORMAL`, `HIGH`, `EXTERNAL`). |
| Rebal | `Y` if a rebalance operation is in progress. |
| Sector | Sector size in bytes. |
| Block | Block size in bytes. |
| AU | Allocation unit size in bytes. |
| Total\_MB | Size of the disk group in megabytes. |
| Free\_MB | Free space in the disk group in megabytes, without regard to redundancy. From the `V$ASM_DISKGROUP` view. |
| Req\_mir\_free\_MB | Amount of space that must be available in the disk group to restore full redundancy after the most severe failure that can be tolerated by the disk group. This is the `REQUIRED_MIRROR_FREE_MB` column from the `V$ASM_DISKGROUP` view. |
| Usable\_file\_MB | Amount of free space, adjusted for mirroring, that is available for new files. From the `V$ASM_DISKGROUP` view. |
| Offline\_disks | Number of offline disks in the disk group. Offline disks are eventually dropped. |
| Voting\_files | Specifies whether the disk group contains voting files (`Y` or `N`). |
| Name | Disk group name. |

Example

The following example lists the attributes of the `data` disk group.

Example 12-37 Using the ASMCMD lsdg command

```
ASMCMD [+] > lsdg data
State    Type    Rebal  Sector  Block       AU  Total_MB  Free_MB  Req_mir_free_MB  Usable_file_MB
MOUNTED  NORMAL  N         512   4096  4194304     12288     8835             1117            3859

(continued)
Offline_disks  Voting_files  Name
            0             N  DATA
```

## lsdsk

Purpose

Lists Oracle ASM disks.

Syntax and Description

  
`lsdsk` \[`--suppressheader`\] \[`-kptgMI`\] \[`-G` `diskgroup` \]  
 \[ `--member` | `--candidate`\]  
 \[`--discovery`\]\[`--statistics`\] `[``pattern``]`  

Table 12-36 lists the options for the `lsdsk` command.

Table 12-36 Options for the lsdsk command

| Option | Description |
| --- | --- |
| (none) | Displays the `PATH` column of the `V$ASM_DISK_STAT` view. |
| `-k` | Displays the `TOTAL_MB`, `FREE_MB`, `OS_MB`,`NAME`, `FAILGROUP`, `LIBRARY`, `LABEL`, `UDID`, `PRODUCT`, `REDUNDANCY`, and `PATH` columns of the `V$ASM_DISK` view. |
| `--statistics` | Displays the `READS`, `WRITES`, `READ_ERRS`, `WRITE_ERRS`, `READ_TIME`, `WRITE_TIME`, `BYTES_READ`, `BYTES_WRITTEN`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-p` | Displays the `GROUP_NUMBER`, `DISK_NUMBER`, `INCARNATION`, `MOUNT_STATUS`, `HEADER_STATUS`, `MODE_STATUS`, `STATE`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-t` | Displays the `CREATE_DATE`, `MOUNT_DATE`, `REPAIR_TIMER`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-g` | Selects from `GV$ASM_DISK_STAT`, or from `GV$ASM_DISK` if the `--discovery` flag is also specified. `GV$ASM_DISK.INST_ID` is included in the output. |
| `--discovery` | Selects from `V$ASM_DISK`, or from `GV$ASM_DISK` if the -g flag is also specified. This option is always enabled if the Oracle ASM instance is version 10.1 or earlier. This flag is disregarded if `lsdsk` is running in non-connected mode. |
| `--suppressheader` | Suppresses column headings. |
| `-I` | Scans disk headers for information rather than extracting the information from an Oracle ASM instance. This option forces non-connected mode. |
| `-G` | Restricts results to only those disks that belong to the group specified by `diskgroup`. |
| `-M` | Displays the disks that are visible to some but not all active instances. These are disks that, if included in a disk group, cause the mount of that disk group to fail on the instances where the disks are not visible. |
| `--candidate` | Restricts results to only disks having membership status equal to `CANDIDATE`. |
| `--member` | Restricts results to only disks having membership status equal to `MEMBER`. |
| `pattern` | Returns only information about the specified disks that match the supplied pattern. |

The `lsdsk` command can run in connected or non-connected mode. The connected mode is always attempted first. The `-I` option forces non-connected mode.

- In connected mode, `lsdsk` uses the `V$ASM_DISK_STAT` and `V$ASM_DISK` dynamic views to retrieve disk information. The `V$ASM_DISK_STAT` view is used by default.
- In non-connected mode, `lsdsk` scans disk headers to retrieve disk information. Some information is not available in this mode and some options are not valid combinations with this mode.

Note:

The non-connected mode is not supported on Windows.

`pattern` restricts the output to only disks that match the pattern specified. Wild-card characters and slashes (`/` or `\`) can be part of the pattern. `pattern` should be specified as the last option for the command. For information about wildcards, see ["Wildcard Characters"](asm_util001.md).

The `-k`, `-p`, `-t`, and `--statistics` options modify how much information is displayed for each disk. If any combination of the options are specified, then the output shows the union of the attributes associated with each flag.

Example

The following are examples of the `lsdsk` command. The first and second examples list information about disks in the `data` disk group. The third example lists information about candidate disks.

Example 12-38 Using the ASMCMD lsdsk command

```
ASMCMD [+] > lsdsk -t -G data
Create_Date  Mount_Date  Repair_Timer  Path
13-JUL-09    13-JUL-09   0             /devices/diska1
13-JUL-09    13-JUL-09   0             /devices/diska2
13-JUL-09    13-JUL-09   0             /devices/diska3
13-JUL-09    13-JUL-09   0             /devices/diskb1
13-JUL-09    13-JUL-09   0             /devices/diskb2
13-JUL-09    13-JUL-09   0             /devices/diskb3
13-JUL-09    13-JUL-09   0             /devices/diskc1
13-JUL-09    13-JUL-09   0             /devices/diskc2
...

ASMCMD [+] > lsdsk -p -G data /devices/diska*
Group_Num  Disk_Num      Incarn  Mount_Stat  Header_Stat  Mode_Stat  State   Path
        1         0  2105454210  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska1
        1         1  2105454199  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska2
        1         2  2105454205  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska3

ASMCMD [+] > lsdsk --candidate -p
Group_Num  Disk_Num      Incarn  Mount_Stat  Header_Stat  Mode_Stat  State   Path
        0         5  2105454171  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske1
        0        25  2105454191  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske2
        0        18  2105454184  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske3
        0        31  2105454197  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk1
        0        21  2105454187  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk2
        0        26  2105454192  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk3
        0        14  2105454180  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskl1
...
```

## lsod

Purpose

Lists the open Oracle ASM disks.

Syntax and Description

  
`lsod` \[`--suppressheader`\] \[`-G` `diskgroup`\] \[`--process` `process`\] \[`pattern`\]  

Table 12-37 lists the syntax options for the `lsod` command.

Table 12-37 Options for the lsod command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column header information from the output. |
| `-G` `diskgroup` | Specifies the disk group that contains the open disks. |
| `--process` `process` | Specifies a pattern to filter the list of processes. |
| `pattern` | Specifies a pattern to filter the list of disks. |

The rebalance operation (`RBAL`) opens a disk both globally and locally so the same disk may be listed twice in the output for the `RBAL` process.

Example

The following are examples of the `lsod` command. The first example lists the open devices associated with the `data` disk group and the `LGWR` process. The second example lists the open devices associated with the `LGWR` process for disks that match the `diska` pattern.

Example 12-39 Using the ASMCMD lsod command

```
ASMCMD [+] > lsod -G data --process *LGWR*
Instance Process                  OSPID Path
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska1 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska2 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska3 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diskb1 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diskb2 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diskb3 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diskd1 

ASMCMD [+] > lsod --process *LGWR* *diska*
Instance Process                  OSPID Path
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska1 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska2 
1        oracle@dadvmn0652 (LGWR) 26593 /devices/diska3
```

For another example of the `lsod` command, see [Example 12-2](asm_util001.md).

## md\_backup

Purpose

The `md_backup` command creates a backup file containing metadata for one or more disk groups.

Syntax and Description

  
`md_backup` `backup_file`  
`     [-G` `'` `diskgroup` \[`,``diskgroup``,...]'`\]  

Table 12-38 describes the options for the `md_backup` command.

Table 12-38 Options for the md\_backup command

| Option | Description |
| --- | --- |
| `backup_file` | Specifies the backup file in which you want to store the metadata. |
| `-G` `diskgroup` | Specifies the disk group name of the disk group that must be backed up |

By default all the mounted disk groups are included in the backup file, which is saved in the current working directory if a path is not specified with the file name.

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) volume and file system information is not backed up.

Example

The first example shows the use of the backup command when run without the disk group option. This example backs up all the mounted disk groups and creates the backup image in the `/scratch/backup/alldgs20100422` file. The second example creates a backup of the `data` disk group. The metadata backup that this example creates is saved in the `/scratch/backup/data20100422` file.

Example 12-40 Using the ASMCMD md\_backup command

```
ASMCMD [+] > md_backup /scratch/backup/alldgs20100422
Disk group metadata to be backed up: DATA
Disk group metadata to be backed up: FRA
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ORCL/PARAMETERFILE
Current alias directory path: ORCL
Current alias directory path: ASM
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ASM/ASMPARAMETERFILE
Current alias directory path: ORCL/TEMPFILE
Current alias directory path: ORCL/ARCHIVELOG/2010_04_20
Current alias directory path: ORCL
Current alias directory path: ORCL/BACKUPSET/2010_04_21
Current alias directory path: ORCL/ARCHIVELOG/2010_04_19
Current alias directory path: ORCL/BACKUPSET/2010_04_22
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ORCL/BACKUPSET/2010_04_20
Current alias directory path: ORCL/ARCHIVELOG
Current alias directory path: ORCL/BACKUPSET
Current alias directory path: ORCL/ARCHIVELOG/2010_04_22
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ORCL/ARCHIVELOG/2010_04_21

ASMCMD [+] > md_backup /scratch/backup/data20100422 -G data
Disk group metadata to be backed up: DATA
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ASM
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ASM/ASMPARAMETERFILE
Current alias directory path: ORCL/PARAMETERFILE
Current alias directory path: ORCL
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/TEMPFILE
```

## md\_restore

Purpose

The `md_restore` command restores disk groups from a metadata backup file.

Syntax and Description

  
`md_restore` `backup_file` `[--silent]`  
`     [``--full` `|` `--nodg` `|` `--newdg` `-o` `'` `old_diskgroup``:``new_diskgroup` \[`,`...\]'\]  
 `[``-S` `sql_script_file``]` \[`-G` `'` `diskgroup` \[`,``diskgroup`...\] `'`\]  

Table 12-39 describes the options for the `md_restore` command.

Table 12-39 Options for the md\_restore command

| Option | Description |
| --- | --- |
| `backup_file` | Reads the metadata information from `backup_file`. |
| `--silent` | Ignore errors. Typically, if `md_restore` encounters an error, it stops. Specifying this flag ignores any errors. |
| `--full` | Specifies to create a disk group and restore metadata. |
| `--nodg` | Specifies to restore metadata only. |
| `--newdg` `-o` `old_diskgroup``:``new_diskgroup`\] | Specifies to create a disk group with a different name when restoring metadata. The `-o` option is required with `--newdg`. |
| `-S` `sql_script_file` | Write SQL commands to the specified SQL script file instead of executing the commands. |
| `-G` `diskgroup` | Select the disk groups to be restored. If no disk groups are defined, then all disk groups are restored. |

Example

The first example restores the disk group `data` from the backup script and creates a copy. The second example takes an existing disk group `data` and restores its metadata. The third example restores disk group `data` completely but the new disk group that is created is named `data2`. The fourth example restores from the backup file after applying the overrides defined in the `override.sql` script file.

Example 12-41 Using the ASMCMD md\_restore command

```
ASMCMD [+] > md_restore –-full –G data –-silent /scratch/backup/alldgs20100422

ASMCMD [+] > md_restore –-nodg –G data –-silent /scratch/backup/alldgs20100422

ASMCMD [+] > md_restore –-newdg -o 'data:data2' --silent /scratch/backup/data20100422

ASMCMD [+] > md_restore -S override.sql --silent /scratch/backup/data20100422
```

## mkdg

Purpose

Creates a disk group based on an XML configuration file.

Syntax and Description

  
`mkdg` { `config_file``.xml` | `'` `contents_of_xml_file` `'` }  

Table 12-40 lists the syntax options for the `mkdg` command.

Table 12-40 Options for the mkdg command

| Option | Description |
| --- | --- |
| `config_file` | Name of the XML file that contains the configuration for the new disk group. `mkdg` searches for the XML file in the directory where ASMCMD was started unless a path is specified.  For examples of the valid tags and XML configuration file, see Example 12-42 and Example 12-43. |
| `contents_of_xml_file` | The XML script enclosed in single quotations. |

`mkdg` creates a new disk group with an XML configuration file that specifies the name of the disk group, redundancy, attributes, and paths of the disks that form the disk group. Redundancy is an optional parameter; the default is normal redundancy. For some types of redundancy, disks are required to be gathered into failure groups. In the case that failure groups are not specified for a disk group, each disk in the disk group belongs to its own failure group.

Note that `mkdg` only mounts a disk group on the local node.

It is possible to set some disk group attribute values during disk group creation. Some attributes, such as `AU_SIZE` and `SECTOR_SIZE`, can be set only during disk group creation. For more information about disk groups attributes, refer to ["Disk Group Attributes"](asmdiskgrps.md).

The default disk group compatibility settings are `10.1` for Oracle ASM compatibility, `10.1` for database compatibility, and no value for Oracle ADVM compatibility. For information about disk group compatibility attributes, see ["Disk Group Compatibility"](asmdiskgrps.md).

Example 12-42 shows the basic structure and the valid tags with their respective attributes for the `mkdg` XML configuration file.

Example 12-42 Tags for mkdg XML configuration file

```
<dg>  disk group
      name         disk group name
      redundancy   normal, external, high
 
<fg>  failure group
      name         failure group name
</fg>

<dsk> disk
      name         disk name
      string       disk path
      size         size of the disk to add
      force        true specifies to use the force option
</dsk>

<a>   attribute
      name         attribute name
      value        attribute value
</a>

</dg>
```

For information about altering a disk group with ASMCMD `chdg`, see "chdg". For information about creating a disk group, see ["Creating Disk Groups"](asmdiskgrps.md).

Example

The following is an example of an XML configuration file for `mkdg`. The configuration file creates a disk group named `data` with `normal` redundancy. Two failure groups, `fg1` and `fg2`, are created, each with two disks identified by associated disk strings. The disk group compatibility attributes are all set to `11.2`.

Example 12-43 mkdg sample XML configuration file

```
<dg name="data" redundancy="normal">
  <fg name="fg1">
    <dsk string="/dev/disk1"/>
    <dsk string="/dev/disk2"/>
  </fg>
  <fg name="fg2">
    <dsk string="/dev/disk3"/>
    <dsk string="/dev/disk4"/>
  </fg>
  <a name="compatible.asm" value="11.2"/>
  <a name="compatible.rdbms" value="11.2"/>
  <a name="compatible.advm" value="11.2"/>
</dg>
```

The following are examples of the `mkdg` command. The first example runs `mkdg` with an XML configuration file in the directory where ASMCMD was started. The second example runs `mkdg` using information on the command line.

Example 12-44 Using the ASMCMD mkdg command

```
ASMCMD [+] > mkdg data_config.xml

ASMCMD [+] > mkdg '<dg name="data"><dsk string="/dev/disk*"/></dg>'
```

## mount

Purpose

Mounts a disk group.

Syntax and Description

  
`mount` \[`--restrict`\] { \[`-a`\] | \[`-f`\] `diskgroup` \[ `diskgroup`...\] }  

Table 12-41 lists the syntax options for the `mount` command.

Table 12-41 Options for the mount command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group. |
| `-a` | Mounts all disk groups. |
| `--restrict` | Mounts in restricted mode. |
| `-f` | Forces the mount operation. |

This operation mounts one or more disk groups. A disk group can be mounted with or without force or restricted options. For more information about mounting disk groups, see ["Mounting and Dismounting Disk Groups"](asmdiskgrps.md).

Example

The following are examples of the `mount` command showing the use of the force, restrict, and all options.

Example 12-45 Using the ASMCMD mount command

```
ASMCMD [+] > mount -f data

ASMCMD [+] > mount --restrict data

ASMCMD [+] > mount -a
```

## offline

Purpose

Offline disks or failure groups that belong to a disk group.

Syntax and Description

  
`offline` `-G` `diskgroup`  
 { `-F` `failgroup` | `-D` `disk` }  
 \[`-t` { `minutes` | `hours` }\]  

Table 12-42 lists the syntax options for the `offline` command.

Table 12-42 Options for the offline command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `-F` `failgroup` | Failure group name. |
| `-D` `disk` | Specifies a single disk name. |
| `-t` `minutes` \| `hours` | Specifies the time before the specified disk is dropped as `n` `m` or `n` `h`, where `m` specifies minutes and `h` specifies hours. For example, `120m` or `2h`.The default unit is hours. |

When a failure group is specified, this implies all the disks that belong to it should be offlined.

Example

The following are examples of the `offline` command. The first example offlines the `failgroup1` failure group of the `data` disk group. The second example offlines the `data_0001` disk of the `data` disk group with a time of `1.5` hours before the disk is dropped.

Example 12-46 Using the ASMCMD offline command

```
ASMCMD [+] > offline -G data -F failgroup1

ASMCMD [+] > offline -G data -D data_0001 -t 1.5h
```

## online

Purpose

Online all disks, a single disk, or a failure group that belongs to a disk group.

Syntax and Description

  
`online` `-G` `diskgroup` { `-a` | `-F` `failgroup` | `-D` `disk` } \[`-w`\]  

Table 12-43 lists the syntax options for the `online` command.

Table 12-43 Options for the online command

| Option | Description |
| --- | --- |
| `-a` | Online all offline disks in the disk group. |
| `-G` `diskgroup` | Disk group name. |
| `-F` `failgroup` | Failure group name. |
| `-D` `disk` | Disk name. |
| `-w` | Wait option. Causes ASMCMD to wait for the disk group to be rebalanced before returning control to the user. The default is not waiting. |

When a failure group is specified, this implies all the disks that belong to it should be onlined.

Example

The following are examples of the `online` command. The first example onlines all disks in the `failgroup1` failure group of the `data` disk group with the `wait` option enabled. The second example onlines the `data_0001` disk in the `data` disk group.

Example 12-47 Using the ASMCMD online command

```
ASMCMD [+] > online -G data -F failgroup1 -w 

ASMCMD [+] > online -G data -D data_0001
```

## rebal

Purpose

Rebalances a disk group.

Syntax and Description

  
`rebal` \[`--power` `power`\] \[`-w`\] `diskgroup`  

Table 12-44 lists the syntax options for the `rebal` command.

Table 12-44 Options for the rebal command

| Option | Description |
| --- | --- |
| `diskgroup` | Disk group name. |
| `--power` `power` | Power setting. |
| `-w` | Wait option. Causes ASMCMD to wait for the disk group to be rebalanced before returning control to the user. The default is not waiting. |

The power level can be set to the same values as the `ASM_POWER_LIMIT` initialization parameter. A value of `0` disables rebalancing. If the rebalance power is not specified, the value defaults to the setting of the `ASM_POWER_LIMIT` initialization parameter. For information about the power level, see ["ASM\_POWER\_LIMIT"](asminst.md) and ["Tuning Rebalance Operations"](asmdiskgrps.md).

You can determine if a rebalance operation is occurring with the ASMCMD `lsop` command. See ["lsop"](asm_util002.md). For more information about rebalancing a disk group, see ["Manually Rebalancing Disk Groups"](asmdiskgrps.md).

Example

The following is an example of the `rebal` command that rebalances the `fra` disk group with a power level set to `4`.

Example 12-48 Using the ASMCMD rebal command

```
ASMCMD [+] > rebal --power 4 fra

ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power
FRA         REBAL    RUN    4
```

## remap

Purpose

Marks a range of blocks as unusable on the disk and relocates any data allocated in that range.

Syntax and Description

`remap` `diskgroup` `disk` `block_range`

Table 12-45 lists the syntax options for the `remap` command.

Table 12-45 Options for the remap command

| Option | Description |
| --- | --- |
| `diskgroup` | Disk group name in which a disk must have data relocated. |
| `disk` | Name of the disk that must have data relocated. The name must match the `NAME` column in the `V$ASM_DISK` view. |
| `block_range` | Range of physical blocks to relocate in the format `start_range_number` `-` `end_range_number`. |

The `remap` command only relocates blocks. It does not correct or repair blocks that contain corrupted contents. The command uses a physical block size based on the `SECTOR_SIZE` disk group attribute.

Examples

The first example remaps blocks `5000` through `5999` for disk `DATA_0001` in disk group `DATA`. The second example remaps blocks `6230` through `6339` for disk `FRA_0002` in disk group `FRA`

Example 12-49 Using the ASMCMD remap command

```
ASMCMD [+] > remap DATA DATA_0001 5000-5999

ASMCMD [+] > remap FRA FRA_0002 6230-6339
```

## setattr

Purpose

Sets the attributes for an Oracle ASM disk group.

Syntax and Description

  
`setattr` `-G` `diskgroup` `attribute_name` `attribute_value`  

Table 12-46 lists the syntax options for the `setattr` command.

Table 12-46 Options for the setattr command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `attribute_name` | Name of the attribute. |
| `attribute_value` | Value of the attribute. |

The `COMPATIBLE.ASM` attribute must be advanced before advancing other disk group compatibility attributes and its value must be greater than or equal to the value of other disk group compatibility attributes.

For information about disk group attributes, see ["Disk Group Attributes"](asmdiskgrps.md).

Example

The following are examples of the `setattr` command. The first example sets the disk group attribute `COMPATIBLE.ASM` to `11.2` for the `data` disk group. The second example sets the disk group attribute `COMPATIBLE.RDBMS` to `11.2` for the `data` disk group.

Example 12-50 Using the ASMCMD setattr command

```
ASMCMD [+] > setattr -G data compatible.asm 11.2.0.0.0

ASMCMD [+] > setattr -G data compatible.rdbms 11.2.0.0.0
```

## umount

Purpose

Dismounts a disk group.

Syntax and Description

  
`umount` { `-a` | \[`-f`\] `diskgroup` }  

Table 12-47 lists the syntax options for the `umount` command.

Table 12-47 Options for the umount command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group. |
| `-a` | Dismounts all mounted disk groups. These disk groups are listed in the output of the `V$ASM_DISKGROUP` view. |
| `-f` | Forces the dismount operation. |

Example

The following are examples of the `umount` command. The first example dismounts all disk groups mounted on the Oracle ASM instance. The second example forces the dismount of the `data` disk group.

Example 12-51 Using the ASMCMD umount command

```
ASMCMD [+] > umount -a

ASMCMD [+] > umount -f data
```
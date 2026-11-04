---
title: Oracle Cluster Registry Utility Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/ocrsyntax.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## G Oracle Cluster Registry Utility Reference

This appendix describes the syntax of the Oracle Cluster Registry (OCR) configuration utility, OCRCONFIG, and troubleshooting OCR, which includes descriptions and usage information for OCRCHECK and OCRDUMP.

This appendix contains the following topics:

## About OCRCONFIG

This section contains topics which relate to using the OCRCONFIG utility.

Overview

Use the `ocrconfig` command to manage OCR. Using this utility you can import, export, add, delete, restore, overwrite, backup, repair, replace, move, upgrade, or downgrade OCR.

Operational Notes

Usage Information

- The OCRCONFIG executable is located in the `Grid_home/bin` directory
- The `ocrconfig` command syntax is as follows:
	```
	ocrconfig -option
	```

Using Utility Help

To display the help output for the OCRCONFIG utility:

```
ocrconfig -help
```

Privileges and Security

To use the OCRCONFIG utility you must be logged into the operating system as a user with administrative privileges.

Log Files

The OCRCONFIG utility creates a log file in `Grid_home` `/log/` `host_name` `/client`.

To change the amount of logging, edit the path in the `Grid_home` `/srvm/admin/ocrlog.ini` file.

## OCRCONFIG Command Reference

This section lists the following OCRCONFIG commands:

- `ocrconfig -add`
- `ocrconfig -backuploc`
- `ocrconfig -delete`
- `ocrconfig -downgrade`
- `ocrconfig -export`
- `ocrconfig -import`
- `ocrconfig -manualbackup`
- `ocrconfig -overwrite`
- `ocrconfig -repair`
- `ocrconfig -replace`
- `ocrconfig -restore`
- `ocrconfig -showbackup`
- `ocrconfig -upgrade`

ocrconfig -add

Use the `ocrconfig -add` command to add an OCR location to a storage device or Oracle Automatic Storage Management (Oracle ASM) disk group. OCR locations that you add must exist, have sufficient permissions, and, in the case of Oracle ASM disk groups, must be mounted before you can add them.

Syntax

```
ocrconfig -add location_name
```

Usage Notes

- You must run this command as `root`.
- The `location_name` variable can be a device name, a file name, or the name of an Oracle ASM disk group. For example:
	- `/dev/raw/raw1`: Ensure that the device exists
		- `/oradbocfs/crs/data.ocr`: You must create an empty (0 byte) OCR location
		- `d:\oracle\mirror.ocr`: You must create an empty (0 byte) OCR location
		- `+newdg`: Ensure that the disk group exists and is mounted
		If you specify an Oracle ASM disk group, the name of the disk group must be preceded by a plus sign (`+`).
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCR locations and setting correct permissions
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management

Example

To add an OCR location to the default location in Oracle ASM, `data`:

```
# ocrconfig -add +data
```

ocrconfig -backuploc

Use the `ocrconfig -backuploc` command to specify an OCR backup directory location.

Syntax

```
ocrconfig [-local] -backuploc file_name
```

Usage Notes

- You must run this command as `root`.
- Use the `-local` option to specify an OLR backup directory location.
- The `file_name` variable can be a full directory path name that is accessible by all nodes. For example:
	- `Grid_home` `/cdata/cluster3/`: Ensure that the location exists
		- `d:\cdata\cluster3`: Ensure that the location exists
- The default location for generating OCR backups on Linux or UNIX systems is `Grid_home` `/cdata/` `cluster_name`, where `cluster_name` is the name of your cluster. The Windows default location for generating OCR backups uses the same path structure.
- The default location for generating OLR backups on Linux or UNIX systems is `Grid_home` `/cdata/` `host_name`, where `host_name` is the name of the node on which the OLR resides that you want to back up. The Windows default location for generating OLR backups uses the same path structure.

Example

To specify an OCR backup location in a directory:

```
# ocrconfig -backuploc $Grid_home/cdata/cluster3
```

ocrconfig -delete

Use the `ocrconfig -delete` command to remove an OCR device or file.

Syntax

```
ocrconfig -delete file_name
```

Usage Notes

- You must run this command as `root`.
- The `file_name` variable can be a device name, a file name, or the name of an Oracle ASM disk group. For example:
	- `/dev/raw/raw1`
		- `/oradbocfs/crs/data.ocr`
		- `d:\oracle\mirror.ocr`
		- `+olddg`
	If you specify an Oracle ASM disk group, the name of the disk group must be preceded by a plus sign (`+`).

Example

To remove an OCR location:

```
# ocrconfig -delete +olddg
```

ocrconfig -downgrade

Use the `ocrconfig -downgrade` command to downgrade OCR to an earlier specified version.

Syntax

```
ocrconfig -downgrade [-version version_string]
```

Usage Notes

- You must run this command as `root`.

Example

To downgrade OCR to an earlier version:

```
# ocrconfig -downgrade -version
```

ocrconfig -export

Use the `ocrconfig -export` command to export the contents of OCR to a target file.

Syntax

```
ocrconfig [-local] -export file_name
```

Usage Notes

- You must run this command as `root`.
- Use the `-local` option to export the contents of OLR.
- The `file_name` variable can be a full path name that is accessible by all nodes. For example:
	- `/oradbocfs/crs/data.ocr`
		- `d:\oracle\`

Example

To export the contents of OCR to a file:

```
# ocrconfig -export d:\tmp\a
```

ocrconfig -import

Use the `ocrconfig -import` command to import the contents of a target file into which you exported the contents of OCR back into OCR.

Syntax

```
ocrconfig [-local] -import file_name
```

Usage Notes

- You must run this command as `root`.
- Use the `-local` option to import the contents of OLR from a file.
- The `file_name` variable must be a full path name that is accessible by all nodes. For example:
	- `/oradbocfs/crs/data.ocr`
		- `d:\oracle\`
- You must shut down Oracle Clusterware before running this command.

Example

To import the contents a file back into OCR:

```
# ocrconfig -import d:\tmp\a
```

ocrconfig -manualbackup

Use the `ocrconfig -manualbackup` command to back up OCR on demand in the location you specify with the `-backuploc` option.

Syntax

```
ocrconfig [-local] -manualbackup
```

Usage Notes

- You must run this command as `root`.
- Use the `-local` option to perform a manual backup of OLR.

Example

To back up OCR:

```
# ocrconfig -manualbackup
```

ocrconfig -overwrite

Use the `ocrconfig -overwrite` command to overwrite an OCR configuration in the OCR metadata with the current OCR configuration information that is found on the node from which you run this command.

Syntax

```
ocrconfig -overwrite
```

Usage Notes

- You must run this command as `root`.

Example

To overwrite an OCR configuration:

```
# ocrconfig -overwrite
```

ocrconfig -repair

Use the `ocrconfig -repair` command to repair an OCR configuration on the node from which you run this command. Use this command to add, delete, or replace an OCR location on a node that may have been stopped while you made changes to the OCR configuration in the cluster. OCR locations that you add must exist, have sufficient permissions, and, in the case of Oracle ASM disk groups, must be mounted before you can add them.

Syntax

```
ocrconfig -repair -add file_name | -delete file_name | -replace 
current_file_name -replacement new_file_name
```

Usage Notes

- You must run this command as `root`.
- Oracle High Availability Services must be started to successfully complete the repair.
- The Cluster Ready Services daemon must be stopped before running `ocrconfig -repair`.
- The `file_name` variable can be a valid OCR and either a device name, an absolute path name of an existing file, or the name of an Oracle ASM disk group. For example:
	- `/dev/raw/raw1`
		- `/oradbocfs/crs/data.ocr`
		- `d:\oracle\mirror.ocr`
		- `+newdg`
		If you specify an Oracle ASM disk group, the name of the disk group must be preceded by a plus sign (`+`).
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs and setting correct permissions
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
- You can only use one option with `ocrconfig -repair` at a time.
- Running this command only modifies the local configuration and it and only affects the current node.

Example

To repair an OCR configuration:

```
# ocrconfig -repair -delete +olddg
```

ocrconfig -replace

Use the `ocrconfig -replace` command to replace an OCR device or file on the node from which you run this command. OCR locations that you add must exist, have sufficient permissions, and, in the case of Oracle ASM disk groups, must be mounted before you can add them.

Syntax

```
ocrconfig -replace current_location_name -replacement new_location_name
```

Usage Notes

- You must run this command as `root`.
- The `new_location_name` variable can be a device name, a file name, or the name of an Oracle ASM disk group. For example:
	- `/dev/raw/raw1`: Ensure that the device exists
		- `/oradbocfs/crs/data.ocr`: You must create an empty (0 byte) OCR location
		- `d:\oracle\mirror.ocr`: You must create an empty (0 byte) OCR location
		- `+newdg`: Ensure that the disk group exists and is mounted
		If you specify an Oracle ASM disk group, the name of the disk group must be preceded by a plus sign (`+`).
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs and setting correct permissions
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
- You must have at least two OCR devices to use this command. If you do not have at least two OCR devices, then you must run the `ocrconfig -add` command to add a new OCR device followed by the `ocrconfig -delete` command to delete the OCR device you want to replace.

Example

To replace an OCR device or file:

```
# ocrconfig -replace /dev/raw/raw1 -replacement +newdg
```

ocrconfig -restore

Use the `ocrconfig -restore` command to restore OCR from an automatically created OCR backup file.

Syntax

```
ocrconfig [-local] -restore file_name
```

Usage Notes

- You must run this command as `root`.
- Before running this command, ensure that the original OCR or OLR files exist. If the original file does not exist, then you must create an empty file.
	Note:
	You cannot use a file generated by the `ocrconfig -export` to restore OCR. The file must be a manual or automatic backup.
- Use the `-local` option to restore a backup of OLR.
- Example file names are:
	- `/oradbocfs/crs/BACKUP00.ocr`
		- `d:\oracle\BACKUP01.ocr`
- Ensure that the storage devices that you specify exist and that those devices are valid.

Example

To restore OCR from a file:

```
# ocrconfig -restore /oradbocfs/crs/BACKUP00.ocr
```

ocrconfig -showbackup

Use the `ocrconfig -showbackup` command to display the backup location, timestamp, and the originating node name of the backup files. By default, this command displays information for both automatic and manual backups unless you specify `auto` or `manual`.

Syntax

```
ocrconfig [-local] -showbackup [auto | manual]
```

Usage Notes

- Use the `-local` option to show manual OLR backup information. The `-local` flag functions only with the `manual` option.
- You can optionally specify `auto` or `manual` to display information about only automatic backups or only manual backups, respectively:
	- `auto`: Displays information about automatic backups that Oracle Clusterware created in the past 4 hours, 8 hours, 12 hours, and in the last day and week.
		- `manual`: Displays information about manual backups that you invoke using the `ocrconfig -manualbackup` command.

Example

To display manual backup information for OLR:

```
$ ocrconfig -local -showbackup manual
```

ocrconfig -upgrade

Only `root` scripts use the `ocrconfig -upgrade` command to upgrade OCR from a previous version.

## Troubleshooting Oracle Cluster Registry and Diagnostic Output

This section describes various methods for troubleshooting problems with OCR, and obtaining diagnostic information from the utilities used to manage OCR. You can use these utilities to troubleshoot OLR.

This section contains the following topics:

- Troubleshooting Oracle Cluster Registry
- Using the OCRCHECK Utility
- Using the OCRDUMP Utility to View Oracle Cluster Registry Content

### Troubleshooting Oracle Cluster Registry

Table G-1 describes common OCR problems with corresponding resolution suggestions.

Table G-1 Common Oracle Cluster Registry Problems and Solutions

| Problem | Solution |
| --- | --- |
| Not currently using OCR mirroring and would like to enable it. | Run the `ocrconfig` command with the `-replace` option. |
| OCR failed and you must replace it. Error messages in Oracle Enterprise Manager or OCR log file. | Run the `ocrconfig` command with the `-replace` option. |
| OCR has a misconfiguration. | Run the `ocrconfig` command with the `-repair` option as described. |
| You are experiencing a severe performance effect from OCR processing or you want to remove OCR for other reasons. | Run the `ocrconfig` command with the `-replace` option as described. |
| OCR has failed and before you can fix it, the node must be rebooted with only one OCR. | Run the `ocrconfig` with the `-repair` option to remove the bad OCR location. Oracle Clusterware cannot start if it cannot find all OCRs defined. |

### Using the OCRCHECK Utility

The OCRCHECK utility displays the version of the OCR's block format, total space available and used space, OCRID, and the OCR locations that you have configured. OCRCHECK performs a block-by-block `checksum` operation for all of the blocks in all of the OCRs that you have configured. It also returns an individual status for each file and a result for the overall OCR integrity check.

Note:

You can only use OCRCHECK when the Oracle Cluster Ready Services stack is ONLINE on all nodes in the cluster.

See Also:

["The Oracle Clusterware Stack"](intro.md) for more information about the Oracle Cluster Ready Services stack

You can run the `ocrcheck -help` command to display usage information about this utility.

The following example shows a sample of the OCRCHECK utility output:

```
# ocrcheck

Status of Oracle Cluster Registry is as follows :
        Version                  :          3
        Total space (kbytes)     :     262120
        Used space (kbytes)      :        752
        Available space (kbytes) :     261368
        ID                       : 2098980155
        Device/File Name         : +ocrdg1
                                   Device/File integrity check succeeded
        Device/File Name         : +ocrdg2
                                   Device/File integrity check succeeded
                                   Device/File not configured
                                   Device/File not configured
                                   Device/File not configured
        Cluster registry integrity check succeeded 
        Logical corruption check succeeded
```

Note:

The logical corruption check is only performed if you run the `ocrcheck` command as `root`.

The following two examples show samples of the OCRCHECK utility output. Each example shows only configured OCRs located on an Oracle ASM disk group and on a raw device.

Example G-1 OCR Located on an Oracle ASM Disk Group

```
$ ocrcheck -config

Oracle Cluster Registry configuration is :
        Device/File Name         : +ocrvd11
        Device/File Name         :  +ocrvd2
.
.
.
Status of Oracle Cluster Registry is as follows :
        Version                  :          3
        Total space (kbytes)     :     262120
        Used space (kbytes)      :       2384
        Available space (kbytes) :     259736
        ID                       : 1517109829
        Device/File Name         : +ocrvd11
                                   Device/File integrity check succeeded
        Device/File Name         : +ocrvd2
                                   Device/File integrity check succeeded
                                   Device/File not configured
                                   Device/File not configured
                                   Device/File not configured
        Cluster registry integrity check succeeded 
        Logical corruption check succeeded
```

Example G-2 OCR Located on a Raw Device

```
$ ocrcheck -config

Oracle Cluster Registry configuration is :
        Device/File Name         : /dev/raw/raw15
        Device/File Name         : /dev/raw/raw17
        Device/File Name         : /dev/raw/raw16
.
.
.
Status of Oracle Cluster Registry is as follows :
        Version                  :          3
        Total space (kbytes)     :     262120
        Used space (kbytes)      :       2884
        Available space (kbytes) :     259236
        ID                       :  157485888
        Device/File Name         : /dev/raw/raw15
                                   Device/File integrity check succeeded
        Device/File Name         : /dev/raw/raw17
                                   Device/File integrity check succeeded
        Device/File Name         : /dev/raw/raw16
                                   Device/File integrity check succeeded
                                   Device/File not configured
                                   Device/File not configured
        Cluster registry integrity check succeeded 
        Logical corruption check succeeded
```

Run the `ocrcheck -local -config` command to obtain OLR information.

Note:

You can use the `ocrcheck -local` command only when the Oracle Cluster Ready Services stack and Oracle High Availability Services stack are OFFLINE on the local node.

See Also:

["The Oracle Clusterware Stack"](intro.md) for more information about the Oracle Cluster Ready Services and the Oracle High Availability Services stacks

```
$ ocrcheck -local -config

Oracle Local Registry configuration is :
        Device/File Name         : Grid_home/oracle/has_work/data.olr.stact23
```

OCRCHECK creates a log file in the `Grid_home` `/log/` `host_name` `/client` directory. To change the log level, edit the `Grid_home` `/srvm/admin/ocrlog.ini` file.

### Using the OCRDUMP Utility to View Oracle Cluster Registry Content

This section explains how to use the OCRDUMP utility to view OCR and Oracle Local Registry (OLR) content for troubleshooting. The OCRDUMP utility enables you to view OCR and OLR contents by writing the content to a file or `stdout` in a readable format.

You can use several options for OCRDUMP. For example, you can limit the output to a key and its descendents. You can also write the contents to an XML file that you can view using a browser. OCRDUMP writes the OCR keys as ASCII strings and values in a data type format. OCRDUMP retrieves header information based on a best effort basis.

OCRDUMP also creates a log file in `Grid_home` `/log/` `host_name` `/client`. To change the log level, edit the `Grid_home` `/srvm/admin/ocrlog.ini` file.

To change the logging component, edit the entry containing the `comploglvl=` entry. For example, to change the log level of the `OCRAPI` component to 3 and to change the log level of the `OCRRAW` component to 5, make the following entry in the `ocrlog.ini` file:

```
comploglvl="OCRAPI:3;OCRRAW:5"
```

Note:

Make sure that you have file creation privileges in the `Grid_home` directory before using the OCRDUMP utility.

This section includes the following topics:

- OCRDUMP Utility Syntax and Options
- OCRDUMP Utility Examples
- Sample OCRDUMP Utility Output

#### OCRDUMP Utility Syntax and Options

This section describes the OCRDUMP utility command syntax and usage. Run the `ocrdump` command with the following syntax where `file_name` is the name of a target file to which you want Oracle Database to write the Oracle Cluster Registry output and where `key_name` is the name of a key from which you want Oracle Database to write Oracle Cluster Registry subtree content:

```
$ ocrdump [file_name | -stdout] [-local] [-backupfile backup_file_name
[-keyname key_name] [-xml] [-noheader]
]
```

Table G-2 describes the OCRDUMP utility options and option descriptions.

Table G-2 OCRDUMP Options and Option Descriptions

| Options | Description |
| --- | --- |
| `file_name` | The name of a file to which you want OCRDUMP to write output.  By default, OCRDUMP writes output to a predefined output file named `OCRDUMPFILE`. The `file_name` option redirects OCRDUMP output to a file that you specify. |
| `-stdout` | Use this option to redirect the OCRDUMP output to the text terminal that initiated the program.  If you do not redirect the output, OCRDUMP writes output to a predefined output file named `OCRDUMPFILE`. |
| `-local` | Use this option to dump the contents of OLR. |
| `-backupfile` | Use this option to view the contents of an OCR backup file. Use the `-local` option with this option to view the contents of an OLR backup file. |
| `backup_file_name` | The name of the backup file with the content you want to view. You can query the backups using the `ocrconfig -showbackup` command. |
| `-keyname` `key_name` | The name of an Oracle Cluster Registry key whose subtree is to be dumped. |
| `-xml` | Use this option to write the output in XML format. |
| `-noheader` | Does not print the time at which you ran the command and when the Oracle Cluster Registry configuration occurred. |

#### OCRDUMP Utility Examples

The following `ocrdump` utility examples extract various types of OCR information and write it to various targets:

```
ocrdump
```

Writes OCR content to a file called `OCRDUMPFILE` in the current directory.

```
ocrdump MYFILE
```

Writes OCR content to a file called `MYFILE` in the current directory.

```
ocrdump -stdout -keyname SYSTEM
```

Displays OCR content from the subtree of the key `SYSTEM` in the terminal window.

```
ocrdump -stdout -xml
```

Displays OCR content in the terminal window in XML format.

```
ocrdump -stdout -backupfile Grid_home/cdata/cluster_name/file_name
```

Displays the content of the in the `Grid_home` `/cdata/` `cluster_name` / `file_name` directory. You must run this command as `root` to be able to view all of the keys. Be sure to name the file appropriately so that it can be recognized by anyone as an OCR backup file, such as `BACKUPOO.ocr`.

#### Sample OCRDUMP Utility Output

The following OCRDUMP examples show the `KEYNAME`, `VALUE TYPE`, `VALUE`, permission set (`user`, `group`, `world`) and access rights for two sample runs of the `ocrdump` command. The following shows the output for the `SYSTEM.language` key that has a text value of `AMERICAN_AMERICA.WE8ASCII37`.

```
[SYSTEM.language]
ORATEXT : AMERICAN_AMERICA.WE8ASCII37
SECURITY : {USER_PERMISSION : PROCR_ALL_ACCESS, GROUP_PERMISSION : PROCR_READ,
OTHER_PERMISSION : PROCR_READ, USER_NAME : user, GROUP_NAME : group}
```

The following shows the output for the `SYSTEM.version` key that has integer value of `3`:

```
[SYSTEM.version]
UB4 (10) : 3
SECURITY : {USER_PERMISSION : PROCR_ALL_ACCESS, GROUP_PERMISSION : PROCR_READ,
OTHER_PERMISSION : PROCR_READ, USER_NAME : user, GROUP_NAME : group}
```
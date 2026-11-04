---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/administer-acfs-advm-em.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

Oracle Enterprise Manager Cloud Control provides tools for administering Oracle Advanced Cluster File System (Oracle ACFS).

This chapter describes how to administer Oracle Advanced Cluster File System (Oracle ACFS) with Oracle Enterprise Manager Cloud Control.

All Oracle ASM administration tasks begin with the Oracle Automatic Storage Management home page in Oracle Enterprise Manager Cloud Control.

Note:

To manage or monitor Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance.

This chapter contains the following topics:

See Also:

- [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md) for information about using command-line tools to administer Oracle ACFS file systems
- [Basic Steps to Manage Oracle ACFS Systems](steps-manage-acfs.md) for information about the basic steps for creating Oracle ACFS file systems
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30) for information about Oracle Flex ASM

### Accessing the Oracle ASM and Oracle ACFS Home Page

All Oracle ASM administration tasks begin with the Oracle Automatic Storage Management home page in Oracle Enterprise Manager Cloud Control. The Oracle Automatic Storage Management home page displays:

- The status of the Oracle ASM instance.
- A chart that shows the used and free space of each disk group and disk group internal usage.
- A list of databases that are serviced by the Oracle ASM instance.
- A list of Oracle Advanced Cluster File System (Oracle ACFS) file systems that are serviced by the Oracle ASM instance.
- A list of other non-Oracle ACFS volumes.
- A list of alerts for the Oracle ASM instance and the host computer.
- Links to the Oracle ASM Performance, Disk Groups, Configuration, Users, and Oracle ACFS pages.

To access the Oracle Automatic Storage Management home page on a single-instance system:

1. Log in to Oracle Enterprise Manager Cloud Control.
2. Under the Targets drop down menu at the top of the page, select All Targets.
3. In the lists of targets on the All Targets page, click the target for the Oracle ASM instance.
4. If prompted for Oracle ASM login credentials, then enter the user `SYS`, provide the `SYS` password that was set for the Oracle ASM instance during installation, and connect as `SYSASM`. The Oracle Automatic Storage Management home page displays.

See Also:

- [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md) for information about using command-line tools to administer Oracle ACFS file systems
- [Basic Steps to Manage Oracle ACFS Systems](steps-manage-acfs.md) for information about the basic steps for creating Oracle ACFS file systems
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-519175D4-B857-4DD2-B177-09A2D1643E3C) for additional information about the Oracle ASM home page

### Managing Oracle ACFS File Systems and Volumes with Oracle Enterprise Manager

This section discusses how to manage Oracle ACFS file systems and volumes systems with Oracle Enterprise Manager Cloud Control.

This section contains the following topics:

- Creating Oracle ACFS File Systems and Volumes
- Viewing and Modifying Oracle ACFS Volumes and File Systems

For more information about Oracle ACFS file systems and volumes, refer to " [About Oracle ACFS](understand-acfs-concepts.md) ".

See Also:

[Oracle Enterprise Manager Cloud Control Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=EMADM-GUID-5BA58E51-3D84-4591-B8CD-AA91B3C00373)

#### Creating Oracle ACFS File Systems and Volumes

To create an Oracle ACFS volume, perform the following steps.

1. Access the Disk Groups page from the Oracle ASM home page.
2. Click the Volumes link in the General tab of the Disk Group page.
3. Click Create in the Volumes tab of the Disk Group page.
	The Create ASM Volume page displays.
	Enter the volume name, disk group name that contains the volume, and the initial size of the volume.
	You can also select the redundancy setting for the volume and the region settings for primary and mirror extents.

To create an Oracle ACFS file system on a volume in a disk group, perform the following steps.

1. Access the Volumes tab of the Disk Group page.
2. Select an existing volume in the disk group and click Create ASM Cluster File System.
	The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to `11.2` or higher for the disk group..
3. On the Create ASM Cluster File System page, enter the information to create a file system. You can optionally register and mount the file system.
	You must enter the volume name. You can enter an optional volume label.
	You can optionally choose to register and mount the file system when it is created. Select a mount point from available directories.
	Enter the host credentials needed to run the command when prompted. To register or mount a file system, you need root or administrator privileges.
	After a directory has been selected, click Show Command to have Oracle Enterprise Manager generate the commands that you can run at an operating system prompt. Examples of commands on a Linux system are:
	```
	/sbin/mkfs -t acfs -b 4k /dev/asm/volume1-361
	/sbin/acfsutil registry -f -a /dev/asm/volume1-361 /oracle/acfsmounts/acfs2
	/bin/mount -t acfs -rw /dev/asm/volume1-361 /oracle/acfsmounts/acfs2
	```
	You can also generate the commands to register or mount an Oracle ACFS file system on the ASM Cluster File System tab.

See Also:

- [ASMCMD Volume Management Commands](manage-advm-asmcmd.md) for information about creating a volume with the ASMCMD `volcreate` command
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [About the Oracle ACFS Mount Registry](understand-acfs-concepts.md) for information about the registry process

#### Viewing and Modifying Oracle ACFS Volumes and File Systems

To view and modify information about Oracle ACFS file systems, click the ASM Cluster File System link in the Oracle ASM home page.

The ASM Cluster File System tab in Oracle Enterprise Manager lists all of the Oracle ACFS associated with the Oracle ASM instance.

On this page, you can choose to mount, dismount, delete, create snapshot, view content, register, and deregister a selected file system. In addition, you can create a file system, mount all file systems, or dismount all file systems.

For each Oracle ACFS, the columns provide information for Mount Point, Availability, State, Snapshots, Used (%), Used (GB), Size (GB), Allocated Space, Redundancy, Volume, and Disk Group. Redundancy, Volume, and Disk Group columns are on the far right of the page and are not shown in the illustration. The mount point, snapshots, volume, and disk group are provided as links to further information.

To view information about a specific volume, click the volume name in the Volume column on the ASM Cluster File System page to display the General tab of the ASM Volumes page.

To view information about a file system, click the link in the Mount Point column on the ASM Cluster File System page.

To view information about a disk group for an Oracle ACFS, click the disk group name in the Disk Group column on the ASM Cluster File System page. The General tab of the Disk Group page displays.

To view information about volumes in a disk group, click the Volumes tab at the top of the Disk Group page.

### Managing Oracle ACFS Snapshots with Oracle Enterprise Manager

This section describes how to manage snapshots with Oracle Enterprise Manager.

- Creating, Modifying, and Viewing Snapshots
- Converting Snapshots Between Read-Only and Read-Write
- Creating Child Snapshots from Existing Snapshots

For more information about Oracle ACFS snapshots, refer to " [About Oracle ACFS Snapshots](understand-acfs-concepts.md) ".

#### Creating, Modifying, and Viewing Snapshots

To view and modify information about existing snapshots or create snapshots for a file system, perform the following steps.

1. Click the ASM Cluster File System tab on the Oracle ASM home page
2. Click a mount point link in the Mount Point column.
3. Click the Snapshots tab.

Optionally, you can click a number link for existing snapshots in the Snapshots column on the ASM Cluster File System page to display the Snapshots page.

On the Snapshots page, you can create snapshots or search for and display specific snapshots. To search for a snapshot, enter a name with optional wildcard characters in the search field then click Search.

To create a snapshot, perform the following steps.

1. Click Create in the Snapshots page.
2. Complete the information on the Create Snapshot page.
	Accept the default snapshot name, or provide a name. Optionally, you can choose to delete the oldest snapshot.
3. When you have completed the screen, you can click OK to run the command, or click Show Command to view the generated command.
	For example, the following is a generated command for creating a snapshot:
	```
	/sbin/acfsutil snap create "snapshot_20090702_142135" /oracle/acfsmounts/acfs1
	```
	To run the generated command, you need the appropriate privileges on the host computer. Oracle Enterprise Manager prompts you to enter host credentials if they have not been set up.
	You can also open a Telnet session from the Create Snapshot page to manually enter the generated operating system command.

To drill down in a snapshot directory, click the snapshot name in the Snapshots page to display the Search and List Directory page.

#### Converting Snapshots Between Read-Only and Read-Write

You can use edit snapshot to convert the snapshot attribute between Read Only and Read Write. To edit a snapshot, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the file or directory in which you want to edit a snapshot.
	Enterprise Manager displays ASM Cluster File System page.
3. Click the Snapshots tab.
4. Select the snapshot you want to edit, then click Edit.
	The Snapshot page displays.
5. Change the Attribute. You can choose Read Only or Read Write.
6. Click OK.

#### Creating Child Snapshots from Existing Snapshots

Use the Create Child snapshot operation to create a point-in-time copy of an existing Oracle ACFS snapshot. Future changes to the parent snapshot are not inherited by the child snapshot. To create a child snapshot of an existing snapshot, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the file or directory Mount Point in which you want to create a child snapshot.
	Enterprise Manager displays ASM Cluster File System page.
3. Click the Snapshots tab.
4. Select the parent snapshot you want to use to create a child snapshot, then click Create Child.
	The Create Child Snapshot on ASM Cluster File System page displays.
5. The Snapshot Name field is automatically populated with a default child snapshot name. You can replace the name with a name you designate.
6. Set the Attribute to Read Only or Read Write.
7. Optionally you can turn on the option to delete the oldest snapshot by turning on the delete option. Oracle Enterprise Manager tabulates the number of remaining snapshots before the maximum limit is reached.
8. Click OK to create the child snapshot.
	Oracle Enterprise Manager returns to the Snapshots tab where you can see the new snapshot with its Parent Name listed in the table.

### Managing Encryption Features with Oracle Enterprise Manager

This section describes how to manage encryption with Oracle Enterprise Manager.

- Initializing Oracle ACFS Encryption
- Enabling, Disabling, and Setting Parameters for Encryption On an Oracle ACFS
- Viewing Encryption Status

For more information about Oracle ACFS encryption, refer to " [Oracle ACFS Encryption](understand-acfs-admin.md) ".

#### Initializing Oracle ACFS Encryption

To initialize Oracle ACFS encryption, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click a mount point in the list.
3. Click the Security/Encryption tab to display the Security and Encryption section.
4. In the Encryption Configuration section, you can specify various options, such as Unset Encryption Parameters.
5. If Oracle ACFS encryption is not initialized in the cluster, the Initialize Encryption button displays. Click the button to initialize Oracle ACFS encryption. This operation needs to be performed only once in the cluster.

#### Enabling, Disabling, and Setting Parameters for Encryption On an Oracle ACFS

To enable, disable, or set parameters for Oracle ACFS encryption, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the Mount Point that contains the realms you want to view. The Oracle ACFS home page is displayed for this mount point.
3. Click the Security/Encryption tab.
4. Click Encryption Configuration link to display the Encryption configuration section.

#### Viewing Encryption Status

To view encryption status, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click Show Security and Encryption to display the Security and Encryption section.
	The section displays the mount points and the security and encryption settings for each.

### Managing Tagging Features with Oracle Enterprise Manager

This section describes how to manage tagging with Oracle Enterprise Manager.

- Adding a Tag in Oracle ACFS
- Removing a Tag in Oracle ACFS
- Searching for Tags in Oracle ACFS

For more information about Oracle ACFS tagging, refer to " [Oracle ACFS Tagging](understand-acfs-admin.md) ".

#### Adding a Tag in Oracle ACFS

You can add tags to directories and files that reside in a single Oracle ACFS file system or across multiple Oracle ACFS file systems. With the tag names, you can organize your files or perform operations, such as search and replication.

To add tags for specific files or directories from the ASM Cluster File System Page, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Select the file or directory you want to tag and select Add Tag from the Actions menu, then click Go.
	Enterprise Manager displays the Add Tag page.
3. Add a Tag Name (or a comma-delimited list of names) in the Tag Name box. Optionally, you can turn on the option that enables you to add tags recursively to subdirectories and files.
4. In the Directories and Files section, enter either the directory paths directly as a comma-delimited list in the Enter Directory box, or search for directory paths with the ASM Cluster File System by selecting Search Directory. You can add a directory path by clicking Add.
5. Click OK to add tags.

#### Removing a Tag in Oracle ACFS

You can remove tags for specific files or directories in an Oracle ACFS file system. Optionally, you can recursively apply the remove operation to all subdirectories and files.

To remove tags, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Select the file or directory from which you want to remove tags and select Remove Tag from the Actions menu, then click Go.
	Enterprise Manager displays the Remove Tag page.
3. In the Tag Name box, enter the name of the tag you want to remove or specify a comma-delimited list of tag names to remove. Optionally, you can remove tags recursively from all directories and files that exist in the specified directory paths by turning on the option.
4. In the Directories and Files section, select Enter Directory to enter the directory paths directly as a comma-delimited list, or select Search Directory to search for directory paths within an Oracle ACFS file system. To add directory paths repeatedly from different Oracle ACFS file systems, choose the file system and click Add.
5. Click OK to remove tags.

#### Searching for Tags in Oracle ACFS

You can search for tags from selected files and directories in an Oracle ACFS file system. Optionally, you can recursively apply this operation to all subdirectories and files. To search for tags for specific files or directories in an Oracle ACFS file system, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. From the Action menu, select Search Tags, then click Go.
	Enterprise Manager displays the Search Tags page.
3. In the Search Criteria section, specify a comma-delimited list of tag names in the Tag Name box. Optionally, you can search tags recursively in all directories and files by turning on the option.
4. In the Directories and Files section, select Enter Directory to enter the directory path as a comma-delimited list, or select Search Directory to choose the Oracle ACFS file system and click Add to add directory paths repeatedly from different Oracle ACFS file systems.
5. Click Search.
	The results of the search appear in the Search Results table.
6. Click Return to navigate back to the Oracle ASM home page displaying the ASM Cluster File System tab.
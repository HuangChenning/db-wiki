---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-ii-oracle-asm-instances-and-disk-groups/administering-oracle-asm-with-oracle-enterprise-manager.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Administering Oracle ASM with Oracle Enterprise Manager

Oracle Enterprise Manager Cloud Control provides tools for administering Oracle ASM.

See also

[*Oracle Enterprise Manager Cloud Control Administrator's Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=EMADM-GUID-5BA58E51-3D84-4591-B8CD-AA91B3C00373)

## Accessing the Oracle Automatic Storage Management Home Page

All Oracle ASM administration tasks begin with the Oracle Automatic Storage Management home page in Oracle Enterprise Manager Cloud Control. The Oracle Automatic Storage Management home page displays:

- The status of the Oracle ASM instance.
- A chart that shows the used and free space of each disk group and disk group internal usage.
- A list of databases that are serviced by the Oracle ASM instance.
- A list of Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems that are serviced by the Oracle ASM instance.
- A list of other non-Oracle ACFS volumes.
- A list of alerts for the Oracle ASM instance and the host computer.
- Links to the Oracle ASM Performance, Disk Groups, Configuration, Users, and Oracle ACFS pages.

To access the Oracle Automatic Storage Management home page on a single-instance system:

1. Log in to Oracle Enterprise Manager Cloud Control.
2. Under the **Targets** drop down menu at the top of the page, select **All** **Targets**.
3. In the lists of targets on the **All** **Targets** page, click the target for the Oracle ASM instance.
4. If prompted for Oracle ASM login credentials, then enter the user `SYS`, provide the `SYS` password that was set for the Oracle ASM instance during installation, and connect as `SYSASM`. The Oracle Automatic Storage Management home page displays.

For more information about authentication, refer to [Authentication for Accessing Oracle ASM Instances](administering-oracle-asm-instances.md).

## Configuring Oracle ASM Initialization Parameters with Oracle Enterprise Manager

You can configure Oracle ASM with the Oracle Enterprise Manager Configuration Parameters page.

To configure the Oracle ASM instance:

1. Access the Oracle Automatic Storage Management home page.
2. Click the **Configuration** link at the top of the page to view the Configuration Parameters page.
3. Update the configuration options on the page as follows:
	- Disk Discovery Path ( `ASM_DISKSTRING` initialization parameter)
	Enter a string value.
	- Auto Mount Disk Groups ( `ASM_DISKGROUPS` initialization parameter)
	Enter a string value.
	- Rebalance Power ( `ASM_POWER_LIMIT` initialization parameter)
	Enter an integer value.
	- Preferred Read Failure Groups (Only in Oracle RAC environments) ( `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter)
	Enter a comma-delimited string of values in which each string represents a failure group. This parameter is generally used only for clustered Oracle ASM instances.
4. Click **Apply** to save your changes or click **Revert** to discard any changes made on the page.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions on accessing the Oracle Automatic Storage Management home page
- [ASM\_DISKSTRING](administering-oracle-asm-instances.md) for information about the `ASM_DISKSTRING` initialization parameter
- [ASM\_DISKGROUPS](administering-oracle-asm-instances.md) for information about the `ASM_DISKGROUPS` initialization parameter
- [ASM\_POWER\_LIMIT](administering-oracle-asm-instances.md) for information about the `ASM_POWER_LIMIT` initialization parameter
- [ASM\_PREFERRED\_READ\_FAILURE\_GROUPS](administering-oracle-asm-instances.md) for information about the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter

## Managing Oracle ASM Users with Oracle Enterprise Manager

You can manage Oracle ASM users with the Oracle Enterprise Manager Users page

. Access this page by clicking the Users tab that is near the top center of the Oracle Automatic Storage Management home page.

To manage Oracle ASM users:

1. Access the Oracle Automatic Storage Management home page.
2. Click the **Users** link at the top to view the Users property page.
	`ASMSNMP` is a less privileged user that is primarily used by Oracle Enterprise Manager to monitor Oracle ASM instances. This account is granted the `SYSDBA` privilege. `ASMSNMP` is created by Oracle ASM Configuration Assistant (ASMCA) when an Oracle ASM instance is created.
	Click **Create** to add a new Oracle ASM user. When you add users, Oracle Enterprise Manager displays a Create User page in which you must enter user login credentials that include the user name, password, and password confirmation. You can also grant privileges to the new user by selecting privileges in the Available Privileges column and clicking the right arrow buttons to move privileges to the Granted Privileges column, or move the privilege by double clicking it. The available privileges include SYSDBA, SYSOPER, and SYSASM. Click **OK** to create the user, **Cancel** to cancel the procedure, or **Show SQL** to view the SQL that Oracle Enterprise Manager uses to create the user.
3. To edit a user's properties, select the box in the Select column of the user to edit, then click **Edit**. On the Edit User page, modify the password if needed. You can also alter the privileges that are assigned to the user by selecting the privilege and using the right and left arrow buttons to move the privilege from the Granted Privileges column to the Available Privileges column and vice versa. You can also move the privilege by double clicking it. Click **OK** to edit the user properties, **Revert** to cancel the procedure, or **Show SQL** to view the SQL that Oracle Enterprise Manager uses to edit the user's properties.
4. To delete an Oracle ASM user, select the box in the Select column for the user to delete, then click **Delete**. On the confirmation dialog, click **Yes** to delete the user or **No** to stop the user deletion procedure.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions on accessing the Oracle Automatic Storage Management home page
- [Creating Oracle ASM Instances with ASMCA](managing-oracle-asm-with-asmca.md) for information about creating an Oracle ASM instance with ASMCA
- [Authentication for Accessing Oracle ASM Instances](administering-oracle-asm-instances.md) for information about authentication for Oracle ASM instances
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for information about installing Oracle ASM
- [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=GINST) for information about reviewing database accounts and passwords

## Managing Disk Groups with Oracle Enterprise Manager

This section describes how to manage disk groups.

For more information about managing Oracle ASM disk groups, refer to [Administering Oracle ASM Disk Groups](administering-oracle-asm-disk-groups.md)

### Creating Disk Groups

You can create disk groups with Oracle Enterprise Manager.

You can create additional Oracle ASM disk groups to:

- Have disk groups with different redundancy levels (normal, high, or external), depending on availability requirements and storage system capabilities.
- Separate different classes of storage, such as SCSI drives and SATA drives, into different disk groups. Disks in a disk group should have similar size and performance characteristics.
- Store the fast recovery area in a separate disk group from the database.

To create a disk group:

1. Access the Oracle Automatic Storage Management home page.
2. Click the **Disk** **Groups** link at the top of the page to display the Disk Groups property page.
3. If you are not logged in, then the Log In page appears and you should log in as the `SYS` user, connecting as `SYSASM`. Provide the `SYS` password for the Oracle ASM instance. This password was set up when the Oracle ASM instance was created.
4. Click **Create** and Oracle Enterprise Manager displays a Create Disk Group page. The Create Disk Group page displays a list of Oracle ASM disks that are available to be added to a disk group. This includes disks with a header status of `CANDIDATE`, `PROVISIONED`, or `FORMER`, and so on.
5. To display not only disks that are available to be added to a disk group, but all Oracle ASM disks, including disks that belong to a disk group (header status = `MEMBER` ), select **All Disks** from the Select Member Disks list.
	The page is re-displayed with the complete list of Oracle ASM disks that were discovered by the Oracle ASM instance.
6. Enter the disk name, select a redundancy type (high, normal, or external), and optionally, you can enter a failure group name.
7. Select disks as follows:
	- Select the box to the left of each disk to be included in the new disk group.
		- Optionally, you can enter a disk name, the size of the disk for Oracle ASM to use, and the failure group name.
		- To force the inclusion of a disk in the disk group, select the **Force Usage** box for that disk.
	Caution:
	Selecting the Force Usage box causes the disk to be added to the new disk group even if the disk belongs to another disk group and has valid database data. The existing data is then lost. You must be certain that you are selecting a disk that can legitimately be added to the disk group.
8. Specify a **Disk** **Compatibility** value for the disk group to enable your system to use the latest Oracle ASM features.
	Note:
	You cannot reverse the setting of a disk group compatibility value.
9. Click **OK** to create the disk group or click **Cancel** to stop the disk group creation operation. You can also click **Show SQL** to show the SQL statements that the disk group creation operation uses.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions on accessing the Oracle Automatic Storage Management home page
- [Creating Disk Groups](administering-oracle-asm-disk-groups.md) for information about using the `FORCE` option when creating disk groups
- Configuring Disk Group Compatibility Attributes for information about configuring disk group compatibility attributes
- [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) for information about disk group compatibility attributes
- [Creating Disk Groups](administering-oracle-asm-disk-groups.md) for more information about creating disk groups

### Adding Disks to Disk Groups

You can add disks to disk groups with Oracle Enterprise Manager.

You can add disks to a disk group to increase the storage space in a disk group. If you add multiple disks in a single operation, then Oracle ASM rebalances the disk group to evenly distribute the data on all disks, including the newly added disks.

You can control the power of a rebalance operation with the setting of the Rebalance Power. The higher the number, the faster the rebalance operation completes. Lower numbers cause rebalancing to take longer, but consume fewer processing and I/O resources. This leaves these resources available for the database. The default value of `1` minimizes disruption to the database.

A value of `0` blocks the rebalance operation. Manual or automatic rebalance can then occur later. You might want to postpone rebalancing until there are fewer demands on the database, or when you have completed all of your disk group changes.

To add one or more disks to a disk group:

1. Access the Oracle Automatic Storage Management home page.
2. Click the **Disk** **Groups** link to display the Disk Groups property page.
3. If the Oracle ASM Login page appears, then log in as the `SYS` user, connecting as `SYSASM`. Provide the `SYS` password for the Oracle ASM instance. This password was set up when the Oracle ASM instance was created.
4. Click a link in the **Name** column to select the disk group to which you want to add disks. The Disk Group page appears, displaying a list of disks that are in the disk group.
5. Click **Add** and Oracle Enterprise Manager displays the Add Disks page. This page displays a list of Oracle ASM disks that are available to be added to the disk group. This includes disks with the header status of `CANDIDATE`, `PROVISIONED`, or `FORMER`, and so on.
6. To display not only disks that are available to be added to a disk group, but all of the Oracle ASM disks, including disks that belong to a disk group (header status = `MEMBER` ), select **All Disks** from the Select Member Disks drop-down list on the right hand side of the page. Oracle Enterprise Manager re-displays the page with the complete list of Oracle ASM disks that were discovered by the Oracle ASM instance.
7. Optionally change the rebalance power by selecting a value from the Rebalance Power list.
8. Select disks as follows:
	- Check the box to the left of each disk to be added to the disk group.
		- To force the inclusion of a disk in the disk group, select the **Force Reuse** box in the right-most column.
	Caution:
	The Force Reuse box causes the disk to be added to the disk group even if the disk belongs to another disk group and has valid database data. The existing data is then lost. You must be certain that you are selecting a disk that can legitimately be added to the disk group.
	- Optionally enter an Oracle ASM disk name for each disk. Oracle ASM provides a name if you do not.
9. Click **OK** to add the selected disks.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions on accessing the Oracle Automatic Storage Management home page
- [Manually Rebalancing Disk Groups](administering-oracle-asm-disk-groups.md) and [Tuning Rebalance Operations](administering-oracle-asm-disk-groups.md) for information about controlling rebalance operations
- [ASM\_POWER\_LIMIT](administering-oracle-asm-instances.md) for information about rebalance power settings and the `ASM_POWER_LIMIT` initialization parameter
- [Adding Disks to a Disk Group](administering-oracle-asm-disk-groups.md) for an example of using the `FORCE` option
- [Altering Disk Groups](administering-oracle-asm-disk-groups.md) for more information about modifying disk group properties

### Bringing Disks Online and Offline

Perform the following procedures to bring a disk online or offline:

1. Access the Oracle Automatic Storage Management home page.
	See Accessing the Oracle Automatic Storage Management Home Page for instructions.
2. Click the **Disk Groups** link at the top of the page to view the Disk Groups page.
	Click the name of a disk in the Name column and Oracle Enterprise Manager displays the General page for the disk group to modify.
3. To bring a disk online, select the disk to bring online and click **Online**. If you bring a disk online, then Oracle ASM performs the following:
	- Oracle ASM performs the online operation on the selected disks. You can select one or more or disks, or all of the disks to bring online. If you select all of the disks, then Oracle uses the `ALL` keyword for this operation. Otherwise, only the selected disks are affected by the online operation.
		- During the online process, Oracle Enterprise Manager first places a disk into online mode to accommodate write operations. Then Oracle Enterprise Manager resynchronizes stale data on the disk with the current data until the disk is fully online for read operations; this is the Oracle ASM fast mirror resync feature.
		- You can also choose the By Failure Group view to perform this operation on a selected disk group. In this case, Oracle uses the SQL for `disks` `in` `failure` `group`.
		- You can also select a disk that is online, but Oracle Enterprise Manager ignores that selection and only brings disks online that were previously offline.
		- Click **Yes** on the Oracle Enterprise Manager Confirmation dialog to begin bringing the disk online or click **No** to cancel the operation. You can also click **Show SQL** to review the SQL that Oracle Enterprise Manager uses for the online operation.
4. To take a disk offline, select the disk to take offline and click **Offline**. If you bring a disk offline, then Oracle ASM performs the following:
	- Depending on how much data is stale, the operation may require additional time to complete. You can monitor the operation's progress using the Pending Operations link from the Disk Group home page.
		- The value that you set for Rebalance Power using `ASM_POWER_LIMIT` must be a whole number. The text on the page describes how the value of Rebalance Power affects the fast mirror resync operation. If the `ASM_POWER_LIMIT` is set to `0`, then Oracle ASM does not perform automatic rebalance. For information about rebalance power settings and the `ASM_POWER_LIMIT` initialization parameter, refer to " [ASM\_POWER\_LIMIT](administering-oracle-asm-instances.md) ".
		- By default, the Rebalance Power value uses the value of the `ASM_POWER_LIMIT` initialization parameter.
		- Oracle Enterprise Manager displays an Offline Confirmation page and the text on this page explains that after Oracle Enterprise Manager takes the selected disks offline, the Oracle ASM instance waits for the time interval that is specified by the value that you have set for the `DISK_REPAIR_TIME` initialization parameter before Oracle ASM drops the disks. During the disk repair time period, you can repair the disks and then place them back online. For each disk that you successfully place online, the pending drop operation is canceled and a resynchronization operation begins.
		- If you have set `DISK_REPAIR_TIME` to a large value, for example, greater than one day, then this increases the possibility of data loss. This is because the files in the disk group are protected with a lower degree of redundancy during this period.
	Click **Yes** on the Oracle Enterprise Manager Conformation dialog to begin the offline processing or click **No** to stop the operation. You can also click **Show SQL** to see the SQL that Oracle Enterprise Manager uses for the offline operation.

### Monitoring Disk Group Usage

Perform the following procedures to monitor disk group usage:

To view Oracle ASM disk group usage and free space:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the **Disk** **Groups** link to view the Disk Groups property page.
3. If the Oracle ASM Login page appears, then log in as the `SYS` user, connecting as `SYSASM`. Provide the `SYS` password that was set up for Oracle ASM when the Oracle ASM instance was created.

The Disk Group list page displays all of the disk groups and their space usage information.

The Usable Free column displays the space in megabytes that is available in the disk group. The values in this column consider the redundancy level of the disk group, and exclude the space that the disk group reserves for restoring full redundancy for all files in the disk group after a disk failure.

For more information, see " [Managing Capacity in Disk Groups](administering-oracle-asm-disk-groups.md) " and " [Views Containing Oracle ASM Disk Group Information](using-views-to-display-oracle-asm-information.md) "

### Administering Advanced Disk Group Properties

This section explains how to administer advanced disk group properties.

Perform the following steps to change the values for disk group attributes that can be altered after the disk group has been created.

1. On the Automatic Storage Disk Group List page, click a disk group name and Oracle Enterprise Manager displays the Disk Group home page.
2. Click **Edit** under the Advanced Attributes section.

#### Configuring Disk Group Compatibility Attributes

Specify a **Disk** **Compatibility** value for the disk group to enable your system to use the latest Oracle ASM features.

Note:

You cannot reverse the setting of a disk group compatibility value.

- **ASM** **Compatibility**
	Specify the value that is the minimum software version required for an Oracle ASM instance to mount this disk group.
- **Database** **Compatibility**
	Specify a value that must be less than or equal to the Oracle ASM compatibility. This is the minimum software version that is required for a database instance to use the files in the disk group. If the database compatibility value that you use is greater than the Oracle ASM compatibility, then Oracle Enterprise Manager displays an error.
	Note:
	You cannot modify the database compatibility for an Oracle ASM cluster that is in a rolling migration state.
- **ASM** **Volume**
	Specify a value that is 11.2 or greater to use the Oracle ASM Dynamic Volume Manager (Oracle ADVM) functionality. The `ASM` compatibility of the disk group must be set to `11.2` or greater to enable Oracle ADVM. Also, the Oracle ADVM volume drivers must be loaded in the supported environment.

For information about disk group compatibility attributes, see " [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) ".

#### Configuring Disk Repair Time

Specify a time period that is long enough for you to repair a disk in the disk group.

For information about disk group repair time, see " [Oracle ASM Fast Mirror Resync](administering-oracle-asm-disk-groups.md) ".

#### Configuring Smart Scan Compatibility

Specify to disable or enable smart scan compatibility for the disk group.

This attribute is only applicable to Oracle Exadata storage.

See also

*Oracle Exadata documentation* for information about the `CELL.SMART_SCAN_CAPABLE` attribute

#### Configuring File Access Control

Specify to disable or enable Oracle ASM File Access Control. If Oracle ASM File Access Control is enabled, then specify the default permissions for newly created files in the disk group.

For information about Oracle ASM File Access Control, see " [Managing Oracle ASM File Access Control for Disk Groups](administering-oracle-asm-disk-groups.md) ".

### Specifying a Power Limit For Disk Online

To specify a power limit for disk online, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
2. Select the **Disk Groups** tab. The Disk Groups page is displayed.
3. Select a disk group. The Disk Group page appears and shows all Member Disks that belong to the disk group in the Member Disks table.
4. Select a disk, then click **Online**. The online confirmation page is displayed with the advance option to specify a power limit.
5. Specify the **Power Limit**, then click **Submit**. The disk is set to online with the specified power limit.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions about accessing the Oracle ASM home page
- [Manually Rebalancing Disk Groups](administering-oracle-asm-disk-groups.md) for information about the power option in rebalancing a disk group
- [ASM\_POWER\_LIMIT](administering-oracle-asm-instances.md) for information about the `ASM_POWER_LIMIT` initialization parameter

### Replacing An Existing Disk With a New Disk

To replace an existing disk with a new disk, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the Disk Group tab. The Disk Group page displays.
3. Select a Disk Group. The Disk Group page appears which shows all Member Disks that belong to the disk group.
4. Select an offline disk to replace. The Replace Disks page is displayed.
	Select a new disk of size equal to or greater than the original disk being replaced to ensure the same level of data protection.
5. Select a new disk and then specify the options, such as Rebalance Power, and then click **OK**. The disk is then replaced. Rebalance operations redistribute data evenly across all drives. Oracle ASM automatically rebalances a disk group whenever disks are added or dropped. To manually rebalance all disk groups, you must specify the Rebalance Power. Higher values use more I/O bandwidth and complete rebalance more quickly. Lower values cause rebalance to take longer, but use less I/O bandwidth. Values range from 0 to 1024.

For additional information about replacing a disk, refer to " [Replacing Disks in Disk Groups](administering-oracle-asm-disk-groups.md) ".

### Setting and Modifying Content Type for the Disk Group

To set and modify the content type for a disk group, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the Disk Groups tab. The Disk Group page displays.
3. Click **Create**. In the Disk Resync Attributes section of the Create Disk Group page, you can select the value **Recovery**, **Data** or **System** from the **Content Type** drop-down list. The attribute can be set only if the `ASM` compatibility is greater than or equal to 12.1.0.0.
4. To edit the content type for an existing disk group, navigate to the Disk Group home page by clicking the disk group in the Disk Groups table. The Disk Group home page displays.
5. Click **Edit** in the Advanced Attribute Section. The Edit Advanced Attributes for Disk Group page appears. In the Disk Resync Attributes section, select from the values **Recovery**, **Data**, or **System** from the **Content Type** drop-down list.

For information about the `CONTENT.TYPE` disk group attribute, refer to " [CONTENT.TYPE](administering-oracle-asm-disk-groups.md) ".

### Setting and Modifying the Failure Group Repair Time

To set and modify the Failure Group Repair Time, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the Disk Groups tab. The Disk Groups page displays.
3. Click **Create**. Specify the repair time for the **Failure Group** in the Candidate Member Disks table.
4. To edit an existing Failure Group repair time, from the Disk Group page choose the **Disk Group** for the repair time you want to modify. The Disk Group page appears.
5. In the Advanced Attributes section, click **Edit**. The Edit Advanced Attributes for Disk Group page displays.
6. In the Disk Resync Attributes section, modify the **Failure Group Repair Time**, then click **OK**. The failure Group Repair Time applies to all the failure groups in the disk group except those containing only one disk. This value overrides the disk repair time and is overridden by the actual value provided when a disk is taken offline.

For additional information about setting and modifying the failure group repair time, refer to " [Oracle ASM Fast Mirror Resync](administering-oracle-asm-disk-groups.md) ".

### Running Rebalance on Multiple Disk Groups

Enterprise Manager enables you to rebalance on multiple disk groups and distribute the data copy across other member instances in the cluster. To run rebalance on multiple disk groups, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See "Accessing the Oracle Automatic Storage Management Home Page" for instructions.
2. Click the Disk Group tab. The Disk Group page displays.
3. Select multiple disk groups then click **Rebalance**. The Rebalance Disk Groups Confirmation page appears where you can set the Rebalance Power by displaying Advanced Options.
4. Set the Rebalance Power value, then click **OK**. The command to rebalance is submitted.

For additional information about rebalancing disk groups, refer to " [Manually Rebalancing Disk Groups](administering-oracle-asm-disk-groups.md) ".

### Viewing Rebalance Process Related Data

To view rebalance process-related data, including the number of participating instances on the Pending Operations page, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See "Accessing the Oracle Automatic Storage Management Home Page" for instructions.
2. Click the Disk Group tab. The Disk Groups page displays.
3. Click a Disk Group link. The Disk Group home page General section displays the number of **Pending Operations** as a link to the Pending Operations page.
4. Click the link. Information on the rebalance process, along with details on the number of participating instances, are displayed.

For additional information about rebalancing disk groups, refer to " [Tuning Rebalance Operations](administering-oracle-asm-disk-groups.md) ".

### Setting and Modifying the Thin Provisioned Disk Group Attribute

To set and modify the thin-provisioned disk group attribute, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See "Accessing the Oracle Automatic Storage Management Home Page" for instructions.
2. Click the Disk Groups tab. The Disk Groups page is displayed.
3. Click the Disk Group that contains the Thin Provisioned attribute you want to change. The Disk Group page displays.
4. In the Advance Attributes section, click **Edit**. The Edit Advanced Attributes for Disk Group page displays.
5. In the Thin Provisioning section, select **True** or **False** from the Thin Provisioned field drop-down list. If thin provisioning is enabled, the disk space not in use can be returned to the array. This attribute can be set only if the `ASM` compatibility is greater than or equal to 12.1.0.0.

For information about the `THIN_PROVISIONED` disk group attribute, refer to " [THIN\_PROVISIONED](administering-oracle-asm-disk-groups.md) ".

### Running the On Demand Scrubbing Process

To run the On Demand scrubbing process, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See "Accessing the Oracle Automatic Storage Management Home Page" for instructions.
2. Click the Disk Group tab. The Disk Group page is displayed.
3. Click **Scrub**. The Scrub Disk Group page is displayed where you can use advanced options such as repair, power level, wait and force. You can also use the scrub action on disks and files.
4. Provide the advance option and click **OK**. A background process is initiated that scrubs the disk group.

For additional information about scrubbing disk groups, refer to " [Scrubbing Disk Groups](administering-oracle-asm-disk-groups.md) ".

### Determining Whether Scrubbing Process Is Running

To determine whether the scrubbing process is running, follow these steps:

1. Access the Oracle Automatic Storage Management home page.
	See "Accessing the Oracle Automatic Storage Management Home Page" for instructions.
2. Click the Disk Group tab. The Disk Group page displays.
3. Click a Disk Group link. The Disk Group General Section displays a Pending Operation link if a scrubbing process is ongoing.
4. Click the link. Details on the scrubbing process are displayed.

## Managing Oracle ASM File Access Control with Oracle Enterprise Manager

You can manage Oracle ASM File Access Control with Oracle Enterprise Manager Integration for Oracle ASM File Access Control.

To manage Oracle ASM File Access Control:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the **Disk** **Groups** link to display the Disk Groups property page.
3. Click a link in the **Name** column to select a disk group.
4. Click the **Access** **Control** tab to display the **Access** **Control** page.
	On this page, you can add, remove, or replace users from a user group and create or delete user groups. You can also modify the ownership or permission of files.
	To access files in a disk group, operating system users must be granted access privileges to the disk group. After granted access privileges, users can be added as members of groups. The operating system user who owns the oracle binary for the database instance is automatically added and cannot be removed.
	Oracle ASM File Access Control operations on this page are available when the files are open.

For more information about Oracle ASM File Access Control, see " [Managing Oracle ASM File Access Control for Disk Groups](administering-oracle-asm-disk-groups.md) ".

## Managing Directories, Files, and Aliases with Oracle Enterprise Manager

You can manage directories, files, and aliases with the **Files** tab of the Oracle Enterprise Manager Disk Group page.

To manage Oracle ASM files:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the **Disk** **Groups** link to display the Disk Groups property page.
3. Click a link in the **Name** column to select a disk group.
4. Click the **Files** tab to display the **Files** page.
5. Click the icons to left on the folders to expand or contract the folders. When you expand the folders, you can drill down to individual files.
6. You can select a file with the **Select** box, then click **Rename** to rename the file, click **Edit** to change the properties of a file, or click **Delete** to remove a file. You can click the name of a file to display the properties page.

For more information about managing Oracle ASM files, directories, and aliases, see [Administering Oracle ASM Files, Directories, and Templates](administering-oracle-asm-files-directories-and-templates.md).

## Managing Disk Group Templates with Oracle Enterprise Manager

You can manage disk group templates with the Templates tab of the Disk Group page.

To manage Oracle ASM templates:

1. Access the Oracle Automatic Storage Management home page.
2. Click the **Disk** **Groups** link to display the Disk Groups property page.
3. Click a link in the **Name** column to select a disk group.
4. Click the **Templates** tab to display the Templates page.
5. You can click **Create** to add a new template, click **Edit** to change a page, or click **Delete** to remove a template.
	If you click **Create**, then the Create Template page displays and you can enter a name in the Template Name field. You can also specify a redundancy level or striped granularity.

See also

- Accessing the Oracle Automatic Storage Management Home Page for instructions about accessing the Oracle ASM home page
- [Managing Disk Group Templates](administering-oracle-asm-files-directories-and-templates.md) for more information about disk group templates

## Managing Oracle ASM Filter Driver With Oracle Enterprise Manager

You can manage Oracle ASM Filter Driver with Oracle Enterprise Manager.

This section contains the following sections:

- Discovering ASM Filter Driver Disks
- Provisioning ASM Filter Driver Disks
- Releasing ASM Filter Driver Disks

For more information about managing Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) ".

### Discovering ASM Filter Driver Disks

To discover disks for Oracle ASM Filter Driver follow these steps:

1. From **Targets** menu, select **All Targets.**
2. On the All Targets page, select any target of type **Automatic Storage Management**.
3. On the target home page, from **Automatic Storage Management** menu, select **Configuration Parameters.**
4. On the Configuration page, click **Manage Disk Provisioning.** The ASM Filter Driver Page is displayed.
5. On the Disks available for Provisioning table, click **Discover** to discover additional Oracle ASM disks.
6. In the Discover Disks dialog box, enter additional discovery paths from where you would like to provision disks. If you are providing more than one path, then ensure that the values are separated by a comma.
	For example, `'/dev/','/tmp'`.
7. Click **Ok.**

In the Disks available for Provisioning table, all the disks available in the discovery paths are listed.

### Provisioning ASM Filter Driver Disks

To provision a set of disks for Oracle ASM Filter Driver, follow these steps:

1. From **Targets** menu, select **All Targets.**
2. On the All Targets page, select any target of type **Automatic Storage Management**.
3. On the target home page, from **Automatic Storage Management** menu, select **Configuration Parameters.**
4. On the Configuration page, click **Manage Disk Provisioning.** The ASM Filter Driver Page is displayed.
5. From the Disks available for Provisioning table, select one or more disks, then click **Provision.**
6. The Provision Disks dialog box lists all the disks that were selected for provisioning. You can update the Label info if you want, then click **OK.**

After provisioning, the Oracle ASM disks appear in the Provisioned Disks table. These disks display with their new label. For example, if you select `/dev/loop3` to be provisioned with a label `LOOP3,` then after provisioning the disk displays as `AFD:LOOP3` in the Provisioned Disks table.

After the disks are provisioned, they become eligible to be managed by the Oracle ASM Filter Driver.

### Releasing ASM Filter Driver Disks

To release the disks currently managed by Oracle ASM Filter Driver, follow these steps:

1. From **Targets** menu, select **All Targets.**
2. On the All Targets page, select any target of type **Automatic Storage Management**.
3. On the target home page, from **Automatic Storage Management** menu, select **Configuration Parameters.**
4. On the Configuration page, click **Manage Disk Provisioning.** The ASM Filter Driver Page is displayed.
5. From the Provisioned Disks table, select one or more disks, then click **Release.**
6. In the Release Provisioned Disks dialog box, click **Yes** to release the disks

After the disks are released, they are removed from the Provisioned Disks table. They instead appear in the Disks available for provisioning table as a candidate eligible to be provisioned.

## Monitoring Oracle ASM Performance With Oracle Enterprise Manager

This section describes how to perform the following performance-related Oracle ASM administrative tasks:

- Monitoring General Oracle ASM Performance
- Checking Disk Group Integrity

### Monitoring General Oracle ASM Performance

You can monitor Oracle ASM performance with the Oracle Enterprise Manager Performance page.

To monitor Oracle ASM performance:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the **Performance** link to view the Performance property page.
3. Determine the view and refresh rate of the performance graphs with the **View** and **Refresh** options. Click **Refresh** to manually refresh the graphs. The refresh option has the following two intervals:
	- Manual refresh: manual, 15 second interval, 30 second interval
		- Historical data: Last 24 hours, last 7 days, last 31 days
	For more information, refer to " [Performance and Scalability Considerations for Disk Groups](administering-oracle-asm-disk-groups.md) ".

### Checking Disk Group Integrity

When you check the integrity of Oracle ASM disk groups, Oracle Enterprise Manager performs consistency checks on all of the disk group metadata. If Oracle ASM detects errors, then Oracle ASM stores information about errors in the alert log. To check disk groups, perform the following steps:

1. From the **Disk** **Groups** page, select a disk group in the list and click **Check**.
	A confirmation dialog for the check disk group operation displays.
2. Select **Check Without Repair** to record information about disk group inconsistencies in the alert log. In this operation, Oracle ASM does not resolve the errors. Select **Check And Repair** to attempt to repair errors that Oracle Enterprise Manager identifies during the disk group consistency check.
3. Click **Yes** to start the disk group check operation or **No** to cancel it. You can also select **Show SQL** to review the SQL statements that the disk group check operation uses. Click **OK** to run the check operation as a command. To schedule a job, click **Schedule Job**. Optionally, you can modify or reenter the job name and description. Also provide host credentials and enter the scheduling options by selecting **Immediately** or **Later** and modifying the date and time as needed. Click **OK** to schedule the job or **Cancel** to terminate the job creation process.

## Backing Up Oracle ASM Files with Oracle Enterprise Manager

Oracle recommends that you use RMAN to back up files managed by Oracle ASM.

You can also back up your Oracle ASM managed files by performing a files related operation using the following procedures:

1. Create an alias.
2. Create a directory.
3. Delete the alias and directory.
4. Rename the alias and directory.

See also

- [Performing Oracle ASM Data Migration with RMAN](performing-oracle-asm-data-migration-with-rman.md) for information about migrating data with RMAN
- [Oracle Database 2 Day DBA](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMQS-GUID-C6EEB732-9548-4814-8558-8B903DD74759) for information about the procedures for using RMAN
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=BRADV-GUID-9997EF87-B293-44D4-92F3-DD938E79170D) for additional information about RMAN

## Performing Bad Block Recovery with Oracle Enterprise Manager

The procedures that you use in Oracle Enterprise Manager to perform bad block recovery correspond to the steps that you could manually perform with the `remap` command using the Oracle ASM Command utility (ASMCMD). Use the following procedures to perform bad block recovery:

1. Access the Oracle Automatic Storage Management home page.
	See " Accessing the Oracle Automatic Storage Management Home Page " for instructions.
2. Click the **Disk Groups** link at the top of the page.
3. If you are not logged in, then the Log In page appears and you should log in as the SYS user, connecting as SYSASM. Provide the SYS password for the Oracle ASM instance. This password was set up when the Oracle ASM instance was created.
4. Click a disk group name and Oracle Enterprise Manager displays the disk group home page for that disk group.
5. Click a box in the Select column to the left of a disk in which to recover bad blocks, then click **Recover Bad Blocks**.

Note:

You can only recover bad blocks for disk groups that you have configured with normal or high redundancy; you cannot use this feature for disk groups that you have configured with external redundancy.

## Migrating to Oracle ASM with Oracle Enterprise Manager

This section explains how to use Oracle Enterprise Manager to migrate your database storage to use Oracle ASM.

Perform the following steps to migrate to Oracle ASM:

1. At the top of the Oracle Enterprise Manager Database Instance home page, click the **Administration** pull down list and select **MigratetoOracle ASM**.
2. You may need to set credentials for the database, Oracle ASM, and host.
	If prompted for database login credentials, then enter the user `SYS`, provide the SYS password that was set for the Oracle Database instance during installation, and connect as SYSDBA.
	If prompted for Oracle ASM login credentials, then enter the user `SYS`, provide the SYS password that was set for the Oracle ASM instance during installation, and connect as SYSASM. For more information about authentication, see " [Authentication for Accessing Oracle ASM Instances](administering-oracle-asm-instances.md) ".
3. On the **Migrate Database To ASM: Migration Options Page**, which is the first step in a four-step process, verify the information about the files that you plan to migrate to Oracle ASM. If the target database is in `ARCHIVELOG` mode, then you could perform online or offline migration by selecting the corresponding option. Otherwise, using offline migration is the default. If you perform an online migration, then you can suspend the migration by selecting the check box next to **Suspend Migration Job Before Switching Database To ASM**.
	Additionally, you can enter an e-mail address to which Oracle Enterprise Manager sends a message to notify you about the suspension. By default on this page, the Recovery-related Files option is selected. Deselect this option if you do not want to use it. Also verify the entry for the initialization parameter file. Lastly, the **ParallelizeFileCopy** **Operations** option is selected by default. Deselect this if you do not want Oracle Enterprise Manager to perform copy operations in parallel. Click **Next** when you complete your selections on this page and Oracle Enterprise Manager displays the **MigrateDatabaseTo** **ASM**: **DiskGroupOptions** page.
4. On the Disk Group Options page under Database Area, verify the location where Oracle ASM should create data files, temporary files, redo log files, and control files. Also verify the fast recovery area where Oracle ASM should create the recovery-related files such as archived redo log files, backup files, and so on. Also under fast recovery area, the option for Setup fast recovery area without Migrating Recovery-related Files is selected by default. If needed, change the selection to migrate the files. Click **Next** when you complete your selections on the Disk Group Options page.
5. If you chose to use a fast recovery area and Oracle Enterprise Manager displays a warning that the available space on the disk group is less than the specified fast recovery area size for the migration, then you can either continue by clicking **Yes**, or click **No** to stop the operation and modify your storage.
6. When you continue, Oracle Enterprise Manager displays the Schedule page on which you can specify a job name and a date and time for the migration job to begin. Click **Next** when you have configured your desired settings.
7. Oracle Enterprise Manager displays the Review page on which you can review all of your selections before beginning your migration operation. To expand the tablespace details and review them, click the plus (+) sign next to Tablespaces and Files To Be Migrated. Click **Back** to modify any of your selections or **Submit** **Job** to begin the migration. Click **Cancel** to cancel the operation.
	Note:
	If your migration job fails, then do not start your database until you complete a recovery operation. Otherwise, you may corrupt your database.
8. After you submit your job, Oracle Enterprise Manager should display a confirmation dialog indicating that the migration job was successful. Click **View** **Status** on the confirmation dialog to examine the progress of your migration job.

After the migration job has completed, the Oracle ASM links on the Oracle Enterprise Manager page may not display immediately. You may need to wait for the links to display after a subsequent refresh.

## Monitoring Alerts and Incidents With Oracle ASM Support Workbench

Oracle Enterprise Manager provides Support Workbench to monitor Oracle ASM alerts and incidents.

To access Support Workbench, select **Diagnostics** > **Support** **Workbench** under the **Automatic** **Storage** **Management** target menu at the top of the page.

On the Oracle ASM Support Workbench page **Problems** tab you can view information about current and past problems. You also have options to view additional details and create a package that you can send to Oracle Support Services.

Support Workbench guides you through the packaging process as follows:

1. To create a package, select an incident and click **Package** on the Support Workbench Problems page. The Support Workbench **Select packaging** **mode** page of the wizard displays.
2. On the **Select packaging** **mode** page, select either the **Quick** or **Custom** packaging mode.
3. Depending on the packaging mode chosen, you are presented with various entry fields and options as you click **Next** through the wizard.
	The wizard guides you through the packaging process using a series of steps that include:
	- Viewing and editing the contents of the package
		- Viewing and editing the manifest of the package
		- Adding additional diagnostic details
		- Scheduling the generation and uploading of the package

On the Support Workbench **Checker** **Findings** tab, you can view and edit information about packages created for problems on the Support Workbench **Packages** tab. You can also check findings on the **Checker** **Findings** tab.

See also

[*Oracle Database Administrator's Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-CD3CB35D-969B-4976-B7E3-D3F4E537E1B8) for information about viewing problems with Oracle Enterprise Manager Support Workbench

## Monitoring Oracle Flex ASM

Oracle Enterprise Manager provides functionality to monitor your Oracle Flex ASM configuration.

- On the Oracle Flex ASM home page, you can view and administer components of the Oracle Flex ASM configuration.
- On the Oracle Flex ASM Members page, you can view all the members of the Oracle Flex ASM configuration.
- On the Oracle Flex ASM Topology page, you can view the topology of the Oracle Flex ASM configuration.

For information about Oracle Flex ASM, refer to " [Managing Oracle Flex ASM](managing-oracle-flex-asm.md) ".
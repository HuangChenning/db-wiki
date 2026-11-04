---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iii-oracle-automatic-storage-management-cluster-file-system/administering-oracle-acfs-with-oracle-enterprise-manager.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Administering Oracle ACFS with Oracle Enterprise Manager

Oracle Enterprise Manager Cloud Control provides tools for administering Oracle Automatic Storage Management Cluster File System (Oracle ACFS).

This chapter describes how to administer Oracle Automatic Storage Management Cluster File System (Oracle ACFS) with Oracle Enterprise Manager Cloud Control.

All Oracle ASM administration tasks begin with the Oracle Automatic Storage Management home page in Oracle Enterprise Manager Cloud Control.

Note:

To manage or monitor Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance.

See also

- [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) for information about the Oracle ASM home page and how to access that page
- [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md) for information about using command-line tools to administer Oracle ACFS file systems
- [Basic Steps to Manage Oracle ACFS Systems](managing-oracle-acfs-with-command-line-tools.md) for information about the basic steps for creating Oracle ACFS file systems
- [Managing Oracle Flex ASM](managing-oracle-flex-asm.md) for information about Oracle Flex ASM

## Managing Oracle ACFS File Systems and Volumes with Oracle Enterprise Manager

This section discusses how to manage Oracle ACFS file systems and volumes systems with Oracle Enterprise Manager Cloud Control.

For more information about Oracle ACFS file systems and volumes, refer to " [About Oracle ACFS](introducing-oracle-acfs-and-oracle-advm.md) ".

See also

[*Oracle Enterprise Manager Cloud Control Administrator's Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=EMADM-GUID-5BA58E51-3D84-4591-B8CD-AA91B3C00373)

### Creating Oracle ACFS File Systems and Volumes

To create an Oracle ACFS volume, perform the following steps.

1. Access the **Disk Groups** page from the Oracle ASM home page.
2. Click the **Volumes** link in the **General** tab of the **Disk** **Group** page.
3. Click **Create** in the **Volumes** tab of the **Disk** **Group** page.
	The **Create** **ASM** **Volume** page displays.
	Enter the volume name, disk group name that contains the volume, and the initial size of the volume.
	You can also select the redundancy setting for the volume and the region settings for primary and mirror extents.

To create an Oracle ACFS file system on a volume in a disk group, perform the following steps.

1. Access the **Volumes** tab of the **Disk** **Group** page.
2. Select an existing volume in the disk group and click **Create ASM Cluster File System**.
	The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to `11.2` or higher for the disk group..
3. On the **CreateASMClusterFileSystem** page, enter the information to create a file system. You can optionally register and mount the file system.
	You must enter the volume name. You can enter an optional volume label.
	You can optionally choose to register and mount the file system when it is created. Select a mount point from available directories.
	Enter the host credentials needed to run the command when prompted. To register or mount a file system, you need root or administrator privileges.
	After a directory has been selected, click **Show** **Command** to have Oracle Enterprise Manager generate the commands that you can run at an operating system prompt. Examples of commands on a Linux system are:
	```
	/sbin/mkfs -t acfs -b 4k /dev/asm/volume1-361
	/sbin/acfsutil registry -f -a /dev/asm/volume1-361 /oracle/acfsmounts/acfs2
	/bin/mount -t acfs -rw /dev/asm/volume1-361 /oracle/acfsmounts/acfs2
	```
	You can also generate the commands to register or mount an Oracle ACFS file system on the **ASMCluster FileSystem** tab.

See also

- [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) for information about the Oracle ASM home page and how to access that page
- [Mirroring, Redundancy, and Failure Group Options](administering-oracle-asm-disk-groups.md) for information about redundancy settings
- [ASMCMD Volume Management Commands](managing-oracle-advm-with-asmcmd.md) for information about creating a volume with the ASMCMD `volcreate` command
- [Disk Group Compatibility Attributes](administering-oracle-asm-disk-groups.md) for information about disk group compatibility
- [About the Oracle ACFS Mount Registry](introducing-oracle-acfs-and-oracle-advm.md) for information about the registry process

### Viewing and Modifying Oracle ACFS Volumes and File Systems

To view and modify information about Oracle ACFS file systems, click the **ASM** **Cluster File** **System** link in the Oracle ASM home page.

The **ASM** **Cluster File** **System** tab in Oracle Enterprise Manager lists all of the Oracle ACFS associated with the Oracle ASM instance.

On this page, you can choose to mount, dismount, delete, create snapshot, view content, register, and deregister a selected file system. In addition, you can create a file system, mount all file systems, or dismount all file systems.

For each Oracle ACFS, the columns provide information for Mount Point, Availability, State, Snapshots, Used (%), Used (GB), Size (GB), Allocated Space, Redundancy, Volume, and Disk Group. Redundancy, Volume, and Disk Group columns are on the far right of the page and are not shown in the illustration. The mount point, snapshots, volume, and disk group are provided as links to further information.

To view information about a specific volume, click the volume name in the **Volume** column on the **ASM** **Cluster File** **System** page to display the **General** tab of the ASM **Volumes** page.

To view information about a file system, click the link in the **Mount Point** column on the **ASM** **Cluster File** **System** page.

To view information about a disk group for an Oracle ACFS, click the disk group name in the **Disk Group** column on the **ASM** **Cluster File** **System** page. The **General** tab of the **Disk** **Group** page displays.

To view information about volumes in a disk group, click the **Volumes** tab at the top of the **Disk** **Group** page.

## Managing Oracle ACFS Snapshots with Oracle Enterprise Manager

This section describes how to manage snapshots with Oracle Enterprise Manager.

For more information about Oracle ACFS snapshots, refer to " [About Oracle ACFS Snapshots](introducing-oracle-acfs-and-oracle-advm.md) ".

### Creating, Modifying, and Viewing Snapshots

To view and modify information about existing snapshots or create snapshots for a file system, perform the following steps.

1. Click the **ASM** **Cluster File** **System** tab on the Oracle ASM home page
2. Click a mount point link in the **Mount** **Point** column.
3. Click the **Snapshots** tab.

Optionally, you can click a number link for existing snapshots in the **Snapshots** column on the **ASM** **Cluster File** **System** page to display the **Snapshots** page.

On the **Snapshots** page, you can create snapshots or search for and display specific snapshots. To search for a snapshot, enter a name with optional wildcard characters in the search field then click **Search**.

To create a snapshot, perform the following steps.

1. Click **Create** in the **Snapshots** page.
2. Complete the information on the **Create** **Snapshot** page.
	Accept the default snapshot name, or provide a name. Optionally, you can choose to delete the oldest snapshot.
3. When you have completed the screen, you can click **OK** to run the command, or click **Show** **Command** to view the generated command.
	For example, the following is a generated command for creating a snapshot:
	```
	/sbin/acfsutil snap create "snapshot_20090702_142135" /oracle/acfsmounts/acfs1
	```
	To run the generated command, you need the appropriate privileges on the host computer. Oracle Enterprise Manager prompts you to enter host credentials if they have not been set up.
	You can also open a Telnet session from the **Create** **Snapshot** page to manually enter the generated operating system command.

To drill down in a snapshot directory, click the snapshot name in the **Snapshots** page to display the **Search** **and** **List** **Directory** page.

### Converting Snapshots Between Read-Only and Read-Write

You can use edit snapshot to convert the snapshot attribute between Read Only and Read Write. To edit a snapshot, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the file or directory in which you want to edit a snapshot.
	Enterprise Manager displays ASM Cluster File System page.
3. Click the **Snapshots** tab.
4. Select the snapshot you want to edit, then click **Edit**.
	The Snapshot page displays.
5. Change the Attribute. You can choose **Read Only** or **Read Write**.
6. Click **OK**.

### Creating Child Snapshots from Existing Snapshots

Use the Create Child snapshot operation to create a point-in-time copy of an existing Oracle ACFS snapshot. Future changes to the parent snapshot are not inherited by the child snapshot. To create a child snapshot of an existing snapshot, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the file or directory Mount Point in which you want to create a child snapshot.
	Enterprise Manager displays ASM Cluster File System page.
3. Click the **Snapshots** tab.
4. Select the parent snapshot you want to use to create a child snapshot, then click **Create Child**.
	The Create Child Snapshot on ASM Cluster File System page displays.
5. The Snapshot Name field is automatically populated with a default child snapshot name. You can replace the name with a name you designate.
6. Set the Attribute to **Read Only** or **Read Write**.
7. Optionally you can turn on the option to delete the oldest snapshot by turning on the delete option. Oracle Enterprise Manager tabulates the number of remaining snapshots before the maximum limit is reached.
8. Click **OK** to create the child snapshot.
	Oracle Enterprise Manager returns to the Snapshots tab where you can see the new snapshot with its Parent Name listed in the table.

## Managing Security Features with Oracle Enterprise Manager

This section describes how to manage security with Oracle Enterprise Manager.

For more information about Oracle ACFS security, refer to " [Oracle ACFS Security](introducing-oracle-acfs-and-oracle-advm.md) ".

### Initializing Oracle ACFS Security

Oracle ACFS security provides a unified security infrastructure that allows users to define security policies and groups for accessing file system objects. Oracle ACFS encryption allows users to store data on disk in an encrypted format. To initialize Oracle ACFS security, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a mount point in the list.
3. Click the **Security/Encryption** to display the Security and Encryption section.
4. In the **Security** **Configuration** section, you can click **Configuration**, **Rules**, **Rulesets**, and **Realms** under **Security** to display various options.
5. If Oracle ACFS security is not initialized in the cluster, the **Initialize** **Security** button displays on the page. Click the button to initialize Oracle ACFS security. This operation needs to be performed only once in the cluster. On this page, you can also prepare security for the file system.

### Preparing an Oracle ACFS For Security

To prepare an Oracle ACFS for security, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** of the file system for which you want to prepare security.
	Enterprise Manager displays the ASM Cluster File System page for that mount point.
3. Click the **Security/Encryption** tab to display the Security Overview section. This page shows the security details for the current file system.
4. From the Actions menu, click **Prepare Security**.

### Undoing Oracle ACFS Security

To undo preparation for Oracle ACFS security, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** of the file system for which you want to unprepare security.
	Enterprise Manager displays the ASM Cluster File System page for that mount point.
3. Click the **Security/Encryption** tab to display the Security Overview section. This page shows the security details for the current file system.
4. From the Actions menu, click **Unprepare Security**.

### Enabling Security on Oracle ACFS

To enable security on Oracle ACFS, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** of the file system for which you want to enable security.
	Enterprise Manager displays the ASM Cluster File System page for that mount point.
3. Click the **Security/Encryption** tab to display the Security Overview section. This page shows the security details for the current file system.
4. From the Actions menu, click **Enable Security**.

### Disabling Security on Oracle ACFS

To disable security on an Oracle ACFS, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** of the file system for which you want to disable security.
	Enterprise Manager displays the ASM Cluster File System page for that mount point.
3. Click the **Security/Encryption** tab to display the Security Overview section. This page shows the security details for the current file system.
4. From the Actions menu, click **Disable Security**.

### Viewing Security Status

To view security status, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **Show Security and Encryption** to display the Security and Encryption section.
	The section displays the mount points and the security and encryption settings for each.

### Adding an Oracle ACFS Security Administrator

To add an Oracle ACFS security administrator, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **ShowSecurityand** **Encryption** to display the **SecurityandEncryption** section.
3. The list of Oracle ACFS security administrators in this cluster is displayed. Click the **Create** button. The **Create** **Administrator** page is displayed.
4. Enter the input details and click **OK**.

### Changing an Oracle ACFS Security Administrator Password

To change an Oracle ACFS security administrator password, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **ShowSecurityand** **Encryption** to display the **SecurityandEncryption** section.
3. The list of Oracle ACFS security administrators in this cluster is displayed. Select a security administrator and click the **Change** **Password** button. The **ChangeAdministratorPassword** page is displayed.
4. Enter the input details and click **OK**.

### Deleting an Oracle ACFS Security Administrator

To delete an Oracle ACFS security administrator, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **ShowSecurityand** **Encryption** to display the **SecurityandEncryption** section.
3. The list of Oracle ACFS security administrators in this cluster is displayed. Click the **Delete** button.

### Viewing Oracle ACFS Security Administrators

To view Oracle ACFS security administrators, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **ShowSecurityand** **Encryption** to display the **SecurityandEncryption** section.
3. The list of Oracle ACFS security administrators in this cluster is displayed.

### Creating a Rule

Rules are created in a file system and can be added to one or more rulesets, which can then be applied on an Oracle ACFS realm. Rules can also be cloned within the same file system or across file systems.

To create a rule, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rules.**
	The list of rules in the mount point is displayed.
5. Click **Create**. The Create Rule page displays along with the available rule options.
6. Enter the input details and click **OK**.

### Cloning a Rule

Rules can be cloned within the same mount point or across mount points. To clone a rule, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rules**.
	The list of rules in the mount point is displayed.
5. Click **Clone**. The Clone Rule page is displayed with the available rule options.
6. Enter the input details and click **OK**.

### Editing a Rule

You can modify values and options for an existing rules. Rule types cannot be changed. To edit a rule, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rules**.
	The list of rules in the mount point is displayed.
5. Select a rule and click **Edit**.
6. Edit the input details and click **OK**.

### Deleting a Rule

You can delete a rule so it no longer is used to enforce security on realms. To delete a rule, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rules**.
	The list of rules in the mount point is displayed.
5. Select a rule and click the **Delete Rule** button.

### Searching For and Viewing Rules

You can view or search the list of rules on a mount point, including the details of each rule. To search for and view rules, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the **Security** section, click **Rules**.
	The list of rules in the file system is displayed.

### Creating a Ruleset

You can create a ruleset which is a collection of one or more rules that you can associate with a command rule for realm authorization. A ruleset evaluates to true or false based on the evaluation of each rule it contains and the evaluation type (All True or Any True). Rulesets cannot be applied on an Oracle ACFS security realm directly; they are always associated with a Command Rule, which are then applied on a realm to enforce security. To create a ruleset, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rulesets**.
	The list of rulesets in the mount point is displayed.
5. Click **Create**. The Create Ruleset page is displayed along with the available ruleset options.
6. Enter the input details and click **OK**.

### Cloning a Ruleset

Rulesets can be cloned within the same mount point or across mount points. To clone a ruleset, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rulesets**.
	The list of rulesets in the mount point is displayed.
5. Click the ruleset you want to clone then click **Clone**. The Clone Ruleset page is displayed along with the available ruleset options.
6. Enter input details and click **OK**.

### Editing a Ruleset

You can add or delete rules to or from a Ruleset. You can also edit the Ruleset options. To edit a ruleset, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rulesets**.
	The list of rulesets in the mount point is displayed.
5. Select a ruleset and click **Edit**. The Edit Ruleset page is displayed along with all the ruleset values.
6. Edit the ruleset details and click **OK**.

### Deleting a Ruleset

Deleted rulesets are no longer used to enforce security on realms. To delete a ruleset, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Rulesets**.
	The list of rulesets in the mount point is displayed.
5. Select a ruleset and click **Delete**.

### Searching For and Viewing Rulesets

A ruleset is a collection of one or more rules that you can associate with a command rule for realm authorization. A ruleset evaluates to true or false based on the evaluation of each rule it contains and the evaluation type (All True or Any True). Enterprise Manager enables you to view and search the list of rulesets applied on an Oracle ACFS mount point, including the details of each ruleset. To search for and view rulesets, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the **Security** section, click **Rulesets**.
	The list of rulesets in the file system is displayed.

### Creating a Realm

Oracle ACFS Security realms provide the capability to classify file system objects into functional groups to provide fine-grained access control to data stored in these objects.

Realms are created at the file system level. To enforce security on the file objects in a realm, a ruleset is associated with a command rule which is then applied on the realm.

To create a realm, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Realms**.
5. Click **Create**. The Create Realm wizard displays along with the available realm options.
6. Enter the input details and click **OK**.

### Cloning a Realm

Cloning a realm creates a new realm with all the objects of which the cloned realm consists. To clone a realm, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a **Mount Point**. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Realms**. The list of realms in the mount point is displayed.
5. Select a realm and click **Clone Realm**. The **Clone** **Realm** page is displayed along with the available realm options. A realm can be cloned within the same mount point with a different name or across mount points. You can choose the properties; such as users, groups, and encryption; to propagate to the cloned realm.
6. Enter the input details and click **OK**.

### Adding Objects to a Realm

Once a realm is created, you can add objects to a realm. To add objects to a realm, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** that contains the realm to which you want to add objects. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Realms**. The list of realms in the mount point is displayed.
5. Select a realm and click the **Edit** button. The Edit Realm wizard displays.
6. Click **Next** to move to the Realm Objects page where you can click **Add** to add objects to the realm.
7. Click **Done**.

### Deleting Objects from a Realm

You can delete various objects from a realm. If a file or directory is removed from a realm, it is not subjected to security or encryption that is enforced on the realm. If a command rule is deleted from a realm, it is not evaluated while enforcing security on the realm. The command rule still continues to exist for use in other realms. If an encryption object is removed, it disables encryption on the realm and results in decryption of all encrypted files in the realm.

To delete an object from a realm, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** that contains the realm from which you want to delete objects. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Realms**. The list of realms in the mount point is displayed.
5. Select a realm and click the **Edit** button. The Edit Realm wizard displays.
6. Click **Next** to move to the Realm Objects page where you can click **Remove** to delete objects from the realm.
7. Click **Done**.

### Deleting a Realm

You can delete a realm from an Oracle ACFS file system. After a realm is deleted, access to all objects that were part of the realm is reverted to the state prior to their addition to the realm. These objects are not subjected to security and encryption that were enabled on the realm.

To delete a realm, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** that contains the realm you want to delete. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the Security section, click **Realms**. The list of realms in the mount point is displayed.
5. Select the realm you want to delete and click **Delete**.

### Viewing Realms

To view realms, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click the **Mount Point** that contains the realms you want to view. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. In the **Security** section, click **Realms**. The list of realms in the file system is displayed.

## Managing Encryption Features with Oracle Enterprise Manager

This section describes how to manage encryption with Oracle Enterprise Manager.

- Initializing Oracle ACFS Encryption
- Enabling, Disabling, and Setting Parameters for Encryption On an Oracle ACFS
- Viewing Encryption Status

For more information about Oracle ACFS encryption, refer to " [Oracle ACFS Encryption](introducing-oracle-acfs-and-oracle-advm.md) ".

### Initializing Oracle ACFS Encryption

To initialize Oracle ACFS encryption, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click a mount point in the list.
3. Click the **Security/Encryption** tab to display the Security and Encryption section.
4. In the **Encryption** **Configuration** section, you can specify various options, such as **Unset** **Encryption** **Parameters**.
5. If Oracle ACFS encryption is not initialized in the cluster, the **Initialize** **Encryption** button displays. Click the button to initialize Oracle ACFS encryption. This operation needs to be performed only once in the cluster.

### Enabling, Disabling, and Setting Parameters for Encryption On an Oracle ACFS

To enable, disable, or set parameters for Oracle ACFS encryption, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
2. Click the **Mount Point** that contains the realms you want to view. The Oracle ACFS home page is displayed for this mount point.
3. Click the **Security/Encryption** tab.
4. Click **Encryption** **Configuration** link to display the Encryption configuration section.

### Viewing Encryption Status

To view encryption status, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Click **Show Security and Encryption** to display the Security and Encryption section.
	The section displays the mount points and the security and encryption settings for each.

## Managing Tagging Features with Oracle Enterprise Manager

This section describes how to manage tagging with Oracle Enterprise Manager.

- Adding a Tag in Oracle ACFS
- Removing a Tag in Oracle ACFS
- Searching for Tags in Oracle ACFS

For more information about Oracle ACFS tagging, refer to " [Oracle ACFS Tagging](introducing-oracle-acfs-and-oracle-advm.md) ".

### Adding a Tag in Oracle ACFS

You can add tags to directories and files that reside in a single Oracle ACFS file system or across multiple Oracle ACFS file systems. With the tag names, you can organize your files or perform operations, such as search and replication.

To add tags for specific files or directories from the ASM Cluster File System Page, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Select the file or directory you want to tag and select **Add Tag** from the Actions menu, then click **Go**.
	Enterprise Manager displays the Add Tag page.
3. Add a Tag Name (or a comma-delimited list of names) in the Tag Name box. Optionally, you can turn on the option that enables you to add tags recursively to subdirectories and files.
4. In the Directories and Files section, enter either the directory paths directly as a comma-delimited list in the **Enter Directory** box, or search for directory paths with the ASM Cluster File System by selecting **Search Directory**. You can add a directory path by clicking **Add**.
5. Click **OK** to add tags.

### Removing a Tag in Oracle ACFS

You can remove tags for specific files or directories in an Oracle ACFS file system. Optionally, you can recursively apply the remove operation to all subdirectories and files.

To remove tags, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. Select the file or directory from which you want to remove tags and select **Remove Tag** from the Actions menu, then click **Go**.
	Enterprise Manager displays the Remove Tag page.
3. In the Tag Name box, enter the name of the tag you want to remove or specify a comma-delimited list of tag names to remove. Optionally, you can remove tags recursively from all directories and files that exist in the specified directory paths by turning on the option.
4. In the Directories and Files section, select **Enter Directory** to enter the directory paths directly as a comma-delimited list, or select **Search Directory** to search for directory paths within an Oracle ACFS file system. To add directory paths repeatedly from different Oracle ACFS file systems, choose the file system and click **Add**.
5. Click **OK** to remove tags.

### Searching for Tags in Oracle ACFS

You can search for tags from selected files and directories in an Oracle ACFS file system. Optionally, you can recursively apply this operation to all subdirectories and files. To search for tags for specific files or directories in an Oracle ACFS file system, follow these steps:

1. From the Oracle ASM home page, select the ASM Cluster File System tab to display the mount points in the cluster file system.
	For information about the Oracle ASM home page and how to access that page, see " [Accessing the Oracle Automatic Storage Management Home Page](administering-oracle-asm-with-oracle-enterprise-manager.md) ".
2. From the Action menu, select **Search Tags,** then click **Go**.
	Enterprise Manager displays the Search Tags page.
3. In the Search Criteria section, specify a comma-delimited list of tag names in the Tag Name box. Optionally, you can search tags recursively in all directories and files by turning on the option.
4. In the Directories and Files section, select **Enter Directory** to enter the directory path as a comma-delimited list, or select **Search Directory** to choose the Oracle ACFS file system and click **Add** to add directory paths repeatedly from different Oracle ACFS file systems.
5. Click **Search**.
	The results of the search appear in the Search Results table.
6. Click **Return** to navigate back to the Oracle ASM home page displaying the ASM Cluster File System tab.
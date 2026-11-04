---
title: Managing Oracle Cluster Registry and Voting Disks
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## 3 Managing Oracle Cluster Registry and Voting Disks

Oracle Clusterware includes two important components that manage configuration and node membership: Oracle Cluster Registry (OCR), which also includes the local component Oracle Local Registry (OLR), and voting disks.

- OCR manages Oracle Clusterware and Oracle RAC database configuration information
- OLR resides on every node in the cluster and manages Oracle Clusterware configuration information for each particular node
- Voting disks manage information about node membership. Each voting disk must be accessible by all nodes in the cluster for nodes to be members of the cluster

You can store OCR and voting disks on Oracle Automatic Storage Management (Oracle ASM), or a certified cluster file system.

Oracle Universal Installer for Oracle Clusterware 11g release 2 (11.2), does not support the use of raw or block devices. However, if you upgrade from a previous Oracle Clusterware release, then you can continue to use raw or block devices. Oracle recommends that you use Oracle ASM to store OCR and voting disks.

Oracle recommends that you configure multiple voting disks during Oracle Clusterware installation to improve availability. If you choose to put the voting disks into an Oracle ASM disk group, then Oracle ASM ensures the configuration of multiple voting disks if you use a normal or high redundancy disk group. If you choose to store the voting disks on a cluster file system, then select the option to configure multiple voting disks, in which case you will have to specify three different file systems based on different disks.

If necessary, you can dynamically add or replace voting disks after you complete the Oracle Clusterware installation process without stopping the cluster.

Note:

If you use CRSCTL to add a new voting disk to a raw device after installation, then the file permissions of the new voting disk on remote nodes may be incorrect. On each remote node, check to ensure that the file permissions for the voting disk are correct (owned by the Grid Infrastructure installation owner and by members of the OINSTALL group). If the permissions are incorrect, then change them manually.

For example:

```
grid@myserver>$ ls -l /dev/rhdisk18
crwxrwxrwx  1 root  oinstall  36, 02 Feb 10 20:28 /dev/rhdisk18
$ su root
root@myserver> # chown grid:oinstall /dev/rhdisk18
# exit
$ ls -l /dev/rhdisk18
crwxrwxrwx  1001 grid  oinstall  36, 19 Sep 09 20:29 /dev/rhdisk18
```

This chapter includes the following topics:

- Managing Oracle Cluster Registry and Oracle Local Registry
- Managing Voting Disks

## Managing Oracle Cluster Registry and Oracle Local Registry

This section describes how to manage OCR and the Oracle Local Registry (OLR) with the following utilities: OCRCONFIG, OCRDUMP, and OCRCHECK.

OCR contains information about all Oracle resources in the cluster.

OLR is a registry similar to OCR located on each node in a cluster, but contains information specific to each node. It contains manageability information about Oracle Clusterware, including dependencies between various services. Oracle High Availability Services uses this information. OLR is located on local storage on each node in a cluster. Its default location is in the path `Grid_home` `/cdata/` `host_name``.olr`, where `Grid_home` is the Oracle Grid Infrastructure home, and `host_name` is the host name of the node.

This section describes how to administer OCR in the following topics:

See Also:

["About OCRCONFIG"](ocrsyntax.md) for information about the OCRCONFIG utility, and ["Troubleshooting Oracle Cluster Registry"](ocrsyntax.md) for information about the OCRDUMP and OCRCHECK utilities

### Migrating Oracle Cluster Registry to Oracle Automatic Storage Management

To improve Oracle Clusterware storage manageability, OCR is configured, by default, to use Oracle ASM in Oracle Database 11g release 2 (11.2). With the Oracle Clusterware storage residing in an Oracle ASM disk group, you can manage both database and clusterware storage using Oracle Enterprise Manager.

However, if you upgrade from a previous version of Oracle Clusterware, you can migrate OCR to reside on Oracle ASM, and take advantage of the improvements in managing Oracle Clusterware storage.

Note:

If you upgrade from a previous version of Oracle Clusterware to 11g release 2 (11.2) and you want to store OCR in an Oracle ASM disk group, then you must set the ASM Compatibility compatibility attribute to `11.2.0.0`.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG02700) for information about setting Oracle ASM compatibility attributes

To migrate OCR to Oracle ASM using OCRCONFIG:

1. Ensure the upgrade to Oracle Clusterware 11g release 2 (11.2) is complete. Run the following command to verify the current running version:
	```
	$ crsctl query crs activeversion
	```
2. Use the Oracle ASM Configuration Assistant (ASMCA) to configure and start Oracle ASM on all nodes in the cluster.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmca.htm#OSTMG50000) for more information about using ASMCA
3. Use ASMCA to create an Oracle ASM disk group that is at least the same size of the existing OCR and has at least normal redundancy.
	Notes:
	- If OCR is stored in an Oracle ASM disk group with external redundancy, then Oracle recommends that you add another OCR location to another disk group to avoid the loss of OCR, if a disk fails in the disk group.
		Oracle does not support storing OCR on different storage types simultaneously, such as storing OCR on both Oracle ASM and a shared file system, except during a migration.
	- If an Oracle ASM instance fails on any node, then OCR becomes unavailable on that particular node.
		If the `crsd` process running on the node affected by the Oracle ASM instance failure is the [OCR writer](glossary.md), the majority of the OCR locations are stored in Oracle ASM, and you attempt I/O on OCR during the time the Oracle ASM instance is down on this node, then `crsd` stops and becomes inoperable. Cluster management is now affected on this particular node.
		Under no circumstances will the failure of one Oracle ASM instance on one node affect the whole cluster.
	- Ensure that Oracle ASM disk groups that you create are mounted on all of the nodes in the cluster.
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more detailed sizing information
4. To add OCR to an Oracle ASM disk group, ensure that the [Oracle Clusterware stack](glossary.md) is running and run the following command as `root`:
	```
	# ocrconfig -add +new_disk_group
	```
	You can run this command more than once if you add multiple OCR locations. You can have up to five OCR locations. However, each successive run must point to a different disk group.
5. To remove storage configurations no longer in use, run the following command as `root`:
	```
	# ocrconfig -delete old_storage_location
	```
	Run this command for every configured OCR.

The following example shows how to migrate two OCRs to Oracle ASM using OCRCONFIG.

```
# ocrconfig -add +new_disk_group
# ocrconfig -delete /dev/raw/raw2
# ocrconfig -delete /dev/raw/raw1
```

Note:

OCR inherits the redundancy of the disk group. If you want high redundancy for OCR, you must configure the disk group with high redundancy when you create it.

#### Migrating Oracle Cluster Registry from Oracle ASM to Other Types of Storage

To migrate OCR from Oracle ASM to another storage type:

1. Ensure the upgrade to Oracle Clusterware 11g release 2 (11.2) is complete. Run the following command to verify the current running version:
	```
	$ crsctl query crs activeversion
	```
2. Create a file in a shared or cluster file system with the following permissions: `root`, `oinstall`, `640`.
	Note:
	Create at least two mirrors of the primary storage location to eliminate a single point of failure for OCR. OCR supports up to five locations.
3. Ensure there is at least 280 MB of space on the mount partition.
4. Ensure that the file you created is visible from all nodes in the cluster.
5. To add the file as an OCR location, ensure that the Oracle Clusterware stack is running and run the following command as `root`:
	```
	# ocrconfig -add file_location
	```
	You can run this command more than once if you add more than one OCR location. Each successive run of this command must point to a different file location.
6. To remove storage configurations no longer in use, run the following command as `root`:
	```
	# ocrconfig -delete +asm_disk_group
	```
	You can run this command more than once if there is more than one OCR location configured.

The following example shows how to migrate OCR from Oracle ASM to block devices using OCRCONFIG. For OCRs not stored on Oracle ASM, Oracle recommends that you mirror OCR on different devices.

```
# ocrconfig -add /dev/sdd1
# ocrconfig -add /dev/sde1
# ocrconfig -add /dev/sdf1
# ocrconfig -delete +unused_disk_group
```

### Adding, Replacing, Repairing, and Removing Oracle Cluster Registry Locations

The Oracle installation process for Oracle Clusterware gives you the option of automatically mirroring OCR. You can manually put the mirrored OCRs on a shared network file system (NFS), or on any cluster file system that is certified by Oracle. Alternatively, you can place OCR on Oracle ASM and allow it to create mirrors automatically, depending on the redundancy option you select.

This section includes the following topics:

- Adding an Oracle Cluster Registry Location
- Removing an Oracle Cluster Registry Location
- Replacing an Oracle Cluster Registry Location
- Repairing an Oracle Cluster Registry Configuration on a Local Node
- Overriding the Oracle Cluster Registry Data Loss Protection Mechanism

You can manually mirror OCR, as described in the "Adding an Oracle Cluster Registry Location" section, if you:

- Upgraded to Oracle Clusterware 11g release 2 (11.2) but did not choose to mirror OCR during the upgrade
- Created only one OCR location during the Oracle Clusterware installation

Oracle recommends that you configure:

- At least three OCR locations, if OCR is configured on non-mirrored or non-redundant storage. Oracle strongly recommends that you mirror OCR if the underlying storage is not RAID. Mirroring can help prevent OCR from becoming a single point of failure.
- At least two OCR locations if OCR is configured on an Oracle ASM disk group. You should configure OCR in two independent disk groups. Typically this is the work area and the recovery area.
- At least two OCR locations if OCR is configured on mirrored hardware or third-party mirrored volumes.

Notes:

- If the original OCR location does not exist, then you must create an empty (0 byte) OCR location with appropriate permissions before you run the `ocrconfig -add` or `ocrconfig -replace` commands.
- Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
- Ensure that the Oracle ASM disk group that you specify exists and is mounted.
- The new OCR file, device, or disk group must be accessible from all of the active nodes in the cluster.

See Also:

- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management

In addition to mirroring OCR locations, you can also:

- Replace an OCR location if there is a misconfiguration or other type of OCR error, as described in the "Replacing an Oracle Cluster Registry Location" section.
- Repair an OCR location if Oracle Database displays an OCR failure alert in Oracle Enterprise Manager or in the Oracle Clusterware alert log file, as described in the "Repairing an Oracle Cluster Registry Configuration on a Local Node" section.
- Remove an OCR location if, for example, your system experiences a performance degradation due to OCR processing or if you transfer your OCR to RAID storage devices and choose to no longer use multiple OCR locations, as described in the "Removing an Oracle Cluster Registry Location" section.

Note:

The operations in this section affect OCR clusterwide: they change the OCR configuration information in the `ocr.loc` file on Linux and UNIX systems and the Registry keys on Windows systems. However, the `ocrconfig` command cannot modify OCR configuration information for nodes that are shut down or for nodes on which Oracle Clusterware is not running.

#### Adding an Oracle Cluster Registry Location

Use the procedure in this section to add an OCR location. Oracle Clusterware can manage up to five redundant OCR locations.

Note:

If OCR resides on a cluster file system file or a network file system, create an empty (0 byte) OCR location file before performing the procedures in this section.

As the `root` user, run the following command to add an OCR location to either Oracle ASM or other storage device:

```
# ocrconfig -add +asm_disk_group | file_name
```

Note:

On Linux and UNIX systems, you must be `root` to run `ocrconfig` commands. On Windows systems, the user must be a member of the Administrator's group.

#### Removing an Oracle Cluster Registry Location

To remove an OCR location or a failed OCR location, at least one other OCR must be online. You can remove an OCR location to reduce OCR-related overhead or to stop mirroring your OCR because you moved OCR to redundant storage such as RAID.

Perform the following procedure as the `root` user to remove an OCR location from your Oracle Clusterware environment:

1. Ensure that at least one OCR location other than the OCR location that you are removing is online.
	Caution:
	Do not perform this OCR removal procedure unless there is at least one other active OCR location online.
2. Run the following command on any node in the cluster to remove an OCR location from either Oracle ASM or other location:
	```
	# ocrconfig -delete +ASM_disk_group | file_name
	```
	The `file_name` variable can be a device name or a file name. This command updates the OCR configuration on all of the nodes on which Oracle Clusterware is running.

#### Replacing an Oracle Cluster Registry Location

If you must change an existing OCR location, or change a failed OCR location to a working location, then you can use the following procedure, as long as all remaining OCR locations remain online. The `ocrconfig -replace` command requires that at least two OCR locations are configured.

To change an Oracle Cluster Registry location:

Complete the following procedure:

1. Use the OCRCHECK utility to verify that a copy of OCR other than the one you are going to replace is online, using the following command:
	```
	$ ocrcheck
	```
	OCRCHECK displays all OCR locations that are registered and whether they are available (online). If an OCR location suddenly becomes unavailable, then it might take a short period for Oracle Clusterware to show the change in status.
	Note:
	The OCR location that you are replacing can be either online or offline.
2. Use the following command to verify that Oracle Clusterware is running on the node on which the you are going to perform the replace operation:
	```
	$ crsctl check crs
	```
3. Run the following command as `root` to replace the current OCR location using either `destination_file` or `+` `ASM_disk_group` to indicate the current and target OCR locations:
	```
	# ocrconfig -replace current_OCR_location -replacement new_OCR_location
	```
	The preceding command fails if you have less than two configured OCR locations that are online.
	If you have only one OCR location configured and online, then you must first add a new location and then delete the failed location, as follows:
	```
	# ocrconfig -add new_OCR_location
	# ocrconfig -delete current_OCR_location
	```
	Note:
	If your cluster configuration changes while the node on which OCR resides is stopped, and the Oracle Clusterware stack is running on the other nodes, then OCR detects configuration changes and self-corrects the configuration by changing the contents of the `ocr.loc` file.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_rman.htm#OSTMG12000) for more information about migrating storage

#### Repairing an Oracle Cluster Registry Configuration on a Local Node

It may be necessary to repair OCR if your cluster configuration changes while that node is stopped and this node is the only member in the cluster. Repairing an OCR involves either adding, deleting, or replacing an OCR location. For example, if any node that is part of your current Oracle RAC cluster is shut down, then you must update the OCR configuration on the stopped node to let that node rejoin the cluster after the node is restarted. Use the following command syntax as `root` on the restarted node where you use either a `destination_file` or `+` `ASM_disk_group` to indicate the current and target OCR locations:

```
ocrconfig -repair -replace current_OCR_location -replacement target_OCR_location
```

This operation only changes OCR on the node on which you run this command. For example, if the OCR location is `/dev/sde1`, then use the command syntax `ocrconfig -repair -add /dev/sde1` on this node to repair OCR on that node.

Notes:

- You cannot repair the OCR configuration on a node on which the Oracle Cluster Ready Services daemon is running.
- When you repair OCR on a stopped node using `ocrconfig -repair`, you must provide the same OCR file name (which should be case-sensitive) as the OCR file names on other nodes.
- If you run the `ocrconfig -add | -repair | -replace` command, then the device, file, or Oracle ASM disk group that you are adding must be accessible. This means that a device must exist. You must create an empty (0 byte) OCR location, or the Oracle ASM disk group must exist and be mounted.

See Also:

- ["OCRCONFIG Command Reference"](ocrsyntax.md) for more information about OCRCONFIG commands
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management

#### Overriding the Oracle Cluster Registry Data Loss Protection Mechanism

OCR has a mechanism that prevents data loss due to accidental overwrites. If you configure a mirrored OCR and if Oracle Clusterware cannot access the mirrored OCR locations and also cannot verify that the available OCR location contains the most recent configuration, then Oracle Clusterware prevents further modification to the available OCR location. In addition, the process prevents overwriting by prohibiting Oracle Clusterware from starting on the node on which only one OCR is available. In such cases, Oracle Database displays an alert message in either Oracle Enterprise Manager, the Oracle Clusterware alert log files, or both. If this problem is local to only one node, you can use other nodes to start your cluster database.

However, if you are unable to start any cluster node in your environment and if you can neither repair OCR nor restore access to all OCR locations, then you can override the protection mechanism. The procedure described in the following list enables you to start the cluster using the available OCR location. However, overriding the protection mechanism can result in the loss of data that was not available when the previous known good state was created.

Caution:

Overriding OCR using the following procedure can result in the loss of OCR updates that were made between the time of the last known good OCR update made to the currently accessible OCR and the time at which you performed the overwrite. In other words, running the `ocrconfig -overwrite` command can result in data loss if the OCR location that you are using to perform the overwrite does not contain the latest configuration updates for your cluster environment.

Perform the following procedure to overwrite OCR if a node cannot start and if the alert log contains CLSD-1009 and CLSD-1011 messages.

1. Attempt to resolve the cause of the CLSD-1009 and CLSD-1011 messages.
	Compare the node's OCR configuration (`ocr.loc` on Linux and UNIX systems and the Registry on Windows systems) with other nodes on which Oracle Clusterware is running.
	- If the configurations do not match, run `ocrconfig -repair`.
		- If the configurations match, ensure that the node can access all of the configured OCRs by running an `ls` command on Linux and UNIX systems. On Windows, use a `dir` command if the OCR location is a file and run `GuiOracleObjectManager.exe` to verify that the part of the cluster with the name exists.
2. Ensure that the most recent OCR contains the latest OCR updates.
	Look at output from the `ocrdump` command and determine whether it has your latest updates.
3. If you cannot resolve the problem that caused the CLSD message, then run the command `ocrconfig -overwrite` to start the node.

### Backing Up Oracle Cluster Registry

This section describes how to back up OCR content and use it for recovery. The first method uses automatically generated OCR copies and the second method enables you to issue a backup command manually:

- Automatic backups: Oracle Clusterware automatically creates OCR backups every four hours. At any one time, Oracle Database always retains the last three backup copies of OCR. The CRSD process that creates the backups also creates and retains an OCR backup for each full day and at the end of each week. You cannot customize the backup frequencies or the number of files that Oracle Database retains.
- Manual backups: Run the `ocrconfig -manualbackup` command on a node where the Oracle Clusterware stack is up and running to force Oracle Clusterware to perform a backup of OCR at any time, rather than wait for the automatic backup. You must run the command as a user with administrative privileges. The `-manualbackup` option is especially useful when you want to obtain a binary backup on demand, such as before you make changes to OCR. The OLR only supports manual backups.

When the clusterware stack is down on all nodes in the cluster, the backups that are listed by the `ocrconfig -showbackup` command may differ from node to node.

Note:

After you install or upgrade Oracle Clusterware on a node, or add a node to the cluster, when the `root.sh` script finishes, it backs up OLR.

Listing Backup Files

Run the following command to list the backup files:

```
ocrconfig -showbackup
```

The `ocrconfig -showbackup` command displays the backup location, timestamp, and the originating node name of the backup files that Oracle Clusterware creates. By default, the `-showbackup` option displays information for both automatic and manual backups but you can include the `auto` or `manual` flag to display only the automatic backup information or only the manual backup information, respectively.

Run the following command to inspect the contents and verify the integrity of the backup file:

```
ocrdump -backupfile backup_file_name
```

You can use any backup software to copy the automatically generated backup files at least once daily to a different device from where the primary OCR resides.

The default location for generating backups on Linux or UNIX systems is `Grid_home` `/cdata/` `cluster_name`, where `cluster_name` is the name of your cluster. The Windows default location for generating backups uses the same path structure. Because the default backup is on a local file system, Oracle recommends that you include the backup file created with the OCRCONFIG utility as part of your operating system backup using standard operating system or third-party tools.

Tip:

You can use the `ocrconfig -backuploc` option to change the location where OCR creates backups. [Appendix G, "Oracle Cluster Registry Utility Reference"](ocrsyntax.md) describes the OCRCONFIG utility options.

Note:

On Linux and UNIX systems, you must be `root` user to run most but not all of the `ocrconfig` command options. On Windows systems, the user must be a member of the Administrator's group.

See Also:

- "Administering Oracle Cluster Registry with Oracle Cluster Registry Export and Import Commands" to use manually created OCR export files to copy OCR content and use it for recovery
- ["OCRCONFIG Command Reference"](ocrsyntax.md) for more information about OCRCONFIG commands

### Restoring Oracle Cluster Registry

If a resource fails, then before attempting to restore OCR, restart the resource. As a definitive verification that OCR failed, run `ocrcheck` and if the command returns a failure message, then both the primary OCR and the OCR mirror have failed. Attempt to correct the problem using the OCR restoration procedure for your platform.

Notes:

- You cannot restore your configuration from an OCR backup file using the `-import` option, which is explained in "Administering Oracle Cluster Registry with Oracle Cluster Registry Export and Import Commands". You must instead use the `-restore` option, as described in the following sections.
- If you store OCR on an Oracle ASM disk group and the disk group is not available, then you must recover and mount the Oracle ASM disk group.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about managing Oracle ASM disk groups

- Restoring the Oracle Cluster Registry on Linux or UNIX Systems
- Restoring the Oracle Cluster Registry on Windows Systems
- Restoring the Oracle Cluster Registry in an Oracle Restart Environment

Restoring the Oracle Cluster Registry on Linux or UNIX Systems

If you are storing OCR on an Oracle ASM disk group, and that disk group is corrupt, then you must restore the Oracle ASM disk group using Oracle ASM utilities, and then mount the disk group again before recovering OCR. Recover OCR by running the `ocrconfig -restore` command, as instructed in the following procedure.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about how to restore Oracle ASM disk groups

Note:

If the original OCR location does not exist, then you must create an empty (0 byte) OCR location with the same name as the original OCR location before you run the `ocrconfig -restore` command.

Use the following procedure to restore OCR on Linux or UNIX systems:

1. List the nodes in your cluster by running the following command on one node:
	```
	$ olsnodes
	```
2. Stop Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl stop crs
	```
	If the preceding command returns any error due to OCR corruption, stop Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl stop crs -f
	```
3. If you are restoring OCR to a cluster file system or network file system, then run the following command as `root` to restore OCR with an OCR backup that you can identify in "Listing Backup Files":
	```
	# ocrconfig -restore file_name
	```
	After you complete this step, proceed to step [^1].
4. Start the Oracle Clusterware stack on one node in exclusive mode by running the following command as `root`:
	```
	# crsctl start crs -excl -nocrs
	```
	The `-nocrs` option ensures that the `crsd` process and OCR do not start with the rest of the Oracle Clusterware stack.
	Ignore any errors that display.
	Check whether `crsd` is running. If it is, then stop it by running the following command as `root`:
	```
	# crsctl stop resource ora.crsd -init
	```
	Caution:
	Do not use the `-init` flag with any other command.
5. If you want to restore OCR to an Oracle ASM disk group, then you must first create a disk group using SQL\*Plus that has the same name as the disk group you want to restore and mount it on the local node.
	If you cannot mount the disk group locally, then run the following SQL\*Plus command:
	```
	SQL> drop diskgroup disk_group_name force including contents;
	```
	Optionally, if you want to restore OCR to a raw device, then you must run the `ocrconfig -repair -replace` command as `root`, assuming that you have all the necessary permissions on all nodes to do so and that OCR was not previously on Oracle ASM.
6. Restore OCR with an OCR backup that you can identify in "Listing Backup Files" by running the following command as `root`:
	```
	# ocrconfig -restore file_name
	```
	Notes:
	- Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	- If you configured OCR in an Oracle ASM disk group, then ensure that the Oracle ASM disk group exists and is mounted.
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
7. Verify the integrity of OCR:
	```
	# ocrcheck
	```
8. Stop Oracle Clusterware on the node where it is running in exclusive mode:
	```
	# crsctl stop crs -f
	```
9. Run the `ocrconfig -repair -replace` command as `root` on all the nodes in the cluster where you did not the `ocrconfig -restore` command. For example, if you ran the `ocrconfig -restore` command on node 1 of a four-node cluster, then you must run the `ocrconfig -repair -replace` command on nodes 2, 3, and 4.
10. Begin to start Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl start crs
	```
11. Verify OCR integrity of all of the cluster nodes that are configured as part of your cluster by running the following CVU command:
	```
	$ cluvfy comp ocr -n all -verbose
	```

See Also:

[Appendix A, "Cluster Verification Utility Reference"](cvu.md) for more information about enabling and using CVU

Restoring the Oracle Cluster Registry on Windows Systems

If you are storing OCR on an Oracle ASM disk group, and that disk group is corrupt, then you must restore the Oracle ASM disk group using Oracle ASM utilities, and then mount the disk group again before recovering OCR. Recover OCR by running the `ocrconfig -restore` command, as instructed in the following procedure.

Note:

If the original OCR location does not exist, then you must create an empty (0 byte) OCR location with the same name as the original OCR location before you run the `ocrconfig -restore` command.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about how to restore Oracle ASM disk groups

Use the following procedure to restore OCR on Windows systems:

1. List the nodes in your cluster by running the following command on one node:
	```
	C:\>olsnodes
	```
2. Stop Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl stop crs
	```
	If the preceding command returns any error due to OCR corruption, stop Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl stop crs -f
	```
3. Start the Oracle Clusterware stack on one node in exclusive mode by running the following command as a member of the Administrators group:
	```
	C:\>crsctl start crs -excl -nocrs
	```
	The `-nocrs` option ensures that the `crsd` process and OCR do not start with the rest of the Oracle Clusterware stack.
	Ignore any errors that display.
4. Restore OCR with the OCR backup file that you identified in "Listing Backup Files" by running the following command as a member of the Administrators group:
	```
	C:\>ocrconfig -restore file_name
	```
	Make sure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	Notes:
	- Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	- Ensure that the Oracle ASM disk group you specify exists and is mounted.
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
5. Verify the integrity of OCR:
	```
	C:\>ocrcheck
	```
6. Stop Oracle Clusterware on the node where it is running in exclusive mode:
	```
	C:\>crsctl stop crs -f
	```
7. Begin to start Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl start crs
	```
8. Run the following Cluster Verification Utility (CVU) command to verify OCR integrity of all of the nodes in your cluster database:
	```
	C:\>cluvfy comp ocr -n all -verbose
	```
	See Also:
	[Appendix A, "Cluster Verification Utility Reference"](cvu.md) for more information about enabling and using CVU

Restoring the Oracle Cluster Registry in an Oracle Restart Environment

Notes:

- OCR is present for backward compatibility.
- Once an OCR location is created, it does not get updated in the Oracle Restart environment.
- If the Oracle Restart home has been backed up, and if there is a failure, then restoring the Oracle Restart home restores OCR.

Use the following procedure to restore OCR in an Oracle Restart environment:

1. Stop Oracle High Availability Services by running the following command on all of the nodes:
	```
	$ crsctl stop has [-f]
	```
2. Run the `ocrcheck -config` command to determine the OCR location and then create an empty (0 byte) OCR location with appropriate permissions in that location.
3. Restore OCR by running the following command as `root`:
	```
	# crsctl pin css -n host_name
	```
	Notes:
	Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs
4. Run the `ocrcheck` command to verify the integrity of OCR:
5. Start Oracle High Availability Services by running the following command on all of the nodes:
	```
	$ crsctl start has
	```

### Diagnosing Oracle Cluster Registry Problems

You can use the OCRDUMP and OCRCHECK utilities to diagnose OCR problems.

See Also:

- ["OCRDUMP Utility Syntax and Options"](ocrsyntax.md) for more information about the OCRDUMP utility
- ["Using the OCRCHECK Utility"](ocrsyntax.md) for more information about the OCRCHECK utility

### Administering Oracle Cluster Registry with Oracle Cluster Registry Export and Import Commands

In addition to using the automatically created OCR backup files, you should also export OCR contents before and after making significant configuration changes, such as adding or deleting nodes from your environment, modifying Oracle Clusterware resources, and upgrading, downgrading or creating a database. Do this by using the `ocrconfig -export` command, which exports OCR content to a file format.

Caution:

Note the following restrictions for restoring OCR:
- The file format generated by `ocrconfig -restore` is incompatible with the file format generated by `ocrconfig -export`. The `ocrconfig -export` and `ocrconfig -import` commands are compatible. The `ocrconfig -manualbackup` and `ocrconfig -restore` commands are compatible. The two file formats are incompatible and must not be interchangeably used.
- When exporting OCR, Oracle recommends including " `ocr` ", the cluster name, and the timestamp in the name string. For example:
	```
	ocr_mycluster1_20090521_2130_export
	```

Using the `ocrconfig -export` command also enables you to restore OCR using the `-import` option if your configuration changes cause errors. For example, if you have configuration problems that you cannot resolve, or if you are unable to restart Oracle Clusterware after such changes, then restore your configuration using the procedure for your platform.

Oracle recommends that you use either automatic or manual backups, and the `ocrconfig -restore` command instead of the `ocrconfig -export` and `ocrconfig -import` commands to restore OCR for the following reasons:

- A backup is a consistent snapshot of OCR, whereas an export is not.
- Backups are created when the system is online. You must shut down Oracle Clusterware on all nodes in the cluster to get a consistent snapshot using the `ocrconfig -export` command.
- You can inspect a backup using the OCRDUMP utility. You cannot inspect the contents of an export.
- You can list backups with the `ocrconfig -showbackup` command, whereas you must keep track of all generated exports.

This section includes the following topics:

- Importing Oracle Cluster Registry Content on Linux or UNIX Systems
- Importing Oracle Cluster Registry Content on Windows Systems

Note:

Most configuration changes that you make not only change OCR contents, the configuration changes also cause file and database object creation. Some of these changes are often not restored when you restore OCR. Do not restore OCR as a correction to revert to previous configurations, if some of these configuration changes should fail. This may result in an OCR location that has contents that do not match the state of the rest of your system.

#### Importing Oracle Cluster Registry Content on Linux or UNIX Systems

Note:

This procedure assumes default installation of Oracle Clusterware on all nodes in the cluster, where Oracle Clusterware autostart is enabled.

Use the following procedure to import OCR on Linux or UNIX systems:

1. List the nodes in your cluster by running the following command on one node:
	```
	$ olsnodes
	```
2. Stop Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl stop crs
	```
	If the preceding command returns any error due to OCR corruption, stop Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl stop crs -f
	```
3. Start the Oracle Clusterware stack on one node in exclusive mode by running the following command as `root`:
	```
	# crsctl start crs -excl
	```
	Ignore any errors that display.
	Check whether `crsd` is running. If it is, stop it by running the following command as `root`:
	```
	# crsctl stop resource ora.crsd -init
	```
	Caution:
	Do not use the `-init` flag with any other command.
4. Import OCR by running the following command as `root`:
	```
	# ocrconfig -import file_name
	```
	If you are importing OCR to a cluster or network file system, then skip to step [^2].
	Notes:
	- If the original OCR location does not exist, then you must create an empty (0 byte) OCR location before you run the `ocrconfig -import` command.
	- Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	- If you configured OCR in an Oracle ASM disk group, then ensure that the Oracle ASM disk group exists and is mounted.
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about creating OCRs
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
5. Verify the integrity of OCR:
	```
	# ocrcheck
	```
6. Stop Oracle Clusterware on the node where it is running in exclusive mode:
	```
	# crsctl stop crs -f
	```
7. Begin to start Oracle Clusterware by running the following command as `root` on all of the nodes:
	```
	# crsctl start crs
	```
8. Verify OCR integrity of all of the cluster nodes that are configured as part of your cluster by running the following CVU command:
	```
	$ cluvfy comp ocr -n all -verbose
	```

Note:

You can only import an exported OCR. To restore OCR from a backup, you must instead use the `-restore` option, as described in "Backing Up Oracle Cluster Registry".

See Also:

[Appendix A, "Cluster Verification Utility Reference"](cvu.md) for more information about enabling and using CVU

#### Importing Oracle Cluster Registry Content on Windows Systems

Note:

This procedure assumes default installation of Oracle Clusterware on all nodes in the cluster, where Oracle Clusterware autostart is enabled.

Use the following procedure to import OCR on Windows systems:

1. List the nodes in your cluster by running the following command on one node:
	```
	C:\>olsnodes
	```
2. Stop Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl stop crs
	```
	If the preceding command returns any error due to OCR corruption, stop Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl stop crs -f
	```
3. Start the Oracle Clusterware stack on one node in exclusive mode by running the following command as a member of the Administrators group:
	```
	C:\>crsctl start crs -excl
	```
	Ignore any errors that display.
	Check whether `crsd` is running. If it is, stop it by running the following command as a member of the Administrators group:
	```
	C:\>crsctl stop resource ora.crsd -init
	```
	Caution:
	Do not use the `-init` flag in any other command.
4. Import OCR by running the following command as a member of the Administrators group:
	```
	C:\>ocrconfig -import file_name
	```
	Make sure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	Notes:
	- If the original OCR location does not exist, then you must create an empty (0 byte) OCR location before you run the `ocrconfig -import` command.
	- Ensure that the OCR devices that you specify in the OCR configuration exist and that these OCR devices are valid.
	- Ensure that the Oracle ASM disk group you specify exists and is mounted.
	See Also:
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for information about creating OCRs
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about Oracle ASM disk group management
5. Verify the integrity of OCR:
	```
	C:\>ocrcheck
	```
6. Stop Oracle Clusterware on the node where it is running in exclusive mode:
	```
	C:\>crsctl stop crs -f
	```
7. Begin to start Oracle Clusterware by running the following command as a member of the Administrators group on all of the nodes:
	```
	C:\>crsctl start crs
	```
8. Run the following Cluster Verification Utility (CVU) command to verify OCR integrity of all of the nodes in your cluster database:
	```
	C:\>cluvfy comp ocr -n all -verbose
	```
	See Also:
	[Appendix A, "Cluster Verification Utility Reference"](cvu.md) for more information about enabling and using CVU

### Oracle Local Registry

In Oracle Clusterware 11g release 2 (11.2), each node in a cluster has a local registry for node-specific resources, called an Oracle Local Registry (OLR), that is installed and configured when Oracle Clusterware installs OCR. Multiple processes on each node have simultaneous read and write access to the OLR particular to the node on which they reside, regardless of whether Oracle Clusterware is running or fully functional.

By default, OLR is located at `Grid_home` `/cdata/` `host_name``.olr` on each node.

Manage OLR using the OCRCHECK, OCRDUMP, and OCRCONFIG utilities as `root` with the `-local` option.

- You can check the status of OLR on the local node using the OCRCHECK utility, as follows:
	```
	# ocrcheck -local
	Status of Oracle Cluster Registry is as follows :
	        Version                  :          3
	        Total space (kbytes)     :     262132
	        Used space (kbytes)      :       9200
	        Available space (kbytes) :     252932
	        ID                       :  604793089
	        Device/File Name         : /private2/crs/cdata/localhost/dglnx6.olr
	                                   Device/File integrity check succeeded
	        Local OCR integrity check succeeded
	```
- You can display the content of OLR on the local node to the text terminal that initiated the program using the OCRDUMP utility, as follows:
	```
	# ocrdump -local -stdout
	```
- You can perform administrative tasks on OLR on the local node using the OCRCONFIG utility.
	- To export OLR to a file:
		```
		# ocrconfig –local –export file_name
		```
		Notes:
		- Oracle recommends that you use the `-manualbackup` and `-restore` commands and not the `-import` and `-export` commands.
		- When exporting OLR, Oracle recommends including " `olr` ", the host name, and the timestamp in the name string. For example:
			```
			olr_myhost1_20090603_0130_export
			```
		- To import a specified file to OLR:
		```
		# ocrconfig –local –import file_name
		```
		- To manually back up OLR:
		```
		# ocrconfig –local –manualbackup
		```
		Note:
		The OLR is backed up at the end of an installation or an upgrade. After that time, you can only manually back up the OLR. Automatic backups are not supported for the OLR. You should create a new backup when you migrate OCR from Oracle ASM to other storage, or when you migrate OCR from other storage to Oracle ASM.
		The default backup location for the OLR is in the path `Grid_home` `/cdata/` `host_name`.
		- To view the contents of the OLR backup file:
		```
		ocrdump -local -backupfile olr_backup_file_name
		```
		- To change the OLR backup location:
		```
		ocrconfig -local -backuploc new_olr_backup_path
		```
		- To restore OLR:
		```
		# crsctl stop crs
		# ocrconfig -local -restore file_name
		# ocrcheck -local
		# crsctl start crs
		$ cluvfy comp olr
		```

### Upgrading and Downgrading the Oracle Cluster Registry Configuration

When you upgrade Oracle Clusterware, it automatically runs the `ocrconfig -upgrade` command. To downgrade, follow the downgrade instructions for each component and also downgrade OCR using the `ocrconfig -downgrade` command. If you are upgrading OCR, then you can use the OCRCHECK utility to verify the integrity of OCR.

## Managing Voting Disks

This section includes the following topics for managing voting disks in your cluster:

- Storing Voting Disks on Oracle ASM
- Backing Up Voting Disks
- Restoring Voting Disks
- Adding, Deleting, or Migrating Voting Disks

Caution:

The `dd` commands used to back up and recover voting disks in previous versions of Oracle Clusterware are not supported in Oracle Clusterware 11g release 2 (11.2). Restoring voting disks that were copied using `dd` or `cp` commands can prevent the Oracle Clusterware 11g release 2 (11.2) stack from coming up. Use the backup and restore procedures described in this chapter to ensure proper voting disk functionality.

Notes:

- Voting disk management requires a valid and working OCR. Before you add, delete, replace, or restore voting disks, run the `ocrcheck` command as `root`. If OCR is not available or it is corrupt, then you must restore OCR as described in "Restoring Oracle Cluster Registry".
- If you upgrade from a previous version of Oracle Clusterware to Oracle Clusterware 11g release 2 (11.2) and you want to store voting disks in an Oracle ASM disk group, then you must set the ASM Compatibility (`COMPATIBLE.ASM`) compatibility attribute to `11.2.0.0`.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG02700) for information about setting Oracle ASM compatibility attributes

### Storing Voting Disks on Oracle ASM

Oracle ASM manages voting disks differently from other files that it stores. If you choose to store your voting disks in Oracle ASM, then Oracle ASM stores all the voting disks for the cluster in the disk group you choose. You cannot use voting disks stored in Oracle ASM and voting disks not stored in Oracle ASM in the same cluster.

Once you configure voting disks on Oracle ASM, you can only make changes to the voting disks' configuration using the `crsctl replace votedisk` command. This is true even in cases where there are no working voting disks. Despite the fact that `crsctl query css votedisk` reports zero vote disks in use, Oracle Clusterware remembers the fact that Oracle ASM was in use and the `replace` verb is required. Only after you use the `replace` verb to move voting disks back to non-Oracle ASM storage are the verbs `add css votedisk` and `delete css votedisk` again usable.

The number of voting files you can store in a particular Oracle ASM disk group depends upon the redundancy of the disk group.

- External redundancy: A disk group with external redundancy can store only one voting disk
- Normal redundancy: A disk group with normal redundancy stores three voting disks
- High redundancy: A disk group with high redundancy stores five voting disks

By default, Oracle ASM puts each voting disk in its own failure group within the disk group. A failure group is a subset of the disks in a disk group. Failure groups define disks that share components, such that if one fails then other disks sharing the component might also fail. An example of what you might define as a failure group would be a set of SCSI disks sharing the same SCSI controller. Failure groups are used to determine which Oracle ASM disks to use for storing redundant data. For example, if two-way mirroring is specified for a file, then redundant copies of file extents must be stored in separate failure groups.

If voting disks are stored on Oracle ASM with normal or high redundancy, and the storage hardware in one failure group suffers a failure, then if there is another disk available in a disk group in an unaffected failure group, Oracle ASM recovers the voting disk in the unaffected failure group.

A normal redundancy disk group must contain at least two failure groups but if you are storing your voting disks on Oracle ASM, then a normal redundancy disk group must contain at least three failure groups. A high redundancy disk group must contain at least three failure groups. However, Oracle recommends using several failure groups. A small number of failure groups, or failure groups of uneven capacity, can create allocation problems that prevent full use of all of the available storage.

You must specify enough failure groups in each disk group to support the redundancy type for that disk group.

Using the `crsctl replace votedisk` command, you can move a given set of voting disks from one Oracle ASM disk group into another, or onto a certified file system. If you move voting disks from one Oracle ASM disk group to another, then you can change the number of voting disks by placing them in a disk group of a different redundancy level as the former disk group.

Notes:

- You cannot directly influence the number of voting disks in one disk group.
- You cannot use the `crsctl add | delete votedisk` commands on voting disks stored in Oracle ASM disk groups because Oracle ASM manages the number of voting disks according to the redundancy level of the disk group.
- You cannot add a voting disk to a cluster file system if the voting disks are stored in an Oracle ASM disk group. Oracle does not support having voting disks in Oracle ASM and directly on a cluster file system for the same cluster at the same time.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about disk group redundancy and quorum failure groups
- "Adding, Deleting, or Migrating Voting Disks" for information about migrating voting disks

### Backing Up Voting Disks

In Oracle Clusterware 11g release 2 (11.2), you no longer have to back up the voting disk. The voting disk data is automatically backed up in OCR as part of any configuration change and is automatically restored to any voting disk added. If all voting disks are corrupted, however, you can restore them as described in "Restoring Voting Disks".

### Restoring Voting Disks

If all of the voting disks are corrupted, then you can restore them, as follows:

1. Restore OCR as described in "Restoring Oracle Cluster Registry", if necessary.
	This step is necessary only if OCR is also corrupted or otherwise unavailable, such as if OCR is on Oracle ASM and the disk group is no longer available.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG137) for more information about managing Oracle ASM disk groups
2. Run the following command as `root` from only one node to start the Oracle Clusterware stack in exclusive mode, which does not require voting files to be present or usable:
	```
	# crsctl start crs -excl
	```
3. Run the `crsctl query css votedisk` command to retrieve the list of voting files currently defined, similar to the following:
	```
	$ crsctl query css votedisk
	--  -----    -----------------                --------- ---------
	##  STATE    File Universal Id                File Name Disk group
	 1. ONLINE   7c54856e98474f61bf349401e7c9fb95 (/dev/sdb1) [DATA]
	```
	This list may be empty if all voting disks were corrupted, or may have entries that are marked as status `3` or `OFF`.
4. Depending on where you store your voting files, do one of the following:
	- If the voting disks are stored in Oracle ASM, then run the following command to migrate the voting disks to the Oracle ASM disk group you specify:
		```
		crsctl replace votedisk +asm_disk_group
		```
		The Oracle ASM disk group to which you migrate the voting files must exist in Oracle ASM. You can use this command whether the voting disks were stored in Oracle ASM or some other storage device.
		- If you did not store voting disks in Oracle ASM, then run the following command using the File Universal Identifier (FUID) obtained in the previous step:
		```
		$ crsctl delete css votedisk FUID
		```
		Add a voting disk, as follows:
		```
		$ crsctl add css votedisk path_to_voting_disk
		```
5. Stop the Oracle Clusterware stack as `root`:
	```
	# crsctl stop crs
	```
	Note:
	If the Oracle Clusterware stack is running in exclusive mode, then use the `-f` option to force the shutdown of the stack.
6. Restart the Oracle Clusterware stack in normal mode as `root`:
	```
	# crsctl start crs
	```

### Adding, Deleting, or Migrating Voting Disks

You can add, remove, and migrate voting disks after you install Oracle Clusterware. Note that the commands you use to do this are different, depending on whether your voting disks are located in Oracle ASM, or are located in another storage option.

Modifying voting disks that are stored in Oracle ASM

- To display the voting disk FUID and file path of each current voting disk, run the `crsctl query css votedisk` command to display output similar to the following:
	```
	$ crsctl query css votedisk
	--  -----    -----------------                --------- ---------
	##  STATE    File Universal Id                File Name Disk group
	 1. ONLINE   7c54856e98474f61bf349401e7c9fb95 (/dev/sdb1) [DATA]
	```
	This command returns a disk sequence number, the status of the disk, the FUID, the path of the disk, and the name of the Oracle ASM disk group on which the disk is stored.
- To migrate voting disks from Oracle ASM to an alternative storage device, specify the path to the non-Oracle ASM storage device with which you want to replace the Oracle ASM disk group using the following command:
	```
	$ crsctl replace votedisk path_to_voting_disk
	```
	You can run this command on any node in the cluster.
- To replace all voting disks not stored in Oracle ASM with voting disks managed by Oracle ASM in an Oracle ASM disk group, run the following command:
	```
	$ crsctl replace votedisk +asm_disk_group
	```

Modifying voting disks that are not stored on Oracle ASM:

- To display the voting disk FUID and file path of each current voting disk, run the following command:
	```
	$ crsctl query css votedisk
	##  STATE    File Universal Id                File Name Disk group
	--  -----    -----------------                --------- ---------
	 1. ONLINE   7c54856e98474f61bf349401e7c9fb95 (/cfs/host09_vd3) []
	```
	This command returns a disk sequence number, the status of the disk, the FUID, and the path of the disk and no name of an Oracle ASM disk group.
- To add one or more voting disks, run the following command, replacing the `path_to_voting_disk` variable with one or more space-delimited, complete paths to the voting disks you want to add:
	```
	$ crsctl add css votedisk path_to_voting_disk [...]
	```
- To replace voting disk A with voting disk B, you must add voting disk B, and then delete voting disk A. To add a new disk and remove the existing disk, run the following command, replacing the `path_to_voting_diskB` variable with the fully qualified path name of voting disk B:
	```
	$ crsctl add css votedisk path_to_voting_diskB -purge
	```
	The `-purge` option deletes existing voting disks.
- To remove a voting disk, run the following command, specifying one or more space-delimited, voting disk FUIDs or comma-delimited directory paths to the voting disks you want to remove:
	```
	$ crsctl delete css votedisk {FUID | path_to_voting_disk[...]}
	```

Note:

If the cluster is down and cannot restart due to lost voting disks, then you must start CSS in exclusive mode by running the following command, as `root`:
```
# crsctl start crs -excl
```

After you start CSS in exclusive mode, you can replace the voting disk, as follows:

```
# crsctl replace votedisk path_to_voting_disk
```

Migrating voting disks to Oracle ASM

To migrate voting disks to Oracle ASM, specify the Oracle ASM disk group name in the following command:

```
$ crsctl replace votedisk +asm_disk_group
```

You can run this command on any node in the cluster.

Verifying the voting disk location

After modifying the voting disk, verify the voting disk location, as follows:

```
$ crsctl query css votedisk
```

See Also:

[Appendix E, "CRSCTL Utility Reference"](crsref.md) for more information about CRSCTL commands

[^1]: Begin to start Oracle Clusterware by running the following command as `root` on all of the nodes:

```
# crsctl start crs
```

[^undefined]: Verify OCR integrity of all of the cluster nodes that are configured as part of your cluster by running the following CVU command:

```
$ cluvfy comp ocr -n all -verbose
```

[^2]: Begin to start Oracle Clusterware by running the following command as `root` on all of the nodes:

```
# crsctl start crs
```

[^undefined]: Verify OCR integrity of all of the cluster nodes that are configured as part of your cluster by running the following CVU command:

```
$ cluvfy comp ocr -n all -verbose
```
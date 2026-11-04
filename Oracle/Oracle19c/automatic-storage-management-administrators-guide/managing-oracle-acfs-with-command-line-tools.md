---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iii-oracle-automatic-storage-management-cluster-file-system/managing-oracle-acfs-with-command-line-tools.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Managing Oracle ACFS with Command-Line Tools

Numerous command-line tools are provided for managing Oracle ASM Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM).

Note:

Oracle does not recommend using identifiers for Oracle Database object names that must be quoted. While the use of quoted identifiers may be valid as names in some command-line tools or in SQL statements, the names may not be valid when using other tools that manage the object.

See also

- About Using Oracle ACFS Command-Line Tools for information about running Oracle ACFS `acfsutil` commands
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SQLRF-GUID-3C59E44A-5140-4BCA-B9E1-3039C8050C49) for more information about naming Oracle Database objects

## Basic Steps to Manage Oracle ACFS Systems

This topic provides an overview of the basic steps when managing Oracle ACFS file systems using command-line utilities.

The examples in this section show operating system commands that are run in a Linux environment system. ASMCMD commands manage the Oracle ADVM volumes, but you can also use SQL\*PLus and Oracle ASM Configuration Assistant (ASMCA) to manage volumes.

### About Using Oracle ACFS Command-Line Tools

This topic provides an overview of the use of Oracle ACFS `acfsutil` commands.

Privileges to Run Oracle ACFS acfsutil Commands

To run many Oracle ACFS `acfsutil` commands, you must be a system administrator or an Oracle ASM administrator user that has been enabled to run the commands. These privileges are described as follows:

On Non-Windows systems:

- For system administrator privileges, you must be the `root` user.
- For Oracle ASM administrator user privileges, you must belong to the `OSASM` group and the `oinstall` group (for the `OINSTALL` privilege ).

On Windows systems:

- For system administrator privileges, you must belong to the `Administrators` group.
- For Oracle ASM administrator user privileges, you must belong to the `ORA_ASMADMIN` group and the `ORA_CRS_USERS` group.

Displaying Help for Oracle ACFS acfsutil Commands

You can display help and usage text for Oracle ACFS `acfsutil` commands with the `h` option. When you include a command or a subcommand with the command, the help and usage display is specific to the command and subcommand entered.

The following example illustrates several different ways to display help and usage text, from the most general to more specific. This example shows the `-h` format to display help on a non-Windows platform. On Windows, use `/h` in place of `-h`.

Example: Displaying help for Oracle ACFS acfsutil commands

```
$ /sbin/acfsutil -h

$ /sbin/acfsutil -h compress
$ /sbin/acfsutil compress -h

$ /sbin/acfsutil -h repl info
$ /sbin/acfsutil repl info -h

$ /sbin/acfsutil -h sec admin info
$ /sbin/acfsutil sec admin info -h
```

Running Oracle ACFS acfsutil Commands on Windows

When the options are specified with Oracle ACFS `acfsutil` commands on a Windows platform, use `/` in place of `-` with the option. For example, you can display help for `acfsutil` commands on a Linux platform with `acfsutil` `-h`. On a Windows platform, use `acfsutil` `/h`.

A mount point on a Windows operating system can be a just the drive letter (`M:`) or a directory including the drive letter (`M:\my_mount_point`).

When an `acfsutil` command on Windows targets the root of the file system that is mounted on a drive letter, include the backslash and a period (`\.`) with the drive letter (`P:\.`) to avoid the possibility of triggering a Windows path substitution to the last accessed path on the specified drive. For example:

```
C:\oracle> acfsutil info fs P:\.
```

Displaying Oracle ACFS Version Information

You can run `acfsutil` `version` to display the Oracle ACFS version. For example:

```
$ /sbin/acfsutil version
acfsutil version: 12.2.0.0.3
```

For more information about displaying Oracle ACFS version details, refer to acfsutil version.

Managing Trace Files for acfsutil Commands

The Automatic Diagnostic Repository (ADR) generates a separate internal file for each `acfsutil` command invocation to trace the operation of the command. The space consumed by these trace files can increase significantly, and some features, such as snapshot-based replication, may generate a significant number of trace files.

To limit the number of trace files and the space consumed by them, you can set policy attributes with the Automatic Diagnostic Repository Command Interpreter (ADRCI) utility to purge trace files after a specified retention period. ADRCI considers trace files to be short-lived files and the retention period is controlled by the setting of the `SHORTP_POLICY` attribute. You can view the current retention period for these trace files with the ADRCI `show` `control` command.

By default, the short-lived files are retained for `720` hours (30 days). The value in hours specifies the number of hours after creation when a given file is eligible for purging. To limit the number of these files and the space consumed by them, you can update the number of hours set for the `SHORTP_POLICY` retention period, such as `240` hours (10 days).

The following steps summarize how to update the retention period for short-lived trace files. These steps should be performed on each node where features like replication will be active.

- Start the Automatic Diagnostic Repository Command Interpreter (ADRCI) utility.
	`$ adrci`
- Display the ADR home directory paths (ADR homes):
	`ADRCI> show homes`
- If more than one home is shown, then set the appropriate home for the trace files you want to administer:
	`ADRCI> set homepath` `my_specified_homepath`
- Display the current configuration values.
	`ADRCI> show control`
- Update a specific ADRCI configuration value. For example, set `SHORTP_POLICY` to `240` hours (10 days).
	In the displayed `show control` output, check the value of the `SHORTP_POLICY` attribute, which is the retention period in hours for short-lived files. If necessary, set a new retention period for short-lived trace files with the following:
	`ADRCI> set control (SHORTP_POLICY=240)`

If you want to start an immediate purge of the trace files in the current ADR home path, you can use the following command:

`ADRCI> purge -type TRACE -age` `number_of_minutes`

The value *number\_of\_minutes* controls which files are purged based on the age of the files. Files older than the specified number of minutes are targeted for the purge operation. Note that automated purges of files in ADR occur on a fixed schedule that is not affected by changes in retention period. In other words, changing the retention period changes how soon after creation files are eligible to be purged, but does not change when a purge occurs. To force a purge, you must request it manually.

See also

- [About Privileges for Oracle ASM](administering-oracle-asm-instances.md) for information about user privileges for Oracle ASM
- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SUTIL-GUID-DC5744C7-FAC0-436B-99D5-DBD45B66930B) for information about the Automatic Diagnostic Repository Command Interpreter (ADRCI) utility

### Creating an Oracle ACFS File System

You can create an Oracle ACFS file system using the steps in this topic.

To create and verify a file system, perform the following steps:

1. Create an Oracle ADVM volume in a mounted disk group with the ASMCMD `volcreate` command.
	The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to `11.2` or higher for the disk group to contain an Oracle ADVM volume. To use Oracle ACFS encryption, replication, security, or tagging, the disk group on which the volume is created for the file system must have compatibility attributes for `ASM` and `ADVM` set to `11.2.0.2` or higher.
	Start ASMCMD connected to the Oracle ASM instance. You must be a user in the OSASM operating system group.
	When configuring Oracle ADVM volume devices within a disk group, Oracle recommends assigning the Oracle Grid Infrastructure user and Oracle ASM administrator roles to users who have root privileges.
	To create a volume:
	```
	ASMCMD [+] > volcreate -G data -s 10G volume1
	```
	When creating an Oracle ADVM volume, a volume device name is created that includes a unique Oracle ADVM persistent disk group number. The volume device file functions in the same manner as any other disk or logical volume to mount file systems or for applications to use directly.
	The format of the volume name is platform-specific.
2. Determine the device name of the volume that was created.
	You can determine the volume device name with the ASMCMD `volinfo` command or from the `VOLUME_DEVICE` column in the `V$ASM_VOLUME` view.
	For example:
	```
	ASMCMD [+] > volinfo -G data volume1
	Diskgroup Name: DATA
	         Volume Name: VOLUME1
	         Volume Device: /dev/asm/volume1-123
	         State: ENABLED
	     ... 
	SQL> SELECT volume_name, volume_device FROM V$ASM_VOLUME 
	     WHERE volume_name ='VOLUME1';
	VOLUME_NAME        VOLUME_DEVICE
	-----------------  --------------------------------------
	VOLUME1            /dev/asm/volume1-123
	```
3. Create a file system with the Oracle ACFS `mkfs` command.
	Create a file system using an existing volume device.
	For example:
	```
	$ /sbin/mkfs -t acfs /dev/asm/volume1-123
	mkfs.acfs: version                   = 19.0.0.0.0
	mkfs.acfs: on-disk version           = 46.0
	mkfs.acfs: volume                    = /dev/asm/volume1-123
	mkfs.acfs: volume size               = 10737418240  (   10.00 GB )
	mkfs.acfs: Format complete.
	```
	The `root` privilege is not required to run `mkfs`. The ownership of the volume device file dictates who can run this command.
4. Register the file system.
	In an Oracle Grid Infrastructure Clusterware configuration, you can run the `srvctl` `add` `filesystem` command to register and automount a file system. For example:
	```
	# srvctl add filesystem -device /dev/asm/volume1-123 -path /acfsmounts/acfs1
	       -user user1,user2,user3 -mountowner sysowner -mountgroup sysgrp -mountperm 755
	```
	You can also register a file system with the `acfsutil` `registry` command. For example:
	```
	$ /sbin/acfsutil registry -a /dev/asm/volume1-123 /acfsmounts/acfs1
	```
	After registering an Oracle ACFS file system in the cluster mount registry, the file system is mounted automatically on each cluster member listed in the registry entry during the next registry check action. This automatic process runs every 30 seconds and eliminates the requirement to manually mount the file system on each member of the cluster. Registering an Oracle ACFS file system also causes the file system to be mounted automatically whenever Oracle Clusterware or the system is restarted.
	Note:
	- The `srvctl` `add` `filesystem` command is required when an Oracle Database home is installed on an Oracle ACFS file system. In this case, the file system should not be explicitly added to the registry with the Oracle ACFS registration command (`acfsutil` `registry`).
		- Oracle ACFS registration is not supported in an Oracle Restart (standalone) configuration, which is a single-instance (non-clustered) environment.
		- The `root` or `asmadmin` privileges are required to modify the registry. The Windows `Administrator` privilege is equivalent to the `root` privilege on Linux.
5. Mount or start the file system.
	If you have previously registered the file system, then start the file system with SRVCTL. For example:
	```
	$ srvctl start filesystem -device /dev/asm/volume1-123
	```
	If you have not previously registered the file system, then mount the file system with the Oracle ACFS `mount` command. For example:
	```
	# /bin/mount -t acfs /dev/asm/volume1-123 /acfsmounts/acf1
	```
	After an unregistered file system has been mounted, ensure that the permissions are set to allow access to the file system for the appropriate users. For example:
	```
	# chown -R oracle:dba /acfsmounts/acfs1
	```
	The `root` privilege is required to run the `mount` command and the Windows `Administrator` privilege is required to run the `acfsmountvol` command.
6. Create a test file in the file system.
	The user that creates the test file should be a user that is intended to access the file system. This test ensures that the appropriate user can write to the file system.
	For example:
	```
	$ echo "Oracle ACFS File System" > /acfsmounts/acfs1/myfile
	```
7. List the contents of the test file that was created in the file system.
	For example:
	```
	$ cat /acfsmounts/acfs1/myfile
	Oracle ACFS File System
	```

See also

- [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md) for information about the `volcreate` command and the `volinfo` command
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-6005A792-228F-44C2-885C-A1F02CA558F6) for information about the `V$ASM_VOLUME` view
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-F2CBA060-E4F2-4EB1-A0A7-11144D68A26A) for information about Server Control Utility (SRVCTL) commands

### Accessing an Oracle ACFS File System on a Different Node in the Cluster

If the node is part of a cluster, perform the following steps on node 2 to view the test file you created on node 1.

Note:

If the file system has been registered with the Oracle ACFS mount registry, you can skip steps 1 to 3.

1. Enable the volume that was previously created and enabled on node 1.
	Start ASMCMD connected to the Oracle ASM instance. You must be a user in the OSASM operating system group.
	For example:
	```
	ASMCMD [+] > volenable -G data volume1
	```
2. View information about the volume that you created on node 1.
	For example:
	```
	ASMCMD [+] > volinfo -G data volume1
	```
3. Mount the file system using the Oracle ACFS `mount` command.
	For example:
	```
	# /bin/mount -t acfs /dev/asm/volume1-123 /acfsmounts/acfs1
	```
	The `root` privilege is required run the `mount` command and the Windows `Administrator` privilege is required to run the `acfsmountvol` command.
	After the file system has been mounted, ensure that the permissions are set to allow access for the appropriate users.
4. List the contents of the test file you previously created on the file system.
	For example:
	```
	$ cat /acfsmounts/acfs1/myfile
	Oracle ACFS File System
	```
	The contents should match the file created previously on node 1.

See also

- [About Privileges for Oracle ASM](administering-oracle-asm-instances.md) for information about operating system groups and privileges.
- [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md) for information about the `volenable` command
- [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md) for information about the `volinfo` command
- mount (Linux environments) or acfsmountvol (Windows) for information about commands to mount Oracle ACFS file systems

### Managing Oracle ACFS Snapshots

To create and verify a snapshot on node 1:

1. Create snapshot of the new file system created on node 1.
	For example:
	```
	$ /sbin/acfsutil snap create mysnapshot_20090725 /acfsmounts/acfs1
	```
	See " acfsutil snap create ".
2. Update the test file in the file system so that it is different than the snapshot.
	For example:
	```
	$ echo "Modifying a file in Oracle ACFS File System" > /acfsmounts/acfs1/myfile
	```
3. List the contents of the test file and the snapshot view of the test file.
	For example:
	```
	$ cat /acfsmounts/acfs1/myfile
	$ cat /acfsmounts/acfs1/.ACFS/snaps/mysnapshot_20090725/myfile
	```
	The contents of the test file and snapshot should be different. If node 1 is in a cluster, then you can perform the same list operation on node 2.

### Securing Oracle ACFS File Systems

The basic operations to manage security for an Oracle ACFS file system on Linux are discussed in this topic.

The scenario in this topic shows how to use Oracle ACFS security to ensure that only the maintenance user can access medical history files during the maintenance period. Oracle ACFS encryption is also enabled on the same file system.

In this scenario, the disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3` or higher.

For the examples in this section, various operating system users, operating system groups, and directories must exist.

The basic steps to manage security are:

1. Initialize security for Oracle ACFS.
	Run the `acfsutil` `sec` `init` command to configure storage for security credentials and identify an operating system user as the first security administrator and the operating system security group. The security administrator must belong to the operating system group. This command must be run before any other security command and requires root or Windows `Administrator` privileges to run.
	The `acfsutil` `sec` `init` command is only run once to set up Oracle ACFS security for each cluster and can be run from any node in the cluster. Other security commands can also be run from any node in a cluster. Security administrators are common for all Oracle ACFS file systems in a cluster.
	For example, the following command initializes security for a cluster and creates the first security administrator (`medHistAdmin1`).
	```
	# /sbin/acfsutil sec init -u medHistAdmin1 -g medHistAdminGrp
	```
	The `medHistAdmin1` security administrator must belong to the `medHistAdminGrp` operating system group. That group is identified as the security group for the security administrators.
	When the root user or Windows `Administrator` user runs the command, the user assigns a security password to the security administrator. Security administrators can change their password with the `acfsutil` `sec` `admin` `password` command.
	All `acfsutil` `sec` commands (other than `acfsutil` `sec` `init`) must be run by an Oracle ACFS security administrator and the administrator is prompted for the security administrator's password when each command is run.
	Note:
	When prompting for the security administrator's password, the following text displays: `Realm` `management` `password`
	The password required is the Oracle ACFS security administrator's password, not the operating system password of the user.
	Security administrators are allowed to browse all directories in an Oracle ACFS file system whether they have the underlying operating system permissions and whether any realm checks allow it. This functionality enables a security administrator to check the location of the files when securing them with Oracle ACFS security realms. However, a security administrator cannot view the contents of individual files without the appropriate operating system and security realm permissions.
2. Add additional security administrators as necessary.
	The first security administrator can add additional security administrators to administer Oracle ACFS security with the `acfsutil` `sec` `admin` `add` command.
	For example, add a new security administrator `medHistAdmin2`.
	```
	$ /sbin/acfsutil sec admin add medHistAdmin2
	```
	The `medHistAdmin2` user must belong to the operating system group (`medHistAdminGrp`) identified as the security administrator group with the `acfsutil` `sec` `init` command.
	The `medHistAdmin2` security administrator should change the assigned temporary security password with the `acfsutil` `sec` `admin` `password` command. The `medHistAdmin2` administrator can add new security administrators.
3. Prepare an Oracle ACFS file system for security.
	Run the `acfsutil` `sec` `prepare` on an Oracle ACFS file system before adding any security realms.
	For example, prepare the Oracle ACFS file system mounted on `/acfsmounts/acfs1` for Oracle ACFS security.
	```
	$ /sbin/acfsutil sec prepare -m /acfsmounts/acfs1
	```
	By default, security is enabled for a file system after running this command. You can explicitly disable or enable security with the `acfsutil` `sec` `disable` or `acfsutil` `sec` `enable` commands.
	This command automatically creates several security realms, such as the `SYSTEM_BackupOperators` security realm. Administrators can add users to the `SYSTEM_BackupOperators` realm which gives those users permissions to make backups of realm-secured files in the Oracle ACFS file system.
4. Provide encryption for this file system.
	Encrypting the file system is optional, but is enabled in this scenario.
	1. First, run the `acfsutil` `encr` `init` command to initialize encryption and create the storage necessary for the encryption keys. This command must be run one time for each cluster on which encryption is set up.
		For example, the following command initializes encryption for a cluster.
		```
		# /sbin/acfsutil encr init
		```
		This command must be run before any other encryption command and requires root or administrator privileges to run.
		2. Next, run the `acfsutil` `encr` `set` command to set encryption for the Oracle ACFS file system.
		For example, the following command sets encryption for the file system mounted on the `/acfsmounts/acfs1` directory.
		```
		# /sbin/acfsutil encr set -m /acfsmounts/acfs1/
		```
		The `acfsutil` `encr` `set` command transparently generates a volume encryption key which is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command. This command requires root or administrator privileges to run.
5. Create a security realm on the file system.
	Run the `acfsutil` `sec` `realm` `create` command to create a security realm for a file system.
	For example, create a security realm named `medHistRealm` which contains medical records files with all files encrypted in the realm.
	```
	$ /sbin/acfsutil sec realm create medHistRealm -m /acfsmounts/acfs1/ 
	                                               -e on -a AES -k 128
	```
	The `-e` option specifies that all the files in the realm are encrypted with the `AES` algorithm and the key length set to 128 bits. The file system must first be prepared for encryption with the `acfsutil` `encr` `init` and `acfsutil` `encr` `set` commands. You do not have to enter the same value for the `-k` option with `acfsutil` `sec` `realm` `create` as you have entered with the `acfsutil` `encr` `set` command.
6. Create security rules.
	Run the `acfsutil` `sec` `rule` `create` command to create rules which determine access to the files and directories of a security realm.
	For example, create rules that can enable the `medMaintenance` user to access medical records for the time period 10 PM to 2 AM for file maintenance. Also, create rules that can deny operations during the time period 8 AM to 9 AM and deny operations to the `medBrowse` user.
	```
	$ /sbin/acfsutil sec rule create medHistRule1a -m /acfsmounts/acfs1/
	      -t time 22:00:00,02:00:00 -o ALLOW
	$ /sbin/acfsutil sec rule create medHistRule1b -m /acfsmounts/acfs1/
	      -t username medMaintenance -o ALLOW
	$ /sbin/acfsutil sec rule create medHistRule1c -m /acfsmounts/acfs1/ 
	      -t time 08:00:00,09:00:00 -o DENY
	$ /sbin/acfsutil sec rule create medHistRule1d -m /acfsmounts/acfs1/ 
	      -t username medBrowse -o DENY
	```
	You can edit rules with the `acfsutil` `sec` `rule` `edit` command.
7. Create security rule sets and add rules to rule sets.
	Run the `acfsutil` `sec` `ruleset` `create` command to create rule sets to which rules can be added.
	For example, create rule sets named `medRuleSet1` and `medRuleSet2` that include rules for operations on the files and directories of the security `medHistRealm` realm.
	```
	$ /sbin/acfsutil sec ruleset create medRuleSet1 -m /acfsmounts/acfs1/
	$ /sbin/acfsutil sec ruleset create medRuleSet2 -m /acfsmounts/acfs1/
	```
	Add existing rules to the rule sets.
	```
	$ /sbin/acfsutil sec ruleset edit medRuleSet1 -m /acfsmounts/acfs1/ 
	           -a medHistRule1a,medHistRule1b -o ALL_TRUE
	$ /sbin/acfsutil sec ruleset edit medRuleSet2 -m /acfsmounts/acfs1/ 
	           -a medHistRule1c,medHistRule1d -o ALL_TRUE
	```
	The `ALL_TRUE` option is the default action, but is added here to emphasize that both rules in each rule set must be true.
8. Add objects to a security realm.
	Run the `acfsutil` `sec` `realm` `add` command to add objects, such as command rules, rule sets, and files, to a security realm. For example, add the `medRuleSet1` and `medRuleSet2` rule sets and all the files in the `/acfsmounts/acfs1/medicalrecords` directory to the `medHistRealm`.
	When adding a rule set to a realm, the rule set is added with a command rule, such as `DELETEFILE:medRuleSet1`. Only one rule set can be included with each command rule. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option.
	The following `acfsutil` `sec` `realm` `add` command enables the `medMaintenance` user to delete medical records during the time period 10 PM to 2 AM, but blocks writing to files during 8 AM to 9 AM.
	```
	$ /sbin/acfsutil sec realm add medHistRealm -m /acfsmounts/acfs1/ 
	        -l DELETEFILE:medRuleSet1 
	        -f -r /acfsmounts/acfs1/medicalrecords
	```
	This `acfsutil` `sec` `realm` `add` command prevents the `medBrowse` user from writing or deleting medical records anytime.
	```
	$ /sbin/acfsutil sec realm add medHistRealm -m /acfsmounts/acfs1/ 
	        -l WRITE:medRuleSet2 
	        -f -r /acfsmounts/acfs1/medicalrecords
	```
	This `acfsutil` `sec` `realm` `add` command adds backup operators to the `SYSTEM_BackupOperators` security realm that was automatically created with the `acfsutil` `sec` `prepare` command.
	```
	$ /sbin/acfsutil sec realm add SYSTEM_BackupOperators -m /acfsmounts/acfs1/ 
	        -G sysBackupGrp
	```
	Users that belong to the `sysBackupGrp` operating system group can now make backups of realm-secured files in the Oracle ACFS file system.
9. Display security information.
	Run the `acfsutil` `sec` `info` command to display information for a security realm. For example, display security information for the `medHistRealm` realm.
	```
	$ /sbin/acfsutil sec info -m /acfsmounts/acfs1/ -n medHistRealm
	```
	To display the security realms to which a file or a directory belongs, run the `acfsutil` `sec` `info` `file` command. For example:
	```
	$ /sbin/acfsutil sec info file -m /acfsmounts/acfs1/
	                               /acfsmounts/acfs1/medicalrecords
	```
10. Save security metadata as a backup.
	Run the `acfsutil` `sec` `save` command to save the security metadata of a file system.
	For example, save the security metadata of the `/acfsmounts/acfs1` file system to the `acfs1_backup.xml` file.
	```
	$ /sbin/acfsutil sec save -m /acfsmounts/acfs1 
	                          -p acfs1_backup.xml
	```
	The `acfs1_backup.xml` security metadata backup file is saved in the `/acfsmounts/acfs1/.Security/backup/` directory. The saved XML file can be loaded with the `acfsutil` `sec` `load` command.

You can run some `acfsutil` `sec` commands in a batch file with the `acfsutil` `sec` `batch` command. For example, you could create a batch file that contains a group of `acfsutil` `sec` `rule` and `acfsutil` `sec` `ruleset` commands.

Auditing and diagnostic data for Oracle ACFS security is saved to log files.

See also

- [Oracle ACFS Security](introducing-oracle-acfs-and-oracle-advm.md) for more information about Oracle ACFS security, including security log files
- [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) for information about disk group compatibility
- acfsutil sec prepare and acfsutil sec init for information about commands to set up security

### Encrypting Oracle ACFS File Systems

Basic operations to manage encryption on an Oracle ACFS file system on Linux are discussed in this topic.

The examples in this section show a scenario in which the medical history files are encrypted in an Oracle ACFS file system. The steps in this section assume Oracle ACFS security is not configured for the file system; however, you can use both Oracle ACFS security and encryption on the same file system. If you decide to use both security and encryption, then both encryption and security must be initialized for the cluster containing the file system. After security is initialized on the file system, then an Oracle ACFS security administrator runs `acfsutil` `sec` commands to provide encryption for the file system.

Because the `acfsutil` `encr` `set` and `acfsutil` `encr` `rekey` `-v` commands modify the encryption key store, you should back up the Oracle Cluster Registry (OCR) after running these commands to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3` or higher.

For the examples in this section, various operating system users, operating system groups, and directories must exist.

The basic steps to manage encryption are:

1. Initialize encryption.
	Run the `acfsutil` `encr` `init` command to initialize encryption and create the storage necessary for the encryption keys. This command must be run one time for each cluster on which encryption is set up.
	For example, the following command initializes encryption for a cluster.
	```
	# /sbin/acfsutil encr init
	```
	This command must be run before any other encryption command and requires root or administrator privileges to run.
2. Set encryption parameters.
	Run the `acfsutil` `encr` `set` command to set the encryption parameters for the entire Oracle ACFS file system.
	For example, the following command sets the `AES` encryption algorithm and a file key length of `128` for a file system mounted on the `/acfsmounts/acfs1` directory.
	```
	# /sbin/acfsutil encr set -a AES -k 128 -m /acfsmounts/acfs1/
	```
	The `acfsutil` `encr` `set` command also transparently generates a volume encryption key which is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command.
	This command requires root or administrator privileges to run.
3. Enable encryption.
	Run the `acfsutil` `encr` `on` command to enable encryption for directories and files.
	For example, the following command enables encryption recursively on all files in the `/acfsmounts/acfs1/medicalrecords` directory.
	```
	# /sbin/acfsutil encr on -r /acfsmounts/acfs1/medicalrecords
	                         -m /acfsmounts/acfs1/
	```
	For users that have appropriate permissions to access files in the `/acfsmounts/acfs1/medicalrecords` directory, they can still read the decrypted files.
	This command can be run by an administrator or the file owner.
4. Display encryption information.
	Run the `acfsutil` `encr` `info` command to display encryption information for directories and files.
	```
	# /sbin/acfsutil encr info -m /acfsmounts/acfs1/ 
	                           -r /acfsmounts/acfs1/medicalrecords
	```
	This command can be run by an administrator or the file owner.

Auditing and diagnostic data for Oracle ACFS encryption is saved to log files..

See also

- [Oracle ACFS Encryption](introducing-oracle-acfs-and-oracle-advm.md) for more information about Oracle ACFS encryption, including log files
- Securing Oracle ACFS File Systems for information about setting up security with encryption
- acfsutil encr init for information about initializing encryption

### Tagging Oracle ACFS File Systems

The operations to manage tagging on directories and files in an Oracle ACFS file system on Linux are discussed in this topic.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3` or higher.

Oracle ACFS implements tagging with Extended Attributes. There are some requirements when using Extended Attributes that should be reviewed.

The steps to manage tagging are:

1. Specify tag names for directories and files.
	Run the `acfsutil` `tag` `set` command to set tags on directories or files. You can use these tags to specify which objects are replicated.
	For example, add the `comedy` and `drama` tags to the files in the subdirectories of the `/acfsmounts/repl_data/films` directory.
	```
	$ /sbin/acfsutil tag set -r comedy /acfsmounts/repl_data/films/comedies
	$ /sbin/acfsutil tag set -r drama /acfsmounts/repl_data/films/dramas
	$ /sbin/acfsutil tag set -r drama /acfsmounts/repl_data/films/mysteries
	```
	In this example, the `drama` tag is purposely used twice and that tag is changed in a later step.
	You must have system administrator privileges or be the file owner to run this command.
2. Display tagging information.
	Run the `acfsutil` `tag` `info` command to display the tag names for directories or files in Oracle ACFS file systems. Files without tags are not be displayed.
	For example, display tagging information for files in the `/acfsmounts/repl_data/films` directory.
	```
	$ /sbin/acfsutil tag info -r /acfsmounts/repl_data/films
	```
	Display tagging information for files with the `drama` tag in the `/acfsmounts/repl_data/films` directory.
	```
	$ /sbin/acfsutil tag info -t drama -r /acfsmounts/repl_data/films
	```
	You must have system administrator privileges or be the file owner to run this command.
3. Remove and change tag names if necessary.
	Run the `acfsutil` `tag` `unset` command to remove tags on directories or files. For example, unset the `drama` tag on the files in the `mysteries` subdirectory of the `/acfsmounts/repl_data/films` directory to apply a different tag to the subdirectory.
	```
	$ /sbin/acfsutil tag unset -r drama /acfsmounts/repl_data/films/mysteries
	```
	Add the `mystery` tag to the files in the `mysteries` subdirectory of the `/acfsmounts/repl_data/films` directory.
	```
	$ /sbin/acfsutil tag set -r mystery /acfsmounts/repl_data/films/mysteries
	```
	You must have system administrator privileges or be the file owner to run these commands.

See also

- [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) for information about disk group compatibility
- [Oracle ACFS Tagging](introducing-oracle-acfs-and-oracle-advm.md) for information about tagging an Oracle ACFS file system, including requirements for using Extended Attributes in tagging
- acfsutil tag set for information about specifying tag names

### Replicating Oracle ACFS File Systems

The operations to manage Oracle ACFS snapshot-based replication on an Oracle ACFS file system on Linux are discussed in this topic.

The disk groups on which volumes are created for the primary and standby file systems must have compatibility attributes for `ASM` and `ADVM` set to `12.2` or higher. To use a snapshot as a storage location, or to use replication role reversal, the compatibility attributes for Oracle ASM and Oracle ADVM must be set to `18.0` or higher.

The steps to manage replication are:

1. Determine the user to be employed for replication.
	Choose or create the replication user who logs in with `ssh` to the standby cluster to apply data replicated from the primary location to the standby location. This user is defined only at the operating system (OS) level and not within Oracle. The user should belong to the groups defined for Oracle ASM administrator access. This user is designated the *repluser*.
	Note:
	The same user and group identities (including all `uids` and `gids`) must be specified for the replication user on both your primary cluster and your standby cluster.
2. Ensure that `ssh` has been configured for replication.
	The use of `ssh` by replication involves two different user identities: root and *repluser*. Configuring `ssh` involves the following high-level steps:
	- Configuring a user key for root on each cluster, then ensuring that key is authorized to log in as *repluser* on the other cluster.
		- Configuring a user key for *repluser* on each cluster, then ensuring that key is authorized to log in as *repluser* on the other cluster.
		- Ensuring that a host key for each node in each cluster is known to the user *repluser* in the other cluster.
3. Ensure that the snapshots needed by replication can be created at all times.
	At any given point, replication may need to be able to use two concurrent snapshots of the primary location, and one snapshot of the standby location. You can check how many snapshots are in use in the primary and standby file systems using the `acfsutil` `snap` `info` command.
	You can confirm how many snapshots are available in each file system (usually 1024) by looking at the flags value in the output of the `acfsutil` `info` `fs` command. If the value contains the string `KiloSnap`, then 1024 snapshots are available.
4. Ensure that there is adequate network connectivity between the primary and standby sites. You should verify that the achievable network data transfer rate from primary to standby is substantially larger than the rate of change of data on the primary location.
	One way to estimate network data transfer rate is to start with an observed transfer rate, then reduce it to account for known sources of overhead. For example, you can calculate the elapsed time needed to FTP a 1 GB file from the primary location to the intended standby location, during a period when network usage is low. This provides an estimate of the maximum achievable transfer rate. This rate should be reduced to account for other demands on the network.
	To estimate the average rate of change on the primary, you can use the command `acfsutil` `info` `fs` with the `-s` option. This command should be run on each node where the file system that contains the primary location is mounted. The command displays the amount and rate of change to the file system on that node. To compute the total rate of change for the file system, the rate of changed for each node must be aggregated. A reasonable value to use for `-s` is `900`, which would yield a 15 minute sampling interval.
	With the output from `acfsutil` `info` `fs` with the `-s` option, you can determine the average rate of change, the peak rate of change, and how long the peaks last. A conservative approach to using this data is to choose the peak rate of change as the target rate that must be accommodated.
	Because replication must transfer all data changed on the primary to the standby, obviously the achievable network transfer rate must be higher, ideally significantly higher, than the target rate of change on the primary. If this is not the case, you should increase network capacity before implementing replication for this primary location and workload.
	For example, assume you have a four node primary cluster and you determine that a 1 GB file can be transferred in 30 seconds, yielding a current FTP transfer rate of 33 MB per second. An estimate of the current replication transfer rate would be approximately 20 MB per second, calculated as follows:
	```
	33 MB/sec * (1 - 0.2 - (4 * 0.05)) = 33 * 0.6 = ~20 MB/sec
	```
	Also, you find that the average rate of change to the primary is 8 GB per hour, with a peak rate of 25 GB per hour. Using the peak rate, you can calculate a target rate of change of approximately 7 MB per second as follows:
	```
	(25 GB/hour * 1024) / 3600 = ~7 MB/sec
	```
	In the scenario that was discussed in this step, you can reasonably expect the network to be able to handle the additional workload from replication.
5. Ensure that there is adequate storage capacity on the primary and standby sites.
	Estimate the storage capacity needed for replication on the sites hosting the primary and standby locations. In the general case, the primary site must store two snapshots of the primary location on an ongoing basis and the standby site must store a single snapshot of the standby location. The space occupied by these snapshots mostly consists of user data or metadata preserved in the snapshot, that has since been modified which triggers a new copy of the data to be created.
	The space occupied by replication-related snapshots can be directly viewed using the command `acfsutil` `snap` `info`. On the primary, check for snapshots with the names starting with the string `REPL`. On the standby, look for snapshots for names starting with `SDBACKUP`.
	If you use interval-based replication, the `-i` option to `acfsutil` `repl` `init` `primary`, and if the replication operations are successfully completing within the specified interval, then the size of replication-related snapshots is related to the rate of change of the primary and the length of the interval. For example, with an average rate of change of 8 GB per hour and a two hour replication interval, you would expect that snapshot storage usage is in the range of 16 GB per snapshot.
	Snapshot size does vary with the rate of change of the primary. Another factor is that snapshot size depends in part on the number of files in the file system, as well as the rate of change. Potentially more importantly, if you use constant mode replication, the `-C` option to `acfsutil` `repl` `init` `primary`, or if replication operations are not completing successfully in the interval given with interval-based replication because the interval is too small, the size of replication-related snapshots is difficult to predict in advance. In these cases, observe the size of the snapshots being generated over time and adjust the file system size as needed with the `acfsutil` `size` command to accommodate normal storage needs in addition in the presence of the snapshots. When collecting this information, a good starting point is to accommodate space for the snapshots to contain the data that is multiple times larger than the collection period, at the average rate of change of the primary.
	While collecting this information, choose a conservative starting point for the amount of space to allow for replication snapshots. For example, you can compute the space needed to store changes to the file system over the collection period as described previously, then you can allocate several times that space for future snapshots.
6. Optionally set tags on directories and files to replicate only selected files in an Oracle ACFS primary location. You can also add tags to files after replication has started.
7. Configure the site hosting the standby location.
	Before replicating an Oracle ACFS a primary storage location, configure the site hosting the standby location by performing the following:
	- To use the file system as a standby location, create a new *standby* file system of adequate size to hold the files replicated from the primary location, as well as a single replication snapshot, and mount the file system. For example:
		`/standby/repl_data`
		- To use a snapshot of an existing file system as a standby location, create a new read-write snapshot, and ensure that the file system is of adequate size to hold the files replicated from the primary location, as well as a single replication snapshot.
		- For either kind of standby location, run the `acfsutil` `repl` `init` `standby` command on the site hosting the standby location. For example:
		```
		# /sbin/acfsutil repl init standby -u repluser /standby/repl_data
		```
		Note:
		If the `acfsutil` `repl` `init` `standby` command is interrupted for any reason, the user must re-create the file system or snapshot used for the location, re-mount the file system if needed, and re-run the command.
		This command requires the name of the replication user and the standby location. The specified user is the user under which `ssh`, invoked from the primary cluster, logs in to the standby cluster to apply changes. This user is specified with the **\-u** option. For example: `-u repluser`.
		If the standby location is a file system, it is named with its mount point. For example: `/standby/repl_data`.
		If the standby location is a read-write snapshot, it is named with the snapshot name and the mount point of the containing file system, with the two separated by the `@` character. For example: `drsnap1101@/standby/repl_data`.
		In addition, for either kind of standby location, if the standby cluster contains multiple nodes, then specify a VIP, such as the SCAN VIP, as the network endpoint that replication uses on the standby to receive information from the primary. A hostname should be used as this network endpoint in single-node clusters only.
8. After the standby location has been set up, configure the site hosting the primary location and start replication.
	Run the `acfsutil` `repl` `init` `primary` command on the site hosting the primary location. For example:
	```
	$ /sbin/acfsutil repl init primary -i 2h -s repluser@standby12_vip -m /standby/repl_data /acfsmounts/repl_data
	```
	This command requires the following configuration information.
	- The replication mode:
		- Interval-based, during which a replication operation starts once for a specified interval
				- Constant-mode, during which a new replication operation starts as soon as the previous one ends
				- Manual-mode, during which replication occurs only when requested using the `acfsutil` `repl` `sync` command
		If an interval is specified, the option value is the minimum amount of time that elapses between replication operations.
		In all cases, at the start of each operation, replication takes a new snapshot of the primary and compares it to the previous snapshot, if one exists. The changes needed to update the standby to match the primary are then sent to the standby.
		For example, to set up a replication interval of two hours, specify `-i 2h`.
		- The user name and network endpoint (VIP name or address, or host name or address) to be used to connect to the site hosting the standby location, specified with the `-s` option. For example: `-s repluser@standby12_vip`
		- If the primary location is a file system, then specify the name of the mount point of the file system. For example: `/acfsmounts/repl_data`
		- If the primary storage location is a snapshot, then specify the snapshot name plus the mount point of the containing file system, the two separated by the `@` character. For example: `drsnap1101@/acfsmounts/repl_data`
		- If the mount point, or snapshot name with the mount point, is different on the site hosting the standby location than it is on the site hosting the primary location, then specify the name of the standby location with the `-m` option. For example: `-m /standby/repl_data`
	Because replication is unidirectional, when it is first initiated only the network endpoint specified for the standby cluster is immediately used. However, to support failover (described in a later step), in which the direction of replication may be reversed,`acfsutil` `repl` `init` `primary` also sets up a network endpoint for the primary cluster. The command looks for a SCAN VIP and uses it as the endpoint if present. If no SCAN VIP is identified, then the command uses the hostname of the node where the command runs as the endpoint instead. If the primary cluster contains multiple nodes, then a VIP should always be used as the network endpoint. A hostname should be used as this endpoint only in single-node clusters. You can specify the endpoint to be used for the primary using the `-p` option to `acfsutil` `repl` `init` `primary`.
	You can verify the endpoint being used for either cluster using the `acfsutil` `repl` `info` `-c` command. You can change the endpoint at any time using the `acfsutil` `repl` `update` `primary` command.
9. Monitor information about replication on the location.
	The `acfsutil` `repl` `info` command displays information about the state of the replication processing on the primary or standby location.
	For example, you can run the following on the site hosting the primary location to display configuration information.
	```
	$ /sbin/acfsutil repl info -c -v /acfsmounts/repl_data
	```
	You must have system administrator (the user root) or Oracle AM administrator privileges to run this command.
10. Pause replication momentarily if necessary.
	Run the `acfsutil` `repl` `pause` to momentarily stop replication. Run the `acfsutil` `repl` `resume` command as soon as possible to resume replication.
	For example, the following command pauses replication on the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl pause /acfsmounts/repl_data
	```
	The following command resumes replication on the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl resume /acfsmounts/repl_data
	```
	You must have system administrator or Oracle AM administrator privileges to run the `acfsutil` `repl` `pause` and `acfsutil` `repl` `resume` commands.
11. Failing over to a standby or turning a standby location into an active location.
	A replication standby can be converted to a replication primary, or can be used by itself as a read/write storage location without replication active. The `acfsutil` `repl` `failover` command provides the key support for these operations. This command is run on the standby cluster.
	The `acfsutil` `repl` `failover` command begins by verifying the status of the original replication primary. If it finds that the primary is unavailable, then it can optionally retry for a specified period to see if the primary becomes available.
	When both the standby location and corresponding primary location are operating normally, `acfsutil` `repl` `failover` reverses the replication relationship. That is, the original standby becomes the current primary, and the original primary becomes the current standby. There is no data loss. Note that failover fails in this case if replication is paused. To enable this case to succeed, run `acfsutil` `repl` `resume`.
	If `acfsutil` `repl` `failover` has determined that the primary location is not available, then the command restores the standby location to its state as of the last successful replication transfer from the primary, then converts the standby into a primary. Some data loss may occur. After the standby has been converted to a primary, you can do any of the following next:
	- You can wait until the original primary location becomes available. In this case, the original primary is aware that the failover command has been run and converts itself to the replication standby location. Replication is restored, but in the opposite direction.
		- If you do not want to wait, but do want to continue replication, then you can specify a new standby location using the `acfsutil` `repl` `update` command. This command also restores replication. Note that the operation is harmless if the original primary returns (as a standby) after you have specified the new standby. The original primary remains idle (as a standby) until you run `acfsutil` `repl` `terminate` `standby` for it.
		- If you want to terminate replication, then run the `acfsutil` `repl` `terminate` `primary` command on the current primary (the original standby).
12. Manage the replication background process.
	Run the `acfsutil` `repl` `bg` command to start, stop, or retrieve information about the replication background process.
	For example, run the following command to display information about the replication process for the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl bg info /acfsmounts/repl_data
	```

Note:

When replication is in use, replication snapshots can be viewed using the `acfsutil` `snap` `info` command, just as any other snapshot can. You can use this command to get an approximate idea of the space currently occupied by replication snapshots.

Note:

When the Oracle Grid Infrastructure software must be upgraded on the primary and standby sites, either site may be upgraded first, so long as the upgrade starts from GI version 19c or later. Replication will continue to run correctly while this upgrade is in progress. However, any upgrade should be completed on both sites as quickly as possible, so that both sites are running the same GI version on an ongoing basis.

See also

- [Oracle ACFS Replication](introducing-oracle-acfs-and-oracle-advm.md) for information about replicating Oracle ACFS file systems or snapshots
- [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) for information about disk group compatibility
- [Configuring SSH for Use with Oracle ACFS Replication](configuring-oracle-acfs-snapshot-based-replication.md) and [Installing ssh and Cygwin on Windows](configuring-oracle-acfs-snapshot-based-replication.md) for information about configuring replication
- acfsutil repl init for information initiating replication
- [About Privileges for Oracle ASM](administering-oracle-asm-instances.md) for information about user privileges for Oracle AM
- acfsutil repl bg for more information about managing replication background operations
- acfsutil repl pause and acfsutil repl resume for more information about pausing and resuming replication operations
- acfsutil repl info for information about displaying replication details
- Creating an Oracle ACFS File System for information about creating a file system
- Tagging Oracle ACFS File Systems for information about the steps to tag files

## Oracle ACFS Command-Line Tools for Linux Environments

This topic provides a summary of the Oracle ACFS commands for Linux environments.

The Oracle ACFS command summary lists the Oracle ACFS commands for Linux environments with brief descriptions. The commands in this summary have been extended with additional options to support Oracle ACFS. All other Linux file system commands operate without change for Oracle ACFS.

For example, Oracle ACFS adds a set of Oracle ACFS-specific mount options to those provided with the base operating system platform. You should review both the mount options for the Linux platforms in addition to the Oracle ACFS-specific options for the complete set of file system mount options.

File systems on Oracle ADVM volumes that are not Oracle ACFS file systems, such as `ext3`, are managed with the same Linux commands that are listed in this section using the file-specific options for the type of file system. You can refer to the `man` pages for options available for the Linux commands in this section.

Note:

When using Security-Enhanced Linux (SELinux) in enforcing mode with Oracle ACFS, ensure that the Oracle ACFS file systems are mounted with an SELinux default context. Refer to your Linux vendor documentation for information about the context mount option.

Table: Summary of Oracle ACFS commands for Linux environments

| Command | Description |
| --- | --- |
| fsck (offline mode) | Checks and repairs a dismounted Oracle ACFS file system. |
| fsck (online mode) | Checks and repairs a mounted Oracle ACFS file system. |
| mkfs | Creates an Oracle ACFS file system. |
| mount | Mounts an Oracle ACFS file system. |
| umount | Dismounts an Oracle ACFS file system. |

### fsck (offline mode)

#### Purpose

Checks and repairs a dismounted Oracle ACFS file system.

#### Syntax and Description

```
fsck -t acfs -h /dev/null
fsck [-a|-f] [-v]  -t acfs [-n|-y] [-x file_name] volume_device
```

`fsck` `-t` `acfs` `-h` `/dev/null` displays usage text and exits.

The following table contains the options available with the `fsck` command.

Table: Options for the offline fsck command on Linux

| Option | Description |
| --- | --- |
| `-a` | Specifies to automatically repair the file system. |
| `-f` | Forces the file system into mountable state without completing a file system check or repair. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `-t acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `-x` `file_name` | Specified for accelerator data collected by `acfsutil meta`. Only used for this type of data. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS file system. This topic describes an offline mode of the `fsck` command that can only be run on a dismounted file system. For information about running `fsck` on a mounted file system, refer to fsck (online mode).

`root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to repair errors in the file system. Do not interrupt `fsck` during the repair operation.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most three such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one to three 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The *id* fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` *id* *mount\_point* to attempt to determine the directory associated with `parent.`*id*. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see acfsutil info file.

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

#### Examples

The following example shows how to check and repair a dismounted Oracle ACFS file system.

Example: Using the fsck command in offline mode

```
# /sbin/fsck -a -y -t acfs /dev/asm/volume1-123
```

### fsck (online mode)

#### Purpose

Checks and repairs a mounted Oracle ACFS file system.

#### Syntax and Description

```
fsck -t acfs -h /dev/null

fsck [-a] [-v] -t acfs -O mount_point -- -C cow_file_path -S cow_file_size
fsck.acfs [-a] [-v] -O -C cow_file_path -S cow_file_size mount_point
```

Note:

The latter two syntax formats are equivalent. When invoking the Linux `fsck` command, the `--` separator must be placed before either the `-C` or `-S` options to ensure that the options are correctly passed to the Oracle ACFS `fsck` command. When directly invoking the ACFS `fsck.acfs` command, the `--` separator is not required.

`fsck` `-t` `acfs` `-h` `/dev/null` displays usage text and exits.

The following table contains the options available with the `fsck` command.

Table: Options for the online fsck command on Linux

| Option | Description |
| --- | --- |
| `-a` | Specifies to automatically repair the file system. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `-t acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-O` | Specifies to run in an online mode that enables checking of a mounted Oracle ACFS file system. |
| `-C` `cow_file_path` | Specifies the location of the Copy-On-Write (COW) file required by online `fsck`. |
| `-s` `cow_file_size` | Specifies the size of the Copy-On-Write (COW) file required by online `fsck`.  The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). If a unit is not specified, the default is bytes. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`fsck` checks and repairs an existing Oracle ACFS file system. This topic describes an online mode of the `fsck` command that can be run on a mounted file system. For information about running `fsck` in offline mode, refer to fsck (offline mode).

When online `fsck` is run on a mounted file system, online `fsck` initially creates a point-in-time snapshot of the file system metadata. Online `fsck` then executes file system checks against this metadata snapshot. Because the file system is mounted and live, file system metadata can be created or updated underneath online `fsck`. However, any new or updated metadata is not checked by online `fsck` because online `fsck` checks only the initial metadata snapshot.

Online `fsck` utilizes a special file called a Copy-On-Write (COW) file. While online `fsck` is running on a file system, whenever any file system metadata must be updated, the original version of the metadata is first copied into the COW file to preserve it for file system checks. The COW file helps preserve the metadata snapshot that is checked by online `fsck`.

The size of the COW file must be chosen in advance. As a result, the COW file has a limited amount of space for preserving copies of metadata. If the COW file runs out of space while preserving copies of metadata, then online `fsck` may be forced to stop. The size of the COW file must be chosen carefully to avoid running out of space during execution of online `fsck`. The appropriate size of the COW file depends on the amount of file system metadata that may change during the execution of online `fsck`, which is workload dependent and may need to be determined empirically. Oracle recommends the size of the COW file to start at 5% of the file system undergoing online `fsck`.

The COW file must be placed on a separate Oracle ACFS file system. The separate Oracle ACFS file system must be mounted on the same nodes as the Oracle ACFS file system undergoing online `fsck`.

The COW file is a temporary file that supports the execution of online `fsck` and is deleted after online `fsck` is complete.

The Oracle ACFS file system undergoing online `fsck` must have the same mount point path on all nodes. The Oracle ACFS file system storing the COW file must also have the same mount point path on all nodes.

Online `fsck` has the following restrictions and limitations while the command is running on an Oracle ACFS file system:

- Another instance of online `fsck` cannot be started within the same cluster.
- A mount of the file system on a new node causes online `fsck` to stop.
- If the separate Oracle ACFS file system containing the COW file is unmounted on any node, then that situation may cause online `fsck` to stop.
- Deleted snapshots within the file system do not have their storage freed until the completion of online `fsck`.
- Resizing the file system with `acfsutil` `size` is not allowed and returns an error. Automatic resizing is also not allowed until online `fsck` completes.
- A freeze of the file system with `acfsutil` `freeze` causes online `fsck` to wait for the freeze to end.

By default, online `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct online `fsck` to repair errors in the file system. Note that online `fsck` can only repair a limited set of file system errors. Most file system errors require offline `fsck` for repair.

#### Examples

The following example shows how to check and repair a mounted Oracle ACFS file system.

Example: Using the fsck command in online mode

```
# /sbin/fsck -a -t acfs -O /acfs_mountpoint_1 -- -C /acfs_mountpoint_2/cow_file -S 512M

# /sbin/fsck.acfs -O -C /acfs_mountpoint_2/cow_file -S 512M /acfs_mountpoint_1
```

### mkfs

Purpose

Creates an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
mkfs -V acfs -o h /dev/null
mkfs -V acfs [-v name ] [-s size][-o options] volume_device
  [-c release_version]
```

`mkfs` `-V` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

The following table contains the options available with the AIX `mkfs` command.

Table: Options for the AIX mkfs command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-v` `name` | Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. |
| `-s` `size` | Specifies the size of the file system in 512-byte units or in units of `K` \| `M` \| `G` \| `T` \| `P`. Units specified are in `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). |
| `-o` `options` | Specifies that options follow (f, h, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `f,v`  - `f` 	Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. - `h` 	Displays the usage text and exits. - `i=512 \| i=4096` 	Specifies a file system with metadata block size of 512 or 4096 bytes. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM device file that is to be formatted. |
| `-c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of \_release *version*. |

You can use `mkfs` to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional Linux command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. `root` privilege is not required. The ownership of the volume device file dictates who can run this command.

The value specified with the `-c` `release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `-c` `release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `-c` `release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to acfsutil compat set. For information about Oracle ASM disk group compatibility attributes, see [Disk Group Compatibility](administering-oracle-asm-disk-groups.md).

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `mkfs` to work.

4 KB Sector/Metadata

The following list summarizes the use of the `-o i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or higher to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `-o i=4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

Examples

Before creating an Oracle ACFS file system, first determine which Oracle ADVM volume devices are available. You can use the ASMCMD `volinfo` command to display information about the volumes and volume devices.

```
ASMCMD [+] > volinfo -a
...
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
...
```

For more information about `volinfo`, refer to [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md).

Next create an Oracle ACFS file system on the volume device file.

Example: Using the mkfs command

```
$ /usr/sbin/mkfs -V acfs /dev/asm/volume1-123
```

### mount

Purpose

Mounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
mount -V acfs -o h /dev/null /xxx
mount -v acfs [-o options] volume_device mount_point
```

`mount` `-V` `acfs` `-o` `h` `/dev/null` `/xxx` displays usage text and exits.

The following table contains the options available with the `mount` command.

Table: Options for the AIX mount command

| Option | Description |
| --- | --- |
| `-v` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-o` `options` | Specifies that options follow. Options are preceded with the `-o` flag followed by a comma-delimited string of options. For example: `-o` `all,ro,v`  The following options are available:  - `all` 	Reads the Oracle ACFS managed file systems in the Oracle Clusterware namespace, mounting all file systems with the `AUTO_START=always`. 	The `-o` `all` option requires two placeholders to satisfy the command arguments: a dummy argument for the volume device and directory. 	When the `-o` `all` option is specified, other `-o` options are ignored. 	To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `h` 	Displays the usage help text and exits. - `nosuid` 	Specifies that the execution of `setuid` and `setgid` programs by way of this mount is not allowed. - `nodev` 	Specifies that you cannot open devices from this mount. - `norootsuid` 	Fails the execution of binaries by non-root users whose permissions allow set user Id execution, and are owned by root. An attempt to run these executables as a non-root user fails with a permission denied error. - `rootsuid` 	Allows the execution of binaries by non-root users of set user Id files owned by root. This is the default action. - `ro` 	Mounts the file system in read-only mode. - `rw` 	Mounts the file system in read-write mode. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount happens on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/acfsmounts/acfs1`. The second example shows how to mount all the registered Oracle ACFS file systems. The dummy names (`none`) have been entered as placeholders for the device and directory as these arguments are required, but not used, when the `all` option is specified.

Example: Using the mount command

```
# /usr/sbin/mount -v acfs /dev/asm/volume1-123 /acfsmounts/acfs1

# /usr/sbin/mount -v acfs -o all none none
```

### umount

#### Purpose

Dismounts an Oracle ACFS file system.

#### Syntax and Description

```
umount -h
umount [-v] -l -n volume_device |mount_point
umount -a -l -n [-t acfs]
```

`umount` `-h` displays usage text and exits.

The following table contains the options available with the `umount` command.

Table: Options for the Linux umount command

| Option | Description |
| --- | --- |
| `-h` | Displays the usage help text and exits. |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-a` | Specifies to dismount all Oracle ACFS file systems on this node. |
| `-l` | Specifies a lazy unmount. The Oracle ACFS file system is dismounted, but the cleanup of all references to the file system occurs when the system is no longer busy. |
| `-n` | Specifies not to update the `/etc/mtab` file. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`umount` detaches an Oracle ACFS from the file system hierarchy on the current node.

The `umount` command does not return control back to the operating system prompt until the file system has been completely unmounted.

If the file system is busy, `umount` fails.

`root` privileges are required to run the `umount` command.

#### Examples

The following examples show how to dismount an Oracle ACFS file system. The first example uses the volume device file and the second example uses the file system.

Example: Using the umount command

```
# /bin/umount /dev/asm/volume1-123

# /bin/umount /acfsmounts/acfs1
```

## Oracle ACFS Command-Line Tools for the Solaris Environment

This topic provides a summary of the Oracle ACFS commands for Solaris.

Note:

If a disk group is dismounted with the force option on Solaris, any Oracle ADVM volumes device files that were on that disk group remain on the system. These files are removed when the disk group is remounted.

The following table lists the Oracle ACFS commands for Solaris with brief descriptions. The commands in this table have been extended with additional options to support Oracle ACFS on Solaris.

Table: Summary of Oracle ACFS commands for Solaris

| Command | Description |
| --- | --- |
| fsck | Checks and repairs an Oracle ACFS file system on Solaris. |
| mkfs | Creates an Oracle ACFS file system on Solaris. |
| mount | Mounts an Oracle ACFS file system on Solaris. |
| umount/umountall | Dismounts an Oracle ACFS file system on Solaris. |

### fsck

Purpose

Checks and repairs an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
fsck -F acfs -o h /dev/null
fsck -F acfs [{-n|N}|{-y|Y}] [-o options] volume_device
```

`fsck` `-F` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

The following table contains the options available with the `fsck` command.

Table: Options for the Solaris fsck command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-n` \| `N` | Answers no to any prompts. |
| `-y` \| `Y` | Answers yes to any prompts. |
| `-o` | Specifies that options follow (a, f, h, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `a,v`  - `a` 	Specifies to automatically fix the file system. - `f` 	Forces the file system into mountable state without completing a file system check or fix. - `h` 	Displays the usage text and exits. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `volume_device` | Specifies an Oracle ADVM device file. |

`fsck` checks and repairs an existing Oracle ACFS file system. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-o` `a` option must be specified to instruct `fsck` to fix errors in the file system. Do not interrupt `fsck` during the repair operation.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most three such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one to three 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The *id* fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` *id* *mount\_point* to attempt to determine the directory associated with `parent.`*id*. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see " acfsutil info file ".

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair an Oracle ACFS file system.

Example: Using the fsck command

```
# /usr/sbin/fsck -F acfs -y -o a /dev/asm/volume1-123
```

### mkfs

Purpose

Creates an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
mkfs -F acfs -o h /dev/null
mkfs -F acfs [-o options] [-c release_version] volume_device [size]
```

`mkfs` `-F` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

The following table contains the options available with the `mkfs` command.

Table: Options for the Solaris mkfs command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-o` `options` | Specifies that options follow (f, h, n, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `f,v`  - `h` 	Displays the usage text and exits. - `f` 	Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. - `i=512 \| i=4096` 	Specifies a file system with metadata block size of 512 or 4096 bytes. - `n` = *name* 	Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of \_release *version*. |
| `volume_device` | Specifies an Oracle ADVM device file. |
| `size` | Specifies the size of the file system in 512-byte units or in units of `K` \| `M` \| `G` \| `T` \| `P`. Units specified are in `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). |

You can use `mkfs` to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional Linux command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. `root` privilege is not required. The ownership of the volume device file dictates who can run this command.

The value specified with the `-c` `release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `-c` `release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `-c` `release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to " acfsutil compat set ". For information about Oracle ASM disk group compatibility attributes, see " [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) ".

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `mkfs` to work.

4 KB Sector/Metadata

The following list summarizes the use of the `-o i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or greater to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `-o i=4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

Examples

Before creating an Oracle ACFS file system, first determine which Oracle ADVM volume devices are available. You can use the ASMCMD `volinfo` command to display information about the volumes and volume devices.

```
ASMCMD [+] > volinfo -a
...
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
...
```

See [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md).

Next create an Oracle ACFS file system on the volume device file.

Example: Using the mkfs command

```
$ /usr/sbin/mkfs -F acfs /dev/asm/volume1-123
```

### mount

Purpose

Mounts an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
mount -F acfs -o h /tmp /dev/null
mount -F acfs [-r] [-o options] volume_device mount_point
```

`mount` `-F` `acfs` `-o` `h` `/tmp` `/dev/null` displays usage text and exits.

The following table contains the options available with the `mount` command.

Table: Options for the Solaris mount command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-r` | Mounts in read-only mode. |
| `-o` | Specifies that options follow. Options are preceded with the `-o` flag followed by a comma-delimited string of options. For example: `-o` `all,v`  The following options are available:  - `all` 	Reads the Oracle ACFS managed file systems in the Oracle Clusterware namespace, mounting all file systems with the `AUTO_START=always`. 	The `-o` `all` option requires two placeholders to satisfy the command arguments: a dummy argument for the volume device and any valid directory. 	When the `-o` `all` option is specified, other `-o` options are ignored. 	To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `devices` / `nodevices` 	Allows or disallows the opening of any character or block special devices from this mount. - `exec` / `noexec` 	Allows or disallows the execution of programs in this file system. - `h` 	Displays the usage help text and exits. - `rootsuid` / `norootsuid` 	Allows or disallows the execution of `setuid` to root executables (binaries by non-root users whose permissions allow set user Id execution, and are owned by root). `rootsuid` is the default action. If `norootsuid` is specified, an attempt to run these executables as a non-root user fails with a permission denied error. - `ro` 	Mounts the file system in read-only mode. - `rw` 	Mounts the file system in read-write mode. - `setuid` / `nosetuid` 	Allows or disallows the execution of `setuid` and `setgid` programs. - `suid` / `nosuid` 	Allows or disallows the execution of `setuid` and `setgid` programs and the opening of any character or block special devices from this mount. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount occurs on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/acfsmounts/acfs1`. The second example shows how to mount all the registered Oracle ACFS file systems. Placeholder arguments must be provided for the volume device name and mount point when specifying the `-o` `all` option. The volume device can be a dummy value, such as `none`. Any valid directory can be specified for the mount point, such as `/tmp`.

Example: Using the mount command

```
# /sbin/mount -F acfs /dev/asm/volume1-123 /acfsmounts/acfs1

# /sbin/mount -F acfs -o all none /tmp
```

### umount/umountall

Purpose

Dismounts an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
umount -V [mount_point | volume_device]
umountall -F acfs
```

`unmountall` `-F` `acfs` dismounts all Oracle ACFS file systems.

The following table contains the options available with the `umount` command.

Table: Options for the Solaris umount command

| Option | Description |
| --- | --- |
| `-V` | Echoes the complete command line, but does not run the command. Use this option to verify and validate the command line before execution. Valid only with `umount`. |
| `mount_point` | Specifies the directory where the file system is mounted. Valid only with `umount`. |
| `volume_device` | Specifies the Oracle ADVM volume device name associated with the file system. Valid only with `umount`. |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. Valid only with `umountall`. |

`umount` and `umountall` detach an Oracle ACFS from the file system hierarchy on the current node.

The `umount` and `umountall` commands do not return control back to the operating system prompt until the file system has been completely unmounted.

If a file system is busy, `umount` and `umountall` fail.

`root` privileges are required to run the `umount` and `umountall` commands.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example specifies the mount point of the file system to dismount. The second example specifies the volume device associated with the file system to dismount. The third example dismounts all Oracle ACFS file systems.

Example: Using the umount command

```
# /sbin/umount /dev/asm/volume1-123

# /sbin/umount /acfsmounts/acfs1

# /sbin/umountall -F acfs
```

### fsck

Purpose

Checks and repairs an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
fsck -V acfs [-n|-y] [-o options] volume_device
```

The following table contains the options available with the AIX `fsck` command.

Table: Options for the AIX fsck command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies an Oracle ADVM volume on AIX. `acfs` designates the Oracle ACFS type. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `-o` `options` | Specifies that options follow (a, f, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `a,v`  - `a` 	Specifies to automatically fix the file system. - `f` 	Forces the file system into mountable state without completing a file system check or fix. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to fix errors in the file system. Do not interrupt `fsck` during the repair operation.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most three such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one to three 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The *id* fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` *id* *mount\_point* to attempt to determine the directory associated with `parent.`*id*. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see " acfsutil info file ".

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair an Oracle ACFS file system.

Example: Using the fsck command

```
# /usr/sbin/fsck -V acfs -y -o a /dev/asm/volume1-123
```

### umount/umountall

Purpose

Dismounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
umount [mount_point | volume_device]
umountall -F acfs
```

`unmountall` `-F` `acfs` dismounts all Oracle ACFS file systems.

The following table contains the options available with the `umount` command.

Table: Options for the AIX umount command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. Valid only with `umount`. |
| `volume_device` | Specifies the Oracle ADVM volume device name associated with the file system. Valid only with `umount`. |
| `-F` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. Valid only with `umountall`. |

`umount` and `umountall` detach an Oracle ACFS from the file system hierarchy on the current node.

The `umount` and `umountall` commands do not return control back to the operating system prompt until the file system has been completely unmounted.

If a file system is busy, `umount` and `umountall` fail.

`root` privileges are required to run the `umount` and `umountall` commands.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example specifies the mount point of the file system to dismount. The second example specifies the volume device associated with the file system to dismount. The third example dismounts all Oracle ACFS file systems.

Example: Using the umount command

```
# /usr/sbin/umount /dev/asm/volume1-123

# /usr/sbin/umount /acfsmounts/acfs1

# /usr/sbin/umountall -F acfs
```

## Oracle ACFS Command-Line Tools for the AIX Environment

This topic provides a summary of the Oracle ACFS commands for the AIX operating system.

During the installation of Oracle ACFS and Oracle ADVM with Oracle Grid Infrastructure on AIX, several system security classes (authorizations) are created for Oracle ACFS and Oracle ADVM operations. These authorizations enable the following operations:

- Configuration of Oracle ACFS and Oracle ADVM devices
- Removal of Oracle ACFS and Oracle ADVM devices
- Definition of Oracle ACFS and Oracle ADVM devices

These authorizations are collected in a role (`oracle_devmgmt`) which is assigned by default to the Oracle Grid Infrastructure user and Oracle ASM administrator. You can run the `lsrole` or `rolelist` command after installation to see this new role. These commands can be run at any time to ensure that the user has the proper authorization to manage Oracle ACFS and Oracle ADVM.

For example, run the following as the Oracle ASM administrator:

```
$ rolelist -e
 oracle_devmgmt
```

After the initial installation on an AIX operating system, the shell from which the root script was run does not inherit the new role. If the role is not present for the user, then the `swrole` command must be run before performing Oracle ACFS or Oracle ADVM operations.

For example, run the following as the Oracle ASM administrator:

```
$ swrole oracle_devmgmt
```

Alternatively, you can open a new shell to perform Oracle ACFS or Oracle ADVM operations.

During the removal of Oracle Grid Infrastructure, the `oracle_devmgmt` role and its associated authorizations are deleted from the system.

See also

Oracle Grid Infrastructure on AIX, refer to [*Oracle Grid Infrastructure Installation Guide for IBM AIX on POWER Systems (64-Bit)*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWAIX) for more information about installing

Note:

If a disk group is dismounted with the force option on AIX, any Oracle ADVM volumes device files that were on that disk group remain on the system. These files are removed when the disk group is remounted.

The following table lists the Oracle ACFS AIX commands with brief descriptions. The commands in this table have been extended with additional options to support Oracle ACFS on AIX.

Table: Summary of Oracle ACFS commands for AIX

| Command | Description |
| --- | --- |
| fsck | Checks and repairs an Oracle ACFS file system on AIX. |
| mkfs | Creates an Oracle ACFS file system on AIX. |
| mount | Mounts an Oracle ACFS file system on AIX. |
| umount/umountall | Dismounts an Oracle ACFS file system on AIX. |

### fsck

Purpose

Checks and repairs an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
fsck -V acfs [-n|-y] [-o options] volume_device
```

The following table contains the options available with the AIX `fsck` command.

Table: Options for the AIX fsck command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies an Oracle ADVM volume on AIX. `acfs` designates the Oracle ACFS type. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `-o` `options` | Specifies that options follow (a, f, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `a,v`  - `a` 	Specifies to automatically fix the file system. - `f` 	Forces the file system into mountable state without completing a file system check or fix. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to fix errors in the file system. Do not interrupt `fsck` during the repair operation.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most three such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one to three 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The *id* fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` *id* *mount\_point* to attempt to determine the directory associated with `parent.`*id*. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see " acfsutil info file ".

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair an Oracle ACFS file system.

Example: Using the fsck command

```
# /usr/sbin/fsck -V acfs -y -o a /dev/asm/volume1-123
```

### mkfs

Purpose

Creates an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
mkfs -V acfs -o h /dev/null
mkfs -V acfs [-v name ] [-s size][-o options] volume_device
  [-c release_version]
```

`mkfs` `-V` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

The following table contains the options available with the AIX `mkfs` command.

Table: Options for the AIX mkfs command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-v` `name` | Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. |
| `-s` `size` | Specifies the size of the file system in 512-byte units or in units of `K` \| `M` \| `G` \| `T` \| `P`. Units specified are in `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). |
| `-o` `options` | Specifies that options follow (f, h, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `f,v`  - `f` 	Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. - `h` 	Displays the usage text and exits. - `i=512 \| i=4096` 	Specifies a file system with metadata block size of 512 or 4096 bytes. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM device file that is to be formatted. |
| `-c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of \_release *version*. |

You can use `mkfs` to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional Linux command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. `root` privilege is not required. The ownership of the volume device file dictates who can run this command.

The value specified with the `-c` `release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `-c` `release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `-c` `release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to acfsutil compat set. For information about Oracle ASM disk group compatibility attributes, see [Disk Group Compatibility](administering-oracle-asm-disk-groups.md).

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `mkfs` to work.

4 KB Sector/Metadata

The following list summarizes the use of the `-o i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or higher to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `-o i=4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

Examples

Before creating an Oracle ACFS file system, first determine which Oracle ADVM volume devices are available. You can use the ASMCMD `volinfo` command to display information about the volumes and volume devices.

```
ASMCMD [+] > volinfo -a
...
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
...
```

For more information about `volinfo`, refer to [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md).

Next create an Oracle ACFS file system on the volume device file.

Example: Using the mkfs command

```
$ /usr/sbin/mkfs -V acfs /dev/asm/volume1-123
```

### mount

Purpose

Mounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
mount -V acfs -o h /dev/null /xxx
mount -v acfs [-o options] volume_device mount_point
```

`mount` `-V` `acfs` `-o` `h` `/dev/null` `/xxx` displays usage text and exits.

The following table contains the options available with the `mount` command.

Table: Options for the AIX mount command

| Option | Description |
| --- | --- |
| `-v` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-o` `options` | Specifies that options follow. Options are preceded with the `-o` flag followed by a comma-delimited string of options. For example: `-o` `all,ro,v`  The following options are available:  - `all` 	Reads the Oracle ACFS managed file systems in the Oracle Clusterware namespace, mounting all file systems with the `AUTO_START=always`. 	The `-o` `all` option requires two placeholders to satisfy the command arguments: a dummy argument for the volume device and directory. 	When the `-o` `all` option is specified, other `-o` options are ignored. 	To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `h` 	Displays the usage help text and exits. - `nosuid` 	Specifies that the execution of `setuid` and `setgid` programs by way of this mount is not allowed. - `nodev` 	Specifies that you cannot open devices from this mount. - `norootsuid` 	Fails the execution of binaries by non-root users whose permissions allow set user Id execution, and are owned by root. An attempt to run these executables as a non-root user fails with a permission denied error. - `rootsuid` 	Allows the execution of binaries by non-root users of set user Id files owned by root. This is the default action. - `ro` 	Mounts the file system in read-only mode. - `rw` 	Mounts the file system in read-write mode. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount happens on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/acfsmounts/acfs1`. The second example shows how to mount all the registered Oracle ACFS file systems. The dummy names (`none`) have been entered as placeholders for the device and directory as these arguments are required, but not used, when the `all` option is specified.

Example: Using the mount command

```
# /usr/sbin/mount -v acfs /dev/asm/volume1-123 /acfsmounts/acfs1

# /usr/sbin/mount -v acfs -o all none none
```

### umount/umountall

Purpose

Dismounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

```
umount [mount_point | volume_device]
umountall -F acfs
```

`unmountall` `-F` `acfs` dismounts all Oracle ACFS file systems.

The following table contains the options available with the `umount` command.

Table: Options for the AIX umount command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. Valid only with `umount`. |
| `volume_device` | Specifies the Oracle ADVM volume device name associated with the file system. Valid only with `umount`. |
| `-F` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. Valid only with `umountall`. |

`umount` and `umountall` detach an Oracle ACFS from the file system hierarchy on the current node.

The `umount` and `umountall` commands do not return control back to the operating system prompt until the file system has been completely unmounted.

If a file system is busy, `umount` and `umountall` fail.

`root` privileges are required to run the `umount` and `umountall` commands.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example specifies the mount point of the file system to dismount. The second example specifies the volume device associated with the file system to dismount. The third example dismounts all Oracle ACFS file systems.

Example: Using the umount command

```
# /usr/sbin/umount /dev/asm/volume1-123

# /usr/sbin/umount /acfsmounts/acfs1

# /usr/sbin/umountall -F acfs
```

## Oracle ACFS Command-Line Tools for Windows Environments

This topic provides a summary of the Oracle ACFS file system commands for Windows.

The Oracle ACFS Windows file system command summary lists the Oracle ACFS Windows file system commands with brief descriptions. These commands have been extended to support Oracle ACFS. All other Windows file system commands operate without change for Oracle ACFS.

Note:

Starting with Oracle ACFS 19c (19.5), Oracle ACFS is deprecated on Microsoft Windows. Deprecating certain clustering features with limited adoption allows Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS file systems on Microsoft Windows are deprecated, and can be desupported in a future release. Depending on the use case, to replace current Oracle ACFS file systems, Oracle recommends that you move to Oracle Automatic Storage Management (Oracle ASM), Oracle Database File System (DBFS), or Microsoft Windows shares.

Table: Summary of Oracle ACFS file system commands for Windows

| Command | Description |
| --- | --- |
| acfschkdsk | Checks and repairs an Oracle ACFS file system on Windows. |
| acfsdismount | Dismounts an Oracle ACFS on Windows. |
| acfsformat | Creates an Oracle ACFS file system on Windows. |
| acfsmountvol | Mounts an Oracle ACFS file system on Windows. |
| acfsutil detach | Prepares the Oracle ACFS driver for module unload on Windows. |

The following table lists the non-Oracle ACFS Windows file system commands with brief descriptions.

Table: Summary of Non-Oracle ACFS file system commands for Windows

| Command | Description |
| --- | --- |
| advmutil dismount | Dismounts Oracle ADVM volume devices for file systems that are not Oracle ACFS on Windows. |
| advmutil list | Lists Oracle ADVM volume devices for file systems that are not Oracle ACFS on Windows. |
| advmutil mount | Mounts Oracle ADVM volume devices for file systems that are not Oracle ACFS on Windows. |

### acfschkdsk

Purpose

Checks and repairs an Oracle ACFS file system.

Syntax and Description

```
acfschkdsk /h
acfschkdsk [/a|/f] [/v] [/n|/y] volume_device
```

The following table contains the options available with the `acfschkdsk` command.

Table: Options for the acfschkdsk command

| Option | Description |
| --- | --- |
| `/a` | Specifies to automatically repair the file system. |
| `/f` | Forces the file system into mountable state without completing a file system check or repair. |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `/h` | Displays the usage help text and exits. |
| `/n` | Answers no to any prompts. |
| `/y` | Answers yes to any prompts. |
| `volume_device` | Specifies the Oracle ADVM volume device. |

`acfschkdsk` checks and repairs an existing Oracle ACFS. This command can only be run on a file system that has been dismounted clusterwide.

The Oracle ACFS driver must be loaded for `acfschkdsk` to work. If the driver is not loaded, the administrator is prompted to ensure this is intentional. For information about loading drivers, see " [Oracle ACFS Drivers Resource Management](understanding-oracle-acfs-advanced-topics.md) ".

The Oracle ACFS driver normally ensures that `acfschkdsk` is the only user of the file system clusterwide. In extreme cases it may be necessary to fix a file system without loading the driver if the file system automount causes the system to fail. The verifications that are normally done by the driver for exclusive access are bypassed in this case.

By default `acfschkdsk` only checks for and only reports errors. The `/a` flag must be specified to instruct `acfschkdsk` to repair errors in the file system. Do not interrupt `acfschkdsk` during the repair operation.

In a few cases, `acfschkdsk` prompts for questions before proceeding to check a file system. For example, if `acfschkdsk` detects that another `acfschkdsk` is in progress on the file system, or if `acfschkdsk` detects that the Oracle ACFS driver is not loaded, or if the file system does not appear to be Oracle ACFS. In checking mode, `acfschkdsk` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `/y` or `/n` options to answer yes or no to any questions.

`acfschkdsk` creates working files before it checks a file system. These working files are created in the `temp` directory if space is available. If insufficient space is available, `acfschkdsk` attempts to write in the current working directory. The files `acfschkdsk` creates are roughly the size of the file system being checked divided by 32K. At most three files are allocated. These files are deleted when `acfschkdsk` has finished.

In the event that `acfschkdsk` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `\lost+found` directory when `acfschkdsk` is run in fix mode. For security reasons, only the Windows `Administrator` can read files in `\lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `\lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The *id* fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` *id* *mount\_point* to attempt to determine the directory associated with `parent.`*id*. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see " acfsutil info file ".

If the parent directory is not known, the parent *id* field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `\lost+found` directory from a snapshot.

Examples

The following example shows how to check an Oracle ACFS file system on Windows.

Example: Using the acfschkdsk command

```
C:\> acfschkdsk asm-volume1-311
```

### acfsdismount

Purpose

Dismounts an Oracle ACFS file system and removes its mount point (name space attachment).

Syntax and Description

```
acfsdismount /h
acfsdismount [/v] {drive_letter | mount_point}
acfsdismount [/v] /all
```

The following table contains the options available with the `acfsdismount` command.

Table: Options for the acfsdismount command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/h` | Displays help text and exits. |
| `/all` | Specifies to dismount all Oracle ACFS file systems on this node. |
| `drive_letter` | Specifies the drive letter followed by a colon. |
| `mount_point` | Specifies the full path of the mount point including the drive letter. |

`acfsdismount` removes the mount point (name space attachment) for the specified file system on the current node and dismounts the file system if it is mounted. When the file system is in the dismounted state, the data is preserved on the device and the file system can be re-mounted with the `acfsmountvol` command.

`acfsdismount` can fail in some circumstances because there are open file references from various programs, such as a virus scanner, Process Explorer, or Oracle Enterprise Manager.

Windows Administrator privileges are required to use the `acfsdismount` command.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example dismounts a file system using only the drive letter. The second example dismounts a file system using the full path name. The third examples dismounts all mounted file systems. All the examples enable the verbose mode.

Example: Using the acfsdismount command

```
C:\> acfsdismount /v O:

C:\> acfsdismount /v O:\mnt\

C:\oracle>acfsdismount /v /all
acfsdismount: valid path name: C:\oracle\acfsmounts\acfs1\
acfsdismount: opening handle to volume C:\oracle\acfsmounts\acfs1
acfsdismount: locking volume C:\oracle\acfsmounts\acfs1
acfsdismount: dismounting volume C:\oracle\acfsmounts\acfs1
acfsdismount: removing volume mount point on C:\oracle\acfsmounts\acfs1\
acfsdismount: closing handle to volume C:\oracle\acfsmounts\acfs1 and exiting cleanly
```

### acfsformat

Purpose

Creates an Oracle ACFS file system.

Syntax and Description

```
acfsformat /h
acfsformat [/v] [/i {512 | 4096}] [/f] [/n name] volume_device
  [/c release_version] [blocks]
```

The following table contains the options available with the `acfsformat` command.

Table: Options for the acfsformat command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/i {512 \| 4096}` | Specifies a file system with metadata block size of 512 or 4096 bytes. |
| `/n` `name` | Specifies the name for the file system. This is also known as a volume label. `acfsutil` `info` `fs` returns the name if one was specified. This can also be displayed from the `VOL_LABEL` column in the `V$ASM_ACFSVOLUMES` view. |
| `/f` | Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. |
| `/h` | Displays the usage help text. |
| `volume_device` | Specifies an Oracle ADVM device file to be formatted. |
| `/c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of \_release *version*. |
| `blocks` | Specifies the number of blocks that the file system should consume on the named device. The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), or `T` (terabytes). If a unit is not specified, the default is bytes. If this option is not specified, the entire device is consumed. |

`acfsformat` creates the on disk structure needed for Oracle ACFS to be mounted. `acfsformat` performs a quick format on the target volume. After `acfsformat` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`.

The value specified with the `/c` `release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `/c` `release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `/c` `release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to " acfsutil compat set ". For information about Oracle ASM disk group compatibility attributes, see " [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) ".

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `acfsformat` to work.

Windows Administrator privileges are required to run this command.

4 KB Sector/Metadata

The following list summarizes the use of the `/i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or higher to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `/i 4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

Examples

This example shows how to create an Oracle ACFS file system. The verbose option is specified in this example.

Example: Using the acfsformat command

```
C:\> acfsformat /v asm-volume1-311
```

### acfsmountvol

Purpose

Mounts an Oracle ACFS file system.

Syntax and Description

```
acfsmountvol /h
acfsmountvol
acfsmountvol [/v]  /all
acfsmountvol [/v] { drive_letter |dir } volume_device
```

The following table contains the options available with the `acfsmountvol` command.

Table: Options for the acfsmountvol command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/h` | Displays the help usage text and exits. |
| `/all` | Reads the ACFS mount registry created with `acfsutil` `registry` and mounts the file systems listed in it on this node. |
| `drive_letter` | The Windows drive letter to link to an Oracle ADVM volume device. |
| `dir` | Specifies the full directory of the mount point including the drive letter. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `acfsformat`. |

`acfsmountvol` attaches an Oracle ACFS to the file system hierarchy at the specified path name or drive letter. *dir* must be an empty directory. Oracle ACFS mount points can be created on any empty directory and they can be hierarchical (nested).

After `acfsmountvol` runs successfully, the `MOUNTPATH` column in the `V$ASM_VOLUME` view displays the full path or drive letter on which the file system is now mounted. If no arguments are specified, the command lists all mounted Oracle ACFS file systems on this node.

It is not always possible to return the cause of a mount failure to the `acfsmountvol` command. When this happens Oracle ACFS writes the cause of the failure to the Windows system event logger.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

Windows Administrator privileges are required to mount an Oracle ACFS.

Examples

The first example shows how to mount `asm-volume1-311` on the mount point identified as the `F:` drive. The second example shows how to mount `asm-volume1-215` on the mount point specified by `c:\oracle\acfsmounts\acfs1\`. The first two examples enable verbose mode. The third example lists all the mounted file systems on the node.

Example: Using the acfsmountvol command

```
C:\> acfsmountvol  /v  F:  asm-volume1-215

C:\> acfsmountvol /v  c:\oracle\acfsmounts\acfs1  asm-volume1-311

C:\oracle>acfsmountvol
   asm-volume1-311
       C:\oracle\acfsmounts\acfs1
```

### acfsutil detach

Purpose

Prepares the Oracle ACFS driver for module unload.

Syntax and Description

```
acfsutil detach
```

`acfsutil` `detach` prepares Oracle ACFS for having its driver unloaded. Oracle ACFS registers itself as a base file system upon driver load. In order for the Windows service control manager to send a stop command to the driver, Oracle ACFS must unregister itself as a base file system in addition to deleting any device objects associated with the driver.

After `acfsutil` `detach` has completed successfully, and all volumes have been dismounted, then the administrator can run the Windows service control manager's stop command to the Oracle ACFS driver. If the `acfsutil` `detach` command is not used, then the `stop` command does not call the Oracle ACFS driver unload routine. This command can only be run by the Windows `Administrator`. It is called automatically by the Oracle ACFS shutdown scripts.

Examples

The following examples show how to detach all Oracle ACFS file systems and unload drivers on Windows. The first example dismounts all the Oracle ACFS file systems volume devices. The second example detaches the volume devices.

Example: Using the acfsutil detach command

```
C:\> acfsdismount /all

C:\> acfsutil detach
```

### advmutil dismount

Purpose

The `advmutil` `dismount` command dismounts Oracle ADVM volume devices for file systems that are not Oracle ACFS.

Syntax and Description

```
advmutil dismount [/unregister] {drive_letter | dir}
advmutil dismount [/unregister] [/all | /dg=disk_group]
```

The following table contains the options available with the Windows `advmutil` `dismount` command.

Table: Options for the advmutil dismount command

| Option | Description |
| --- | --- |
| `drive_letter` | Specifies the drive letter to dismount. |
| `dir` | Specifies the directory of the mount point, including the drive letter. |
| `/a` ll | Specifies to dismount all file systems on this node. |
| `/unregister` | Optionally unregister an Oracle ADVM volume device and its drive letter from the system registry. Upon startup of the Oracle ASM instance and Oracle ACFS, the unregistered drive letter and Oracle ADVM volume symbolic links are not created. |
| `/dg=` `disk_group` | Optional name of the disk group containing the registered Oracle ADVM volume devices to create drive letters or possibly mount or dismount file systems. |

Note:

To format an Oracle ADVM volume device with NTFS, it must be mounted on a drive letter. After formatting, Oracle ADVM volume devices with NTFS can be mounted on either a drive letter or a directory.

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

The `advmutil` `dismount` command does not return control back to the operating system prompt until the file system has been completely unmounted.

Examples

These examples show how to dismount a file system that is not Oracle ACFS.

1. The first example shows how to remove a drive letter for an Oracle ADVM volume device which disallows access to the file system.
2. The second example shows how to remove a drive letter for an Oracle ADVM volume device which disallows access to the file system and removes it from the registry.
3. The third example shows how to remove a drive letter for all registered Oracle ADVM volume devices which disallows access to all file systems.
4. The fourth example shows how to remove a drive letter for all registered Oracle ADVM volume devices in a particular Oracle ASM disk group which disallows access to all related file systems.

Example: Using the advmutil dismount command

```
C:\> advmutil dismount H:

C:\> advmutil dismount H: /unregister

C:\> advmutil dismount /all

C:\> advmutil dismount /dg=data
```

### advmutil list

Purpose

The `advmutil` `list` command lists the Oracle ADVM volume devices that were registered with `advmutil` `mount` `/register.`

Syntax and Description

```
advmutil list /registry
```

The following table contains the options available with the Windows `advmutil` `list` command.

Table: Options for the advmutil list command

| Option | Description |
| --- | --- |
| `list` `/registry` | Lists the drive letter and corresponding Oracle ADVM volume device name contained in the Windows registry. |

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

For information about listing Oracle ADVM volume devices for Oracle ACFS, see " acfsutil info file ".

Examples

The following example shows how to list all entries in the system registry.

Example: Using the advmutil list command

```
C:\> advmutil list /registry

  Drive Letter     Asm Volume
  ===================================
  H:               asm-volume1-123
  K:               asm-volume2-245
```

### advmutil mount

Purpose

The `advmutil` `mount` command mounts Oracle ADVM volume devices for file systems that are not Oracle ACFS.

Syntax and Description

```
advmutil mount [/register] {drive_letter | dir} volume_device
advmutil mount /all
```

The following table contains the options available with the Windows `advmutil` `mount` command.

Table: Options for the advmutil mount command

| Option | Description |
| --- | --- |
| `drive_letter` | Specifies the drive letter to mount. |
| `dir` | Specifies the directory of the mount point, including the drive letter. |
| `volume_device` | Indicates the Oracle ADVM volume device. |
| `/a` ll | Specifies to mount all non-Oracle ACFS file systems on this node. |
| `/register` | Optionally register an Oracle ADVM volume device and its drive letter in the Windows system registry. After startup of the Oracle ASM instance and Oracle ACFS, all registered drive letters and Oracle ADVM volume symbolic links are created. This allows for automatic file system mounting by Windows as is also done for Oracle ACFS file systems. |

Note:

To format an Oracle ADVM volume device with NTFS, it must be mounted on a drive letter. After formatting, Oracle ADVM volume devices with NTFS can be mounted on either a drive letter or a directory.

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

For information about registering Oracle ADVM volume devices for Oracle ACFS, see " acfsutil registry ".

Examples

These examples show how to mount a file system that is not Oracle ACFS.

1. The first example shows how to create a drive letter for an Oracle ADVM volume device for use as a non-Oracle ACFS access which you could then use to format the volume for use with NTFS.
2. The second example shows how to create a drive letter for an Oracle ADVM volume device for use as a non-Oracle ACFS access which you could then use to format the volume for use with NTFS and save it in the Windows system registry.
3. The third example shows how to create a drive letter for all Oracle ADVM volume devices which were saved in the system registry which also allows a file system to be accessible.

Example: Using the advmutil mount command

```
C:\> advmutil mount H: asm-volume1-123

C:\> advmutil mount H: asm-volume1-123 /register

C:\> advmutil mount /all
```

## Oracle ACFS Command-Line Tools for Tagging

This topic provides a summary of the Oracle ACFS tagging commands.

The Oracle ACFS tagging command summary lists the Oracle ACFS tagging commands with brief descriptions.

On Solaris, `acfsutil` `tag` commands can set tag names on symbolic link files, but backup and restore utilities do not save the tag names that are explicitly set on the symbolic link files. Also, symbolic link files lose explicitly set tag names if they have been moved, copied, tarred, or paxed.

Table: Summary of commands for Oracle ACFS tagging

| Command | Description |
| --- | --- |
| acfsutil tag info | Displays the tags for directories or files in Oracle ACFS file systems. |
| acfsutil tag set | Adds a tag to directories or files in an Oracle ACFS file system. |
| acfsutil tag unset | Removes a tag or all tag names from directories or files in an Oracle ACFS file system. |

See also

- [Oracle ACFS Tagging](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS tagging
- About Using Oracle ACFS Command-Line Tools for information about running Oracle ACFS `acfsutil` commands
- [Oracle ACFS Tagging Generic Application Programming Interface](understanding-oracle-acfs-advanced-topics.md) for information about Oracle ACFS tagging application programming interfaces (APIs)

### acfsutil tag info

Purpose

Displays the tag names for tagged directories or file names in Oracle ACFS file systems.

Syntax and Description

```
acfsutil tag info -h
acfsutil tag info [-r] [-c -t tagname] path [path ...]
acfsutil tag info [-c -t tagname]
```

`acfsutil` `tag` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `tag` `info` command.

Table: Options for the acfsutil tag info command

| Option | Description |
| --- | --- |
| `-t` `tagname` | Specifies the tag name string to display. Enclose the string in quotes if the string contains a space. |
| `path` | Specifies the path name to one or more files or directories. |
| `-r` | Specifies recursive action on a specified path. |
| `-c` | Specifies case-insensitive partial matching on the tag name. |

The `acfsutil` `tag` `info` command can recursively apply the operation to all child files and subdirectories if the `-r` option is included with specified directory path names.

If no path names are specified, the `acfsutil` `tag` `info` command searches all Oracle ACFS mount points for tagged files.

Only the paths of tagged files in an Oracle ACFS file system are displayed. If the `-t` *tagname* option is included, only paths of files with a tag name exactly matching the specified *tagname* are displayed. If the `-c` option is included, then *tagname* can be a case-insensitive substring of a tag name for a successful match. For example, the `acfsutil` `tag` `info` `-c` `-t` `AG` command would display path names of files with tag names such as `tag1`, `ag`, or `AG`.

Any user may use this command to display tag info on a directory to which the user has read access.

Running `acfsutil` `tag` `info` on a file or directory that is protected by a security realm fails. If a user runs `acfsutil` `tag` `info` with the `-r` option on a directory protected by a security realm and the user does not have browse permissions on the directory, then no output is displayed. To resolve this issue, the user must be added to the security realm and granted `READDIR` permissions. For information about adding objects to an Oracle ACFS security realm, refer to " acfsutil sec realm add ".

Examples

The following example show the use of the `acfsutil` `tag` `info` command.

Example: Using the acfsutil tag info command

```
$ /sbin/acfsutil tag info -r /acfsmounts/acfs1/myrepfiles/
```

### acfsutil tag set

Purpose

Adds the given tag to the specified files or directories in an Oracle ACFS file system

Syntax and Description

```
acfsutil tag set -h
acfsutil tag set [-v] [-r] tagname path [path ...]
```

`acfsutil` `tag` `set` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `tag` `set` command.

Table: Options for the acfsutil tag set command

| Option | Description |
| --- | --- |
| `tagname` | Specifies a tag name string. Enclose the string in quotes if the string contains a space.  The tag string can be composed of ASCII characters that include: a-b, A-Z, 0-9, the space character, the hyphen, and the underscore. The maximum length of a tag name is 32 characters.  `all` is a reserved tag name and cannot be set on any file or directory. |
| `path` | Specifies the path string to one or more files or directories. |
| `-r` | Specifies recursive action on the specified path. |
| `-v` | Displays the progress of the operation. |

The command can recursively apply the operation to all child files and subdirectories for the specified directory path names.

When adding a tag name to a file or directory, the existing tags on that file or directory remain unchanged. New files that are created after a directory is assigned a tag implicitly inherit tags from their parent directories. Existing files in the directory do not inherit the new tag; these files must be explicitly assigned the tag. Renaming a file or moving a file to a subdirectory within the same file system does not cause the file to inherit tag names from the new parent directory. Moving a file between file systems uses a copy operation and the newly created file does inherit the tag names of the parent directory.

There is no fixed maximum number of tag names for an Oracle ACFS file system or for each file and directory. However, the number of tag names is limited by the tag names that fit in up to 64 KB of special metadata storage for each file and directory. This metadata also contains information to manage the extended attributes. Longer tag names reduce the total of tag names that can be set on a file or directory. For example, if all tag names were 4 bytes long, then it is possible to hold approximately 1730 tag names, assuming no other extended attribute information is present.

Any user who has the privilege to modify the target file or directory may run this command.

If a user runs `acfsutil` `tag` `set` with the `-r` option on a directory protected by a security realm and does not have browse permissions on the directory, then no tags are applied. To resolve this issue, the user must be added to the security realm and granted `READDIR` permissions. For information about adding objects to an Oracle ACFS security realm, refer to " acfsutil sec realm add ".

Examples

The following example show the use of the `acfsutil` `tag` `set` command.

Example: Using the acfsutil tag set command

```
$ /sbin/acfsutil tag set repl_grp1 -r /acfsmounts/acfs1/myrepfiles/*.dat
```

### acfsutil tag unset

Purpose

Removes the given tag name or all tag names from the specified file or directory.

Syntax and Description

```
acfsutil tag unset -h
acfsutil tag unset [-v] [-r] {all | tagname} path [path ...]
```

`acfsutil` `tag` `unset` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `tag` `unset` command.

Table: Options for the acfsutil tag unset command

| Option | Description |
| --- | --- |
| `all` | Specifies to remove all tags in the path string. |
| `tagname` | Specifies a tag name string. Enclose the string in quotes if the string contains a space. |
| `path` | Specifies the path string to one or more files or directories. |
| `-r` | Specifies recursive action on the specified path. |
| `-v` | Displays the progress of the operation. |

The command can recursively apply the operation to all child files and subdirectories for the specified directory path names.

When removing a tag name from a file or directory, other existing tags on that file or directory remain unchanged.

Any user who has privilege to modify the target file or directory may run this command.

If a user runs `acfsutil` `tag` `unset` with the `-r` option on a directory protected by a security realm and does not have browse permissions on the directory, then no tags are removed. To resolve this issue, the user must be added to the security realm and granted `READDIR` permissions. For information about adding objects to an Oracle ACFS security realm, refer to " acfsutil sec realm add ".

Examples

The following example show the use of the `acfsutil` `tag` `unset` command.

Example: Using the acfsutil tag unset command

```
$ /sbin/acfsutil tag unset repl_grp1 -r
     /acfsmounts/acfs1/myrepfiles/*.log
```

## Oracle ACFS Command-Line Tools for Replication

This topic provides a summary of the commands for Oracle ACFS snapshot-based replication.

The Oracle ACFS snapshot-based replication command summary lists the Oracle ACFS snapshot-based replication commands with brief descriptions. For an overview of Oracle ACFS replication, refer to [Oracle ACFS Replication](introducing-oracle-acfs-and-oracle-advm.md).

For information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of commands for Oracle ACFS replication

| Command | Description |
| --- | --- |
| acfsutil repl bg | Starts, stops, or displays information about the Oracle ACFS replication background processes. |
| acfsutil repl compare | Verifies that files have been replicated on an Oracle ACFS storage location. |
| acfsutil repl failover | Converts the role of the replication standby location to that of a primary location in the event of an unplanned failure. |
| acfsutil repl info | Displays information about replication processing on an Oracle ACFS storage location. |
| acfsutil repl init | Initiates replication on files in an Oracle ACFS storage location. |
| acfsutil repl pause | Pauses replication on an Oracle ACFS storage location. |
| acfsutil repl resume | Resumes replication on an Oracle ACFS storage location. |
| acfsutil repl reverse | Reverses the roles of the replication primary and standby storage location. |
| acfsutil repl switchover | Converts the role of the replication standby location to that of a primary location, and the primary location to that of a standby. |
| acfsutil repl sync | Synchronizes primary and standby storage locations. |
| acfsutil repl terminate | Stops all replication activity on the Oracle ACFS storage location. |
| acfsutil repl trace | Specifies the trace level for replication information. |
| acfsutil repl update | Updates replication information while replication is running. |
| acfsutil repl upgrade | Upgrades an active, existing replication installation to use snapshot-based replication. |

### acfsutil repl bg

Purpose

Starts, stops, or displays information about the Oracle ACFS replication background processes.

Syntax and Description

```
acfsutil repl bg -h
acfsutil repl bg {start | stop | info} [snap_shot@]mount_point
```

`acfsutil` `repl` `bg` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `bg` command.

Table: Options for the acfsutil repl bg command

| Option | Description |
| --- | --- |
| `start` | Starts the replication background processing. |
| `stop` | Stops the replication background processing |
| `info` | Displays information about the replication background process through the associated clusterware resource. If the resource is `ONLINE` on a node in the primary cluster, the process is running. Otherwise, the process is not running. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

Oracle ACFS replication uses a background process on the primary cluster to transport file system changes to the standby location, either a file system or snapshot. This process must be running for replication to function. When replication is started with the `acfsutil` `repl` `init` command, the process is started and registered with Oracle Clusterware, enabling an automatic restart after a reboot or system crash. This process is clusterwide.

To determine if the Oracle ACFS replication background process is running at the primary site, you can run the `acfsutil` `repl` `bg` `info` command on the primary cluster. The example in this section shows how to use the command.

Note:

- A primary file system containing a location participating in replication can always be unmounted, even if its replication background process is running. The `umount` command (the `acfsdismount` command on Windows) stops the background process if it is necessary to enable the unmount to proceed. Any in-progress replication operation is interrupted. When a primary file system containing a location participating in replication is remounted, replication automatically restarts and the background process is restarted.
- A standby file system containing a location participating in replication can be unmounted only if a replication operation is not currently in progress on it. If a replication operation is in progress, then an attempt to unmount the file system fails with an indication that the file system is busy.

Examples

The following example shows the use of the `acfsutil` `repl` `bg` command to display information about replication processes.

Example: Using the acfsutil repl bg command

```
$ /sbin/acfsutil repl bg info /acfsmounts/acfs1
Resource:      ora.repl.dupd.crsdg1.crsdg1vol1.acfs
Target State:  ONLINE
Current State: ONLINE on primnode1
```

### acfsutil repl compare

Purpose

Verifies that files have been replicated on an Oracle ACFS storage location.

Syntax and Description

```
acfsutil repl compare -h
acfsutil repl compare [-v] [ -a [-s] | -t { all | tagname, ...} [-s] ]
[snap_shot@]primary_mount_point [snap_shot@]standby_mount_point
```

`acfsutil` `repl` `compare` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `compare` command.

Table: Options for the acfsutil repl compare command

| Option | Description |
| --- | --- |
| `-a` | Compares all files and their extended attribute names. |
| `-t` { `all` \| `tagname`, `...` } | Compares files with all or some tag names specified in the `acfsutil` `repl` `init` operation. The `all` option specifies all tag names supplied in the `acfsutil` `repl` `init` operation. A comma-delimited list of tag names must only use tag names specified during the `acfsutil` `repl` `init` operation. |
| `-s` | Skips comparisons on symlinks for extended attributes and tags when using the `-a` or `-t` option. The symlinks are still checked for everything else, such as permissions and ownership. |
| `-v` | Causes the name of the file in each location to be output after the file is compared. |
| `[` `snap_shot@` `]` `primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |
| `[` `snap_shot@` `]` `standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |

The `acfsutil` `repl` `compare` command verifies all or part of the primary location has been replicated to the standby location. The standby location must be mounted locally for comparison. Best results are obtained when the primary location is changing as little as possible. The command always tries to check all files on the primary location against those on the standby location. To maximize the ability of the command to check all files, it should be invoked as the root user. However, this is not required -- the command will try to compare files when invoked as any user.

The `-a` option is typically used when no tag names were specified during the `acfsutil` `repl` `init` operation. The `-a` option compares all files on the primary location against those on the standby location. The `-a` option also enables tests for extra files on the standby location that do not exist on the primary. When testing for extra files, the command also attempts to check extended attributes. However, if NFS is used to mount the standby location locally, the standby cannot be checked for matching extended attributes due to limitations in the NFS protocol.

The `-t` option is used when tags were specified during the `acfsutil` `repl` `init` operation. The `-t` operation locates all file names on the primary location with the specified tag names and compares them to the corresponding files on the standby. The `-t` option takes as arguments either `all` option or a comma-delimited list of tag names. If the `-t` option is used with the `all` argument, then all tag names supplied during the `acfsutil` `repl` `init` operation are selected. Otherwise, any specified tag names must exactly match a tag name supplied during the `acfsutil` `repl` `init` operation. The `-t` option also tests for extra files on the standby location that do not have an associated tag name that was specified during the `acfsutil` `repl` `init` operation. If NFS is used to mount the standby location locally, the standby cannot be checked for matching tag names and extended attributes due to limitations in the NFS protocol.

You can use the `acfsutil` `repl` `info` `-c` option to determine which tags were specified during the `acfsutil` `repl` `init` operation.

The `-a` and `-t` options cannot both be specified at that same time. When `-a` or `-t` is provided, the `-s` option can also be specified to skip extended attribute comparisons for symlinks. If neither the `-a` nor `-t` option is provided, a primary to standby file comparison is done without testing tag names nor extended attributes.

The `-v` option may be specified to output the name of each file after the file is compared.

Examples

The following example shows the use of the `acfsutil` `repl` `compare` command.

Example: Using the acfsutil repl compare command

```
$ /sbin/acfsutil repl compare /acfsmounts/acfs1 /nfs_mounted_standby
```

### acfsutil repl failover

Purpose

Converts the role of the replication standby location to that of a primary location, and potentially the role of the corresponding primary location to that of a standby.

Syntax and Description

```
acfsutil repl failover -h
acfsutil repl failover [-T timeout] [snap_shot@]mount_point
```

`acfsutil` `repl` `failover` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` failover command.

Table: Options for the acfsutil repl failover command

| Option | Description |
| --- | --- |
| `-T` `timeout` | Specifies the time to wait (minutes) before determining that the primary location is unavailable. If the `-T` option is omitted, the primary location is checked once for availability. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `failover` command is issued at the standby replication site only. The command reverses the role of a replication standby location such that it becomes a replication primary location. The failover command insures that the standby location contains an exact copy of the results of the last successful replication transfer. If necessary, the command restores the location back to its state as of that transfer. `acfsutil` `repl` `failover` behaves differently based on the scenario in which it was run:

- Both the standby location and corresponding primary location are operating normally
	In this scenario, the command reverses the replication relationship. There is no data loss. Note that failover fails in this case if replication is paused. To enable this case to succeed, run `acfsutil` `repl` `resume`.
- The primary location is not currently available, but you want to wait until it is back online
	In this scenario, the command verifies the status of the replication primary. If the primary is not accessible and the timeout period has expired (if specified), then the command restores the standby location to its state as of the last successful replication transfer and converts it into a replication primary. Some data loss is possible, for example if there was a transfer in process when the primary location became unavailable. When the original primary location becomes available, it is aware that the failover command has been run and converts itself into a replication standby location.
- The primary location is not currently available and you do not want to wait until it is back online
	In this scenario, the command verifies the status of the replication primary. If the primary is not accessible and the timeout period has expired (if specified), then the command restores the standby location to its state as of the last successful replication transfer and converts it into a replication primary. Some data loss is possible, for instance if there was a transfer in process when the primary location became unavailable. After the failover command has been run, you have two options:
	- First, a new standby location can be configured using the `acfsutil` `repl` `update` command. Note that it is harmless if the original primary returns (as a standby) after you have specified the new standby. The original primary location remains idle (as a standby) until you run `acfsutil` `repl` `terminate` `standby` for that location.
		- Alternatively, you can terminate replication by running `acfsutil` `repl` `terminate` `primary` on the new primary.

When the current primary location is active, you should quiesce application updates to the primary before running `acfsutil` `repl` `failover`. Any updates attempted to the current primary location before its conversion to a standby are discarded. Any updates attempted to it after its conversion fail, just as updates would to any other standby location.

When application updates are resumed, they must be directed to the new primary location.

Examples

The following example shows the use of the `acfsutil` `repl` `failover` command. The command is invoked at the standby replication site and specifies the primary location (`/repl_data`).

Example: Using the acfsutil repl failover command

```
acfsutil repl failover /repl_data
```

See also

- acfsutil repl update for information about updating replication information
- [Configuring Oracle ACFS Snapshot-Based Replication](configuring-oracle-acfs-snapshot-based-replication.md) for information about configuring `ssh` for use with Oracle ACFS replication

### acfsutil repl info

Purpose

Displays information about replication processing on an Oracle ACFS storage location.

Syntax and Description

```
acfsutil repl info -h

acfsutil repl info -c [-v] {[snap_shot@]mount_point}

acfsutil repl info -c -u user [-o sshStrictKey=yn_value] standby_host [standby_host...]
  [snap_shot@]primary_mount_point

acfsutil repl info -c -u user [-o sshStrictKey=yn_value] primary_host [primary_host...]
  [snap_shot@]standby_mount_point

acfsutil repl info -s [-v][-l] [-n number{m|h|d|w|y}]
  {-f eventlog | [snap_shot@]mount_point}}

acfsutil repl info [-a|-e|-t] [-v][-l]
  {-f eventlog | [snap_shot@]mount_point }
```

`acfsutil` `repl` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `info` command.

Table: Options for the acfsutil repl info command

| Option | Description |
| --- | --- |
| `-a` | Displays only apply records from the replication event log. An apply record contains the date and time that the set of replicated changes were captured on the primary location and the date and time that they were applied on the standby location. |
| `-c` | Displays configuration information. |
| `-e` | Displays only error records from the replication event log. |
| `-f` `eventlog` | Specifies the absolute path to the replication event log to be used as the source of the information. The default location is: `mount_point` `/.ACFS/repl/logs/ReplicationEventsLog` |
| `-h` | Displays help text. |
| `-l` | Displays last event only. |
| `-n` `number` { `m` \| `h` \| `d` \| `w` \| `y` } | Specifies the interval to display information. *number* specifies the number of minutes (`m`), hours (`h`), days (`d`), weeks (`w`), or years (`y`). For example: `-n` `5d`  The statistics are summarized in the units of time specified. |
| `-u` `user` | Validates the host and user keys currently configured between the current host and each standby host specified with a *standby* argument, using *user* as the user for which access is validated. |
| `-o sshStrictKey=` `yn_value` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-s` | Displays statistical information. It is important that the primary and standby nodes are running a network time service to ensure that the statistics are meaningful. |
| `-t` | Displays only transport records from the replication event log. |
| `-v` | Displays verbose output. |
| `standby_host` | Specifies a hostname or IP address for one of the standby hosts to be processed when the `-u` option is specified. |
| \[ `snap_shot@` \] `primary_mount_point` | Specifies a location participating in replication, either a directory or a snapshot where the primary file system is mounted. |
| `primary_host` | Specifies a hostname or IP address for one of the primary hosts to be processed when the `-u` option is specified. |
| \[ `snap_shot@` \] `standy_mount_point` | Specifies a location participating in replication, either a directory or a snapshot where the standby file system is mounted. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary or standby file system. |

To display information about replication configuration, use `acfsutil` `repl` `info` with the `-c` option. The configuration information includes a `Applied` `primary` `as` `of` timestamp that identifies the point in time on the primary location that the standby location represents. You can use this timestamp to set back a database to this point in time if it is necessary to keep the data in Oracle ACFS location synchronized with the database data replicated with Oracle Data Guard.

When specifying the `-u` option, the command should be run as `repluser`, the replication user. With this option, the command confirms that `ssh`, as used by snapshot-based replication, can connect from the local cluster to the remote cluster. The command should be used in two contexts:

- On each host of the primary cluster, to confirm that `ssh` can connect to all standby hosts and log in as user on each host
- On each host of the standby cluster, to confirm that `ssh` can connect to all primary hosts and log in as user on each host

When the command is run on a primary host, each *standby\_host* string specifies a hostname or host IP address for a standby node. The specified \[`snap_shot@`\] `primary_mount_point` should be the active Oracle ACFS location in the primary cluster that is to be used for replication.

When the command is run on a standby host, each *primary\_host* string specifies a hostname or host IP address for a primary node. The specified \[`snap_shot@`\] `standby_mount_point` should be the active Oracle ACFS location in the standby cluster that is to be used for replication.

In all cases, the user specified should be the same as the *repluser* specified in the `acsfutil` `repl` `init` command. If strict host-key checking was or is to be disabled for this instance of replication, for example with `acsfutil` `repl` `init` `primary` using `-o sshStrictKey=no`, then the option should also be specified here to skip host-key validation. `acfsutil` `repl` `info` `-c` `-u` can be run at any time, whether or not replication is currently active on the specified Oracle ACFS location.

To display information about replication statistics, use `acfsutil` `repl` `info` with the `-s` option.

To display information about all replication events, use `acfsutil` `repl` `info` with no options. To display information about a specific kind of event, use `acfsutil` `repl` `info` with the `-a`, `-e`, or `-t` option.

Examples

The following example shows the use of the `acfsutil` `repl` `info` command.

Example: Using the acfsutil repl info command

The validation command has the following format:

```
# /sbin/acfsutil repl info -c -u repluser standby-addr1 [standby-addr2 ...] my_primary_mountpoint
```

The command confirms that user `repluser` can use `ssh` to connect to each *standby-addr* given in the same way as replication does when initializing. The *my\_primary\_mountpoint* given should be the active Oracle ACFS mount point that is to be used for replication.

If you have two standby nodes named *standby1* and *standby2*, and also have a VIP named *standby12\_vip* that can designate either node, then you can validate the key setup for the *standby1* / *standby2* cluster by running the following command on each node of the primary cluster:

```
# /sbin/acfsutil repl info -c -u repluser standby1 standby2 my_primary_mountpoint
```

The same command would be used for validation using the VIP *standby12\_vip* to connect to the cluster.

If you plan to disable strict host key checking, you can skip this checking by adding the `-o` `sshStrictKey=no` option to the command line.

Additional commands for displaying statistics and apply records are the following:

```
$ /sbin/acfsutil repl info -s -n 5d /acfsmounts/acfs1

$ /sbin/acfsutil repl info -a -v /acfsmounts/acfs1
```

### acfsutil repl init

Purpose

Initiates replication on all the files in an Oracle ACFS storage location or only those files with a specified list of tags.

Syntax and Description

```
acfsutil repl init -h

acfsutil repl init standby -u repluser [-d trace_level] [snap_shot@]standby_mount_point

acfsutil repl init primary -s repluser@netname { -C | -M | -i interval} [tag_name...]
  [-m [snap_shot@]standby_mount_point] [-d trace_level] [-z {on | off}]
  [-o sshCmdPath=pathname] [-o sshStrictKey=ynvalue]
  [-o sshCipher=ciphername] [-p repluser@netname] [-o sshOptions=options]
  [-p [repluser@]netname] [snap_shot@]primary_mount_point
```

`acfsutil` `repl` `init` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `init` command.

Table: Options for the acfsutil repl init command

| Option | Description |
| --- | --- |
| `primary` | Specifies replication of the primary location. |
| `standby` | Specifies replication of the standby location. |
| `-s` `repluser` `@` `netname` | Specifies a standard `ssh` connection string for the primary site to contact the standby site.  The *repluser* in the connection string is the user that `ssh` logs in as on the standby node. Choose a minimally-privileged user identity. The user should have Oracle ASM administrator privileges and should belong to the Oracle DBA group.  > Note: >  > The same user and group identities (including all `uids` and `gids`) must be specified for the replication user on both your primary cluster and your standby cluster.  The *netname* in the connection string specifies a network endpoint, such as a host name, VIP name, or IP address. |
| `-C` | Specifies replication in constant mode. Snapshots are continuously generated and replicated to the standby site. As soon as the replication of each snapshot completes, the generation of a new snapshot is started. |
| `-M` | Specifies replication in manual mode. After the initial replication operation is performed, no further replication occurs until requested manually by running `acfsutil` `repl` `sync`. |
| `-i` `interval` | Specifies replication in interval (scheduled) mode. A new snapshot is taken and replicated with the frequency specified, if possible. A suffix must be given to specify the units in which interval is measured. The suffix must be either `s` (seconds), `m` (minutes), `h` (hours), `d` (days), or `w` (weeks). For example, `30m` is thirty minutes and `2h` is two hours. |
| `tag_name` | Specifies one or more tag names to be used in restricting replication. When tag names are specified, only files that are tagged with at least one of the those tag names are replicated. For information about Oracle ACFS tags, refer [Oracle ACFS Tagging](introducing-oracle-acfs-and-oracle-advm.md). |
| `-m` `[` `snap_shot@` `]` `standby_mount_point` | Specifies the standby storage location, if it is different than the primary location. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| `-z` `on` \| `off` | Turns on or off compression of the replication data stream sent from primary to standby. |
| `-o sshCmdPath=` `pathname` | Specifies the pathname to the `ssh` command. |
| `-p` `repluser@netname` | Specifies the network endpoint for the primary location. netname names a network endpoint, such as a host name, VIP name, or IP address. netname is checked to ensure it can be accessed. *repluser* must match the *repluser* specified in the `-s` option.  If `-p` is not given, then the hostname of the machine where this command was invoked is used. |
| `-o sshStrictKey=` `ynvalue` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-o sshCipher=` `ciphername` | Specifies the cipher that is passed to `ssh` to encrypt its sessions. |
| `-o sshOptions=` `options` | Specifies options to be passed to each invocation of `ssh` made by replication. No restrictions are imposed on the contents of *options*. However, the resulting invocation of `ssh` is validated before replication is started, and `acfsutil` `repl` `init` `primary` fails if the validating invocation of `ssh` fails. |
| `-p [` `repluser` `@]` `netname` | Specifies the network endpoint for the primary location. *netname* names a network endpoint, such as a host name, VIP name, or IP address. *netname* is checked to ensure it can be accessed. *repluser*, if given, must match the *repluser* specified to `acfsutil` `repl` `init` `standby`.  If `-p` is not given, then the SCAN VIP associated with the primary cluster, if available, is used as the network endpoint for the primary location. If the SCAN VIP is not available, then the hostname of the machine where this command was invoked is used. |
| `-u` | Specifies the *repluser*. |
| `[` `snap_shot@` `]` `standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |
| `[` `snap_shot@` `]` `primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `init` `primary` and `standby` commands initiate replication between a specified primary site and a specified standby site. The `acfsutil` `repl` `init` `standby` command must be run first. Next, run the `acfsutil` `repl` `init` `primary` command.

When the `acfsutil` `repl` `init` `primary` command completes successfully, processing begins to replicate initial copies of all specified files to the standby location. In addition, any changes to these files and any new files subsequently created in the primary storage location are captured and transported to the standby location. However, successful completion of the command does not indicate that the specified files have been copied in full to the standby location. To monitor the progress of the initial replication of all specified files to the standby location, users can run the `acfsutil` `repl` `info` `-c` command.

The initial replication operation is based on a snapshot of the primary location, which is transferred to the standby location in its entirety. Each subsequent replication operation uses a later snapshot of the primary location, and only the differences between that snapshot and the last previous snapshot are transferred to the standby location.

All directories in the primary location are always replicated to the standby, even if tags are specified.

Symbolic link files are replicated as is. If the symbolic link resolves to an absolute path name, and that path name does not exist on the standby location, then referencing the symbolic link results in errors.

On platforms that support named sockets, character device files or block device files, these file types are not replicated.

The file system containing a primary or standby storage location can be mounted on only one mount point in its cluster. The file system does not have to be mounted on all of the nodes in a cluster, but if it is mounted, it must be mounted on the mount point specified with the `acfsutil` `repl` `init` command. In addition, no other file system can be mounted on that mount point on other nodes.

A single Oracle ACFS location cannot be configured both as a primary and a standby location. If replication is configured on the same host or within the same cluster, then the primary and standby locations cannot use the same named mount point.

Replication is allowed between sites running any combination of the Linux, Solaris or AIX operating systems.

Examples

The following example shows the use of the `acfsutil` `repl` `init` to initiate snapshot-based replication from the primary to standby site.

Example: Using the acfsutil repl init command

```
# /sbin/acfsutil repl init standby -u my_repluser /my_standby/repl_data

# /sbin/acfsutil repl init primary -s my_repluser@my_host -i 2h
                                   -m /my_standby/repl_data /my_primary/repl_data
```

### acfsutil repl pause

Purpose

Pauses replication on an Oracle ACFS primary location.

Syntax and Description

```
acfsutil repl pause -h
acfsutil repl pause [snap_shot@]mount_point
```

`acfsutil` `repl` `pause` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `pause` command.

Table: Options for the acfsutil repl pause command

| Option | Description |
| --- | --- |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `pause` command is issued at the primary replication site only. To continue replication operations, `acfsutil` `repl` `resume` should be run at a later time on the same primary site.

`acfsutil` `repl` `pause` stops the operation of the replication daemon temporarily. Subsequent running of `acfsutil` `repl` `resume` resumes the operation of the daemon.

If `acfsutil` `repl` `pause` is run while a replication operation is active, then the active replication operation completes regardless of the pause action. The pause operation is not effective in this case, and the command does not return, until the current data stream has been applied on the standby. After that, operations are not performed for this replication until the `acfsutil` `repl` `resume` is issued.

Note:

If replication is paused when using `acfsutil` `repl` `reverse`, or when using `acfsutil` `repl` `failover` with both the primary and the standby operating normally, then planned failover fails. To enable planned failover to succeed in these situations, run `acfsutil` `repl` `resume`.

Examples

The following example shows the use of the `acfsutil` `repl` `pause` command.

Example: Using the acfsutil repl pause command

```
$ /sbin/acfsutil repl pause /acfsmounts/acfs1
```

### acfsutil repl resume

Purpose

Resumes replication on an Oracle ACFS location where replication has been paused.

Syntax and Description

```
acfsutil repl resume -h
acfsutil repl resume [snap_shot@]mount_point
```

`acfsutil` `repl` `resume` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `resume` command.

Table: Options for the acfsutil repl resume command

| Option | Description |
| --- | --- |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `resume` command resumes the replication process after the `acfsutil` `repl` `pause` command has been run. This command should be run on the same primary site soon after replication has been paused with the `acfsutil` `repl` `pause` command.

Examples

The following example shows the use of the `acfsutil` `repl` `resume` command.

Example: Using the acfsutil repl resume command

```
$ /sbin/acfsutil repl resume /acfsmounts/acfs1
```

### acfsutil repl reverse

Purpose

Reverses the roles of the replication primary and standby locations.

Note:

Starting with Oracle Grid Infrastructure 19c Release Update 19.14, use the `acfsutil repl switchover` command instead of running the `acfsutil repl reverse` command twice. The `acfsutil repl reverse` command is still supported. The `acfsutil repl switchover` command performs the same role reversal in a single step, simplifying the process.

Syntax and Description

```
acfsutil repl reverse -h
acfsutil repl reverse primary [snap_shot@]mount_point
acfsutil repl reverse standby [-o sshCmdPath=path_name] [snap_shot@]mount_point
```

`acfsutil` `repl` `reverse` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `reverse` command.

Table: Options for the acfsutil repl reverse command

| Option | Description |
| --- | --- |
| `primary` | Specifies the primary location. |
| `standby` | Specifies the standby location. |
| `-o sshCmdPath=` `path_name` | Specifies the *path\_name* to the `ssh` command on the current standby location. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `reverse` command reverses the roles of a replication primary and standby location without requiring replication to be terminated and restarted. First, complete the necessary configuration for role reversal replication that is described in [Configuring Oracle ACFS Snapshot-Based Replication](configuring-oracle-acfs-snapshot-based-replication.md). After the configuration is completed, perform the following steps for role reversal of the primary and standby:

1. To begin the role reversal, run the `acfsutil` `repl` `reverse` `primary` operation in the primary cluster. This step ensures that the primary replication location, standby replication location, and the backup snapshot of the standby are all identical, and then converts the current primary to be a standby. Replication is now suspended until the final step is completed.
2. To complete the role reversal, run the `acfsutil` `repl` `reverse` `standby` operation in the standby cluster. This step converts the current standby replication location to be a primary location, then resumes replication from the new primary to the new standby.

You should quiesce application updates to the current primary before running `acfsutil` `repl` `reverse` `primary`. Any updates attempted to the current primary after its conversion to a standby fail, just as updates would to any other standby. When application updates are resumed, they must be directed to the new primary.

Examples

The following example shows the use of the `acfsutil` `repl` `reverse` command.

Example: Using the acfsutil repl reverse command

```
acfsutil repl reverse primary /my_primary/repl_data
acfsutil repl reverse standby /my_standby/repl_data
```

### acfsutil repl switchover

Purpose

Converts the role of the replication standby location to that of a primary location, and the role of the corresponding primary location to that of a standby.

Syntax and Description

```
acfsutil repl switchover -h
acfsutil repl switchover [-T timeout] [snap_shot@]mount_point
```

`acfsutil` `repl` `switchover` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `switchover` command.

Table: Options for the acfsutil repl switchover command

| Option | Description |
| --- | --- |
| `-T` `timeout` | Specifies the time to wait (minutes) before determining that the primary location is unavailable. If the `-T` option is omitted, the primary location is checked once for availability. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil repl switchover` command is issued at the standby replication site only. The command reverses the role of a replication standby location such that it becomes a replication primary location and the role of a replication primary such that it becomes a standby. There is no data loss. The switchover command fails in the case where replication between the primary and standby locations is not operating normally. Such situations include when the standby site can't communicate with the primary site, when the primary location is not available, or if replication is paused. In these situations, the `acfsutil repl failover` command may be used to perform an unplanned failover. You should quiesce application updates to the primary before running `acfsutil repl switchover`. Any updates attempted to the primary location after its conversion fail, just as updates would to any other standby location. When application updates are resumed, they must be directed to the new primary location.

Examples

The following example shows the use of the `acfsutil repl switchover` command. The command is invoked at the standby replication site and specifies the standby storage location (`/repl_data`).

Example: Using the acfsutil repl switchover command

```
acfsutil repl switchover /repl_data
```

### acfsutil repl sync

Purpose

Synchronizes primary and standby locations.

Syntax and Description

```
acfsutil repl sync -h
acfsutil repl sync [apply] [snap_shot@]mount_point
```

`acfsutil` `repl` `sync` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `sync` command.

Table: Options for the acfsutil repl sync command

| Option | Description |
| --- | --- |
| `apply` | Specifies that all changes be applied to the standby location. Currently has no effect on the operation of the command. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `sync` command can be used to synchronize the state of the primary site and the standby site. This command can only be run on the primary site. Users should first quiesce their applications and issue a `sync(1)` call to ensure that the synchronized state is known and meaningful to the user. Running `acfsutil` `repl` `sync` then ensures all outstanding replication data is shipped from the primary site to the standby site. Specifically, the command enables any in-progress replication operation to complete, and then performs replication one final time to ensure that all changes on the primary have been replicated.

The command completes successfully when all of the changes have been successfully applied to the replication location on the standby site. At this point, unless an unmount of the last node on the primary site cluster is about to occur, applications may be restarted.

Successfully unmounting a replicated location on the primary site does not guarantee that all changes made prior to the unmount have been successfully sent to the standby site or applied to the standby location. If the primary location is on a file system that is unmounted on one primary site node, but remains mounted on one or more primary site nodes, changes to the location made before the unmount continue to be transported to the standby site from the other nodes after the unmount. However, if you are in the process of unmounting the primary location on the last primary site node where it is mounted, and if you want to know that all file system changes on the primary location up to that point have been successfully applied to the standby location, then you should perform the following operations to ensure that the standby location is up to date.

- Quiesce applications on the primary site which modify the replication location.
- Run `acfsutil` `repl` `sync`.

After `acfsutil` `repl` `sync` has returned successfully, you can unmount the file system which contains the participating replication location. Unmounting the file system stops the replication background process for that location.

Examples

The following example shows the use of the `acfsutil` `repl` `sync` command.

Example: Using the acfsutil repl sync command

```
$ /sbin/acfsutil repl sync /acfsmounts/acfs1
```

### acfsutil repl terminate

Purpose

Stops all replication activity on the Oracle ACFS location at the site where it is run.

Syntax and Description

```
acfsutil repl terminate -h
acfsutil repl terminate primary [-d trace_level] [snap_shot@]mount_point
acfsutil repl terminate standby [remote [-f]] [immediate] [-k] [-d trace_level] [snap_shot@]mount_point
```

`acfsutil` `repl` `terminate` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `terminate` command.

Table: Options for the acfsutil repl terminate command

| Option | Description |
| --- | --- |
| `primary` | Stops replication on the primary location. |
| `standby` | Stops replication on the standby location. |
| `remote [-f]` | Stops replication processing on the primary location before stopping the processing on the standby location.  When the remote keyword is given, the `-f` option forces the termination of replication on the standby location even if replication on the primary location cannot be terminated. |
| `immediate` | Stops replication processing immediately on the standby location. |
| `-k` | Specifies to keep any backup snapshot that is present for the standby. However, this option does not ensure that a backup snapshot exists, and the absence of such a backup snapshot is not an error.  If this option is not specified, then any backup snapshot present is deleted. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `terminate` command stops all replication processing. When terminating replication, you should terminate replication for the primary location first, and then the standby location. If you want to ensure all changes are sent to the standby location before terminating the primary site, ensure that all applications are quiesced and run the `acfsutil` `repl` `sync` command. The terminate command must be run on both sites if both sites hosting the locations are available.

After `acfsutil` `repl` `terminate` `standby` has been run, you can use the standby location in read-write mode. If you want to restart replication after running `acfsutil` `repl` `terminate`, then you must restart replication from the beginning with the `acfsutil` `repl` `init` command.

The `repl` `terminate` `standby` command waits until replication data at the standby location has been applied. If you want to terminate replication immediately without applying all the replication data, use the `immediate` option. However, this option can leave some files at the standby location in an indeterminate state.

To momentarily stop Oracle ACFS replication, you can use the `acfsutil` `repl` `pause` command, followed soon after by the `acfsutil` `repl` `resume` command.

Note:

Running `acfsutil` `repl` `terminate` `standby` with the `remote` option fails:

- If the primary location is paused.
- While the primary location is converting to a standby.

For example, if `acfsutil` `repl` `reverse` `primary` has been invoked on the primary location.

Examples

The following example shows the use of the `acfsutil` `repl` `terminate` command.

Example: Using the acfsutil repl terminate command

```
$ /sbin/acfsutil repl terminate /acfsmounts/acfs1
```

### acfsutil repl trace

Purpose

Sets the replication trace level for gathering trace information on an Oracle ACFS location.

Syntax and Description

```
acfsutil repl trace -h
acfsutil repl trace level [snap_shot@]mount_point
```

`acfsutil` `repl` `trace` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `trace` command.

Table: Options for the acfsutil repl trace command

| Option | Description |
| --- | --- |
| `level` | Specifies the trace level setting \[0..6\]. The default level is 2. |
| \[ `snap_shot@` \] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

Increasing the trace level can have a performance impact and should be done at the recommendation of Oracle support services.

Trace files for Oracle ACFS replication are stored in the following location:

```
GRID_BASE/diag/crs/hostname/crs/trace
```

In the location above, `GRID_BASE` specifies the `ORACLE_BASE` of the Oracle Grid Infrastructure home.

Examples

The following example shows the use of the `acfsutil` `repl` `trace` command.

Example: Using the acfsutil repl trace command

```
$ /sbin/acfsutil repl trace 5 /acfsmounts/acfs1
```

### acfsutil repl update

Purpose

Updates replication information after replication has started and is running on an Oracle ACFS location.

Syntax and Description

```
acfsutil repl update -h

acfsutil repl update  [-s repluser@netname] [-C | -M | -i interval]
  [-d trace_level] [-z {on | off}]
  [-o sshCmdPath=pathname] [-o sshStrictKey=ynvalue] [-o sshCipher=ciphername]
  [-p repluser@netname]
  [-m [snap_shot@]standby_mount_point]
  [snap_shot@]primary_mount_point
acfsutil repl update [-u repluser] [-d trace_level] [snap_shot@]standby_mount_point
```

`acfsutil` `repl` `update` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `update` command.

Table: Options for the acfsutil repl update command

| Option | Description |
| --- | --- |
| `-s` `repluser` `@` `netname` | Specifies a standard `ssh` connection string for the primary site to contact the standby site.  The *repluser* in the connection string is the user that `ssh` logs in as on the standby node. Choose a minimally-privileged user identity. The user should have Oracle ASM administrator privileges and should belong to the Oracle DBA group.  The *netname* in the connection string specifies a network endpoint, such as a host name, VIP name, or IP address. |
| `-C` | Specifies replication in constant mode. Snapshots are continuously generated and replicated to the standby site. As soon as the replication of each snapshot completes, the generation of a new snapshot is started. |
| `-M` | Specifies replication in manual mode. After the next replication operation is performed, no further replication occurs until requested manually by running acfsutil repl sync. |
| `-i` `interval` | Specifies replication in interval (scheduled) mode. A new snapshot is taken and replicated with the frequency specified, if possible. A suffix must be given to specify the units in which interval is measured. The suffix must be either `s` (seconds), `m` (minutes), `h` (hours), `d` (days), or `w` (weeks). For example, `30m` is thirty minutes and `2h` is two hours. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| `-z` `on` \| `off` | Turns on or off compression of the replication data stream sent from primary to standby. |
| `-o sshCmdPath=` `pathname` | Specifies the pathname to the `ssh` command. |
| `-o sshStrictKey=` `ynvalue` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-o sshCipher=` `ciphername` | Specifies the cipher that is passed to `ssh` to encrypt its sessions. |
| `-p` `repluser@netname` | Specifies a new replication user, a new network endpoint, or both for the primary site. *netname* names a network endpoint, such as a host name, VIP name, or IP address. *netname* is checked to ensure it can be accessed.  If the existing value for *repluser* or *netname* is specified, it will continue to be used. |
| `-u` | Specifies the *repluser*. |
| `-m [` `snap_shot@` `]` `standby_mount_point` | Specifies the standby storage area. |
| \[ `snap_shot@` \] `primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |
| \[ `snap_shot@` \] `standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |

The `acfsutil` `repl` `update` command updates replication information and configuration after replication has been started. For example, a system administrator can change the network interface that is currently being used by replication to connect to the remote site. Issuing the `acfsutil` `repl` `update` command to update the configuration in this situation enables replication to continue running uninterrupted.

If `acfsutil` `repl` `update` is run on the primary site, the command can be used to alter the user name and network interface name (hostname or VIP name) that is used to connect to the standby site as well as to alter the standby storage location.. The command can also be used to change the replication interval or tracing level, change the cipher used by or the pathname used for `ssh`, and turn compression on or off. Finally, the command can be used to update the network interface recorded for the primary site.

If `acfsutil` `repl` `update` is run on the standby site, the command can be used to alter either the tracing level or the user name used by the primary site to connect to the standby site.

At least one of the options must be specified when issuing this command; the command cannot be run with only the required location.

The `acfsutil` `repl` `update` command returns success when the updated information has been accepted on the local site. To change the user name, the command must be run on both the primary and the standby sites. If the replication interval is changed with the `-C` or `-i` option, a replication operation occurs at the point when `acfsutil` `repl` `update` is run. The next replication operation occurs based on the newly-specified interval.

Examples

The following example shows the use of the `acfsutil` `repl` `update` command.

Example: Using the acfsutil repl update command

```
$ /sbin/acfsutil repl update -i 1h /my_primary/repl_data
```

### acfsutil repl upgrade

Purpose

Upgrades an existing replication installation to snapshot-based replication.

Syntax and Description

```
acfsutil repl upgrade -h

acfsutil repl upgrade prepare -s {repluser@netname | -u} primary_mount_point

acfsutil repl upgrade standby standby_mount_point

acfsutil repl upgrade primary {-C | -M | -i interval}
  [-d trace_level] [-z {on | off}]
  [-o sshCmdPath=pathname] [-o sshStrictKey=ynvalue]
  [-o sshCipher=ciphername]
  primary_mount_point
```

`acfsutil` `repl` `upgrade` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `upgrade` command.

Table: Options for the acfsutil repl upgrade command

| Option | Description |
| --- | --- |
| `prepare` | Prepares an existing replication installation for upgrade to snapshot-based replication. |
| `-s` `repluser` `@` `netname` | Specifies a standard `ssh` connection string for the primary site to contact the standby site.  The *repluser* in the connection string is the user that `ssh` logs in as on the standby node. Choose a minimally-privileged user identity. The user should have Oracle ASM administrator privileges and should belong to the Oracle DBA group.  The *netname* in the connection string specifies a network endpoint, such as a host name, VIP name, or IP address. |
| `-u` ( `prepare` option) | Undoes a completed `acfsutil` `repl` `upgrade` `prepare` operation.  This action restores the `<span class="codeinlineitalic">primary_mount_point</span>` to its state before the previously completed `acfsutil` `repl` `upgrade` `prepare` operation. |
| `standby` | Specifies replication of the standby file system. |
| `standby_mount_point` | Specifies the directory where the standby file system is mounted. |
| `primary` | Specifies replication of the primary file system. |
| `-C` | Specifies replication in constant mode. Snapshots are continuously generated and replicated to the standby site. As soon as the replication of each snapshot completes, the generation of a new snapshot is started. |
| `-M` | Specifies replication in manual mode. After a single replication operation is performed, no further replication occurs until requested manually by running `acfsutil` `repl` `sync`. |
| `-i` `interval` | Specifies replication in interval (scheduled) mode. A new snapshot is taken and replicated with the frequency specified, if possible. A suffix must be given to specify the units in which interval is measured. The suffix must be either `s` (seconds), `m` (minutes), `h` (hours), `d` (days), or `w` (weeks). For example, `30m` is thirty minutes and `2h` is two hours. |
| `-d` `trace_level` | Specifies the trace level setting (0..6). |
| `-z` `on` \| `off` | Turns on or off compression of the replication data stream sent from primary to standby. |
| `-o sshCmdPath=` `pathname` | Specifies the pathname to the `ssh` command. |
| `-o sshStrictKey=` `ynvalue` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-o sshCipher=` `ciphername` | Specifies the cipher that is passed to `ssh` to encrypt its sessions. |
| `primary_mount_point` | Specifies the directory where the primary file system is mounted. |

The `acfsutil` `repl` `upgrade` command provides support for upgrading an active, existing replication relationship to use snapshot-based replication. The intent of the upgrade process is to provide an active snapshot-based replication relationship between the current primary and standby file systems without terminating or reinitiating replication and without losing any data in the replicating process.

Before you start the upgrade procedure, you must ensure that the primary file system is mounted on only one node of its cluster. You should quiesce any application activity targeting the primary or standby file system to ensure an optimal upgrade; however, the upgrade proceeds if this recommendation is ignored.

Note:

After the upgrade has been started, the process must be completed. The `acfsutil` `repl` `upgrade` `prepare` operation can be undone using the `-u` option. However, after the `acfsutil` `repl` `upgrade` `standby` operation has been started, the entire upgrade process must be completed. From that point forward, there is no provision for stopping or undoing the upgrade.

To begin the upgrade process, first run the `acfsutil` `repl` `upgrade` `prepare` command on the primary cluster. This command specifies the user and host or interface name, as well as the primary mount point, that is used for snapshot-based replication. The user and host names are given with the `-s` option, the same as with the `acfsutil` `repl` `init` `primary` command option for snapshot-based replication.

Next, upgrade the standby site. On the standby, run the `acfsutil` `repl` `upgrade` `standby` command. This command specifies the standby mount point that is used for snapshot-based replication.

After this command has been issued, the upgrade must be completed by issuing the `acfsutil` `repl` `upgrade` `primary` command.

After the `acfsutil` `repl` `upgrade` `standby` command has been run on the standby site, the `acfsutil` `repl` `upgrade` `primary` command must be run on the primary site to complete the upgrade to snapshot-based replication. This command automatically terminates the original replication process and initiates snapshot-based replication. `acfsutil` `repl` `upgrade` `primary` accepts any of the command-line options accepted by the `acfsutil` `repl` `init` `primary` command for snapshot-based replication, except for the `-m` option, `-s` option, and tag names. The necessary information for the `-m` and `-s` options has been obtained from other sources. Any tag names that were specified for the original replication relationship are automatically transferred to the new relationship. For information about Oracle ACFS tags, refer to [Oracle ACFS Tagging](introducing-oracle-acfs-and-oracle-advm.md).

On platforms supporting named sockets, character device files or block device files, snapshot-based replication does not replicate these file types. However, the `acfsutil` `repl` `upgrade` process preserves any files of these types that already exist on the standby file system. They are not further updated, but are not deleted as part of the upgrade.

Examples

The following example shows the use of the `acfsutil` `repl` `upgrade` command.

Example: Using the acfsutil repl upgrade command

```
# /sbin/acfsutil repl upgrade prepare -s my_repluser@my_host /my_primary/repl_data

# /sbin/acfsutil repl upgrade standby /my_standby/repl_data

# /sbin/acfsutil repl upgrade primary -i 2h /my_primary/repl_data
```

## Oracle ACFS Command-Line Tools for Auditing

This topic provides a summary of the commands for Oracle ACFS auditing.

The Oracle ACFS auditing command summary lists the Oracle ACFS auditing commands with brief descriptions. For an overview of Oracle ACFS auditing, refer to [Oracle ACFS Auditing](introducing-oracle-acfs-and-oracle-advm.md).

For information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Note:

Starting with Oracle ACFS 19c (19.5), Oracle ACFS Security (Vault) and ACFS Auditing are deprecated. Deprecating certain clustering features with limited adoption enables Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS Security (Vault) and Oracle ACFS Auditing are deprecated, and can be desupported in a future release.

Table: Summary of commands for Oracle ACFS auditing

| Command | Description |
| --- | --- |
| acfsutil audit archive | Forces an archival of the audit trail. |
| acfsutil audit disable | Disables auditing for Oracle ACFS encryption or security. |
| acfsutil audit enable | Enables auditing for Oracle ACFS encryption or security. |
| acfsutil audit info | Displays auditing information. |
| acfsutil audit init | Initializes auditing on an Oracle ACFS environment. |
| acfsutil audit purge | Purges the audit trail for a specified file system. |
| acfsutil audit read | Marks the audit trail to indicate that the audit trail has been read. |

### acfsutil audit archive

Purpose

Forces an archival of the audit trail for the current host on the specified Oracle ACFS file system.

Syntax and Description

```
acfsutil audit archive -h
acfsutil audit archive -m mount_point
```

`acfsutil` `audit` `archive` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `archive` command.

Table: Options for the acfsutil audit archive command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

You can use the `acfsutil` `audit` `archive` command to safely back up or remove audit data without the possibility of losing intermediate audit messages.

Only an audit manager can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `archive` command.

Example: Using the acfsutil audit archive command

```
$ /sbin/acfsutil audit archive -m /acfsmounts/acfs1
```

### acfsutil audit disable

Purpose

Disables auditing for either Oracle ACFS encryption or security on a specified file system.

Syntax and Description

```
acfsutil audit disable -h
acfsutil audit disable -m mount_point -s {encr |sec}
```

`acfsutil` `audit` `disable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `disable` command.

Table: Options for the acfsutil audit disable command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-s` { `encr` \| `sec` } | Specifies whether to disable auditing for encryption or security. |

Only an audit manager can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `disable` command.

Example: Using the acfsutil audit disable command

```
$ /sbin/acfsutil audit disable -m /acfsmounts/acfs1 -s encr
```

### acfsutil audit enable

Purpose

Enables auditing for either Oracle ACFS encryption or security on a specified file system.

Syntax and Description

```
acfsutil audit enable -h
acfsutil audit enable -m mount_point -s {encr |sec}
```

`acfsutil` `audit` `enable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `enable` command.

Table: Options for the acfsutil audit enable command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-s` { `encr` \| `sec` } | Specifies whether to enable auditing for encryption or security. |

The `acfsutil` `audit` `enable` command may also create the *mount\_point* `/.Security/audit` directory, which is a location for audit source files. The audit directory is created when auditing first is enabled for a file system, as a result of either the `acfsutil` `encr` `set`, `acfsutil` `sec` `prepare`, or a `cfsutil` `audit` `enable` command.

Only an audit manager can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `enable` command.

Example: Using the acfsutil audit enable command

```
$ /sbin/acfsutil audit enable -m /acfsmounts/acfs1 -s encr
```

### acfsutil audit info

Purpose

Displays auditing information.

Syntax and Description

```
acfsutil audit info -h
acfsutil audit info [-m mount_point ]
```

`acfsutil` `audit` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `info` command.

Table: Options for the acfsutil audit info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Optionally specifies the directory where the file system is mounted. |

Only an audit manager can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `info` command.

Example: Using the acfsutil audit info command

```
$ /sbin/acfsutil audit info -m /acfsmounts/acfs1

Auditing information for '/acfsmounts/acfs1':
Audit trail size: 10MB
Archive File: READ
Audit Sources:
Security: ENABLED
Encryption: ENABLED
```

### acfsutil audit init

Purpose

Initializes Oracle ACFS auditing.

Syntax and Description

```
acfsutil audit init -h
acfsutil audit init -M audit_manager_group -A auditor_group
```

`acfsutil` `audit` `init` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `init` command.

Table: Options for the acfsutil audit init command

| Option | Description |
| --- | --- |
| `-M` `audit_manager_group` | Specifies the operating system (OS) group which assigns users to the Oracle ACFS audit manager role. To achieve separation of duties, you should create a new group specifically for this purpose and this group should be different from the system administrator group, Oracle ACFS security administrator OS group, and the Oracle ACFS audit auditor OS group |
| `-A` `auditor_group` | Specifies the operating system (OS) group which assigns users to the Oracle ACFS audit auditor role. To achieve separation of duties, you should create a new group specifically for this purpose and this group should be different from the system administrator group, Oracle ACFS security administrator OS group, and the Oracle ACFS audit manager OS group. |

The `acfsutil` `audit` `init` command must be run by the system administrator before enabling auditing for any of the audit sources on a file system. The command sets up the required roles for auditing and must be run before any type of auditing can be enabled on a file system. After running the command, auditing is enabled by default for all features which use auditing.

Because you cannot choose a different OS group for either the Oracle ACFS audit manager or auditor after initialization, you should create new OS groups for these specific purposes before initializing Oracle ACFS auditing.

Only a system administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `init` command.

Example: Using the acfsutil audit init command

```
# /sbin/acfsutil audit init -M myaudit_mgr_grp -A myauditor_grp
```

### acfsutil audit purge

Purpose

Purges the audit trail for a specified file system.

Syntax and Description

```
acfsutil audit purge -h
acfsutil audit purge -m mount_point [-f]
```

`acfsutil` `audit` `purge` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `purge` command.

Table: Options for the acfsutil audit purge command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-f` | Forces the removal of the audit trail even if the audit auditor has not marked the file as read using the `acfsutil` `audit` `read` command. |

Only an audit manager can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `purge` command.

Example: Using the acfsutil audit purge command

```
$ /sbin/acfsutil audit purge -m /acfsmounts/acfs1 -f
```

### acfsutil audit read

Purpose

Marks the audit trail to indicates to the audit manager that the log archive file for the current node has been reviewed, backed up as necessary, and is safe to purge.

Syntax and Description

```
acfsutil audit read -h
acfsutil audit read -m mount_point
```

`acfsutil` `audit` `read` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `audit` `read` command.

Table: Options for the acfsutil audit read command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

Only an audit auditor can run this command.

Examples

The following example shows the use of the `acfsutil` `audit` `read` command.

Example: Using the acfsutil audit read command

```
$ /sbin/acfsutil audit read -m /acfsmounts/acfs1
```

## Oracle ACFS Command-Line Tools for Security

This topic provides a summary of the commands for Oracle ACFS security.

The Oracle ACFS security command summary lists the Oracle ACFS security commands with brief descriptions. For an overview of Oracle ACFS security, refer to [Oracle ACFS Security](introducing-oracle-acfs-and-oracle-advm.md).

For more information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Note:

Starting with Oracle ACFS 19c (19.5), Oracle ACFS Security (Vault) and ACFS Auditing are deprecated. Deprecating certain clustering features with limited adoption enables Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS Security (Vault) and Oracle ACFS Auditing are deprecated, and can be desupported in a future release.

Table: Summary of commands for Oracle ACFS security

| Command | Description |
| --- | --- |
| acfsutil sec admin add | Adds a security administrator. |
| acfsutil sec admin info | Lists the Oracle ACFS security administrators. |
| acfsutil sec admin password | Changes the password of a security administrator. |
| acfsutil sec admin remove | Removes a security administrator. |
| acfsutil sec batch | Runs a batch file. |
| acfsutil sec disable | Disables Oracle ACFS security. |
| acfsutil sec enable | Enables Oracle ACFS security. |
| acfsutil sec info | Displays Oracle ACFS file system security information. |
| acfsutil sec info file | Lists the security realms that a specified file or directory belongs to. |
| acfsutil sec init | Initializes Oracle ACFS file system security. |
| acfsutil sec load | Loads Oracle ACFS file system security metadata. |
| acfsutil sec prepare | Prepares an Oracle ACFS file system for security. |
| acfsutil sec realm add | Adds objects to an Oracle ACFS file system security realm. |
| acfsutil sec realm audit disable | Disables auditing of command rules for files in an Oracle ACFS security realm. |
| acfsutil sec realm audit enable | Enables auditing of command rules for files in an Oracle ACFS security realm. |
| acfsutil sec realm audit info | Displays the realm auditing information for a specified Oracle ACFS security realm. |
| acfsutil sec realm clone | Clones an Oracle ACFS file system security realm. |
| acfsutil sec realm create | Creates an Oracle ACFS file system security realm. |
| acfsutil sec realm delete | Removes objects from an Oracle ACFS file system security realm. |
| acfsutil sec realm destroy | Removes an Oracle ACFS file system security realm. |
| acfsutil sec rule clone | Clones an Oracle ACFS file system security rule. |
| acfsutil sec rule create | Creates an Oracle ACFS file system security rule. |
| acfsutil sec rule destroy | Removes an Oracle ACFS file system security rule. |
| acfsutil sec rule edit | Updates an Oracle ACFS file system security rule. |
| acfsutil sec ruleset clone | Clones an Oracle ACFS file system security rule set. |
| acfsutil sec ruleset create | Creates an Oracle ACFS file system security rule set. |
| acfsutil sec ruleset destroy | Removes an Oracle ACFS file system rule set. |
| acfsutil sec ruleset edit | Updates an Oracle ACFS file system rule set. |
| acfsutil sec save | Saves Oracle ACFS file system security metadata. |

### acfsutil sec admin add

Purpose

Adds a new security administrator for an Oracle ACFS file system.

Syntax and Description

```
acfsutil sec admin add -h
acfsutil sec admin add admin
```

`acfsutil` `sec` `admin` `add` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `admin` `add` command.

Table: Options for the acfsutil sec admin add command

| Option | Description |
| --- | --- |
| `admin` | Specifies a security administrator user name. The user specified must be an existing operating system user and a member of the security group specified with the `acfsutil` `sec` `init` command.  On Windows, a security administrator user name must be specified with a fully qualified domain user name in the form of *domain\_name* `\` *username*. |

Security administrators are common for all Oracle ACFS file systems in a cluster. A temporary password must be provided for the new security administrator. The password must conform to the format that is described in " acfsutil sec init ".

The new security administrator can change the password with the `acfsutil` `sec` `admin` `password` command. For information, refer to " acfsutil sec admin password ".

Security administrators are allowed to browse all directories in an Oracle ACFS file system whether they have the underlying operating system permissions and whether any realm checks allow it. This exception enables a security administrator to check the location of the files when securing them with Oracle ACFS security realms. However, a security administrator cannot view the contents of individual files without the appropriate operating system and security realm permissions.

Only an existing security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `admin` `add` command.

Example: Using the acfsutil sec admin add command

```
$ /sbin/acfsutil sec admin add sec_admin_three
```

### acfsutil sec admin info

Purpose

Displays a list of the Oracle ACFS security administrators.

Syntax and Description

```
acfsutil -h sec admin info
acfsutil sec admin info
```

`acfsutil` `sec` `admin` `info` `-h` displays help text and exits.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `admin` `info` command.

Example: Using the acfsutil sec info password command

```
$ /sbin/acfsutil sec admin info
```

### acfsutil sec admin password

Purpose

Changes the password of a security administrator for an Oracle ACFS file system.

Syntax and Description

```
acfsutil sec admin password -h
acfsutil sec admin password
```

`acfsutil` `sec` `admin` `password` `-h` displays help text and exits.

The `acfsutil` `sec` `admin` `password` command changes the security password for the administrator that is running the command. When you run this command, you are prompted to enter a new password. The password must conform to the format that is described in " acfsutil sec init ".

Every time a security administrator runs an `acfsutil` `sec` command, the administrator is prompted for the security administrator's password.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `admin` `password` command.

Example: Using the acfsutil sec admin password command

```
$ /sbin/acfsutil sec admin password
ACFS Security administrator password:
New password:
Re-enter new password:
```

### acfsutil sec admin remove

Purpose

Removes a security administrator from an Oracle ACFS file system.

Syntax and Description

```
acfsutil sec admin remove -h
acfsutil sec admin remove admin
```

`acfsutil` `sec` `admin` `remove` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `admin` `remove` command.

Table: Options for the acfsutil sec admin remove command

| Option | Description |
| --- | --- |
| `admin` | Specifies an existing security administrator user name.  On Windows, the security administrator user name must be specified with a fully qualified user name in the form of *domain\_name* `\` *username*. |

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `admin` `remove` command.

Example: Using the acfsutil sec admin remove command

```
$ /sbin/acfsutil sec admin remove sec_admin_three
```

### acfsutil sec batch

Purpose

Runs a specified batch file.

Syntax and Description

```
acfsutil sec batch -h
acfsutil sec batch batch_file
```

`acfsutil` `sec` `batch` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `batch` command.

Table: Options for the acfsutil sec batch command

| Option | Description |
| --- | --- |
| `batch_file` | Specifies an existing batch file name. The batch file contains a list of `acfsutil` `sec` commands. |

The batch file can only contain security realm management commands. Interactive commands are not recommended. The `acfsutil` `sec` `admin` `add`, `acfsutil` `sec` `admin` `password`, and `acfsutil` `sec` `init` commands are not supported in the batch file. Also, other `acfsutil` commands, such as `acfsutil` `encr` commands, are not allowed in the batch file. If a command in the batch file fails, subsequent commands in the batch file are not run.

The following are examples of commands that can be in a batch file:

```
acfsutil sec realm create my_realm1 -m /mnt1 -e off
acfsutil sec realm create my_realm2 -m /mnt2 -e off
```

Only a security administrator can run this command. When the command is run, the administrator is prompted once for a password.

Examples

The following example shows the use of the `acfsutil` `sec` `batch` command.

Example: Using the acfsutil sec batch command

```
$ /sbin/acfsutil sec batch my_batch_file
```

### acfsutil sec disable

Purpose

Disables Oracle ACFS security on a mount point or a realm in a mount point.

Syntax and Description

```
acfsutil sec disable -h
acfsutil sec disable -m mount_point [-S snap_name] [realm]
```

`acfsutil` `sec` `disable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `disable` command.

Table: Options for the acfsutil sec disable command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-S` `snap_name` | Disables security for the specified read-write snapshot. |
| `realm` | Specifies the name of the security realm in the Oracle ACFS file system. |

The `acfsutil` `sec` `disable` `-m` *mount\_point* command disables security functionality on the Oracle ACFS file system specified by the mount point option. When security is disabled on the file system, security realms do not enforce realm authorization.

The `acfsutil` `sec` `disable` `-m` *mount\_point* *realm* command disables security for the realm specified in the command.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `disable` command.

Example: Using the acfsutil sec disable command

```
$ /sbin/acfsutil sec disable -m /acfsmounts/acfs1 my_realm
```

### acfsutil sec enable

Purpose

Enables Oracle ACFS security on a mount point or a realm in a mount point.

Syntax and Description

```
acfsutil sec enable -h
acfsutil sec enable -m mount_point [-S snap_name] [realm]
```

`acfsutil` `sec` `enable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `enable` command.

Table: Options for the acfsutil sec enable command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-S` `snap_name` | Enables security for the specified read-write snapshot. |
| `realm` | Specifies the name of the security realm. |

The `acfsutil` `sec` `enable` `-m` *mount\_point* command enables security functionality on the Oracle ACFS file system specified by the mount point option. When security is enabled on the file system, security realms that have been enabled enforce realm authorization. You should run this command before enabling any individual security realm.

The `acfsutil` `sec` `enable` `-m` *mount\_point* *realm* command enables security for the realm specified in the command. The realm enforces authorization if security has been enabled on the file system.

Only a security administrator can run this command.

Examples

These example shows the use of the `acfsutil` `sec` `enable` command.

Example: Using the acfsutil sec enable command

```
$ /sbin/acfsutil sec enable -m /acfsmounts/acfs1

$ /sbin/acfsutil sec enable -m /acfsmounts/acfs1 my_realm
```

### acfsutil sec info

Purpose

Displays information about Oracle ACFS security.

Syntax and Description

```
acfsutil sec info -h
acfsutil sec info -m mount_point
  [{-n [realm] | -l [rule] |-s [ruleset] |-c }] [-S snap_name]
```

`acfsutil` `sec` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `info` command.

Table: Options for the acfsutil sec info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-n` `realm` | Displays information about the specified security realm. If the realm name is omitted, a list of all realms is displayed. |
| `-l` `rule` | Displays information about the specified rule. If the rule name is omitted, a list of all rules is displayed. |
| `-s` `ruleset` | Displays information about the specified rule set. If the rule set name is omitted, a list of all rule sets is displayed. |
| `-c` | Lists all the command rules. |
| `-S` `snap_name` | Displays information about the realms, rules, and rule sets in the specified snapshot. |

The `acfsutil` `sec` `info` command retrieves information about the list of realms, rules, and rule sets on the specified mount point. By specifying a particular realm, rule, or ruleset, you can retrieve information specific about the specified realm, rule, or ruleset. You can also display information about a specified snapshot.

If the `-m` option is specified without any other options, then the security enabled status and prepared status are displayed for the specified mount point.

To access files in the system security realms, the user should be assigned as a security administrator with the `acfsutil` `sec` `admin` `add` command. Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `info` command.

Example: Using the acfsutil sec info command

```
$ /sbin/acfsutil sec info -m /acfsmounts/acfs1 -n my_realm
```

### acfsutil sec info file

Purpose

Lists the names of the Oracle ACFS security realms that the specified file or directory belongs to.

Syntax and Description

```
acfsutil sec info file -h
acfsutil sec info file -m mount_point path
```

`acfsutil` `sec` `info` `file` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `info` `file` command.

Table: Options for the acfsutil sec info file command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `path` | Specifies the path of the file or directory in the file system. |

This command also displays the encryption status of files.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `info` `file` command.

Example: Using the acfsutil sec info file command

```
$ /sbin/acfsutil sec info file -m /acfsmounts/acfs1
                                  /acfsmounts/acfs1/myfiles
```

### acfsutil sec init

Purpose

Initializes Oracle ACFS security.

Syntax and Description

```
acfsutil sec init -h
acfsutil sec init -u admin -g admin_sec_group
```

`acfsutil` `sec` `init` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `init` command.

Table: Options for the acfsutil sec init command

| Option | Description |
| --- | --- |
| `-u` `admin` | Specifies the first security administrator user name. The user specified must be an existing operating system (OS) user and a member of the operating system group specified by the `-g` option.  On Windows, the security administrator user name must be specified with a fully qualified user name in the form of *domain\_name* `\` *username*. |
| `-g` `admin_sec_group` | Specifies the name of the security group for the administrator. The group specified must be an existing operating system (OS) group.  On Windows, the group name must be specified with a fully qualified domain group name in the form of *domain\_name* `\` *groupname*. If the *domain\_name* `\` *groupname* contains a space, then enclose the string in quotes (" "). |

The `acfsutil` `sec` `init` command creates the storage necessary for security credentials and identifies an operating system user as the first security administrator. The command also identifies the operating system group that is the designated security group. All users that are security administrators must be members of the designated security group. Security administrators are common for all Oracle ACFS file systems.

If you are setting up an OS user and OS group, refer to your operating system-specific (OS) documentation for information.

The `acfsutil` `sec` `init` command is run once to set up Oracle ACFS security for each cluster and can be run from any node in the cluster. Other security commands can also be run from any node in a cluster.

Only the root user or Windows `Administrator` user can run this command. The user specifies a password for the security administrator. The security administrator password must conform to the following format:

- The maximum number of characters is 20.
- The minimum number of characters is 8.
- The password must contain at least one digit.
- The password must contain at least one letter.

The new security administrator can change the password with the `acfsutil` `sec` `admin` `password` command. For information, refer to " acfsutil sec admin password ".

Security administrators are allowed to browse all directories in an Oracle ACFS file system whether they have the underlying operating system permissions and whether any realm checks allow it. This exception enables a security administrator to check the location of the files when securing them with Oracle ACFS security realms. However, a security administrator cannot view the contents of individual files without the appropriate operating system and security realm permissions.

Examples

The following example shows the use of the `acfsutil` `sec` `init` command.

Example: Using the acfsutil sec init command

```
$ /sbin/acfsutil sec init -u grid -g asmadmin
```

### acfsutil sec load

Purpose

Loads Oracle ACFS security metadata into a file system identified by a mount point.

Syntax and Description

```
acfsutil sec load -h
acfsutil sec load -m mount_point -p file
```

`acfsutil` `sec` `load` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `load` command.

Table: Options for the acfsutil sec load command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-p` `file` | Specifies the name of an existing saved security metadata file. |

The `acfsutil` `sec` `load` command loads the security metadata in a saved XML file into the specified Oracle ACFS file system. `acfsutil` `sec` `load` restores only user-created security policies; the command does not add files to the realms.

`acfsutil` `sec` `load` and `acfsutil` `sec` `save` can be used together to copy user-created policies from one file system to another. For example, if you have security policies on one file system that you want to replicate on other file systems, then use `acfsutil` `sec` `save` on the source file system to create an XML backup file. Next, use `acfsutil` `sec` `load` on the other destination file systems to load the saved security metadata and create the same policies. After creating the policies, you can choose to apply policies on different directories and files on that file system by adding directories and files in different realms, according to the policies you want to impose on those files.

To run the `acfsutil` `sec` `load` command, the destination mount point must have a file system that has been prepared for security and does not contain any user-created security objects.

If the file system mounted on destination mount point contains security objects, then you must run `acfsutil` `sec` `prepare` `-u` to remove all previously created security objects on the file system. After successfully running `acfsutil` `sec` `prepare` `-u`, you must run `acfsutil` `sec` `prepare` to prepare the file system for security. After successfully running `acfsutil` `sec` `prepare`, you can run `acfsutil` `sec` `load` on the file system. For information about preparing security on or removing security from a file system, refer to " acfsutil sec prepare ".

The `acfsutil` `sec` `load` command does not load system security realms from the backup file. System security realms are created with the `acfsutil` `sec` `prepare` command; `acfsutil` `sec` `load` does not re-create these realms. For information about the system-created security realms, refer to " acfsutil sec prepare ".

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `load` command.

Example: Using the acfsutil sec load command

```
$ /sbin/acfsutil sec load -m /acfsmounts/acfs1 -p my_metadata_file.xml
```

### acfsutil sec prepare

Purpose

Prepares an Oracle ACFS file system for security features.

Syntax and Description

```
acfsutil sec prepare -h
acfsutil sec prepare [-u] -m mount_point
```

`acfsutil` `sec` `prepare` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `prepare` command.

Table: Options for the acfsutil sec prepare command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-u` | Backs out security for the specified mount point.  This command removes security from in the file system and reverts the file system to the state before `acfsutil` `sec` `prepare` was run on the file system.  This command removes all realm-secured files and directories from the realms and then destroys all Oracle ACFS security rules, rule sets and realms from the file system. However, the `.Security` directory and its contents, including log files and the security metadata backup files, are not deleted.  If you want to remove encryption and security is being used, then this command must be run before encryption is backed out. To back out encryption, refer to " acfsutil encr set ". |

The `acfsutil` `sec` `prepare` command must be run before any of the realm management commands. This command prepares the specified Oracle ACFS file system for security and by default turns security on for the file system.

When running `acfsutil` `sec` `prepare` `-u`, ensure that no other Oracle ACFS security commands are run until `acfsutil` `sec` `prepare` has completed.

If auditing is initialized on a cluster, this command also enables an Oracle ACFS security auditing source on the file system. The actions performed when enabling this audit source are the same as those done when the `acfsutil` `audit` `enable` command is run directly. For more information, refer to " acfsutil audit enable ".

This command creates the `/` *mount\_point* `/.Security`, `/` *mount\_point* `/.Security/backup`, and `/` *mount\_point* `/.Security/realm/logs` directories where *mount\_point* is the option specified in the command line.

This command creates the following system security realms:

- `SYSTEM_Logs`
	This is a system-created realm to protect the Oracle ACFS security log files in the directory `.Security/realm/logs/` directory.
- `SYSTEM_Audit`
	This is a system-created realm to protect audit trail files. This realm is created if auditing has been initialized. If auditing has not been initialized, it is created when auditing is enabled for the security source through the `acfsutil` `audit` `enable` command. This realm secures the audit trail file so that the audit manager can read and write and the auditor can read the file, and no one else has access. This realm also protects the audit trail file so the audit manager cannot delete (without running the `acfsutil` `audit` `purge` command), truncate, overwrite, or chmod the file.
- `SYSTEM_SecurityMetadata`
	This is a system-created realm to protect the Oracle ACFS metadata XML file in the directory `.Security/backup/` directory.
- `SYSTEM_Antivirus`
	This is a system-created realm that allows access for the antivirus software that is running on an Oracle ACFS file system. For every realm protected file or directory, the `SYSTEM_Antivirus` realm is evaluated when authorization checks are performed to determine if the `SYSTEM_Antivirus` realm allows access to the file or directory.
	To allow the antivirus process to access realm-protected files or directories, you must add the `LocalSystem` or `SYSTEM` group to the realm with the `acfsutil` `sec` `realm` `add` command, as shown in the realm-add command example in this section. If other antivirus processes are running as `Administrator`, then the user `Administrator` must be added to the `SYSTEM_Antivirus` realm to allow access to realm protected files and directories.
	If no Antivirus products have been installed, do not add any users or groups to the `SYSTEM_Antivirus` realm. Because users or groups added to the `SYSTEM_Antivirus` realm have `READ` and `READDIR` access, limit the users or groups added to this realm. You can restrict the time window when the users or groups of this realm can access the realm protected files or directories with time-based rules. You can also have application-based rules if you can identify the process name for the antivirus installation that scans the files.
	The `SYSTEM_Antivirus` realm can only perform the following operations on a file or directory: `OPEN`, `READ`, `READDIR`, and setting time attributes. To remove or delete files or directories, you may need to disable security to clean up the infected files.
	This realm is set up only for Windows systems.
- `SYSTEM_BackupOperators`
	This is a system-created realm that enables you to authorize users that can back up realm-secured files and directories. You can add users, groups, rule sets, and command rules to this realm to provide fine-grain authorization for backing up realm-secured files and directories. A user must be added to this realm to back up realm-secured files and directories.
	Use caution when adding groups to this system realm. After you add a group to this system realm, all the users of the added group are able to override the realm protections to access files.

To access files in the system security realms, the user should be assigned as a security administrator with the `acfsutil` `sec` `admin` `add` command.

You can add users, groups, rule sets, and command rules to system-created realms with the `acfsutil` `sec` `realm` `add` command, the same as for user-created realms. However, adding files and directories to system realms is not recommended. You can use the `acfsutil` `sec` `realm` `delete` command to delete objects from the system-created realms.

System-created security realms cannot be removed by a security administrator with the `acfsutil` `sec` `admin` `destroy` command. These realms are only removed when security is backed out of a file system when executing the `acfsutil` `sec` `prepare` command with the `-u` option.

The `acfsutil` `sec` `prepare` `-u` command is not allowed if any snapshots exist in the file system.

Only a security administrator can run the `acfsutil` `sec` `prepare` command.

Examples

The following example shows the use of the `acfsutil` `sec` `prepare` command.

Example: Using the acfsutil sec prepare command

```
$ /sbin/acfsutil sec prepare -m /acfsmounts/acfs1
```

### acfsutil sec realm add

Purpose

Adds objects to an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm add -h
acfsutil sec realm add realm -m mount_point
   {[-u user, ...] [-G os_group,...]
    [-l commandrule:ruleset,commandrule:ruleset, ...]
    [-e [-a {AES}] [-k {128|192|256}]]
    [-f [ -r] path ...]}
```

`acfsutil` `sec` `realm` `add` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `add` command.

Table: Options for the acfsutil sec realm add command

| Option | Description |
| --- | --- |
| `realm` | Specifies the realm name to add. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-u` `user` | Specifies user names to add. |
| `-G` `os_group` | Specifies the operating system groups to add. |
| `-l` `commandrule`: `ruleset` | Specifies the filters to add. The *commandrule* switch is used to add one or more command rules to the realm with a rule set.  *ruleset* specifies the rule set associated with the command rule for this realm. Only one rule set can be included with each command rule.  For a list of command rules, refer to the Security Realm Command Rules table. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option. Refer to " acfsutil sec info ". |
| `-e` | Enables encryption on the realm. Turning encryption on for the realm causes all files contained in the realm to be encrypted. These files remain encrypted until they are no longer part of an encrypted realm.  Files that are encrypted are not re-encrypted to match the new specified encryption parameters. |
| `-a` { `AES` } | Specifies the encryption algorithm for the realm. |
| `-k` { `128` \| `192` \| `256` } | Specifies the encryption key length. |
| `-f` \[ `-r` \] `path` `...` | Adds files specified by *path* to the realm. `-r` specifies a recursive operation. File paths must be separated by spaces and must be placed at the end of the command.  If a specified file is not realm secured, the file is encrypted or decrypted to match the encryption status for the realm. |

The `acfsutil` `sec` `realm` `add` command adds objects to the specified realm. The objects to be added include users, groups, command rules, rule sets, and files. If the command encounters an error when adding an object, a message is displayed and the command continues processing the remaining objects.

Multiple entries can be added in a comma-delimited list when adding users, operating system groups, or command rules. Do not use spaces in the comma-delimited list. If spaces are added, then enclose the list in quotes.

If the `-e` option is specified, then encryption must have been initialized for the cluster and set on the file system. For more information, refer to " acfsutil encr init " and " acfsutil encr set ".

If the entire mount point, which includes the `.Security` directory, is added to the realm then the security administrator operating system group should be added to the realm to maintain security logging and backing up operations.

The supported command are rules listed in the following table. These command rules restrict or protect against file system operations on realm-secured files and directories.

Table: Security Realm Command Rules

| Rule | Description |
| --- | --- |
| `ALL` | Protects against all file system operations on files and directories. |
| `APPENDFILE` | Restricts against additions to the end of a file. Restrictions include writes that start within the current file size, but proceed beyond the end of the file. |
| `CHGRP` | Protects from changing the group ownership on a file or directory. |
| `CHMOD` | Protects from changing the permissions on a file or directory. |
| `CHOWN` | Protects from changing the owner information of a file or directory. |
| `CREATEFILE` | Protects from creation of new file in a directory. |
| `DELETEFILE` | Protects from deletion of a file from a directory. |
| `EXTEND` | Restricts the extension operation of a file size. A file size may still be modifiable with other operations. `EXTEND` does not protect against a `truncate` followed by an `append` operation. |
| `IMMUTABLE` | Denies any changes to the files and directories in the realm except changes to extended attributes resulting from commands such as `acfsutil` `tag` and `acfsutil` `encr`.  Includes the following protection for a file or directory: `APPENDFILE`, `CHGRP`, `CHMOD`, `CHOWN`, `DELETEFILE`, `EXTEND`, `OVERWRITE`, `RENAME`, `RMDIR`, `TRUNCATE`, and `WRITE`.  `IMMUTABLE` does not deny any changes to the `atime` attribute. The `atime` attribute changes when a user accesses the file.  Can be set to archive the files and directories in a security realm. |
| `LINKFILE` | Restricts the creation of hard links to files. |
| `MKDIR` | Protects from the creation of new directory in a directory. |
| `MMAPREAD` | Protects a file from being memory mapped for a read operation using `mmap()` on Linux or using `CreateFileMapping` followed by `MapViewOfFile()` on Windows. |
| `MMAPWRITE` | Protects a file from being memory mapped for a write operation. Setting `MMAPWRITE` also protects a file from mapping for read as the operating system maps a file for both read and write. |
| `OPENFILE` | Protects from the opening of a file. |
| `OVERWRITE` | Prevents existing content in a file from being overwritten with a `write` operation whose start and end offsets are within the current file size.  If the operations on a file are `truncate` followed by `append`, `OVERWRITE` does not protect the file. To provide additional protection from both `append` and `overwrite` operations, use the `WRITE` command rule. |
| `READDIR` | Restricts for a directory listing, except for use by the security administrator group. |
| `READ` | Protects from reading the contents of a file. `READ` also protects against `read` operations using `mmap(2)`. |
| `RENAME` | Protects against renaming a file or directory. |
| `RMDIR` | Protects against removing a directory. |
| `SYMLINK` | Restricts the creation of symbolic links in the directories protected by a security realm. When creating symbolic links, it does not matter whether the source file is protected by a security realm. |
| `TRUNCATE` | Restricts the truncation of a file. |
| `WRITE` | Protects a file against the `write` system call. `WRITE` also protects against `append` and `overwrite` operations, plus `write` operations using `mmap(2)`.  A file may still be modifiable with other file operations. To protect the file from other modifications, also use the `TRUNCATE` and `DELETEFILE` command rules. |

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `add` command. The first `acfsutil` `sec` command adds a user group to a security realm. The second and third commands add the `LocalSystem` or `SYSTEM` group to the `SYSTEM_Antivirus` realm in a Windows environment.

Example: Using the acfsutil sec realm add command

```
$ /sbin/acfsutil sec realm add my_security_realm -m /acfsmounts/acfs1
     -G my_os_group

C:\> acfsutil sec realm add SYSTEM_Antivirus /m e: /G "NT AUTHORITY\\SYSTEM"

C:\> acfsutil sec realm add SYSTEM_Antivirus /m e: /G "SYSTEM"
```

### acfsutil sec realm audit disable

Purpose

Disables auditing of a specific command rule or all command rules for files in an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm audit disable -h
acfsutil sec realm audit disable realm -m mount_point
  [-l commandrule,commandrule,...] {-a |-v }
```

`acfsutil` `sec` `realm` `audit` `disable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `audit` `disable` command.

Table: Options for the acfsutil sec realm audit disable command

| Option | Description |
| --- | --- |
| `realm` | Specifies the security realm name. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-l` `commandrule` | Specifies the command rules on which to disable auditing.  If this option is not specified, then the list of all command rules is the default.  For a list of command rules, refer to the Security Realm Command Rules table. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option. Refer to " acfsutil sec info ". |
| `-a` \| `-v` | Specifies to disable audit realm authorizations ( `-a` ) or disable audit realm violations ( `-v` ). Either `-a` or `-v` must be specified. |

Multiple entries can be added in a comma-delimited list when listing command rules. Do not use spaces in the comma-delimited list. If spaces are added, then enclose the list in quotes.

Only a security administrator can run this command. This command is authenticated using the Oracle ACFS security administrator password.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `audit` `disable` command. This command disables auditing on the `OPEN` (all violations) and `WRITE` (all violations) command rules.

Example: Using the acfsutil sec realm audit disable command

```
$ /sbin/acfsutil sec realm audit disable mySecureRealm
    -m /acfsmounts/acfs1 -l OPEN,WRITE -v
```

### acfsutil sec realm audit enable

Purpose

Enables auditing of a specific command rule or all command rules for files in an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm audit enable -h
acfsutil sec realm audit enable realm -m mount_point
  [-l commandrule,commandrule,...]
  [-a ] [-v [ -u] ]
```

`acfsutil` `sec` `realm` `audit` `enable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `audit` `enable` command.

Table: Options for the acfsutil sec realm audit enable command

| Option | Description |
| --- | --- |
| `realm` | Specifies the security realm name. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-l` `commandrule` | Specifies the command rules on which to enable auditing.  If this option is not specified, then the list of all command rules is the default.  For a list of command rules, refer to the Security Realm Command Rules table. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option. Refer to " acfsutil sec info ". |
| `-a` | Specifies to audit realm authorizations. |
| `-v` \[ `-u` \] | Specifies to audit realm violations. If `-u` is also specified, only realm violations by users who are members of a realm are audited. |

If the `acfsutil` `sec` `realm` `audit` `enable` command is run multiple times, then the earlier configuration is not negated and the new settings are also applied. An exception to this behavior occurs when the command is run with the `-v` option and the specified command rule has auditing set for realm violations. In this case, the behavior is updated according to whether the `-u` flag was specified. For more information, see the example in this section.

Multiple entries can be added in a comma-delimited list when listing command rules. Do not use spaces in the comma-delimited list. If spaces are added, then enclose the list in quotes.

If neither `-a` or `-v` are specified with the `acfsutil` `sec` `realm` `audit` `enable` command, the default is `-v`. Both `-a` and `-v` can be specified.

Only a security administrator can run this command. This command is authenticated using the Oracle ACFS security administrator password.

Examples

The following example shows how to enable auditing of the Oracle ACFS backup operators. Because these users are allowed access to files through the `SYSTEM_Backup` realm and are granted special privileges that give them access to all files on the file system, a security administrator may want to audit their actions. After the command is executed, any time a member of the `SYSTEM_Backup` realm opens a file an audit record is written to the Oracle ACFS Security audit trail on the file system.

Example: Auditing Oracle ACFS security backup operators

```
$ /sbin/acfsutil sec realm audit enable SYSTEM_Backup
    -m /acfsmounts/acfs1 -l OPEN -a
```

The following example shows how to use the `-u` option to audit realm violations by users who are part of the realm. In this scenario sensitive human resources information is stored in `HumanResources` security realm and the `hr` group is allowed to access this information. However, a ruleset applied to the `ALL` command rule prevents access to this data from 6 PM to 8 AM. With this command, the security administrator could discover if any human resource employees are attempting to access sensitive data outside of the allowed time period. After this command is executed, only access violations by users who are members of the `hr` group are audited.

Example: Auditing only security realm users

```
$ /sbin/acfsutil sec realm audit enable HumanResources
    -m /acfsmounts/acfs1 -l ALL -v -u
```

The following example shows multiple runs of the `acfsutil` `sec` `realm` `audit` `enable` command. After run 1, the `OPEN` (all violations) and `WRITE` (all violations) command rules are audited. After run 2, the `OPEN` (all violations), `WRITE` (all violations), and `DELETEFILE` (authorizations) command rules are audited. After run 3, the `OPEN` (authorizations and realm user violations), `WRITE` (all violations), `DELETEFILE` (authorizations), and `TRUNCATE` (authorizations and realm user violations) command rules are audited. After run 4, all violations are audited on all command rules. In addition, authorizations are audited for `OPEN`, `DELETEFILE`, and `TRUNCATE`.

Example: Running acfsutil sec realm audit enable multiple times

```
$ echo run 1
$ /sbin/acfsutil sec realm audit enable mySecureRealm
    -m /acfsmounts/acfs1 -l OPEN,WRITE -v

$ echo run 2
$ /sbin/acfsutil sec realm audit enable mySecureRealm
    -m /acfsmounts/acfs1 -l DELETEFILE -a

$ echo run 3
$ /sbin/acfsutil sec realm audit enable mySecureRealm
    -m /acfsmounts/acfs1 -l OPEN,TRUNCATE -a -v -u

$ echo run 4
$ /sbin/acfsutil sec realm audit enable mySecureRealm
    -m /acfsmounts/acfs1 -v
```

### acfsutil sec realm audit info

Purpose

Displays the realm auditing information for a specified Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm audit info -h
acfsutil sec realm audit info -m mount_point -n realm
```

`acfsutil` `sec` `realm` `audit` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `audit` `info` command.

Table: Options for the acfsutil sec realm audit info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-n` `realm` | Specifies the security realm name. |

The `acfsutil` `sec` `realm` `audit` `info` command provides information about a specified Oracle ACFS security realm.

Examples

The following example shows an example of the `acfsutil` `sec` `realm` `audit` `info` command.

Example: Running acfsutil sec realm audit info

```
$ /sbin/acfsutil sec realm audit info -m /acfsmounts/acfs1
    -n mySecureRealm

Command rule auditing information for realm 'mySecureRealm'
   on mount point '/acfsmounts/acfs1':

Realm authorization            :    'READ, WRITE'
Realm violation for all users  :    'READ, OPENFILE'
Realm violation for realm users:    'None'
```

### acfsutil sec realm clone

Purpose

Clones an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm clone -h
acfsutil sec realm clone realm -s src_mount_point new_realm
  [-e] [-f] [-G] [-l] [-u]
acfsutil sec realm clone realm -s src_mount_point
  [new_realm] -d destination_mount_point
  [-e] [-G] [-l] [-u]
```

`acfsutil` `sec` `realm` `clone` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `clone` command.

Table: Options for the acfsutil sec realm clone command

| Option | Description |
| --- | --- |
| `realm` | Specifies the realm name to be cloned. |
| `-s` `src_mount_point` | Specifies the directory where the source file system is mounted. |
| `new_realm` | Specifies the new realm name. |
| `-d` `destination_mount_point` | Specifies the directory for the destination mount point for the new realm. |
| `-e` | Copy encryption attributes to the new realm. |
| `-f` | Copy file objects to the new realm. |
| `-G` | Copy operating system groups to the new realm. |
| `-l` | Copy filters to the new realm. |
| `-u` | Copy users to the new realm. |

The `acfsutil` `sec` `realm` `clone` makes a copy of the specified realm in the destination mount point. If the source and mount points are different and the new realm name is not specified, then the realm is cloned using the existing realm name in the Oracle ACFS file system specified by destination mount point. If the destination mount point is not specified, then the cloned realm is located in the source mount point and a new unique realm name must be specified.

If the `-l` option is specified and the destination mount point is different than the source mount point, then the rules and rule sets must be cloned first.

If the `-e` option is specified and the destination mount point is different than the source mount point, then encryption must be set on destination mount point. For more information, refer to " acfsutil encr set ".

The `-f` option can only be used if the destination mount point is the same as the source mount point.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `clone` command.

Example: Using the acfsutil sec realm clone command

```
$ /sbin/acfsutil sec realm clone my_security_realm -s /acfsmounts/acfs1
      my_new_security_realm -d /acfsmounts/acfs2 -G
```

### acfsutil sec realm create

Purpose

Creates an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm create -h
acfsutil sec realm create realm -m mount_point
  -e { on -a {AES}  -k {128|192|256} | off }
  [-o {enable|disable}] [-d "description"]
```

`acfsutil` `sec` `realm` `create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `create` command.

Table: Options for the acfsutil sec realm create command

| Option | Description |
| --- | --- |
| `realm` | Specifies the realm name. |
| `-m` `mount_point` | Specifies the mount point for the file system. A mount point is specified as a path on Linux platforms. |
| `-e` { `on` \| `off` } | Specifies encryption on or off for the realm. |
| `-a` { `AES` } | Specifies the encryption algorithm. |
| `-k` { `128` \| `192` \| `256` } | Specifies the encryption key length. |
| `-o` { `enable` \| `disable` } | Specifies where security is on or off for the realm. |
| `-d` `"` `description` `"` | Specifies a realm description. |

The `acfsutil` `sec` `create` `realm` creates a new realm in the specified Oracle ACFS file system. The new realm name must be unique in the file system identified by the mount point.

A maximum of 500 Oracle ACFS security realms can be created, including any default system realms created by the `acfsutil` `sec` `prepare` command.

The realm is enabled by default unless the `-o` `disable` option is specified.

If the `-e` `on` option is specified, then encryption must have been initialized for the cluster and set on the file system. For more information, refer to " acfsutil encr init " and " acfsutil encr set ".

If the `-e` `off` option is specified, you cannot specify the `-a` and `-k` options.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `create` command.

Example: Using the acfsutil sec realm create command

```
$ /sbin/acfsutil sec realm create my_security_realm -m /acfsmounts/acfs1
     -e on -a AES -k 192 -o enable
```

### acfsutil sec realm delete

Purpose

Deletes objects from an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm delete -h
acfsutil sec realm delete realm -m mount_point
  {[-u user, ...] [-G os_group, ...]
  [-l :ruleset,commandrule:ruleset, ...]
  [-f [ -r] path, ...] ] [-e ]}
```

`acfsutil` `sec` `realm` `delete` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `delete` command.

Table: Options for the acfsutil sec realm delete command

| Option | Description |
| --- | --- |
| `realm` | Specifies the realm name. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-u` `user` | Specifies user names to delete. |
| `-G` `os_group` | Specifies the operating system groups to delete. |
| `-l` `commandrule`: `ruleset` | Specifies the filters to delete from the realm. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option. `ruleset` specifies the rule set associated with the command rule for this realm. |
| `-f` \[ `-r` \] `path` `...` | Deletes files specified by *path* from the realm. `-r` specifies a recursive operation. File paths must be separated by spaces.  If this is the last realm securing the file, the file is encrypted or decrypted to match the file system level encryption state. |
| `-e` | Disables encryption on the realm.  When disabling encryption, this option decrypts any files in the realm that do not belong to any other encrypted realms. If a file is part of another realm which is encrypted or if encryption is turned on for the file system, then the file remains encrypted. |

The `acfsutil` `sec` `realm` `delete` command removes objects from the specified realm. The objects to be deleted include users, groups, rule sets, and files. If the command encounters an error when deleting an object, a message is displayed and the command continues processing the remaining objects.

Multiple entries can be added in a comma-delimited list when adding users, operating system groups, or command rules. Do not use spaces in the comma-delimited list. If spaces are added, then enclose the list in quotes.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `delete` command.

Example: Using the acfsutil sec realm delete command

```
$ /sbin/acfsutil sec realm delete my_security_realm -m /acfsmounts/acfs1
     -f -r /acfsmounts/acfs1/myoldfiles/*.log
```

### acfsutil sec realm destroy

Purpose

Destroys an Oracle ACFS security realm.

Syntax and Description

```
acfsutil sec realm destroy -h
acfsutil sec realm destroy realm -m mount_point
```

`acfsutil` `sec` `realm` `destroy` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `realm` `destroy` command.

Table: Options for the acfsutil sec realm destroy command

| Option | Description |
| --- | --- |
| `realm` | Specifies the realm name. |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `sec` `destroy` `realm` removes a security realm from the specified Oracle ACFS file system. Destroying the realm does not destroy the objects in the realm; this command simply removes the security associated with the realm from the objects.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `realm` `destroy` command.

Example: Using the acfsutil sec realm destroy command

```
$ /sbin/acfsutil sec realm destroy my_security_realm -m /acfsmounts/acfs1
```

### acfsutil sec rule clone

Purpose

Clones a security rule.

Syntax and Description

```
acfsutil sec rule clone -h
acfsutil sec rule clone rule -s src_mount_point new_rule
acfsutil sec rule clone rule -s src_mount_point
  [new_rule] -d mount_point
```

`acfsutil` `sec` `rule` `clone` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `rule` `clone` command.

Table: Options for the acfsutil sec rule clone command

| Option | Description |
| --- | --- |
| `rule` | Specifies the existing name of the rule. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-s` `src_mount_point` | Specifies the directory where the source file system is mounted. |
| `-d` `mount_point` | Specifies the directory for the destination mount point of the file system. |
| `new_rule` | Specifies the new name of the rule. If the name contains a space, enclose in quotes ( `"` `"` ). |

If the source and mount points are different and the new rule name is not specified, then the rule is cloned using the existing rule name in the Oracle ACFS file system specified by destination mount point. If the destination mount point is not specified, then the cloned rule is located in the source mount point and a new unique rule name must be specified.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `rule` `clone` command.

Example: Using the acfsutil sec rule clone command

```
$ /sbin/acfsutil sec rule clone my_security_rule -s /acfsmounts/acfs1
      my_new_security_rule -d /acfsmounts/acfs2
```

### acfsutil sec rule create

Purpose

Creates a security rule.

Syntax and Description

```
acfsutil sec rule create -h
acfsutil sec rule create rule -m mount_point
  -t rule_type rule_value
  [-o {ALLOW|DENY}]
```

`acfsutil` `sec` `rule` `create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `rule` `create` command.

Table: Options for the acfsutil sec rule create command

| Option | Description |
| --- | --- |
| `rule` | Specifies the name of the rule. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-t` `rule_type` `rule_value` | Specifies a rule type and a rule value. The rule type can be `application`, `hostname`, `time`, or `username`. The rule value depends on the type of rule. The valid rule types and values are described in this section. |
| `-o` `option` | Specifies options preceded by `-o`. The option specified can be `ALLOW` or `DENY`. The default value is `DENY`. |

The `acfsutil` `sec` `rule` `create` command creates a new rule in the Oracle ACFS file system specified by the mount point. The new rule can be added to a rule set and that rule set can be added to a security realm.

A maximum of 500 Oracle ACFS security rules can be created.

The rule types and associated rule values are:

- `application`
	This rule type specifies the name of an application which is allowed or denied access to the objects protected by a realm.
- `hostname`
	This rule type specifies the name of a computer from which a user accesses the objects protected by a realm. Access from a node can be allowed or denied using this rule. The `hostname` should be one of the cluster node names and not any other external nodes which could have mounted the Oracle ACFS file system as a network File System (NFS) mount.
- `time`
	This rule type specifies the time interval in the form *start\_time*,*end\_time*. This time interval specifies access to a realm. Access can be allowed or denied to objects protected by a realm only during certain times of the day by setting this rule in a realm. The time is based on the local time of the host.
- `username`
	This rule type specifies the name of a user to be added or deleted from a realm. You can use this option to deny access for any user that belongs to a security group that is part of a realm.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `rule` `create` command.

Example: Using the acfsutil sec rule create command

```
$ /sbin/acfsutil sec rule create my_security_rule -m /acfsmounts/acfs1
      -t username security_user_one -o ALLOW
```

### acfsutil sec rule destroy

Purpose

Removes a security rule.

Syntax and Description

```
acfsutil sec rule destroy -h
acfsutil sec rule destroy rule -m mount_point
```

`acfsutil` `sec` `rule` `destroy` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `rule` `destroy` command.

Table: Options for the acfsutil sec rule destroy command

| Option | Description |
| --- | --- |
| `rule` | Specifies the name of the rule. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `sec` `rule` `destroy` command removes a rule from the rule sets in the Oracle ACFS file system specified by the mount point. A rule set is not destroyed if all the rules are destroyed. The empty rule set must be explicitly destroyed.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `rule` `destroy` command.

Example: Using the acfsutil sec rule destroy command

```
$ /sbin/acfsutil sec rule destroy my_security_rule -m /acfsmounts/acfs1
```

### acfsutil sec rule edit

Purpose

Updates a security rule.

Syntax and Description

```
acfsutil sec rule edit -h
acfsutil sec rule edit rule -m mount_point
  { [-t rule_type rule_value ] [-o {ALLOW|DENY}] }
```

`acfsutil` `sec` `rule` `edit` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `rule` `edit` command.

Table: Options for the acfsutil sec rule edit command

| Option | Description |
| --- | --- |
| `rule` | Specifies the name of the rule. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-t` `rule_type` `rule_value` | Specifies a rule type and a rule value. The rule type can be `application`, `hostname`, `time`, or `username`. Rule value depends on the type of rule. For information on the rule type and rule value, refer to " acfsutil sec rule create ". |
| `-o` `option` | Specifies options preceded by `-o`. The option specified can be `ALLOW` or `DENY`. |

The `acfsutil` `sec` `rule` `edit` updates a rule. The value that is associated with a rule can be updated, but not the rule type.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `rule` `edit` command to update `my_security_rule`. The existing rule is of type `username` and that value cannot be changed.

Example: Using the acfsutil sec rule edit command

```
$ /sbin/acfsutil sec rule edit my_security_rule -m /acfsmounts/acfs1
      -t username security_user_three -o ALLOW
```

### acfsutil sec ruleset clone

Purpose

Clones a security rule set.

Syntax and Description

```
acfsutil sec ruleset clone -h
acfsutil sec ruleset clone ruleset -s mount_point  new_ruleset
acfsutil sec ruleset clone ruleset -s mount_point
  [new_ruleset] -d mount_point
```

`acfsutil` `sec` `ruleset` `clone` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `ruleset` `clone` command.

Table: Options for the acfsutil sec ruleset clone command

| Option | Description |
| --- | --- |
| `rule_set` | Specifies the existing name of the rule set. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-s` `mount_point` | Specifies the directory where the source file system is mounted. |
| `-d` `mount_point` | Specifies the directory for the destination mount point of the file system. |
| `new_rule_set` | Specifies the new name of the rule set. If the name contains a space, enclose in quotes ( `"` `"` ). |

If the source mount point is different from destination mount point, the rules in the rule set must be cloned first.

If the source and mount points are different and the new rule set name is not specified, then the rule set is cloned using the existing rule set name in the Oracle ACFS file system specified by destination mount point. If the destination mount point is not specified, then the cloned rule set is located in the source mount point and a new unique rule set name must be specified.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `ruleset` `clone` command.

Example: Using the acfsutil sec ruleset clone command

```
$ /sbin/acfsutil sec ruleset clone
      my_security_ruleset -s /acfsmounts/acfs1
      my_new_security_ruleset -d /acfsmounts/acfs2
```

### acfsutil sec ruleset create

Purpose

Creates a security rule set.

Syntax and Description

```
acfsutil sec ruleset create -h
acfsutil sec ruleset create rule_set -m mount_point
  [-o {ALL_TRUE|ANY_TRUE}]
```

`acfsutil` `sec` `ruleset` `create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `ruleset` `create` command.

Table: Options for the acfsutil sec ruleset create command

| Option | Description |
| --- | --- |
| `rule_set` | Specifies the name of the rule set. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-o` `option` | Specifies options preceded by `-o`. The option specified can be `ALL_TRUE` or `ANY_TRUE`. The default value is `ALL_TRUE`. |

The `acfsutil` `sec` `ruleset` `create` command creates a new rule set in the specified mount point.

A maximum of 500 Oracle ACFS security rule sets can be created.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `ruleset` `create` command.

Example: Using the acfsutil sec ruleset create command

```
$ /sbin/acfsutil sec ruleset create
       my_security_ruleset -m /acfsmounts/acfs1 -o ANY_TRUE
```

### acfsutil sec ruleset destroy

Purpose

Removes a security rule set.

Syntax and Description

```
acfsutil sec ruleset destroy -h
acfsutil sec ruleset destroy rule_set -m mount_point
```

`acfsutil` `sec` `ruleset` `destroy` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `ruleset` `destroy` command.

Table: Options for the acfsutil sec ruleset destroy command

| Option | Description |
| --- | --- |
| `rule_set` | Specifies the name of the rule set. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `sec` `ruleset` `destroy` command removes a rule set from the Oracle ACFS file system specified by the mount point. Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `ruleset` `destroy` command.

Example: Using the acfsutil sec ruleset destroy command

```
$ /sbin/acfsutil sec ruleset destroy
       my_security_ruleset -m /acfsmounts/acfs1
```

### acfsutil sec ruleset edit

Purpose

Updates a security rule set.

Syntax and Description

```
acfsutil sec ruleset edit -h
acfsutil sec ruleset edit rule_set -m mount_point
    { [-a rule,...] [-d rule,...] [-o {ALL_TRUE|ANY_TRUE}]}
```

`acfsutil` `sec` `ruleset` `edit` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `ruleset` `edit` command.

Table: Options for the acfsutil sec ruleset edit command

| Option | Description |
| --- | --- |
| `rule_set` | Specifies the name of the rule set. If the name contains a space, enclose in quotes ( `"` `"` ). |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-a` `rule` | Specifies the rule to add. |
| `-d` `rule` | Specifies the rule to remove. |
| `-o` `option` | Specifies options preceded by `-o`. The option specified can be `ALL_TRUE` or `ANY_TRUE`. |

The `acfsutil` `sec` `ruleset` `edit` command updates a rule set in the Oracle ACFS file system specified by the mount point.

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `ruleset` `edit` command.

Example: Using the acfsutil sec ruleset edit command

```
$ /sbin/acfsutil sec ruleset edit
       my_security_ruleset -m /acfsmounts/acfs1
       -a my_new_rule -o ANY_TRUE
```

### acfsutil sec save

Purpose

Saves Oracle ACFS file system security metadata.

Syntax and Description

```
acfsutil sec save -h
acfsutil sec save -m mount_point -p file
```

`acfsutil` `sec` `save` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `sec` `save` command.

Table: Options for the acfsutil sec save command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-p` `file` | Specifies a file name to store the security metadata. The file is saved in the `/` `mount_point` `/.Security/backup/` directory. |

The `acfsutil` `sec` `save` command saves the security metadata for an Oracle ACFS file system to an XML file. By default, the file is saved in the `/` *mount\_point* `/.Security/backup` directory.

This file can be backed up as a regular file by a backup application. System realms protect this file and allow only members of these realms to access this file and prevent all other users including the root user and system administrator from access. For information about the system-created security realms, refer to " acfsutil sec prepare ".

Only a security administrator can run this command.

Examples

The following example shows the use of the `acfsutil` `sec` `save` command.

Example: Using the acfsutil sec save command

```
$ /sbin/acfsutil sec save -m /acfsmounts/acfs1 -p my_metadata_file.xml
```

## Oracle ACFS Command-Line Tools for Encryption

This topic provides a summary of the commands for Oracle ACFS encryption.

The Oracle ACFS encryption command summary lists the Oracle ACFS encryption commands with brief descriptions. For an overview of Oracle ACFS encryption, refer to [Oracle ACFS Encryption](introducing-oracle-acfs-and-oracle-advm.md).

For information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of commands for Oracle ACFS encryption

| Command | Description |
| --- | --- |
| acfsutil encr info | Displays encryption-related information about Oracle ACFS file systems. |
| acfsutil encr init | Creates storage for encryption keys. |
| acfsutil encr off | Disables encryption for an Oracle ACFS file system. |
| acfsutil encr on | Encrypts an Oracle ACFS file system. |
| acfsutil encr rekey | Generates a new key and re-encrypts an Oracle ACFS file system. |
| acfsutil encr set | Sets or changes encryption parameters for an Oracle ACFS file system. |
| acfsutil keystore migrate | Migrates the encryption keystore. |

### acfsutil encr info

Purpose

Displays encryption-related information about Oracle ACFS file systems, directories, or files.

Syntax and Description

```
acfsutil encr info -h
acfsutil encr info -m mount_point [[-r] path [path ...]]
```

`acfsutil` `encr` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `info` command.

Table: Options for the acfsutil encr info command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies recursive action under an existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

If `-m` is specified without a *path*, the encryption status, algorithm, and key length are displayed for the file system level.

If `-r` is specified with a *path*, the encryption status, algorithm, and key length are displayed for all objects under the directory specified by *path*.

The `acfsutil` `encr` `info` command displays encryption status and parameters for files in a snapshot if the files are specified with the *path* option.

This command fails when it is run on realm-secured objects.

Any user can run this command to display encryption information about a file system, directory, or file.

If the `acfsutil` `encr` `info` command is run as a system administrator, then the output displays the types of keystore used. The types are single-sign-on wallet in the OCR (SSO), password-protected wallet in the OCR (PKS), and Oracle Key Vault as the key store (OKV).

Examples

The following are examples of the use of `acfsutil` `encr` `info`.

Example: Using the acfsutil encr info command

```
# /sbin/acfsutil encr info -m /acfsmounts/acfs1

# /sbin/acfsutil encr info -m /acfsmounts/acfs1
                           -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr init

Purpose

Creates storage for encryption keys.

Syntax and Description

```
acfsutil encr init -h
acfsutil encr init [-p ]
```

`acfsutil` `encr` `init` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `init` command.

Table: Options for the acfsutil encr init command

| Option | Description |
| --- | --- |
| `-p` | Creates PKCS (password-protected) storage for keys. |

The `acfsutil` `encr` `init` command must be run before any other encryption `acfsutil` commands can be run. This command must be run once for each cluster on which Oracle ACFS encryption is run.

If you plan to use Oracle Key Vault as the key store, then you still must run `acfsutil` `encr` `init` first.

If the `-p` option is specified, you must provide a password when prompted. The password must conform to the format that is described in " acfsutil sec init ".

If the `-p` option is not specified, a single sign-on (SSO) wallet is created.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `encr` `init`.

Example: Using the acfsutil encr init command

```
# /sbin/acfsutil encr init
```

### acfsutil encr off

Purpose

Disables encryption for an Oracle ACFS file system, directories, or individual files.

Syntax and Description

```
acfsutil encr off -h
acfsutil encr off -m mount_point [[-r] path [ path ...]]
```

`acfsutil` `encr` `off` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `off` command.

Table: Options for the acfsutil encr off command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-r` | Specifies to disable encryption recursively under an existing directory identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a *path* specified). When the `-m` option is specified without a *path*, all the files under the mount point are decrypted.

The *path* option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a decryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

Only a user with root or system administrator privileges can run this command to disable encryption on a file system. The file owner can also run this command to disable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `off`.

Example: Using the acfsutil encr off command

```
# /sbin/acfsutil encr off -m /acfsmounts/acfs1

# /sbin/acfsutil encr off -m /acfsmounts/acfs1
                          -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr on

Purpose

Encrypts an Oracle ACFS file system, directories, or individual files.

Syntax and Description

```
acfsutil encr on -h
acfsutil encr on -m mount_point
  [-a {AES} -k {128|192|256}] [[-r] path [path...]]
```

`acfsutil` `encr` `on` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `on` command.

Table: Options for the acfsutil encr on command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-a` `algorithm` | Specifies the encryption algorithm type for a directory or file. Advanced Encryption Standard (AES) is the only encryption algorithm supported for this release. |
| `-k` `key_length` | Specifies the encryption key length for a directory or file. |
| `-r` | Specifies encryption recursively under existing directory folder identified by `path`. |
| `path` | Specifies the absolute or relative path of a directory. Multiple path values are allowed. |

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run. To set the key length at the volume level, use the `acfsutil` `encr` `set` command.

Only an administrator can run this command on an Oracle ACFS file system (`-m` option without a *path* specified). When the `-m` option is specified without a *path*, all the files under the mount point are encrypted.

The *path* option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If an encryption operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

When you run `acfsutil` `encr` `on` with the `-r` option, the command encrypts the specified directory recursively, but does not enable encryption on the file system level.

Only a user with root or system administrator privileges can run this command to enable encryption on a file system. The file owner can also run this command to enable encryption on a directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `on`.

Example: Using the acfsutil encr on command

```
# /sbin/acfsutil encr on -m /acfsmounts/acfs1

# /sbin/acfsutil encr on -m /acfsmounts/acfs1
                         -a AES -k 128 -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr rekey

Purpose

Generates a new key and re-encrypts volume or file.

Syntax and Description

```
acfsutil encr rekey -h
acfsutil encr rekey -m mount_point
    {-f [-r] path [path...] |-v } [-a {AES} -k {128|192 |256}]
```

`acfsutil` `encr` `rekey` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `rekey` command.

Table: Options for the acfsutil encr rekey command

| Option | Description |
| --- | --- |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |
| `-f` \[ `-r` \] `path`... | Generates a new file encryption key for the specified path and then encrypts the data with the new key.  If -r is specified, the rekey operation is performed recursively under *path*.  *path* specifies the absolute or relative path of a directory. Multiple path values are allowed. |
| `-v` | Generates a new volume encryption key (VEK) for the specified mount point and then encrypts all the file encryption keys in file system with the new key. Prompts for the wallet password because the wallet must be accessed to store the new VEK.  The generated key is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command. |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard (AES) is the only encryption supported for this release. |
| `-k` `key_length` | Specifies the key length for the directory or file specified by `path`. |

The default values for the `-a` and `-k` are determined by the volume parameters specified when `acfsutil` `encr` `set` was run.

The *path* option can specify a path to a file or directory in a read-write snapshot. If the `-r` option is specified with the command on the root directory, the command does not transverse the snapshots under the `.ACFS` directory. If a rekey operation is specified at the file system level, then the operation does not process files and directories of snapshots in the `.ACFS/snaps/` directory.

If Oracle Key Vault is the key store for the file system, then the Oracle Key Vault home environmental variable (`OKV_HOME`) must be set when using the `-v` option to generate a new volume key. If the client was configured to use a password with Oracle Key Vault, then the same password must be entered when prompted.

Only a user with root or system administrator privileges can run this command with the `-v` option. The file owner can also run this command with the `-f` option to rekey encryption on the directory or file.

Examples

The following are examples of the use of `acfsutil` `encr` `rekey`.

Example: Using the acfsutil encr rekey command

```
# /sbin/acfsutil encr rekey -m /acfsmounts/acfs1 -v

# /sbin/acfsutil encr rekey -m /acfsmounts/acfs1 -f
                            -r /acfsmounts/acfs1/myfiles
```

### acfsutil encr set

Purpose

Sets or changes encryption parameters for an Oracle ACFS file system.

Syntax and Description

```
acfsutil encr set -h
acfsutil encr set [ [-a {AES} -k {128|192|256}] [-e] | -u ] -m mount_point
```

`acfsutil` `encr` `set` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `encr` `set` command.

Table: Options for the acfsutil encr set command

| Option | Description |
| --- | --- |
| `-a` `algorithm` | Specifies the algorithm. Advanced Encryption Standard ( `AES` ) is the default value and the only encryption supported for this release. The algorithm must be specified if `-k` is specified. |
| `-k` { `128` \| `192` \| `256` } | Specifies the key length. The key length is set at the volume level. The default is `192`. Must be specified if `-a` is specified. |
| `-e` | Specifies to use Oracle Key Vault as the key store. |
| `-u` | Backs out encryption. Decrypts all encrypted files in the file system and reverts the file system to the state before `acfsutil` `encr` `set` was run on the file system. If security is being used, then this command can only be run after security has been backed out. To remove security, refer to " acfsutil sec prepare ". |
| `-m` `mount_point` | Specifies the directory where the file system is mounted. |

Before running the `acfsutil` `encr` `set` command, you must first run the `acfsutil` `encr` `init` command.

The `acfsutil` `encr` `set` command configures encryption parameters for a file system, transparently generates a volume encryption key, and stores that the generated key in the key store that was previously configured with the `acfsutil` `encr` `init` command.

If auditing is initialized on a cluster, this command also enables an Oracle ACFS encryption auditing source on the file system. The actions performed when enabling this audit source are the same as those done when the `acfsutil` `audit` `enable` command is run directly. For more information, refer to " acfsutil audit enable ".

In addition `acfsutil` `encr` `set` creates the *mount\_point* `/.Security` `/encryption/logs/` directory that contains the log file (`encr-` *hostname* `_fsid.log`) that collects auditing and diagnostic data.

Password requirements when storing the key are dependent on how the encryption key storage was configured. If `-p` was specified with `acfsutil` `encr` `init`, then a password is required to run this command.

Before using the `-e` option to specify Oracle Key Vault as the key store, Oracle Key Vault must be configured first. If you want to choose Oracle Key Vault as the key store for the file system, then the Oracle Key Vault home environmental variable (`OKV_HOME`) must be set when running the command with the `-e` option. If the client was configured to use a password with Oracle Key Vault, then the same password must be entered when prompted.

See also

[*Oracle Key Vault Administrator's Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=OKVAG10489) for information about configuring Oracle Key Vault

The `acfsutil` `encr` `set` `-u` command is not allowed if any snapshots exist in the file system.

Only a user with root or system administrator privileges can run the `acfsutil` `encr` `set` command.

Examples

The following example shows the use of `acfsutil` `encr` `set` command.

Example: Using the acfsutil encr set command

```
# /sbin/acfsutil encr set -a AES -k 256 -m /acfsmounts/acfs1
```

### acfsutil keystore migrate

Purpose

Migrates the encryption keystore.

Syntax and Description

```
acfsutil keystore migrate -h
acfsutil keystore migrate [-p ]
```

`acfsutil` `keystore migrate` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `keystore migrate` command.

Table: Options for the acfsutil keystore migrate command

| Option | Description |
| --- | --- |
| `-p` | Converts the encryption keystore from a SSO wallet to a PKCS wallet. |

If the `-p` option is specified, `acfsutil` `keystore` `migrate` converts the SSO wallet to a PKCS wallet. If the `-p` option is not specified, `acfsutil` `keystore` `migrate` converts the PKCS wallet to a SSO wallet.

Only a user with root or system administrator privileges can run this command.

Examples

The following is an example of the use of `acfsutil` `keystore` `migrate`.

Example: Using the acfsutil keystore migrate command

```
# /sbin/acfsutil keystore migrate
```

## Oracle ACFS Command-Line Tools for Snapshots

This topic provides a summary of commands to manage Oracle ACFS snapshots.

The Oracle ACFS snapshot command summary lists Oracle ACFS snapshot commands with brief descriptions. For an overview of Oracle ACFS snapshots, refer to [About Oracle ACFS Snapshots](introducing-oracle-acfs-and-oracle-advm.md).

For more information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of commands for Oracle ACFS snapshots

| Command | Description |
| --- | --- |
| acfsutil snap convert | Converts the type of an existing snapshot. |
| acfsutil snap create | Creates a snapshot of an Oracle ACFS file system or an existing snapshot. |
| acfsutil snap delete | Deletes a snapshot of an Oracle ACFS file system. |
| acfsutil snap duplicate apply | Updates a duplicate snapshot or file system. |
| acfsutil snap duplicate create | Creates a duplicate of an existing snapshot. |
| acfsutil snap info | Displays information about Oracle ACFS file system snapshots. |
| acfsutil snap link | Creates or deletes a snapshot link. |
| acfsutil snap quota | Sets the quota limit for a specified snapshot. |
| acfsutil snap remaster | Remasters a file system with a specified snapshot. |
| acfsutil snap rename | Renames a snapshot. |

### acfsutil snap convert

Purpose

Converts the type of an existing snapshot image from read-only to read-write or read-write to read-only.

Syntax and Description

```
acfsutil snap convert -h
acfsutil snap convert [-r|-w] snap_shot mount_point
```

`acfsutil` `snap` `convert` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `convert` command.

Table: Options for the acfsutil snap convert command

| Option | Description |
| --- | --- |
| `-r` | Converts snapshot to read-only snapshot. |
| `-w` | Converts snapshot to read-write snapshot. |
| `snap_shot` | Specifies the name of the snapshot to be converted. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `convert` converts the type of an existing snapshot image from a read-only snapshot image to a read-write snapshot image, or from a read-write snapshot image to a read-only snapshot image.

The type option (`-r` or `-w`) is required for the convert operation. Specifying a type parameter that matches the type of the existing snapshot image results in no conversion and no failure. An 11.2 read-only snapshot image can be converted to a read-write snapshot image, but this conversion results in an update of the Oracle ACFS on-disk structure version. After the Oracle ACFS on-disk structure version has been updated, the updated version is not compatible with previous Oracle ACFS 11.2 versions.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `snap` `convert` command.

Example: Using the acfsutil snap convert command

```
$ acfsutil snap convert -w midday_test1 /acfsmounts/critical_apps

$ acfsutil snap convert -r midday_test2 /acfsmounts/critical_apps
```

### acfsutil snap create

Purpose

Creates a read-only or read-write snapshot of an Oracle ACFS file system or an existing snapshot.

Syntax and Description

```
acfsutil snap create -h
acfsutil snap create [-r|-w] [-p parent_snap_shot] snap_shot mount_point
```

`acfsutil` `snap` `create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `create` command.

Table: Options for the acfsutil snap create command

| Option | Description |
| --- | --- |
| `-r` | Creates a read-only snapshot. This is the default setting. |
| `-w` | Creates a read-write snapshot. |
| `snap_shot` | Specifies a name for the snapshot. The name provided must follow host operating system specific naming rules for directories. The `.ACFS/snaps` directory itself cannot be snapped. |
| `-p` `parent_snap_shot` | Specifies the name of an existing snapshot image within the Oracle ACFS file system. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `create` creates a read-only or read-write snapshot of the Oracle ACFS file system mounted on *mount\_point* or creates a snapshot of an existing snapshot if the `-p` option is specified. You can specify `-r` for read-only or `-w` for read-write; read-only is the default if neither `-r` or `-w` are specified.

The read-write snapshot enables the fast creation of an Oracle ACFS snapshot image that can be both read and written without impacting the state of the Oracle ACFS file system hosting the snapshot images. You can use the read-write functionality for testing new versions of application software or running test scenarios on production file data without modifying the original file system.

Snapshots are not separate file systems. The snapshot appears in the `.ACFS/snaps/` *snapshot* directory and initially is a complete replica of the file system at the time the snapshot command was given. A read-only snapshot continues to preserve that initial point-in-time view. A read-write snapshot can be modified by updates written directly to the files located within the `.ACFS/snaps/` *snapshot* hierarchy.

A symbol link (symlink) file is a pointer to a path specified at the time that the symlink is created. For any existing symlink in the source of the `acfsutil` `snap` `create` command, a new link is made in the snapshot; however, the stored path to the symlink target is not modified during snap creation time. When an absolute path is used as the target of the link, the link target of the snapshot still refers to the absolute path, outside the newly-created snapshot namespace. Future modifications to the targeted file can occur through the snapshot symlink, not to a new target inside the snapshot namespace. The contents of the targeted file can also be changed outside of the snapshot. Because of this behavior, you should use relative path targets for all symlinks that are within the same file system.

Any user can access the snapshot directory by specifying the path name. However, the.`ACFS` directory itself is hidden from directory listings of the root of the file system. This prevents recursive commands, such as `rm` `-rf` or `acfsutil` `tag` `set` `-r`, from the root of the file system inadvertently operating on snapshot files.

Snapshots usually use very little storage initially as they share file system blocks with the original file system until a file changes.

Tools such as `du` report the total disk space usage of the snapshotted files, which includes the storage shared with the original versions of the files. To determine the total space used for the snapshots, use the `acfsutil` `snap` `info` or `acfsutil` `info` `fs` command.

Oracle ACFS snapshots are immediately available for use after they are created. They are always online under the`.ACFS/snaps` directory when the original file system is mounted. No separate command is needed to mount them.

The `acfsutil` `snap` `create` operation fails if the cluster is in rolling migration.

Creation from an existing snapshot is not permitted if there are:

- Any snapshots present in the file system that were created with the `ADVM` compatibility set to less than 12.1
- Any snapshots of the file system that were created after `ADVM` compatibility was set to `12.1` but while 11.2 snapshots existed
- Any snapshot deletion cleanup operations still running in the background for the above conditions
	You can display pending snapshot operations with the `acfsutil` `snap` `info` command.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `snap` `create` command to create snapshots on a Linux platform.

Example: Using the acfsutil snap create command on Linux

```
$ /sbin/acfsutil snap create -w midday_test1 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create -w midday_test2 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create payroll_report1 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create payroll_report2 /acfsmounts/critical_apps

$ ls /acfsmounts/critical_apps/.ACFS/snaps
midday_test1  midday_test2  payroll_report1  payroll_report2
```

The following example shows the use of the `acfsutil` `snap` `create` command to create snapshots on a Windows platform. This example shows the creation of a snapshot from an existing snapshot.

Example: Using the acfsutil snap create command on Windows

```
C:\oracle> acfsutil snap create /w snap_1 e:

C:\oracle> acfsutil snap create /w snap_1-1 /p snap_1 e:
```

See also

- [About Oracle ACFS Snapshots](introducing-oracle-acfs-and-oracle-advm.md) for information about Oracle ACFS snapshots
- [Oracle ACFS Disk Space Usage](understanding-oracle-acfs-advanced-topics.md) for information about the number of snapshots supported
- acfsutil snap info for information about displaying pending snapshots operations
- acfsutil info fs for information about displaying the space used for snapshots
- Oracle ACFS Command-Line Tools for Snapshots for information about the `acfsutil` `snap` `duplicate` `apply` and `acfsutil` `snap` `duplicate` `create` commands

### acfsutil snap delete

Purpose

Deletes a snapshot of an Oracle ACFS file system.

Syntax and Description

```
acfsutil -h snap delete
acfsutil snap delete snapshot mount_point
```

`acfsutil` `-h` `snap` `delete` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `delete` command.

Table: Options for the acfsutil snap delete command

| Option | Description |
| --- | --- |
| `snapshot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `delete` deletes the snapshot named *snapshot* in the Oracle ACFS mounted on *mount\_point*. After successful completion of the command, the representation of the snapshot in the`.ACFS/snaps` directory is removed. The command succeeds even if there are open files or directory references; however, storage associated with the snapshot is not released until all such references are closed.

The disk space used by the snapshot being deleted is released by a background task after the completion of the `acfsutil` `snap` `delete` command or after the last close of a file in the snapshot. If one of these background threads is running to clean up a deleted snapshot, then the `acfsutil` `snap` `info` command shows a pending delete operation. For information about the `acfsutil` `snap` `info` command, refer to " acfsutil snap info ".

The `acfsutil` `snap` `delete` operation fails if the cluster is in rolling migration.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `snap` `delete` command.

Example: Using the acfsutil snap delete command

```
$ /sbin/acfsutil snap delete midday_test1 /acfsmounts/critical_apps
acfsutil snap delete: Snapshot operation is complete.
```

### acfsutil snap duplicate apply

Purpose

Applies a previously created duplicated snapshot to an Oracle ACFS snapshot or file system.

Syntax and Description

```
acfsutil snap duplicate apply -h
acfsutil snap duplicate apply [-b | -B snap_shot] [-d trace_level] [snap_shot] mount_point
```

`acfsutil snap duplicate apply` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil snap duplicate apply` command.

Table: Options for the acfsutil snap duplicate apply command

| Option | Description |
| --- | --- |
| `-b` | Specifies that a backup snapshot is generated after a successful completion of the command. The name of the backup is generated in the format `SDBACKUP_seccnt_sourcesnap_targetsnap`, which is described in the text of this topic. |
| `-B` `snap_shot` | Specifies that a backup snapshot with the name specified is generated after a successful completion of the command. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\] for the command execution. |
| `snap_shot` | Specifies that the named snapshot of that file system is the target. The specified snapshot must exist and must be writable. If the \_snap *shot* is not specified, the target for the apply operation is the file system currently mounted at the mount point |
| `mount_point` | Specifies the directory where the duplicate snapshot is applied. |

The `acfsutil` `snap` `duplicate` `apply` command uses the snapshot duplication stream produced by `acfsutil snap duplicate create` to update the specified target file system or snapshot. The stream of data is read from the standard input.

If the target has never been applied to by a `acfsutil` `snap` `duplicate` `apply` operation, this is an initial apply, and the target must be initially empty. If the target has been applied to by a previous apply operation, this is an incremental apply, and the initial contents of the target must match the contents of the older snapshot used to produce the snapshot duplication stream.

If the contents of the target no longer match the older snapshot for the stream, the command returns an error and the stream is not applied. The target must not be updated by other means while the apply operation is in progress. If another update occurs, the command returns an error and stops applying the snapshot duplication stream. If the data stream being applied is identical to the last data stream applied to the specified target, the command exits without writing anything to the target with a status value of `2`.

If the `-b` or `-B` option is specified, then a backup snapshot is taken of the target after the apply operation completes the update. Because the snapshot taken for an apply operation is automatically deleted when the next apply operation completes, the snapshot present is the one from the last-completed apply operation. The backup snapshot provides a known and consistent version of the target for the last successful apply operation and a comparison point to identify the in-progress changes made by a `acfsutil snap duplicate apply` operation.

If a name was not specified with the `-B` option, then a backup snapshot has a name of the form `SDBACKUP_seccnt_sourcesnap` or `SDBACKUP_seccnt_sourcesnap_targetsnap`. In the name string, `seccnt` is a local timestamp (number of seconds since the Unix epoch) indicating the point at which the target was captured by the backup snapshot. `sourcesnap` indicates the snapshot from the source file system that was applied by the last completed `acfsutil snap duplicate apply` operation. `targetsnap`, if present, indicates the snapshot name in the target file system that was updated by the last completed `acfsutil` `snap` `duplicate` `apply` operation.

System administrator (`root`) privileges are required to use this command.

The `acfsutil` `snap` `duplicate` `apply` command produces an exit status of `0` on success, `1` if a fatal error occurs, or `2` if the data stream read matches the last previous data stream applied to the specified target.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

The following example shows the use of the `acfsutil` `snap` `duplicate` `apply` command. Because the command expects to read a binary data stream from its standard input, this command is normally used in a pipeline with the `acfsutil` `snap` `duplicate` `create` command, as shown in the example.

Example: Using the acfsutil snap duplicate apply command

```
$ /sbin/acfsutil snap duplicate create new_snapshot_name /acfsmounts/critical_apps | \
      /sbin/acfsutil snap duplicate apply /acfsmounts/ca_backups
```

### acfsutil snap duplicate create

Purpose

Creates a duplicate snapshot of an existing snapshot.

Syntax and Description

```
acfsutil snap duplicate create -h
acfsutil snap duplicate create [-r] [-d trace_level] [-p parent_snapshot]
  [-i old_snapshot] new_snapshot mount_point
```

`acfsutil snap duplicate create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `duplicate` `create` command.

Table: Options for the acfsutil snap duplicate create command

| Option | Description |
| --- | --- |
| `-r` | Specifies to mark the snap duplication stream as a restart stream. This option is intended for use on the second or later attempt to create and apply a given stream. This option might be necessary if an earlier attempt terminated prematurely. |
| `-d` *trace\_level* | Specifies the trace level setting \[0..6\] for the command execution. |
| `-p` `parent_snapshot` | Specifies the name of a parent snapshot image of which both the `<span class="codeinlineitalic">old_snapshot</span>` and `<span class="codeinlineitalic">new_snapshot</span>` are children.  This option ensures that both snapshots are children (*snap-of-snap*) of the same snapshot. If the `-p` option is not specfied, then either the `<span class="codeinlineitalic">new_snapshot</span>` must be a child of the `<span class="codeinlineitalic">old_snapshot</span>`, or the two snapshots must be snapshots of the base file system at the specified mount point. |
| `-i` `old_snapshot` | Specifies the name of an existing snapshot. |
| `new_snapshot` | Specifies a name for the new snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. This is the mount point of the file system of which the snapshots were taken. |

The `acfsutil` `snap` `duplicate` `create` command externalizes snapshot-related data in a form suitable for use by snap duplicate apply to create a different instance of a compatible snapshot. This externalized data is called a snapshot duplication stream.

If only the new snapshot name is specified, then this command encodes the entire contents of the named snapshot (the difference between an empty snapshot and this snapshot). This is an initial snap duplicate operation.

If both the old snapshot name and new snapshot name are given, this command encodes only the differences between the two snapshots. This is an incremental snap duplicate operation.

In either case, this command writes the snapshot duplication stream to its standard output.

System administrator (`root`) privileges are required to use this command.

The `acfsutil` `snap` `duplicate` `create` command produces an exit status of `0` on success or `1` if a fatal error occurs.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

The following example shows the use of the `acfsutil` `snap` `duplicate` `create` command. Because the command writes a binary data stream to its standard output, this command is normally used in a pipeline with the `acfsutil` `snap` `duplicate` `apply` command, as shown in the example.

Example: Using the acfsutil snap duplicate create command

```
$ /sbin/acfsutil snap duplicate create new_snapshot_name /acfsmounts/critical_apps | \
      /sbin/acfsutil snap duplicate apply /acfsmounts/ca_backups
```

### acfsutil snap info

Purpose

Displays information about Oracle ACFS file system snapshots.

Syntax and Description

```
acfsutil snap info -h
acfsutil snap info [-t] [snap_shot] mount_point
```

`acfsutil` `snap` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `info` command.

Table: Options for the acfsutil snap info command

| Option | Description |
| --- | --- |
| `-t` | Displays a tree structure for the specified snapshot and mount point. |
| `snap_shot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `snap` `info` command displays information about an individual specified snapshot or all snapshots in the specified Oracle ACFS file system.

The snapshot name, snapshot type, parent name, creation date and time, and space used are displayed. The parent name is either the mount point, or the parent snapshot if the snapshot was created from an existing snapshot.

The type of a snapshot is indicated by one or more of the following strings. Any relevant strings are displayed on the same line.

- `RO` - snapshot is read-only
- `RW` - snapshot is read-write
- `Primary` - snapshot is a primary storage location for replication
- `Standby` - snapshot is a standby storage location for replication
- `REPL` - snapshot is an internal snapshot used by replication
- `DUP` - snapshot or its parent is a target of snap duplicate apply

The appearance of the string `REPL` is not related to whether a snapshot is a replication primary or standby. This string appears only if the snapshot is one that was created by replication for its own internal use.

The string `DUP` appears if either of the following conditions is true:

- The snapshot is in use as the target of an apply operation.
- The parent of the snapshot was in use as the target of an apply operation at the point when the snapshot was created.

The `snapshot` `space` `usage` amount includes snapshot metadata. If all the files are deleted from a snapshot, some metadata still remains and that amount is displayed with `acfsutil` `snap` `info`.

When using an accelerator volume, the reported `snapshot` `space` `usage` amount can include space that is in use on the accelerator volume.

To reclaim the disk space used by snapshots, delete the snapshots. Deleting the files within the snapshots may not reclaim this disk space.

The `acfsutil` `snap` `info` command shows the status of a snapshot that is in the process of being deleted as follows:

- When waiting on files to be closed:
	```
	snapshot_name (delete waiting for last close)
	```
- When freeing the storage for the snapshot in the background:
	```
	snapshot_name (delete in progress)
	```

Oracle ACFS caches and asynchronously updates snapshot storage usage statistics. If an Oracle ASM instance is terminated, power is lost to the machine, or the Oracle ACFS file system goes offline for any reason, one of these cached updates may be lost. This loss can result in the display of a message similar to `Reported` `snapshot` `space` `usage` `is` `inaccurate` when `acfsutil` `snap` `info` is run.

Examples

The following example shows the use of the `acfsutil` `snap` `info` command on a Linux platform. The command output contains information about a read-only (RO) snapshot, a read-write (RW) snapshot with quota information, a snapshot in `delete` `waiting` `for` `last` `close` status, and a snapshot in `delete` `in` `progress` status. After a delete operation completes on a snapshot and the background process finishes the clean up of a deleted snapshot, messages about the delete operation do not appear in the output.

Example: Using the acfsutil snap info command on Linux

```
$ /sbin/acfsutil snap info /acfsmounts/critical_apps/
snapshot name:               midday_test (delete waiting for last close)
snapshot creation time:      Tue Apr  5 10:52:55 2016

snapshot name:               payroll_report1
snapshot location:           /acfsmounts/critical_apps/.ACFS/snaps/payroll_report1
RO snapshot or RW snapshot:  RW
parent name:                 /acfsmounts/critical_apps/
snapshot creation time:      Tue Apr  5 10:52:59 2016
storage added to snapshot:   95514624   (  91.09 MB )

quota:                       104857600  ( 100.00 MB )
quota usage:                 91 %

snapshot name:               midday_test2 (delete in progress)
snapshot creation time:      Mon Apr 11 11:40:13 2016

snapshot name:               payroll_report2
snapshot location:           /acfsmounts/critical_apps/.ACFS/snaps/payroll_report2
RO snapshot or RW snapshot:  RO
parent name:                 midday_test2
snapshot creation time:      Mon Apr 11 12:05:42 2016
storage added to snapshot:   1081344   (   1.03 MB )

    number of snapshots:  3 (active)
                          1 (delete in progress)
        snapshot space usage: 102084608  (  97.36 MB )

$ /sbin/acfsutil snap info -t /acfsmounts/critical_apps
/acfsmounts/critical_apps RW
midday_test               RW    /acfsmounts/critical_apps
payroll_report1           RW    /acfsmounts/critical_apps
midday_test2              RW    /acfsmounts/critical_apps
payroll_report2           RO    midday_test2

$ /sbin/acfsutil snap info -t midday_test2 /acfsmounts/critical_apps
midday_test2              RW
payroll_report2           RO    midday_test2
```

### acfsutil snap link

Purpose

Creates or deletes a snapshot link.

Syntax and Description

```
acfsutil snap link -h
acfsutil snap link -s snap_shot path_to_link
acfsutil snap link -s snap_shot -d path_to_link
```

`acfsutil` `snap` `link` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `link` command.

Table: Options for the acfsutil snap link command

| Option | Description |
| --- | --- |
| `-s` `snap_shot` | Specifies the name of an Oracle ACFS snapshot in the Oracle ACFS file system. |
| `-d` | Deletes the specified snapshot link. |
| `path_to_link` | Specifies a directory in the Oracle ACFS file system. |

You can create or delete snapshot links with the `acfsutil` `snap` `link` command. A snapshot link provides access to the contents of a snapshot using an alternate path which does not include the `.ACFS/snaps` directory, the default location where snapshot are created.

A snapshot link is a specialized hard link that requires that only one snapshot link may exist for a snapshot. Snapshot links can only be created in the primary file system, not within another snapshot. Snapshot links can be recreated to change the name or location of the snapshot link. The name that you specify for a snapshot link does not have to be the same as the name or the snapshot to which it links. A snapshot link does require on disk changes and the `COMPATIBLE.ADVM` disk group attribute must be set to `18.0` or higher. Snapshot links can only be created and deleted with the `acfsutil` `snap` `link` command. The links cannot be moved or removed with normal operating system commands.

You can display information about snapshot links with the `acfsutil` `snap` `info` command. You can use `acfsutil` `snap` `info` `snap_shot` to determine whether the specified snapshot has a link.

Examples

The following example shows the use of the `acfsutil` `snap` `link` command. After a new snapshot is created, a link is created to the new snapshot.

Example: Using the acfsutil snap link command

```
$ /sbin/acfsutil snap create -w snap1 /usmmnt
acfsutil snap create: Snapshot operation is complete.

$ /sbin/acfsutil snap link -s snap1 /usmmnt/dir1/link
acfsutil snap link: Snapshot operation is complete.

$ /sbin/acfsutil snap info /usmmnt
snapshot name:               snap1
snapshot location:           /usmmnt/.ACFS/snaps/snap1
snapshot link:               /usmmnt/dir1/link
RO snapshot or RW snapshot:  RW
parent name:                 /usmmnt
...
```

### acfsutil snap quota

Purpose

Sets the quota limit for a specified snapshot.

Syntax and Description

```
acfsutil -h snap quota

acfsutil snap quota [+|-]n[K|M|G|T|P] snapshot mount_point
```

`acfsutil` `-h` `snap` `quota` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `quota` command.

Table: Options for the acfsutil snap quota command

| Option | Description |
| --- | --- |
| \[`+` \| `-`\] *n*  `K` \| `M` \| `G` \| `T` \| `P` | Specifies the quota limit size for the Oracle ACFS snapshot where *n* is a valid positive whole number greater than zero. The number can be preceded by a `+` or - to indicate the amount to add or decrease. If no operand exists, the new size is the absolute size.  Specifies that the integer supplied for size is in the units of `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), `T` (Terabytes), or `P` (Petabytes). If the unit indicator is specified, then it must be appended to the integer. If omitted, the default unit is bytes. |
| `snapshot` | Specifies a name of the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The acfsutil snap quota command sets the quota limit for a specified snapshot on the specified Oracle ACFS file system.

The quota can be larger than the size of the file system because a file system can be resized or automatically resized.

The quota limit specified does not reserve space. The quota only establishes an upper limit on the amount of storage that can be added to the snapshot.

Only snapshots created after ADVM compatibility (`COMPATIBLE.ADVM`) has been set to `12.2` or greater have storage accounting tracking and the ability to have quotas set.

Snapshots can be converted from read-write (RW) to read-only (RO) and vice versa. Both RW and RO snapshots can have a quota.

There is a grace period and advanced warnings for quota usage. A warning message is written to both the alert log and the console if the requested storage allocation causes the local storage usage to be near or exceeding more than `90%` of the quota. If an allocation exceeds the quota, then the write or other modifying operation fails as `EDQUOT`, or it may fail as `ENOSPC`, depending whether the quota limit is set larger than the size of the file system.

System administrator (`root`) privileges are required to use this command.

You can display snapshot information, including the quota limit and quota usage percentage, with the `acfsutil` `snap` `info` command. For information about `acfsutil` `snap` `info`, refer to " acfsutil snap info ".

Examples

The following example shows the use of the `acfsutil` `snap` `quota` command.

Example: Using the acfsutil snap quota command

```
$ /sbin/acfsutil snap quota +500M snap_test /acfsmounts/acfs1
```

### acfsutil snap remaster

Purpose

Remasters an Oracle ACFS file system with a snapshot.

Syntax and Description

```
acfsutil snap remaster -h
acfsutil snap remaster { snapshot | -c } -f volume
```

`acfsutil snap remaster` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `remaster` command.

Table: Options for the acfsutil snap remaster command

| Option | Description |
| --- | --- |
| `-c` | Continues the interrupted remaster operation. After the command has started, the remastering must run to completion. |
| `-f` | Forces the operation and does not prompt for questions. |
| `snapshot` | Specifies the name of an existing snapshot. |
| `volume` | Specifies specifies the primary Oracle ADVM volume device path for the file system. |

This command accepts a snapshot name or the `-c` option.

The specified snapshot is used for the base of the file system, replacing the current base of the file system. Using an existing read-only or read-write snapshot, the command reintegrates the snapshot extents into the base of the current file system creating a new remastered file system with the point in time state of the snapshot. The remastered file system is left with no snapshots. This operation must be done on an unmounted file system and it cannot be reversed.

Use the `-c` option, instead of the snapshot name, to complete an interrupted snapshot remastering.

You cannot remaster a file system on which replication, security, or encryption is running. You must terminate replication, security, or encryption before running the `acfsutil` `snap` `remaster` command. In addition, you cannot remaster a file system with plugins enabled.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `snap` `remaster` command.

Example: Using the acfsutil snap remaster command

```
$ /sbin/acfsutil snap remaster snapshot volume
```

### acfsutil snap rename

Purpose

Renames an Oracle ACFS snapshot.

Syntax and Description

```
acfsutil snap rename -h
acfsutil snap rename old_snapshot new_snapshot mount_point
```

`acfsutil snap rename` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `duplicate create` command.

Table: Options for the acfsutil snap rename command

| Option | Description |
| --- | --- |
| `old_snapshot` | Specifies the name of an existing snapshot. |
| `new_snapshot` | Specifies a name for the new snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `snap` `rename` command is used to safely rename an existing snapshot in the filesystem.

While a snapshot with open files can be renamed, applications accessing files in that snapshot experience the same behavior as operating in a non-snap directory tree in which one of the parent directories was renamed.

Renaming snapshots used in conjunction with pluggable databases (PDBs) is not supported at this time. Such a snapshot should not be renamed.

Replication-specific snapshots cannot be renamed as this may cause complications and inconsistencies with replication.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

The following example shows the use of the `acfsutil snap rename` command.

Example: Using the acfsutil snap rename command

```
$ /sbin/acfsutil snap rename old_snapshot_name new_snapshot_name /acfsmounts/critical_apps
```

## Oracle ACFS Command-Line Tools for Compression

This topic provides a summary of commands to manage Oracle ACFS compression.

The Oracle ACFS compression command summary lists Oracle ACFS compression commands with brief descriptions. For an overview of Oracle ACFS compression, refer to [Oracle ACFS Compression](introducing-oracle-acfs-and-oracle-advm.md).

For more information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of commands for Oracle ACFS compression

| Command | Description |
| --- | --- |
| acfsutil compress copy | Copies and compresses a file or files in a directory. |
| acfsutil compress info | Displays compression information about a file. |
| acfsutil compress off | Disables Oracle ACFS file compression. |
| acfsutil compress on | Enables Oracle ACFS file compression. |

### acfsutil compress copy

Purpose

Compresses and copies a file.

Syntax and Description

```
acfsutil compress copy -h
acfsutil compress copy [-v] [-f] {-c size source | [-n] {-r source | source [...]}
  target_dir
```

The following table contains the options available with the `acfsutil` `compress` `copy` command.

Table: Options for the acfsutil compress copy command

| Option | Description |
| --- | --- |
| `-v` | Specifies verbose mode. |
| `-f` | Specifies to overwrite any existing copies. |
| `-c` `size source` | Copies a single source file and uses compression unit (CU) *size* for the copy.  The format of *size* is *n* `K`. The CU sizes supported are: `4K`, `8K`, `16K`, `32K`, `64K` and `128K` bytes. |
| `-n` `source` | Specifies that copies created are not compressed. |
| `-r` `source` | Specifies to recursively copy files and directories starting from a single source directory. |
| `source [...]` | Specifies source files to be copy. |
| `target_dir` | Specifies the target directory to copy into. |

The `acfsutil` `compress` `copy` command does not copy over an existing files unless the `-f` option is used. If `-f` is not used, the copy operation terminates when the first existing target is found.

The command does not copy to an Oracle ACFS file system which is capable of supporting compression if compression is disabled unless the `-n` option is specified.

Example: Using the acfsutil compress copy command

```
$ /sbin/acfsutil compress copy -v -f my_file1 my_file2 /my_target_directory
```

### acfsutil compress info

Purpose

Displays information about compressed files.

Syntax and Description

```
acfsutil compress info -h
acfsutil compress info pathname
```

The following table contains the options available with the `acfsutil` `compress` `info` command.

Table: Options for the acfsutil compress info command

| Option | Description |
| --- | --- |
| `pathname` | Specifies the pathname to a file. |

Example: Using the acfsutil compress info command

```
$ /sbin/acfsutil compress info /my_mount_point/testfile1

Compression Unit size: 8192
Disk storage used: ( 189.89 MB )
Disk storage saved: ( 810.20 MB )
Storage used is 18% of what the uncompressed file would use
```

### acfsutil compress off

Purpose

Disables Oracle ACFS compression.

Syntax and Description

```
acfsutil compress off -h
acfsutil compress off mount_point
```

The following table contains the options available with the `acfsutil` `compress` `off` command.

Table: Options for the acfsutil compress off command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

When running `acfsutil` `compress` `off`, the following apply:

- Files that are created after compression is disabled are created uncompressed.
- Any compressed files in the file system remain compressed.

You must have root or system administrator privileges to run this command.

Example: Using the acfsutil compress off command

```
$ /sbin/acfsutil compress off /my_mount_point
```

### acfsutil compress on

Purpose

Enables Oracle ACFS compression.

Syntax and Description

```
acfsutil compress on -h
acfsutil compress on [-a algorithm] mount_point
```

The following table contains the options available with the `acfsutil` `compress` `on` command.

Table: Options for the acfsutil compress on command

| Option | Description |
| --- | --- |
| `-a` `algorithm` | Specifies the default compression algorithm. Currently only `lzo` is available and that is the default algorithm used. |
| `mount_point` | Specifies the directory where the file system is mounted. |

Note:

Oracle ACFS compression is not supported on Oracle Database files. Oracle ACFS file systems which are intended to hold database files should not be compressed with Oracle ACFS compression.

When running `acfsutil` `compress` `on`, the following apply:

- Files created after compression is enabled are compressed by default.
- Any uncompressed files in the file system remain uncompressed.

You must have root or system administrator privileges to run this command.

Example: Using the acfsutil compress on command

```
$ /sbin/acfsutil compress on /my_mount_point
```

## Oracle ACFS Command-Line Tools for Oracle ACFS in the Cluster Domain

This topic provides a summary of commands to manage Oracle ACFS in the cluster domain.

The Oracle ACFS cluster domain command summary lists commands for managing Oracle ACFS in the cluster domain and provides brief descriptions. For information about Oracle ACFS in the cluster domain and Oracle ACFS remote service, refer to [About Oracle ACFS in the Cluster Domain](introducing-oracle-acfs-and-oracle-advm.md).

For more information about running Oracle ACFS commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of commands for Oracle ACFS in the cluster domain

| Command | Description |
| --- | --- |
| acfsremote installed | Checks whether your current node has the Oracle ACFS remote service drivers and any applicable system transports installed. |
| acfsremote loaded | Checks the status of system resources to determine if Oracle ACFS remote service is loaded. |
| acfsremote supported | Checks to ensure that your current node is supported for Oracle ACFS remote service. |
| acfsutil cluster credential | Generates, updates, and imports the Oracle ACFS remote service credentials. |
| acfsutil cluster info | Displays the information on the type of cluster and internal information for the running cluster. |
| acfsutil remote clear | Clears the Oracle ACFS remote attribute from a file. |
| acfsutil remote set | Sets a file attribute as Oracle ACFS remote. |
| advmutil export create | Creates the exports for a cluster and allocates their initial storage. |
| advmutil export list | Queries information for export management. |
| advmutil export lsof | Displays active files for all repositories or in a single repository. |
| advmutil export mapping | Reexports all exports or only exports for a particular cluster. |
| advmutil export remove | Removes the configuration metadata of an export. |
| advmutil export resize | Resizes storage to the underlying backing file for an export. |
| advmutil session list | Lists the current state and description of Oracle ACFS remote service sessions on the Oracle Database member cluster. |
| advmutil transport create | Creates a transport on the Domain Services Cluster (DSC). |
| advmutil transport list | Displays the configured transports on the system. |
| advmutil transport remove | Removes a transport. |

### acfsremote installed

Purpose

Checks whether your current node has the Oracle ACFS remote service drivers installed.

Syntax and Description

```
acfsremote installed -h
acfsremote installed [-trace trace_level] [-member] [-domain]
```

The following table contains the options available with the `acfsremote` `installed` command.

Table: Options for the acfsremote installed command

| Option | Description |
| --- | --- |
| `-trace` `trace_level` | Specifies the trace level. |
| `-member` | Specifies to check the member cluster |
| `-domain` | Specifies to check the Domain Services Cluster (DSC). |

`acfsremote` `installed` checks whether your current node has the Oracle ACFS remote service drivers and any applicable system transports installed.

This command is applicable on both member clusters and Domain Services Clusters (DSC).

Example: Using acfsremote installed

In this example the Oracle ACFS remote service drivers and an iSCSI transport have been installed.

```
#acfsremote installed
ACFS-9843: ACFS Remote installed: True
ACFS-9844: iSCSI installed: True
```

### acfsremote loaded

Purpose

Checks the status of system resources to determine if Oracle ACFS remote service is loaded.

Syntax and Description

```
acfsremote loaded -h
acfsremote loaded [-trace trace_level] [-member] [-domain]
```

The following table contains the options available with the `acfsremote` `loaded` command.

Table: Options for the acfsremote loaded command

| Option | Description |
| --- | --- |
| `-trace` `trace_level` | Specifies the trace level. |
| `-member` | Specifies to check the member cluster |
| `-domain` | Specifies to check the Domain Services Cluster (DSC). |

`acfsremote` `loaded` checks the status of system resources to determine if Oracle ACFS remote service is loaded. If all services are loaded, then Oracle ACFS remote service is loaded and running correctly. If a transport is not used or configured, then it may show as `False`.

This command is applicable on both member clusters and Domain Services Clusters (DSC).

Example: Using acfsremote loaded

In the following example, Oracle ACFS remote service drivers and configuration are determined to be correct and running. However, there are no iSCSI transports currently configured, so iSCSI has not been started.

```
#acfsremote loaded
ACFS-9846: ACFS Remote loaded: True
ACFS-9847: iSCSI loaded: False
```

### acfsremote supported

Purpose

Checks to ensure that your current node is supported for Oracle ACFS remote service.

Syntax and Description

```
acfsremote supported -h
acfsremote supported [-trace trace_level] [-member] [-domain]
```

The following table contains the options available with the `acfsremote` `supported` command.

Table: Options for the acfsremote supported command

| Option | Description |
| --- | --- |
| `-trace` `trace_level` | Specifies the trace level. |
| `-member` | Specifies to check the member cluster |
| `-domain` | Specifies to check the Domain Services Cluster (DSC). |

`acfsremote` `supported` checks to ensure that your current node is supported for Oracle ACFS remote service.

This command is applicable on both member clusters and Domain Services Clusters (DSC).

Example: Using acfsremote supported

In this example, the node is supported for Oracle ACFS remote service with the correct kernels and package requirements, and also supported for the iSCSI transport.

```
#acfsremote supported
ACFS-9840: ACFS Remote supported: True
ACFS-9841: iSCSI supported: True
```

### acfsutil cluster credential

Purpose

Generates, updates, or imports the Oracle ACFS remote service credentials.

Syntax and Description

```
acfsutil cluster credential -h
acfsutil cluster credential { [-n] |
  -l [cluster_name] [-n] |
  -g cluster_name -o cluster_manifest_file [-c version] |
  -r cluster_name [-f] |
  -s user_name:group_name |
  -i cluster_manifest_file
  }
```

The following table contains the options available with the `acfsutil` `cluster` `credential` command.

Table: Options for the acfsutil cluster credential command

| Option | Description |
| --- | --- |
| `-n` | Suppresses headers when listing registered member clusters. |
| `-l` \[ `cluster_name` \] | Lists registered member clusters. Optionally, include a cluster name to list only a specific cluster or include the `-n` flag to suppress the headers in the output. |
| `-g` `cluster_name` -o `cluster_manifest_file` \[-c `version` \] | Generate the member cluster's credentials with specified name and export the credentials to the specified file. Optionally, add the `-c` flag to specify the version that the client cluster is running. |
| `-r` `cluster_name` | Deletes the credential for the specified cluster. Optionally, use `-f` to force the deletion. |
| `-s` `user_name`*:* `group_name` | Adds \_user *name* and \_group *name* to the credential file to enable permissions for access to Oracle ACFS remote service. The \_user *name* and \_group *name* must specify an existing operating system user and group. |
| `-i` `cluster_manifest_file` | Import the credentials contained in the \_cluster\_manifest *file*. |

`acfsutil` `cluster` `credential` generates or imports the Oracle ACFS remote service credentials. In most cases, this command is not directly called by an end user.

This command is applicable on all cluster types.

Example: Using acfsutil cluster credential

In the following example, `acfsutil` `cluster` `credential` sets up the OCR for Oracle ACFS remote service, and then imports an existing credential file into it.

```
#/sbin/acfsutil cluster credential -s grid_user:asm_group
#/sbin/acfsutil cluster credential -s grid2:oinstall
#/sbin/acfsutil cluster credential -i my_credential_file
```

### acfsutil cluster info

Purpose

Displays information about the type of cluster and the internal information for the running cluster.

Syntax and Description

```
acfsutil cluster info -h
acfsutil cluster info
```

`acfsutil` `cluster` `info` displays information about the type of cluster and the internal information for the running cluster. The command can be used to ensure that the kernel Oracle ACFS cluster is in sync with Oracle ASM. This command is applicable on all cluster types.

Example: Using acfsutil cluster info

```
# /sbin/acfsutil cluster info
Node Count: 2
Rebuild Master: 2
Local Node: 1
Current Incarnation: 10
ACFS DLM Interfaces: ENABLED
OKS DLM Interfaces: ENABLED
Cluster State: [ NORMAL_OPERATION ]
ACFS Remote mode: [DOMAIN SERVICES]
ASM Storage mode: [LOCAL]
Oracle Appliance: [NONAPP]
Nodes:
Node 1 - IP 10.0.0.2 - node1
Node 2 - IP 10.0.0.3 - node2
```

The output from the `acfsutil` `cluster` `info` command includes the following information about the current cluster.

- Node Count: Number of nodes in the cluster.
	In this example, this is a 2-node cluster.
- Rebuild Master: Rebuild master node.
	In this example, node 2 is in charge of rebuilding the cluster.
- Current Incarnation: An incarnation is any significant membership change in the cluster.
	In this example, there have been 10 incarnations of the cluster.
- Cluster State: NORMAL\_OPERATION, MIGRATION, UNKNOWN
	In this example, the cluster is operating normally.
- ACFS Remote mode:
- MEMBER - a member cluster
- DOMAIN SERVICES - a domain services cluster
	In this example, the ACFS remote mode is set to a domain services cluster,
	- OFF - a standalone cluster
- ASM Storage Mode:
- LOCAL - the cluster has locally attached storage
	In this example, the ASM Storage mode is set to local attached storage.
	- REMOTE - the cluster is using storage served from a REMOTE Domain Services Cluster. REMOTE should only display when Oracle ACFS Remote mode is MEMBER.

### acfsutil remote clear

Purpose

Clears the Oracle ACFS remote attribute from a file.

Syntax and Description

```
acfsutil remote clear -h
acfsutil remote clear path_name
```

The following table contains the options available with the `acfsutil` `remote` `clear` command.

Table: Options for the acfsutil remote clear command

| Option | Description |
| --- | --- |
| `path_name` | Specifies the location of the file. |

`acfsutil` `remote` `clear` clears the Oracle ACFS remote attribute from a file identified by the specified path name. Clearing the remote attribute allows the file on disk to be removed or truncated by a system administrator.

Example: Using acfsutil remote clear

```
$ acfsutil remote clear my_remote_file
```

### acfsutil remote set

Purpose

Sets a file attribute as Oracle ACFS remote.

Syntax and Description

```
acfsutil remote set -h
acfsutil remote set path_name
```

The following table contains the options available with the `acfsutil` `remote` `set` command.

Table: Options for the acfsutil remote set command

| Option | Description |
| --- | --- |
| `path_name` | Specifies the location of the file. |

`acfsutil` `remote` `set` sets the Oracle ACFS remote attribute on a file identified by the specified path name. Setting the remote attribute prevents the file on disk from being removed or truncated by a system administrator.

Example: Using the acfsutil remote set command

```
$ acfsutil remote set my_remote_file
```

### advmutil export create

Purpose

Creates exports and allocates their initial storage.

Syntax and Description

```
advmutil export create -h
advmutil export create -n export_name -c cluster_name -p storage_repos {-s file_size | -f}
```

The following table contains the options available with the `advmutil` `export` `create` command.

Table: Options for the advmutil export create command

| Option | Description |
| --- | --- |
| `-n` `export_name` | Specifies the export name. |
| `-c` `cluster_name` | Specifies the member cluster name. |
| `-p` `storage_repos` | Specifies the location of the repository where the backing file is stored. |
| `-s` `file_size` | Specifies the file size in the format *n* {K\|M\|G\|T\|P\|E}. The units are K (Kilobytes), M (Megabytes), G (Gigabytes), T (Terabytes), P (Petabytes) or E (Exabytes). |
| `-f` | Specifies to reuse an existing storage repository. |

`advmutil` `export` `create` manages the exports for a cluster. It is responsible for creating exports and allocating their initial storage. When creating an export, a fully-allocated (non-sparse) file is allocated for performance reasons.

When creating an export, the name provided with `-n` option also becomes the name of the volume on the member cluster. If `-n` `expvol1` is provided, then that would result in device `/dev/asm/expvol1-000` created on the member cluster.

The `-p` option must specify an Oracle ACFS file system for the storage repository. If an Oracle ACFS clusterware (CRS) resource exists, then it is modified to depend on any transport VIP resources registered to the cluster.

If the backing file already exists in a repository, then the `-f` option must be provided. After a backing file is created, Oracle ACFS lists it as in-use by Oracle ACFS remote service (with the `Remote` flag) and prevents various actions against the file.

Snapshots of exports are on the DSC only. Snapshots created on the member cluster of the Oracle ACFS file system mounted on the member cluster are accessible on the member cluster only.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export create

In the following example, `export1` is created on `cluster1` with the repository located at `/repository1` and the size allocated is 512 M.

```
#/sbin/advmutil export create -n export1 -c cluster1 -p /repository1 -s 512M
Creating File Backed Volume.
Export and backing store for volume 'export1' for cluster 'cluster1' created.
```

To use Oracle ACFS remote service repositories with Oracle ACFS snapshots of the DSC repository, some manual steps must be performed on the DSC. When snapping a DSC repository, all backing files in the repository are snapped.

In the following example, a snapshot is exported to the same member cluster.

1. Create a backing file.
	```
	#/sbin/advmutil export create -c mc1 -p /repo -n vol1 -s 2G
	```
2. Snap the backing file.
	```
	$/sbin/acfsutil snap create -w snap1 /repo
	```
3. Create a snapshot link in the root of the repository:
	```
	$/sbin/acfsutil snap link -s snap1 /repo/snap1_link
	```
4. Export the snap, using the -f option.
	```
	#/sbin/advmutil export create -f -n vol1 -p /repo/snap1_link -c mc1
	```

In the following example, a snapshot is exported to a different member cluster.

1. Create a backing file.
	```
	#/sbin/advmutil export create -c mc1 -p /repo -n vol1 -s 2G
	```
2. Snap the backing file.
	```
	$/sbin/acfsutil snap create -w snap3 /repo
	```
3. Create a snapshot link in the root of the repository:
	```
	$/sbin/acfsutil snap link -s snap3 /repo/snap3_link
	```
4. Use `ln` to link to the file from the new member cluster repository.
	Note that f903... is the GUID of the old member cluster and 54633... is the GUID of the new member cluster.
	```
	$ln -sf /repo/54633dd2059d6f2cbff1217a6054564b/vol1 /repo/snap3_link/f9038b6ff0d64f36fff4d345803dfacd/vol1
	```
5. Add the new snapshot to the new member cluster.
	```
	#/sbin/advmutil export create -f -n vol1 -p //repo/ -c mc2
	```

### advmutil export list

Purpose

Displays information about exports and member clusters.

Syntax and Description

```
advmutil export list -h
advmutil export list [-c cluster_name] [-o options] [-g group_type] [-a] [-n]
```

The following table contains the options available with the `advmutil` `export` `list` command.

Table: Options for the advmutil export list command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the name of the member cluster. |
| `-o` `options` | Specifies an options list, comma separated, with no spaces. The options are *clientDev*, *clusterGUID*, *clusterName*, *storageRepo*, *exportName*, *filePath*, *state*, *exportSize*, *active*, *domainNode*, and *minor*. |
| `-g` `group_type` | Specifies the group type by *clusterName*, *clusterGUID*, or *storageRepo*. |
| `-a` | Displays only active exports. |
| `-n` | Specifies not to print column headers. |

`advmutil` `export` `list` is a powerful query command for export management. It contains a default view that displays basic information, but can also be used to sort by different groups, and to display different pieces of information on different clusters.

By default, `advmutil` `export` `list` sorts by cluster name (the *clusterName* group sort option). Exports can also be sorted by storage repository (*storageRepo*) or by cluster GUID (*clusterGUID*).

The default view of the exports is meant to be easily readable with appropriate headers and informational queues. You can use the `-n` option to display all output on a single line with no headers so that the information can be used in a script.

The default view includes the *clientDev* option which displays the pathname to the device on the member cluster system. This default view can be provided to member cluster administrators to describe the information the administrators require to administer their systems.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export list

The following example lists the export name, storage size, export minor, storage repository, and client ADVM volume device for the member cluster `cluster1`. Note the client ADVM volume device is displayed by default.

```
#/sbin/advmutil export list -c cluster1 -o exportSize,minor,storageRepo
clusterName: cluster1
exportName storageSize exportMinor storageRepository  (client ADVM device)
-------------------------------------------------------------------------
exporta       512.00M          0   /repo              (/dev/asm/exporta-000)
exportb       512.00M          1   /repo              (/dev/asm/exportb-001)
exportc       512.00M          2   /repo              (/dev/asm/exportc-002)
```

### advmutil export lsof

Purpose

Lists active files for in repositories.

Syntax and Description

```
advmutil export lsof -h
advmutil export lsof [-p path] [-a]
```

The following table contains the options available with the `advmutil` `export` `lsof` command.

Table: Options for the advmutil export lsof command

| Option | Description |
| --- | --- |
| `-p` `path` | Specifies the location of the directory or file. |
| `-a` | Displays only active exports. |

`advmutil` `export` `lsof` shows active files for all repositories, or a specified file or directory in a single repository.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export lsof

In the following example, the active files are displayed for the member cluster `cluster1`.

```
#/sbin/advmutil export lsof
EXPORT_NAME STATE    CLUSTER_NAME REPO_ID  REPO_PATH
exporta     unknown  cluster1     45057_2  /repo
exportb     unknown  cluster1     45057_2  /repo
exportc     unknown  cluster1     45057_2  /repo
```

### advmutil export mapping

Purpose

Reexports all exports or only exports for a particular cluster.

Syntax and Description

```
advmutil export mapping -h
advmutil export mapping [-c cluster_name]
```

The following table contains the options available with the `advmutil` `export` `mapping` command.

Table: Options for the advmutil export mapping command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the name of the member cluster. |

`advmutil` `export` `mapping` reexports all exports or only exports for a specified member cluster. It can be used to force Oracle ACFS remote service to reexport all configured exports in the event of a system administrator action that has removed access to a particular export.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export mapping

In the following example, exports are reexported for the member cluster `cluster1`.

```
#/sbin/advmutil export mapping -c cluster1
```

### advmutil export remove

Purpose

Removes the configuration metadata of an export.

Syntax and Description

```
advmutil export remove -h
advmutil export remove -c cluster_name [-p storage_repos -n export_name] [-f] [-b] [-y]
```

The following table contains the options available with the `advmutil` `export` `remove` command.

Table: Options for the advmutil export remove command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the member cluster name. |
| `-p` `storage_repos` | Specifies the location of the repository where the backing file is stored. |
| `-n` `export_name` | Specifies the export name. |
| `-f` | Forces removal whether or not export mapping is active. |
| `-b` | Removes the backing file for this mapping. |
| `-y` | Does not prompt when removing the backing file for cluster. |

`advmutil` `export` `remove` removes the configuration metadata of an export.

By default, the backing file remains after the removal operation. This file can be reused by running `advmutil` `export` `create` with the `-f` option. If the backing file is no longer required, then you can use the `-b` option to delete the backing file and return the storage space to the repository.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export remove

In the following example, the metadata for `export1` is removed.

```
#/sbin/advmutil export remove -c cluster1 -p /repository1 -n export1
```

### advmutil export resize

Purpose

Adds storage to the underlying backing file for an export.

Syntax and Description

```
advmutil export resize -h
advmutil export resize -c cluster_name -p storage_repos -n export_name -s file_size
```

The following table contains the options available with the `advmutil` `export` `resize` command.

Table: Options for the advmutil export resize command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the member cluster name. |
| `-p` `storage_repos` | Specifies the location of the repository where the backing file is stored. |
| `-n` `export_name` | Specifies the export name. |
| `-s` `file_size` | Specifies the file size in the format *n* {K\|M\|G\|T\|P\|E}. The units are K (Kilobytes), M (Megabytes), G (Gigabytes), T (Terabytes), P (Petabytes) or E (Exabytes). |

`advmutil` `export` `resize` adds storage to the underlying backing file for an export. After the backing file is grown, the device on the member cluster is also resized. To use the new size, an administrator must run `acfsutil` `size` on the member cluster mounted file system that is using the newly-sized device. Optionally, the new storage is used when needed if Oracle ACFS automatic resize functionality is configured on the mounted member cluster Oracle ACFS file system that is associated with this device.

To shrink a device, you must run `acfsutil` `size` on the member cluster to decrease the size of the file system. This action also shrinks the size of the associated backing file.

You can run `advmutil` `volinfo` on the member cluster to display the size of the underlying volume. However, this may be different than the size of the current Oracle ACFS file system that is using this device.

This command is only applicable to the Domain Services Cluster (DSC).

Example: Using advmutil export resize

In the following example, the size of the backing file for `export1` has been increased to 1 G.

```
#/sbin/advmutil export resize -c cluster1 -p /repository1 -n export1 -s 1G
```

### advmutil session list

Purpose

Lists the current state and description of Oracle ACFS remote service sessions on the Oracle Database member cluster.

Syntax and Description

```
advmutil session list -h
advmutil session list [-n node_name] [[-i transport_id] [-v]]
```

The following table contains the options available with the `advmutil` `session` `list` command.

Table: Options for the advmutil session list command

| Option | Description |
| --- | --- |
| `-n` `node_name` | Specifies the node name. |
| `-i` `transport_id` | Specifies the transport Id in the format `'` `transport_type` `.` `sequence_num` `'`. |
| `-v` | Displays verbose output, including XML data. |

`advmutil` `session` `list` lists the current state and description of Oracle ACFS remote service sessions on the Oracle Database member cluster. This list is useful for debugging and informational purposes.

In the output of the command, the possible state value are:

- `ONLINE`
	Oracle ACFS remote service transport session is currently up and configured.
- `REFRESH`
	Oracle ACFS remote service transport session, that is associated with the configured transport of `'` `transport_type` `.` `sequence_num` `'` on the DSC, is being refreshed. A refresh logs out of all existing targets and attempts to reinitialize the underlying operating system transport sessions associated with the Oracle ACFS remote service transport configuration.
- `RESCAN`
	Oracle ACFS remote service transport session is currently being scanned. The rescan process only removes operating system transport sessions that no longer exist, or adds new sessions that have been added. Existing sessions are not scanned.

The `advmutil` `session` `list` command only applies to the Oracle Database member cluster.

Example: Using advmutil session list

In the following example, session information is displayed for `Node1` and `Node2` on the member cluster.

```
#/sbin/advmutil session list
nodeName transportType sequenceNum state
-----------------------------------------
Node1    iSCSI                   0 ONLINE
Node2    iSCSI                   0 ONLINE
```

### advmutil transport create

Purpose

Creates a transport on the Domain Services Cluster (DSC).

Syntax and Description

```
advmutil transport create -h
advmutil transport create -c cluster_name [-b binding [-n network_num ] | [-i resource_id] [-f]
```

The following table contains the options available with the `advmutil` `transport` `create` command.

Table: Options for the advmutil transport create command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the member cluster name that the transport belongs to. |
| `-b` `binding` | Specifies the transport VIP, either the host name or the network address. |
| `-n` `network_num` | Specifies the network number for the specified VIP. The default is `1`. |
| `-i` `resource_id` | Specifies an existing alternate resource identifier. |
| `-f` | Forces the acceptance of the specified existing binding. |

`advmutil` `transport` `create` creates a transport on the Domain Services Cluster (DSC).

The cluster name can be discovered using the `crsctl` `query` `member_cluster_configuration` command. The transport VIP can be an IPv4 or IPv6 address, and can be either a resolvable DNS entry, or an IP address.

When creating a transport with additional features enabled, such as multipathing and failover, multiple transports must be enabled for a single member cluster. You can create multiple transports by running the `advmutil` `transport` `create` command multiple times, specifying additional VIP addresses.

Member clusters may share VIPs. You can accomplish this by specifying a common VIP name when registering a transport for a new member cluster. However, all member clusters must have the `advmutil` `transport` `create` command run at least once to specify their transport.

Transport IDs are created for each transport with the identifier of the form *cluster\_name\_transport\_type\_sequence#*, where *n* is an number starting from 0 and increased by 1 for each transport.

This command is only applicable on the Domain Services Cluster.

Example: Using advmutil transport create

In the following example, a transport is created for member cluster `cluster1` with VIP `havip1` using network `2`.

```
#/sbin/advmutil transport create -c cluster1 -b havip1 -n 2
```

### advmutil transport list

Purpose

Displays the configured transports on the system.

Syntax and Description

```
advmutil transport list [-h]
advmutil transport list [-c cluster_name [-i transport_id] [-v]] | [-g cluster_guid [-i transport_id [-v]]]
```

The following table contains the options available with the `advmutil` `transport` `list` command.

Table: Options for the advmutil transport list command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the member cluster name that the transport belongs to. |
| `-i` `transport_id` | Specifies the transport Id in the format `transport_type` `.` `sequence_num`. |
| `-g` `cluster_guid` | Specifies the cluster Globally Unique IDentifier (GUID). |
| `-v` | Specifies verbose output including XML data. |

`advmutil` `transport` `list` displays the configured transports on the system. The command can be configured to display information about specific clusters using the `-c` or `-g` options, as well as displaying the full configuration output.

This command is only applicable on the Domain Services Cluster.

Example: Using advmutil transport list

In the following example, the output shows a single iSCSI transport configured with sequence number `0`.

```
#/sbin/advmutil transport list
clusterName: cluster1 (clusterGUID: f403401d0518ffcfff54324f2cc2f6d8)
transportType sequenceNum
-----------------------------------------------------------
iSCSI                   0
```

Using the information in the output above, the sequence number (`0`) can be used on the member cluster to display information about a specific transport. Additionally, you can retrieve the full transport specification using the transport Id (`iSCSI.0`).

### advmutil transport remove

Purpose

Removes a transport.

Syntax and Description

```
advmutil transport remove [-h]
advmutil transport remove -c cluster_name -i transport_id
```

The following table contains the options available with the `advmutil` `transport` `remove` command.

Table: Options for the advmutil transport remove command

| Option | Description |
| --- | --- |
| `-c` `cluster_name` | Specifies the member cluster name that the transport belongs to. |
| `-i` `transport_id` | Specifies the transport Id in the format `transport_type` `.` `sequence_num`. |

`advmutil` `transport` `remove` removes a transport. This also removes any associated transport VIP resources if the transport is the last transport using this ID.

This command is only applicable on the Domain Services Cluster.

Example: Using advmutil transport remove

In the following example, the transport with transport Id `iSCSI.0` is removed from `cluster1`.

```
#/sbin/advmutil transport remove -c cluster1 -I iSCSI.0
```

## Oracle ACFS Command-Line Utilities

This topic provides a summary of the Oracle ACFS command-line utilities.

The Oracle ACFS command-line utility summary lists the Oracle ACFS command-line utilities with brief descriptions.

For information about running Oracle ACFS `acfsutil` commands, refer to About Using Oracle ACFS Command-Line Tools.

Table: Summary of Oracle ACFS command-line utilities

| Command | Description |
| --- | --- |
| acfsutil accel replace | Replaces an existing accelerator volume with a new one. |
| acfsutil compat get | Displays the compatibility level of an Oracle ACFS file system. |
| acfsutil compat set | Changes the compatibility level of an Oracle ACFS file system. |
| acfsutil defrag dir | Defragments all the files in a specified directory. |
| acfsutil defrag file | Defragments the specified files. |
| acfsutil freeze | Freezes modification activity temporarily in the file system. |
| acfsutil info file | Displays information for a file in an Oracle ACFS file system. |
| acfsutil info fs | Displays detailed Oracle ACFS file system information. |
| acfsutil info id | Displays Oracle ACFS file system information for a specified file identifier and mount point. |
| acfsutil info storage | Displays space usage for the Oracle ASM, Oracle ACFS, and Oracle ADVM components in Oracle ASM disk groups. |
| acfsutil plugin disable | Disables the Oracle ACFS plug-in infrastructure. |
| acfsutil plugin enable | Enables the Oracle ACFS plug-in infrastructure. |
| acfsutil plugin info | Displays information about the Oracle ACFS plug-in infrastructure. |
| acfsutil registry | Adds, deletes, or displays entries in the Oracle ACFS mount registry. |
| acfsutil rmfs | Removes an Oracle ACFS file system. |
| acfsutil scrub | Checks for and reports any inconsistencies in the metadata or file data. |
| acfsutil size | Resizes an Oracle ACFS file system. |
| acfsutil thaw | Resumes activity after an acfsutil freeze command has been issued on a file system. |
| acfsutil version | Displays Oracle ACFS version information. |
| advmutil canonical | Displays the canonical name of an Oracle ADVM volume. |
| advmutil volinfo | Displays information about Oracle ADVM volumes. |

### acfsutil accel replace

Purpose

Replaces an existing accelerator volume with a new one.

Syntax and Description

```
acfsutil accel replace -h
acfsutil accel replace -a new_accel_volume primary_volume
```

`acfsutil` `accel` `replace` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `accel` `replace` command.

Table: Options for the acfsutil accel replace command

| Option | Description |
| --- | --- |
| `-a` `new_accel_volume` | Specifies the name of the new accelerator volume. |
| `primary_volume` | Specifies the name of the primary volume with which the Oracle ACFS file system is mounted. |

This command allows an administrator to replace an existing accelerator volume with a new accelerator volume. The command is useful if the current accelerator volume is full and cannot be grown, or to migrate an accelerator to a faster volume.

The file system must be unmounted on all nodes to use this command. The new accelerator must be at least as large as the existing accelerator. If new accelerator volume is larger than the existing accelerator volume, then the administrator should run `acfsutil` `resize` `-d` `new_accel_volume` after the file system is remounted following the `acfsutil` `accel` `replace` operation to enable Oracle ACFS to utilize the entire space of the new accelerator volume.

You must be the `root` user or an Oracle ASM administrator user to run this command.

The following example shows the use of the `acfsutil` `accel` `replace` command.

Example: Using the acfsutil accel replace command

```
$ /sbin/acfsutil accel replace -a new_accelerator_volume my_primary_volume
```

### acfsutil compat get

Purpose

Displays the Oracle ACFS compatibility level for the file system and the `COMPATIBLE.ADVM` level for the disk group.

Syntax and Description

```
acfsutil compat get -h
acfsutil compat get mount_point
```

`acfsutil` `compat` `get` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `compat` `get` command.

Table: Options for the acfsutil compat get command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `compat` `get` command displays the Oracle ACFS compatibility level for the file system that may have been set by the `mkfs` command or the `acfsutil` `compat` `set` command. `acfsutil` `compat` `get` also displays the `COMPATIBLE.ADVM` setting for the disk group, which is default compatibility level for the file system if not otherwise explicitly set. For information about Oracle ASM disk group compatibility attributes, see [Disk Group Compatibility](administering-oracle-asm-disk-groups.md).

Examples

The following example shows the use of the `acfsutil` `compat` `get` command.

Example: Using the acfsutil compat get command

```
$ /sbin/acfsutil compat get /acfsmounts/acfs1
```

### acfsutil compat set

Purpose

Change the compatibility level of an Oracle ACFS file system.

Syntax and Description

```
acfsutil compat set -h
acfsutil compat set -c release_version mount_point
```

`acfsutil` `compat` `set` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `compat` `set` command.

Table: Options for the acfsutil compat set command

| Option | Description |
| --- | --- |
| `-c` `release_version` | Specifies the release version for the Oracle ACFS file system determined by \_mount *point*. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The value specified with the `-c` `release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `-c` `release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `-c` `release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. For information about Oracle ASM disk group compatibility attributes, see " [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) ".

The following example shows the use of the `acfsutil` `compat` `set` command.

Example: Using the acfsutil compat set command

```
$ /sbin/acfsutil compat set -c 12.2 /acfsmounts/acfs1
```

### acfsutil defrag dir

Purpose

Defragments all the files in a specified directory.

Syntax and Description

```
acfsutil defrag dir -h
acfsutil defrag dir [-r] dir_path
```

`acfsutil defrag dir` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil defrag dir` command.

Table: Options for the acfsutil defrag dir command

| Option | Description |
| --- | --- |
| `-r` | Specifies recursive defragment operation. |
| `dir_path` | Specifies the directory where the files to be defragmented are located. |

The `acfsutil defrag dir` command is used to defragment files in the specified subdirectory. The `-r` option is used to recursively defragment files in the subdirectories of the specified directory.

You must have write access to the files to be defragmented.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil defrag dir` command.

Example: Using the acfsutil defrag dir command

```
$ /sbin/acfsutil defrag dir /acfsmounts/critical_apps/01jan1015
```

### acfsutil defrag file

Purpose

Defragments the specified files.

Syntax and Description

```
acfsutil defrag file -h
acfsutil defrag file [-i] file_path [file_path ... ]
```

`acfsutil defrag file` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil defrag file` command.

Table: Options for the acfsutil defrag file command

| Option | Description |
| --- | --- |
| `-i` | Estimates the reduction in number of extents possible. Requires read access to the file. |
| `file_path` | Specifies the file to be defragmented. |

The `acfsutil defrag file` command defragments files. The `-i` option displays the estimated reduction in the number of extents for the files to be defragmented.

You must have write access to the files to be defragmented.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil defrag file` command.

Example: Using the acfsutil defrag file command

```
$ /sbin/acfsutil defrag file /acfsmounts/critical_apps/testfile
```

### acfsutil freeze

Purpose

Freezes modification activity temporarily in the file system.

Syntax and Description

```
acfsutil freeze -h
acfsutil freeze [-f] mount_point
```

`acfsutil` `freeze` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `freeze` command.

Table: Options for the acfsutil freeze command

| Option | Description |
| --- | --- |
| `-f` | Specifies the command to flush data to disk before freezing the file system. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `freeze` command temporarily halts modification activity on a file system. You can use `acfsutil` `freeze` to create point-in-time images across different snapshots without stopping applications. To resume activity after the `acfsutil` `freeze` command has been issued on a file system, run the `acfsutil` `thaw` command. For information about `acfsutil` `thaw`, refer to acfsutil thaw.

Use the `acfsutil` `freeze` command with caution to prevent application timeouts and possible instance evictions. If a database or database diagnostic area is running on an Oracle ACFS file system and the file system is frozen for more than three minutes, the database instance can be terminated due to processes that are hung while waiting to update files on the file system.

Using the `acfsutil` `freeze` command on a file system where Oracle ACFS replication is active may block replication operations if the operations modify on-disk replication configuration information or if the operations are updates to a frozen standby file system. Replication operations that are likely to be affected are:

- `acfsutil` `repl` `reverse` `standby`
- `acfsutil` `repl` `sync`
- `acfsutil` `repl` `terminate` `primary`
- `acfsutil` `repl` `terminate` `standby`

Examples

The following example shows the use of the `acfsutil` `freeze` command.

Example: Using the acfsutil freeze command

```
$ /sbin/acfsutil freeze -f /acfsmounts/acfs1
```

### acfsutil info file

Purpose

Displays information for a file in an Oracle ACFS file system.

Syntax and Description

```
acfsutil info file -h
acfsutil info file [ [-d] [-o acfs_extent_offset] [-m] [-u] | [-c] ] path [path ... ]
```

`acfsutil` `info` `file` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `info` `file` command.

Table: Options for the acfsutil info file command

| Option | Description |
| --- | --- |
| `-d` | Displays detailed extent information, from Oracle ACFS to the Oracle ASM devices in the disk group. |
| `-o` `acfs_extent_offset` | `acfs_extent_offset` - Filters the extent display to the Oracle ACFS file offset specified. |
| `-c` | Displays extent counts only. |
| `-m` | Displays details about file metadata extents. The `-m` option is compatible with `-d`, `-o`, and `-u`. The `-m` option is not compatible with `-c`. |
| `-u` | Displays extent usage information. |
| `path` | Specifies the full path name of a file. |

The `acfsutil` `info` `file` command displays information about a file in an Oracle ACFS file system. The information includes the extent map which details the locations of the blocks comprising the file and the used versus allocated storage for a file. Tagging information is also displayed for a file.

The `-u` option adds an additional column to the standard `acfsutil info file` output indicating whether or not the extent is inherited between a snapshot parent and child. The `-c` option displays the total extent count and the number of primary and accelerator volume extent nodes, while omitting the details of each individual extent. The output from the `-c` option is useful when you want to display the number of extents, and when using an accelerator, to ensure that the metadata is situated on the accelerator volume.

You must have read access to the specified file to run `acfsutil` `info` `file`.

Examples

The following is an example of the use of the `acfsutil` `info` `file` command.

Example: Using the acfsutil info file command

```
$ /sbin/acfsutil info file /usmmnt/.ACFS/snaps/s1/afile
  /usmmnt/.ACFS/snaps/s1/afile
    flags:        File
    inode:        18014398509482029
    owner:        root
    group:        root
    size:         13013  (  12.71 KB )
    allocated:    24576  (  24.00 KB )
    hardlinks:    1
    device index: 1
    major, minor: 202,64
    access time:  Thu Jan  7 14:13:24 2016
    modify time:  Thu Jan  7 14:13:24 2016
    change time:  Thu Jan  7 14:13:24 2016
    extents:
        -offset ----length | -dev --------offset
              0      24576 |    1      142188544
         extent count: 1
         granularity level: -1

$ /sbin/acfsutil info file -c /usmmnt/.ACFS/snaps/s1/afile
  /usmmnt/.ACFS/snaps/s1/afile
    flags:        File
    inode:        18014398509482029
    owner:        root
    group:        root
    size:         13013  (  12.71 KB )
    allocated:    24576  (  24.00 KB )
    hardlinks:    1
    device index: 1
    major, minor: 202,64
    access time:  Thu Jan  7 14:13:24 2016
    modify time:  Thu Jan  7 14:13:24 2016
    change time:  Thu Jan  7 14:13:24 2016
    extents:
         extent count: 1
         primary volume extent nodes:     0
         accelerator volume extent nodes: 0
         granularity level: -1

$ /sbin/acfsutil info file -u /usmmnt/.ACFS/snaps/s1/afile
  /usmmnt/.ACFS/snaps/s1/afile
    flags:        File
    inode:        18014398509482029
    owner:        root
    group:        root
    size:         13013  (  12.71 KB )
    allocated:    24576  (  24.00 KB )
    hardlinks:    1
    device index: 1
    major, minor: 202,64
    access time:  Thu Jan  7 14:13:24 2016
    modify time:  Thu Jan  7 14:13:24 2016
    change time:  Thu Jan  7 14:13:24 2016
    extents:
        -offset ----length | -dev --------offset | inherited
              0      24576 |    1      142188544 | Yes
         extent count: 1
         added extent count: 0
         inherited extent count: 1
         granularity level: -1
```

### acfsutil info fs

Purpose

Displays detailed Oracle ACFS file system information.

Syntax and Description

```
acfsutil info fs -h
acfsutil info fs [-l] [{-o option_item | -s [interval[count][-d]] | -f [-v]}]
  [mount_point]
```

`acfsutil` `info` `fs` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `info` `fs` command.

Table: Options for the acfsutil info fs command

| Option | Description |
| --- | --- |
| `-l` | Displays symbolic links for an Oracle ACFS file system specified by the mount point or displays symbolic links for all mounted Oracle ACFS file systems if a mount point is not specified. |
| `-o` | Displays the specific file system option item from the following list:  - `allvolumes [<span class="codeinlineitalic">mount_point</span> \| <span class="codeinlineitalic">primary_volume_device</span> \| <span class="codeinlineitalic">auxiliary_volume_device</span>]` - Lists all volumes that are associated with a file system. - `autoresize` - 1 if automatic resize is enabled, 0 if not. - `autoresizeincrement` - Lists the automatic resize increment for the file system. - `autoresizemax` - Lists the automatic resize maximum. - `auxvolume {<span class="codeinlineitalic">mount_point</span> \| <span class="codeinlineitalic">primary_volume_device</span>}` - Lists the auxiliary volumes associated with the file system. Can be run against a mount point or device. - `available` - Length of time the file system has been available. - `compatacfs` - Lists the ACFS compatibility setting - `compatadvm` - Lists the ADVM compatibility setting. - `diskgroup` - Name of the disk group associated with *path*. - `fetasize` - File entry table size which is the amount of storage consumed by the on disk metadata for inodes. - `freespace` - Amount of free space available in the file system. - `isadvm` - 1 if an Oracle ADVM volume is present, 0 if not. - `isauxvolume {<span class="codeinlineitalic">volume_device</span>}` - 1 if a volume is an auxiliary volume or 0 if not. Must be run against a volume device. - `isavailable` - 1 if the file system is available, 0 if file system is not available. - `iscompression` - State of compression on the file system. 1 for enabled, 0 for disabled. - `iscorrupt` - 1 if the file system is corrupt, 0 if file system is not corrupt. - `isencryption` - State of encryption on the file system, 0 for disabled, 1 for enabled. |
| `-o` (continued) | - `ismountpoint` - 1 if *path* is the mount point, 0 if *path* is not a mount point. - `isreplprimary` - 1 if primary file system, 0 if not. - `isreplstandby` - 1 if standby file system, 0 if not. - `issecurity` - State of security on the file system, 0 for disabled, 1 for enabled. - `metablocksize` - Size of metadata blocks on the file system. - `mountpoints` - Mount points associated with file systems. - `primaryvolume` - Path name of the device associated with file system. - `redundancy` - Type of redundancy used by the Oracle ADVM volume. - `replication` - 1 if file system has been initialized for replication as the primary or standby file system, 0 if not initialized for replication. - `resizeincrement` - Allocation unit size in bytes of the Oracle ADVM volume used by *path*. - `stripewidth` - Stripe width for the Oracle ADVM volume used by *path*. - `stripecolumns` - Stripe set columns for the Oracle ADVM volume used by *path*. - `totalspace` - Size of the file system. - `volumes` - Number of volumes associated with the file system. |
| `-s` \[ `interval` \[ `count` \] \[ `-d]` \] | Displays file system statistics.  The optional *interval* parameter specifies the amount of time in seconds between each report. The first report contains statistics for the time since the file system mount. Each subsequent report contains statistics collected during the interval since the previous report.  The optional *count* parameter can be specified with the *interval* parameter. If the *count* parameter is specified, the value of count determines the number of reports generated at interval seconds apart.  If the *interval* parameter is specified without the *count* parameter, the command generates reports continuously until you break out of the command with `Ctrl+c`.  The optional `-d` option displays more detailed statistical information. |
| `-f` \[ `-v` \] | Displays file system fragmentation. The `-v` option displays additional fragmentation information. |
| `mount_point` | Specifies the directory where the file system is mounted. Not a valid option for replication data. |

`acfsutil` `info` `fs` displays information and statistics about Oracle ACFS file systems. If compression, encryption, security, or replication has been initiated on a file system, additional flags and status information are displayed.

The `-o` *option\_item* option displays file system information for the *option\_item* specified.

The `-s` option displays the amount and rate of change currently on a file system for the node that the command is run on.

With no option specified, the command displays file system information that includes the volume device name, the size of the file system, the amount of space available on the volume device, the file system mount time on this node, the state of the file system, the user specified block size, the number of Oracle ACFS snapshots, the space consumed by snapshots in the file system, and the optional name or volume label associated with the file system. The possible file system states are displayed in the `flags` line. These states include:

- `Offline` indicates that the underlying devices are not accessible, possibly due to an Oracle ASM instance failure, disk group forced dismount, or an irrecoverable I/O error. The file system on this node can only be dismounted. All other attempts at access result in errors.
- `Available` indicates that the file system is on line and operational.
- `Corrupt` indicates that the file system should be checked and repaired at the earliest possible convenience to correct a detected inconsistency. For example, run the `fsck` command on Linux or the `acfschkdsk` command on Windows to check and repair the file system. Ensure that you run the command in repair mode to correct the problem. For more information, refer to " fsck (offline mode) " and " acfschkdsk ".

When viewing space usage values with `acfsutil` `info` `fs` on Windows systems, the values may differ from sizes in Windows folders. The mechanism used by **Folder** **Properties** on Windows systems only accounts for files and should be considered an approximate value.

Any user can run `acfsutil` `info` `fs`.

Examples

The following are examples of the use of `acfsutil` `info` `fs`.

The following example displays information about an Oracle ACFS file system in a Linux environment.

Example: Using the acfsutil info fs command on Linux

```
$ /sbin/acfsutil info fs
/primary
    ACFS Version: 11.2.0.2.0
    flags:        MountPoint,Available,Replication
    mount time:   Mon Oct 25 12:11:03 2010
    volumes:      1
    total size:   5368709120
    total free:   4144230400
    primary volume: /dev/asm/pvol-74
        label:
        flags:                 Primary,Available,ADVM
        on-disk version:       40.0
        allocation unit:       4096
        major, minor:          252, 37889
        size:                  5368709120
        free:                  4144230400
        ADVM diskgroup         REPLDG
        ADVM resize increment: 268435456
        ADVM redundancy:       unprotected
        ADVM stripe columns:   4
        ADVM stripe width:     131072
    number of snapshots:  0
    snapshot space usage: 0
    replication status: primary

/standby
    ACFS Version: 11.2.0.2.0
    flags:        MountPoint,Available,Replication
    mount time:   Mon Oct 25 12:11:03 2010
    volumes:      1
    total size:   5368709120
    total free:   5263945728
    primary volume: /dev/asm/svol-74
        label:
        flags:                 Primary,Available,ADVM
        on-disk version:       40.0
        allocation unit:       4096
        major, minor:          252, 37890
        size:                  5368709120
        free:                  5263945728
        ADVM diskgroup         REPLDG
        ADVM resize increment: 268435456
        ADVM redundancy:       unprotected
        ADVM stripe columns:   4
        ADVM stripe width:     131072
    number of snapshots:  0
    snapshot space usage: 0
    replication status: standby

$ /sbin/acfsutil info fs -o mountpoints,replication
/primary
1
/standby
1

$ /sbin/acfsutil info fs -o mountpoints,isreplprimary
/primary
1
/standby
0

$ /sbin/acfsutil info fs -o mountpoints,isreplstandby
/primary
0
/standby
1
```

The following example illustrates the use of `acfsutil` `info` `fs` in a Windows environment.

Example: Using the acfsutil info fs command on Windows

```
C:\oracle>acfsutil info fs /o freespace c:\oracle\acfsmounts\acfs1
968667136

C:\oracle>acfsutil info fs /o totalspace c:\oracle\acfsmounts\acfs1
1073741824

C:\oracle>acfsutil info fs /o volumes c:\oracle\acfsmounts\acfs1
1

C:\oracle>acfsutil info fs /o primaryvolume c:\oracle\acfsmounts\acfs1
asm-volume1-311

C:\oracle>acfsutil info fs /o diskgroup c:\oracle\acfsmounts\acfs1
DATA

C:\oracle>acfsutil info fs /o redundancy c:\oracle\acfsmounts\acfs1
mirror
```

The following example illustrates the use of `acfsutil` `info` `fs` with `-s` option to display the current amount and rate of change on a file system.

Example: Using the acfsutil info fs command with the -s option

```
$ /sbin/acfsutil info fs -s /acfsmounts/acfs1
    amount of change since mount:       359.22 MB
    average rate of change since mount: 3 KB

$ /sbin/acfsutil info fs -s 60 4 /acfsmounts/acfs1
    amount of change since mount:       359.22 MB
    average rate of change since mount: 3 KB/s

    amount of change: 15.02 MB   rate of change: 256 KB/s
    amount of change: 9.46 MB   rate of change: 161 KB/s
    amount of change: 7.32 MB   rate of change: 125 KB/s
    amount of change: 6.89 MB   rate of change: 117 KB/s
...
```

### acfsutil info id

Purpose

Displays Oracle ACFS file system information for a specified file identifier number and mount point.

Syntax and Description

```
acfsutil info id -h
acfsutil info id file_identifier mount_point
```

`acfsutil` `info` `id` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `info` `id` command.

Table: Options for the acfsutil info id command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |
| `file_identifier` | Specifies the Oracle ACFS file identifier number reported by the Oracle ACFS driver. The file identifier number should be specified in decimal format. |

You can use `acfsutil` `info` `id` to translate an internal numeric Oracle ACFS file identifier to a path name in the file system. This is useful when the Oracle ACFS driver reports I/O errors to the system event logger associated with a particular file in an Oracle ACFS and identifies it by its internal identifier. You must have administrator privileges or you must be a member of the Oracle ASM administrator group to run `acfsutil` `info` `id`.

Examples

The following is an example of `acfsutil` `info` `id`.

Example: Using the acfsutil info id command

```
$ /sbin/acfsutil info id 117 /acfsmounts/acfs1
```

### acfsutil info storage

Purpose

Displays space usage for the Oracle ASM, Oracle ACFS, and Oracle ADVM components in Oracle ASM disk groups.

Syntax and Description

```
acfsutil info storage -h
acfsutil info storage [-u {B|MB|GB|TB}] [-l] [disk_group,...]
```

`acfsutil` `info` `storage` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `info` `storage` command.

Table: Options for the acfsutil info storage command

| Option | Description |
| --- | --- |
| `-u`  { `B` \| `MB` \| `GB` \| `TB` } | Specifies the unit of measurement.  Specifies that the space usage values are in units of `B` (kilobytes), `MB` (megabytes), `GB` (gigabytes), or `TB` (terabytes). |
| `-l` | Displays more detailed space information for the Oracle ASM disk group, the Oracle ADVM volume, and the Oracle ACFS file system. |
| `disk_group` | Specifies the disk group or disk groups for which space usage is displayed. If a disk group is not specified, then information for all disk groups is displayed. |

`acfsutil` `info` `storage` provides a platform independent way to view how the space in an Oracle ASM disk group is being consumed by components of Oracle ASM, Oracle ACFS, and Oracle ADVM.

This command gathers the space information from multiple sources, including `V$ASM_DISKGROUP`, `V$ASM_FILE`, `acfsutil` `snap` `info`, and `acfsutil` `info` `fs`. Each line in the summary output displays the primary Oracle ACFS consumers of storage in a disk group.

For each disk group, all information for that disk group is grouped together. The `%` `Free` column is calculated using the `Space` and the `Usable` `Free` columns. For `NORMAL` and `HIGH` redundancy disk groups, the `Usable` `Free` column displays the unused portion of the disk group after accounting for mirroring. For `FLEX` or `EXTENDED` disk group, the `Usable` `Free` column reports the raw total free space as the redundancy is flexible and can vary.

The `Consumer` and `Path` columns are always empty on the line that displays information for the disk group. The `Consumer` column is populated on the lines for the consumers of storage in the disk group.

If a volume is enabled, then the volume name is displayed in the `Consumer` column. The `Space` column displays the current size of the volume. The `Usable` `Free` column displays the amount of free space in the file system if the volume is part of an Oracle ACFS file system or part of a mounted non-Oracle ACFS file system. The `Path` column displays the mount point if the volume is part of a mounted file system. The `Path` column displays `*ACFS` if the volume is part of an unmounted Oracle ACFS file system.

If a snapshot exists in the Oracle ACFS file system associated with the previously listed volume, then the snapshot name is displayed on the next line in the `Consumer` column. The `Space` column associated with a snapshot is always marked with an asterisk (`*`) because the space used by a snapshot in the file system has been accounted for in the volume line. The `Size` `With` `Mirroing` column associated with a snapshot represents the space currently being used by that snapshot in the file system. If a snapshot quota has been established, then the `Usable` `Free` column displays the amount of free space left before for that snapshot reaches the quota. If a snapshot quota has not been set, then this column is empty. The `Path` column for a snapshot is a full path to the root of the snapshot. If a snapshot link has been established, then the snapshot link is displayed in the `Path` column.

`root` or users who are members of the `asmadmin` group can run this command. For information about operating system group privileges, see [About Privileges for Oracle ASM](administering-oracle-asm-instances.md).

Examples

The following example shows the use of `acfsutil` `info` `storage` to display space usage information in both summary and long format.

Example: Using the acfsutil info storage command

```
$ /sbin/acfsutil info storage -u MB
Diskgroup      Consumer      Space     Size With Mirroring  Usable Free  %Free   Path
DATA                       4608.00            2304.00         895.00       38%
                   VOL1    2048.00            1024.00         831.45       81%   /acfsmnt
                 052317          *               0.25                            /acfsmnt/latest
                 052217          *             131.26         893.00       87%   /acfsmnt/.ACFS/snaps/052217
FLASH                      2048.00            1024.00         147.00       14%
              ACCELVOL1    1024.00             512.00         260.92       50%   ACCEL for VOL1 in DATA
TST                        2048.00            1024.00         143.00       13%
                   VOL1    1024.00             512.00         512.00      100%
----
unit of measurement: MB
```
```
$ /sbin/acfsutil info storage -l

Diskgroup: DATA (38% free)
  total disk space:           4.50
  ASM file space:             2.05
  total free space:           2.25
  net free with mirroring:    1.12
  usable after reservation:   0.87
  redundancy type:          NORMAL

    Total space used by ASM non-volume files:
      used:                      0.00
      mirror used:               0.00

    volume: /dev/asm/vol1-447
      total:                     1.00
      free:                      0.81
      redundancy type:         mirror
      file system:             /acfsmnt
        snapshot: 052317 (/acfsmnt/latest)
          used:          0.00
          quota limit:   none
        snapshot: 052217 (/acfsmnt/.ACFS/snaps/052217)
          used:          0.13
          quota limit:   1.00

...

----
unit of measurement: GB
```

### acfsutil plugin disable

Purpose

Disables the Oracle ACFS plug-in infrastructure for an Oracle ACFS file system.

Syntax and Description

```
acfsutil plugin disable -h
acfsutil plugin disable mount_point
```

`acfsutil` `plugin` `disable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `plugin` `disable` command.

Table: Options for the acfsutil plugin disable command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `plugin` `disable` disables the collection of Oracle ACFS plug-in metrics and the associated communication with a plug-in application.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `plugin` `disable` command. After monitoring has completed for the Oracle ACFS file metric data for the file system mounted on the `/humanresources`, the command in this example disables the subsequent collection of summary data in the Oracle ACFS driver.

Example: Disabling the Oracle ACFS driver

```
# /sbin/acfsutil plugin disable /humanresource
```

See also

- About Using Oracle ACFS Command-Line Tools for information about running Oracle ACFS `acfsutil` commands
- [Oracle ACFS Plugins](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS plug-ins
- [Oracle ACFS Plug-in Generic Application Programming Interface](understanding-oracle-acfs-advanced-topics.md) for information about the Oracle ACFS plug-in application programming interface

### acfsutil plugin enable

Purpose

Enables the Oracle ACFS plug-in infrastructure for an Oracle ACFS file system.

Syntax and Description

```
acfsutil plugin enable -h
acfsutil plugin enable -m metrictype [-t tag, ...]
  [-i interval[s|m]] mount_point
```

`acfsutil` `plugin` `enable` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `plugin` `enable` command.

Table: Options for the acfsutil plugin enable command

| Option | Description |
| --- | --- |
| `-t` `tag`,... | An optional list of tag names selecting Oracle ACFS files that you want to be monitored. The maximum number of tags is 12. The names are separated by commas. The default is to monitor all files in the Oracle ACFS file system.  The tag names are managed by the Oracle ACFS tagging APIs. |
| `-m` `metrictype` | Selects the message payload to be transmitted from Oracle ACFS to the plug-in module with each call-out message. Oracle ACFS provides the `acfsmetric1` and `acfsmetric2` pre-defined metric types. |
| `-i` `interval` \[ `s` \| `m` \] | Selects posting message delivery and the posting interval. The Oracle ACFS plug-in mechanism posts a metrics message during each specified message interval.  An interval is the maximum amount of time which can pass before metrics are posted. The application blocks in the API call to retrieve metrics until a posting occurs.  The interval can be specified as an integer value in `s` seconds or `m` minutes. The default is minutes. The maximum value allowed for an interval is 60 minutes or 3600 seconds.  If an interval is specified, then Oracle ACFS is requested to post metrics messages to the plug-in application on an interval basis.  If an interval is not specified, then the application polls for metrics updates from the Oracle ACFS file system. This is the default action. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `plugin` `enable` enables an Oracle ACFS file system for application plug-in service. Oracle ACFS plug-ins are enabled for single nodes only, either a standalone host or one or more individual nodes of a Grid Cluster. After enabled for plug-ins, the Oracle ACFS file system begins collecting metric information for either the set of specified tagged files or all files in the Oracle ACFS file system, and transmits callout messages to the plug-in application based upon the selected message payload and delivery parameters. Metrics are reset after every delivery to the application (whether through polling or posting).

In general, metrics are collected from the point of view of a user application. I/O for metadata or internal Oracle ACFS activities; such as snapshot copy-on-writing, encrypting, and replicating files; are not included. Metrics are collected for user I/O to both files in the original file system and snapshot files. Memory mapping of files that results in I/O operations is recorded in the metrics. Replication related files under the `.ACFS/repl` directory are not included in the metrics.

Oracle ACFS provides the `acfsmetric1` and `acfsmetric2` pre-defined metric types.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `plugin` `enable` command to provide additional storage usage metrics to a monitoring application.

Example: Enabling the Oracle ACFS driver for storage visibility: poll model

```
# /sbin/acfsutil plugin enable -m acfsmetric1 -t HRDATA /humanresource
```

An Oracle ACFS file system mounted on `/humanresources` is to be enabled for plug-in service and configured with the objective of providing additional storage usage metrics to a monitoring application. The message payload type is `acfsmetric1`, the files to be monitored are human resource files that have been tagged with the Oracle ACFS file tag `HRDATA`, and the message delivery type is `poll` which means that the application plug-in polls to request metric data update messages. No interval is specified with polled message delivery.

When this command completes, the Oracle ACFS file system mounted on the `/humanresources` mount point is enabled for plug-in communication and begins collecting Oracle ACFS file access metrics for files tagged with `HRDATA`. Oracle ACFS maintains metrics collecting a summary of read and write activity. Each time the associated application plug-in module polls for the metrics, Oracle ACFS sends a message with the data as defined in the `ACFS_METRIC1` structure that is a summary of the selected Oracle ACFS activity since either the Oracle ACFS driver plug-in functionality was enabled or since the last delivery of metric data.

The following example shows the use of the `acfsutil` `plugin` `enable` command to monitor movie file updates.

Example: Enabling the Oracle ACFS driver for storage visibility: post on interval model

```
# /sbin/acfsutil plugin enable -m acfsmetric1 -t FILECONTENT -i 120s /moviemods
```

An Oracle ACFS file system mounted on `/moviemods` is enabled for plug-in service and is configured to record and deliver storage usage messages to a monitoring application. On an interval basis, the Oracle ACFS file system sends a wakeup on a driver event on which the application API call is waiting. The application then collects a summary of read and write activity on the files.

The message payload type is `acfsmetric1` and the files to be monitored are movie files that have been tagged with the `FILECONTENT` tag. The message delivery type is `post`, which means that Oracle ACFS posts messages containing the metrics to the plug-in application for the specified interval of 120 seconds.

When this command completes, the Oracle ACFS file system mounted on the `/moviemods` mount point is enabled for plug-in communication and begins collecting Oracle ACFS storage visibility metrics for files tagged with `FILECONTENT`. On each interval, Oracle ACFS posts one or more messages to the application plug-in containing the storage visibility information.

See also

- About Using Oracle ACFS Command-Line Tools for information about running Oracle ACFS `acfsutil` commands
- [Oracle ACFS Plugins](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS plug-ins
- [Oracle ACFS Pre-defined Metric Types](understanding-oracle-acfs-advanced-topics.md) for information about the pre-defined metric types
- [Oracle ACFS Plug-in Generic Application Programming Interface](understanding-oracle-acfs-advanced-topics.md) for information about the Oracle ACFS plug-in application programming interface
- [Oracle ACFS Tagging Generic Application Programming Interface](understanding-oracle-acfs-advanced-topics.md) for information about the Oracle ACFS tagging application programming interface

### acfsutil plugin info

Purpose

Displays information about the Oracle ACFS plug-in infrastructure for an Oracle ACFS file system.

Syntax and Description

```
acfsutil plugin info -h
acfsutil plugin info mount_point
```

`acfsutil` `plugin` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `plugin` `info` command.

Table: Options for the acfsutil plugin info command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `plugin` `info` displays information about the state of the Oracle ACFS plug-in mechanism.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

The following example shows the use of the `acfsutil` `plugin` `info` command.

Example: Displaying information about the Oracle ACFS driver

```
# /sbin/acfsutil plugin info /humanresource

Plug-in status: ENABLED
Metric type: acfsmetric1
Enabled tags: HRDATA
Delivery method: Poll
Post interval (seconds):

# /sbin/acfsutil plugin info /moviemods

Plug-in status: ENABLED
Metric type: acfsmetric1
Enabled tags: FILECONTENT
Delivery method: Post
Post interval (seconds): 120
```

See also

- About Using Oracle ACFS Command-Line Tools for information about running Oracle ACFS `acfsutil` commands
- [Oracle ACFS Plugins](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS plug-ins
- [Oracle ACFS Plug-in Generic Application Programming Interface](understanding-oracle-acfs-advanced-topics.md) for information about the Oracle ACFS plug-in application programming interface

### acfsutil registry

Purpose

Adds, deletes, or displays entries in the Oracle ACFS mount registry.

Syntax and Description

```
acfsutil registry -h
acfsutil registry
acfsutil registry -a [-f] [-o moptions] [-n { nodes|all } ]
  [-u user] [-t description] device mount_point
acfsutil registry -c  {device | mount_point} [-o moptions]
  [-n { nodes|all } ] [-u user] [-t description]
acfsutil registry -d {device | mount_point}
acfsutil registry -l [device | mount_point]
acfsutil registry -m deviceacfsutil registry -r
```

`acfsutil` `registry` `-h` displays help text and exits.

If no options are specified, the command displays all the Oracle ACFS file systems that are configured for automatic start.

The following table contains the options available with the `acfsutil` `registry` command.

Table: Options for the acfsutil registry command

| Option | Description |
| --- | --- |
| `-a` | Add the device, mount point, and associated *moptions* to the Oracle ACFS mount registry. The Oracle ADVM volume device specified must exist on the local node to add the information to the mount registry.  The arguments represent all the information needed to mount the file system. At Oracle ACFS startup time these file systems are automatically mounted.  Duplicate device entries are not allowed. Duplicate mount points are allowed but must be include the `-n` option for disjoint node-specific mounts. |
| `-c` | Changes an existing registry entry for the specified device or mount point. |
| `-d` | Deletes the specified device or mount point from the Oracle ACFS mount registry. If a mount point is specified and it is not unique in the Oracle ACFS mount registry, the command fails and you must run the command again specifying the device. |
| `-f` | This option is used in combination with `-a` when the specified device might exist in the registry and the administrator wants to replace the registration. |
| `-l` \[ `device` \| `mount_point` \] | Without specifying a device or mount point, the `-l` option lists all the file systems currently in the registry on a single line, with fields separated by a colon ( `:` ). With a device specified, lists information about the device in the Oracle ACFS registry. With a mount point specified, lists information about the mount point in the Oracle ACFS registry. |
| `-m` `device` | Lists the registered mount point, if one exists, associated with the specified device. The mount point is only returned if the Oracle ACFS file system has been registered or has been previously mounted. |
| `-n` { `nodes` \| `all` } | This option, used in combination with `-a` and `-c`, specifies an optional comma-delimited list of nodes, or the `all` keyword. This specifies which nodes should attempt to mount this device on the specified mount point. Host names should be specified. The `all` keyword is functionally equivalent to not specifying a list of nodes and indicates that the device should be mounted on all nodes. Mounting on all nodes is the default behavior. |
| `-o` `moptions` | Specifies the mount options for use when mounting the file system. Valid for Linux, Solaris, and AIX. Used in combination with `-a` and `-c`. For specific `-o` `moptions`, refer to the `mount` command for each operating system. All the options for each operating system are available except the `all` option. |
| `-r` | Displays all registered file systems, not just file systems with `auto_start=always`. |
| `-t` `description` | Adds a description of the mount. Used in combination with `-a` and `-c`. For example: `-t` `"HR Exports share"`. This description can be seen later when looking at configured resources. |
| `-u` `user` | Specifies a user that is allowed to mount or umount (start and stop) the file system. This option, used in combination with `-a` and `-c`, is useful for creating a registered file system that can be started or stopped by someone other than root. |
| `mount_point` | Specifies the directory where the file system is mounted. |
| `device` | Specifies an Oracle ACFS device file that has been formatted. |

`acfsutil` `registry` adds, deletes, or displays a file system from the Oracle ACFS persistent mount registry. The mount registry is a global registry that is used at Oracle ACFS startup on each node to mount all file systems specified in it. `root` or `asmadmin` privileges are required to modify the registry. For information about operating system group privileges, see " [About Privileges for Oracle ASM](administering-oracle-asm-instances.md) ".

Any user is allowed to display the contents of the registry. To mount all the file systems in the Oracle ACFS mount registry, use the platform specific mount command with the `all` option. This is done automatically at Oracle ACFS startup on each node.

Note:

Oracle ACFS registration (`acfsutil` `registry`) is not supported in an Oracle Restart (standalone) configuration, which is a single-instance (non-clustered) environment.

See " [About the Oracle ACFS Mount Registry](introducing-oracle-acfs-and-oracle-advm.md) ".

Examples

The following examples show the use of `acfsutil` `registry`. The first example shows how to add the volume device file and file system mount point to the registry. The second example shows how to list the registered mount point associated with the specified volume device file. The third example shows how to delete the specified volume device file from the registry.

Example: Using the acfsutil registry command

```
$ /sbin/acfsutil registry -a /dev/asm/volume1-123 /acfsmounts/acfs1

$ /sbin/acfsutil registry -m /dev/asm/volume1-123

$ /sbin/acfsutil registry -d /dev/asm/volume1-123
```

### acfsutil rmfs

Purpose

Removes an Oracle ACFS file system.

Syntax and Description

```
acfsutil rmfs -h
acfsutil rmfs device
acfsutil rmfs device -b
```

`acfsutil` `rmfs` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `rmfs` command.

Table: Options for the acfsutil rmfs command

| Option | Description |
| --- | --- |
| `device` | Specifies an Oracle ACFS device file that has been formatted. |
| `-b` | Specifies batch mode. No user interaction is required. |

You can use `acfsutil` `rmfs` to remove an Oracle ACFS that is dismounted. When the command is run, the superblock of the file system is disabled. `root` or `asmadmin` privileges are required to run this command. For information about operating system group privileges, see " [About Privileges for Oracle ASM](administering-oracle-asm-instances.md) ".

After `acfsutil` `rmfs` runs successfully, the `MOUNTPATH` and `USAGE` columns in the `V$ASM_VOLUME` view are cleared for the device. The removed Oracle ACFS can be restored using `fsck` or `acfschkdsk`. The device can be reformatted with a new Oracle ACFS using the `mkfs` or `acfsformat` commands.

Examples

The following example shows the use of `acfsutil` `rmfs` to remove the specified volume device file and associated file system.

Example: Using the acfsutil rmfs command

```
$ /sbin/acfsutil rmfs /dev/asm/volume1-123
```

### acfsutil scrub

Purpose

Checks for and reports any inconsistencies in the metadata or file data.

Syntax and Description

```
acfsutil scrub [-h] [-n] [-m] [-q] [-e number] [-b ext1[,...]] [-z] [-a] [-p level]
  [-t level] {file | directory}
```

`acfsutil` `-h` `scrub` displays help text and exits.

The following table contains the options available with the `acfsutil` `scrub` command.

Table: Options for the acfsutil scrub command

| Option | Description |
| --- | --- |
| `-n` | Specifies not to scrub the directory recursively. |
| `-m` | Specifies to scrub the metadata only. |
| `-q` | Specifies quiet mode. Only report inconsistencies to STDOUT. |
| `-e` `number` | Specifies the number of inconsistencies encountered before program terminates. |
| `-b` `ext1,ext2, ...` | Specifies not to scrub files with the specified extensions. |
| `-z` | Specifies not to scrub the Oracle ACFS snapshot directory. |
| `-a` | Specifies to scrub extensions skipped by default ( `.dbf`, `.arc` ). |
| `-p` `level` | Specifies I/O load level, from `0` (lowest) to `6` (highest). |
| `-t` `level` | Specifies trace level verbosity, from `0` (terse) to `6` (verbose). |
| `file` | Specifies the full path name of a file. |
| `directory` | Specifies the full path name of a directory. |

On Linux and AIX systems, the `acfsutil` `scrub` command checks the mirror consistency of Oracle ACFS directory metadata and file user data and metadata.

For paths with metadata inconsistencies, the scrubber displays the inconsistent path.

For file paths with user data inconsistencies, the scrubber provides the following information:

- Pathname
- Byte offset of inconsistency
- Byte length of inconsistency
- ADVM volume byte offset of inconsistency

You must have `root` privileges to run `acfsutil` `scrub`.

Examples

The following example illustrates the use of the `acfsutil` `scrub` command. The first command scrubs only the metadata of the specified file. The second command scrubs the specified directory and all nested files, except for snapshots, `txt` files, and `pdf` files. The third command scrubs the specified directory and all nested files with the power level set to `5` and trace level set to `3`.

Example: Using the Oracle ACFS acfsutil scrub command

```
$ /sbin/acfsutil scrub -m /acfsmnt/textdoc1.txt

$ /sbin/acfsutil scrub -b txt,pdf -z /acfsmnt/dir1

$ /sbin/acfsutil scrub -p 5 -t 3 /acfsmnt/dir1
```

### acfsutil size

Purpose

Resizes an Oracle ACFS file system.

Syntax and Description

```
acfsutil size -h
acfsutil size {[[+|-]n[K|M|G|T|P]] [-d volume_device] [-q]} |
  {[-a n[K|M|G|T] ] [-x n[K|M|G|T] ]} mount_point
```

`acfsutil` `size` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `size` command.

Table: Options for the acfsutil size command

| Option | Description |
| --- | --- |
| \[`+` \| `-`\] *n*  `K` \| `M` \| `G` \| `T` \| `P` | Specifies the new size for the Oracle ACFS file system where *n* is a valid positive whole number greater than zero. The number can be preceded by a `+` or - to indicate the amount to add or decrease. If no operand exists, the new size is the absolute size.  Specifies that the integer supplied for size is in the units of `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), `T` (Terabytes), or `P` (Petabytes). If the unit indicator is specified, then it must be appended to the integer. If omitted, the default unit is bytes. |
| `-q` | Provides an estimate of how much data may need to be moved to complete the command. |
| `-a` `n` | Specifies the increment by which an automatic resize increases the file system when the amount of free space falls below the amount specified by the increment. A nonnegative numeric value must be provided, and may optionally be followed by `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), or `T` (Terabytes) to specify a value in kilobytes, megabytes, gigabytes, or terabytes. If the unit is omitted, the default is bytes. A value of 0 disables automatic resize. The minimum allowed increment is 1G. |
| `-x` `n` | Specifies the maximum size to which a file system automatically resizes. A nonnegative numeric value must be provided, and may optionally be followed by `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), or `T` (Terabytes) to specify a value in kilobytes, megabytes, gigabytes, or terabytes. If the unit is omitted, the default is bytes. If this value is less than the current size of the file system then no error is returned, but automatic resize does not take place until the file system is shrunk (by manual action of the system administrator) below this value. A value of 0 indicates that no maximum size is configured, so the file system may continue to automatic resize until the underlying volume is out of space. |
| `-d` `volume_device` | Resizes only the specified device. |
| `mount_point` | Specifies the directory where the file system is mounted |

At least one of the `+` or `-`, `-a`, or `-x` options must be specified.

The size value is rounded up based on the block size of the file system and the allocation unit of the Oracle ADVM volume device file. To determine the Oracle ADVM volume device resize increment, examine the `RESIZE_UNIT_MB` field in the `V$ASM_VOLUME` view, `Resize` `Unit` in the output of `asmcmd` `volinfo`, or `ADVM` `resize` `increment` in the output of `acfsutil` `info` `fs`.

Before issuing an `acfsutil` `size` command to grow or shrink a file system, you can issue `acfsutil` `size` `-q` to report how much data may be needed to be moved to complete the command. This estimation can be helpful in predicting how long the command may take to complete. Using the `-q` option does not cause any resizing of the file system.

There is no limit to the number of times a file system can be expanded for a disk group with the ADVM compatibility attribute set to `11.2.0.4` or higher.

For a disk group with the ADVM compatibility attribute set to less than `11.2.0.4`, there is a limit of 5 extents for the file system's internal storage bitmap. This causes any attempts to increase the file system to fail after it has been increased four or more times. However, if after increasing the file system four times or more times the file system size is decreased, then you may be able to increase the file system size again if the size of the increase is less than the size of the decrease. When the limit on a file system expansion has been reached, running `fsck` or `acfschkdsk` with the `-a` option may consolidate the internal storage bitmap, allowing future file system expansion.

`root` or users who are members of the `asmadmin` group can run this command. For information about operating system group privileges, see [About Privileges for Oracle ASM](administering-oracle-asm-instances.md).

Manual Resize Option

The `+` or `-` option grows or shrinks the mounted Oracle ACFS and its underlying Oracle ADVM storage to match the new size specified. This operation also resizes the underlying Oracle ADVM volume file to match the new length that is specified. However, the disk group must have enough free storage to accommodate any requested increase to the file system size.

You can use `acfsutil` `size` to extend or shrink an entire file system or only a specified device.

Reducing a file system size returns unused storage space located at the end of the file system to the disk group.

Prior to Oracle ASM release 18c, the shrinking operation would only succeed if the operation did not require existing files in the file system to be moved. For Oracle ASM release 18c, the shrink process moves files as necessary when shrinking the file system. This process of moving files can be time consuming. In addition, a subsequent command to grow the file system may also need to move data, which may be time-consuming.

Note:

- An attempt to extend or shrink the file system may partially succeed, resulting in the file system having a larger or smaller size than before the `acfsutil` `size` command was issued. However, because of errors or environmental changes, the new size may not be the requested size. If a grow or shrink operation fails on a node for any reason, an error message is written to the `USM` event log and the `OKS` log.
- A shrink of the accelerator volume does not cause the migration of metadata from the accelerator volume to the primary volume. The process fails if there is too much data on the accelerator.
- A shrink command moves files out of the area of the volume that is to be removed and into a different part of the volume. This moving of files could change the fragmentation of these files. It could result in their becoming more fragmented than they were prior to the file system shrink operation. It could also result in their becoming less fragmented.

Automatic Resize Option

The automatic resize option (`-a` option) specifies an increment by which an Oracle ACFS file system grows automatically if the amount of available free space in the file system falls below the amount specified by the increment. You can also specify the maximum size (`-x` option) allowed when using the automatic resize option. The output of the `acfsutil info fs` command displays the automatic resize increment and maximum amounts. If only the `-x` option is provided without the `-a` option (and no automatic resize increment has previously been specified) then a warning is issued if the increment is still zero. If the increment had previously been set by an earlier invocation of the command, then the command succeeds. Automatic resize requires ADVM compatibility attribute set to `12.2` or higher.

If an automatic resize fails on a node for any reason, automatic resizing on the node is temporarily disabled. An error message is written to the `USM` event log and the `OKS` log. Automatic resizing may still take place on another node; however, if the failure is due to the underlying volume being out of free space then all nodes quickly disable automatic resize. The file system does continue to periodically try to automatic resize, at increasingly longer intervals. After a resize succeeds, such as when more space is added to the underlying Oracle ASM disk group, then automatic resize becomes re-enabled on the node. Note that other nodes may remain in the error state even after one node successfully auto-resizes the file system. Automatic resize can be manually re-enabled by either re-mounting the file system or running the acfsutil size command again with the `-a` or `-x` option to update automatic resize settings. When a file system has grown to the maximum size specified with `acfsutil size -x`, automatic resize remains enabled but does not grow the file system any further until the maximum is increased.

The `-d` argument is not compatible with the `-a` and `-x` automatic resize arguments. Unless a volume device is specified with `-d`, it is assumed that the caller is specifying an amount of storage that applies to the primary volume, which represents the size of the file system. When growing a file system with an accelerator volume, the `acfsutil` `size` command determines if the accelerator size needs to be increased. If the accelerator must be larger and cannot be increased, the command fails and the primary volume remains at the same size. When shrinking a file system, only the primary volume is shrunk. If a volume device is specified with the `-d` option, then the size specified applies to either the primary volume or the accelerator volume, whichever is specified, and only that volume device is changed. The command warns the user if the resulting accelerator volume size is not large enough to accommodate the primary volume size.

When using an accelerator volume and automatic resize, the increment specified with the automatic resize `-a` argument applies to the primary volume; however, both the primary volume and the accelerator volume are monitored. Automatic resize grows the primary volume by the specified increment, or greater if needed. Automatic resize monitors and grows the accelerator volume as needed as well by smaller increments. When automatic resize needs to grow the primary volume, it first attempts to grow the accelerator if insufficient space remains on the accelerator to accommodate the new growth, and if that fails the primary volume remains at the same size.

In addition to being triggered because the free space falls below the configured automatic resize increment, an automatic resize also takes place under other conditions, such as:

- If the free space in the file system falls below 10% of the current file system size or 5 GB, whichever is smaller.
- If a copy-on-write cannot find enough contiguous space in the file system to allocate new storage for the write.
- If the defragger cannot find enough contiguous space to allocate in order to defragment 8 MB worth of extents in a file.

These conditions protect against a large file system having enough total free space so that an automatic resize appears unnecessary, but the space is so fragmented that applications cannot use it.

When a non-sparse file is resized so that it grows by more than the configured auto-resize interval, the file system automatic resizes by a multiple of the automatic resize increment so that the resize request can be satisfied.

Examples

The following example shows the use of `acfsutil` `size`. This example increases the primary device file of `/acfsmounts/acfs1` file system by 500 MB.

Example: Using the acfsutil size command

```
$ /sbin/acfsutil size +500M /acfsmounts/acfs1
```

### acfsutil thaw

Purpose

Resumes activity after an `acfsutil` `freeze` command has been issued on a file system.

Syntax and Description

```
acfsutil thaw -h
acfsutil thaw mount_point
```

`acfsutil` `thaw` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `thaw` command.

Table: Options for the acfsutil thaw command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

You can use the `acfsutil` `thaw` command to resume activity after the `acfsutil` `freeze` command has been issued to temporarily halt modification activity on a file system. For information about `acfsutil` `freeze`, refer to acfsutil freeze.

Examples

The following example shows the use of the `acfsutil` `thaw` command.

Example: Using the acfsutil thaw command

```
$ /sbin/acfsutil thaw /acfsmounts/acfs1
```

### acfsutil version

Purpose

Displays Oracle ACFS version information.

Syntax and Description

```
acfsutil version -h
acfsutil version -v
```

`acfsutil` `version` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `version` command.

Table: Options for the acfsutil version command

| Option | Description |
| --- | --- |
| `-v` | Displays verbose version information about Oracle ACFS. |

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Example: Using acfsutil version

In the first example, basic information is displayed about the Oracle ACFS release version. In the second example, detailed version information is displayed about the installed Oracle ACFS components.

```
$ /sbin/acfsutil version
acfsutil version: 19.0.0.0.0

$ /sbin/acfsutil version -v
Kernel:
    Build version: 19.0.0.0.0
    Build full version: 19.2.0.0.0
    Build hash:    9728583571
    Bug numbers:   26947218
Commands:
    Build version: 19.0.0.0.0
    Build full version: 19.2.0.0.0
    Build hash:    9728583571
    Bug numbers:   26947218
```

### advmutil canonical

Purpose

`advmutil` `canonical` displays the canonical name of the specified Oracle ADVM device name.

Syntax and Description

```
advmutil -h
advmutil canonical volume_device
```

`advmutil` `-h` displays help text and exits.

The following table contains the options available with the `advmutil` `canonical` command.

Table: Options for the advmutil canonical command

| Option | Description |
| --- | --- |
| `volume_device` | Specifies a string identifying an Oracle ADVM volume device. |

There are several different formats that can identify an Oracle ADVM volume device, but a normalized, unambiguous (canonical) name should be used when the volume device name is used with other commands such as `SRVCTL`.

For example, on the Windows operating system you can use the following prefixes with a volume device name: `\\.\`, `\??\`, `\\?\`

The `advmutil` `canonical` command would return the canonical name that another utility would recognize without having to strip off extra characters. The command would most likely be used in a script.

Examples

The following examples show the use of `advmutil` `canonical` on a Windows operating system. For each example, the command returns the canonical name of the volume device.

Example: Using advmutil canonical

```
[C:\]advmutil canonical asm-volume1-274
asm-volume1-274

[C:\]advmutil canonical \\.\asm-volume1-274
asm-volume1-274

[C:\]advmutil canonical \\?\asm-volume1-274
asm-volume1-274

[C:\]advmutil canonical \??\asm-volume1-274
asm-volume1-274
```

### advmutil volinfo

Purpose

`advmutil` `volinfo` displays information about Oracle ADVM volume devices.

Syntax and Description

```
advmutil -h
advmutil volinfo [-l][-L] [volume_device]
```

`advmutil` `-h` displays help text and exits.

The following table contains the options available with the `advmutil` `volinfo` command.

Table: Options for the advmutil volinfo command

| Option | Description |
| --- | --- |
| `volume_device` | Specifies an optional volume device name. |
| `-l` | Separates the Oracle ADVM volume device information by field descriptions and colons on one line. |
| `-L` | Separates the Oracle ADVM volume device information by spaces on one line. |

`advmutil` `volinfo` displays information about Oracle ADVM volume devices in a list format by default. The `-l` option on Linux (`/l` on Windows) formats the display into a colon-separated string with field descriptions. The `-L` option on Linux (`/L` on Windows) formats the display into a space-separated string in a format suitable for scripting.

Examples

The first example displays information about an Oracle ADVM volume device, using the `advmutil` `volinfo` command with the volume device name. The second example displays information about the volume device using the `-l` option. The third example displays information about the volume device using the `-L` option.

Example: Using advmutil volinfo

```
$ /sbin/advmutil volinfo /dev/asm/volume1-123
Device : /dev/asm/volume1-228
Interface Version: 1
Size (MB): 256
Resize Increment (MB): 32
Redundancy: mirror
Stripe Columns: 4
Stripe Width (KB): 128
Disk Group: DATA
Volume: VOLUME1
Compatible.advm : 11.2.0.0.0

$ /sbin/advmutil volinfo -l /dev/asm/volume1-228
Device : /dev/asm/volume1-228 : Interface Version : 1 : Size (MB) : 256 :
Resize Increment (MB) : 32 : Redundancy : mirror : Stripe Columns : 4 :
Stripe Width (KB) : 128 : Disk Group : DATA : Volume : VOLUME1 :
Compatible.advm : 11.2.0.0.0

$ /sbin/advmutil volinfo -L /dev/asm/volume1-228
/dev/asm/volume1-228  1  256 32  mirror  4  128  DATA  VOLUME1  11.2.0.0.0
```

### Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems

This topic discusses the operations to deregister or dismount a file system and disable a volume.

Deregistering an Oracle ACFS File System

You can deregister an Oracle ACFS file system if you do not want the file system to be automatically mounted.

For example:

```
$ /sbin/acfsutil registry -d /acfsmounts/acfs1
```

If you deregister a file system, then you must explicitly mount the file system after Oracle Clusterware or the system is restarted.

For more information about the registry, refer to [About the Oracle ACFS Mount Registry](introducing-oracle-acfs-and-oracle-advm.md). For information about `acfsutil` `registry`, refer to acfsutil registry.

Dismounting an Oracle ACFS File System

You can dismount a file system without deregistering the file system or disabling the volume on which the file system is mounted.

For example, you can dismount a file system and run `fsck` to check the file system.

```
# /bin/umount /acfsmounts/acfs1

# /sbin/fsck -a -v -y -t acfs /dev/asm/volume1-123
```

After you dismount a file system, you must explicitly mount the file system.

Use `umount` on Linux systems or `acfsdismount` on Windows systems. For information about the commands to dismount a file system, refer to umount or acfsdismount.

Use `fsck` on Linux systems or `acfschkdsk` on Windows systems to check a file system. For information about the commands to check a file system, refer to fsck (offline mode) or acfschkdsk.

Disabling a Volume

To disable a volume, you must first dismount the file system on which the volume is mounted.

For example:

```
# /bin/umount /acfsmounts/acfs1
```

After a file system is dismounted, you can disable the volume and remove the volume device file.

For example:

```
ASMCMD> voldisable -G data volume1
```

Dismounting the file system and disabling a volume does not destroy data in the file system. You can enable the volume and mount the file system to access the existing data. For information about `voldisable` and `volenable`, refer to [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md).

### Removing an Oracle ACFS File System and a Volume

You can remove an Oracle ACFS file system and volume with `acfsutil` and ASMCMD commands.

To permanently remove a volume and Oracle ACFS file system, perform the following steps. These steps destroy the data in the file system.

1. Deregister the file system with `acfsutil` `registry` `-d`.
	For example:
	```
	$ /sbin/acfsutil registry -d /acfsmounts/acfs1
	acfsutil registry: successfully removed ACFS mount point
	   /acfsmounts/acfs1 from Oracle Registry
	```
2. Dismount the file system.
	For example:
	```
	# /bin/umount /acfsmounts/acfs1
	```
	You must dismount the file system on all nodes of a cluster.
	Use `umount` on Linux systems or `acfsdismount` on Windows systems.
3. Remove the file system with `acfsutil` `rmfs`.
	If you were not planning to remove the volume in a later step, this step is necessary to remove the file system. Otherwise, the file system is removed when the volume is deleted.
	For example:
	```
	$ /sbin/acfsutil rmfs /dev/asm/volume1-123
	```
4. Optionally you can disable the volume with the ASMCMD `voldisable` command.
	For example:
	```
	ASMCMD> voldisable -G data volume1
	```
5. Delete the volume with the ASMCMD `voldelete` command.
	For example:
	```
	ASMCMD> voldelete -G data volume1
	```

See also

- acfsutil registry for information about running `acfsutil` `registry`
- umount or acfsdismount for information about running the `umount` or `acfsdismount` commands
- acfsutil rmfs for information about running the `acfsutil` `rmfs` command
- [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md) for information about running the `voldisable` command
- [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md) for information about running the `voldelete` command
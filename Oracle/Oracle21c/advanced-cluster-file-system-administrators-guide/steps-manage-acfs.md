---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/steps-manage-acfs.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides an overview of the basic steps when managing Oracle ACFS file systems using command-line utilities.

The examples in this section show operating system commands that are run in a Linux environment system. ASMCMD commands manage the Oracle ADVM volumes, but you can also use SQL\*PLus and Oracle ASM Configuration Assistant (ASMCA) to manage volumes.

This section contains these topics:

### About Using Oracle ACFS Command-Line Tools

This topic provides an overview of the use of Oracle ACFS `acfsutil` commands.

The discussions include:

- Privileges to Run Oracle ACFS acfsutil Commands
- Displaying Help for Oracle ACFS acfsutil Commands
- Displaying Oracle ACFS Version Information
- Managing Trace File Space for acfsutil Commands

Privileges to Run Oracle ACFS acfsutil Commands

To run many Oracle ACFS `acfsutil` commands, you must be a system administrator or an Oracle ASM administrator user that has been enabled to run the commands. These privileges are described as follows:

- For system administrator privileges, you must be the `root` user.
- For Oracle ASM administrator user privileges, you must belong to the `OSASM` group and the `oinstall` group (for the `OINSTALL` privilege ).

Displaying Help for Oracle ACFS `acfsutil` Commands

You can display help and usage text for Oracle ACFS `acfsutil` commands with the `h` option. When you include a command or a subcommand with the command, the help and usage display is specific to the command and subcommand entered.

The following example illustrates several different ways to display help and usage text, from the most general to more specific. This example shows the `—h` format to display help on a Linux platform.

Example 6-1 Displaying help for Oracle ACFS acfsutil commands

```
$ /sbin/acfsutil -h

$ /sbin/acfsutil -h compress
$ /sbin/acfsutil compress -h

$ /sbin/acfsutil -h repl info 
$ /sbin/acfsutil repl info -h

$ /sbin/acfsutil -h sec admin info
$ /sbin/acfsutil sec admin info -h
```

Displaying Oracle ACFS Version Information

You can run `acfsutil` `version` to display the Oracle ACFS version. For example:

```
$ /sbin/acfsutil version
acfsutil version: 12.2.0.0.3
```

For more information about displaying Oracle ACFS version details, refer to [acfsutil version](acfs-commands-utilities.md).

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
	`ADRCI> set homepath my_specified_homepath`
- Display the current configuration values.
	`ADRCI> show control`
- Update a specific ADRCI configuration value. For example, set `SHORTP_POLICY` to `240` hours (10 days).
	In the displayed `show control` output, check the value of the `SHORTP_POLICY` attribute, which is the retention period in hours for short-lived files. If necessary, set a new retention period for short-lived trace files with the following:
	`ADRCI> set control (SHORTP_POLICY=240)`

If you want to start an immediate purge of the trace files in the current ADR home path, you can use the following command:

`ADRCI> purge -type TRACE -age number_of_minutes`

The value number\_of\_minutes controls which files are purged based on the age of the files. Files older than the specified number of minutes are targeted for the purge operation.

Note that automated purges of files in ADR occur on a fixed schedule that is not affected by changes in retention period. In other words, changing the retention period changes how soon after creation files are eligible to be purged, but does not change when a purge occurs. To force a purge, you must request it manually, as shown above.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges
- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=SUTIL-GUID-DC5744C7-FAC0-436B-99D5-DBD45B66930B) for information about the Automatic Diagnostic Repository Command Interpreter (ADRCI) utility

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
	       -user user1,user2,user3 -mtowner sysowner -mtgroup sysgrp -mtperm 755
	```
	You can also register a file system with the `acfsutil` `registry` command. For example:
	```
	$ /sbin/acfsutil registry -a /dev/asm/volume1-123 /acfsmounts/acfs1
	```
	After registering an Oracle ACFS file system in the cluster mount registry, the file system is mounted automatically on each cluster member listed in the registry entry during the next registry check action. This automatic process runs every 30 seconds and eliminates the requirement to manually mount the file system on each member of the cluster. Registering an Oracle ACFS file system also causes the file system to be mounted automatically whenever Oracle Clusterware or the system is restarted.
	Note:
	- The `srvctl` `add` `filesystem` command is required when an Oracle Database home is installed on an Oracle ACFS file system. In this case, the file system should not be explicitly added to the registry with the Oracle ACFS registration command (`acfsutil` `registry`).
	- Oracle ACFS registration is not supported in an Oracle Restart (standalone) configuration, which is a single-instance (non-clustered) environment.
	- The `root` or `asmadmin` privileges are required to modify the registry.
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
	The `root` privilege is required to run the `mount` command.
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

See Also:

- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [mkfs](acfs-commands-linux.md) (Linux environments) for information about the command to create an Oracle ACFS file system
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about the `volcreate` command and the `volinfo` command
- [acfsutil registry](acfs-commands-utilities.md) for information about the `acfsutil` `registry` command to register an Oracle ACFS file system
- [About the Oracle ACFS Mount Registry](understand-acfs-concepts.md) for about information registering an Oracle ACFS file system
- [mount](acfs-commands-linux.md) (Linux environments) for information about the command to mount an Oracle ACFS file system
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=REFRN-GUID-6005A792-228F-44C2-885C-A1F02CA558F6) for information about the `V$ASM_VOLUME` view
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=CWADD-GUID-F2CBA060-E4F2-4EB1-A0A7-11144D68A26A) for information about Server Control Utility (SRVCTL) commands

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
	The `root` privilege is required run the `mount` command.
	After the file system has been mounted, ensure that the permissions are set to allow access for the appropriate users.
4. List the contents of the test file you previously created on the file system.
	For example:
	```
	$ cat /acfsmounts/acfs1/myfile
	Oracle ACFS File System
	```
	The contents should match the file created previously on node 1.

See Also:

- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about the `volenable` command
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about the `volinfo` command
- [mount](acfs-commands-linux.md) (Linux environments) for information about the command to mount Oracle ACFS file systems
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges

### Managing Oracle ACFS Snapshots

To create and verify a snapshot on node 1:

1. Create snapshot of the new file system created on node 1.
	For example:
	```
	$ /sbin/acfsutil snap create mysnapshot_20090725 /acfsmounts/acfs1
	```
	See " [acfsutil snap create](acfs-commands-snapshots.md) ".
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

### Encrypting Oracle ACFS File Systems using OCR as Encryption Key Store

This topic discusses basic operations to manage encryption on an Oracle ACFS file system on Linux while using the OCR as encryption key store.

The examples in this section show a scenario in which the medical history files are encrypted in an Oracle ACFS file system.

Because the `acfsutil` `encr` `set` and `acfsutil` `encr` `rekey` `-v` commands modify the encryption key store, you should back up the Oracle Cluster Registry (OCR) after running these commands to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3` or higher.

For the examples in this section, various operating system users, operating system groups, and directories must exist.

The basic steps to manage encryption are:

1. Initialize encryption.
	Run the `acfsutil` `encr` `init` command to initialize encryption and create an encryption key store within the OCR. This command must be run one time for each cluster on which encryption is set up.
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
	The `acfsutil` `encr` `set` command also transparently generates a volume encryption key which is stored in the OCR encryption key store that was previously configured with the `acfsutil` `encr` `init` command.
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

See Also:

- [Oracle ACFS Encryption](understand-acfs-admin.md) for more information about Oracle ACFS encryption, including log files
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [acfsutil encr init](acfs-commands-encryption.md) for information about initializing encryption
- [acfsutil encr set](acfs-commands-encryption.md) for information about setting encryption parameters
- [acfsutil encr on](acfs-commands-encryption.md) for information about enabling encryption
- [acfsutil encr info](acfs-commands-encryption.md) for information displaying encryption information

### Encrypting Oracle ACFS File Systems using Oracle Key Vault as Encryption Key Store

This topic discusses basic operations to manage encryption on an Oracle ACFS file system on Linux while using the Oracle Key Vault as encryption key store.

The examples in this section show a scenario in which the medical history files are encrypted in an Oracle ACFS file system. The steps in this section assume Oracle ACFS security is not configured for the file system; however, you can use both Oracle ACFS security and encryption on the same file system. If you decide to use both security and encryption, then both encryption and security must be initialized for the cluster containing the file system. After security is initialized on the file system, then an Oracle ACFS security administrator runs `acfsutil                                                   sec` commands to provide encryption for the file system.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3` or higher.

For the examples in this section, various operating system users, operating system groups, and directories must exist.

The basic steps to manage encryption are:

1. Initialize encryption.
	Run the `acfsutil` `encr` `init -o` command to initialize encryption and create an autologin wallet for the Oracle Key Vault. This command must be run one time for each cluster on which encryption is set up.
	For example, the following command initializes encryption for a cluster.
	```
	# /sbin/acfsutil encr init -o
	```
	If the Oracle Kev Vault endpoint requires a password for login, the command will prompt for the password and save it within the Oracle Key Vault autologin wallet. The saved password will be used by ACFS to autologin to the Oracle Key Vault. Note that all Oracle Key Vault endpoints within the cluster must have the same endpoint password.
	This command must be run before any other encryption command and requires root or administrator privileges to run.
2. Set encryption parameters.
	Run the `acfsutil` `encr` `set` command to set the encryption parameters for the entire Oracle ACFS file system.
	For example, the following command sets the `AES` encryption algorithm and a file key length of `128` for a file system mounted on the `/acfsmounts/acfs1` directory.
	```
	# /sbin/acfsutil encr set -a AES -k 128 -m /acfsmounts/acfs1/
	```
	The `acfsutil` `encr` `set` command also transparently generates a volume encryption key which is stored in the Oracle Key Vault that was previously configured with the `acfsutil` `encr` `init -o` command.
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

See Also:

- [Oracle ACFS Encryption](understand-acfs-admin.md) for more information about Oracle ACFS encryption, including log files
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [acfsutil encr init](acfs-commands-encryption.md) for information about initializing encryption
- [acfsutil encr set](acfs-commands-encryption.md) for information about setting encryption parameters
- [acfsutil encr on](acfs-commands-encryption.md) for information about enabling encryption
- [acfsutil encr info](acfs-commands-encryption.md) for information displaying encryption information

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

See Also:

- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [Oracle ACFS Tagging](understand-acfs-admin.md) for information about tagging an Oracle ACFS file system, including requirements for using Extended Attributes in tagging
- [acfsutil tag set](acfs-commands-tagging.md) for information about specifying tag names
- [acfsutil tag info](acfs-commands-tagging.md) for information about displaying tag name and details
- [acfsutil tag unset](acfs-commands-tagging.md) for information about changing and removing tag names

### Replicating Oracle ACFS File Systems

The operations to manage Oracle ACFS snapshot-based replication on an Oracle ACFS file system on Linux are discussed in this topic.

The disk groups on which volumes are created for the primary and standby file systems must have compatibility attributes for `ASM` and `ADVM` set to `12.2` or higher. To use a snapshot as a storage location, or to use replication role reversal, the compatibility attributes for Oracle ASM and Oracle ADVM must be set to `18.0` or higher.

The steps to manage replication are:

1. Determine the user to be employed for replication.
	Choose or create the replication user who logs in with `ssh` to the standby cluster to apply data replicated from the primary location to the standby location. This user is defined only at the operating system (OS) level and not within Oracle. The user should belong to the groups defined for Oracle ASM administrator access. This user is designated the repluser.
	Note:
	The same user and group identities (including all `uids` and `gids`) must be specified for the replication user on both your primary cluster and your standby cluster.
2. Ensure that `ssh` has been configured for replication.
	The use of `ssh` by replication involves the user identity repluser. Configuring `ssh` involves the following high-level steps:
	- Configuring a user key for repluser on each cluster, then ensuring that key is authorized to log in as repluser on the other cluster.
		- Ensuring that a host key for each node in each cluster is known to the user repluser in the other cluster.
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
	33 MB/sec * (1 – 0.2 – (4 * 0.05)) = 33 * 0.6 = ~20 MB/sec
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
	Snapshot size does vary with the rate of change of the primary. Another factor is that snapshot size depends in part on the number of files in the file system, as well as the rate of change. Potentially more importantly, if you use constant mode replication, the `-C` option to `acfsutil` `repl` `init` `primary`, or if replication operations are not completing successfully in the interval given with interval—based replication because the interval is too small, the size of replication-related snapshots is difficult to predict in advance. In these cases, observe the size of the snapshots being generated over time and adjust the file system size as needed with the `acfsutil` `size` command to accommodate normal storage needs in addition in the presence of the snapshots. When collecting this information, a good starting point is to accommodate space for the snapshots to contain the data that is multiple times larger than the collection period, at the average rate of change of the primary.
	While collecting this information, choose a conservative starting point for the amount of space to allow for replication snapshots. For example, you can compute the space needed to store changes to the file system over the collection period as described previously, then you can allocate several times that space for future snapshots.
6. Optionally set tags on directories and files to replicate only selected files in an Oracle ACFS primary location. You can also add tags to files after replication has started.
7. Configure the site hosting the standby location.
	Before replicating an Oracle ACFS a primary storage location, configure the site hosting the standby location by performing the following:
	- To use the file system as a standby location, create a new standby file system of adequate size to hold the files replicated from the primary location, as well as a single replication snapshot, and mount the file system. For example:
		`/standby/repl_data`
		- To use a snapshot of an existing file system as a standby location, create a new read-write snapshot, and ensure that the file system is of adequate size to hold the files replicated from the primary location, as well as a single replication snapshot.
		- For either kind of standby location, run the `acfsutil` `repl` `init` `standby` command on the site hosting the standby location. For example:
		```
		$ /sbin/acfsutil repl init standby -u repluser /standby/repl_data
		```
		Note:
		If the `acfsutil` `repl` `init` `standby` command is interrupted for any reason, the user must re-create the file system or snapshot used for the location, re-mount the file system if needed, and re-run the command.
		This command requires the name of the replication user and the standby location. The specified user is the user under which `ssh`, invoked from the primary cluster, logs in to the standby cluster to apply changes. This user is specified with the -u option. For example: `-u repluser`.
		If the standby location is a file system, it is named with its mount point. For example: `/standby/repl_data`.
		If the standby location is a read-write snapshot, it is named with the snapshot name and the mount point of the containing file system, with the two separated by the `@` character. For example: `drsnap1101@/standby/repl_data`.
		In addition, for either kind of standby location, if the standby cluster contains multiple nodes, then specify a VIP, such as the SCAN VIP, as the network endpoint that replication uses on the standby to receive information from the primary. A hostname should be used as this network endpoint in single-node clusters only.
		You may run this command as either `root` or repluser. This is the same for all `acfsutil` `repl` commands except for the following commands that read, but never modify the replication state:
		- The `acfsutil` `repl` `info` and `acfsutil` `repl` `bg` `info` commands may be run by any Oracle ASM administrator user.
				- The `acfsutil` `repl` `compare` command is allowed to be run by any Oracle ASM administrator user, but should be run as `root` to maximize its access to the files being compared..
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
		- The user name and network endpoint (VIP name or address, or host name or address) to be used to connect to the site hosting the standby location, specified with the `—s` option. For example: `-s repluser@standby12_vip`
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

See Also:

- [Oracle ACFS Replication](understand-acfs-admin.md) for information about replicating Oracle ACFS file systems or snapshots
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [Configuring ssh for Use With Oracle ACFS Replication](acfs-advanced-topics.md) for information about configuring replication
- [acfsutil repl init](acfs-commands-replication.md) for information initiating replication
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM user privileges
- [acfsutil repl bg](acfs-commands-replication.md) for more information about managing replication background operations
- [acfsutil repl pause](acfs-commands-replication.md) and [acfsutil repl resume](acfs-commands-replication.md) for more information about pausing and resuming replication operations
- [acfsutil repl info](acfs-commands-replication.md) for information about displaying replication details
- Creating an Oracle ACFS File System for information about creating a file system
- Tagging Oracle ACFS File Systems for information about the steps to tag files

### Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems

This topic discusses the operations to deregister or dismount a file system and disable a volume.

Deregistering an Oracle ACFS File System

You can deregister an Oracle ACFS file system if you do not want the file system to be automatically mounted.

For example:

```
$ /sbin/acfsutil registry -d /acfsmounts/acfs1
```

If you deregister a file system, then you must explicitly mount the file system after Oracle Clusterware or the system is restarted.

For more information about the registry, refer to [About the Oracle ACFS Mount Registry](understand-acfs-concepts.md). For information about `acfsutil` `registry`, refer to [acfsutil registry](acfs-commands-utilities.md).

Dismounting an Oracle ACFS File System

You can dismount a file system without deregistering the file system or disabling the volume on which the file system is mounted.

For example, you can dismount a file system and run `fsck` to check the file system.

```
# /bin/umount /acfsmounts/acfs1

# /sbin/fsck -y -t acfs /dev/asm/volume1-123
```

After you dismount a file system, you must explicitly mount the file system.

Use `umount` on Linux systems. For information about the command to dismount a file system, refer to [umount](acfs-commands-linux.md).

Use `fsck` on Linux systems to check a file system. For information about the command to check a file system, refer to [fsck (offline mode)](acfs-commands-linux.md).

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

Dismounting the file system and disabling a volume does not destroy data in the file system. You can enable the volume and mount the file system to access the existing data. For information about `voldisable` and `volenable`, refer to [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md).

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
2. Dismount the file system with the `umount` command.
	For example:
	```
	# /bin/umount /acfsmounts/acfs1
	```
	You must dismount the file system on all nodes of a cluster.
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

See Also:

- [acfsutil registry](acfs-commands-utilities.md) for information about running `acfsutil` `registry`
- [umount](acfs-commands-linux.md) for information about running the `umount` command
- [acfsutil rmfs](acfs-commands-utilities.md) for information about running the `acfsutil` `rmfs` command
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about running the `voldisable` command
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about running the `voldelete` command
---
title: Basic Steps to Manage Oracle ACFS Systems
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util001.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section provides an outline of the basic steps when managing Oracle ACFS file systems using command-line utilities.

The examples in this section show operating system commands that are run in a Linux environment system. ASMCMD commands manage the volumes, but you can also use SQL\*PLus, Oracle ASM Configuration Assistant (ASMCA), and Oracle Enterprise Manager to manage volumes.

This section contains these topics:

## Creating an Oracle ACFS File System

To create and verify a file system, perform the following steps:

1. Create an Oracle ASM volume in a mounted disk group with the ASMCMD `volcreate` command.
	The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to 11.2 or higher for the disk group to contain an Oracle ADVM volume. To use Oracle ACFS encryption, replication, security, or tagging, the disk group on which the volume is created for the file system must have compatibility attributes for `ASM` and `ADVM` set to `11.2.0.2`. See ["Disk Group Compatibility Attributes"](asmdiskgrps.md).
	Start ASMCMD connected to the Oracle ASM instance. You must be a user in the OSASM operating system group. See ["About Privileges for Oracle ASM"](asminst.md).
	When configuring Oracle ADVM volume devices within a disk group, Oracle recommends assigning the Oracle Grid Infrastructure user and Oracle ASM administrator roles to users who have root privileges.
	To create a volume:
	```
	ASMCMD [+] > volcreate -G data -s 10G volume1
	```
	On Linux platforms, the volume name must be less than or equal to eleven alphanumeric characters, starting with an alphabetic character. On AIX platforms, the volume name must be less than or equal to twenty three alphanumeric characters, starting with an alphabetic character. On Windows and Solaris platforms, the volume name must be less than or equal to thirty alphanumeric characters, starting with an alphabetic character.
	When creating an Oracle ASM volume, a volume device name is created that includes a unique Oracle ADVM persistent disk group number. The volume device file functions in the same manner as any other disk or logical volume to mount file systems or for applications to use directly.
	For information about the `volcreate` command, see ["volcreate"](asm_util007.md).
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
	For information about the `volinfo` command, see ["volinfo"](asm_util007.md).
	See Also:
	[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1036.htm#REFRN30625) for information about the `V$ASM_VOLUME` view
3. Create a file system with the Oracle ACFS `mkfs` command.
	Create a file system using an existing volume device.
	For example:
	```
	$ /sbin/mkfs -t acfs /dev/asm/volume1-123
	mkfs.acfs: version                   = 11.2.0.1.0.0
	mkfs.acfs: on-disk version           = 39.0
	mkfs.acfs: volume                    = /dev/asm/volume1-123
	mkfs.acfs: volume size               = 10737418240
	mkfs.acfs: Format complete.
	```
	See ["mkfs"](asmfs_util002.md) (Linux or UNIX) or ["acfsformat"](asmfs_util005.md) (Windows). The `root` privilege is not required. The ownership of the volume device file dictates who can run this command.
4. Optionally register the file system with the `acfsutil` `registry` command.
	For example:
	```
	$ /sbin/acfsutil registry -a /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs
	acfsutil registry: mount point /u01/app/acfsmounts/myacfs successfully added 
	  to Oracle Registry
	```
	See ["acfsutil registry"](asmfs_util010.md). The `root` or `asmadmin` privileges are required to modify the registry. The Windows `Administrator` privilege is equivalent to the `root` privilege on Linux.
	Registering a file system is optional. After registering an Oracle ACFS file system in the cluster mount registry, the file system is mounted automatically on each cluster member listed in the registry entry during the next registry check action. This automatic process runs every 30 seconds and eliminates the requirement to manually mount the file system on each member of the cluster.
	Registering an Oracle ACFS file system also causes the file system to be mounted automatically whenever Oracle Clusterware or the system is restarted.
	Note:
	In an Oracle Grid Infrastructure Clusterware configuration, you can run `srvctl` `add` `filesystem` to automount a file system; this method is required when an Oracle Database home is installed on an Oracle ACFS file system. However, that file system should not be added to the registry. For information about Server Control Utility (SRVCTL), see [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005).
	For more information, see ["About the Oracle ACFS Mount Registry"](asmfilesystem.md).
	Note:
	A file system is not automatically mounted for an Oracle Restart configuration, which is a single-instance (non-clustered) environment.
5. Mount the file system with the Oracle ACFS `mount` command. You can mount a file system before or after registering the file system. If the file system has been registered, you can wait for the file system to be mounted automatically.
	For example:
	```
	# /bin/mount -t acfs /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs
	```
	See ["mount"](asmfs_util002.md) (Linux or UNIX) or ["acfsmountvol"](asmfs_util005.md) (Windows). The `root` privilege is required to run the `mount` command and the Windows `Administrator` privilege is required to run the `acfsmountvol` command.
	After the file system has been mounted, ensure that the permissions are set to allow access to the file system for the appropriate users. For example:
	```
	# chown -R oracle:dba /u01/app/acfsmounts/myacfs
	```
6. Create a test file in the file system.
	The user that creates the test file should be a user that is intended to access the file system. This test ensures that the appropriate user can write to the file system.
	For example:
	```
	$ echo "Oracle ACFS File System" > /u01/app/acfsmounts/myacfs/myfile
	```
7. List the contents of the test file that was created in the file system.
	For example:
	```
	$ cat /u01/app/acfsmounts/myacfs/myfile
	Oracle ACFS File System
	```

## Accessing an Oracle ACFS File System on a Different Node in the Cluster

If the node is part of a cluster, perform the following steps on node 2 to view the test file you created on node 1.

Note:

If the file system has been registered with the Oracle ACFS mount registry, you can skip steps 1 to 3.
1. Enable the volume that was previously created and enabled on node 1.
	Start ASMCMD connected to the Oracle ASM instance. You must be a user in the OSASM operating system group. See ["About Privileges for Oracle ASM"](asminst.md).
	For example:
	```
	ASMCMD [+] > volenable -G data volume1
	```
	See ["volenable"](asm_util007.md).
2. View information about the volume that you created on node 1.
	For example:
	```
	ASMCMD [+] > volinfo -G data volume1
	```
	See ["volinfo"](asm_util007.md).
3. Mount the file system using the Oracle ACFS `mount` command.
	For example:
	```
	# /bin/mount -t acfs /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs
	```
	See ["mount"](asmfs_util002.md) (Linux or UNIX) or ["acfsmountvol"](asmfs_util005.md) (Windows). The `root` privilege is required run the `mount` command and the Windows `Administrator` privilege is required to run the `acfsmountvol` command.
	After the file system has been mounted, ensure that the permissions are set to allow access for the appropriate users.
4. List the contents of the test file you previously created on the file system.
	For example:
	```
	$ cat /u01/app/acfsmounts/myacfs/myfile
	Oracle ACFS File System
	```
	The contents should match the file created previously on node 1.

## Managing Oracle ACFS Snapshots

To create and verify a snapshot on node 1:

1. Create snapshot of the new file system created on node 1.
	For example:
	```
	$ /sbin/acfsutil snap create mysnapshot_20090725 /u01/app/acfsmounts/myacfs
	```
	See ["acfsutil snap create"](asmfs_util010.md).
2. Update the test file in the file system so that it is different than the snapshot.
	For example:
	```
	$ echo "Modifying a file in Oracle ACFS File System" > /u01/app/acfsmounts/myacfs/myfile
	```
3. List the contents of the test file and the snapshot view of the test file.
	For example:
	```
	$ cat /u01/app/acfsmounts/myacfs/myfile
	$ cat /u01/app/acfsmounts/myacfs/.ACFS/snaps/mysnapshot_20090725/myfile
	```
	The contents of the test file and snapshot should be different. If node 1 is in a cluster, then you can perform the same list operation on node 2.

To manage snapshots with Oracle Enterprise Manager, see ["Managing Oracle ACFS Snapshots with Oracle Enterprise Manager"](asmfs_em.md).

## Securing Oracle ACFS File Systems

This section discusses the basic operations to manage security for an Oracle ACFS file system on Linux.

The scenario in this section shows how could you use Oracle ACFS security to ensure that only the maintenance user can access medical history files during the maintenance period. Also, Oracle ACFS encryption is also enabled on the same file system.

The scenario in this section assumes you are not planning to use Oracle ACFS replication on the file system. You cannot use Oracle ACFS security with replication.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3`. For information about disk group compatibility, refer to ["Disk Group Compatibility"](asmdiskgrps.md).

The basic steps to manage security are:

1. Initialize security for Oracle ACFS.
	Run the `acfsutil` `sec` `init` command to configure storage for security credentials and identify an operating system user as the first security administrator and the operating system security group. The security administrator must belong to the operating system group. This command must be run before any other security command and requires root or Windows `Administrator` privileges to run.
	The `acfsutil` `sec` `init` command is only run once to set up Oracle ACFS security for each cluster and can be run from any node in the cluster. Other security commands can also be run from any node in a cluster. Security administrators are common for all Oracle ACFS file systems in a cluster.
	For example, the following command initializes security for a cluster and creates the first security administrator (`medHistAdmin1`).
	```
	# /sbin/acfsutil sec init -u medHistAdmin1 -g medHistAdminGrp
	```
	The `medHistAdmin1` security administrator must belong to the `medHistAdminGrp` operating system group. That group is identified as the security group for the security administrators.
	When the root user or Windows `Administrator` user runs the command, the user assigns a temporary security password to the first security administrator. The first security administrator should now change the temporary password with the `acfsutil` `sec` `admin` `password` command. The valid password format is described in ["acfsutil sec init"](asmfs_util008.md).
	```
	$ /sbin/acfsutil sec admin password
	```
	Note that all `acfsutil` `sec` commands (other than `acfsutil` `sec` `init`) must be run by an Oracle ACFS security administrator and the administrator is prompted for the security administrator's password when each command is run.
	Note:
	When prompting for the security administrator's password, the following text displays: `Realm` `management` `password`
	The password required is the Oracle ACFS security administrator's password, not the operating system password of the user.
	Security administrators are allowed to browse all directories in an Oracle ACFS file system whether they have the underlying operating system permissions and whether any realm checks allow it. This functionality enables a security administrator to check the location of the files when securing them with Oracle ACFS security realms. However, a security administrator cannot view the contents of individual files without the appropriate operating system and security realm permissions.
	For more information, refer to ["acfsutil sec init"](asmfs_util008.md) and ["acfsutil sec admin password"](asmfs_util008.md).
2. Add additional security administrators as necessary.
	The first security administrator can add additional security administrators to administer Oracle ACFS security with the `acfsutil` `sec` `admin` `add` command.
	For example, add a new security administrator `medHistAdmin2`.
	```
	$ /sbin/acfsutil sec admin add medHistAdmin2
	```
	The `medHistAdmin2` user must belong to the operating system group (`medHistAdminGrp`) identified as the security administrator group with the `acfsutil` `sec` `init` command.
	The `medHistAdmin2` security administrator should change the assigned temporary security password with the `acfsutil` `sec` `admin` `password` command. The `medHistAdmin2` administrator can add new security administrators.
	For more information, refer to ["acfsutil sec admin add"](asmfs_util008.md) and ["acfsutil sec admin password"](asmfs_util008.md).
3. Prepare an Oracle ACFS file system for security.
	Run the `acfsutil` `sec` `prepare` on an Oracle ACFS file system before adding any security realms.
	For example, prepare the Oracle ACFS file system mounted on `/acfsmounts/acfs1` for Oracle ACFS security.
	```
	$ /sbin/acfsutil sec prepare -m /acfsmounts/acfs1
	```
	By default, security is enabled for a file system after running this command. You can explicitly disable or enable security with the `acfsutil` `sec` `disable` or `acfsutil` `sec` `enable` commands. For more information, refer to ["acfsutil sec disable"](asmfs_util008.md) and ["acfsutil sec enable"](asmfs_util008.md).
	This command automatically creates several security realms, such as the `SYSTEM_BackupOperators` security realm. Administrators can add users to the `SYSTEM_BackupOperators` realm which gives those users permissions to make backups of realm-secured files in the Oracle ACFS file system.
	For more information, refer to ["acfsutil sec prepare"](asmfs_util008.md).
4. Provide encryption for this file system.
	Encrypting the file system is optional, but is enabled in this scenario.
	1. First, run the `acfsutil` `encr` `init` command to initialize encryption and create the storage necessary for the encryption keys. This command must be run one time for each cluster on which encryption is set up.
		For example, the following command initializes encryption for a cluster.
		```
		# /sbin/acfsutil encr init
		```
		This command must be run before any other encryption command and requires root or administrator privileges to run. For more information, refer to ["acfsutil encr init"](asmfs_util009.md).
		2. Next, run the `acfsutil` `encr` `set` command to set encryption for the Oracle ACFS file system.
		For example, the following command sets encryption for the file system mounted on the `/acfsmounts/acfs1` directory.
		```
		# /sbin/acfsutil encr set -m /acfsmounts/acfs1/
		```
		The `acfsutil` `encr` `set` command transparently generates a volume encryption key which is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command. This command requires root or administrator privileges to run.
	For more information, refer to ["acfsutil encr init"](asmfs_util009.md) and ["acfsutil encr set"](asmfs_util009.md).
5. Create a security realm on the file system.
	Run the `acfsutil` `sec` `realm` `create` command to create a security realm for a file system.
	For example, create a security realm named `medHistRealm` which contains medical records files with all files encrypted in the realm.
	```
	$ /sbin/acfsutil sec realm create medHistRealm -m /acfsmounts/acfs1/ 
	                                               -e on -a AES -k 128
	```
	The `-e` option specifies that all the files in the realm are encrypted with the `AES` algorithm and the key length set to 128 bits. The file system must first be prepared for encryption with the `acfsutil` `encr` `init` and `acfsutil` `encr` `set` commands. Note that you do not have to enter the same value for the `-k` option with `acfsutil` `sec` `realm` `create` as you have entered with the `acfsutil` `encr` `set` command.
	For more information, refer to ["acfsutil sec realm create"](asmfs_util008.md).
6. Create security rules.
	Run the `acfsutil` `sec` `rule` `create` command to creates rules which determine access to the files and directories of a security realm.
	For example, create rules that allow the `medMaintenance` user to access medical records for the time period 10 PM to 2 AM for file maintenance.
	```
	$ /sbin/acfsutil sec rule create medHistRule1a –m /acfsmounts/acfs1/
	      –t time 22:00:00,02:00:00 –o ALLOW
	$ /sbin/acfsutil sec rule create medHistRule1b –m /acfsmounts/acfs1/
	      –t username medMaintenance –o ALLOW
	```
	You can edit rules with the `acfsutil` `sec` `rule` `edit` command.
	For more information, refer to ["acfsutil sec rule create"](asmfs_util008.md) and ["acfsutil sec rule edit"](asmfs_util008.md).
7. Create security rule sets and add rules to rule sets.
	Run the `acfsutil` `sec` `ruleset` `create` command to create a rule set to which rules can be added.
	For example, create a rule set named `medRuleSet1` that includes rules for operations on the files and directories of the security `medHistRealm` realm.
	```
	$ /sbin/acfsutil sec ruleset create medRuleSet1 –m /acfsmounts/acfs1/
	```
	Add the rules to the `medRuleSet1` rule set.
	```
	$ /sbin/acfsutil sec ruleset edit medRuleSet1 –m /acfsmounts/acfs1/ 
	           -a medHistRule1a,medHistRule1b -o ALL_TRUE
	```
	The `ALL_TRUE` option is the default action, but is added here to emphasize that both rules in each rule set must be true.
	For more information, refer to ["acfsutil sec ruleset create"](asmfs_util008.md) and ["acfsutil sec ruleset edit"](asmfs_util008.md).
8. Add objects to a security realm.
	Run the `acfsutil` `sec` `realm` `add` command to add objects, such as command rules, rule sets, and files, to a security realm.
	For example, add the `medRuleSet1` rule set and all the files in the `/acfsmounts/acfs1/medicalrecords` directory to the `medHistRealm`.
	```
	$ /sbin/acfsutil sec realm add medHistRealm –m /acfsmounts/acfs1/ 
	        -l ALL:medRuleSet1
	        –f -r /acfsmounts/acfs1/medicalrecords
	```
	When adding a rule set to a realm, the rule set is added with a command rule, such as `ALL:medRuleSet1`. Only one rule set can be included with each command rule. To display a list of the command rules, use `acfsutil` `sec` `info` with the `-c` option. Refer to ["acfsutil sec info"](asmfs_util008.md).
	Add backup operators to the `SYSTEM_BackupOperators` security realm that was automatically created with the `acfsutil` `sec` `prepare` command.
	```
	$ /sbin/acfsutil sec realm add SYSTEM_BackupOperators –m /acfsmounts/acfs1/ 
	        -G sysBackupGrp
	```
	Users that belong to the `sysBackupGrp` operating system group can now make backups of realm-secured files in the Oracle ACFS file system.
	For more information, refer to ["acfsutil sec realm add"](asmfs_util008.md) and ["acfsutil sec realm delete"](asmfs_util008.md).
9. Display security information.
	Run the `acfsutil` `sec` `info` command to display information for a security realm. For example, display security information for the `medHistRealm` realm.
	```
	$ /sbin/acfsutil sec info -m /acfsmounts/acfs1/ –n medHistRealm
	```
	To display the security realms to which a file or a directory belongs, run the `acfsutil` `sec` `info` `file` command. For example:
	```
	$ /sbin/acfsutil sec info file -m /acfsmounts/acfs1/
	                               /acfsmounts/acfs1/medicalrecords
	```
	For more information, refer to ["acfsutil sec info"](asmfs_util008.md) and ["acfsutil sec info file"](asmfs_util008.md).
10. Save security metadata as a backup.
	Run the `acfsutil` `sec` `save` command to save the security metadata of a file system.
	For example, save the security metadata of the `/acfsmounts/acfs1` file system to the `acfs1_backup.xml` file.
	```
	$ /sbin/acfsutil sec save –m /acfsmounts/acfs1 
	                          –p acfs1_backup.xml
	```
	The `acfs1_backup.xml` security metadata backup file is saved in the `/acfsmounts/acfs1/.Security/backup/` directory. The saved XML file can be loaded with the `acfsutil` `sec` `load` command.
	For more information, refer to ["acfsutil sec save"](asmfs_util008.md) and ["acfsutil sec load"](asmfs_util008.md).

You can run some `acfsutil` `sec` commands in a batch file with the `acfsutil` `sec` `batch` command. For example, you could create a batch file that contains a group of `acfsutil` `sec` `rule` and `acfsutil` `sec` `ruleset` commands. For more information, refer to ["acfsutil sec batch"](asmfs_util008.md).

Auditing and diagnostic data for Oracle ACFS security is saved to log files. For more information about Oracle ACFS security, including the log files, refer to ["Oracle ACFS Security"](asmfilesystem.md).

## Encrypting Oracle ACFS File Systems

This section discusses the basic operations to manage encryption on an Oracle ACFS file system on Linux. The examples in this section show a scenario in which the medical history files are encrypted in an Oracle ACFS file system.

The steps in this section assume Oracle ACFS security is not configured for the file system; however, you can use both Oracle ACFS security and encryption on the same file system. If you decide to use both security and encryption, then both encryption and security must be initialized for the cluster containing the file system. After security is initialized on the file system, then an Oracle ACFS security administrator runs `acfsutil` `sec` commands to provide encryption for the file system. For information about setting up security with encryption, refer to "Securing Oracle ACFS File Systems".

The steps in this section assume you are not planning to use Oracle ACFS replication on the file system. You cannot use Oracle ACFS encryption with replication.

Because the `acfsutil` `encr` `set` and `acfsutil` `encr` `rekey` `-v` commands modify the encryption key store, you should back up the Oracle Cluster Registry (OCR) after running these commands to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3`. For information about disk group compatibility, refer to ["Disk Group Compatibility"](asmdiskgrps.md).

The basic steps to manage encryption are:

1. Initialize encryption.
	Run the `acfsutil` `encr` `init` command to initialize encryption and create the storage necessary for the encryption keys. This command must be run one time for each cluster on which encryption is set up.
	For example, the following command initializes encryption for a cluster.
	```
	# /sbin/acfsutil encr init
	```
	This command must be run before any other encryption command and requires root or administrator privileges to run.
	For more information, refer to ["acfsutil encr init"](asmfs_util009.md).
2. Set encryption parameters.
	Run the `acfsutil` `encr` `set` command to set the encryption parameters for the entire Oracle ACFS file system.
	For example, the following command sets the `AES` encryption algorithm and a file key length of `128` for a file system mounted on the `/acfsmounts/acfs1` directory.
	```
	# /sbin/acfsutil encr set -a AES -k 128 -m /acfsmounts/acfs1/
	```
	The `acfsutil` `encr` `set` command also transparently generates a volume encryption key which is stored in the key store that was previously configured with the `acfsutil` `encr` `init` command.
	This command requires root or administrator privileges to run.
	For more information, refer to ["acfsutil encr set"](asmfs_util009.md).
3. Enable encryption.
	Run the `acfsutil` `encr` `on` command to enable encryption for directories and files.
	For example, the following command enables encryption recursively on all files in the `/acfsmounts/acfs1/medicalrecords` directory.
	```
	# /sbin/acfsutil encr on -r /acfsmounts/acfs1/medicalrecords
	                         -m /acfsmounts/acfs1/
	```
	For users that have appropriate permissions to access files in the `/acfsmounts/acfs1/medicalrecords` directory, they can still read the decrypted files.
	This command can be run by an administrator or the file owner.
	For more information, refer to ["acfsutil encr on"](asmfs_util009.md).
4. Display encryption information.
	Run the `acfsutil` `encr` `info` command to display encryption information for directories and files.
	```
	# /sbin/acfsutil encr info -m /acfsmounts/acfs1/ 
	                           -r /acfsmounts/acfs1/medicalrecords
	```
	This command can be run by an administrator or the file owner.
	For more information, refer to ["acfsutil encr info"](asmfs_util009.md).

Auditing and diagnostic data for Oracle ACFS encryption is saved to log files. For more information about Oracle ACFS encryption, including the log files, refer to ["Oracle ACFS Encryption"](asmfilesystem.md).

## Tagging Oracle ACFS File Systems

This section discusses the operations to manage tagging on directories and files in an Oracle ACFS file system on Linux.

The disk group on which the volume is created for the file system has compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3`. For information about disk group compatibility, refer to ["Disk Group Compatibility"](asmdiskgrps.md).

Oracle ACFS implements tagging with Extended Attributes. There are some requirements for using Extended Attributes; refer to ["Oracle ACFS Tagging"](asmfilesystem.md).

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
	For more information, refer to ["acfsutil tag set"](asmfs_util006.md).
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
	For more information, refer to ["acfsutil tag info"](asmfs_util006.md).
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
	For more information, refer to ["acfsutil tag unset"](asmfs_util006.md).

For more information about tagging an Oracle ACFS file system, refer to ["Oracle ACFS Tagging"](asmfilesystem.md).

## Replicating Oracle ACFS File Systems

This section discusses the operations to manage replication on an Oracle ACFS file system on Linux.

The steps in this section assume you are not planning to use Oracle ACFS security or encryption on the file system. You cannot use Oracle ACFS replication with security or encryption.

The disk groups on which volumes are created for the primary and standby file systems must have compatibility attributes for `ASM` and `ADVM` set to `11.2.0.3`. For information about disk group compatibility, refer to ["Disk Group Compatibility"](asmdiskgrps.md).

The steps to manage replication are:

1. Determine the storage capacity necessary for replication on the sites hosting the primary and standby file systems. The primary file system must have a minimum size of 4 GB for each node that is mounting the file system. The standby file system must have a minimum size of 4 GB and should be sized appropriately for the amount of data being replicated and the space necessary for the replication logs sent from the primary file system.
	Calculate the replication-related storage requirement for the primary file system, then use the same size requirement for the standby file system. If Oracle ACFS tagging is used to replicate only a subset of the files in the primary file system, then the size requirement for the standby file system is proportional to that subset of the primary file system.
	Run the `acfsutil` `info` `fs` command with the `-s` `interval` option on the node where the primary file system is mounted to display the amount and rate of change to the primary file system for the node. The amount of change includes all user and metadata modifications to the primary file system. This amount approximates the size of replication logs that are generated when recording changes to the file system. Changes are stored in temporary files called replication logs which are kept in a special directory in the primary file system until they can be sent to the standby to be applied. After confirmation is received that the changes contained in a replication log have been successfully applied to the standby file system, the replication logs on the primary file system are deleted.
	To approximate the extra storage capacity necessary for the replication logs, determine the following:
	- The time interval during which the site hosting the primary file system may experience network connectivity problems or slowdowns when accessing the site hosting the standby file system.
		- The time interval during which the site hosting the standby file system may be taken offline for maintenance.
	These time intervals are used in calculating the amount and rate of change in storage space. You must account for the time interval when the primary file system cannot send the replication logs over to the standby file system at its usual rate or when standby file systems are inaccessible while undergoing maintenance. The replication logs will accumulate on the site hosting the primary file system and may eventually cause that site to run out of space.
	For the following scenario, assume `t` = 60 minutes is the time interval in your environment that would adequately account for network problems or maintenance on site hosting the standby file system.
	Run `acfsutil` `info` `fs` `-s` `900` on the primary file system to collect the average rate of change over a 24 hour period with a 15 minute (900 seconds) interval. Note that `t/4` (60/4) is the value for the sampling interval. Do not exceed a value of `t/2` for the time interval as you may miss some important peaks.
	```
	$ /sbin/acfsutil info fs -s 900 /acfsmounts/repl_data
	```
	With the output, you can determine the average rate of change, the peak rate of change, and how long the peaks last. However, the command displays information only for the node on which the command is run. To collect the total amount of change in the file system the command must be run on every node that is modifying the file system. Note that the maximum number of supported nodes is eight.
	The following formula approximates the extra storage capacity needed:
	```
	Extra storage capacity to hold replication logs = 
	    (Number-nodes-on-primary * 1GB) + P
	```
	where `P` is the peak amount of change generated across all nodes for time `t` as reported by the `acfsutil` `info` `fs` `–s` output.
	In the example, we need to total the changes from four 15-minute intervals to find the total amount of change that could occur in 60 minutes. You may choose to use the single hour that generated the largest amount of change, or you could select the top four 15-minute intervals even if they did not occur together to prepare for the worst-case scenario.
	Assume that you have four nodes modifying the primary file system, and that during the measured interval, the peak amount of change reported for the 60 minutes is approximately 20 GB for all nodes. Using the storage capacity formula, 24 GB of excess storage capacity on each site hosting the primary file system is required for storage of the replication logs.
	```
	Extra storage capacity to hold replication logs = (4 * 1GB per node) + 
	 20GB maximum change per hour = 24GB of extra storage capacity
	```
	Next, check that the network transfer rate is greater than or equal to the rate of change observed during the monitoring period. In the previous example, the peak of 20 GB of changed data per hour is equivalent to a peak rate of change of about 5.5 MB/sec. To keep up with this rate of change, you must ensure that the network can reliably transfer at least this amount of data per second without negatively impacting your existing network workloads.
	To estimate your current actual network transfer rate, calculate the elapsed time required to FTP a 1 GB file from the primary file system to the intended standby file system during a period of time when network usage is low. For example, if the 1 GB file transfers in 30 seconds, then your current FTP transfer rate is 33 MB per seconds (1000 MB/30 seconds = 33 MB per second). Because of various delays inherent in the transfers, for planning purposes you should reduce this measured FTP transfer rate by 20%, and then by an additional 5% per node.
	In the previous example with 4 nodes, the FTP transfer rate used for planning is:
	```
	33 MB/sec * (1 – (0.2) – (4 * 0.05)) = 33 * (0.6) = ~20MB/sec
	```
	Because the peak rate of change was only 5.5 MB/second, you can expect the network to be able to handle this additional workload in this example. However, if the network capacity was already close to being fully utilized, you might want to consider increasing network capacity before implementing replication for this file system and workload.
	In addition, insure you have sufficient network capacity to allow replication to catch up after times when network problems prevent a primary file system from sending replication logs to the standby file system.
	For more information, refer to ["acfsutil info fs"](asmfs_util010.md).
2. Set up tags, user names, and service names.
	When starting replication on an Oracle ACFS file system, first perform the following steps:
	- Determine the user name and password that the sites hosting the primary and standby file systems use to connect to the remote Oracle ASM instance as the Oracle ASM and DBA administrator. All nodes that have the file system mounted must support this user name and password. The user must have `SYSASM` and `SYSDBA` privileges. For example:
		```
		SQL> CREATE USER primary_admin IDENTIFIED BY primary_passwd;
		SQL> GRANT sysasm,sysdba TO primary_admin;
		```
		Oracle wallets can also be used to manage security credentials.
		See Also:
		- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asowalet.htm#ASOAG160) for information about Oracle wallets
		- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_hierarch.htm#ADLOB46075) for information about wallet management
		- [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm#NETRF182) for information about wallet parameters in the `SQLNET.ORA` file
		- Determine a unique service name for the replicated file system.
		When both the primary and standby file systems are located in different clusters for disaster tolerance, then the service names for the primary and standby file systems can be the same. However, if the both file systems are mounted on the same node, such as a test configuration, then unique service names must be used for the primary and standby file systems. Using unique service names for the primary and standby file systems requires the use of the `-c` option during replication initialization. Service names are limited to a maximum of 128 bytes.
		Notes:
		- You must specify a service name other than +ASM because that service name is already in use by the Oracle ASM instance.
		- You must specify a unique service name for each file system that you want to replicate when there are multiple replicated file systems on a node or cluster.
		Using this service name, create a net service alias on the sites hosting the primary and standby file system that connects to the remote site. This alias along with the user name and password are used as the connection string in the replication initialization commands.
		For example, the following are examples of connect descriptors with net service aliases for the sites hosting the primary and standby file systems.
		```
		primary_repl_site=(DESCRIPTION=
		  (ADDRESS=(PROTOCOL=tcp)(HOST=primary1.example.com)(PORT=1521))
		  (ADDRESS=(PROTOCOL=tcp)(HOST=primary2.example.com)(PORT=1521))
		  (CONNECT_DATA=(SERVICE_NAME=primary_service)))
		standby_repl_site=(DESCRIPTION=
		  (ADDRESS=(PROTOCOL=tcp)(HOST=standby1.example.com)(PORT=1521))
		  (CONNECT_DATA=(SERVICE_NAME=standby_service)))
		```
		If you want to perform replication using a single client access name (SCAN) VIP, you must update the `REMOTE_LISTENER` initialization parameter in the Oracle ASM instance before initializing replication. You can update the parameter in the initialization file or with the `ALTER` `SYSTEM` SQL statement.
		For example:
		```
		SQL> ALTER SYSTEM SET remote_listener='SCAN_NAME:1521' sid='*' scope=both;
		```
		See Also:
		[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/concepts.htm#NETAG002) for information about connect descriptors
		- Optionally set tags on directories and files to replicate only selected files in an Oracle ACFS file system. You can also add tags to files after replication has already started. For information about the steps to tag files, refer to "Tagging Oracle ACFS File Systems".
3. Configure the site hosting the standby file system.
	Before replicating an Oracle ACFS file system, configure the site hosting the standby file system by performing the following procedures.
	- Create a new file system of adequate size to hold the replicated files and associated replication logs from the primary file system. For example: `/standby/repl_data`
		- Mount the file system on one node only.
		- Run the `acfsutil` `repl` `init` `standby` command. If this command is interrupted for any reason, the user must re-create the file system, mount it on one node only, and rerun the command. This command requires the following configuration information:
		- The connect string to be used to connect to the site hosting the primary file system. For example:
			`primary_admin/primary_passwd@primary_repl_site`
			The user `primary_admin` must have `SYSASM` and `SYSDBA` privileges.
				- If the standby file system is using a different service name than the primary file system, then the use `-c` option. This option specifies the service name for the standby file system. For example:
			`standby_repl_service`
				- The mount point of the standby file system. For example:
			`/standby/repl_data`
	For example, run the following `acfsutil` `repl` `init` `standby` command on the site hosting the standby file system.
	```
	$ /sbin/acfsutil repl init standby 
	    -p primary_admin/primary_passwd@primary_repl_site
	    -c standby_repl_service /standby/repl_data
	```
	The `acfsutil` `repl` `init` `standby` command requires root or system administrator privileges to run.
	For more information, refer to ["acfsutil repl init"](asmfs_util007.md).
4. Configure the site hosting the primary file system.
	After the standby file system has been set up, configure the site hosting the primary file system and start replication by performing the following procedures.
	Run the `acfsutil` `repl` `init` `primary` command. This command requires the following configuration information:
	- The connect string to be used to connect to the site hosting the standby file system. For example:
		`standby_admin/standby_passwd@standby_repl_site`
		The user `standby_admin` must have `SYSASM` and `SYSDBA` privileges.
		- The mount point of the primary file system. For example: `/acfsmounts/repl_data`
		- If the primary file system is using a different service name than the standby file system, then use the `-c` option. This option specifies the service name on the site hosting the primary file system. For example:
		`primary_repl_service`
		- If the mount point is different on the site hosting the standby file system than it is on the site hosting the primary file system, specify the mount point on the standby file system with the `-m` `standby_mount_point` option. For example:
		`-m /standby/repl_data`
	For example, run the following `acfsutil` `repl` `init` `primary` command on the site hosting the primary file system.
	```
	$ /sbin/acfsutil repl init primary 
	     -s standby_admin/standby_passwd@standby_repl_site
	     -m /standby/repl_data -c primary_repl_service 
	     /acfsmounts/repl_data
	```
	The `acfsutil` `repl` `init` `primary` command requires root or system administrator privileges to run.
	For more information, refer to ["acfsutil repl init"](asmfs_util007.md).
5. Monitor information about replication on the file system.
	The `acfsutil` `repl` `info` command displays information about the state of the replication processing on the primary or standby file system.
	For example, run the following `acfsutil` `repl` `info` command on the site hosting the primary file system to display configuration information.
	```
	$ /sbin/acfsutil repl info -c -v /acfsmounts/repl_data
	```
	You must have system administrator or Oracle ASM administrator privileges to run this command.
	For information, refer to ["acfsutil repl info"](asmfs_util007.md).
6. Manage replication background processes.
	Run the `acfsutil` `repl` `bg` command to start, stop, or retrieve information about replication background processes.
	For example, the following example displays information about the replication processes for the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl bg info /acfsmounts/repl_data
	```
	You must have system administrator or Oracle ASM administrator privileges to run the `acfsutil` `repl` `bg` `info` command.
	For more information, refer to ["acfsutil repl bg"](asmfs_util007.md).
7. Pause replication momentarily only if necessary.
	Run the `acfsutil` `repl` `pause` to momentarily stop replication. You should run the `acfsutil` `repl` `resume` command soon as possible to resume replication.
	For example, the following command pauses replication on the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl pause /acfsmounts/repl_data
	```
	The following command resumes replication on the `/acfsmounts/repl_data` file system.
	```
	$ /sbin/acfsutil repl resume /acfsmounts/repl_data
	```
	You must have system administrator or Oracle ASM administrator privileges to run these commands.
	For more information, refer to ["acfsutil repl pause"](asmfs_util007.md) and ["acfsutil repl resume"](asmfs_util007.md).

Note:

On an Oracle ACFS file system `df` reports space usage by internal metadata plus user files and directories. `du` only reports the space usage of user files and directories. Depending on the size of the volume and number of the nodes, internal metadata is allocated in varying sizes. Additionally, with replication enabled an internal replication log is allocated for each node that is used to record changes to the file system before exposing the replication log to user space daemons to transport to the standby.

For more information about replicating an Oracle ACFS file system, refer to ["Oracle ACFS Replication"](asmfilesystem.md).

## Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems

This section discusses the operations to deregister or dismount a file system and disable a volume. This section contains these topics:

- Deregistering an Oracle ACFS File System
- Dismounting an Oracle ACFS File System
- Disabling a Volume

### Deregistering an Oracle ACFS File System

You can deregister an Oracle ACFS file system if you do not want the file system to be automatically mounted.

For example:

```
$ /sbin/acfsutil registry -d /u01/app/acfsmounts/myacfs
```

If you deregister a file system, then you must explicitly mount the file system after Oracle Clusterware or the system is restarted.

For more information about the registry, see ["About the Oracle ACFS Mount Registry"](asmfilesystem.md). For information about `acfsutil` `registry`, see ["acfsutil registry"](asmfs_util010.md).

### Dismounting an Oracle ACFS File System

You can dismount a file system without deregistering the file system or disabling the volume on which the file system is mounted.

For example, you can dismount a file system and run `fsck` to check the file system.

```
# /bin/umount /u01/app/acfsmounts/myacfs

# /sbin/fsck -a -v -y -t acfs /dev/asm/volume1-123
```

After you dismount a file system, you must explicitly mount the file system.

Use `umount` on Linux systems or `acfsdismount` on Windows systems. For information about the commands to dismount a file system, see ["umount"](asmfs_util002.md) or ["acfsdismount"](asmfs_util005.md).

Use `fsck` on Linux systems or `acfschkdsk` on Windows systems to check a file system. For information about the commands to check a file system, see ["fsck"](asmfs_util002.md) or ["acfschkdsk"](asmfs_util005.md).

### Disabling a Volume

To disable a volume, you must first dismount the file system on which the volume is mounted.

For example:

```
# /bin/umount /u01/app/acfsmounts/myacfs
```

After a file system is dismounted, you can disable the volume and remove the volume device file.

For example:

```
ASMCMD> voldisable -G data volume1
```

Dismounting the file system and disabling a volume does not destroy data in the file system. You can enable the volume and mount the file system to access the existing data. For information about `voldisable` and `volenable`, see ["voldisable"](asm_util007.md) and ["volenable"](asm_util007.md).

## Removing an Oracle ACFS File System and a Volume

To permanently remove a volume and Oracle ACFS file system, perform the following steps. These steps destroy the data in the file system.

1. Deregister the file system with `acfsutil` `registry` `-d`.
	For example:
	```
	$ /sbin/acfsutil registry -d /oracle/acfsmounts/acfs1
	acfsutil registry: successfully removed ACFS mount point
	   /oracle/acfsmounts/acfs1 from Oracle Registry
	```
	For information about running `acfsutil` `registry`, see ["acfsutil registry"](asmfs_util010.md).
2. Dismount the file system.
	For example:
	```
	# /bin/umount /oracle/acfsmounts/acfs1
	```
	You must dismount the file system on all nodes of a cluster.
	Use `umount` on Linux systems or `acfsdismount` on Windows systems. For information about running `umount` or `acfsdismount`, see ["umount"](asmfs_util002.md) or ["acfsdismount"](asmfs_util005.md).
3. Remove the file system with `acfsutil` `rmfs`.
	If you were not planning to remove the volume in a later step, this step is necessary to remove the file system. Otherwise, the file system is removed when the volume is deleted.
	For example:
	```
	$ /sbin/acfsutil rmfs /dev/asm/volume1-123
	```
	For information about running `acfsutil` `rmfs`, see ["acfsutil rmfs"](asmfs_util010.md).
4. Optionally you can disable the volume with the ASMCMD `voldisable` command.
	For example:
	```
	ASMCMD> voldisable -G data volume1
	```
	For information about running `voldisable`, see ["voldisable"](asm_util007.md).
5. Delete the volume with the ASMCMD `voldelete` command.
	For example:
	```
	ASMCMD> voldelete -G data volume1
	```
	For information about running `voldelete`, see ["voldelete"](asm_util007.md).
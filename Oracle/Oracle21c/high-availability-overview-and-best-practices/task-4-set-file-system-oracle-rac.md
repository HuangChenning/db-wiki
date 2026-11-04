---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-4-set-file-system-oracle-rac.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 4: Set Up a File System on Oracle RAC

Oracle GoldenGate Microservices Architecture is designed with a simplified installation and deployment directory structure. The installation directory should be placed on local storage on each Oracle RAC node to provide minimized downtime during software patching.

The deployment directory, which is created during deployment creation using the Oracle GoldenGate Configuration Assistant (oggca.sh), must be placed on a shared file system. The deployment directory contains configuration, security, log, parameter, trail, and checkpoint files.

Placing the deployment in DBFS or ACFS provides the best recovery and failover capabilities in the event of a system failure. Ensuring the availability of the checkpoint files cluster-wide is essential so that after a failure occurs the GoldenGate processes can continue running from their last known position.

If Oracle GoldenGate will be configured along with Oracle Data Guard, the recommended file system is DBFS. DBFS is contained in the database protected by Data Guard, and can be fully integrated with XAG. In the event of a Data Guard role transition, the file system can be automatically mounted on the new primary server, followed by automated start-up of Oracle GoldenGate. This is currently not possible with ACFS, because it is not part of the Oracle Data Guard configuration.

Follow the instructions in the appropriate section below to configure the file system for either DBFS or ACFS.

Oracle Database File System (DBFS)

It is required that you create the DBFS tablespace inside the same database that the Oracle GoldenGate processes are connected to. For example, if a GoldenGate integrated Extract process is extracting from a database called GGDB, the DBFS tablespace would be located in the same GGDB database.

Follow instructions in [My Oracle Support note 869822.1](https://support.oracle.com/rs?type=doc&id=869822.1) to install the required FUSE libraries if they are not already installed.

Use the instructions in [My Oracle Support note 1054431.1](https://support.oracle.com/rs?type=doc&id=1054431.1) to configure the database, tablespace, database user, `tnsnames.ora` Oracle Net connection alias, and permissions on source or target GoldenGate environments required for DBFS.

Note:

When using an Oracle Multitenant Database, the DBFS tablespace MUST be created in a Pluggable Database (PDB). It is recommended that you use the same PDB that the GoldenGate Extract or Replicat processes are connecting to, allowing DBFS to use the same database service, created above in Task 2, for its database dependency.

When you create a file system for storing the GoldenGate deployment files, it is recommended that you allocate enough trail file disk space to permit storage of up to 12 hours of trail files. Doing this provides sufficient space for trail file generation should a problem occur with the target environment that prevents it from receiving new trail files. The amount of space needed for 12 hours can only be determined by testing trail file generation rates with real production data.

Example DBFS creation:

```
$ cd $ORACLE_HOME/rdbms/admin
$ sqlplus dbfs_user/dbfs_password@database_tns_alias
SQL> start dbfs_create_filesystem dbfs_gg_tbs goldengate
```

Follow the instructions in [My Oracle Support note 1054431.1](https://support.oracle.com/rs?type=doc&id=1054431.1) to configure the newly created DBFS file system so that the DBFS instance and mount point resources are automatically started by Cluster Ready Services (CRS) after a node failure, with the following DBFS configuration and script file modifications.

1. Change the `mount-dbfs.conf` parameters to reflect your database environment.
	Modify the `MOUNT_OPTIONS` parameter to the following:
	```
	MOUNT_OPTIONS=allow_other,direct_io,failover,nolock
	```
	The `failover` option forces all file writes to be committed to the DBFS database in an `IMMEDIATE WAIT` mode. This prevents data getting lost when it has been written into the `dbfs_client` cache but not yet written to the database at the time of a database or node failure.
	The `nolock` mount option is required if you are using Oracle Database 18c or a later release, due to a change in the DBFS file locking which can cause issues for GoldenGate processes after an Oracle RAC node failure when a file is currently locked.
	If you are using a `dbfs_client` from Oracle Database 12c Release 2 (12.2), make sure you have applied the latest release update that includes the fix for bug 27056711. Once the fix has been applied, the `MOUNT_OPTIONS` should also include the `nolock` option.
2. Modify the `mount-dbfs.sh` script to force unmounting of DBFS when the CRS resource is stopped.
	Change two occurrences of:
	`$FUSERMOUNT -u $MOUNT_POINT`
	To the following:
	`$FUSERMOUNT -uz $MOUNT_POINT`
3. When registering the resource with Oracle Clusterware, be sure to create it as a `cluster_resource` instead of a `local_resource`, as specified in the My Oracle Support note.
	The reason for using `cluster_resource` is so that the file system can only be mounted on a single node at a time, preventing mounting of DBFS from concurrent nodes, which creates the potential for concurrent file writes, causing file corruption problems.
	Make sure to use the database service name created in a previous step for the DBFS service dependency.
	For example:
	```
	DBNAME=ggdb
	DEPNAME=ora.$DBNAME.oggserv.svc
	crsctl add resource $RESNAME \
	  -type cluster_resource \
	  -attr "ACTION_SCRIPT=$ACTION_SCRIPT, \
	         CHECK_INTERVAL=30,RESTART_ATTEMPTS=10, \      
	START_DEPENDENCIES='hard($DEPNAME)pullup($DEPNAME)',\
	         STOP_DEPENDENCIES='hard($DEPNAME)',\
	         SCRIPT_TIMEOUT=300"
	```
	Once the DBFS resource has been created, the file system should be mounted and tested.
	```
	$ crsctl start res dbfs_mount
	$ crsctl stat res dbfs_mount
	```
	After the file system is mounted, create the directory for storing the GoldenGate files.
	```
	$ cd /mnt/dbfs/goldengate
	$ mkdir deployments
	```
	Note:
	Leave the shared file system mounted. It is required for creating the GoldenGate deployment in a later step.

Oracle Advanced Cluster File System (ACFS)

Oracle ACFS is an alternative to DBFS for the shared GoldenGate files in an Oracle RAC configuration.

Refer to [My Oracle Support note 1929629.1](https://support.oracle.com/rs?type=doc&id=1929629.1) for more information about ACFS configuration requirements for Oracle Exadata Database Machine.

Create a single ACFS file system for storing the Oracle deployment files.

It is recommended that you allocate enough trail file disk space to permit storage of up to 12 hours of trail files. Doing this provides sufficient space for trail file generation should a problem occur with the target environment that prevents it from receiving new trail files. The amount of space needed for 12 hours can only be determined by testing trail file generation rates with real production data.

1. Create the file system using ASMCMD as the Oracle ASM administrator user.
	```
	ASMCMD [+] > volcreate -G datac1 -s 1200G ACFS_GG
	```
	Note:
	Modify the file system size according to the determined size requirements.
	```
	ASMCMD> volinfo -G datac1 acfs_gg
	Diskgroup Name: DATAC1
	         Volume Name: ACFS_GG
	         Volume Device: /dev/asm/acfs_gg-151
	         State: ENABLED
	         Size (MB): 1228800
	         Resize Unit (MB): 64
	         Redundancy: MIRROR
	         Stripe Columns: 8
	         Stripe Width (K): 1024
	         Usage:
	         Mountpath:
	```
	Make the file system with the following mkfs command.
	```
	$ /sbin/mkfs -t acfs /dev/asm/acfs-gg-151
	```
2. Create the CRS resource for the newly created ACFS file system, if not already created.
	Check to see if the file system resource was already created.
	```
	$ srvctl status filesystem -volume ACFS_GG -diskgroup DATAC1
	ACFS file system /mnt/acfs_gg is mounted on nodes oggadm07, oggadm08
	```
	If not already created, create the ACFS mount point on all of the Oracle RAC nodes.
	```
	# mkdir -p /mnt/acfs_gg
	```
	Create the file system resource as the root user. Due to the implementation of distributed file locking on ACFS, unlike DBFS, it is acceptable to mount ACFS on more than one RAC node at any one time.
	Create the ACFS resource using srvctl from the Oracle Grid Infrastructure ORACLE\_HOME.
	```
	# srvctl add filesystem -device /dev/asm/acfs_gg-151 -volume ACFS_GG
	-diskgroup DATAC1 -path /mnt/acfs_gg -user oracle -autostart RESTORE
	```
	To verify the currently configured ACFS file systems, use the following command to view the file system details.
	```
	$ srvctl config filesystem
	Volume device: /dev/asm/acfs_gg-151
	Diskgroup name: datac1
	Volume name: ACFS_GG
	Canonical volume device: /dev/asm/acfs_gg-151
	Accelerator volume devices:
	Mountpoint path: /mnt/acfs_gg
	Mount point owner: oracle
	Check the status of the ACFS resource and mount it.
	$ srvctl status filesystem -volume ACFS_GG -diskgroup DATAC1
	ACFS file system /mnt/acfs is not mounted
	$ srvctl start filesystem -volume ACFS_GG -diskgroup DATAC1 –node dc1north01
	```
	The CRS resource that is created is named using the format ora.diskgroup\_name.volume\_name.acfs. Using the above file system example, the CRS resource is called `ora.datac1.acfs_gg.acfs`.
	To see all ACFS file system CRS resources that currently exist, use the following command.
	```
	$ crsctl stat res -w "((TYPE = ora.acfs.type) OR (TYPE = ora.acfs_cluster.type))"
	NAME=ora.datac1.acfs_gg.acfs
	TYPE=ora.acfs.type
	TARGET=ONLINE              , OFFLINE
	STATE=ONLINE on dc1north01, OFFLINE
	```
3. Create a GoldenGate deployment directory on ACFS.
	After the file system is mounted, create the directory for storing the GoldenGate deployments.
	```
	$ cd /mnt/acfs_gg
	$ mkdir deployments
	```

Note:

Leave the shared file system mounted. It is required for creating the GoldenGate deployment in a later Task.
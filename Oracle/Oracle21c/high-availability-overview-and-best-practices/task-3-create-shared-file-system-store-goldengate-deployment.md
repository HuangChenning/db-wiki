---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-3-create-shared-file-system-store-goldengate-deployment.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 3 - Create a Shared File System to Store the Oracle GoldenGate Deployment

Oracle GoldenGate Microservices Architecture is designed with a simplified installation and deployment directory structure.

- The installation directory should be placed on local storage on each database node to minimize downtime during software patching.
- The deployment directory which is created during deployment creation using the Oracle GoldenGate Configuration Assistant (oggca.sh), must be placed on a shared file system. The deployment directory contains configuration, security, log, parameter, trail, and checkpoint files.

Placing the deployment in DBFS or Oracle Automatic Storage Management Cluster File System (ACFS) provides the best recoverability and failover capabilities in the event of a system failure. Ensuring the availability of the checkpoint files cluster-wide is essential so that the GoldenGate processes can continue running from their last known position after a failure occurs.

If Oracle GoldenGate will be configured along with Oracle Data Guard, the recommended file system is DBFS. DBFS is contained in the database protected by Data Guard and can be fully integrated with XAG. In the event of a Data Guard role transition, the file system can be automatically mounted on the new primary server, followed by the automated start-up Oracle GoldenGate. This is currently not possible with ACFS since it is not part of the Oracle Data Guard configuration.

Note:

This document does not include steps to configure Oracle GoldenGate with Oracle Data Guard.

If Oracle Data Guard is not present, the recommended file system is ACFS. ACFS is a multi-platform, scalable file system and storage management technology that extends Oracle Automatic Storage Management (Oracle ASM) functionality to support customer files maintained outside the Oracle Database.

Perform one of the following steps to complete this task, based on your file system requirements:

- Step 3a - Oracle Database File System (DBFS)
- Step 3b - Oracle ASM Cluster File System (ACFS)

Step 3a - Oracle Database File System (DBFS)

You must create the DBFS tablespace inside the same database to which the Oracle GoldenGate processes are connected. For example, if an Oracle GoldenGate integrated Extract process is extracted from a database called GGDB, the DBFS tablespace would be located in the same GGDB database.

Create a file system for storing the Oracle GoldenGate deployment files. You should allocate enough trail file disk space to permit storage of up to 12 hours of trail files. Doing this will give sufficient space for trail file generation should a problem occur with the target environment that prevents it from receiving new trail files. The amount of space needed for 12 hours can only be determined by testing trail file generation rates with real production data.

Perform the following sub-steps to complete this step:

- Step 3a.1 - Configuring DBFS on Oracle Exadata Database Service
- Step 3a.2 - Create the DBFS Repository
- Step 3a.3 - (Only for CDB) Create an Entry in TNSNAMES
- Step 3a.4 - Download and Edit the mount-dbfs Scripts
- Step 3a.5 - Register the DBFS Resource with Oracle Clusterware
- Step 3a.6 - Start the DBFS Resource
Step 3a.1 - Configuring DBFS on Oracle Exadata Database Service
1. As the `opc` OS user, add the `grid` user to the `fuse` group:
	```
	[opc@exadb-node1]$ sudo -u grid $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/bin/olsnodes > ~/dbs_group
	[opc@exadb-node1]$ dcli -g ~/dbs_group -l opc sudo usermod -a -G fuse grid
	```
2. As the `opc` OS user, validate that the file /etc/fuse.conf exists and contains the `user_allow_other` option:
	```
	[opc@exadb-node1]$ cat /etc/fuse.conf
	# mount_max = 1000
	# user_allow_other
	```
3. Skip this step if the option `user_allow_other` is already in the `/etc/fuse.conf` file.
	Otherwise, run the following commands as the `opc` OS user to add the option:
	```
	[opc@exadb-node1]$ dcli -g ~/dbs_group -l opc "echo user_allow_other | sudo tee -a /etc/fuse.conf"
	```
4. As the `opc` OS user, create an empty directory that will be used as the mount point for the DBFS file system:
	```
	[opc@exadb-node1]$ dcli -g ~/dbs_group -l opc sudo mkdir -p /mnt/dbfs
	```
5. As the `opc` OS user, change ownership on the mount point directory so the `grid` OS user can access it:
	```
	[opc@exadb-node1]$ dcli -g ~/dbs_group -l opc sudo chown oracle:oinstall /mnt/dbfs
	```
Step 3a.2 - Create the DBFS Repository

Create the DBFS repository inside the target database. To create the repository, create a new tablespace within the target PDB to hold the DBFS objects and a database user that will own the objects.

Note:

When using an Oracle Multitenant Database, the DBFS tablespace MUST be created in a Pluggable Database (PDB). It is recommended that you use the same PDB that the GoldenGate Extract or Replicat processes connect to, allowing DBFS to use the same database service created above for its database dependency.

1. As the `oracle` OS user, create the tablespace in the database:
	```
	[opc@exadb-node1]$ sudo su - oracle
	[oracle@exadb-node1]$ source DB_NAME.env
	[oracle@exadb-node1]$ sqlplus / as sysdba
	SQL> alter session set container=<pdb_name>;
	SQL> create bigfile tablespace dbfstb1 datafile size 32g autoextend on next 8g
	 maxsize 300g NOLOGGING EXTENT MANAGEMENT LOCAL AUTOALLOCATE SEGMENT SPACE
	 MANAGEMENT AUTO;
	SQL> create user dbfs_user identified by "<dbfs_user_password>"
	 default tablespace dbfstb1 quota unlimited on dbfstb1;
	SQL> grant connect, create table, create view, create procedure,
	 dbfs_role to dbfs_user;
	```
2. As the `oracle` OS user, create the database objects that will hold DBFS. This script takes two arguments:
	- `dbfstb1`: tablespace for the DBFS database objects
		- `goldengate`: file system name - this can be any string and will appear as a directory under the mount point
	```
	[oracle@exadb-node1]$ sqlplus dbfs_user/"<dbfs_user_password>"@<db_name>_dbfs
	SQL> start $ORACLE_HOME/rdbms/admin/dbfs_create_filesystem dbfstb1 goldengate
	```

Step 3a.3 - (Only for CDB) Create an Entry in TNSNAMES

1. As the `oracle` OS user, find the database domain name:
	```
	[opc@exadb-node1]$ sudo su - oracle
	[oracle@exadb-node1]$ source DB_NAME.env
	[oracle@exadb-node1]$ sqlplus / as sysdba
	SQL> show parameter db_domain
	NAME                                 TYPE        VALUE
	------------------------------------ ----------- ------------------------------
	db_domain                            string      <db_domain_name>
	```
2. As the `oracle` OS user, add a connect entry in `$TNS_ADMIN/tnsnames.ora` file:
	```
	[oracle@exadb-node1]$ vi $TNS_ADMIN/tnsnames.ora
	dbfs =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL = IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <pdb_service_name>.<db_domain_name> )
	       )
	    )
	```
3. As the `oracle` OS user, distribute the `$TNS_ADMIN/tnsnames.ora` file to the rest of the nodes:
	```
	[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group
	 -f $TNS_ADMIN/tnsnames.ora -d $TNS_ADMIN/
	```

Step 3a.4 - Edit the mount-dbfs Scripts

1. Unzip the zip file and edit the variable settings in the file `mount-dbfs.conf` for your environment.
	Comments in the file will help you to confirm the values for these variables:
	- `DBNAME: echo $ORACLE_UNQNAME`
		- `MOUNT_POINT: /mnt/dbfs/goldengate`
		- `ORACLE_HOME (RDBMS ORACLE_HOME directory): echo                                 $ORACLE_HOME`
		- `GRID_HOME (GRID INFRASTRUCTURE HOME directory): echo                                 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)`
		- `DBFS_PASSWD` (used only if `WALLET=false`)
		- `DBFS_PWDFILE_BASE` (used only if `WALET=false`)
		- `WALLET` (must be `true` or `false`)
		- `TNS_ADMIN` (used only if `WALLET=true` or `PDB): echo                                 $TNS_ADMIN`
		- `DBFS_LOCAL_TNSALIAS` (used only if `WALLET=true`)
		- `IS_PDB` (set to `true` if using PDB)
		- `PDB` (PDB name, if applicable): `PDB                                 name`
		- `PDB_SERVICE` (the database service created in step 2.3, if applicable): `PDB_SERVICE_NAME`
		- `MOUNT_OPTIONS:                                 allow_other,direct_io,failover,nolock`
		- The `failover` option forces all file writes to be committed to the DBFS database in an `IMMEDIATE WAIT` mode. This prevents data from getting lost when it has been written into the `dbfs_client` cache, but not yet written to the database at the time of a database or node failure.
				- The `nolock` mount option is required if you use Oracle Database 18c or later versions because of a change in the DBFS file locking, which can cause issues for GoldenGate processes after an Oracle RAC node failure when a file is currently locked.
2. As the `grid` OS user, unzip the `mount-dbfs-<version>.zip` and edit the configuration file `mount-dbfs.conf`:
	```
	[opc@exadb-node1]$ sudo su - grid
	[grid@exadb-node1]$ cd /u02/app_acfs/goldengate
	[grid@exadb-node1]$ unzip mount-dbfs-<version>.zip
	[grid@exadb-node1]$ vi mount-dbfs.conf
	```
	Example of `mount-dbfs.conf`:
	```
	DBNAME=<DB_UNIQUE_NAME>
	MOUNT_POINT=/mnt/dbfs/goldengate
	DBFS_USER=dbfs_user
	GRID_HOME=$(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)
	if [ -z "${GRID_HOME}" ]; then
	    echo "GRID_HOME is unset or set to the empty string"
	fi
	ORACLE_HOME=$($GRID_HOME/bin/srvctl config database -d $DBNAME |grep 'Oracle home:' | cut -d: -f2 |sed 's/ //g')
	if [ -z "${ORACLE_HOME}" ]; then
	    echo "ORACLE_HOME is unset or set to the empty string"
	fi
	LOGGER_FACILITY=user
	MOUNT_OPTIONS=allow_other,direct_io,failover,nolock
	PERL_ALARM_TIMEOUT=14
	DBFS_PASSWD=<DBFS_USER_PASSWORD>
	DBFS_PWDFILE_BASE=/tmp/.dbfs-passwd.txt
	WALLET=false
	TNS_ADMIN=$ORACLE_HOME/network/admin/<DB_NAME>
	IS_PDB=true
	PDB=<PDB_NAME>
	PDB_SERVICE=<PDB_SERVICE_NAME>
	```
3. As the `grid` OS user, modify the `mount-dbfs.sh` script to force unmounting of DBFS when the CRS resource is stopped:
	```
	[grid@exadb-node1]$ vi /u02/app_acfs/goldengate/mount-dbfs.sh
	# Change two occurrences of:
	$FUSERMOUNT -u $MOUNT_POINT
	# To the following:
	$FUSERMOUNT -uz $MOUNT_POINT
	```
4. As the `opc` OS user, copy `mount-dbfs.conf` (rename it if desired or needed) to the directory `/etc/oracle` on database nodes and set proper permissions on it:
	```
	[opc@exadb-node1]$ sudo -u grid $(grep ^crs_home /etc/oracle/olr.loc | cut
	 -d= -f2)/bin/olsnodes > ~/dbs_group
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc -d /tmp
	 -f /u02/app_acfs/goldengate/mount-dbfs.conf
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 cp /u02/app_acfs/goldengate/mount-dbfs.conf /etc/oracle
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 chown grid:oinstall /etc/oracle/mount-dbfs.conf
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 chmod 660 /etc/oracle/mount-dbfs.conf
	```
5. As the `opc` OS user, copy `mount-dbfs.sh` (rename it if desired or needed) to the proper directory (`$GI_HOME/crs/script`) on database nodes and set proper permissions on it:
	```
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 mkdir $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo chown
	 grid:oinstall $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l grid
	 -d $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	 -f /u02/app_acfs/goldengate/mount-dbfs.sh
	[opc@exadb-node1]$ /usr/local/bin/dcli -g ~/dbs_group -l grid chmod 770
	 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script/mount-dbfs.sh
	```

Step 3a.5 - Register the DBFS Resource with Oracle Clusterware

When registering the resource with Oracle Clusterware, create it as a `cluster_resource`.

The reason for using `cluster_resource` is so the file system can only be mounted on a single node at one time, preventing mounting of DBFS from concurrent nodes creating the potential of concurrent file writes, and causing file corruption problems.

1. As the `grid` OS user, find the resource name for the database service created in a previous step for the DBFS service dependency:
	```
	[opc@exadb-node1]$ sudo su - grid
	[grid@exadb-node1]$ crsctl stat res |grep <PDB_NAME>
	NAME=ora.<DB_UNIQUE_NAME>.<SERVICE_NAME>.svc
	```
2. As the `oracle` OS user, register the Clusterware resource by running the following script:
	```
	[opc@exadb-node1]$ sudo su - oracle
	[oracle@exadb-node1]$ vi /u02/app_acfs/goldengate/add-dbfs-resource.sh
	##### start script add-dbfs-resource.sh
	#!/bin/bash
	ACTION_SCRIPT=$(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script/mount-dbfs.sh
	RESNAME=dbfs_mount
	DEPNAME=ora.<DB_UNIQUE_NAME>.<SERVICE_NAME>.svc
	ORACLE_HOME=$(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)
	PATH=$ORACLE_HOME/bin:$PATH
	export PATH ORACLE_HOME
	crsctl add resource $RESNAME \
	  -type cluster_resource \
	  -attr "ACTION_SCRIPT=$ACTION_SCRIPT, \
	         CHECK_INTERVAL=30,RESTART_ATTEMPTS=10, \
	         START_DEPENDENCIES='hard($DEPNAME)pullup($DEPNAME)',\
	         STOP_DEPENDENCIES='hard($DEPNAME)',\
	         SCRIPT_TIMEOUT=300"
	##### end script add-dbfs-resource.sh
	[oracle@exadb-node1]$ sh /u02/app_acfs/goldengate/add-dbfs-resource.sh
	```

Note:

After creating the `$RESNAME` resource, to stop the `$DBNAME` database when the `$RESNAME` resource is `ONLINE`, you specify the `force` flag when using `srvctl`.

For example: `srvctl stop database -d fsdb -f`

Step 3a.6 - Start the DBFS Resource

As the `grid` OS user, start the resource:

```
[opc@exadb-node1]$ sudo su - grid
[grid@exadb-node1]$ crsctl start res dbfs_mount -n \`hostname\`
CRS-2672: Attempting to start 'dbfs_mount' on 'exadb-node1'
CRS-2676: Start of 'dbfs_mount' on 'exadb-node1' succeeded

[grid@exadb-node1]$ crsctl stat res dbfs_mount -t

--------------------------------------------------------------------------------
Name           Target  State        Server                   State details      
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
dbfs_mount
      1        ONLINE  ONLINE       exadb-node1              STABLE
--------------------------------------------------------------------------------
```

Note:

Leave the shared file system mounted. It is required for creating the Oracle GoldenGate deployment in a later step.

Step 3b - Oracle ASM Cluster File System (ACFS)

Oracle ACFS is an alternative to DBFS for the shared Oracle GoldenGate files in an Oracle RAC configuration. Create a single ACFS file system for storing the Oracle deployment files.

It is recommended that you allocate enough trail file disk space to permit the storage of up to 12 hours of trail files. Doing this will give sufficient space for trail file generation should a problem occur with the target environment that prevents it from receiving new trail files. The amount of space needed for 12 hours can only be determined by testing trail file generation rates with real production data.

Perform the following sub-steps to complete this step:

- Step 3b.1 - Create the ASM File System
- Step 3b.2 - Make the File System
- Step 3b.3 - Create the Cluster Ready Services (CRS) Resource
- Step 3b.4 - Verify the Currently Configured ACFS File Systems
- Step 3b.5 - Start and Check the Status of the ACFS Resource
- Step 3b.6- Create GoldenGate ACFS Directory

Step 3b.1 - Create the ASM File System

As the `grid` OS user, use `asmcmd` to create the volume:

```
[opc@exadb-node1 ~]$ sudo su - grid
[grid@exadb-node1 ~]$ asmcmd volcreate -G DATAC1 -s 1200G ACFS_GG
```

Note:

Modify the file system size according to the determined size requirements.

Step 3b.2 - Make the File System

1. As the `grid` OS user, use `asmcmd` to confirm the “Volume Device”:
	```
	[grid@exadb-node1 ~]$ asmcmd volinfo -G DATAC1 ACFS_GG
	```
	Following is an example of the ACFS volume device output:
	```
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
2. As the `grid` OS user, make the file system with the following `mkfs` command:
	```
	[grid@exadb-node1 ~]$ /sbin/mkfs -t acfs /dev/asm/acfs_gg-151
	```
Step 3b.3 - Create the Cluster Ready Services (CRS) Resource
1. As the `opc` OS user, create the ACFS mount point:
	```
	[opc@exadb-node1 ~]$ dcli -l opc -g ~/dbs_group sudo mkdir -p /mnt/acfs_gg
	[opc@exadb-node1 ~]$ dcli -l opc -g ~/dbs_group sudo chown
	 oracle:oinstall /mnt/acfs_gg
	```
2. Create the file system resource as the `root` user.
	Because the implementation of distributed file locking on ACFS, unlike DBFS, it is acceptable to mount ACFS on more than one Oracle RAC node at any one time.
3. As the `root` OS user, create the ACFS resource for the new ACFS file system:
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/bin/srvctl
	 add filesystem -device /dev/asm/acfs_gg-151 -volume ACFS_GG -diskgroup DATAC1
	 -path /mnt/acfs_gg -user oracle
	```

Step 3b.4 - Verify the Currently Configured ACFS File Systems

As the `grid` OS user, use the following command to view the file system details:

```
[opc@exadb-node1 ~]$ sudo su - grid
[grid@exadb-node1 ~]$ srvctl config filesystem -volume ACFS_GG -diskgroup DATAC1

Volume device: /dev/asm/acfs_gg-151
Diskgroup name: datac1
Volume name: acfs_gg
Canonical volume device: /dev/asm/acfs_gg-151
Accelerator volume devices:
Mountpoint path: /mnt/acfs_gg
Mount point owner: oracle
Mount point group: oinstall
Mount permissions: owner:oracle:rwx,pgrp:oinstall:r-x,other::r-x
Mount users: grid
Type: ACFS
Mount options:
Description:
ACFS file system is enabled
ACFS file system is individually enabled on nodes:
ACFS file system is individually disabled on nodes:
```

Step 3b.5 - Start and Check the Status of the ACFS Resource

As the `grid` OS user, use the following command to start and check the file system:

```
[grid@exadb-node1 ~]$ srvctl start filesystem -volume ACFS_GG
 -diskgroup DATAC1 -node \`hostname\`
[grid@exadb-node1 ~]$ srvctl status filesystem -volume ACFS_GG -diskgroup DATAC1
```

ACFS file system `/mnt/acfs_gg` is mounted on nodes `exadb-node1`

The CRS resource created is named using the format `ora.diskgroup_name.volume_name.acfs`. Using the above file system example, the CRS resource is called `ora.datac1.acfs_gg.acfs`.

To see all ACFS file system CRS resources that currently exist, use the following command.

```
[grid@exadb-node1 ~]$ crsctl stat res -w "((TYPE = ora.acfs.type) OR (TYPE = ora.acfs_cluster.type))"

NAME=ora.datac1.acfs_gg.acfs
TYPE=ora.acfs.type
TARGET=ONLINE                   , OFFLINE
STATE=ONLINE on exadb-node1, OFFLINE
NAME=ora.datac1.acfsvol01.acfs
TYPE=ora.acfs.type
TARGET=ONLINE                   , ONLINE
STATE=ONLINE on exadb-node1, ONLINE on exadb-node2
```

Step 3b.6- Create GoldenGate ACFS Directory

As the `grid` OS user, create the directory for storing the Oracle GoldenGate deployments.

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ mkdir -p /mnt/acfs_gg/deployments
```

Refer to the [Oracle Automatic Storage Management Cluster File System Administrator’s Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/index.html) for more information about ACFS.

Note:

Leave the shared file system mounted. It is required for creating the Oracle GoldenGate deployment in a later step.
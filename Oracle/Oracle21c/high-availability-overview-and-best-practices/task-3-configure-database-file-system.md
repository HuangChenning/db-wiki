---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-3-configure-database-file-system.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 3 - Configure Oracle Database File System

The Database File System (DBFS) is the only recommended solution when configuring Oracle GoldenGate with Oracle Data Guard.

The DBFS user, tablespace, and file system in the database was previously created in the primary database, as detailed in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md).

Perform the following steps to complete this task:

- Step 3.1 - Configuring DBFS on Oracle Exadata Database Service
- Step 3.2 - (PDB Only) Create an Entry in TNSNAMES
- Step 3.3 - Copy and Edit the mount-dbfs Scripts from the Primary System
- Step 3.4 - Register the DBFS Resource with Oracle Clusterware

Step 3.1 - Configuring DBFS on Oracle Exadata Database Service

1. As the `opc` OS user on the standby system, add the `grid` user to the `fuse` group:
	```
	[opc@exastb-node1 ~]$ sudo -u grid
	 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/bin/olsnodes > ~/dbs_group
	[opc@exadb-node1 ~]$ dcli -g ~/dbs_group -l opc sudo usermod -a -G fuse grid
	```
2. As the `opc` OS user on the standby system, validate that the file `/etc/fuse.conf` exists and contains the `user_allow_other` option:
	```
	[opc@exastb-node1 ~]$ cat /etc/fuse.conf
	# mount_max = 1000
	user_allow_other
	```
3. As the `opc` OS user on the standby system, skip this step if the option `user_allow_other` is already in the `/etc/fuse.conf` file. Otherwise run the following commands to add the option:
	```
	[opc@exastb-node1 ~]$ dcli -g ~/dbs_group -l opc “echo user_allow_other |
	 sudo tee -a /etc/fuse.conf”
	```
4. As the `opc` OS user on the standby system, create an empty directory that will be used as the mount point for the DBFS filesystem.
	Note:
	It is important that the mount point is identical as the one in the primary system, because the physical location of the Oracle GoldenGate deployment is included within the deployment configuration files.
	```
	[opc@exastb-node1 ~]$ dcli -g ~/dbs_group -l opc sudo mkdir -p /mnt/dbfs
	```
5. As the `opc` OS user on the standby system, change ownership on the mount point directory so the `grid` OS user can access it:
	```
	[opc@exastb-node1 ~]$ dcli -g ~/dbs_group -l opc
	 sudo chown oracle:oinstall /mnt/dbfs
	```

Step 3.2 - (PDB Only) Create an Entry in TNSNAMES

1. As the `oracle` OS user on the standby system, add a connect entry in `$TNS_ADMIN/tnsnames.ora` file. Use the PDB service name created in Step 2.3:
	```
	[oracle@exadb-node1 ~]$ vi $TNS_ADMIN/tnsnames.ora
	dbfs =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL = IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <PDB_SERVICE_NAME> )
	       )
	    )
	```
2. As the `oracle` OS user, distribute the `$TNS_ADMIN/tnsnames.ora` file to the rest of the nodes:
	```
	[oracle@exadb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group
	 -f $TNS_ADMIN/tnsnames.ora -d $TNS_ADMIN/
	```

Step 3.3 - Copy and Edit the mount-dbfs Scripts from the Primary System

1. As the `root` OS user on the primary system, create a zip file with the files `mount-dbfs.conf` and `mount-dbfs.sh`:
	```
	[opc@exapri-node1 ~]$ sudo su -
	[root@exapri-node1 ~]# zip -j /tmp/mount-dbfs.zip
	 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script/mount-dbfs.sh
	 /etc/oracle/mount-dbfs.conf
	  adding: mount-dbfs.sh (deflated 67%)
	  adding: mount-dbfs.conf (deflated 58%)
	```
2. As the `opc` OS user on the standby system, copy the `mount-dbfs.zip` file from the primary system to the standby system:
	```
	[opc@exastb-node1 ~]$ scp exapri-node1.oracle.com:/tmp/mount-dbfs.zip /tmp
	```
3. As the `opc` OS user on the standby system, unzip the `mount-dbfs.zip` file and edit the configuration file `mount-dbfs.conf`:
	```
	[opc@exastb-node1 ~]$ unzip /tmp/mount-dbfs.zip -d /tmp
	Archive:  /tmp/mount-dbfs.zip
	  inflating: /tmp/mount-dbfs.sh     
	  inflating: /tmp/mount-dbfs.conf 
	[opc@exastb-node1 ~]$ vi /tmp/mount-dbfs.conf
	```
	It is recommended that you place them in the same directory as the primary system. You will need to modify the following parameters in the `mount-dbfs.conf` file to match the standby database:
	- `DBNAME`
		- `TNS_ADMIN`
		- `PDB_SERVICE`
4. As the `opc` OS user on the standby system, copy `mount-dbfs.conf` to the directory `/etc/oracle` on database nodes and set proper permissions on it:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc -d /tmp
	 -f /tmp/mount-dbfs.conf
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 cp /tmp/mount-dbfs.conf /etc/oracle
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 chown oracle:oinstall /etc/oracle/mount-dbfs.conf
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo
	 chmod 660 /etc/oracle/mount-dbfs.conf
	```
5. As the `opc` OS user on the standby system, copy `mount-dbfs.sh` to the directory `$GI_HOME/crs/script` on database nodes and set proper permissions on it:
	```
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo mkdir
	 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l opc sudo chown
	 grid:oinstall $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l grid
	 -d $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script
	 -f /tmp/mount-dbfs.sh
	[opc@exastb-node1 ~]$ /usr/local/bin/dcli -g ~/dbs_group -l grid chmod 770
	 $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/crs/script/mount-dbfs.sh
	```

Step 3.3 - Register the DBFS Resource with Oracle Clusterware

When registering the resource with Oracle Clusterware, be sure to create it as a cluster\_resource. The reason for using cluster\_resource is so the file system can only by mounted on a single node at one time, preventing mounting of DBFS from concurrent nodes creating the potential of concurrent file writes, causing file corruption problems.

If using Oracle Multitenant, make sure to use the service name for the same PDB that contains the DBFS repository as was created in the primary database.

1. As the `grid` OS user on the standby system, find the resource name for the database service created in a previous step for the DBFS service dependency:
	```
	[opc@exastb-node1 ~]$ sudo su - grid
	[grid@exastb-node1 ~]$ crsctl stat res |grep <PDB_NAME>
	NAME=ora.<DB_UNIQUE_NAME>.<PDB_SERVICE_NAME>.svc
	```
2. As the oracle OS user on the standby system, register the Clusterware resource by executing the following script:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ vi add-dbfs-resource.sh
	##### start script add-dbfs-resource.sh
	#!/bin/bash
	ACTION_SCRIPT=$(grep ^crs_home /etc/oracle/olr.loc | cut -d=
	 -f2)/crs/script/mount-dbfs.sh
	RESNAME=dbfs_mount
	DEPNAME=ora.<DB_UNIQUE_NAME>.<PDB_SERVICE_NAME>.svc
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
	[oracle@exadb-node1 ~]$ sh add-dbfs-resource.sh
	```

Note:

After creating the `$RESNAME` resource, in order to stop the `$DBNAME` database when the `$RESNAME` resource is `ONLINE`, you will have to specify the force flag when using `srvctl`.

For example: `srvctl stop database -d $ORACLE_UNQNAME -f`
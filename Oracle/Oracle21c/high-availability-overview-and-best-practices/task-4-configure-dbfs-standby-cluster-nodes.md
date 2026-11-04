---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-4-configure-dbfs-standby-cluster-nodes.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 4: Configure DBFS on the Standby Cluster Nodes

The Database File System (DBFS) is the only recommended solution when configuring Oracle GoldenGate with Oracle Data Guard.

The DBFS user, tablespace, and file system in the database was previously created in the primary database, as detailed in [Task 4: Set Up a File System on Oracle RAC](task-4-set-file-system-oracle-rac.md).

The remaining configuration steps are required on all nodes of the standby cluster where Oracle GoldenGate may run.

1. Install the required FUSE libraries, if they are not already installed, by following the instructions in [My Oracle Support Document 869822.1](https://support.oracle.com/rs?type=doc&id=869822.1).
2. Create the `tnsnames.ora` Oracle Net connection alias using the IPC protocol, similar to the one created on the primary cluster.
	```
	dbfs =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL = IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = NAME)
	       )
	    )
	```
3. Create the same mount point for DBFS that is used on the primary cluster.
	It is important that the mount point is identical, because the physical location of the Oracle GoldenGate deployment is included in the deployment configuration files.
	For example:
	```
	# mkdir /mnt/dbfs
	```
4. Copy the `mount-dbfs.conf` and `mount-dbfs.sh` files from the primary cluster to the standby cluster nodes.
	It is recommended that you place them in the same directory as the primary cluster.
5. Register the DBFS resource with Oracle Clusterware, using the following example command.
	If you are using Oracle Multitenant, make sure to use the service name for the same PDB that contains the DBFS repository as was created in the primary database.
	```
	DBNAME=dbName
	DEPNAME=ora.$DBNAME.oggserv_pdb.svc
	crsctl add resource $RESNAME \
	  -type cluster_resource \
	  -attr "ACTION_SCRIPT=$ACTION_SCRIPT, \
	         CHECK_INTERVAL=30,RESTART_ATTEMPTS=10, \
	         START_DEPENDENCIES='hard($DEPNAME)pullup($DEPNAME)',\
	         STOP_DEPENDENCIES='hard($DEPNAME)',\
	         SCRIPT_TIMEOUT=300"
	```
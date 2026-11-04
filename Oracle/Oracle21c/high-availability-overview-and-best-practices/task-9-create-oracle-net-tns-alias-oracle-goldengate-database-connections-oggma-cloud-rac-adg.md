---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-9-create-oracle-net-tns-alias-oracle-goldengate-database-connections-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 9 - Create Oracle Net TNS Alias for Oracle GoldenGate Database Connections

The same TNS aliases created on the primary system for the primary database using the IPC protocol must be created with the same alias names on each database node of the standby system, using the IPC communication protocol as specified in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md).

The location of the `tnsnames.ora` used by the Oracle GoldenGate deployment must be identical on the standby system nodes as it is on the primary system.

1. As the `oracle` user on the primary system, use the following query REST API call to query the `TNS_ADMIN` location:
	```
	[opc@exapri-node1 ~]$ sudo su - oracle
	[oracle@exapri-node1 ~]$ grep -1 TNS_ADMIN
	 /mnt/dbfs/goldengate/deployments/ggsm1/etc/conf/deploymentRegistry.dat
	            {
	                "name": "TNS_ADMIN",
	                "value": "/u02/app/oracle/goldengate/network/admin"
	```
	Make sure the `tnsnames.ora` is in this same directory on all standby database nodes.
2. As the `oracle` OS user on the standby system, follow the steps to create the TNS alias definitions and distribute to all database nodes:
	```
	[opc@exastb-node1 ~]$ sudo su - oracle
	[oracle@exastb-node1 ~]$ dcli -l oracle -g ~/dbs_group mkdir
	 -p /u02/app/oracle/goldengate/network/admin
	[oracle@exastb-node1 ~]$ vi /u02/app/oracle/goldengate/network/admin/tnsnames.ora
	OGGSRV_CDB =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <CDB_SERVICE_NAME>)
	       )
	    )
	OGGSRV_<PDB_NAME> =
	    (DESCRIPTION =
	      (ADDRESS = (PROTOCOL=IPC)(KEY=LISTENER))
	      (CONNECT_DATA =
	        (SERVICE_NAME = <PDB_SERVICE_NAME>)
	       )
	    )
	[oracle@exastb-node1 ~]$ /usr/local/bin/dcli -l oracle -g ~/dbs_group
	 -f /u02/app/oracle/goldengate/network/admin/*.ora
	 -d /u02/app/oracle/goldengate/network/admin
	```

Note:

When the tnsnames.ora or `sqlnet.ora` located in the `TNS_ADMIN` directory for the Oracle GoldenGate deployment are modified, the deployment needs to be restarted in order to pick up the changes.
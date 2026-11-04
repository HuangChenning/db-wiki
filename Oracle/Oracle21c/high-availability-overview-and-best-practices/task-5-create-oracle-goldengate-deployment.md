---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-5-create-oracle-goldengate-deployment.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 5 - Create the Oracle GoldenGate Deployment

When the Oracle GoldenGate software has been installed, your next step is to create a response file to create the Oracle GoldenGate deployment using the Oracle GoldenGate Configuration Assistant.

Perform the following steps to complete this task:

- Step 5.1 - Create a Response File
- Step 5.2 - Create the GoldenGate Deployment
- Step 5.3 - (only if using DBFS) Move the GoldenGate Deployment Temp Directory

Step 5.1 - Create a Response File

For a silent configuration, as the `oracle` OS user, create and edit the response file `oggca.rsp` to create the Oracle GoldenGate deployment:

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ vi /u02/app_acfs/goldengate/oggca.rsp
oracle.install.responseFileersion=/oracle/install/rspfmt_oggca_response_schema_v21_1_0

CONFIGURATION_OPTION=ADD
DEPLOYMENT_NAME=<ggNN>
ADMINISTRATOR_USER=oggadmin
ADMINISTRATOR_PASSWORD=<password_for_oggadmin>
SERVICEMANAGER_DEPLOYMENT_HOME=<ACFS or DBFS mount point>/deployments/<ggsmNN>
HOST_SERVICEMANAGER=localhost
PORT_SERVICEMANAGER=9100
SECURITY_ENABLED=false
STRONG_PWD_POLICY_ENABLED=true
CREATE_NEW_SERVICEMANAGER=true
REGISTER_SERVICEMANAGER_AS_A_SERVICE=false
INTEGRATE_SERVICEMANAGER_WITH_XAG=true
EXISTING_SERVICEMANAGER_IS_XAG_ENABLED=false
OGG_SOFTWARE_HOME=/u02/app/oracle/goldengate/gg21c
OGG_DEPLOYMENT_HOME=<ACFS or DBFS mount point>/deployments/<ggNN>
ENV_LD_LIBRARY_PATH=${OGG_HOME}/lib/instantclient:${OGG_HOME}/lib
ENV_TNS_ADMIN=/u02/app/oracle/goldengate/network/admin
FIPS_ENABLED=false
SHARDING_ENABLED=false
ADMINISTRATION_SERVER_ENABLED=true
PORT_ADMINSRVR=9101
DISTRIBUTION_SERVER_ENABLED=true
PORT_DISTSRVR=9102
NON_SECURE_DISTSRVR_CONNECTS_TO_SECURE_RCVRSRVR=false
RECEIVER_SERVER_ENABLED=true
PORT_RCVRSRVR=9103
METRICS_SERVER_ENABLED=true
METRICS_SERVER_IS_CRITICAL=false
PORT_PMSRVR=9104
UDP_PORT_PMSRVR=9105
PMSRVR_DATASTORE_TYPE=BDB
PMSRVR_DATASTORE_HOME=/u02/app/oracle/goldengate/datastores/<instance_name>
OGG_SCHEMA=<goldengate_database_schema>
```

In the response file, edit the following values appropriately:

- `CONFIGURATION_OPTION`
- `DEPLOYMENT_NAME`
- `ADMINISTRATOR_USER`
- `SERVICEMANAGER_DEPLOYMENT_HOME`
- `OGG_SOFTWARE_HOME`
- `OGG_DEPLOYMENT_HOME`
- `ENV_TNS_ADMIN`
- `OGG_SCHEMA`

Step 5.2 - Create the GoldenGate Deployment

As the `oracle` OS user on the first database node, run `oggca.sh` to create the Oracle GoldenGate deployment:

```
[opc@exadb-node1 ~]$ sudo su - oracle
[oracle@exadb-node1 ~]$ export OGG_HOME=/u02/app/oracle/goldengate/gg21c
[oracle@exadb-node1 ~]$ $OGG_HOME/bin/oggca.sh -silent
 -responseFile /u02/app_acfs/goldengate/oggca.rsp
Successfully Setup Software.
```

Step 5.3 - (only if using DBFS) Move the GoldenGate Deployment Temp Directory

After the deployment has been created, if you use DBFS for the shared file system, run the following commands to move the GoldenGate deployment temp directory from DBFS to local storage.

1. As the `oracle` OS user on the first database node, move the GoldenGate deployment temporary directory to the local storage:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ dcli -l oracle -g ~/dbs_group mkdir
	 -p /u02/app/oracle/goldengate/deployments/<instance_name>
	[oracle@exadb-node1 ~]$ mv
	 /mnt/dbfs/goldengate/deployments/<instance_name>/var/temp
	 /u02/app/oracle/goldengate/datastores/<instance_name>
	[oracle@exadb-node1 ~]$ ln -s
	 /u02/app/oracle/goldengate/deployments/<instance_name>/temp
	 /mnt/dbfs/goldengate/deployments/<instance_name>/var/temp
	```
2. As the `oracle` OS user on the rest of the database nodes, create a directory on the local storage:
	```
	[oracle@exadb-node2 ~]$ mkdir
	 /u02/app/oracle/goldengate/deployments/<instance_name>
	```
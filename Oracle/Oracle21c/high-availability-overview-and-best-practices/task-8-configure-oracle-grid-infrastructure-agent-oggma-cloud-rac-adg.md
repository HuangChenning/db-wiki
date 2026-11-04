---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-8-configure-oracle-grid-infrastructure-agent-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 8 - Configure Oracle Grid Infrastructure Agent

The following procedure shows you how to configure Oracle Clusterware to manage Oracle GoldenGate using the Oracle Grid Infrastructure Standalone Agent (XAG).

Using XAG automates the mounting of the shared file system (DBFS) as well as the stopping and starting of the Oracle GoldenGate deployment when relocating between Oracle RAC nodes.

Perform the following steps to complete this task:

- Step 8.1 - Modify the Primary Cluster XAG GoldenGate Instance
- Step 8.2 - Install Oracle Grid Infrastructure Agent
- Step 8.3 - Configure Oracle Grid Infrastructure Agent
Step 8.1 - Modify the Primary Cluster XAG GoldenGate Instance

The Oracle Grid Infrastructure Standalone Agent (XAG) GoldenGate instance on the primary system, must be modified to identify that it is part of an Oracle Data Guard configuration.

As the root user on the primary system, use the following command to modify the Oracle Data Guard `autostart` flag:

```
[opc@exapri-node1 ~]$ sudo su -
[root@exapri-node1 ~]# /u01/app/grid/xag/bin/agctl modify goldengate <instance_name>
 --dataguard_autostart yes
```

Step 8.2 - Install Oracle Grid Infrastructure Agent

On the standby system, follow the instructions in “Step 7.1 - Install the Oracle Grid Infrastructure Standalone Agent” from [Task 7 - Configure Oracle Grid Infrastructure Agent](task-7-configure-oracle-grid-infrastructure-agent-xag.md).

Step 8.3 - Configure Oracle Grid Infrastructure Agent

The parameters used to register Oracle GoldenGate Microservices with XAG are similar to those used when registering with the primary system.

1. As the `grid` user on the primary system, use the following command to determine the current parameters in the primary system:
	```
	[grid@exapri-node1 ~]$ agctl config goldengate <instance_name>
	Instance name: <instance_name>
	Application GoldenGate location is: /u02/app/oracle/goldengate/gg21c
	Goldengate MicroServices Architecture environment: yes
	Goldengate Service Manager configuration directory:
	 /mnt/dbfs/goldengate/deployments/<instance_name>/etc/conf
	Goldengate Service Manager var directory:
	 /mnt/dbfs/goldengate/deployments/<instance_name>/var
	Service Manager Port: 9100
	Goldengate Administration User: oggadmin
	Autostart on DataGuard role transition to PRIMARY: yes
	Configured to run on Nodes: exapri-node1 exapri-node2
	ORACLE_HOME location is: /u02/app/oracle/goldengate/gg21c/lib/instantclient
	Database Services needed: ora.<DB_UNIQUE_NAME>.<SERVICE_NAME>.<FQDN>.svc
	File System resources needed: dbfs_mount,nginx
	Network: 1, IP:<VIP>, User:oracle, Group:oinstall
	```
	In addition, the XAG parameter `--filesystem_verify no` must be specified to prevent XAG from checking the existence of the DBFS deployment directory when registering the Oracle GoldenGate instance. Without setting this parameter, the XAG registration will fail, because DBFS is not mounted on the standby system.
	Note:
	It is recommended to use the same GoldenGate instance name when registering GoldenGate with XAG as was used in the primary system.
2. As the `root` user on the standby system, register Oracle GoldenGate Microservices Architecture with XAG use the following command format:
	```
	https://support.oracle.com/rs?type=doc&id=2193391.1
	http://www.oracle.com/pls/topic/lookup?ctx=db19&id=SBYDB
	[root@exastb-node1 ~]# /u01/app/grid/xag/bin/agctl add goldengate <instance_name> \
	--gg_home /u02/app/oracle/goldengate/gg21c \
	--service_manager \
	--config_home /mnt/dbfs/goldengate/deployments/<ggsm1>/etc/conf \
	--var_home /mnt/dbfs/goldengate/deployments/<ggsm1>/var \
	--port 9100 \
	--oracle_home /u02/app/goldengate/gg21c/lib/instantclient \
	--adminuser oggadmin \
	--user oracle \
	--group oinstall \
	--network 1 --ip <virtual_IP_address> \
	--filesystems dbfs_mount,nginx \
	--db_services ora.<DB_UNIQUE_NAME>.<SERVICE_NAME>.<FQDN>.svc \
	--use_local_services \
	--nodes <exastb-node1>,<exastb-node2> \
	--filesystem_verify no \
	--dataguard_autostart yes
	```
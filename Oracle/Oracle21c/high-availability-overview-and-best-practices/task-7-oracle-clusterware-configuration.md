---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-7-oracle-clusterware-configuration.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 7: Oracle Clusterware Configuration

The following procedure shows you how to configure Oracle Clusterware to manage Oracle GoldenGate using the Oracle Grid Infrastructure Standalone Agent (XAG).

Using XAG automates the mounting of the shared file system (DBFS or ACFS) and the stopping and starting of the GoldenGate deployment when relocating between Oracle RAC nodes.

1. Install the Oracle Grid Infrastructure Standalone Agent.
	It is recommended that you install the XAG software as a standalone agent outside of the Grid Infrastructure ORACLE\_HOME. This allows you to use the latest XAG release available, and the software can be updated without impact to the Grid Infrastructure.
	When using Oracle GoldenGate Microservices Architecture you MUST use XAG version 10.2 or later.
	The latest agent software is available for download from the following location:
	[http://www.oracle.com/technetwork/database/database-technologies/clusterware/downloads/xag-agents-downloads-3636484.html](http://www.oracle.com/technetwork/database/database-technologies/clusterware/downloads/xag-agents-downloads-3636484.html)
	Install the XAG standalone agent outside of the Oracle Grid Infrastructure home directory. XAG must be installed in the same directory on all RAC nodes in the cluster where Oracle GoldenGate is installed.
	For example, as the Oracle Grid Infrastructure user, the default of oracle:
	```
	$ ./xagsetup.sh --install --directory /u01/oracle/xag --all_nodes
	```
	Add the location of the newly installed XAG software to the PATH variable so that the location of `agctl` is known when the `oracle` user logs on to the machine.
	```
	$ cat .bashrc
	export PATH=/u01/oracle/xag/bin:$PATH
	```
	Note:
	It is important to make sure that the XAG bin directory is specified BEFORE the Grid Infrastructure bin directory, to ensure the correct agctl binary is found. Set this location in the oracle user environment to take effect at time of logging on, such as in the.bashrc file when the Bash shell is in use.
2. Prepare for Application Virtual IP Address (VIP) Creation.
	A dedicated application VIP is required to allow access to the GoldenGate Microservices using the same host name, regardless of which Oracle RAC node is hosting the services. An application VIP also ensures that the GoldenGate Distribution Server can communicate with the Distribution Receiver running the current Oracle RAC node.
	The VIP is a cluster resource that Oracle Clusterware manages. The VIP is assigned to a cluster node and is automatically migrated to another node in the event of a node failure.
	There are two pieces of information needed before creating the application VIP:
	- The network number, which can be identified using the following command.
		```
		$ crsctl status resource -p -attr ADDRESS_TYPE,NAME,USR_ORA_SUBNET -w "TYPE = ora.network.type" |sort | uniq
		ADDRESS_TYPE=IPV4
		NAME=ora.net1.network
		USR_ORA_SUBNET=10.133.16.0
		```
		The net1 in `NAME=ora.net1.network` indicates that this is network 1, and it is of type IPV4.
		- The IP address for the new Application VIP, provided by your system administrator. This IP address must be in the same subnet of the cluster environment as determined above.
		The VIP will be created in the next step, when configuring the Oracle Grid Infrastructure Agent.
3. Configure Oracle Grid Infrastructure Agent (XAG).
	Oracle GoldenGate must be registered with XAG so that the deployment is started and stopped automatically when the database is started and the file system is mounted.
	To register Oracle GoldenGate Microservices Architecture with XAG use the following command format.
	```
	agctl add goldengate instance_name
	  --gg_home GoldenGate_Home
	  --service_manager
	  --config_home GoldenGate_SvcMgr_Config
	  --var_home GoldenGate_SvcMgr_Var_Dir
	  --port port_number
	  --oracle_home $OGG_HOME/lib/instantclient
	  --adminuser OGG_admin_user
	  --user GG_instance_user
	  --group GG_instance_group
	  --network network_number
	  --ip ip_address
	  --vip_name vip_name
	  --filesystems CRS_resource_name
	  --db_services service_name
	  --use_local_services
	  --nodes node1, node2, ... ,nodeN
	```
	Where:
	`--gg_home` specifies the location of the Oracle GoldenGate software. Specify the `OGG_HOME` symbolic link for the `OGG_HOME` if registering multiple Service Managers (see Task 6: Create the Oracle GoldenGate Deployment).
	`--service_manager` indicates this is a GoldenGate Microservices instance.
	`--config_home` specifies the GoldenGate Service Manager deployment configuration home directory.
	`--var_home` specifies the GoldenGate Service Manager deployment variable home directory.
	`--port` specifies the deployment Service Manager port number.
	`--oracle_home` specifies the location of the Oracle database libraries that are included as part of Oracle GoldenGate 21c and later releases. Example: `$OGG_HOME/lib/instantclient`
	`--adminuser` specifies the Oracle GoldenGate Microservices administrator account name.
	`--user` specifies the name of the operating system user that owns the GoldenGate deployment.
	`--group` specifies the name of the operating system group that owns the GoldenGate deployment.
	`--network` specifies the network subnet for the VIP, determined above.
	`--ip` specifies the IP address for the VIP, which was determined above. If you have already created a VIP, then specify it using the `--vip_name` parameter in place of `--network` and `--ip`.
	`--vip_name` specifies a CRS resource name for an application VIP that has previously been created. This parameter replaces `--network` and `-–ip` (optional).
	`--filesystems` specifies the DBFS or ACFS CRS file system resource that must be mounted before the deployment is started.
	`--db_services` specifies the `ora.database.service_name.svc` service name that was created in the previous step. If using Oracle Multitenant Database, specify the PDB database service for Replicat, or the CDB database service for an Extract. If using both Replicat and Extract, specify both services names, separated by a comma.
	`--use_local_services` specifies that the GoldenGate instance must be co-located on the same Oracle RAC node where the `db_services` service is running.
	`--nodes` specifies which of the Oracle RAC nodes this GoldenGate instance can run on. If GoldenGate is configured to run on any of the Oracle RAC nodes in the cluster, this parameter should still be used to determine the preferred order of nodes to run Oracle GoldenGate.

Notes:

- The GoldenGate instance registration with XAG MUST be run as the `root` user.
- The `user` and `group` parameters are mandatory because the GoldenGate registration with XAG is run as the `root` user.

Below are some examples of registering Oracle GoldenGate with XAG.

Example 1: Oracle RAC cluster using DBFS, using an already created application VIP

```
# agctl add goldengate GGNORTH \
--gg_home /u01/oracle/goldengate/gg21c_MS \
--service_manager \
--config_home /mnt/dbfs/goldengate/deployments/ggsm01/etc/conf \
--var_home /mnt/dbfs/goldengate/deployments/ggsm01/var \
--port 9100 \
--oracle_home /u01/oracle/goldengate/gg21c_MS/lib/instantclient
--adminuser oggadmin
--user oracle \
--group oinstall \
--vip_name gg_vip_prmy \
--filesystems dbfs_mount \
--db_services ora.ds19c.oggserv.svc \
--use_local_services \
--nodes dc1north01,dc1north02
```

Where:

- GoldenGate instance is GGNORTH
- GoldenGate home directory is `/u01/oracle/goldengate/gg21c_MS`
- This is an Oracle GoldenGate Microservices Architecture instance (`--service_manager`)
- GoldenGate deployment configuration home directory is `/mnt/dbfs/goldengate/deployments/ggsm01/etc/conf`
- GoldenGate deployment variable home directory is `/mnt/dbfs/goldengate/deployments/ggsm01/var`
- Deployment Service Manager port number is 9100
- Oracle GoldenGate Microservices administrator account name is `oggadmin`
- The GoldenGate user is `oracle` in the group `oinstall`
- Application VIP name, managed by CRS, is called `gg_vip_prmy`
- The CRS resource name for the file system the deployment depends on is `dbfs_mount`
- The GoldenGate instance will be started on the same Oracle RAC node as the CRS service called `ora.ds19c.oraserv.svc` will be co-located on the same node as this GoldenGate instance.

Example 2: Oracle RAC cluster, using ACFS, with an application VIP running on a subset of the nodes in the cluster.

```
# agctl add goldengate GGNORTH \
--gg_home /u01/oracle/goldengate/gg21c_MS \
--service_manager \
--config_home /mnt/acfs/goldengate/deployments/ggsm01/etc/conf \
--var_home /mnt/acfs/goldengate/deployments/ggsm01/var \
--port 9100 \
--oracle_home /u01/oracle/goldengate/gg21c_MS/lib/instantclient
--adminuser admin \
--user oracle \
--group oinstall \
--network 1 --ip 10.13.11.203 \
--filesystems ora.datac1.acfs_gg.acfs \
--db_services ora.ds19c.oraserv.svc \
--use_local_services \
--nodes dc1north01,dc1north02
```

Where:

- GoldenGate instance is GGNORTH
- GoldenGate home directory is `/u01/oracle/goldengate/gg21c_MS`
- This is an Oracle GoldenGate Microservices Architecture instance (`--service_manager`)
- GoldenGate deployment configuration home directory is `/mnt/acfs/goldengate/deployments/ggsm02/etc/conf`
- GoldenGate deployment variable home directory is `/mnt/acfs/goldengate/deployments/ggsm02/var`
- Deployment Service Manager port number is 9100
- Oracle GoldenGate Microservices administrator account name is `admin`
- GoldenGate user is `oracle` in the group `oinstall`
- The network is the default `ora.net1.network` and the VIP is `10.13.11.203`
- The CRS resource name for the file system the deployment depends on is `ora.datac1.acfs_gg.acfs`
- This GoldenGate instance will be started on the same Oracle RAC node as the CRS service called `ora.ds19c.oraserv.svc` will be co-located on the same node as this GoldenGate instance
- Oracle GoldenGate will only run on Oracle RAC nodes dc1north01 and dc1north02, listed in priority order.

Example AGCTL Commands

Below are some example agctl commands that are used to manage the Oracle GoldenGate deployment with XAG.

To check the status of Oracle GoldenGate:

```
% agctl status goldengate
Goldengate  instance 'GGNORTH' is running on dc1north01
```

To start the GoldenGate deployment, and all Extract/Replicat processes that have been configured to autostart (instructions in a later step):

```
% agctl start goldengate GGNORTH --node dc1north02
```

To stop the GoldenGate deployment:

```
% agctl stop goldengate GGNORTH
```

To manually relocate the GoldenGate deployment to another node:

```
% agctl relocate goldengate GGNORTH --node dc1north02
```

To view the configuration parameters for the GoldenGate resource:

```
% agctl config goldengate GGNORTH

Instance name: GGNORTH
Application GoldenGate location is: /u01/oracle/goldengate/gg21c_MS
Goldengate MicroServices Architecture environment: yes
Goldengate Service Manager configuration directory: /mnt/dbfs/goldengate/deployments/ggsm01/etc/conf

Goldengate Service Manager var directory: /mnt/dbfs/goldengate/deployments/ggsm01/var

Service Manager Port: 9100
Goldengate Administration User: oggadmin
Autostart on DataGuard role transition to PRIMARY: no
Configured to run on Nodes: dc1north01 dc1north02
ORACLE_HOME location is: /u01/oracle/goldengate/gg21c_MS/lib/instantclient
Database Services needed: ora.cdb1.oggcdb.svc [use_local_services]
File System resources needed: ora.datac1.acfs_gg.acfs
Network: 1, IP: 10.13.11.203, User:oracle, Group:oinstall
```

To delete the GoldenGate XAG resource:

```
$ agctl stop goldengate GGNORTH
# agctl remove goldengate GGNORTH
```

For more information about the Oracle Grid Infrastructure Bundled Agent see [Oracle Grid Infrastructure Standalone Agents for Oracle Clusterware 11g Rel. 2, 12c, 18c and 19c](https://www.oracle.com/database/technologies/xag-agents-download.html).
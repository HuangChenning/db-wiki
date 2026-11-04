---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-7-configure-oracle-grid-infrastructure-agent-xag.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 7 - Configure Oracle Grid Infrastructure Agent

The following procedure shows you how to configure Oracle Clusterware to manage Oracle GoldenGate using the Oracle Grid Infrastructure Standalone Agent (XAG).

Using XAG automates the mounting of the shared file system (DBFS or ACFS) as well as the stopping and starting of the Oracle GoldenGate deployment when relocating between Oracle RAC nodes.

Perform the following steps to complete this task:

- Step 7.1 - Install the Oracle Grid Infrastructure Standalone Agent
- Step 7.2 - Configure Oracle Grid Infrastructure Agent
- Step 7.2 - Start the Oracle GoldenGate Deployment

Step 7.1 - Install the Oracle Grid Infrastructure Standalone Agent

It is recommended that you install the XAG software as a standalone agent outside the Grid Infrastructure `ORACLE_HOME`. This way, you can use the latest XAG release available, and the software can be updated without impact to the Grid Infrastructure.

XAG must be installed in the same directory on all Oracle RAC database nodes in the system where Oracle GoldenGate is installed.

1. As the `grid` OS user on the first database node, unzip the software and run `xagsetup.sh`:
	```
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ unzip /u02/app_acfs/goldengate/p31215432_190000_Generic.zip
	 -d /u02/app_acfs/goldengate
	[grid@exadb-node1 ~]$ /u02/app_acfs/goldengate/xag/xagsetup.sh --install
	 --directory /u01/app/grid/xag --all_nodes
	Installing Oracle Grid Infrastructure Agents on: exadb-node1
	Installing Oracle Grid Infrastructure Agents on: exadb-node2
	Updating XAG resources.
	Successfully updated XAG resources.
	```
2. Add the location of the newly installed XAG software to the `PATH` variable so that the location of `agctl` is known when the `grid` user logs on to the machine.
	```
	[grid@exadb-node1 ~]$ grep PATH ~/.bashrc
	PATH=
	/u01/app/grid/xag/bin:/sbin:/bin:/usr/sbin:/usr/bin:/u01/app/19.0.0.0/grid/bin:/u01/app/19.0.0.0/grid/OPatch;
	 export PATH
	```

Note:

It is essential that you ensure that the XAG `bin` directory is specified before the Grid Infrastructure `bin` directory to ensure that the correct `agctl` binary is found. This should be set in the `grid` user environment to take effect when logging on, such as in the `.bashrc` file when the Bash shell is in use.

Step 7.2 - Configure Oracle Grid Infrastructure Agent

The following procedure shows you how to configure Oracle Clusterware to manage Oracle GoldenGate using the Oracle Grid Infrastructure Standalone Agent (XAG).

Using XAG automates the mounting of the shared file system (DBFS or ACFS) as well as the stopping and starting of the Oracle GoldenGate deployment when relocating between Oracle RAC nodes.

Oracle GoldenGate must be registered with XAG so that the deployment is started and stopped automatically when the database is started and the file system is mounted.

To register Oracle GoldenGate Microservices Architecture with XAG, use the following command format:

```
agctl add goldengate <instance_name>
--gg_home <GoldenGate_Home>
--service_manager
--config_home <GoldenGate_SvcMgr_Config>
--var_home <GoldenGate_SvcMgr_Var Dir>
--port <port number>
--oracle_home <$OGG_HOME/lib/instantclient>
--adminuser <OGG admin user>
--user <GG instance user>
--group <GG instance group>
--network <network_number>
--ip <ip_address>
--vip_name <vip_name>
--filesystems <CRS_resource_name>
--db_services <service_name>
--use_local_services
--attribute START_TIMEOUT=60
--nodes <node1, node2, ... ,nodeN>
```

Where:

- `--gg_home` specifies the location of the Oracle GoldenGate software.
- `--service_manager` indicates this is a GoldenGate Microservices instance.
- `--config_home` specifies the GoldenGate Service Manager deployment configuration home directory.
- `--var_home` specifies the GoldenGate Service Manager deployment variable home directory.
- `--port` specifies the deployment Service Manager port number.
- `--oracle_home` specifies the location of the Oracle database libraries that are included as part of Oracle GoldenGate 21c and later releases.
	Example: `$OGG_HOME/lib/instantclient`
- `--adminuser` specifies the Oracle GoldenGate Microservices administrator account name.
- `--user` specifies the name of the operating system user that owns the Oracle GoldenGate deployment.
- `--group` specifies the name of the operating system group that owns the Oracle GoldenGate deployment.
- `--network` specifies the network subnet for the VIP.
- `--ip` specifies the IP address for the VIP.
	If you have already created a VIP, specify it using the `--vip_name                                 vip_name` parameter in place of `--network` and `--ip`.
- `--vip_name` specifies a CRS resource name for an application VIP previously created.
	This parameter replaces `--network` and `––ip` (optional).
- `--filesystems` specifies the DBFS or ACFS CRS file system resource that must be mounted before the deployment is started.
- `--db_services` specifies the `ora.<database>.<service_name>.svc` service name created in the previous step.
	If you are using Oracle Multitenant Database, specify the PDB database service for Replicat or the CDB database service for an Extract. If using Replicat and Extract, specify both service names, separated by a comma.
- `--use_local_services` specifies that the Oracle GoldenGate instance must be co-located on the same Oracle RAC node where the `db_services` service is running.
- `--attribute                         name=value` specifies attributes that can be applied.
	It is recommended that you modify the attribute `START_TIMEOUT=60` to optimize the blackout after a database crash and restart.
- `--nodes` specifies which of the Oracle RAC nodes this GoldenGate instance can run on.
	If Oracle GoldenGate is configured to run on any of the Oracle RAC nodes in the cluster, this parameter should still be used to determine the preferred order of nodes to run Oracle GoldenGate.

Perform one of the following steps to complete this task:

- Step 7.2a - GoldenGate Deployments on DBFS
- Step 7.2b - GoldenGate Deployments on ACFS

Step 7.2a - GoldenGate Deployments on DBFS

1. As the `grid` OS user on the first database node, run the following command to identify the network number:
	```
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ srvctl config network
	Network 1 exists
	Subnet IPv4: 10.1.0.0/255.255.255.0/bondeth0, static
	Subnet IPv6:
	Ping Targets: 10.1.0.1
	Network is enabled
	Network is individually enabled on nodes:
	Network is individually disabled on nodes:
	```
2. As the `root` OS user on the first database node, register Oracle GoldenGate Microservices Architecture with XAG using the following command format:
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# /u01/app/grid/xag/bin/agctl add goldengate <instance_name>     \
	--gg_home /u02/app/oracle/goldengate/gg21c                                           \
	--service_manager                                                                    \
	--config_home /mnt/dbfs/deployments/ggsm01/etc/conf                                  \
	--var_home /mnt/dbfs/deployments/ggsm01/var                                          \
	--port 9100                                                                          \
	--oracle_home /u02/app/oracle/goldengate/gg21c/lib/instantclient                     \
	--adminuser oggadmin                                                                 \
	--user oracle                                                                        \
	--group oinstall                                                                     \
	--network 1 --ip <virtual_IP_address>                                                \
	--filesystems <dbfs_mount_name>                                                      \
	--db_services ora.<db_service_name>.svc , ora.<pdb_service_name>.svc                 \
	--use_local_services                                                                 \
	--attribute START_TIMEOUT=60                                                         \
	--nodes <exadb-node1>, <exadb-node2>
	Enter password for 'oggadmin' : <oggadmin_password>
	```

Step 7.2b - GoldenGate Deployments on ACFS

1. As the `grid` OS user on the first database node, run the following command to identify the network number:
	```
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ srvctl config network
	Network 1 exists
	Subnet IPv4: 10.1.0.0/255.255.255.0/bondeth0, static
	Subnet IPv6:
	Ping Targets: 10.1.0.1
	Network is enabled
	Network is individually enabled on nodes:
	Network is individually disabled on nodes:
	```
2. As the `root` OS user on the first database node, register Oracle GoldenGate Microservices Architecture with XAG using the following command format:
	```
	[root@exadb-node1 ~]# /u01/app/grid/xag/bin/agctl add goldengate <instance_name>     \
	--gg_home /u02/app/oracle/goldengate/gg21c                                           \
	--service_manager                                                                    \
	--config_home /mnt/acfs_gg/deployments/ggsm01/etc/conf                               \
	--var_home /mnt/acfs_gg/deployments/ggsm01/var                                       \
	--port 9100                                                                          \
	--oracle_home /u02/app/oracle/goldengate/gg21c/lib/instantclient                     \
	--adminuser oggadmin                                                                 \
	--user oracle                                                                        \
	--group oinstall                                                                     \
	--network 1 --ip <virtual_IP_address>                                                \
	--filesystems ora.<acfs_name>.acfs                                                   \
	--db_services ora.<db_service_name>.svc                                              \
	--use_local_services                                                                 \
	--attribute START_TIMEOUT=60                                                         \
	--nodes <exadb-node1>,<exadb-node2>
	```

Step 7.3 - Start the Oracle GoldenGate Deployment

Below are some example `agctl` commands used to manage the Oracle GoldenGate deployment with XAG.

1. As the `grid` OS user, run the following command to start the Oracle GoldenGate deployment:
	```
	[opc@exadb-node1 ~]$ sudo su - grid
	[grid@exadb-node1 ~]$ agctl start goldengate <instance_name>
	```
2. As the `grid` OS user, run the following command to check the status of the Oracle GoldenGate:
	```
	[grid@exadb-node1 ~]$ agctl status goldengate
	Goldengate instance <instance_name> is running on exadb-node1
	```
3. As the `grid` OS user, run the following command to view the configuration parameters for the Oracle GoldenGate resource:
	```
	[grid@exadb-node1 ~]$ agctl config goldengate <instance_name>
	Instance name: <instance_name>
	Application GoldenGate location is: /u02/app/oracle/goldengate/gg21c_MS
	Goldengate MicroServices Architecture environment: yes
	Goldengate Service Manager configuration directory:
	 /mnt/acfs_gg/deployments/ggsm01/etc/conf
	Goldengate Service Manager var directory: /mnt/acfs_gg/deployments/ggsm01/var
	Service Manager Port: 9100
	Goldengate Administration User: oggadmin
	Autostart on DataGuard role transition to PRIMARY: no
	Configured to run on Nodes: exadb-node1 exadb-node2
	ORACLE_HOME location is: /u02/app/oracle/goldengate/gg21c/lib/instantclient
	Database Services needed: ora.<db_unique_name>.<service_name>.svc [use_local_services]
	File System resources needed: ora.datac1.acfs_gg.acfs
	Network: 1, IP:NN.NN.NN.NN, User:oracle, Group:oinstall
	```

See [Oracle Grid Infrastructure Standalone Agents for Oracle Clusterware 11g Rel. 2, 12c, 18c and 19c](https://www.oracle.com/database/technologies/xag-agents-download.html) for more information about Oracle Grid Infrastructure Bundled Agent.
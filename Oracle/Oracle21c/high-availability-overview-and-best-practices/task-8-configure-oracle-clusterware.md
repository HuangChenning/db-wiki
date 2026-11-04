---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-8-configure-oracle-clusterware.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 8: Configure Oracle Clusterware

1. Modify the primary cluster XAG GoldenGate instance.
	The Oracle Grid Infrastructure Standalone Agent (XAG) GoldenGate instance on the primary cluster must be modified as the root user, to identify that it is part of an Oracle Data Guard configuration using the following example command.
	```
	# agctl modify goldengate instance_name --dataguard_autostart yes
	```
2. On the standby cluster, follow the instructions in [Task 7: Oracle Clusterware Configuration](task-7-oracle-clusterware-configuration.md) to do steps 3-5 below.
3. Install the XAG software on each standby cluster node.
	It is recommended that you install the XAG software into the same directory as the primary cluster.
4. Prepare for the XAG application VIP creation.
	It is assumed that the VIP and VIP name will be different from that of the primary cluster, so the VIP address will need to be allocated by your systems administrator for the standby cluster.
5. Register Oracle GoldenGate Microservices with XAG.
	The parameters used to register Oracle GoldenGate Microservices with XAG are similar to those used when registering with the primary cluster.
	1. Determine the current parameters in the primary cluster using the following command:
		```
		$ agctl config goldengate GoldenGate_instance_name
		Instance name: GoldenGate_instance_name
		Application GoldenGate location is: /u01/oracle/goldengate/gg21c_MS
		Goldengate MicroServices Architecture environment: yes
		Goldengate Service Manager configuration directory:
		 /mnt/dbfs/goldengate/deployments/ggnorth_sm/etc/conf
		Goldengate Service Manager var directory:
		 /mnt/dbfs/goldengate//deployments/ggnorth_sm/var
		Service Manager Port: 9100
		Goldengate Administration User: oggadmin
		Autostart on DataGuard role transition to PRIMARY: yes
		Configured to run on Nodes: dc1north01,dc1north02
		ORACLE_HOME location is: /u01/oracle/goldengate/gg21c_MS/lib/instantclient
		Database Services needed: ora.ggdg.oggserv_cdb.svc,ora.ggdg.oggserv_pdb.svc
		File System resources needed: dbfsgg,nginx
		VIP name: gg_vip_prmy
		```
		In addition, the XAG parameter `--filesystem_verify                                     no` must be specified to prevent XAG from checking the existence of the DBFS deployment directory when registering the GoldenGate instance. Without setting this parameter, the XAG registration will fail, because DBFS is not mounted on the standby cluster.
		Note:
		It is recommended that you use the same GoldenGate instance name when registering GoldenGate with XAG as was used in the primary cluster.
	2. Register GoldenGate with XAG on the standby cluster, as the `root` user:
		```
		# agctl add goldengate GoldenGate_instance_name \
		--gg_home /u01/oracle/goldengate/gg21c_MS \
		--service_manager \
		--config_home /mnt/dbfs/goldengate/deployments/ggnorth_sm/etc/conf \
		--var_home /mnt/dbfs/goldengate/deployments/ggnorth_sm/var \
		--port 9100 \
		--oracle_home /u01/goldengate/gg21c_MS/lib/instantclient \
		--adminuser oggadmin \
		--user oracle \
		--group oinstall \
		--vip_name gg_vip_stby \
		--filesystems dbfsgg,nginx \
		--db_services ora.ggdgs.oggserv_cdb.svc,ora.ggdgs.oggserv_pdb.svc \
		--use_local_services \
		--nodes dc2north01,dc2north02 \
		--filesystem_verify no \
		--dataguard_autostart yes
		```

For more information about the Oracle Grid Infrastructure Bundled Agent, see [http://www.oracle.com/technetwork/database/database-technologies/clusterware/downloads/xag-agents-downloads-3636484.html](http://www.oracle.com/technetwork/database/database-technologies/clusterware/downloads/xag-agents-downloads-3636484.html)
---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/sharding-deployment.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Sharded database deployment includes the prerequisites and instructions for installing the required software components, creating the catalog, roles, and the sharded database, configuring replication for high availability, and creating the schema for the sharded database.

The following topics contain the concepts and tasks you need to deploy a sharded database:

**Parent topic:** [Sharded Database Management](shard_part.md)

### 56.1 Introduction to SDB Deployment

Oracle Sharding provides the capability to automatically deploy the sharded database (SDB), which includes both the shards and the replicas.

The SDB administrator defines the topology (regions, shard hosts, replication technology) and invokes the DEPLOY command with a declarative specification using the GDSCTL command-line interface.

At a high level, the deployment steps are:

1. Set up the components.
	Note:
	In Oracle Database 12c Release 1 (12.2.0.1) all shards and shard catalog must be non-CDB databases.
	- Create a non-CDB database that hosts the shard catalog.
		- Install Oracle Database software on the shard nodes.
		- Install shard director (GSM) software on the shard director nodes.
	Note:
	For production deployments, it is highly recommended that you configure Data Guard for the shard catalog database.
2. Specify the topology layout using the following commands.
	- `CREATE SHARDCATALOG`
		- `ADD GSM`
		- `START GSM`
		- `ADD CREDENTIAL` (if using `CREATE SHARD`)
		- `ADD SHARDGROUP`
		- `ADD INVITEDNODE`
		- `CREATE SHARD` (or `ADD SHARD`) for each shard
3. Run `DEPLOY` and add the global service to access any shard in the SDB.
	- `DEPLOY`
		- `ADD SERVICE`

In Oracle Database 12c Release 1 (12.2.0.1) two replication schemes are supported. The SDB administrator can select either Data Guard or Active Data Guard while specifying the topology.

Deployment Methods: CREATE SHARD

Oracle Sharding supports two deployment methods. The first method is with the `CREATE SHARD` command, where the creation of shards and the replication configuration are automatically done by the Oracle Sharding management tier.

The `DEPLOY` command creates the shards. This is done using the `DBMS_SCHEDULER` package (executed on the shard catalog), which communicates with the Scheduler agents on the remote shard hosts.

Agents then invoke DBCA and NETCA to create the shards and the local listeners. After the primary shards are created the corresponding standby shards are built using the RMAN `DUPLICATE` command. Once the primary and standby shards are built, the `DEPLOY` command configures the Data Guard Broker with Fast-Start Failover (FSFO) enabled. The FSFO observers are automatically started on the regional shard director.

Note:

Archivelog and flashback are enabled for all of the shards. This is required for the FSFO observer to perform standby auto-reinstantiation upon failover.

Deployment Methods: ADD SHARD

The second deployment method is with the `ADD SHARD` command. If your database creation standards require that you deploy the SDB using your own pre-created databases, the `ADD SHARD` deployment method supports this requirement by simply adding your prebuilt database shards.

When the `ADD SHARD` command is used for deployment, the `DEPLOY` command handles the configuration of the Data Guard, Broker, and Fast-start Failover. It also handles the scenario where you have pre-configured Data Guard for the shard that is being added.

**Parent topic:** Sharded Database Deployment

### 56.2 Oracle Sharding Prerequisites

Before you install any software, review these hardware, network, and operating system requirements for Oracle Sharding.

- Hardware and operating system requirements for the shards are the same as that on which Oracle Database 12c Release 2 is supported. See your Oracle Database installation documentation for these requirements.
- Hardware, software, and operating system requirements for the shard catalog and shard directors are the same as for the Global Data Services catalog and global service manager. See [Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GSMUG-GUID-B7010949-4EAE-4AB1-A136-D5A4CD2AE688) for these requirements.
- Network requirements are Low Latency GigE

**Parent topic:** Sharded Database Deployment

### 56.3 Installing Oracle Database Software

Install Oracle Database on each system that will host the shard catalog or database shards.

Before installing Oracle Database, create an operating system user on all of the systems where you will be hosting the sharded database, shard catalog, and shard directors, and assign them to the DBA group. Allow the user to run `su`, and make note of the credentials so that you can use them in later procedures.

See [Oracle Database Installation Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=LADBI-GUID-B65E6113-D056-4DD9-940F-DFF493E413D5), or your platform’s installation guide, for information about configuring operating system users.

1. Download the Oracle Database installer on all of the systems that will host the shard catalog or the database shards.
2. Install Oracle Database on all of the systems where you intend to host the shard catalog and sharded database.
	1. Run the installer on the first system.
		```
		$ cd /u01/stage/database
		$ ./runInstaller
		```
		As you step through the Oracle Database installation, be sure to select the following options on the noted screens:
		- On the Installation Option page, select Install database software only.
		- On the Grid Installation Options page, select Single instance database installation. Oracle RAC and Oracle RAC One Node are not supported in this release.
		- On the Database Edition page, select Enterprise Edition.
		- On the Installation Location page, use the same Oracle base and Software location values that you used when creating the environment scripts in the steps above.
		- On the Create Inventory page, accept the defaults.
		- On the Operating System Groups page, accept the defaults or make changes as appropriate for your environment.
		- On the Summary page, you can click Save Response File to create a file for silent installation of the Oracle Database software on the remaining hosts.
		- During installation, execute the `orainstRoot.sh` and `root.sh` scripts as `root` in a separate terminal when prompted.
		2. Optionally, using the response file you created in the first installation, run a silent install on each of the remaining hosts.
		Note that, after performing a silent install using a response file, when you run the database `root.sh` script its execution might not prompt you interactively for any values and uses only default values (for example, for the local user `bin` directory). If any non-default values are desired, specify just the `-responseFile` location when invoking the Installer and omit the `-silent` option. Click through the Installer screens, accepting the response file values, and then run the root script(s) when prompted. During root script execution, any user prompts are presented to you and non-default values can be entered.

See Also:

[Oracle Database Installation Guide for Linux](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=LADBI-GUID-D53355E9-E901-4224-9A2A-B882070EDDF7) for more information about using the response file for silent installation of Oracle Database

**Parent topic:** Sharded Database Deployment

### 56.4 Installing the Shard Director Software

Install the global service manager software on each system that you want to host a shard director.

1. Download the Oracle Global Service Manager installer on all of the systems that will host the shard directors.
2. See [Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GSMUG-GUID-04D33448-2CB4-40C7-9DA0-1CFC6EC5E101) for information about installing a global service manager.
3. Optionally, using the response file you created in the first installation, run a silent install on each of the remaining shard director hosts.
	Note that, after performing a silent install using a response file, when you run the database `root.sh` script its execution might not prompt you interactively for any values and uses only default values (for example, for the local user `bin` directory). If any non-default values are desired, specify just the `-responseFile` location when invoking the Installer and omit the `-silent` option. Click through the Installer screens, accepting the response file values, and then run the root script(s) when prompted. During root script execution, any user prompts are presented to you and non-default values can be entered.

**Parent topic:** Sharded Database Deployment

### 56.5 Creating the Shard Catalog Database

Create a non-CDB Oracle Database using DBCA to host the shard catalog.

1. Connect to the host where you will host the shard catalog, and verify that the expected environment variables are set to the correct values.
	```
	$ env |grep ORA
	ORACLE_BASE=/u01/app/oracle
	ORACLE_HOME=/u01/app/oracle/product/12.2.0/dbhome_1
	```
2. Create the oradata and fast\_recovery\_area directories.
	```
	$ mkdir /u01/app/oracle/oradata
	$ mkdir /u01/app/oracle/fast_recovery_area
	```
3. Run DBCA to create the shard catalog database.
	```
	$ dbca
	```
4. On the Database Operation page, select Create a database, and click Next.
5. On the Creation Mode page, select Advanced configuration, and click Next.
6. On the Deployment Type page, select the Oracle Single Instance database database type, select the General Purpose or Transaction Processing template, and click Next.
7. On the Database Identification page, enter the Global Database name and the shard catalog SID that you configured in the shard catalog host environment script, uncheck the Create as Container Database option, and click Next.
	Important:
	Container databases are not supported in this release of Oracle Sharding. Be sure to uncheck this option before you continue.
8. On the Storage Option page, select the Use following for the database storage attributes option, select File System, select the Use Oracle-Managed Files (OMF) option, and click Next.
9. On the Select Fast Recovery Option page, select Specify Fast Recovery Area, select Enable archiving, and click Next.
10. On the Specify Network Configuration Details page, select Create a new listener, set the listener name and port number, and click Next.
	Make note of the listener name so that you can connect to the database later.
11. Skip the Data Vault Option page.
12. On the Configuration Options page Memory tab, select Use Automatic Shared Memory Management.
13. On the Configuration Options page Character sets tab, select Use Unicode (AL32UTF8), and click Next
14. On the Management Option page, uncheck the Configure Enterprise Manager (EM) database express option, and click Next.
15. On the User Credentials page, select the appropriate option for your business needs, enter the passwords, and click Next.
	Make a note of the passwords you entered because you will need them later.
16. On the Creation Option page, select Create database, and click Next.
17. On the Summary page, click Finish.
18. After the database has been created, make a note of the Global Database Name, SID, and spfile values.
19. If you plan to use Oracle Data Guard to protect the shard catalog database, click Password Management, unlock the SYSDG account, and make a note of the password you enter for this account.
20. Click Close to exit DBCA.

**Parent topic:** Sharded Database Deployment

### 56.6 Setting Up the Oracle Sharding Management and Routing Tier

The shard catalog, shard directors and shards must be configured to communicate with each other.

1. On the shard catalog host, verify that the expected environment values are set to the correct values.
	```
	$ env |grep ORA
	ORACLE_SID=shardcat
	ORACLE_BASE=/u01/app/oracle
	ORACLE_HOME=/u01/app/oracle/product/12.2.0/dbhome_1
	```
2. If the shard catalog listener is not already started, start the shard catalog listener.
	```
	$ lsnrctl start
	```
3. Verify that `DB_CREATE_FILE_DEST` parameter is set on the shard catalog database.
	If the parameter is not set, then set it as shown in the following example. Note that `open_links` and `open_links_per_instance` are set to 16 for the purposes of the Oracle Sharding demo application.
	```
	$ sqlplus / as sysdba
	SQL> alter system set db_create_file_dest='/u01/app/oracle/oradata' scope=both;
	SQL> alter system set open_links=16 scope=spfile;
	SQL> alter system set open_links_per_instance=16 scope=spfile;
	```
4. Shut down and restart the shard catalog database.
	```
	SQL> shutdown immediate
	Datablase closed.
	Database dismounted.
	SQL> startup
	ORACLE instance started.
	Total System Global Area 4798283776 bytes
	Fixed Size                  4430760 bytes
	Variable Size            1006634072 bytes
	Database Buffers         3774873600 bytes
	Redo Buffers               12345344 bytes
	Database mounted.
	Database opened.
	```
5. Grant roles and privileges on the shard catalog database.
	```
	SQL> set echo on
	SQL> set termout on
	SQL> spool setup_grants_privs.lst
	```
	1. Unlock and set the password for the GSMCATUSER schema.
		This schema is used by the shard director when connecting to the shard catalog database.
		```
		SQL> alter user gsmcatuser account unlock;
		SQL> alter user gsmcatuser identified by gsmcatuser_password;
		```
		2. Create the administrator schema and grant privileges to it.
		The mysdbadmin account is an account in the shard catalog database which stores information on the sharding environment. The mysdbadmin account is the database administrator schema for making administrative changes to the sharded database environment. GDSCTL connects through this user to the database when GDSCTL commands are run, and the mysdbadmin user makes the necessary changes in the database.
		```
		SQL> create user mysdbadmin identified by mysdbadmin_password;
		SQL> grant connect, create session, gsmadmin_role to mysdbadmin;
		SQL> grant inherit privileges on user SYS to GSMADMIN_INTERNAL;
		SQL> spool off
		```
6. Connect to a shard director host and start GDSCTL.
	The commands in the following steps are executed from a shard director host because the GDSCTL command line interface is installed there.
	The following example includes a sanity check that environment variables have been set properly.
	```
	$ env |grep ORA
	ORACLE_BASE=/u01/app/oracle
	ORACLE_HOME=/u01/app/oracle/product/12.2.0/gsmhome_1
	$ gdsctl
	```
7. Create the shard catalog and configure the remote scheduler agent on the shard catalog.
	In this example, the sharded database is given the name cust\_sdb, and two regions are created: region1 and region2. The regions are used as local availability domains for failover of the shards from the primary to physical standby. The regions are not meant to represent geographical regions in this example.
	```
	GDSCTL> create shardcatalog -database shard_catalog_host:1521:shard_catalog_name -chunks 12 -user mysdbadmin/mysdbadmin_password
	 -sdb cust_sdb -region region1, region2  -agent_port port_num -agent_password rsa_password
	```
8. While you are connected to the shard director host, create and start the shard director.
	```
	GDSCTL> add gsm -gsm sharddirector1 -listener listener_port -pwd gsmcatuser_password
	 -catalog shard_catalog_host:1521:shardcat -region region1
	GDSCTL> start gsm -gsm sharddirector1
	```
	Repeat steps 6 and 8 on each shard director host. Replace the shard director name and region name with appropriate values for each host.
9. Using GDSCTL, set the operating system credentials.
	```
	GDSCTL> add credential -credential credential_name -osaccount os_account_name -ospassword os_password
	GDSCTL> exit
	```
	These credentials are the operating system user name and password on the shard hosts (not the catalog host), and the credentials are used by the remote scheduler agent to run jobs on the hosts to set up the shards using DBCA, NETCA, and the like.
	Repeat this step if a different operating system credential will be used for each host.
10. Connect to each of the shard hosts, register remote scheduler agents on them, and create directories for oradata and fast\_recovery\_area on them.
	Note:
	This step is only required if you are using the `CREATE SHARD` method described in Introduction to SDB Deployment. If you are using the `ADD SHARD` method you can skip this step.
	Execute the following statements on each of the machines that will host a shard.
	Note that the os\_account\_name is the account used for Oracle software installation, shard\_host is the host name or IP address of the machine hosting the shard, the shard\_catalog\_host is the host name or IP address of the shard catalog host, and port\_num is the remote scheduler agent port number as specified in the `-agent_port` parameter for `create shardcatalog` in step 7 above. The remote scheduler agent prompts you for the agent registration password specified in the `-agent_password` parameter of `create shardcatalog` in step 7 above.
	```
	$ ssh os_account_name@shard_host
	passwd: os_password
	$ schagent -start
	$ schagent -status
	$ schagent -registerdatabase shard_catalog_host port_num
	$ mkdir /u01/app/oracle/oradata
	$ mkdir /u01/app/oracle/fast_recovery_area
	```

**Parent topic:** Sharded Database Deployment

### 56.7 Creating a System-Managed SDB

The following topics describe the tasks for creating a system-managed SDB.

- Deploying a System-Managed SDB  
	To deploy a system-managed SDB you create shardgroups and shards, create and configure the databases to be used as shards, execute the `DEPLOY` command, and create role-based global services.
- Creating a Schema for a System-Managed SDB  
	Create the schema user, tablespace set, sharded tables, and duplicated tables for the SDB. Verify that the DDLs are propagated to all of the shards, and, while connected to the shards, verify the automatic Data Guard Broker configuration with Fast-Start Failover.
- System-Managed SDB Demo Application  
	The system-managed sharded database (SDB) demo application simulates the workload of an online retail store. Use it to validate the setup of any system-managed (automatic sharding) SDB configuration. The demo application also provides a practical example of sharding concepts for administrators and developers new to database sharding.

**Parent topic:** Sharded Database Deployment

#### 56.7.1 Deploying a System-Managed SDB

To deploy a system-managed SDB you create shardgroups and shards, create and configure the databases to be used as shards, execute the `DEPLOY` command, and create role-based global services.

System-managed sharding does not require the user to map data to shards. Data is automatically distributed across shards using partitioning by consistent hash. The partitioning algorithm evenly and randomly distributes data across shards. For more conceptual information about the system-managed SDB, see [System-Managed Sharding](sharding-methods.md).

1. If you are using the `ADD SHARD` method described in Introduction to SDB Deployment you must first create the databases to be used as shards on their respective hosts.
	The shard databases must have the following characteristics:
	- They must not be container databases (CDBs)
	- They must have an associated TNS Listener on port 1521 on each host
	- The `GSMUSER` account must be unlocked with a known password
	- The primary and standby databases must be configured as such
	- Redo apply should be set up between the corresponding primary and standby databases
	- Flashback and force logging should be enabled
	- The `compatible` parameter must be set to at least 12.2.0
	- A server parameter file (SPFILE) must be in use
	- A `DATA_PUMP_DIR` directory object must be created in each database and must point to a valid directory
	You must then validate that a database is correctly set up for sharding. Execute the following against each database before adding it to the configuration.
	```
	SQL> set serveroutput on
	SQL> execute DBMS_GSM_FIX.validateShard
	```
	Screen output will include INFO, WARNING, and ERROR information that needs to be analyzed for any issues. All WARNING and ERROR messages must be resolved. Re-run `validateShard()` after making changes to confirm the configuration.
2. Connect to the shard director host.
	```
	$ ssh os_user@shard_director1_host
	```
3. Set the global service manager for the current session, and specify the credentials to administer it.
	```
	$ gdsctl
	GDSCTL> set gsm -gsm sharddirector1
	GDSCTL> connect mysdbadmin/mysdbadmin_password
	```
4. Add a shardgroup for the primary shards.
	In this example the shardgroup is named primary\_shardgroup. You can choose your own name.
	```
	GDSCTL> add shardgroup -shardgroup primary_shardgroup -deploy_as primary -region region1
	```
5. Add a shardgroup for the Active Data Guard standby shards.
	In this example the shardgroup is named standby\_shardgroup. You can choose your own name.
	```
	GDSCTL> add shardgroup -shardgroup standby_shardgroup -deploy_as active_standby -region region2
	```
6. Add each shard’s host address to the valid node checking for registration (VNCR) list in the catalog, then create the shard in either the primary or standby shardgroup, as shown in the following example.
	Note:
	The valid node checking for registration (VNCR) feature provides the ability to configure and dynamically update a set of IP addresses, host names, or subnets from which registration requests are allowed by the shard directors. Database instance registration with a shard director succeeds only when the request originates from a valid node. By default, the shard management tier (based on Oracle Global Data Services framework) automatically adds a VNCR entry for the host on which a remote database is running each time `create shard` or `add shard` is executed. The automation (called auto-VNCR) finds the public IP address of the target host, and automatically adds a VNCR entry for that IP address. If the host has multiple public IP addresses, then the address on which the database registers may not be the same as the address which was added using auto-VNCR and, as a result, registration many be rejected. If the target database host has multiple public IP addresses, it is advisable that you configure VNCR manually for this host using the `add invitednode` or `add invitedsubnet` commands in GDSCTL.
	If there are multiple net-cards on the target host (`/sbin/ifconfig` returns more than one public interface), use `add invitednode` to be safe (after finding out which interface will be used to route packets).
	If there is any doubt about registration, then use `config vncr` and use `add invitednode` as necessary. There is no harm in doing this, because if the node is added already, auto-VNCR ignores it, and if you try to add it after auto-VNCR already added it, you will get a warning stating that it already exists.
	The following example shows how to create four shards using the `CREATE SHARD` command, two of which are in the primary shardgroup and two in the standby shardgroup. The credential\_name is the operating system credential you created on each host.
	While creating the shards, you can also set the SYS password in the `create shard` using `-sys_password` as shown in the following example. This sets the SYS password after the shards are created when running `DEPLOY`.
	```
	GDSCTL> add invitednode shard_host_1 
	GDSCTL> create shard -shardgroup primary_shardgroup -destination shard_host_1 -credential credential_name -sys_password sys_password
	GDSCTL> add invitednode shard_host_2
	GDSCTL> create shard -shardgroup standby_shardgroup -destination shard_host_2 -credential credential_name -sys_password sys_password
	GDSCTL> add invitednode shard_host_3 
	GDSCTL> create shard -shardgroup primary_shardgroup -destination shard_host_3 -credential credential_name -sys_password sys_password
	GDSCTL> add invitednode shard_host_4
	GDSCTL> create shard -shardgroup standby_shardgroup -destination shard_host_4 -credential credential_name -sys_password sys_password
	```
	If you are using the `ADD SHARD` method described in Introduction to SDB Deployment, use the following command instead of the `CREATE SHARD` commands in the example above.
	```
	GDSCTL> add shard –shardgroup shgrp1 –connect shard_host:1521/shard_database_name –pwd GSMUSER_password
	```
7. Check the configuration from a shard director.
	Note that the shard names, sh1, sh2, sh3, and sh4, are system generated shard names when the `CREATE SHARD` method is used.
	```
	GDSCTL> config
	Regions
	-----------------------
	region1
	region2
	GSMs
	-----------------------
	sharddirector1
	sharddirector2
	Sharded Database
	-----------------------
	cust_sdb
	Databases
	-----------------------
	sh1
	sh2
	sh3
	sh4
	Shard Groups
	-----------------------
	primary_shardgroup
	standby_shardgroup
	Shard spaces
	-----------------------
	shardspaceora
	Services
	-----------------------
	GDSCTL pending requests
	-----------------------
	Command          Object          Status
	-------          ------          ------
	Global properties
	-----------------------
	Name: oradbcloud
	Master GSM: sharddirector1
	DDL sequence #: 0
	GDSCTL> config shardspace
	SHARDSPACE       Chunks
	----------       ------
	shardspaceora    12
	GDSCTL> config shardgroup
	Shard Group               Chunks    Region    SHARDSPACE
	-----------               ------    ------    ----------
	primary_shardgroup        12        region1   shardspaceora
	standby_shardgroup        12        region2   shardspaceora
	GDSCTL> config vncr
	Name    Group ID 
	----    --------
	shard_host_1 
	shard_host_2
	shard_host_3
	shard_host_4
	shard_catalog_host_IP
	GDSCTL> config shard
	Name     Shard Group          Status    State    Region    Availability
	----     -----------          ------    -----    ------    ------------
	sh1      primary_shardgroup   U         none     region1   -
	sh2      standby_shardgroup   U         none     region2   -
	sh3      primary_shardgroup   U         none     region1   -
	sh4      standby_shardgroup   U         none     region2   -
	```
8. Run the `DEPLOY` command to create the shards and the replicas.
	The `DEPLOY` command takes some time to run, approximately 15 to 30 minutes.
	```
	GDSCTL> deploy
	```
	When the `CREATE SHARD` method is used to create the shards, the DEPLOY command creates the primary and standby shards using DBCA. Archivelog and flashback, which is required for the Fast-Start Failover observers to perform standby reinstantiation, are enabled for all of the shards.
	Once the primary and standby shards are built, the `DEPLOY` command configures the Data Guard Broker with Fast-Start Failover enabled. The Fast-Start Failover observers are automatically started on the standby group’s shard director (sharddirector2 in this example).
9. Verify that all of the shards are deployed.
	```
	GDSCTL> config shard
	Name    Shard Group           Status    State        Region    Availability
	----    -----------           ------    -----        ------    ------------
	sh1      primary_shardgroup   Ok        Deployed     region1   ONLINE
	sh2      standby_shardgroup   Ok        Deployed     region2   READ_ONLY
	sh3      primary_shardgroup   Ok        Deployed     region1   ONLINE
	sh4      standby_shardgroup   Ok        Deployed     region2   READ_ONLY
	```
10. Verify that all of the shards are registered.
	```
	GDSCTL> databases
	Database: "sh1" Registered: Y State: Ok ONS: N. Role: PRIMARY
	Instances: 1 Region: region1
	   Registered instances: 
	     cust_sdb%1
	Database: "sh2" Registered: Y State: Ok ONS: N. Role: PH_STNDBY
	Instances: 1 Region: region2
	   Registered instances: 
	     cust_sdb%11
	Database: "sh3" Registered: Y State: Ok ONS: N. Role: PRIMARY
	Instances: 1 Region: region1
	   Registered instances: 
	     cust_sdb%21
	Database: "sh4" Registered: Y State: Ok ONS: N. Role: PH_STNDBY
	Instances: 1 Region: region2
	   Registered instances: 
	     cust_sdb%31
	```
11. Check the configuration of a shard.
	```
	GDSCTL> config shard -shard sh1
	Name: sh1
	Shard Group: primary_shardgroup
	Status: Ok
	State: Deployed
	Region: region1
	Connection string: shard_host_1:1521/sh1:dedicated
	SCAN address:
	ONS remote port: 0
	Disk Threshold, ms: 20
	CPU Threshold, %: 75
	Version: 12.2.0.1
	Last Failed DDL: 
	DDL Error: ---
	Failed DDL id:
	Availability: ONLINE
	Supported services
	-----------------------
	Name                Preferred Status
	----                --------- ------
	```
12. Add a global service that runs on all of the primary shards.
	The oltp\_rw\_srvc global service is a global data service that a client can use to connect to the sharded database. The oltp\_rw\_srvc service runs the OLTP transactions on the primary shards. Likewise, the oltp\_ro\_srvc global service is created to run read-only workload on the standby shards.
	```
	GDSCTL> add service -service oltp_rw_srvc -role primary 
	GDSCTL> config service 
	Name          Network name                      Pool         Started Preferred all
	----          ------------                      ----         ------- -------------
	oltp_rw_srvc  oltp_rw_srvc.cust_sdb.oracdbcloud cust_sdb     No      Yes
	```
13. ```
	GDSCTL> start service -service oltp_rw_srvc
	GDSCTL> status service
	Service "oltp_rw_srvc.cust_sdb.oradbcloud" has 2 instance(s). Affinity: ANYWHERE
	   Instance "cust_sdb%1", name: "sh1", db: "sh1", region: "region1", status: ready.
	   Instance "cust_sdb%21", name: "sh3", db: "sh3", region: "region1", status: ready.
	```
14. Add a global service for the read-only workload to run on the standby shards.
	```
	GDSCTL> add service -service oltp_ro_srvc -role physical_standby
	GDSCTL> config service 
	Name          Network name                      Pool         Started Preferred all
	----          ------------                      ----         ------- -------------
	oltp_rw_srvc  oltp_rw_srvc.cust_sdb.oracdbcloud cust_sdb     Yes     Yes
	oltp_ro_srvc  oltp_ro_srvc.cust_sdb.oracdbcloud cust_sdb     No      Yes
	```
15. Start the read-only service, and verify the status of the global services.
	```
	GDSCTL> start service -service oltp_ro_srvc
	GDSCTL> status service
	Service "oltp_ro_srvc.cust_sdb.oradbcloud" has 2 instance(s). Affinity: ANYWHERE
	   Instance "cust_sdb%11", name: "sh2", db: "sh2", region: "region2", status: ready.
	   Instance "cust_sdb%31", name: "sh4", db: "sh4", region: "region2", status: ready.
	Service "oltp_rw_srvc.cust_sdb.oradbcloud" has 2 instance(s). Affinity: ANYWHERE
	   Instance "cust_sdb%1", name: "sh1", db: "sh1", region: "region1", status: ready.
	   Instance "cust_sdb%21", name: "sh3", db: "sh3", region: "region1", status: ready.
	```

See Also:

Creating a Schema for a System-Managed SDB

[Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GSMUG-GUID-3285C437-78F8-4339-AAAB-33DBB7A9D400) for more information about GDSCTL command usage

**Parent topic:** Creating a System-Managed SDB

#### 56.7.2 Creating a Schema for a System-Managed SDB

Create the schema user, tablespace set, sharded tables, and duplicated tables for the SDB. Verify that the DDLs are propagated to all of the shards, and, while connected to the shards, verify the automatic Data Guard Broker configuration with Fast-Start Failover.

1. Connect to the shard catalog database, create the application schema user, and grant privileges and roles to the user.
	In this example, the application schema user is called app\_schema.
	```
	$ sqlplus / as sysdba
	SQL> alter session enable shard ddl;
	SQL> create user app_schema identified by app_schema_password;
	SQL> grant all privileges to app_schema;
	SQL> grant gsmadmin_role to app_schema;
	SQL> grant select_catalog_role to app_schema;
	SQL> grant connect, resource to app_schema;
	SQL> grant dba to app_schema;
	SQL> grant execute on dbms_crypto to app_schema;
	```
2. Create a tablespace set for the sharded tables.
	```
	SQL> CREATE TABLESPACE SET TSP_SET_1 using template (datafile size 100m autoextend on next 10M
	 maxsize unlimited extent management local segment space management auto);
	```
	Specifying the shardspace is optional when creating the tablespace set. If the shardspace is not specified in the command, the default shardspace is used.
3. Create a tablespace for the duplicated tables.
	In this example the duplicated table is the Products table in the sample Customers-Orders-Products schema.
	```
	SQL> CREATE TABLESPACE products_tsp datafile size 100m autoextend on next 10M maxsize unlimited extent management local uniform size 1m;
	```
4. Create a sharded table for the root table.
	In this example, the root table is the Customers table in the sample Customers-Orders-Products schema.
	```
	SQL> CONNECT app_schema/app_schema_password
	SQL> ALTER SESSION ENABLE SHARD DDL;
	SQL> CREATE SHARDED TABLE Customers
	  (
	    CustId      VARCHAR2(60) NOT NULL,
	    FirstName   VARCHAR2(60),
	    LastName    VARCHAR2(60),
	    Class       VARCHAR2(10),
	    Geo         VARCHAR2(8),
	    CustProfile VARCHAR2(4000),
	    Passwd      RAW(60),
	    CONSTRAINT pk_customers PRIMARY KEY (CustId),
	    CONSTRAINT json_customers CHECK (CustProfile IS JSON)
	  ) TABLESPACE SET TSP_SET_1
	  PARTITION BY CONSISTENT HASH (CustId) PARTITIONS AUTO;
	```
5. Create a sharded table for the other tables in the table family.
	In this example, sharded tables are created for the Orders and LineItems tables in the sample Customers-Orders-Products schema.
	The Orders sharded table is created first:
	```
	SQL> CREATE SHARDED TABLE Orders
	  (
	    OrderId     INTEGER NOT NULL,
	    CustId      VARCHAR2(60) NOT NULL,
	    OrderDate   TIMESTAMP NOT NULL,
	    SumTotal    NUMBER(19,4),
	    Status      CHAR(4),
	    CONSTRAINT  pk_orders PRIMARY KEY (CustId, OrderId),
	    CONSTRAINT  fk_orders_parent FOREIGN KEY (CustId) 
	    REFERENCES Customers ON DELETE CASCADE
	  ) PARTITION BY REFERENCE (fk_orders_parent);
	```
	Create the sequence used for the OrderId column.
	```
	SQL> CREATE SEQUENCE Orders_Seq;
	```
	Create a sharded table for LineItems
	```
	SQL> CREATE SHARDED TABLE LineItems
	  (
	    OrderId     INTEGER NOT NULL,
	    CustId      VARCHAR2(60) NOT NULL,
	    ProductId   INTEGER NOT NULL,
	    Price       NUMBER(19,4),
	    Qty         NUMBER,
	    CONSTRAINT  pk_items PRIMARY KEY (CustId, OrderId, ProductId),
	    CONSTRAINT  fk_items_parent FOREIGN KEY (CustId, OrderId)
	    REFERENCES Orders ON DELETE CASCADE
	  ) PARTITION BY REFERENCE (fk_items_parent);
	```
6. In this example, the Products table is a duplicated object.
	```
	SQL> CREATE DUPLICATED TABLE Products
	  (
	    ProductId  INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	    Name       VARCHAR2(128),
	    DescrUri   VARCHAR2(128),
	    LastPrice  NUMBER(19,4)
	  ) TABLESPACE products_tsp;
	```
7. From the shard director host, verify that there were no failures during the creation of the tablespaces.
	```
	GDSCTL> show ddl
	id    DDL Text                                  Failed shards
	--    --------                                  -------------
	5     grant connect, resource to app_schema
	6     grant dba to app_schema
	7     grant execute on dbms_crypto to app_s... 
	8     CREATE TABLESPACE SET  TSP_SET_1 usin...
	9     CREATE TABLESPACE products_tsp datafi...
	10    CREATE SHARDED TABLE Customers (   Cu...
	11    CREATE SHARDED TABLE Orders (   Order...
	12    CREATE SEQUENCE Orders_Seq;
	13    CREATE SHARDED TABLE LineItems (   Or...
	14    CREATE MATERIALIZED VIEW "APP_SCHEMA"...
	```
	Note:
	The `show ddl` command output might be truncated. You can run `SELECT ddl_text FROM gsmadmin_internal.ddl_requests` on the catalog to see the full text of the statements.
8. Verify that there were no DDL errors on each of the shards.
	Run the `config shard` and ` config chunks` commands on each shard in your configuration.
	```
	GDSCTL> config shard -shard sh1
	Name: sh1
	Shard Group: primary_shardgroup
	Status: Ok
	State: Deployed
	Region: region1
	Connection string: shard_host_1:1521/sh1_host:dedicated
	SCAN address: 
	ONS remote port: 0
	Disk Threshold, ms: 20
	CPU Threshold, %: 75
	Version: 12.2.0.0
	Last Failed DDL: 
	DDL Error: ---
	Failed DDL id: 
	Availability: ONLINE
	Supported services
	------------------------
	Name                                          Preferred Status    
	----                                          --------- ------    
	oltp_ro_srvc                                  Yes       Enabled   
	oltp_rw_srvc                                  Yes       Enabled  
	GDSCTL> config chunks
	Chunks
	------------------------
	Database                      From      To        
	--------                      ----      --        
	sh1                           1         6         
	sh2                           1         6         
	sh3                           7         12        
	sh4                           7         12
	```
9. Verify that the tablespaces of the tablespace set you created for the sharded table family and the tablespaces you created for the duplicated tables are created on all of the shards.
	The number of tablespaces in the tablespace set is based on the number of chunks you specified in the `create shardcatalog` command.
	The tablespace set with the first 6 chunks of the 12 that were specified in the shard catalog creation example, and the duplicated Products tablespace is shown in the following example.
	```
	$ sqlplus / as sysdba
	SQL> select TABLESPACE_NAME, BYTES/1024/1024 MB from sys.dba_data_files order by tablespace_name;
	TABLESPACE_NAME             MB
	----------------------- ----------
	C001TSP_SET_1           100
	C002TSP_SET_1           100
	C003TSP_SET_1                  100
	C004TSP_SET_1                  100
	C005TSP_SET_1                  100
	C006TSP_SET_1                  100
	PRODUCTS_TSP            100
	SYSAUX                  650
	SYSTEM                  890
	SYS_SHARD_TS                  100
	TSP_SET_1                      100
	TABLESPACE_NAME              MB
	------------------------ ----------
	UNDOTBS1                       105
	USERS                                 5
	13 rows selected.
	```
	Repeat this step on all of the shards in your configuration.
10. Verify that the chunks and chunk tablespaces were created on all of the shards.
	```
	SQL> set linesize 140
	SQL> column table_name format a20
	SQL> column tablespace_name format a20
	SQL> column partition_name format a20
	SQL> show parameter db_unique_name
	NAME             TYPE        VALUE
	---------------- ----------- ------------------------------
	db_unique_name   string      sh1
	SQL> select table_name, partition_name, tablespace_name from dba_tab_partitions where tablespace_name like 'C%TSP_SET_1' order by tablespace_name;
	TABLE_NAME       PARTITION_NAME   TABLESPACE_NAME
	---------------- ---------------- --------------------
	ORDERS           CUSTOMERS_P1     C001TSP_SET_1
	CUSTOMERS        CUSTOMERS_P1     C001TSP_SET_1
	LINEITEM         CUSTOMERS_P1     C001TSP_SET_1
	CUSTOMERS        CUSTOMERS_P2     C002TSP_SET_1
	LINEITEMS        CUSTOMERS_P2     C002TSP_SET_1
	ORDERS           CUSTOMERS_P2     C002TSP_SET_1
	CUSTOMERS        CUSTOMERS_P3     C003TSP_SET_1
	ORDERS           CUSTOMERS_P3     C003TSP_SET_1
	LINEITEMS        CUSTOMERS_P3     C003TSP_SET_1
	ORDERS           CUSTOMERS_P4     C004TSP_SET_1
	CUSTOMERS        CUSTOMERS_P4     C004TSP_SET_1
	TABLE_NAME       PARTITION_NAME   TABLESPACE_NAME
	---------------- ---------------- --------------------
	LINEITEMS        CUSTOMERS_P4     C004TSP_SET_1
	CUSTOMERS        CUSTOMERS_P5     C005TSP_SET_1
	LINEITEMS        CUSTOMERS_P5     C005TSP_SET_1
	ORDERS           CUSTOMERS_P5     C005TSP_SET_1
	CUSTOMERS        CUSTOMERS_P6     C006TSP_SET_1
	LINEITEMS        CUSTOMERS_P6     C006TSP_SET_1
	ORDERS           CUSTOMERS_P6     C006TSP_SET_1
	18 rows selected.
	```
	Repeat this step on all of the shards in your configuration.
11. Connect to the shard catalog database and verify that the chunks are uniformly distributed.
	```
	$ sqlplus / as sysdba
	SQL> set echo off
	SQL> SELECT a.name Shard, COUNT(b.chunk_number) Number_of_Chunks
	  FROM gsmadmin_internal.database a, gsmadmin_internal.chunk_loc b
	  WHERE a.database_num=b.database_num
	  GROUP BY a.name
	  ORDER BY a.name;
	SHARD                   NUMBER_OF_CHUNKS
	------------------------------ ----------------
	sh1                          6
	sh2                          6
	sh3                          6
	sh4                          6
	```
12. Verify that the sharded and duplicated tables were created.
	Log in as the application schema user on the shard catalog database and each of the shards.
	The following example shows querying the tables on a database shard as the app\_schema user.
	```
	$ sqlplus app_schema/app_schema_password
	Connected.
	SQL> select table_name from user_tables;
	TABLE_NAME
	-----------------------------------------------------------------------
	CUSTOMERS
	ORDERS
	LINEITEMS
	PRODUCTS
	4 rows selected.
	```
13. Verify that the Data Guard Broker automatic Fast-Start Failover configuration was done.
	```
	$ ssh os_username@shard_host_1
	$ dgmgrl
	DGMGRL for Linux: Release 12.2.0.0.2 - Beta on Wed Jan 20 02:49:58 2016
	Copyright (c) 1982, 2015, Oracle and/or its affiliates.  All rights reserved.
	Welcome to DGMGRL, type "help" for information.
	DGMGRL> connect sys/password
	Connected to "sh1"
	Connected as SYSDG.
	DGMGRL> show configuration
	Configuration - sh1
	  Protection Mode: MaxPerformance
	  Members:
	  sh1 - Primary database
	    sh2 - (*) Physical standby database 
	Fast-Start Failover: ENABLED
	Configuration Status:
	SUCCESS   (status updated 15 seconds ago)
	DGMGRL> show database sh1
	Database - sh1
	  Role:               PRIMARY
	  Intended State:     TRANSPORT-ON
	  Instance(s):
	    sh1
	Database Status:
	SUCCESS
	DGMGRL> show database sh2
	Database - sh2
	  Role:               PHYSICAL STANDBY
	  Intended State:     APPLY-ON
	  Transport Lag:      0 seconds (computed 0 seconds ago)
	  Apply Lag:          0 seconds (computed 0 seconds ago)
	  Average Apply Rate: 2.00 KByte/s
	  Real Time Query:    ON
	  Instance(s):
	    sh2
	Database Status:
	SUCCESS
	DGMGRL> show fast_start failover
	Fast-Start Failover: ENABLED
	  Threshold:          30 seconds
	  Target:             sh2
	  Observer:           shard_director_host
	  Lag Limit:          30 seconds
	  Shutdown Primary:   TRUE
	  Auto-reinstate:     TRUE
	  Observer Reconnect: (none)
	  Observer Override:  FALSE
	Configurable Failover Conditions
	  Health Conditions:
	    Corrupted Controlfile          YES
	    Corrupted Dictionary           YES
	    Inaccessible Logfile            NO
	    Stuck Archiver                  NO
	    Datafile Write Errors          YES
	  Oracle Error Conditions:
	    (none)
	```
14. Connect to the shard catalog database and run the following commands:
	```
	$ sqlplus / as sysdba
	SQL> SELECT observer_state FROM gsmadmin_internal.broker_configs;
	OBSERVER_STATE
	--------------------------------------------------------------------------------
	GSM server SHARDDIRECTOR2. Observer started. 
	Log files at '/u01/app/oracle/product/12.2.0/gsmhome_1/network/admin/gsm_observer_1.log'.
	GSM server SHARDDIRECTOR2. Observer started. 
	Log files at '/u01/app/oracle/product/12.2.0/gsmhome_1/network.admin/gsm_observer_2.log'.
	```

See Also:

[Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GSMUG-GUID-C338515C-C72E-4DD8-8CB8-4737AB04046A) for information about GDSCTL command usage

**Parent topic:** Creating a System-Managed SDB

#### 56.7.3 System-Managed SDB Demo Application

The system-managed sharded database (SDB) demo application simulates the workload of an online retail store. Use it to validate the setup of any system-managed (automatic sharding) SDB configuration. The demo application also provides a practical example of sharding concepts for administrators and developers new to database sharding.

The demo application assumes that a system-managed SDB environment was already created along with the CUSTOMER table-family. The environment may have any number of chunks and shards (database nodes). When run, the application will first populate the Products table and then start a one-hour workload that can be paused at any time by the administrator. The workload includes four types of transactions: create a customer order, lookup the list of orders, create a new product, and multi-shard query with report generation. All aspects of a sharded database configuration are exercised.

You can download the demo application, along with a README file that describes how to run and monitor it, from [My Oracle Support Document 2184500.1](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2184500.1).

**Parent topic:** Creating a System-Managed SDB

### 56.8 Deploying a Composite SDB

To deploy a composite SDB you must install the required Oracle Sharding software components, configure the objects for a composite SDB, and create the schema.

The composite sharding method allows you to create multiple shardspaces for different subsets of data in a table partitioned by consistent hash. A shardspace is set of shards that store data that corresponds to a range or list of key values.

The following topics describe the tasks for deploying a composite SDB.

- Deploying a Composite SDB  
	To deploy a composite SDB you create shardgroups and shards, execute the `DEPLOY` command, and create role-based global services.
- Creating a Schema for a Composite SDB  
	Create the schema user, tablespace set, sharded tables, and duplicated tables for the SDB. Verify that the DDLs are propagated to all of the shards, and, while connected to the shards, verify the automatic Data Guard Broker configuration with Fast-Start Failover.

**Parent topic:** Sharded Database Deployment

#### 56.8.1 Deploying a Composite SDB

To deploy a composite SDB you create shardgroups and shards, execute the `DEPLOY` command, and create role-based global services.

The examples used in this deployment procedure are based on a global distribution scenario where separate shardspaces and shardgroups are created for America and Europe.

1. Connect to a shard director host, and verify the environment variables.
	```
	$ ssh os_user@shard_director_home
	$ env |grep ORA
	ORACLE_BASE=/u01/app/oracle
	ORACLE_HOME=/u01/app/oracle/product/12.2.0/gsmhome_1
	```
2. Set the global service manager for the current session, and specify the credentials to administer it.
	```
	$ gdsctl
	GDSCTL> set gsm -gsm sharddirector1
	GDSCTL> connect mysdbadmin/mysdbadmin_password
	```
3. Add shardspaces and shardgroups for each customized grouping of shards your business case requires.
	In this example the shardspaces and shardgroups are created for the America and Europe customers. You can choose your own names.
	```
	GDSCTL> add shardspace -shardspace cust_america
	GDSCTL> add shardgroup -shardspace cust_america -shardgroup america_shgrp1 -deploy_as primary -region region1
	GDSCTL> add shardspace -shardspace cust_europe
	GDSCTL> add shardgroup -shardspace cust_europe -shardgroup europe_shgrp1 -deploy_as primary -region region2
	```
	Note:
	For production deployments, additional shardgroups must be created for high availability using the `add shardgroup` command
4. Verify the shardspace and shardgroup configurations.
	```
	GDSCTL> config shardspace
	SHARDSPACE                    Chunks                        
	----------                    ------                        
	cust_america                  12                            
	cust_europe                   12                            
	shardspaceora                 12   
	 
	GDSCTL>config shardgroup
	Shard Group         Chunks Region              SHARDSPACE          
	-----------         ------ ------              ----------          
	america_shgrp1      12     region1             cust_america        
	europe_shgrp1       12     region2             cust_europe
	```
5. ```
	GDSCTL> config
	Regions
	------------------------
	region1                       
	region2                       
	GSMs
	------------------------
	sharddirector1                
	sharddirector2                
	Sharded Database
	------------------------
	cust_sdb_comp                 
	Databases
	------------------------
	Shard Groups
	------------------------
	america_shgrp1                
	europe_shgrp1                 
	Shard spaces
	------------------------
	cust_america                  
	cust_europe                   
	shardspaceora                 
	Services
	------------------------
	GDSCTL pending requests
	------------------------
	Command                       Object                        Status                        
	-------                       ------                        ------                        
	Global properties
	------------------------
	Name: oradbcloud
	Master GSM: sharddirector1
	DDL sequence #: 0
	```
6. Add each shard’s host address to the valid node checking for registration (VNCR) list in the catalog, then create the shard in either the primary or standby shardgroup, as shown in the following example.
	Note:
	The valid node checking for registration (VNCR) feature provides the ability to configure and dynamically update a set of IP addresses, host names, or subnets from which registration requests are allowed by the shard directors. Database instance registration with a shard director succeeds only when the request originates from a valid node. By default, the shard management tier (based on Oracle Global Data Services framework) automatically adds a VNCR entry for the host on which a remote database is running each time `create shard` or `add shard` is executed. The automation (called auto-VNCR) finds the public IP address of the target host, and automatically adds a VNCR entry for that IP address. If the host has multiple public IP addresses, then the address on which the database registers may not be the same as the address which was added using auto-VNCR and, as a result, registration many be rejected. If the target database host has multiple public IP addresses, it is advisable that you configure VNCR manually for this host using the `add invitednode` or `add invitedsubnet` commands in GDSCTL.
	If there are multiple net-cards on the target host (`/sbin/ifconfig` returns more than one public interface), use `add invitednode` to be safe (after finding out which interface will be used to route packets).
	If there is any doubt about registration, then use `config vncr` and use `add invitednode` as necessary. There is no harm in doing this, because if the node is added already, auto-VNCR ignores it, and if you try to add it after auto-VNCR already added it, you will get a warning stating that it already exists.
	The example shows how to create four shards, two of which are in the America shardgroup and two in the Europe shardgroup. The os\_credential is the operating system credential you created on each host.
	While creating the shards, you can also set the SYS password in the `create shard` using `-sys_password` as shown in the following example. This sets the SYS password after the shards are created when running `DEPLOY`.
	```
	GDSCTL> add invitednode shard_host_1 
	GDSCTL> create shard -shardgroup america_shgrp1 -destination shard_host_1 -credential os_credential-sys_password
	GDSCTL> add invitednode shard_host_2
	GDSCTL> create shard -shardgroup america_shgrp1 -destination shard_host_2 -credential os_credential-sys_password
	GDSCTL> add invitednode shard_host_3 
	GDSCTL> create shard -shardgroup europe_shgrp1 -destination shard_host_3 -credential os_credential-sys_password
	GDSCTL> add invitednode shard_host_4
	GDSCTL> create shard -shardgroup europe_shgrp1 -destination shard_host_4 -credential os_credential-sys_password
	```
7. Check the configuration from a shard director.
	Note that the shard names, sh1, sh2, sh3, and sh4, are system generated shard names.
	```
	GDSCTL> config shard
	Name                Shard Group         Status    State       Region    Availability 
	----                -----------         ------    -----       ------    ------------ 
	sh1                 america_shgrp1      U         none        region1   -            
	sh2                 america_shgrp1      U         none        region1   -            
	sh3                 europe_shgrp1       U         none        region2   -            
	sh4                 europe_shgrp1       U         none        region2   -            
	GDSCTL> config vncr
	Name    Group ID 
	----    --------
	shard_host_1
	shard_host_2
	shard_host_3
	shard_host_4
	shard_catalog_host_IP
	```
8. Run the `DEPLOY` command to create the shards.
	```
	GDSCTL> deploy
	```
	The `DEPLOY` command takes some time to run, approximately 15 to 30 minutes. The `DEPLOY` command creates the shards using DBCA.
9. Verify that all of the shards are deployed.
	```
	GDSCTL> config shard
	Name                Shard Group         Status    State       Region    Availability 
	----                -----------         ------    -----       ------    ------------ 
	sh1                 america_shgrp1      Ok        Deployed    region1   ONLINE       
	sh2                 america_shgrp1      Ok        Deployed    region1   ONLINE       
	sh3                 europe_shgrp1       Ok        Deployed    region2   ONLINE       
	sh4                 europe_shgrp1       Ok        Deployed    region2   ONLINE
	```
10. Verify that all of the shards are registered.
	```
	GDSCTL> databases
	Database: "sh1" Registered: Y State: Ok ONS: N. Role: PRIMARY Instances: 1 Region: region1
	   Registered instances:
	     cust_sdb_comp%1
	Database: "sh2" Registered: Y State: Ok ONS: N. Role: PRIMARY Instances: 1 Region: region1
	   Registered instances:
	     cust_sdb_comp%11
	Database: "sh3" Registered: Y State: Ok ONS: N. Role: PRIMARY Instances: 1 Region: region2
	   Registered instances:
	     cust_sdb_comp%21
	Database: "sh4" Registered: Y State: Ok ONS: N. Role: PRIMARY Instances: 1 Region: region2
	   Registered instances:
	     cust_sdb_comp%31
	```
11. Check the configuration of a shard.
	```
	GDSCTL> config shard -shard sh1
	Name: sh1
	Shard Group: america_shgrp1
	Status: Ok
	State: Deployed
	Region: region1
	Connection string: shard1:1521/sh1:dedicated
	SCAN address: 
	ONS remote port: 0
	Disk Threshold, ms: 20
	CPU Threshold, %: 75
	Version: 12.2.0.0
	Last Failed DDL: 
	DDL Error: ---
	Failed DDL id: 
	Availability: ONLINE
	Supported services
	------------------------
	Name                                                            Preferred Status    
	----                                                            --------- ------
	```
12. Add a global service that runs on all of the primary shards.
	The oltp\_rw\_srvc global service is the global data services listener that helps route a connection from the client to the actual database. The oltp\_rw\_srvc service runs the OLTP transactions on the primary shards.
	```
	GDSCTL> add service -service oltp_rw_srvc
	GDSCTL> config service 
	Name           Network name                  Pool           Started Preferred all 
	----           ------------                  ----           ------- ------------- 
	oltp_rw_srvc   oltp_rw_srvc.cust_sdb_comp.or cust_sdb_comp  No      Yes           
	               adbcloud
	```
13. ```
	GDSCTL> start service -service oltp_rw_srvc
	GDSCTL> status service
	Service "oltp_rw_srvc.cust_sdb_comp.oradbcloud" has 4 instance(s). Affinity: ANYWHERE
	   Instance "cust_sdb_comp%1", name: "sh1", db: "sh1", region: "region1", status: ready.
	   Instance "cust_sdb_comp%11", name: "sh2", db: "sh2", region: "region1", status: ready.
	   Instance "cust_sdb_comp%21", name: "sh3", db: "sh3", region: "region2", status: ready.
	   Instance "cust_sdb_comp%31", name: "sh4", db: "sh4", region: "region2", status: ready.
	```

See Also:

[Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=GSMUG-GUID-C338515C-C72E-4DD8-8CB8-4737AB04046A)

**Parent topic:** Deploying a Composite SDB

#### 56.8.2 Creating a Schema for a Composite SDB

Create the schema user, tablespace set, sharded tables, and duplicated tables for the SDB. Verify that the DDLs are propagated to all of the shards, and, while connected to the shards, verify the automatic Data Guard Broker configuration with Fast-Start Failover.

1. Connect to the shard catalog host, and set the ORACLE\_SID to the shard catalog name.
2. Connect to the shard catalog database, create the application schema user, and grant privileges and roles to the user.
	In this example, the application schema user is called app\_schema.
	```
	$ sqlplus / as sysdba
	SQL> connect / as sysdba
	SQL> alter session enable shard ddl;
	SQL> create user app_schema identified by app_schema_password;
	SQL> grant connect, resource, alter session to app_schema;
	SQL> grant execute on dbms_crypto to app_schema;
	SQL> grant create table, create procedure, create tablespace, create materialized view to app_schema;
	SQL> grant unlimited tablespace to app_schema;
	SQL> grant select_catalog_role to app_schema;
	SQL> grant all privileges to app_schema;
	SQL> grant gsmadmin_role to app_schema;
	SQL> grant dba to app_schema;
	```
3. Create tablespace sets for the sharded tables.
	```
	SQL> CREATE TABLESPACE SET  
	  TSP_SET_1 in shardspace cust_america using template
	  (datafile size 100m autoextend on next 10M maxsize
	   unlimited extent management
	   local segment space management auto );
	SQL> CREATE TABLESPACE SET
	  TSP_SET_2 in shardspace cust_europe using template
	  (datafile size 100m autoextend on next 10M maxsize
	   unlimited extent management
	   local segment space management auto );
	```
	Specifying the shardspace is optional when creating the tablespace set. If the shardspace is not specified in the command, the default shardspace is used.
4. Create a tablespace for the duplicated tables.
	In this example the duplicated table is the Products table in the sample Customers-Orders-Products schema.
	```
	CREATE TABLESPACE products_tsp datafile size 100m autoextend on next 10M maxsize unlimited extent management local uniform size 1m;
	```
5. Create a sharded table for the root table.
	In this example, the root table is the Customers table in the sample Customers-Orders-Products schema.
	```
	connect app_schema/app_schema_password
	alter session enable shard ddl;
	CREATE SHARDED TABLE Customers
	(
	  CustId      VARCHAR2(60) NOT NULL,
	  FirstName   VARCHAR2(60),
	  LastName    VARCHAR2(60),
	  Class       VARCHAR2(10),
	  Geo         VARCHAR2(8),
	  CustProfile VARCHAR2(4000),
	  Passwd      RAW(60),
	  CONSTRAINT pk_customers PRIMARY KEY (CustId),
	  CONSTRAINT json_customers CHECK (CustProfile IS JSON)
	) partitionset by list(GEO)
	partition by consistent hash(CustId)
	partitions auto
	(partitionset america values ('AMERICA') tablespace set tsp_set_1,
	partitionset europe values ('EUROPE') tablespace set tsp_set_2
	);
	```
6. Create a sharded table for the other tables in the table family.
	In this example, sharded tables are created for the Orders and LineItems tables in the sample Customers-Orders-Products schema.
	Create the sequence used for the OrderId column.
	```
	CREATE SEQUENCE Orders_Seq;
	```
	The Orders sharded table is created first:
	```
	CREATE SHARDED TABLE Orders
	(
	  OrderId     INTEGER NOT NULL,
	  CustId      VARCHAR2(60) NOT NULL,
	  OrderDate   TIMESTAMP NOT NULL,
	  SumTotal    NUMBER(19,4),
	  Status      CHAR(4),
	  constraint  pk_orders primary key (CustId, OrderId),
	  constraint  fk_orders_parent foreign key (CustId) 
	    references Customers on delete cascade
	) partition by reference (fk_orders_parent);
	```
	Create a sharded table for LineItems
	```
	CREATE SHARDED TABLE LineItems
	(
	  OrderId     INTEGER NOT NULL,
	  CustId      VARCHAR2(60) NOT NULL,
	  ProductId   INTEGER NOT NULL,
	  Price       NUMBER(19,4),
	  Qty         NUMBER,
	  constraint  pk_items primary key (CustId, OrderId, ProductId),
	  constraint  fk_items_parent foreign key (CustId, OrderId)
	    references Orders on delete cascade
	) partition by reference (fk_items_parent);
	```
7. In this example, the Products table is a duplicated object.
	```
	CREATE DUPLICATED TABLE Products
	(
	  ProductId  INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	  Name       VARCHAR2(128),
	  DescrUri   VARCHAR2(128),
	  LastPrice  NUMBER(19,4)
	) tablespace products_tsp;
	```
8. From the shard director host, verify that there were no failures during the creation of the tablespaces.
	```
	GDSCTL> show ddl
	id      DDL Text                                 Failed shards 
	--      --------                                 ------------- 
	11      CREATE TABLESPACE SET  TSP_SET_2 in s...               
	12      CREATE TABLESPACE products_tsp datafi...               
	13      CREATE SHARDED TABLE Customers (   Cu...               
	14      CREATE SEQUENCE Orders_Seq;                            
	15      CREATE SHARDED TABLE Orders (   Order...               
	16      CREATE SHARDED TABLE LineItems (   Or...               
	17      create database link "PRODUCTSDBLINK@...               
	18      CREATE MATERIALIZED VIEW "PRODUCTS"  ...               
	19      CREATE OR REPLACE FUNCTION PasswCreat...               
	20      CREATE OR REPLACE FUNCTION PasswCheck...
	```
9. Verify that there were no DDL errors on each of the shards.
	Run the `config shard` and ` config chunks` commands on each shard in your configuration.
	```
	GDSCTL> config shard -shard sh1
	Name: sh1
	Shard Group: america_shgrp1
	Status: Ok
	State: Deployed
	Region: region1
	Connection string: shard1:1521/sh1:dedicated
	SCAN address: 
	ONS remote port: 0
	Disk Threshold, ms: 20
	CPU Threshold, %: 75
	Version: 12.2.0.0
	Last Failed DDL: 
	DDL Error: ---
	Failed DDL id: 
	Availability: ONLINE
	Supported services
	------------------------
	Name                                                            Preferred Status    
	----                                                            --------- ------    
	oltp_rw_srvc                                                    Yes       Enabled  
	GDSCTL> config chunks
	Chunks
	------------------------
	Database                      From      To        
	--------                      ----      --        
	sh1                           1         6         
	sh2                           7         12        
	sh3                           1         6         
	sh4                           7         12
	```
10. Verify that the tablespaces of the tablespace set you created for the sharded table family and the tablespaces you created for the duplicated tables are created on all of the shards.
	The number of tablespaces in the tablespace set is based on the number of chunks you specified in the `create shardcatalog` command.
	The tablespace set with the first 6 chunks of the 12 that were specified in the shard catalog creation example, and the duplicated Products tablespace is shown in the following example on the shard\_host\_1.
	```
	$ sqlplus / as sysdba
	SQL> select TABLESPACE_NAME, BYTES/1024/1024 MB from sys.dba_data_files order by tablespace_name;
	TABLESPACE_NAME                MB
	------------------------------ ----------
	C001TSP_SET_1                  100
	C002TSP_SET_1                  100
	C003TSP_SET_1                  100
	C004TSP_SET_1                  100
	C005TSP_SET_1                  100
	C006TSP_SET_1                  100
	PRODUCTS_TSP                  100
	SYSAUX                      650
	SYSTEM                      890
	SYS_SHARD_TS                  100
	TSP_SET_1                  100
	TABLESPACE_NAME                MB
	------------------------------ ----------
	TSP_SET_2                  100
	UNDOTBS1                  110
	USERS                    5
	14 rows selected.
	```
	Repeat this step on all of the shards in your configuration.
11. Verify that the chunks and chunk tablespaces were created on all of the shards.
	```
	SQL> set linesize 140
	SQL> column table_name format a20
	SQL> column tablespace_name format a20
	SQL> column partition_name format a20
	SQL> show parameter db_unique_name
	NAME                     TYPE     VALUE
	------------------------------------ ----------- ------------------------------
	db_unique_name                 string     sh2
	SQL> select table_name, partition_name, tablespace_name from dba_tab_partitions where tablespace_name like 'C%TSP_SET_1' order by tablespace_name;
	TABLE_NAME         PARTITION_NAME      TABLESPACE_NAME
	-------------------- -------------------- --------------------
	LINEITEMS         CUSTOMERS_P7      C007TSP_SET_1
	CUSTOMERS         CUSTOMERS_P7      C007TSP_SET_1
	ORDERS             CUSTOMERS_P7      C007TSP_SET_1
	CUSTOMERS         CUSTOMERS_P8      C008TSP_SET_1
	LINEITEMS         CUSTOMERS_P8      C008TSP_SET_1
	ORDERS             CUSTOMERS_P8      C008TSP_SET_1
	LINEITEMS         CUSTOMERS_P9      C009TSP_SET_1
	CUSTOMERS         CUSTOMERS_P9      C009TSP_SET_1
	ORDERS             CUSTOMERS_P9      C009TSP_SET_1
	CUSTOMERS         CUSTOMERS_P10      C00ATSP_SET_1
	LINEITEMS         CUSTOMERS_P10      C00ATSP_SET_1
	TABLE_NAME         PARTITION_NAME      TABLESPACE_NAME
	-------------------- -------------------- --------------------
	ORDERS             CUSTOMERS_P10      C00ATSP_SET_1
	CUSTOMERS         CUSTOMERS_P11      C00BTSP_SET_1
	LINEITEMS         CUSTOMERS_P11      C00BTSP_SET_1
	ORDERS             CUSTOMERS_P11      C00BTSP_SET_1
	CUSTOMERS         CUSTOMERS_P12      C00CTSP_SET_1
	LINEITEMS         CUSTOMERS_P12      C00CTSP_SET_1
	ORDERS             CUSTOMERS_P12      C00CTSP_SET_1
	18 rows selected.
	```
	Repeat this step on all of the shards in your configuration.
12. Connect to the shard catalog database and verify that the chunks are uniformly distributed.
	```
	$ sqlplus / as sysdba
	SQL> set echo off
	SQL> select a.name Shard,  count( b.chunk_number) Number_of_Chunks from  gsmadmin_internal.database a, gsmadmin_internal.chunk_loc b where
	 a.database_num=b.database_num  group by a.name;
	SHARD                   NUMBER_OF_CHUNKS
	------------------------------ ----------------
	sh1                          6
	sh2                          6
	sh3                          6
	sh4                          6
	```
13. Verify that the sharded and duplicated tables were created.
	Log in as the application schema user on the shard catalog database and each of the shards.
	The following example shows querying the tables on a database shard as the app\_schema user.
	```
	$ sqlplus app_schema/app_schema_password
	Connected.
	SQL> select table_name from user_tables;
	TABLE_NAME
	-----------------------------------------------------------------------
	CUSTOMERS
	ORDERS
	LINEITEMS
	PRODUCTS
	4 rows selected.
	```

**Parent topic:** Deploying a Composite SDB
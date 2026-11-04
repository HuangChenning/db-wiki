---
title: Configuring Server Pools and Oracle Enterprise Manager Database Control
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/srvpool.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 6 Configuring Server Pools and Oracle Enterprise Manager Database Control

This chapter describes server pool and Oracle Enterprise Manager Database Control configuration in Oracle Real Application Clusters (Oracle RAC) environments. This chapter contains the following topics:

- Understanding Server Pools
- Configuring Database Control During and After Installation

## 6.1 Understanding Server Pools

Server pools are logical divisions of a cluster into pools of servers, which are allocated to host databases or other applications. Server pools are managed using `crsctl` and `srvctl` commands.

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrator's list.

Each server pool name must be unique within the cluster. Two server pools cannot use the same name.

There are two types of server pool management:

- Administrator-managed: Database administrators define the servers on which databases resource run, and place resources manually as needed. This is the management strategy used in previous releases.
- Policy managed: Database administrators specify in which server pool (excluding generic or free) the database resource will run. Oracle Clusterware is responsible for placing the database resource on a server.
	The server pool name is a required attribute. You can also provide values for the following attributes; if you do not specify them, then they are set to the default value:
	- MIN\_SIZE: Minimum number of servers on which you want a resource to run. The default is `0`.
		- MAX\_SIZE: Maximum number of servers on which you want a resource to run. The default is `-1`, which indicates that resources can run on all available nodes in the cluster.
		- IMPORTANCE: The relative importance of the resource pool, used to determine how to reconfigure servers when a node joins or leaves the cluster. The default is `0`.
	Note:
	It is recommended that clients using Oracle Database 11g release 2 and later databases using policy-managed server pools access the database using the Single Client Access Name (SCAN). Using SCAN is highly recommended because the instances of the policy-managed database can run on different servers at different times; using a virtual IP (VIP) address to connect to a particular node or instances for a policy-managed database is not possible.

### 6.1.1 Oracle RAC One Node and Server Pools

Note the following about Oracle RAC One Node and server pools:

- Oracle RAC One Node runs only in one server pool. This server pool is treated the same as any other server pool.
- Online relocation of an Oracle RAC One Node database instances permits planned migrations of an Oracle RAC One Node database from one node to another node. Relocations must always be within a server pool.
- With WLM integration, online relocation of Oracle RAC One Node database instance operations do not take a server away from a server pool with its importance set to a lower value, because the target server must already be in the server pool, or in Free.
- An Oracle RAC One Node database can be a Data Guard physical standby.

### 6.1.2 Policy-Based Cluster and Capacity Management

Using policy-based server pool management, database administrators define resource requirements for the workload, including the following:

- Defining the number of servers or instances preferred for the application. Oracle Clusterware automatically allocates resources up to the number specified, so long as they are physically available, and relocates a resource to another node as necessary.
- Defining the number of instances required to support the application.

Resources are no longer defined as belonging to a specific instance or node. Instead, the priority of resource requirements is defined.

See Also:

The [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm)

## 6.2 Configuring Database Control During and After Installation

The following sections describe how Oracle Enterprise Manager Database Control is configured during the Oracle RAC installation, and how you can configure Database Control after installation:

### 6.2.1 Understanding Using EMCA with Oracle RAC

Each EMCA command can be used in Oracle RAC environments, and certain commands are only applicable in cluster configurations. To perform EMCA cluster commands, use the `-cluster` flag that is available in almost every EMCA operational mode.

When you use EMCA to configure Database Control for Oracle RAC, you configure the Database Control for each instance in the cluster. However, by default, the Database Control Console will only start on the local node. On every other node of the cluster, only the Enterprise Manager agent will start. This is because the Database Control Console opens a number of connections to the database. If an instance of the console is running on every host in the cluster, then you can easily exceed the maximum number of permitted open connections on a 32-node or 64-node environment.

When Database Control Console is started on the local node, on every other node, the commands `emctl start dbconsole` and `emctl stop dbconsole` only start and stop the agent. Each of the remote agents upload their respective data to the console running on the local node, where you can monitor and manage all the targets in the cluster. On each instance of the Oracle RAC database, the following subdirectories will be created, where `nodename` is the name of a node in the cluster, and `DBUniqueName` is the database unique name.

```
$ORACLE_HOME/nodename_DBUniqueName
$ORACLE_HOME/nodename_DBUniqueName
```

However, note that if you upgrade an existing Oracle RAC 10g release 1 database configured with Database Control to the current release, then the existing Database Control configuration is retained. The existing Database Control has a Database Console running on each cluster node. The console will still be started on each individual node.

If you want to modify the existing configuration, then use the following command:

```
emca -reconfig dbcontrol –cluster –EM_NODE nodename -EM_NODE_LIST NODE_list
```

where `nodename` is the public name of the node, and `NODE_list` is a comma-deliminated list of nodes. This command reconfigures the current Database Control setup, and performs the following actions in sequence:

1. Starts a Database Control Console on `nodename`, if one has not been started yet.
2. Redirects the agents monitoring the database instances in NODE\_list so that they upload their data to the console running on `nodename`. Also, agents monitoring database instances on `nodename` will also upload their data to the local console. Note that if you do not enter the command options -EM\_NODE or -EM\_NODE\_LIST at the command line, you will be prompted for them.

\-EM\_NODE defaults to the local node if not specified when prompted. If not specified, -EM\_NODE\_LIST defaults to all nodes where the database is configured.

Use this command to start the console on more than one node. For instance, on an eight-node cluster with nodes `node1`, `node2`, `node3`, `node4`, `node5`, `node6`, `node7`, and `node8`, you can run the following commands in succession:

```
$ emca -reconfig dbcontrol –cluster –EM_NODE node1 -EM_NODE_LIST node2,node3,node4
$ emca -reconfig dbcontrol –cluster –EM_NODE node5 -EM_NODE_LIST node6,node7,node8
```

In this scenario, there are two Database Control consoles running, one on `node1` and the other on `node5`. From either of these consoles, you can manage and monitor all of the targets in the cluster.

For information about the current cluster configuration, you can run the following command:

```
$ emca -displayConfig dbcontrol –cluster
```

Caution:

If you use the command `emca -cluster` to configure Database Control for Oracle RAC, then check the `TNS_ADMIN` environment variable on all cluster nodes. If you have a different `TNS_ADMIN` set for each node, then the listener for the target cannot be configured correctly. In this case, set the same `TNS_ADMIN` on all cluster nodes before running the `emca -cluster` command.

To configure Enterprise Manager for a newly added node of a cluster, use the following command:

```
$ emca -addNode db
```

On policy managed databases, another common operation is the addition and deletion of cluster nodes. After you add a new node, you can run EMCA to configure Database Control or central agent management for that node using the command `emca -addNode db`. Running EMCA only configures Enterprise Manager so that you can manage the instance in a way that is consistent with the rest of the cluster database instances.

When configuring Enterprise Manager for a new node, run the EMCA command only after you have added the node. Also, run the command from a node in the cluster that already has Enterprise Manager configured for it, because the Enterprise Manager configuration settings on the existing node are propagated to the new node when you run the command. Because the `-addNode` option can be used only in an Oracle RAC environment, you do not need to use the `-cluster` option on the command line.

After running the command `emca -addNode db`, enter the node name and database unique name for the node and database. For example:

```
Node name: node2
Database Unique Name: EM102
```

To deconfigure Enterprise Manager for a specific node you are deleting from the cluster, log into a different node from the node that you plan to delete, and use the command `emca -deleteNode db`. Running this command removes the Enterprise Manager configuration so that you will no longer be able to manage the instance with Enterprise Manager on that node. Ensure that you run the EMCA command before you delete the cluster node. Because this option can be used only in an Oracle RAC environment, you do not need to use the `-cluster` option on the command line.

### 6.2.2 Configuring Database Control During Installation

If you create a database while installing Oracle RAC 11g release 2 (11.2), you have the option of configuring your database so it can be managed by Oracle Enterprise Manager 10g Grid Control Console or by Oracle Enterprise Manager 11g Database Control Console.

To select Grid Control Console as your management option, the Oracle Management Service must be installed on a network host. In addition, the Oracle Management Agent must be installed on the host where you are installing the database. Otherwise, the Grid Control Console option is unavailable and you must instead manage your database with Database Control.

For most of the Oracle RAC 11g release 2 (11.2) installation types, you must choose either Database Control or Grid Control as your management option when you create a database during the installation.

However, if you create a database using one of the following methods, then you can choose not to configure Database Control:

- Choosing the Advanced database configuration option during an Enterprise or Standard Edition installation
- Running Database Configuration Assistant (DBCA) after the installation

If you do not configure Database Control during the Oracle RAC 11g release 2 (11.2) installation, no hostname\_dbuniquename directory is created in the resulting Oracle home directory.

### 6.2.3 Configuring Database Control with DBCA

The primary method for configuring an existing Oracle Database 11g release 2 (11.2) database so it can be managed with Database Control is to use DBCA. You can use DBCA to create a new database or to reconfigure an existing database.

See Also:

"Installing Oracle Software and Building the Database" in [Oracle Database 2 Day DBA Online Help](https://docs.oracle.com/cd/E11882_01/server.112/e10897/install.htm#ADMQS021) for more information about using DBCA to create a new database instance, and [Oracle Enterprise Manager Real Application Clusters Guide Online Help](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for Oracle RAC examples using DBCA

To use DBCA to reconfigure your database so it can be managed with Database Control:

1. Log into the database host as a member of the administrative group that is authorized to install Oracle software and create and run the database.
2. Start DBCA and change directory to the `ORACLE_HOME/bin` directory and enter the following command:
	```
	$ ./dbca
	```
	The DBCA Welcome page appears.
3. Advance to the Operations page and select Configure Database Options.
4. Advance to the Database page and select the database you want to configure.
5. Advance to the Management Options page and select the following options:
	- Configure the Database with Enterprise Manager
		- Use Database Control for Database Management
6. Optionally, select the options for enabling e-mail notifications and enabling daily backups.
	For more information about Enterprise Manager notifications and daily backups, click Help on the Management Options page.
7. Advance until the Finish button is available.
8. Click Finish to reconfigure the database so it uses Database Control.
	After DBCA reconfigures the database, a new subdirectory appears in the Oracle home. This directory is named using the following format and contains Database Control configuration and state files specific to the database you just configured:
	```
	hostname_dbuniquename
	```
	Note that for cluster databases, the directories are named `nodename_dbuniquename`. For example:
	```
	mycluster1.example.com_myNewDB
	```

### 6.2.4 Configuring Database Control After Installation Using EMCA

When you use DBCA to configure Oracle RAC 11g release 2 (11.2), DBCA provides a graphical user interface to help you select Database Control options and to configure other aspects of your database. However, if you want to use the operating system command line to configure Database Control, then you can use the Enterprise Manager Configuration Assistant (EMCA).

Caution:

During the configuration of Database Control using EMCA, the database may become unavailable, and users may not be able to connect to the database or perform operations on the database.

To configure Database Control with EMCA:

1. Set the `ORACLE_HOME` environment variable to identify the Oracle home for the database you want to manage:
2. Change directory to the `ORACLE_HOME/bin` directory.
3. Start EMCA by entering the following command with any of the optional command-line arguments shown in Table 6-1:
	```
	$ ./emca
	```
	Depending upon the arguments you include on the EMCA command line, EMCA prompts you for the information required to configure Database Control.
	For example, enter the following command to configure Database Control so it will perform automatic daily backups of your database:
	```
	$ ./emca -config dbcontrol db -backup
	```

EMCA commands are of the form:

```
emca [operation] [mode] [flags] [parameters]
```

Note:

To configure Database Console for a single-instance database that uses Oracle ASM, you do not need to provide extra parameters with the EMCA command. Run the following command to configure the Database Console which will automatically detect the Oracle ASM instance:
```
emca -config dbcontrol db -repos create
```

Table 6-1 describes the valid execution operations and modes, and lists the optional parameters in brackets. Table 6-2 discusses the flags and their behavior, while Table 6-3 defines the optional parameters in detail. EMCA parameters are of the form \[-parameterName parameterValue\]. Multiple parameters can be used in combination at the command line.

Table 6-1 EMCA Command-Line Operations

| Command | Description |
| --- | --- |
| emca -h \| --h \| -help \| --help | Use this option to display the Help message for the EMCA utility. The options described in Table 6-1, Table 6-2, and Table 6-3, and the valid parameters you may include are listed. |
| emca –version | Prints the version information associated with EMCA. |
| emca -config dbcontrol db \[-repos (create \| recreate)\] \[-cluster\] \[-silent\] \[-backup\] \[parameters\] | Configures Database Control for a database. Options include creating (or recreating) Database Control repository, configuring automatic backups, and performing these operations on a cluster database. |
| emca -config centralAgent (db \| asm) \[-cluster\] \[-silent\] \[parameters\] | Configures central agent management for a database or an Oracle Automatic Storage Management (ASM) instance. Options include performing this operation on a cluster environment.This operation will configure the database so that it can be centrally managed by the Oracle Enterprise Manager 10g Grid Control Console. To use this option, you must have previously installed the Oracle Management Service component of Enterprise Manager on a network host. In addition, the Oracle Management Agent must be installed on the host where you are running the database. |
| emca -config all db \[-repos (create \| recreate)\] \[-cluster\] \[-silent\] \[-backup\] \[parameters\] | Configures both Database Control and central agent management for a database. The possible configuration options are similar to those described above. |
| emca -deconfig dbcontrol db \[-repos drop\] \[-cluster\] \[-silent\] \[parameters\] | Deconfigures Database Control for a database. Options include dropping the Database Control repository and performing these operations on a cluster database. For example, you might use this command to remove the Database Control configuration from a database you are planning to delete. In such a scenario, remove the Database Control configuration before physically deleting the database. This operation does not remove the actual database or its data files. |
| emca -deconfig centralAgent (db \| asm) \[-cluster\] \[-silent\] \[parameters\] | Deconfigures central agent management for a database or an Oracle ASM instance. Options include performing this operation on a cluster environment. For example, you might use this command to remove the central agent management configuration from a database you are planning to delete. In such a scenario, remove the central agent management configuration before physically deleting the database. This operation does not remove the actual database or its data files. |
| emca -deconfig all db \[-repos drop\] \[-cluster\] \[-silent\] \[parameters\] | Deconfigures both Database Control and central agent management for a database. The possible deconfiguration options are similar to those described above. |
| emca -addNode (db \| asm) \[-silent\] \[parameters\] | Configures Enterprise Manager for a new cluster instance of a database or ASM storage.  For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| emca -deleteNode (db \| asm) \[-silent\] \[parameters\] | Deconfigures Enterprise Manager for a node getting deleted. This is discussed further below, in "Understanding Using EMCA with Oracle RAC". For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| emca -addInst (db \| asm) \[-silent\] \[parameters\] | Configures Enterprise Manager for a new cluster instance of a database or Oracle ASM storage. For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| emca -deleteInst (db \| asm) \[-silent\] \[parameters\] | Deconfigures Enterprise Manager for a specific instance of a cluster database or Oracle ASM storage. This is discussed further below, in "Understanding Using EMCA with Oracle RAC". |
| emca -reconfig ports \[-cluster\] \[parameters\] | Explicitly reassigns Database Control ports. Options include performing this operation on a cluster environment. For more information, refer to "Specifying the Ports Used by Database Control". |
| emca -reconfig dbcontrol -cluster \[-silent\] \[parameters\] | Reconfigures Database Control deployment for a cluster database. Note that this command must be used with the "-cluster" option. For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| emca -displayConfig dbcontrol -cluster \[-silent\] \[parameters\] | Displays information about the current deployment configuration of Database Control in a cluster environment. Note that this command must be used with the "-cluster" option. For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| emca -upgrade (db \| asm \| db\_asm) \[-cluster\] \[-silent\] \[parameters\] | Upgrades the configuration of an earlier version of Enterprise Manager to the current version. This operation can be performed for database, Oracle ASM, or database and Oracle ASM instances together simultaneously. This does not upgrade the actual database or Oracle ASM instances, nor does it upgrade the Enterprise Manager software. Instead, it upgrades the configuration files for the specified instance so that they are compatible with the current version of the Enterprise Manager software. EMCA will attempt to upgrade all instances of the specified database and/or Oracle ASM target on the host, across all Oracle Homes (since it is likely that certain target properties, such as listener port or Oracle Home, have changed). |
| emca -restore (db \| asm \| db\_asm) \[-cluster\] \[-silent\] \[parameters\] | Restores the current version of Enterprise Manager configuration to an earlier version. This is the inverse of the "-upgrade" option (and will reverse any changes that result from an "-upgrade" operation), and as such, the options are similar. |

Table 6-2 EMCA Command-Line Flags

| Flag | Description |
| --- | --- |
| db | Performs the operation for a database (including cluster databases). Use this option for databases that use Oracle Automatic Storage Management (ASM) to store the data files. If a database is using Oracle ASM, then all of the configuration operations and modes described here (except for `-upgrade` and " `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instance(s). |
| asm | Performs the operation only for Oracle ASM instances (including cluster Oracle ASM instances). |
| db\_asm | This flag can only be used in `-upgrade` and `-restore` mode. Performs the upgrade/restore operation for a database and an Oracle ASM instance together. Database and Oracle ASM instances may be upgraded or restored separately (that is, upgrading an Oracle ASM instance does not require upgrading the database instances it services). Therefore, the Enterprise Manager configuration can be upgraded or restored separately for a database and its respective Oracle ASM instance. |
| \-repos create | Creates a new Database Control management repository. |
| \-repos drop | Drops the current Database Control management repository. |
| \-repos recreate | Drops the current Database Control management repository and then recreates a new one. |
| \-cluster | Performs the operation for a cluster database or Oracle ASM instance. |
| \-silent | Performs the operation without prompting for additional information. If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the –respFile argument. You can view a list of the available parameters by entering emca -help at the command line. |
| \-backup | Configures automatic backup for a database. EMCA will prompt for daily automatic backup options. The default Enterprise Manager settings will be used to backup the database files.  Note: If you use this option, EMCA will use the value of the db\_recovery\_file\_dest initialization parameter to identify the recovery area for the automated backups. If that parameter is not set, EMCA will generate an error. You can modify these settings later using the Maintenance page in Database Control. For more information, see the Database Control online Help. |

Table 6-3 EMCA Command-Line Parameters

| Parameter | Description |
| --- | --- |
| \-respFile | Specifies the path of an input file listing parameters for EMCA to use while performing its configuration operation. |
| \-SID | Database system identifier |
| \-PORT | Port number for the listener servicing the database |
| \-ORACLE\_HOME | Database Oracle Home, as an absolute path |
| \-LISTENER\_OH | Oracle Home from where the listener is running. If the listener is running from an Oracle Home other than the one on which the database is running, the parameter LISTENER\_OH must be specified. |
| \-HOST\_USER | Host machine user name (for automatic backup) |
| \-HOST\_USER\_PWD | Host machine user password (for automatic backup) |
| \-BACKUP\_SCHEDULE | Schedule in the form of "HH:MM" (for daily automatic backups) |
| \-EMAIL\_ADDRESS | E-mail address for notifications |
| \-MAIL\_SERVER\_NAME | Outgoing Mail (SMTP) server for notifications |
| \-ASM\_OH | Oracle Automatic Storage Management Oracle Home |
| \-ASM\_SID | System identifier for Oracle ASM instance |
| \-ASM\_PORT | Port number for the listener servicing the Oracle ASM instance |
| \-ASM\_USER\_ROLE | User role for connecting to the Oracle ASM instance |
| \-ASM\_USER\_NAME | User name for connecting to the Oracle ASM instance |
| \-ASM\_USER\_PWD | Password for connecting to the Oracle ASM instance |
| \-DBSNMP\_PWD | Password for DBSNMP user |
| \-SYSMAN\_PWD | Password for SYSMAN user |
| \-SYS\_PWD | Password for SYS user |
| \-SRC\_OH | Oracle Home of the database with Enterprise Manager configuration to be upgraded/restored |
| \-DBCONTROL\_HTTP\_PORT | Use this parameter to specify the port you use to display the Database Control Console in your Web browser. For more information, refer to "Specifying the Ports Used by Database Control". |
| \-AGENT\_PORT | Use this parameter to specify the Management Agent port for Database Control. For more information, refer to "Specifying the Ports Used by Database Control". |
| \-RMI\_PORT | Use this parameter to specify the RMI port for Database Control. For more information, refer to "Specifying the Ports Used by Database Control". |
| \-JMS\_PORT | Use this parameter to specify the JMS port for Database Control. For more information, refer to "Specifying the Ports Used by Database Control". |
| \-CLUSTER\_NAME | Cluster name (for cluster databases) |
| \-DB\_UNIQUE\_NAME | Database unique name (for cluster databases) |
| \-SERVICE\_NAME | Database service name (for cluster databases) |
| \-EM\_NODE | Node from which Database Control console is to be run (for cluster databases). For more information, refer to "Understanding Using EMCA with Oracle RAC". |
| \-EM\_NODE\_LIST | Comma-separated list of nodes for agent-only configurations, uploading data to –EM\_NODE. For more information, refer to "Understanding Using EMCA with Oracle RAC". |

### 6.2.5 Using an Input File for EMCA Parameters

Instead of answering a series of prompts when you run EMCA, you can use the `-respFile` argument to specify an input file. The input file that you create must be in a format similar to the following example:

```
PORT=1521
SID=DB
DBSNMP_PWD=xpE234D
SYSMAN_PWD=KDOdk432
```

After you create an EMCA input file, you can use it on the command line as follows:

```
$ ./emca -config dbcontrol db -respFile input_file_path
```

For example, to configure the Database Control to perform daily backups and create the Database Control Management Repository, create an input file similar to the one shown in the following example:

```
PORT=1521
SID=DB
DBSNMP_PWD=dow3l224
SYSMAN_PWD=squN3243
HOST_USER=johnson
HOST_USER_PWD=diTf32of
SYS_PWD=qlKj4352
BACKUP_SCHEDULE=06:30
```

When you have created the input file, then enter the following command at the operating system prompt:

```
$ ./emca -config dbcontrol db -repos create -backup -respFile input_file_path
```

### 6.2.6 Specifying the Ports Used by Database Control

When you initially install Oracle RAC 11g release 2 (11.2) or configure Database Control with EMCA, Database Control uses a set of default system ports. For example, by default, you access Database Control using port 1158 in 11g Release 2, as in:

```
http://host.domain:1158/em
```

This is the default port assigned to Database Control by the Internet Assigned Numbers Authority (IANA). Likewise, the default Database Control Agent port, as assigned by the IANA, is 3938.

To use ports other than the default ports, use the following EMCA command-line arguments when you initially configure the Database Control with EMCA. Alternatively, you can explicitly assign ports after configuring Database Control using the following command:

```
emca -reconfig ports [-cluster]
```

Note:

You can also use the following EMCA command-line arguments to configure Database Control after you have installed and configured Oracle RAC 11g release 2 (11.2).

The following list summarizes the EMCA command-line arguments that control the standard Database Control port assignments:

- \-DBCONTROL\_HTTP\_PORT port\_number
	This port number is used in the Database Control Console URL. For example, if you set this port to 5570, you can then display the Database Control Console using the following URL:
	```
	http://host.domain:5570/em
	```
- \-RMI\_PORT port\_number
	This port number is used by the Remote Method Invocation (RMI) system, which is part of the J2EE software required by Database Control. The default port can be changed if you want to configure a specific port for Database Console. When a port other than the default port (1521) is used, use the -RMI\_PORT or -JMS\_PORT options along with the emca reconfig command.
- \-JMS\_PORT port\_number
	This port is used by the OC4J Java Message Service (JMS), which is part of the J2EE software required by Database Control. The default port can be changed if you want to configure a specific port for Database Console. When a port other than the default port (1521) is used, use the -RMI\_PORT or -JMS\_PORT options along with the emca reconfig command.
- \-AGENT\_PORT port\_number
	This port is used by the Database Control Management Agent, which is monitoring and administering the database for the Database Control.

### 6.2.7 EMCA Troubleshooting Tips

The following section describes some troubleshooting tips to consider when using EMCA to configure the Database Control:

- Using EMCA After Changing the Database Listener Port
- Upgrading 11g Release 2 Grid Control Agents
- Using EMCA When Database Host Name or IP Address Changes
- Using EMCA When the TNS Configuration Is Changed

#### 6.2.7.1 Using EMCA After Changing the Database Listener Port

If you change the listener port of the database after you have configured Database Control, then the database status appears as down. To reconfigure Database Control so it uses the new listener port, run the EMCA command using the -config dbcontrol db \[-cluster\] command-line arguments.

#### 6.2.7.2 Upgrading 11g Release 2 Grid Control Agents

When upgrading an Oracle Database 10g Release 1 database and Oracle ASM instance that was configured for Oracle Enterprise Manager (either Database Control or a Grid Control central agent) to an Oracle Database 11g release 2 (11.2) database, all Enterprise Manager targets on the relevant hosts referring to the upgraded instances are updated automatically. This is because the upgrade involves altering the instance Oracle Home, port, or other target-associated properties. However, some of these targets on the hosts are not updated successfully during the upgrade if they are managed by an Oracle Database 11g release 2 (11.2) Grid Control Agent. To update these targets, in the Home page for the upgraded database (or Oracle ASM) target, click the Monitoring Configuration. On the Monitoring Configuration page, you can update properties such as Oracle Home, listener port and so on to the correct values.

#### 6.2.7.3 Using EMCA When Database Host Name or IP Address Changes

When the database host name (including the domain name) or the IP address changes, deconfigure and then reconfigure the Database Console with the `-repos create` flag for the `emca` command. For example:

```
emca -deconfig dbcontrol db -repos drop
emca -config dbcontrol db -repos create
```

or

```
emca -deconfig dbcontrol db
emca -config dbcontrol db -repos recreate
```

#### 6.2.7.4 Using EMCA When the TNS Configuration Is Changed

When the TNS configuration is changed, set the environment variable and then run the following command:

```
emca -config dbcontrol db
```
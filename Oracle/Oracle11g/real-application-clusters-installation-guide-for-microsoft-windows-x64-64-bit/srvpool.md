---
title: Configuring Server Pools and Oracle Enterprise Manager Database Control
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/srvpool.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 6 Configuring Server Pools and Oracle Enterprise Manager Database Control

This chapter describes server pool and Oracle Enterprise Manager Database Control configuration in Oracle Real Application Clusters (Oracle RAC) environments.

This chapter contains the following topics:

## 6.1 Understanding Server Pools

Server pools are logical divisions of a cluster into groups of servers, which are allocated to host databases or other applications. Server pools are managed using `crsctl` and `srvctl` commands.

Each server pool name must be unique within the cluster. Two server pools cannot use the same name.

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list. See [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list.

There are two types of server pool management:

- Administrator-managed: Database administrators define the servers on which database resources run, and place resources manually as needed. This is the management strategy used in previous releases.
- Policy-managed: Database administrators specify in which server pool (excluding the generic or free server pools) the database resource will run. Oracle Clusterware is responsible for placing the database resource on a server.
	The server pool name is a required attribute. You can also provide values for the following attributes; if you do not specify them, then they are set to the default value:
	- `MIN_SIZE`: Minimum number of servers on which you want a resource to run. The default is `0`.
		- `MAX_SIZE`: Maximum number of servers on which you want a resource to run. The default is `-1`, which indicates that resources can run on all available nodes in the cluster.
		- `IMPORTANCE`: The relative importance of the server pool, used to determine how to reconfigure servers when a node joins or leaves the cluster. The default is `0`.
	Note:
	Policy-managed databases that use Oracle Database 11g release 2 or later and are deployed in on or more server pools should access the database using the Single Client Access Name (SCAN). Using SCAN is highly recommended because the instances of the policy-managed database can run on different servers at different times; using a virtual IP (VIP) address to connect to a particular node or instances for a policy-managed database is not possible.

### 6.1.1 Oracle RAC One Node and Server Pools

Note the following about Oracle RAC One Node and server pools:

- Oracle RAC One Node runs only in one server pool. This server pool is treated the same as any other server pool.
- Online relocation of an Oracle RAC One Node database instances permits planned migrations of an Oracle RAC One Node database from one node to another node. Relocations must always be within a server pool.
- An Oracle RAC One Node database can be a Data Guard physical standby.

### 6.1.2 Policy-Based Cluster and Capacity Management

Using policy-based server pool management, database administrators define resource requirements for the workload, including the following:

- Defining the number of servers or instances preferred for the application. Oracle Clusterware automatically allocates resources up to the number specified as long as they are physically available, and relocates a resource to another node as necessary.
- Defining the number of instances required to support the application.

Resources are no longer defined as belonging to a specific instance or node. Instead, the priority of resource requirements is defined.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information about policy-based management and server pools

## 6.2 Understanding the Database Control Implementation for Oracle RAC

When you configure Database Control for Oracle RAC, you configure the Database Control for each instance in the cluster. However, by default, the Database Control console will only start on the local node, the node on which the Oracle RAC installation was started. On every other node of the cluster, only the Oracle Management Agent starts. This is because the Database Control console opens a number of connections to the database. If an instance of the console is running on every host in the cluster, then you can easily exceed the maximum number of permitted open connections on a 32-node or 64-node environment.

Each of the remote agents upload their respective data to the console running on the local node, where you can monitor and manage all the nodes and instances in the cluster. On each node in the Oracle home of the Oracle RAC database, the following subdirectories are created, where `nodename` is the name of a node in the cluster, and `DBName` is the unique name of the Oracle RAC database.

```
%ORACLE_HOME%\nodename_DBName
%ORACLE_HOME%\nodename_DBName
```

If you upgrade an existing Oracle RAC 10g release 1 database configured with Database Control to the current release, then the existing Database Control configuration is retained. A Database Control console runs on each cluster node associated with the upgraded Oracle RAC database.

See Also:

Section 6.7.1, "Changing the Database Control Implementation for Your Oracle RAC Database"

## 6.3 Understanding EMCA and Enterprise Manager Control with Oracle RAC

When you use Enterprise Manager Configuration Assistant (EMCA) to configure Oracle Enterprise Manager Database Control for Oracle RAC with the `-cluster` option, you configure Database Control for each instance in the cluster. However, by default, the Database Control console starts only on the local node.

If the Database Control console is started on the local node, then you can use the Enterprise Manager Control (EMCTL) commands `start dbconsole` and `stop dbconsole` to start and stop the Database Control console. The commands `emctl start dbconsole` and `emctl stop dbconsole` start and stop only the Management Agent on the other nodes where the Database Control console is not running.

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

## 6.4 Configuring Database Control During Installation

If you create a database while installing Oracle RAC 11g release 2 (11.2), you have the option of configuring your database so it can be managed by Oracle Enterprise Manager Grid Control or by Oracle Enterprise Manager Database Control.

To select Grid Control as your management option, the Oracle Management Service must be installed on a network host. In addition, the Management Agent must be installed on the host where you are installing the database. Otherwise, the Grid Control option is unavailable and you must instead manage your database with Database Control.

For most of the Oracle RAC 11g release 2 (11.2) installation types, you must choose either Database Control or Grid Control as your management option when you create a database during the installation.

If you do not want to configure Enterprise Manager for your Oracle RAC database, then you must use either the Advanced database configuration option during an Enterprise or Standard Edition installation or run Oracle Database Configuration Assistant (DBCA) after the installation to create your Oracle RAC database. If you do not configure Database Control during the Oracle RAC 11g release 2 (11.2) installation, then the `nodename_DBName` directory is not created in the Oracle home for your database.

See Also:

[Section 2.2, "Selecting an Installation Type"](racinstl.md)

## 6.5 Configuring Database Control with DBCA

The primary method for configuring an existing Oracle Database 11g release 2 (11.2) database so it can be managed with Database Control is to use DBCA. You can use DBCA to create a new database or to reconfigure an existing database.

See Also:

- "Installing Oracle Software and Building the Database" in [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm) for more information about using DBCA to create a new database instance
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for Oracle RAC examples using DBCA

To use DBCA to configure your database so it can be managed with Database Control:

1. Log in to the database host as an Administrator user.
2. Click Start, and select Programs, then Oracle - Oracle\_home name. In the Configuration and Migration Tools folder, select Database Configuration Assistant.
	The DBCA Welcome page appears.
3. Click Next until the Operations page is displayed. Select Configure Database Options.
4. Click Next until the Database page is displayed. Select the database you want to configure.
5. Click Next until the Management Options page is displayed. Select the following options:
	- Configure the Database with Enterprise Manager
		- Use Database Control for Database Management
6. Optionally, select the options for enabling daily backups.
	For more information about Oracle Enterprise Manager daily backups, click Help on the Management Options page.
7. Click Next until the Finish button is available, then click Finish to configure the database to use Database Control.

After DBCA configures the database, a new subdirectory appears in the Oracle home. This directory contains Database Control configuration and state files specific to the database you just configured. For cluster databases, the directories are named `nodename_DBName`. For example, if the name of the local node is `node1.example.com` and the database unique name is `myNewDB`, then the directory name is:

```
node1.example.com_myNewDB
```

## 6.6 Configuring Database Control After Installation Using EMCA

EMCA provides a command-line interface for configuring Database Control. EMCA is available in the `bin` directory of the Oracle home of your database.

Caution:

During configuration of Database Control using EMCA, the database may become unavailable and users may not be able to connect to the database or perform operations on the database.

### 6.6.1 Using EMCA in Interactive Mode

To use EMCA to configure your database for management using Database Control:

1. Set the default Oracle home to the location of the home directory for the database you are modifying. See [Section 7.3, "Working with Multiple Oracle Home Directories on Windows"](undrstnd.md) for details.
2. Change the directory to `%ORACLE_HOME%` `\bin`.
3. Start EMCA by entering the following command with any of the optional command-line parameters shown in [Table G-1, "EMCA Optional Command-Line Parameters"](emca_ref_new.md):
	```
	%ORACLE_HOME%\bin> emca.bat
	```
	Depending upon the parameters you include on the EMCA command line, you might be prompted for additional information required to configure Database Control.
	Note:
	To configure Database Control for a single-instance database using Oracle Automatic Storage Management (Oracle ASM), you do not have to include extra parameters in the EMCA command. Run the following command to configure Database Control for a new installation. EMCA automatically detects the Oracle ASM instance:
	```
	emca -config dbcontrol db -repos create
	```
	Example 6-1 Configuring Database Control and Daily Database Backups using EMCA
	Enter the following commands to configure Database Control for your Oracle RAC database and also to enable automatic daily backups of your database:
	```
	X:\> cd %ORACLE_HOME%\bin
	X:\..\bin> emca.bat -config dbcontrol db -backup
	```

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

### 6.6.2 Using EMCA in Silent Mode With an Input File

Instead of answering a series of prompts when you run EMCA, you can use the `-respFile` parameter to specify an input file. The input file you create must be in a format similar to the following example:

```
PORT=1521
SID=DB
DBSNMP_PWD=xpE234D
SYSMAN_PWD=KDOdk432
```

After you create an EMCA input file, you can use it on the command line as follows, where `input_file_path` is the full path name of the input file:

```
emca -config dbcontrol db -respFile input_file_path
```

Example 6-2 Using a Response File with EMCA to Configure Database Control

To configure Database Control to perform daily backups and create the Oracle Management Repository, create an input file similar to the one shown in the following example:

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

After you have created the input file, enter the following command at the operating system prompt from the `bin` directory of the Oracle home, where `input_file_path` is the full path name of the input file:

```
X:\..\bin> emca -config dbcontrol db -repos create -backup -respFile
input_file_path
```

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

## 6.7 Managing Database Control Using EMCA

You can use DBCA to configure Grid Control or Database Control for your Oracle RAC database. However, if you prefer to use a command-line interface to configure Database Control, then you can use the Oracle Enterprise Manager Configuration Assistant (EMCA) utility.

The following sections describe how Database Control can be configured after installation:

- Changing the Database Control Implementation for Your Oracle RAC Database
- Updating Database Control Configuration When Adding and Removing Nodes
- Using EMCA in Silent Mode With an Input File
- Changing the Ports Used by Database Control
- Enterprise Manager and EMCA Troubleshooting Tips

See Also:

Section 6.5, "Configuring Database Control with DBCA"

### 6.7.1 Changing the Database Control Implementation for Your Oracle RAC Database

By default, when you configure Database Control for an Oracle RAC 11g database, the Database Control console starts only on the local node. If you upgrade an existing Oracle RAC database configured with Database Control to the current release, then the existing Database Control configuration is retained. For example, if you have an Oracle RAC 10g release 1 (10.1) database, then the existing Database Control configuration has a Database Control console running on each cluster node. If you upgrade this database to Oracle Database 11g release 2, then the Database Control console is still started on each individual node.

You can modify the number of Database Control consoles started for your Oracle RAC database. If you have one Database Control console running in the cluster, or more than one, you can still monitor and manage every node in the cluster from a single Database Control console.

To modify the implementation of Database Control for your database, use the following command, where `nodename` is the public name of the node, and `node_list` is a comma-deliminated list of node names:

```
emca -reconfig dbcontrol –cluster –EM_NODE nodename -EM_NODE_LIST node_list
```

Caution:

If you use the command `emca -cluster` to configure Database Control for Oracle RAC, then check the `TNS_ADMIN` environment variable on all cluster nodes. If you have a different `TNS_ADMIN` set for each node, then the listener for the target node cannot be configured correctly. In this case, set the same `TNS_ADMIN` on all cluster nodes before running the `emca -cluster` command.

You can use the `emca -reconfig dbcontrol` command to start a Database Control console on multiple nodes. This command performs the following actions in sequence:

1. Starts a Database Control console on the node specified by `nodename`, if there a Database Control console is not started.
2. Redirects the Management Agents monitoring the database instances in `node_list` so that they upload their data to the Database Control console running on `nodename`. Also, Management Agents monitoring the Oracle Database instances on `nodename` upload their data to the local console. Note that if you do not enter the command options `-EM_NODE` or `-EM_NODE_LIST` at the command line, you will be prompted for them.
	Note:
	`-EM_NODE` defaults to the local node if not specified when prompted. If not specified, `-EM_NODE_LIST` defaults to all nodes where the database is configured.

For information about the current cluster configuration, you can run the following command:

```
emca -displayConfig dbcontrol –cluster
```

This command prompts for the database unique name for the cluster database. It prints the current configuration to the screen, indicating the nodes that have Database Control consoles running on them and the Database Control consoles to which each Management Agent is uploading its data.

Example 6-3 Reconfiguring Database Control for an Oracle RAC Database

This example demonstrates how to start the Database Control console on more than one node in a cluster. If you have an eight-node cluster with nodes `node1`, `node2`, `node3`, `node4`, `node5`, `node6`, `node7`, and `node8`, then you can run the following commands in succession:

```
emca -reconfig dbcontrol –cluster –EM_NODE node1 -EM_NODE_LIST node2,node3,node4
emca -reconfig dbcontrol –cluster –EM_NODE node5 -EM_NODE_LIST node6,node7,node8
```

After you execute these commands, there are two Database Control consoles running, one on `node1` and the other on `node5`. From either of these consoles, you can manage and monitor all of the targets in the cluster. Additionally, the Management Agents on nodes `node1`, `node2`, `node3`, and `node4` upload their information to the Database Control console running on `node1`. Similarly, the Management Agents on nodes `node5`, `node6`, `node7`, and `node8` upload their information to the Database Control console running on `node5`.

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

### 6.7.2 Updating Database Control Configuration When Adding and Removing Nodes

For an administrator-managed database, a common operation is the addition and deletion of cluster nodes.

#### 6.7.2.1 Using EMCA After Adding Nodes to the Cluster

After you add a new node, run EMCA to configure Oracle Enterprise Manager so that you can manage the newly added instance in a way consistent with the rest of the cluster database instances. Use EMCA to configure a Database Control console or Management Agent for that node by executing the following command on a node that currently has Enterprise Manager configured:

```
emca -addNode db
```

Because the `-addNode` option can be used only in an Oracle Real Application Clusters environment, you do not have to use the `-cluster` option on the command line. After running the command `emca -addNode db`, enter the node name and database unique name for the node and Oracle RAC database, for example:

```
Node name: node6
Database Unique Name: myNewDB
```

When configuring Oracle Enterprise Manager for a new node, run the EMCA command only after you have added the node to your cluster and Oracle RAC database. Also, run the command from a node in the cluster that has Oracle Enterprise Manager configured, because the Oracle Enterprise Manager configuration settings on the existing node are propagated to the new node when you run the command.

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

#### 6.7.2.2 Using EMCA After Removing Nodes from the Cluster

To deconfigure Oracle Enterprise Manager for a specific node you are deleting from the cluster, log in to a different node from the one you plan to delete, and use the following command:

```
emca -deleteNode db
```

Ensure that you run the EMCA command before you delete the actual cluster node. Because this option can be used only in an Oracle Real Application Clusters environment, you do not have to use the `-cluster` option on the command line.

Running this command removes the Oracle Enterprise Manager configuration so that you can not use Oracle Enterprise Manager to manage any instances on that node.

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

### 6.7.3 Changing the Ports Used by Database Control

When you initially install Oracle RAC 11g release 2 (11.2) or configure Database Control with EMCA, Database Control uses a set of default system ports. For example, by default, you access Database Control in Oracle Database 11g release 2 (11.2) using a web address that consists of the local host name (`host`.`domain`) and port 1158:

```
https://host.domain:1158/em
```

Port 1158 is the default port assigned to Database Control by the Internet Assigned Numbers Authority (IANA). Similarly, the default Management Agent port, as assigned by the IANA, is 3938.

To use ports other than the default ports, use EMCA command-line arguments when configuring Database Control using EMCA. Table 6-1 summarizes the EMCA command-line parameters that control the standard Database Control port assignments.

Table 6-1 EMCA Command Parameters for Configuring Port Assignments

| Option | Description |
| --- | --- |
| `-DBCONTROL_HTTP_PORT` `port_number` | This port number is used in the Database Control console URL. For example, if you set this port to 5570, then you can then access the Database Control console using the following URL:  ``` http://host.domain:5570/em ``` |
| \- `RMI_PORT` `port_number` | This port number is used by the Remote Method Invocation (RMI) system, which is part of the Java EE software required by Database Control. The default port can be changed if the user wants to configure a specific port for Database Control console.  When a port other than the default port (1521) is used, use the `-RMI_PORT` parameter along with the `emca reconfig` command. |
| `-JMS_PORT` `port_number` | This port is used by the Oracle Containers for Java EE (OC4J) and Java Message Service (JMS), which is part of the Java EE software required by Database Control. The default port can be changed if the user wants to configure a specific port for Database Control console.  When a port other than the default port (1521) is used, use the `-JMS_PORT` parameter along with the `emca reconfig` command. |
| `-AGENT_PORT` `port_number` | This port is used by Oracle Management Agent, which monitors and manages the database for the Database Control console. |

Alternatively, you can explicitly assign ports after configuring Database Control using the following command, where `parameters` refers to the command-line parameters listed in Table 6-1:

```
emca -reconfig ports [-cluster] [parameters]
```

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

## 6.8 Enterprise Manager and EMCA Troubleshooting Tips

The following topics describe some troubleshooting tips to consider when using EMCA and Database Control or Grid Control:

- Updating Database Control After Changing the Database Listener Port
- Upgrading Grid Control Agents for Oracle Database 11g Release 2
- Updating Database Control After Changing the Host Name or IP Address
- Using EMCA After Changing the TNS\_ADMIN Configuration

See Also:

[Appendix G, "Oracle Enterprise Manager Configuration Assistant Reference"](emca_ref_new.md)

### 6.8.1 Updating Database Control After Changing the Database Listener Port

If you change the listener port of the database after you have configured Database Control, then the database status appears as down in the Database Control console. To reconfigure Database Control to use the new listener port, run EMCA using the following command:

```
emca.bat -config dbcontrol db [-cluster]
```

### 6.8.2 Upgrading Grid Control Agents for Oracle Database 11g Release 2

When upgrading an Oracle Database 10g release 1 database instance that was configured for Oracle Enterprise Manager (either Database Control or a Grid Control Management Agent) to an Oracle Database 11g release 2 (11.2) database, all resources monitored by Oracle Enterprise Manager targets associated with the upgraded instances are updated automatically. This is because the upgrade involves altering the Oracle home for the instance, the port numbers, or other instance- and node-associated properties.

If an upgraded instance is managed by a Grid Control Agent, then the associated resource information in Grid Control might not be updated successfully during the upgrade. To update the Grid Control target information, perform the following steps:

1. Use Grid Control to access the home page of the upgraded instance.
2. On the home page for the upgraded instance, select Monitoring Configuration.
3. On the Monitoring Configuration page, update the properties to the correct values as needed, for example, Oracle home, listener port, and so on.

### 6.8.3 Updating Database Control After Changing the Host Name or IP Address

After changing the host name (including the domain name) or the IP address for a node, you must deconfigure Database Control on that node and then reconfigure it using EMCA with the `-repos` flag, as shown in the following examples:

Reconfigure Enterprise Manager, deleting the repository when removing the configuration

```
emca -deconfig dbcontrol db -repos drop
emca -config dbcontrol db -repos create
```

Reconfigure Enterprise Manager, re-creating the repository during reconfiguration

```
emca -deconfig dbcontrol db
emca -config dbcontrol db -repos recreate
```

### 6.8.4 Using EMCA After Changing the TNS\_ADMIN Configuration

After you change the `TNS_ADMIN` environment variable to specify a new configuration, you must update Database Control. Set the `TNS_ADMIN` environment variable to the new value, then run the following command:

```
emca -config dbcontrol db
```
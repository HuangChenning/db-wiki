---
title: Understanding the Oracle Real Application Clusters Installed Configuration
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/undrstnd.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 7 Understanding the Oracle Real Application Clusters Installed Configuration

This chapter describes the Oracle Real Application Clusters (Oracle RAC) installed configuration. This chapter contains the following topics:

## 7.1 Understanding the Configured Environment in Oracle RAC

Oracle Net Configuration Assistant (NETCA) and Database Configuration Assistant (DBCA) configure your environment to meet the requirements for database creation and Oracle Enterprise Manager discovery of Oracle RAC databases.

Note:

Configuration files are created on each node in your cluster database.

Avoid changing host names after you complete your Oracle RAC installation, including adding or deleting domain qualifications. Hostnames are created during an Oracle Clusterware installation and are used extensively with database processes. Nodes with changed host names must be deleted from the cluster and added back with the new name.

## 7.2 Understanding Time Zone Settings on Cluster Nodes

Oracle RAC requires that all cluster nodes have the same time zone setting. During an Oracle Clusterware installation, the installation process determines the time zone setting of the Grid installation owner on the node where Oracle Universal Installer (OUI) runs, and uses that time zone value on all of the nodes as the default time zone setting for all processes that Oracle Clusterware manages. This default setting is used for databases, Oracle ASM, and any other managed processes. However, if you start an instance with SQL\*Plus, you must ensure that the time zone value that Oracle RAC uses is the same as the Oracle Clusterware time zone. You can change the time zone that Oracle Clusterware uses for a database by running the command `srvctl setenv database -T 'TZ=` `time zone`.

## 7.3 Oratab Configuration for Oracle RAC

Oracle creates an entry for each Oracle RAC database in the `oratab` configuration file. The `oratab` file is created by the `root.sh` script during installation, and it is updated by the Database Configuration Assistant when creating or deleting a database. The `oratab` file entry is also created automatically by the Database Agent when a database is first started on a node where it has not run previously. Oracle ASM Agent creates Oracle ASM `oratab` entries.

Oracle Enterprise Manager uses the oratab file during service discovery to determine the name of the Oracle RAC database, and to determine if the database should be started automatically when the system is restarted.

The database entry has the following syntax:

```
$DB_UNIQUE_NAME:$ORACLE_HOME:N
```

A colon (:) is used as the field terminator. A new line terminates the entry. Lines beginning with a pound sign (#) are comments. Because all the instances of an Oracle RAC database have the same `DB_UNIQUE_NAME`, but each instance has its own `ORACLE_SID`, use the `$DB_UNIQUE_NAME` environment variable in the `oratab` file as the database entry.

The `$DB_UNIQUE_NAME` identifier for your Oracle RAC database must be unique across your enterprise. `$ORACLE_HOME` is the directory path to the database, and `N` indicates that the database should not be started at restart time. The following is an example entry for a database named `sales`:

```
sales:/u01/app/oracle/sales:N
```

## 7.4 Database Components Created Using Database Configuration Assistant

This section describes the database components that DBCA creates, which include:

- Tablespaces and Data files
- Control Files
- Redo Log Files

### 7.4.1 Tablespaces and Data files

For both single-instance and cluster database environments, an Oracle Database is divided into smaller logical areas of space known as tablespaces. Each tablespace corresponds to one or more data files on the shared storage. Table 7-1 shows the tablespace names used by an Oracle RAC database and the types of data they contain.

Table 7-1 Tablespace Names Used with Oracle Real Application Clusters Databases

| Tablespace Name | Contents |
| --- | --- |
| `SYSTEM` | Consists of the data dictionary, including definitions of tables, views, and stored procedures needed by the database. Oracle Database automatically maintains information in this tablespace. |
| `SYSAUX` | An auxiliary system tablespace that contains the `DRSYS` (contains data for Oracle Text), `CWMLITE` (contains the OLAP schemas), `XDB` (for XML features), `ODM` (for Oracle Data Mining), `TOOLS` (contains Oracle Enterprise Manager tables), `INDEX`, `EXAMPLE`, and `OEM-REPO` tablespaces. |
| `USERS` | Consists of application data. As you create and enter data into tables, Oracle Database fills this space with your data. |
| `TEMP` | Contains temporary tables and indexes created during SQL statement processing. You may need to expand this tablespace if you are running a SQL statement that involves significant sorting, such as `ANALYZE COMPUTE STATISTICS` on a very large table, or the constructs `GROUP BY,` `ORDER` `BY`, or `DISTINCT`. |
| `UNDOTBS` n | Contains undo tablespaces for each instance that DBCA creates for automatic undo management. |
| `RBS` | If you do not use automatic undo management, then Oracle Database uses the `RBS` tablespace for the rollback segments. |

You cannot alter these tablespace names when using the preconfigured database configuration options from OUI. However, you can change the names of the tablespaces if you use the advanced database creation method.

As mentioned, each tablespace has one or more data files. The data file names created by the preconfigured database configuration options vary by storage type such as Oracle ASM, or a file system.

### 7.4.2 Control Files

The database is configured with two control files that are stored on shared storage.

### 7.4.3 Redo Log Files

Each instance is configured with at least two redo log files that are stored in the shared storage. If you use a file system, then these files are shared file system files. If you use Oracle ASM, then these files are stored on the Oracle ASM disk group.

The file names of the redo log files that are created with the preconfigured database configuration options vary by storage type. Unless you are using a cluster file system, you must enter the block or raw device names.

## 7.5 Managing Undo Tablespaces in Oracle RAC

Oracle Database stores rollback or undo information in undo tablespaces. To manage undo tablespaces, Oracle recommends that you use Automatic Undo Management. Automatic Undo Management is an automated undo tablespace management mode that is easier to administer than manual undo management.

When Oracle ASM and Oracle Managed Files are used along with Automatic Undo Management, an instance that is started for the first time, and thus does not have an undo tablespace, will have its undo tablespace created for it by another instance automatically. The same is also true for redo logs.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information about managing undo tablespaces

## 7.6 Initialization Parameter Files

Oracle recommends using the server parameter file (SPFILE) for storing Oracle Database initialization parameters. Oracle recommends that you store all SPFILEs on Oracle ASM, including the Oracle ASM SPFILE. SPFILEs must be located on shared storage; all instances in a cluster database can access this parameter file.

See Also:

[Chapter 5, " Configuring the Server Parameter File in Oracle Real Application Clusters Environments"](params.md) for more information about the creation and use of parameter files

## 7.7 Oracle Database Default Audit Policy and Initialization Parameters

Oracle Database installs a baseline database auditing policy. This policy covers the access control configuration information stored in Oracle Database database tables, information stored in Oracle Catalog (rollback segments, tablespaces, and so on), the use of system privileges, and Oracle Label Security configuration.

See Also:

[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/toc.htm) for more information about the database audit policy

## 7.8 Understanding Service Registration-Related Parameters

Oracle RAC databases provide the important benefits of connection load balancing and failover. Standalone Oracle Databases perform load balancing by distributing connections among local dispatchers.

Oracle RAC databases increase load balancing by using the Oracle Clusterware SCANs (Single Client Access Name) to balance connections among all instances in a cluster database.

Review the following sections to understand the Oracle RAC load-balancing features:

- Understanding Single Client Access Name (SCAN) and Load-balancing
- Understanding Load-Balancing, Failover, and High Availability

### 7.8.1 Understanding Single Client Access Name (SCAN) and Load-balancing

The Single Client Access Name (SCAN) is a fully qualified name (hostname+domain) that is configured to resolve to all the addresses allocated for the SCAN. The addresses resolve using Round Robin DNS either on the DNS server, or within the cluster in a GNS configuration. SCAN listeners can run on any node in the cluster.

Oracle Database 11g release 2 and later instances only register with SCAN listeners as remote listeners. Upgraded databases register with SCAN listeners as remote listeners, and also continue to register with all node listeners.

SCANs run on the cluster, not on a cluster node. SCANs provide location independence for the databases, so that client configuration does not have to depend on which nodes are running a particular database. For example, if you configure policy managed server pools in a cluster, then the SCAN enables connections to databases in these server pools regardless of which nodes are allocated to the server pool.

SCANs function like a node virtual IP (VIP) address. However, SCANs are resolved to SCAN VIPs that run on any node in the cluster, so unlike a virtual IP address for a node, clients connecting to the SCAN no longer require updated virtual IP addresses as nodes are added to or removed from the cluster. Because the SCAN addresses resolve to the cluster, rather than to a node address in the cluster, nodes can be added to or removed from the cluster without affecting the SCAN address configuration.

During Oracle Grid Infrastructure installation, SCAN listeners are created for as many IP addresses as there are addresses assigned to resolve to the SCAN. Oracle recommends that the SCAN resolves to three addresses, to provide high availability and scalability. If the SCAN resolves to three addresses, then there are three SCAN listeners created.

Oracle RAC provides failover with the node VIP addresses by configuring multiple listeners on multiple nodes to manage client connection requests for the same database service. If a node fails, then the service connecting to the VIP is relocated transparently to a surviving node, enabling fast notification of the failure to the clients connecting through the VIP. If the application and client are configured with transparent application failover options, then the client is reconnected to the surviving node. Oracle Clusterware routes client application requests from the SCAN to the VIP on the least loaded instance providing the service.

Clients configured to use IP addresses for Oracle Database releases prior to Oracle Database 11g release 2 can continue to use their existing connection addresses; using SCANs is not required. When an earlier version of Oracle Database is upgraded, it registers with the SCAN listeners, and clients can start using the SCAN to connect to that database. The database registers with the SCAN listener through the remote listener parameter in the init.ora file. The REMOTE\_LISTENER parameter must be set to SCAN:PORT. Do not set it to a TNSNAMES alias with a single address with the SCAN as HOST=SCAN.

See Also:

The [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for detailed information about SCANs and their configuration

### 7.8.2 Understanding Load-Balancing, Failover, and High Availability

Connection load balancing and failover increase availability by taking advantage of the redundant resources within a cluster database.

The Database Agent (previously known as `racgimon`) configures the `LOCAL_LISTENER` initialization parameters automatically. You do not need to alter this setting. Set the `REMOTE_LISTENER` to the SCAN port and SCAN using the SQL command `ALTER SYSTEM SET REMOTE_LISTENER`. If you change the SCAN port, then you need to change the REMOTE\_LISTENER configuration.

The `LOCAL_LISTENER` parameter identifies the local listener, and the `REMOTE_LISTENER` parameter identifies the global list of listeners. The `REMOTE_LISTENER` parameter is always set to the SCAN address. For example, if the name of the cluster is mycluster, and the domain is example.com, then the SCAN address will be similar to `myscan.mycluster.example.com:1521`.

By default, DBCA configures your environment with dedicated servers. However, if you select the Shared server option when using DBCA, then Oracle configures the shared server. In this case, Oracle Database uses both dedicated and shared server processing. When shared servers are configured, the `DISPATCHERS` parameter is specified as in the following example:

```
DISPATCHERS="(protocol=tcp)"
```

If the `DISPATCHERS` initialization parameter does not specify the `LISTENER` attribute as in the previous example, then the PMON process registers information for all dispatchers with the listeners specified by the `LOCAL_LISTENER` and `REMOTE_LISTENER` parameters.

However, when the `LISTENER` attribute is specified, the PMON process registers dispatcher information with the listeners specified by the `LISTENER` attribute. In this case, setting the `LISTENER` attribute overrides `REMOTE_LISTENER` settings for the specified dispatchers as in the following example:

```
DISPATCHERS="(protocol=tcp)(listener=listeners_db_name)"
```

Note:

Where the notation `db_name` appears in the previous example and throughout this chapter, it refers to the database name (or Oracle SID) that you entered when prompted by DBCA, or it refers to the entry you made for the `DATABASE` keyword of the `CREATE DATABASE` statement.

See Also:

The [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for further information about cross-instance registration, shared and dedicated server configurations, and connection load balancing

## 7.9 Configuring the Listener File (listener.ora)

You can configure two types of listeners in the `listener.ora` file as described in the following sections:

- Grid Naming Service (GNS) and Listeners
- About Local Listeners
- About Multiple Listeners
- How Oracle Database Uses the Listener File (listener.ora)

### 7.9.1 Grid Naming Service (GNS) and Listeners

If you enable Grid Naming Service (GNS), then you do not have to manually configure the listener. In GNS configurations, there is one GNS daemon for the cluster. Service requests to the cluster domain that GNS manages are routed to the GNS virtual IP address, which routes these requests to the GNS daemon.

The GNS daemon listens for registrations. When a SCAN virtual IP starts, it registers its addresses with GNS. When GNS receives a request from a DNS for the SCAN, it returns the registered addresses to the DNS.

### 7.9.2 About Local Listeners

During Oracle Database creation, the `LOCAL_LISTENER` parameter is automatically configured to point to the local listener for the database. The Database Agent sets the `LOCAL_LISTENER` parameter to a connect descriptor that does not require a TNS alias.

You can set a value manually for LOCAL\_LISTENER. However, Oracle recommends that you leave the parameter unset so that the Database Agent can maintain it automatically.

For example, after you create the database, if you need to add a second listener, listening on port 2012, then use the following command to have the database register with both listeners on startup:

```
> alter system set local_listener='(DESCRIPTION=
(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.0.61)(PORT=1521))
(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.0.61)(PORT=2012))))' 
scope=BOTH SID='OCRL1';
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for information about understanding and configuring listeners

The `tnsnames.ora` file is located in the path `$ORACLE_HOME/network/admin`. By default, the `tnsnames.ora` file is read from the Oracle Grid Infrastructure home, in the path Grid\_home `/network/admin`.

The listener association no longer requires `tnsnames.ora` file entries. The REMOTE\_LISTENER is configured by DBCA to reference the SCAN name and port, without any need for a `tnsnames.ora` entry.

The following is an example of an Oracle RAC 11g release 2 (11.2) `tnsnames.ora` file:

```
# tnsnames.ora Network Configuration file:
/u01/app/oracle/product/11.2.0/dbhome_1/network/admin/tnsnames.ora
# Generated by Oracle Configuration tools
RACDB =
   (DESCRIPTION = 
     (ADDRESS = (PROTOCOL = TCP)(HOST = myscan.mycluster.example.com)(PORT = 1521)
)
     (CONNECT_DATA =
       (SERVER = DEDICATED)
       (SERVICE_NAME = RACDB)
      )
    )
```

### 7.9.3 About Multiple Listeners

If DBCA detects more than one listener on the node, then it displays a list of the listeners. You can select one or all of these listeners with which to register your database.

Note:

To administer 11g release 2 (11.2) local and scan listeners using the `lsnrctl` command, set your ORACLE\_HOME environment variable to the path for the Oracle Grid Infrastructure home (Grid home). Do not attempt to use the `lsnrctl` commands from Oracle home locations for previous releases, because they cannot be used with the new release.

### 7.9.4 How Oracle Database Uses the Listener File (listener.ora)

Services coordinate their sessions by registering their load with the Local Listener and the SCAN Listeners. Clients are redirected by the SCAN Listener to a local listener on the least loaded node that is running the instance for a particular service. That Listener either redirects the client to a Dispatcher process (if the database was configured for Shared Server), or redirects the client to a dedicated server process. Local Listeners are configured to respond to database connection requests, and to non-database connection requests, such as external procedures or XDB requests.

The Listener agent dynamically updates endpoints with the listener. With the Oracle Database 11g release 2 installation, the `listener.ora` file now only contains an IPC key and the following information:

(ADDRESS = (PROTOCOL=TCP)(HOST=)(PORT=1521))

This information refers implicitly to the local node's HOST endpoint. The `listener.ora` file is the same on every node.

Before you install Oracle RAC, during the Oracle Grid Infrastructure installation, Oracle Net Configuration Assistant creates and starts a default listener in the Grid home called `LISTENER`. The listener is configured with default protocol listening addresses. The listener is configured to respond to connection requests that are directed to one protocol address specified during installation.

During Oracle RAC installation, the Oracle RAC database uses the Oracle Clusterware listener, and configures service information about the Oracle RAC database. An Oracle Database 11g release 2 (11.2) database service automatically registers its information with the listener, such as its service name, instance names, and load information. This feature, called service registration, does not require configuration in the `listener.ora` file. After listener creation, Oracle Net Configuration Assistant starts the listener.

After installation, you can modify listeners by using `srvctl` commands, or by using NetCA. Manual editing of the `listener.ora` file is not required.

The following is an example `listener.ora` file with an entry for a node named `node1`:

```
LISTENER_SCAN1=(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=IPC)(KEY=LISTENER_
SCAN1))))               # line added by Agent
LISTENER_NODE1=(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=IPC) (KEY=LISTENER))))
          # line added by Agent
# listener.ora.mycluster Network Configuration File:
/u01/app/oracle/11.2.0/dbhome_1/network/admin/listener.ora.mycluster
# Generated by Oracle configuration tools.
 
LISTENER_NODE1 =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )
 
ENABLE_GLOBAL_DYNAMIC_ENDPOINT_LISTENER_NODE1=ON              # line added by Agent
ENABLE_GLOBAL_DYNAMIC_ENDPOINT_LISTENER_SCAN2=ON              # line added by Agent
ENABLE_GLOBAL_DYNAMIC_ENDPOINT_LISTENER_SCAN1=ON              # line added by Agen
```

#### 7.9.4.1 Listener Registration and PMON Discovery

When a listener starts after the Oracle instance starts, and the listener is listed for service registration, registration does not occur until the next time the Oracle Database process monitor (PMON) discovery routine starts. By default, PMON discovery occurs every 60 seconds.

To override the 60-second delay, use the SQL `ALTER SYSTEM REGISTER` statement. This statement forces the PMON process to register the service immediately.

Oracle recommends that you create a script to run this statement immediately after starting the listener. If you run this statement while the listener is up and the instance is already registered, or while the listener is down, then the statement has no effect.

See Also:

The [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for further information about the listener and the `listener.ora` file

## 7.10 Net Service Names (tnsnames.ora File)

A `tnsnames.ora` file is created on each node with net service names. A connect identifier is an identifier that maps to a connect descriptor. A connect descriptor contains the following information:

- The network route to the service, including the location of the listener through a protocol address
- The `SERVICE_NAME` for an Oracle Database
	Note:
	The `SERVICE_NAME` parameter that you use in the `tnsnames.ora` file is singular, because you can specify only one service name. There is also the `SERVICE_NAMES` parameter in the database initialization file. The `SERVICE_NAMES` parameter defaults the global database name, a name comprising the `DB_NAME` and `DB_DOMAIN` parameters in the initialization parameter file.

With Oracle Clusterware 11g release 2 and later, Database Configuration Agent (DBCA) no longer sets the LOCAL\_LISTENER parameter. The Oracle Clusterware agent that starts the database sets the LOCAL\_LISTENER parameter dynamically, unless you explicitly set the LOCAL\_LISTENER parameter, using the command ALTER SYSTEM SET LOCAL\_LISTENER to set the LOCAL\_LISTENER parameter manually. Listener\_alias entries are no longer needed in the `tnsnames.ora` file.

For example, after you create the database, if you need to add a second listener, listening on port 2012, then use the following command to have the database register with both listeners on startup:

```
> alter system set local_listener='(DESCRIPTION=
(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.0.61)(PORT=1521))
(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.0.61)(PORT=2012))))' 
scope=BOTH SID='OCRL1';
```

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11120)

For the REMOTE\_LISTENER parameter, Oracle Clusterware uses the EZ connect syntax scanname:scanport, so that no entries are needed for the REMOTE\_LISTENER parameter in the `tnsnames.ora` file.

DBCA creates net service names for connections as described in the following sections:

Review the following sections for information about net service names:

- Net Service Names for Database Connections
- Net Service Name Instance Connections
- tnsnames.ora Example File

### 7.10.1 Net Service Names for Database Connections

Clients that connect to any instance of the database use the SCAN name for the database. This entry also enables Oracle Enterprise Manager to discover an Oracle RAC database.

Three SCAN addresses are configured for the cluster, and allocated to servers. If the chosen address fails, then the connection request to the SCAN name fails over to the next address. Thus, if an instance fails, then clients can still connect using another instance.

In the following example, `myscan.mycluster.example.com` is used by the client to connect to the target database, `mycluster.example.com`.

```
mycluster.example.com =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = host=myscan.mycluster.example.com)(PORT = 1522))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = myApp)
    )
```

An Easy Connect address for this database should be similar to the following:

```
myscan.mycluster.example.com/mycluster.example.com
```

### 7.10.2 Net Service Name Instance Connections

Clients that connect to a particular instance of the database use the SCAN name for the instance. This entry, for example, enables Oracle Enterprise Manager to discover the instances in the cluster. These entries are also used to start and stop instances.

In the following example, Oracle Enterprise Manager uses `myscan.mycluster.example.com` to connect to an instance named `mycluster1` on node1:

```
mycluster1.example.com=
 (description= 
  (address=(protocol=tcp)(host=myscan.mycluster.example.com)(port=1521))
  (connect_data= 
    (service_name=mycluster.example.com)
    (instance_name=mycluster1)))
```

### 7.10.3 tnsnames.ora Example File

This example is a sample `tnsnames.ora` file that is created during a preconfigured database configuration installation.

```
# tnsnames.ora Network Configuration File: /u01/app/oracle/11.2.0/dbhome_1/network/admin/tnsnames.ora
# Generated by Oracle configuration tools.
 
sales =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = myscan.mycluster.example.com)(PORT = 1522))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = myApp)
    )
```

See Also:

The [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG302) for further information about the `tnsnames.ora` file

## 7.11 Net Services Profile (sqlnet.ora File)

Oracle Universal Installer starts Oracle Net Configuration Assistant after the database is installed, and creates the Net Services profile, or `sqlnet.ora` file.

By default, the `sqlnet.ora` file is located in the following directory:

```
$ORACLE_HOME/network/admin
```

In this directory, in addition to the default `sqlnet.ora` file generated during installation, you also can find a sample `sqlnet.ora` file in the directory `sample`.

During installation, Oracle Net Configuration Assistant creates the following entries in the `sqlnet.ora` file, where Oracle\_base is the path to the Oracle RAC installation owner's Oracle base directory:

```
NAMES.DIRECTORY_PATH=(TNSNAMES, EZCONNECT)
ADR_BASE =Oracle_base
```

The parameter `NAMES.DIRECTORY_PATH` specifies the priority order of the naming methods to use to resolve connect identifiers to connect descriptors.

The Easy Connect naming method eliminates the need for service name lookup in the `tnsnames.ora` files for TCP/IP environments. With Easy Connect, clients use a connect string for a simple TCP/IP address, consisting of a host name and optional port and service name. If you use this method, then no naming or directory system is required.

See Also:

The [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for further information about the `sqlnet.ora` file
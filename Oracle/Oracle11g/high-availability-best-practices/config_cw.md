---
title: Configuring Oracle Database with Oracle Clusterware
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_cw.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 6 Configuring Oracle Database with Oracle Clusterware

Oracle Clusterware enables servers to communicate with each other, so that they appear to function as a collective unit. Oracle Clusterware provides the infrastructure necessary to run Oracle Real Application Clusters (Oracle RAC) and Oracle RAC One Node. The Grid Infrastructure is the software that provides the infrastructure for an enterprise grid architecture. In a cluster, this software includes Oracle Clusterware and Oracle ASM. For a standalone server, the Grid Infrastructure includes Oracle Restart and Oracle ASM. Oracle Database 11g Release 2 combines these infrastructure products into one software installation called the Grid Infrastructure home.

This chapter contains the following topics:

## 6.1 About Oracle Clusterware Best Practices

Oracle Clusterware, as part of Oracle Grid Infrastructure, is software that manages the availability of user applications and Oracle databases. Oracle Clusterware is the only clusterware needed for most platforms on which Oracle RAC operates. You can also use clusterware from other vendors in addition to Oracle Clusterware on the same system, if needed. However, adding unnecessary layers of software for functionality that is provided by Oracle Clusterware adds complexity and cost and can reduce system availability, especially for planned maintenance.

Note:

Before installing Oracle RAC or Oracle RAC One Node, you must first install Oracle Grid Infrastructure, which consists of Oracle Clusterware and Oracle Automatic Storage Management (ASM). After Oracle Clusterware and Oracle ASM are operational, you can use Oracle Universal Installer to install the Oracle Database software with the Oracle RAC components.

Oracle Clusterware includes a high availability framework that provides an infrastructure to manage any application. Oracle Clusterware ensures that the applications it manages start when the system starts and monitors the applications to ensure that they are always available. If a process fails then Oracle Clusterware attempts to restart the process using agent programs (agents). Oracle clusterware provides built-in agents so that you can use shell or batch scripts to protect and manage an application. Oracle Clusterware also provides preconfigured agents for some applications (for example for Oracle TimesTen In-Memory Database). If a node in the cluster fails, then you can program processes that normally run on the failed node to restart on another node. The monitoring frequency, starting, and stopping of the applications and the application dependencies are configurable.

Oracle RAC One Node is a single instance of an Oracle RAC database that runs on one node in a cluster. For information about working with Oracle RAC One Node, see [Section 7.2, "Configuring Oracle Database with Oracle RAC One Node"](config_rac.md).

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crschp.htm#CWADD91277) for information about Making Applications Highly Available Using Oracle Clusterware
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/install_rac.htm#TDPRC162) for more information about installing Oracle Grid Infrastructure for a cluster

### 6.1.1 Client Configuration and Migration Concepts

Oracle provides the following features to enable you to migrate client connections between nodes. These features minimize the impact of a node failure from the client perspective:

- Client-side load balancing and connection load balancing. For more information see Section 6.2.6, "Use Client-Side and Server-Side Load Balancing."
- Single Client Access Name (SCAN)
- Fast Application Notification (FAN)
- Fast Connection Failover (FCF) (ideally used by FAN-enabled clients)

Tip:

For more information about using and configuring Fast Connection Failover (FCF), see [Chapter 11, "Configuring Fast Connection Failover."](config_fcf.md)

#### 6.1.1.1 Services

The use of Fast Application Notification (FAN) requires the use of Services. Services de-couple any hardwired mapping between a connection request and an Oracle RAC instance. Services are an entity defined for an Oracle RAC database that allows the workload for an Oracle RAC database to be managed. Services divide the entire workload executing in the Oracle Database into mutually disjoint classes. Each service represents a workload with common attributes, service level thresholds, and priorities. The grouping is based on attributes of the work that might include the application being invoked, the application function to be invoked, the priority of execution for the application function, the job class to be managed, or the data range used in the application function or job class.

To manage workloads or a group of applications, you can define services that you assign to a particular application or to a subset of an application's operations. You can also group work by type under services. For example, online users can use one service, while batch processing can use another and reporting can use yet another service to connect to the database.

Oracle recommends that all users who share a service have the same service level requirements. You can define specific characteristics for services and each service can represent a separate unit of work. There are many options that you can take advantage of when using services. Although you do not have to implement these options, using them helps optimize application performance.

#### 6.1.1.2 Fast Application Notification (FAN)

Fast Application Notification (FAN) is a notification mechanism that is integrated into Oracle Clusterware to notify registered clients about configuration and service level information that includes service status changes, such as UP or DOWN events. Applications can respond to FAN events and take immediate action. FAN UP and DOWN events can apply to instances, services, and nodes.

For cluster configuration changes, the Oracle RAC high availability framework publishes a FAN event immediately when a state change occurs in the cluster. Instead of waiting for the application to poll the database and detect a problem, applications can receive FAN events and react immediately. With FAN, in-flight transactions can be immediately terminated and the client notified when the instance fails.

FAN also publishes load balancing advisory events. Applications can take advantage of the load balancing advisory FAN events to direct work requests to the instance in the cluster that is currently providing the best service quality.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13179) for more information about Overview of Fast Application Notification

#### 6.1.1.3 Single Client Access Name (SCAN)

Single Client Access Name (SCAN) is a new Oracle Real Application Clusters (Oracle RAC) 11g Release 2 feature that provides a single name for clients to access an Oracle Database running in a cluster. The benefit is clients using SCAN do not need to change their connect string if you add or remove nodes in the cluster. Having a single name to access the cluster allows clients to use the EZConnect client and the simple JDBC thin URL to access any database running in the clusters independently of which server(s) in the cluster the database is active. SCAN provides load balancing and failover of client connections to the database. The SCAN is a virtual IP name, similar to the names used for virtual IP addresses, such as `node1-vip`. However, unlike a virtual IP, the SCAN is associated with the entire cluster, rather than an individual node, and associated with multiple IP addresses, not just one address.

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD92091) for more information about Single Client Access Name (SCAN)
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG1125) for more information about EZConnect

## 6.2 Oracle Clusterware Configuration Best Practices

Use the following Oracle Clusterware configuration best practices:

- Use the Cluster Verification Utility (CVU)
- Use a Local Home for Oracle Database and Oracle Clusterware with Oracle ASM
- Ensure Services are Highly Available
- Client Configuration and FAN Best Practices
- Connect to Database Using Services and Single Client Access Name (SCAN)
- Use Client-Side and Server-Side Load Balancing
- Mirror Oracle Cluster Registry (OCR) and Configure Multiple Voting Disks with Oracle ASM
- Use Company Wide Cluster Time Management
- Verify That Oracle Clusterware, Oracle RAC, and Oracle ASM Use the Same Interconnect Network
- Use Redundant Interconnect with Highly Available IP (HAIP)
- Configure Failure Isolation with Intelligent Management Platform Interface (IPMI)

### 6.2.1 Use the Cluster Verification Utility (CVU)

Cluster Verification Utility (CVU) can verify the primary cluster components during installation and you can use utility to verify configuration and components. A component can be basic, such as free disk space, or it can be complex, such as checking Oracle Clusterware integrity. For example, CVU can verify multiple Oracle Clusterware subcomponents across Oracle Clusterware layers. Additionally, CVU can check disk space, memory, processes, and other important cluster components.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for information about the Cluster Verification Utility

### 6.2.2 Use a Local Home for Oracle Database and Oracle Clusterware with Oracle ASM

All rolling patch features require that the software home being patched is local, not shared. The software must be physically present in a local file system on each node in the cluster and it is not on a shared cluster file system.

The reason for this requirement is that if a shared cluster file system is used, patching the software on one node affects all of the nodes, and would require that you shut down all components using the software on all nodes. Using a local file system allows software to be patched on one node without affecting the software on any other nodes.

Note the following when you install Oracle Grid Infrastructure and configure Oracle Clusterware:

- Oracle RAC databases require shared storage for the database files.
- Configure Oracle Cluster Registry (OCR) and voting files to use Oracle ASM. For more information, see Section 6.2.7, "Mirror Oracle Cluster Registry (OCR) and Configure Multiple Voting Disks with Oracle ASM"
- Oracle recommends that you install Oracle Database on local homes, rather than using a shared home on shared storage. It is recommended to not use a shared file system for the Oracle Database Home (using a shared home prevents you from doing rolling upgrades, as all software running from that shared location must be stopped before it can be patched).
- Oracle Clusterware and Oracle ASM are both installed in one home on a non shared file system called the Grid Infrastructure home (`Grid_home`).

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/install_rac.htm#TDPRC162) for more information about installing Oracle ASM

### 6.2.3 Ensure Services are Highly Available

For cases where a service only has one preferred instance, ensure that the service is started immediately on an available instance after it is brought down on its preferred instance. Starting the service immediately ensures that affected clients can instantaneously reconnect and continue working. Oracle Clusterware handles this responsibility and it is of utmost importance during unplanned outages.

Even though you can rely on Oracle Clusterware to start the service during planned maintenance as well, it is safer to ensure that the service is available on an alternate instance by manually starting an alternate preferred instance ahead of time. Manually starting an alternate instance eliminates the single point of failure with a single preferred instance and you have the luxury to do this because it is a planned activity. Add at least a second preferred instance to the service definition and start the service before the planned maintenance. You can then stop the service on the instance where maintenance is being performed with the assurance that another service member is available. Adding one or more preferred instances does not have to be a permanent change. You can revert it back to the original service definition after performing the planned maintenance.

Manually relocating a service rather than changing the service profile is advantageous in cases such as the following:

- If you are using Oracle XA, then use of manual service relocation is advantageous because, although the XA specification allows for a transaction branch to be suspended and resumed by the TM, if connection load balancing is utilized then any resumed connection could land on an alternate Oracle instance to the one that the transaction branch started on and there is a performance implication if a single distributed transaction spans multiple database instances.
- If an application is not designed to work properly with multiple service members, then application errors or performance issues can arise.

As with all configuration changes, you should test the effect of a service with multiple members to assess its viability and impact in a test environment before implementing the change in your production environment.

See Also:

The Technical Article, "XA and Oracle controlled Distributed Transactions" on the Oracle Real Application Clusters website at `http://www.oracle.com/technetwork/database/clustering/overview/index.html`

### 6.2.4 Client Configuration and FAN Best Practices

The ability to migrate client connections to and from the nodes on which you are working is a critical aspect of planned maintenance. Migrating client connections should always be the first step in any planned maintenance activity requiring software shutdown (for example, when performing a rolling upgrade). The potential for problems increases if there are still active database connections when the service switchover commences.

An example of a best-practice process for client redirection during planned maintenance could involve the following steps:

1. Client is configured to receive FAN notifications and is properly configured for run time connection load balancing and Fast Connection Failover.
2. Oracle Clusterware stops services on the instance to be brought down or relocates services to an alternate instance.
3. Oracle Clusterware returns a `Service-Member-Down` event.
4. Client that is configured to receive FAN notifications receives a notification for a `Service-Member-Down` event and moves connections to other instances offering the service.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) for an Introduction to Automatic Workload Management.
- Detailed information about client failover best practices in an Oracle RAC environment are available in the "Automatic Workload Management with Oracle Real Application Clusters 11g" Technical Article on the Oracle Technology Network at
	`http://www.oracle.com/technetwork/database/clustering/overview/index.html`

### 6.2.5 Connect to Database Using Services and Single Client Access Name (SCAN)

With Oracle Database 11g, application workloads can be defined as services so that they can be automatically or manually managed and controlled. For manually managed services, DBAs control which processing resources are allocated to each service during both normal operations and in response to failures. Performance metrics are tracked by service and thresholds set to automatically generate alerts should these thresholds be crossed. CPU resource allocations and resource consumption controls are managed for services using Database Resource Manager. Oracle tools and facilities such as Job Scheduler, Parallel Query, and Oracle Streams Advanced Queuing also use services to manage their workloads.

With Oracle Database 11g, you can define rules to automatically allocate processing resources to services. Oracle RAC in Oracle Database release 11g instances can be allocated to process individual services or multiple services, as needed. These allocation rules can be modified dynamically to meet changing business needs. For example, you could modify these rules at quarter end to ensure that there are enough processing resources to complete critical financial functions on time. You can also define rules so that when instances running critical services fail, the workload is automatically shifted to instances running less critical workloads. You can create and administer services with the SRVCTL utility or with Oracle Enterprise Manager.

You should make application connections to the database by using a VIP address (preferably SCAN) in combination with a service to achieve the greatest degree of availability and manageability.

A VIP address is an alternate public address that client connections use instead of the standard public IP address. If a node fails, then the node's VIP address fails over to another node but there is no listener listening on that VIP, so a client that attempts to connect to the VIP address receives a connection refused error (`ORA-12541`) instead of waiting for long TCP connect timeout messages. This error causes the client to quickly move on to the next address in the address list and establish a valid database connection. New client connections can initially try to connect to a failed-over-VIP, but when there is no listener running on that VIP the "no listener" error message is returned to the clients. The clients traverse to the next address in the address list that has a non-failed-over VIP with a listener running on it.

The Single Client Access Name (SCAN) is a fully qualified name (hostname+domain) that is configured to resolve to all three of the VIP addresses allocated for the SCAN. The addresses resolve using Round Robin DNS either on the DNS server, or within the cluster in a GNS configuration. SCAN listeners can run on any node in the cluster, multiple SCAN listeners can run on one node.

Oracle Database 11g Release 2 and later, by default, instances register with SCAN listeners as remote listeners.

SCANs are cluster resources. SCAN vips and SCAN listeners run on random cluster nodes. SCANs provide location independence for the databases, so that client configuration does not have to depend on which nodes are running a particular database. For example, if you configure policy managed server pools in a cluster, then the SCAN enables connections to databases in these server pools regardless of which nodes are allocated to the server pool.

SCAN names functions like a virtual cluster address. SCANs are resolved to three SCAN VIPs that may run on any node in the cluster. So unlike a VIP address per node as entry point, clients connecting to the SCAN no longer require any updates on how they connect when a virtual IP addresses is added, changed, or removed from the cluster. The SCAN addresses resolve to the cluster, rather than to a specific node address.

During Oracle Grid Infrastructure installation, SCAN listeners are created for as many IP addresses as there are addresses assigned to resolve to the SCAN. Oracle recommends that the SCAN resolves to three addresses, to provide high availability and scalability. If the SCAN resolves to three addresses, then there are three SCAN listeners created.

Oracle RAC provides failover with the node VIP addresses by configuring multiple listeners on multiple nodes to manage client connection requests for the same database service. If a node fails, then the service connecting to the VIP is relocated transparently to a surviving node. If the client or service are configured with transparent application failover options, then the client is reconnected to a surviving node. When a SCAN Listener receives a connection request, the SCAN Listener checks for the least loaded instance providing the requested service. It then re-directs the connection request to the local listener on the node where the least loaded instance is running. Subsequently, the client is given the address of the local listener. The local listener finally creates the connection to the database instance.

Clients configured to use IP addresses for Oracle Database releases before Oracle Database 11g Release 2 can continue to use their existing connection addresses; using SCANs is not required: in this case, the pre-Database 11g Release 2 client would use a TNS connect descriptor that resolves to the node-VIPs of the cluster. When an earlier version of Oracle Database is upgraded, it registers with the SCAN listeners, and clients can start using the SCAN to connect to that database. The database registers with the SCAN listener through the remote listener parameter in the init.ora file. The `REMOTE_LISTENER` parameter must be set to SCAN:PORT. Do not set it to a TNSNAMES alias with a single address with the SCAN as HOST=SCAN. Having a single name to access the cluster allows clients to use the EZConnect client and the simple JDBC thin URL to access any database running in the cluster, independently of which server(s) in the cluster the database is active. For example:

```
sqlplus system@sales1-scan:1521/oltp
```

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) for more information about automatic workload management
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admcon.htm#RACAD7273) for an Overview of Connecting to Oracle Database Using Services and VIP Addresses
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD91886) for more information about Oracle Clusterware Network Configuration Concepts
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG1125) for more information about EZConnect

### 6.2.6 Use Client-Side and Server-Side Load Balancing

Client-side load balancing is defined in your client connection definition (tnsnames.ora file, for example) by setting the `LOAD_BALANCE` parameter to `LOAD_BALANCE=ON`. When you set this parameter to `ON`, Oracle Database randomly selects an address in the address list, and connects to that node's listener. This balances client connections across the available SCAN listeners in the cluster.

The SCAN listener redirects the connection request to the local listener of the instance that is least loaded and provides the requested service. When the listener receives the connection request, the listener connects the user to an instance that the listener knows provides the requested service. To see what services a listener supports, run the `lsnrctl` services command.

When clients connect using SCAN, Oracle Net automatically load balances client connection requests across the three IP addresses you defined for the SCAN, unless you are using EZConnect.

Server-side load balancing When you create an Oracle RAC database with DBCA, it automatically:

- Configures and enables server-side load balancing
- Sets the remote listener parameter to the SCAN listener (Note: If you do not use DBCA, you should set the `REMOTE_LISTENER` database parameter to scan\_name:scan\_port.)
- Creates a sample client-side load balancing connection definition in the tnsnames.ora file on the server

Note:

The following features do not work with the default database service. You must create cluster managed services to take advantage of these features. You can only manage the services that you create. Any service created automatically by the database server is managed by the database server.

To further enhance connection load balancing, use the Load Balancing Advisory and define the connection load balancing for each service. Load Balancing Advisory provides information to applications about the current service levels that the database and its instances are providing. The load balancing advisory makes recommendations to applications about where to direct application requests to obtain the best service based on the policy that you have defined for that service. Load balancing advisory events are published through ONS. There are two types of service-level goals for run-time connection load balancing:

`SERVICE_TIME`: Attempts to direct work requests to instances according to response time. Load balancing advisory data is based on elapsed time for work done in the service plus available bandwidth to the service. An example for the use of `SERVICE_TIME` is for workloads such as internet shopping where the rate of demand changes. The following example shows how to set the goal to `SERVICE_TIME` for connections using the online service:

```
srvctl modify service -d db_unique_name
 -s online -B SERVICE_TIME -j SHORT
```

`THROUGHPUT`: Attempts to direct work requests according to throughput. The load balancing advisory is based on the rate that work is completed in the service plus available bandwidth to the service. An example for the use of `THROUGHPUT` is for workloads such as batch processes, where the next job starts when the last job completes. The following example shows how to set the goal to `THROUGHPUT` for connections using the `sjob` service:

```
srvctl modify service -d db_unique_name
 -s sjob -B THROUGHPUT -j LONG
```

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD7122) for more information about Connection Load Balancing and Load Balancing Advisory
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD7302) for information about Configuring Your Environment to Use the Load Balancing Advisory
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG010) for more information about configuring listeners
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams120.htm#REFRN10082) for more information about the [`LOCAL_LISTENER`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams120.htm#REFRN10082) and [`REMOTE_LISTENER`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams211.htm#REFRN10183) parameters

### 6.2.7 Mirror Oracle Cluster Registry (OCR) and Configure Multiple Voting Disks with Oracle ASM

Configure Oracle Cluster Registry (OCR) and voting files to use Oracle ASM. It is recommended to mirror OCR and configure multiple voting disks using an Oracle ASM high redundancy disk group when available.

The Oracle Cluster Registry (OCR) contains important configuration data about cluster resources. Always protect the OCR by using Oracle ASM redundant disk groups for example. Oracle Clusterware uses the Oracle Cluster Registry (OCR) to store and manage information about the components that Oracle Clusterware controls, such as Oracle RAC databases, listeners, virtual IP addresses (VIPs), and services and any applications. To ensure cluster high availability when using a shared cluster file system, as opposed to when using Oracle ASM, Oracle recommends that you define multiple OCR locations.

In addition:

- You can have up to five OCR locations
- Each OCR location must reside on shared storage that is accessible by all of the nodes in the cluster
- You can replace a failed OCR location online if it is not the only OCR location
- You must update OCR through supported utilities such as Oracle Enterprise Manager, the Server Control Utility (SRVCTL), the OCR configuration utility (OCRCONFIG), or the Database Configuration Assistant (DBCA)

Each OCR location must reside on shared storage that is accessible by all of the nodes in the cluster and the voting disk also must reside on shared storage. For high availability, Oracle recommends that you have multiple voting disks on multiple storage devices across different controllers, where possible. Oracle Clusterware enables multiple voting disks, but you must have an odd number of voting disks, such as three, five, and so on. If you define a single voting disk, then you should use external redundant storage to provide redundancy.

Extended Oracle RAC requires a quorum (voting) disk that should be on an arbiter site at a location different from the main sites (data centers). For more information, see [Section 7.3.2, "Add a Third Voting Disk to Host the Quorum Disk"](config_rac.md).

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm#CWADD90964) for information about Adding, Replacing, Repairing, and Removing Oracle Cluster Registry Locations
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/adminoc.htm#TDPRC221) for more information about managing OCR and voting disks
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD90952) for information about voting disks and oracle cluster registry requirements

### 6.2.8 Use Company Wide Cluster Time Management

The Cluster Time Synchronization Service (CTSS) is installed as part of Oracle Clusterware. By default the CTSS runs in observer mode if it detects a time synchronization service or a time synchronization service configuration, valid or broken, on the system. If CTSS detects that there is no time synchronization service or time synchronization service configuration on any node in the cluster, then CTSS goes into active mode and takes over time management for the cluster.

The Network Time Protocol (NTP) is a client/server application. Each server must have NTP client software installed and configured to synchronize its clock to the network time server. The Windows Time service is not an exact implementation of the NTP, but it based on the NTP specifications.

As a best practice use company-wide NTP.

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/preparing.htm#TDPRC140) for information About Setting the Time on All Nodes
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91999) for information about Cluster Time Synchronization Service (CTSS) and Cluster Time Management

### 6.2.9 Verify That Oracle Clusterware, Oracle RAC, and Oracle ASM Use the Same Interconnect Network

For efficient network detection and failover and optimal performance, Oracle Clusterware, Oracle RAC, and Oracle ASM should use the same dedicated interconnect subnet so that they share the same view of connections and accessibility.

Perform the following steps to verify the interconnect subnet:

1. To verify the interconnect subnet for Oracle RAC and for Oracle ASM instances, do either of the following:
	- Issue the command:
		```
		SQL> select * from v$cluster_interconnects;
		 
		NAME   IP_ADDRESS      IS_PUBLIC    SOURCE
		-----  ----------      ---------    -------
		bond0  192.168.32.87   NO           cluster_interconnects parameter
		```
		- View instances information in the alert log to verify the interconnect subnet.
2. To verify the interconnect subnet used by the clusterware:
	```
	prompt> $GI_HOME/bin/oifcfg getif | grep cluster_interconnect
	bond0 192.168.32.0 global cluster_interconnect
	```

See:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/diag.htm#ADMIN11267) for information about Viewing the Alert Log

### 6.2.10 Use Redundant Interconnect with Highly Available IP (HAIP)

You can define multiple interfaces for Redundant Interconnect Usage by classifying the interfaces as private either during installation or after installation using the `oifcfg` `setif` command. When you do, Oracle Clusterware creates from one to four (depending on the number of interfaces you define) highly available IP (HAIP) addresses, which Oracle Database and Oracle ASM instances use to ensure highly available and load balanced communications. With HAIP, by default, interconnect traffic is load balanced across all active interconnect interfaces, and corresponding HAIP address are failed over transparently to other adapters if one fails or becomes non-communicative.

The Oracle software (including Oracle RAC, Oracle ASM, and Oracle ACFS, all Oracle Database 11g release 2 (11.2.0.2), or later), by default, uses these HAIP addresses for all of its traffic allowing for load balancing across the provided set of cluster interconnect interfaces. If a defined cluster interconnect interface fails or becomes non-communicative, then Oracle Clusterware transparently moves the corresponding HAIP address to a remaining functional interface.

Note:

Oracle Databases releases before Oracle Database 11g release 2 cannot use the Redundant Interconnect Usage feature and must use Operating System based interface bonding technologies instead.

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92358) for information about Redundant Interconnect Usage with HAIP
- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for information about defining interfaces
- For more information, see "11gR2 Grid Infrastructure Redundant Interconnect and ora.cluster\_interconnect.haip" in My Oracle Support Note 1210883.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1210883.1`

### 6.2.11 Configure Failure Isolation with Intelligent Management Platform Interface (IPMI)

Failure isolation is a process by which a failed node is isolated from the rest of the cluster to prevent the failed node from corrupting data. The ideal fencing involves an external mechanism capable of restarting a problem node without cooperation either from Oracle Clusterware or from the operating system running on that node. To provide this capability, Oracle Clusterware 11g Release 2 (11.2) and later supports the Intelligent Management Platform Interface specification (IPMI), an industry-standard management protocol.

Typically, you configure failure isolation using IPMI during Grid Infrastructure installation, when you are provided with the option of configuring IPMI from the Failure Isolation Support screen. If you do not configure IPMI during installation, then you can configure it after installation using the Oracle Clusterware Control utility (`CRSCTL`).

See:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92099) for information about IPMI and for information about Configuring IPMI for Failure Isolation

## 6.3 Oracle Clusterware Operational Best Practices

Operational best practices for Oracle Clusterware include:

- Capacity Planning
- Regularly Back Up OCR to Tape or Offsite

### 6.3.1 Capacity Planning

Proper capacity planning is a critical success factor for all aspects of Oracle clustering technology, but it is of particular importance for planned maintenance. You must ensure that the work a cluster is responsible for can be done when a small part of the cluster, for example, a node, is unavailable. If the cluster cannot keep up after a planned or unplanned outage, the potential for cascading problems is higher due to system resource starvation.

When sizing your cluster, ensure that n percentage of the cluster can meet your service levels where n percentage represents the amount of computing resource left over after a typical planned or unplanned outage. For example, if you have a four-node cluster and you want to apply patches in a rolling fashion—meaning one node is upgraded at a time—then three nodes can run the work requested by the application.

One other aspect to capacity planning that is important during planned maintenance is ensuring that any work being done as part of the planned maintenance is separated from the application work when possible. For example, if a patch requires that a SQL script is run after all nodes have been patched, it is a best-practice to run this script on the last node receiving the patch before allowing the application to start using that node. This technique ensures that the SQL script has full use of the operating system resources on the node and it is less likely to affect the application. For example, the `CATCPU.SQL` script that must be run after installing the CPU patch on all nodes.

### 6.3.2 Regularly Back Up OCR to Tape or Offsite

Oracle Clusterware automatically creates Oracle Cluster Registry (OCR) backups every four hours on one node in the cluster, which is the OCR master node. Oracle always retains the last three backup copies of OCR. The `CRSD` process that creates the backups also creates and retains an OCR backup for each full day and after each week. You should use Oracle Secure Backup, or standard operating-system tools, or third-party tools to back up the backup files created by Oracle Clusterware as part of the operating system backup.

Note:

The default location for generating OCR backups on UNIX-based systems is `CRS_HOME/cdata/` `cluster_name` where `cluster_name` is the name of your cluster. The Windows-based default location for generating backups uses the same path structure. Backups are taken on the OCR master node. To list the node and location of the backup, issue the `ocrconfig -showbackup` command.

In addition to using the automatically created OCR backup files, you can use the `-manualbackup` option on the `ocrconfig` command to perform a manual backup, on demand. For example, you can perform a manual backup before and after you make changes to the OCR such as adding or deleting nodes from your environment, modifying Oracle Clusterware resources, or creating a database. The `ocrconfig -manualbackup` command exports the OCR content to a file format. You can then backup the export files created by `ocrconfig` as a part of the operating system backup using Oracle Secure backup, standard operating-system tools, or third-party tools.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD838) for more information about backing up the OCR
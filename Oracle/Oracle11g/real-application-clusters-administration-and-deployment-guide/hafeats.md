---
title: Introduction to Automatic Workload Management
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 5 Introduction to Automatic Workload Management

When a user or application connects to a database, Oracle recommends that you use a service specified in the `CONNECT_DATA` portion of the connect string. Oracle Database automatically creates one database service when the database is created. For many installations, this may be all you need. To enable more flexibility in the management of the workload using the database, Oracle Database enables you to create multiple services and specify which instances (or the server pools that contain the instances) the services are started on. If you are interested in greater workload management flexibility, then continue reading this chapter to understand the added features that you can use with services.

Note:

The features discussed in this chapter do not work with the default database service. You must create cluster managed services to take advantage of these features. You can only manage the services that you create. Any service created automatically by the database server is managed by the database server.

This chapter describes how to manage workloads in Oracle Real Application Clusters (Oracle RAC) to provide high availability and scalability for your applications. This chapter includes the following topics:

## Overview of Automatic Workload Management

Automatic workload management enables you to manage workload distributions to provide optimal performance for users and applications. Automatic workload management comprises the following:

- Services: Oracle Database provides a powerful automatic workload management facility, called services, to enable the enterprise grid vision. Services are entities that you can define in Oracle RAC databases that enable you to group database workloads and route work to the optimal instances that are assigned to offer the service.
- Connection Load Balancing: A feature of Oracle Net Services that balances incoming connections across all of the instances that provide the requested database service.
- High Availability Framework: An Oracle RAC component that enables Oracle Database to always maintain components in a running state.
- Event Notification: Oracle Clusterware generates events that can be received by application subscribers and listeners. These events are used for:
	- Fast Application Notification (FAN): Provides information to Oracle RAC applications and clients about cluster state changes and workload service level changes, such as `UP` and `DOWN` events for instances, services, or nodes. FAN has two methods for publishing events to clients, the Oracle Notification Service daemon, which is used by Java Database Connectivity (JDBC) clients including the Oracle Application Server, and Oracle Streams Advanced Queueing, which is used by Oracle Call Interface and Oracle Data Provider for.NET (ODP.NET) clients.
		- Load Balancing Advisory: Provides information to applications about the current service levels that the database and its instances are providing. The load balancing advisory makes recommendations to applications about where to direct application requests to obtain the best service based on the policy that you have defined for that service. Load balancing advisory events are published through Oracle Notification Service.
- Automatic Workload Repository (AWR): Tracks service-level statistics as [metric](rac_glossary.md) s. Server generated alerts can be created for these metrics when they exceed or fail to meet certain thresholds.
- Fast Connection Failover: This is the ability of Oracle Clients to provide rapid failover of connections by subscribing to FAN events.
- Runtime Connection Load Balancing: This is the ability of Oracle Clients to provide intelligent allocations of connections in the connection pool based on the current service level provided by the database instances when applications request a connection to complete some work.
- Single Client Access Name (SCAN): Provides a single name to the clients connecting to Oracle RAC that does not change throughout the life of the cluster, even if you add or remove nodes from the cluster. Clients connecting with SCAN can use a simple connection string, such as a thin JDBC URL or EZConnect, and still achieve the load balancing and client connection failover.

You can deploy Oracle RAC and noncluster Oracle database environments to use automatic workload management features in many different ways. Depending on the number of nodes and your environment's complexity and objectives, your choices for optimal automatic workload management and high-availability configuration depend on several considerations that are described in this chapter.

## Automatic Workload Repository

The [Automatic Workload Repository (AWR)](rac_glossary.md) collects, processes, and maintains performance statistics for the database. The gathered data can be displayed in both reports and views. If you use services with your database, then AWR tracks [metric](rac_glossary.md) s at the service level.

Metrics can be measured against a variety of units, including time, transactions, or database calls. For example, the number of database calls per second is a metric. Server generated alerts can be placed on these metrics when they exceed or fail to meet user-specified thresholds. The database or system administrator can then respond, for example, by:

- Using the Oracle Database Resource Manager to configure the service level for one service to have priorities relative to other services
- Stopping overloaded processes
- Modifying a service level requirement
- Implementing recovery scenarios in response to service quality changes

Using AWR metrics and performance alerts enables you to maintain continued service availability despite service level changes. It also enables you to measure the quality of service provided by the database services.

The AWR ensures that the Oracle Clusterware workload management framework and the database resource manager have persistent and global representations of performance data. This information helps Oracle Database schedule job classes by service and to assign priorities to consumer groups. If necessary, you can rebalance workloads manually with either Oracle Enterprise Manager or SRVCTL. You can also disconnect a series of sessions, but leave the service running.

Note:

Oracle does not recommend using the DBMS\_SERVICE package for use with services used by an Oracle RAC database. Use SRVCTL or Oracle Enterprise Manager to create database services for Oracle RAC.

See Also:

- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_alerts.htm#TDPPT046) for more information on creating alerts for metric thresholds
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF02601) for more information about the Automatic Workload Repository
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_serv.htm#ARPLS092) for details about Oracle Database packages

## Service Deployment Options

This section describes the following service deployment topics:

- Using Oracle Services
- Service Characteristics
- Service Usage in an Oracle RAC Database
- Service Usage in an Oracle RAC Database
- Default Service Connections

### Using Oracle Services

To manage workloads or a group of applications, you can define services that you assign to a particular application or to a subset of an application's operations. You can also group work by type under services. For example, online users can use one service, while batch processing can use another and reporting can use yet another service to connect to the database.

Oracle recommends that all users who share a service have the same service level requirements. You can define specific characteristics for services and each service can represent a separate unit of work. There are many options that you can take advantage of when using services. Although you do not have to implement these options, using them helps optimize application performance.

### Service Characteristics

When you create new services for your database, you should define the automatic workload management characteristics for each service. The characteristics of a service include:

- Service Name
- Net Service Name
- Service Edition
- Service Management Policy
- Database Role for a Service
- Instance Preference
- Server Pool Assignment
- Load Balancing Advisory Goal for Runtime Connection Load Balancing
- Connection Load Balancing Goal
- Distributed Transaction Processing
- Subscription to High Availability Events
- Transparent Application Failover Policy

See Also:

- "Creating Services with SRVCTL" for more information
- ["SRVCTL Command Reference"](srvctladmin.md) for more information about using SRVCTL to create or modify services and descriptions of the various options

#### Service Name

Each Oracle database or service has a service name. The service name for an Oracle database is normally its global database name. The service name is used by clients to connect to one or more instances. The service name should be unique throughout your system.

#### Net Service Name

To connect to a database service, clients use a connect descriptor that provides the location of the database and the name of the database service. A connect descriptor is comprised of one or more protocol addresses of the listener and the connect information for the destination service in the `tnsnames.ora` file.

#### Service Edition

The edition attribute of a database service, which specifies the initial session edition for a session that is started using that service. If the program that creates a new session does not specify the initial session, then the edition name specified by the service is used. If the service does not specify the edition name, then the initial session edition is the database default edition.

#### Service Management Policy

When you use Oracle Clusterware to manage your database, you can configure startup options for each individual database service when you add the service using the `srvctl add service` command with the `-y` option. If you set the management policy for a service to `AUTOMATIC` (the default), then the service starts automatically when you start the database with SRVCTL. If you set the management policy to `MANUAL`, then the service does not automatically start, and you must manually start it with SRVCTL. A `MANUAL` setting does not prevent Oracle Clusterware from monitoring the service when it is running and restarting it if a failure occurs. Prior to Oracle RAC 11g release 2 (11.2), all services worked as though they were defined with a `MANUAL` management policy.

See Also:

`"srvctl add service"` for more usage information

Using CRSCTL to stop and restart Oracle Clusterware is treated as a failure and the service is restarted if it was previously running.

Note:

When you use automatic services in an administrator-managed database, during planned database startup, services may start on the first instances to start rather than their preferred instances.

#### Database Role for a Service

If you configured Oracle Data Guard in your environment, then you can define a role for each service using SRVCTL with the `-l` option. When you specify a role for a service, Oracle Clusterware automatically starts the service only when the database role matches the role you specified for the service. Valid roles are `PRIMARY`, `PHYSICAL_STANDBY`, `LOGICAL_STANDBY`, and `SNAPSHOT_STANDBY`.

If multiple databases in the cluster offer the same service name, then Oracle RAC balances connections to that service across all such databases. This is useful for standby and active Oracle Data Guard databases, but if you want client connections to a service to be directed to a particular database, then the service name must be unique within the cluster (not offered by any other database).

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/concepts.htm#SBYDB4701) for more information about database roles

#### Instance Preference

When you define a service for an administrator-managed database, you define which instances normally support that service using SRVCTL with the `-r` option. These are known as the preferred instances. You can also define other instances to support a service if the service's preferred instance fails using SRVCTL with the `-a` option. These are known as available instances.

When you specify preferred instances, you are specifying the number of instances on which a service normally runs. Oracle Clusterware attempts to ensure that the service always runs on the number of instances for which you have configured the service. Afterwards, due to either instance failure or planned service relocations, a service may be running on an available instance. You cannot control which available instance to which Oracle Clusterware relocates the services if there are multiple instances in the list.

When a service moves to an available instance, Oracle Database does not move the service back to the preferred instance when the preferred instance restarts because:

- The service is running on the desired number of instances.
- Maintaining the service on the current instance provides a higher level of service availability.
- Not moving the service back to the initial preferred instance prevents a second outage.

You can, however, easily automate fail back to the preferred instance by using FAN callouts.

See Also:

["Overview of Oracle RAC Database Administration"](admin.md) for more information about policy-managed and administrator-managed databases

#### Server Pool Assignment

When you define services for a policy-managed database, you assign the service to a server pool where the database is running using SRVCTL with the `-g` option. You can define the service as either `UNIFORM` (running on all instances in the server pool) or `SINGLETON` (running on only one instance in the server pool) using the `-c` option. For singleton services, Oracle RAC chooses on which instance in the server pool the service is active. If that instance fails, then the service fails over to another instance in the server pool. A service can only run in one server pool.

Note:

If you use Oracle Database Quality of Service Management (Oracle Database QoS Management), then you cannot have singleton services in a server pool, unless the maximum size of that server pool is one.

See Also:

["Overview of Oracle RAC Database Administration"](admin.md) for more information about policy-managed and administrator-managed databases

#### Load Balancing Advisory Goal for Runtime Connection Load Balancing

With runtime connection load balancing, applications can use load balancing advisory events to provide better service to users. Oracle JDBC, Oracle Universal Connection Pool (UCP) for Java, Oracle Call Interface, Connection Manager (CMAN), and ODP.NET clients are automatically integrated to take advantage of load balancing advisory events. The load balancing advisory informs the client about the current service level that an instance is providing for a service. To enable the load balancing advisory, use SRVCTL with the `-B` option when creating or modifying the service.

The load balancing advisory also recommends how much of the workload should be sent to that instance. The goal determines whether connections are made to the service based on best service quality (how efficiently a single transaction completes) or best throughput (how efficiently a complete job or long-running query completes).

#### Connection Load Balancing Goal

Oracle Net Services provides connection load balancing to enable you to spread user connections across all of the instances that are supporting a service. For each service, you can use SRVCTL to define the method you want the listener to use for load balancing by setting the connection load balancing goal, specified with the `-j` option. Connections are classified as `LONG` (such as connection pools and SQL\*FORMS) which tells the listener to use session-based statistics, or `SHORT` which tells the listener to use CPU-based statistics. If the load balancing advisory is enabled, its information is used to balance connections; otherwise, CPU utilization is used to balance connections.

#### Distributed Transaction Processing

Distributed transaction processing applications have unique requirements. To make it easier to use Oracle RAC with global transactions, use SRVCTL and specify the distributed transaction processing option (`-x` `TRUE`) for the service so that all tightly coupled branches of a distributed transaction processing transaction are run on the same instance.

See Also:

"Services and Distributed Transaction Processing in Oracle RAC" for more information about distributed transaction processing in Oracle RAC

#### Subscription to High Availability Events

Oracle RAC uses FAN to notify applications about configuration changes and the current service level that is provided by each instance where the service is enabled. If you are using a client that uses Oracle Streams Advanced Queuing, such as OCI and ODP.NET clients, to receive FAN events, you must enable the service used by that client to access the alert notification queue by using SRVCTL with the `-q` option.

#### Transparent Application Failover Policy

When Oracle Net Services establishes a connection to an instance, the connection remains open until the client closes the connection, the instance is shutdown, or a failure occurs. If you configure transparent application failover (TAF) for the connection, then Oracle Database moves the session to a surviving instance when an outage occurs.

TAF can restart a query after failover has completed but for other types of transactions, such as `INSERT`, `UPDATE`, or `DELETE`, the application must rollback the failed transaction and resubmit the transaction. You must also reexecute any session customizations, in other words, `ALTER SESSION` statements, after failover has occurred. However, with TAF, a connection is not moved during normal processing, even if the workload changes over time.

Services simplify the deployment of TAF. You can define a TAF policy for a service, and all connections using this service will automatically have TAF enabled. This does not require any client-side changes. The TAF setting on a service overrides any TAF setting in the client connection definition.

To define a TAF policy for a service, use SRVCTL as in the following example, where the service name is `tafconn.example.com` and the database name is CRM:

```
$ srvctl modify service -d crm -s tafconn.example.com -P BASIC
   -e SELECT -z 5 -w 120
```

You can also specify a single transparent application failover (TAF) policy for all users of a service by defining the `FAILOVER_METHOD` (`-m` option), `FAILOVER_TYPE` (`-e` option). The TAF policy can also define the number of times that a failed session attempts to reconnect to the service (`-z` option) and how long it should wait between reconnection attempts (`-w` option).

Oracle Call Interface applications with TAF enabled should use FAN high availability events for fast connection failover.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about configuring TAF

### Service Usage in an Oracle RAC Database

A service name can identify multiple database instances, and an instance can belong to multiple services. Services for an Oracle RAC database are used by several database features, as described in the following topics:

- Resource Profile for a Service
- Database Resource Manager Consumer Group Mappings for Services
- Performance Monitoring by Service with AWR
- Parallel Operations and Services

#### Resource Profile for a Service

Resource profiles are automatically created when you define a service. A resource profile describes how Oracle Clusterware should manage the service and which instance the service should failover to if the preferred instance stops. Resource profiles also define service dependencies for the instance and the database. Due to these dependencies, if you stop a database, then the instances and services are automatically stopped in the correct order.

#### Database Resource Manager Consumer Group Mappings for Services

Services are integrated with the Resource Manager, which enables you to restrict the resources that are used by the users who connect to an instance by using a service. The Resource Manager enables you to map a consumer group to a service so that users who connect to an instance using that service are members of the specified consumer group.

#### Performance Monitoring by Service with AWR

The metric data generated by Automatic Workload Repository (AWR) is organized into various groups, such as event, event class, session, service, and tablespace metrics. Typically, you view the AWR data using Oracle Enterprise Manager or AWR reports.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF94183) for more information about generating and viewing AWR reports

#### Parallel Operations and Services

By default, in an Oracle RAC environment, a SQL statement executed in parallel can run across all of the nodes in the cluster. For this cross-node or inter-node parallel execution to perform well, the interconnect in the Oracle RAC environment must be size appropriately because inter-node parallel execution may result in a lot of interconnect traffic. To limit inter-node parallel execution, you can control parallel execution in an Oracle RAC environment using the `PARALLEL_FORCE_LOCAL` initialization parameter. By setting this parameter to `TRUE`, the parallel execution servers can only execute on the same Oracle RAC node where the SQL statement was started.

Services are used to limit the number of instances that participate in a parallel SQL operation. When the default database service is used, the parallel SQL operation can run on all available instances. You can create any number of services, each consisting of one or more instances. When a parallel SQL operation is started, the parallel execution servers are only spawned on instances which offer the specified service used in the initial database connection.

`PARALLEL_INSTANCE_GROUP` is an Oracle RAC parameter that, when used in conjunction with services, lets you restrict parallel query operations to a limited number of instances.To restrict parallel query operations to a limited number of instances, set the `PARALLEL_INSTANCE_GROUP` initialization parameter to the name of a service. This does not affect other parallel operations such as parallel recovery or the processing of `GV$` queries.

#### Oracle Streams and Oracle RAC

Oracle Streams takes advantage of Oracle RAC features in many ways. When Oracle Streams is configured in an Oracle Real Application Clusters (Oracle RAC) environment, each queue table has an owning instance. If the instance that hosts a queue table fails, another instance in the Oracle RAC database becomes the owning instance for the queue table, allowing Oracle Streams to continue operating.

Also, on an Oracle RAC database, a service is created for each buffered queue. This service always runs on the owner instance of the destination queue and follows the ownership of this queue if the ownership switches because of instance startup, instance shutdown, and so on. This service is used by queue-to-queue propagations.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/ap_other.htm#STRMS179)

### Default Service Connections

A special Oracle database service is created by default for your Oracle RAC database. This default service is always available on all instances in an Oracle RAC environment, unless an instance is in restricted mode. You cannot alter this service or its properties. The database also supports the following two internal services:

- `SYS$BACKGROUND` is used by the background processes only
- `SYS$USERS` is the default service for user sessions that are not associated with any application service

Both of these internal services support all of the automatic workload management features. You cannot stop or disable either of these internal services.

Note:

You can explicitly manage only the services that you create. If a feature of the database creates an internal service, you cannot manage it using the information in this chapter.

## Connection Load Balancing

Oracle Net Services provides the ability to balance client connections across the instances in an Oracle RAC configuration. There are two types of load balancing that you can implement: client-side and server-side load balancing. Client-side load balancing balances the connection requests across the listeners. With server-side load balancing, the SCAN listener directs a connection request to the best instance currently providing the service by using the load balancing advisory.

In an Oracle RAC database, client connections should use both types of connection load balancing.

- Client-Side Load Balancing
- Other Client-Side Connection Features
- Server-Side Load Balancing

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for detailed information about both types of load balancing

### Client-Side Load Balancing

Client-side load balancing is defined in your client connection definition (`tnsnames.ora` file, for example) by setting the parameter `LOAD_BALANCE=ON`. When you set this parameter to `ON`, Oracle Database randomly selects an address in the address list, and connects to that node's listener. This balances client connections across the available SCAN listeners in the cluster.

The SCAN listener redirects the connection request to the local listener of the instance that is least loaded and provides the requested service. When the listener receives the connection request, the listener connects the user to an instance that the listener knows provides the requested service. To see what services a listener supports, run the `lsnrctl services` command.

When clients connect using SCAN, Oracle Net automatically load balances client connection requests across the three IP addresses you defined for the SCAN, unless you are using EZConnect.

If you want to use both SCAN and non-SCAN VIPs on the client side, then set the `REMOTE_LISTENER` parameter on the Oracle RAC database to a mix of SCAN VIPs and a list of node VIPs (you must manually update the `REMOTE_LISTENER` parameter to include all the SCAN VIPs and all the node VIPs).

The following is an example of the format you use to add SCAN and node VIP information to the `tnsnames.ora` file for a two-node cluster:

```
LISTENERS_db_unique_name =
  (ADDRESS_LIST =
    (ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP1)(PORT = scan_port_number))
    (ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP2)(PORT = scan_port_number))
    (ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP3)(PORT = scan_port_number))
    (ADDRESS = (PROTOCOL = TCP)(HOST = node_VIP_name1-vip)(PORT = listener_port_number))
    (ADDRESS = (PROTOCOL = TCP)(HOST = node_VIP_name2-vip)(PORT = listener_port_number))
  )
```

Note:

The number of node VIPs you add must correspond to the number of nodes in the cluster.

Run the following SQL\*Plus command:

```
SQL> ALTER SYSTEM SET REMOTE_LISTENER = 'LISTENERS_db_unique_name' SCOPE=BOTH SID='*'
```

Alternatively, you can run the following SQL\*Plus command to update a two-node cluster:

```
SQL> ALTER SYSTEM SET remote_listener = '
(ADDRESS_LIST=
(ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP1)(PORT = scan_port_number))
(ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP2)(PORT = scan_port_number))
(ADDRESS=(PROTOCOL=TCP)(HOST=scan_VIP3)(PORT = scan_port_number))
(ADDRESS=(PROTOCOL=TCP)(HOST=node_VIP_name1-vip)(PORT = listener_port_number))
(ADDRESS=(PROTOCOL=TCP)(HOST=node_VIP_name2-vip)(PORT = listener_port_number)))' 
SCOPE=BOTH SID=*
```

#### Generic Database Clients

With Oracle Database 11g Release 2 (11.2), Oracle Net Services introduces the ability to add the `connect_timeout` and `retry_count` parameters to individual `tnsnames.ora` connection strings.

```
(CONNECT_TIMEOUT=10)(RETRY_COUNT=3)
```

The granularity is seconds. Oracle Net waits for 10 seconds to receive a response, after which it assumes a failure. Oracle Net goes through the address list three times before it returns a failure to the client.

### Other Client-Side Connection Features

In addition to client-side load balancing, Oracle Net Services include connection failover. If an error is returned from the chosen address in the list, Oracle Net Services tries the next address in the list until it is either successful or it has exhausted all addresses in its list. For SCAN, Oracle Net Services tries all three addresses before returning a failure to the client. EZConnect with SCAN includes this connection failover feature.

To increase availability, you can specify a timeout that specifies how long Oracle Net waits for a response from the listener before returning an error. The method of setting this timeout parameter depends on the type of client access.

#### JDBC Clients

You can avoid delays by setting the `oracle.net.ns.SQLnetDef.TCP_CONNTIMEOUT_STR` property, as follows:

```
Properties prop = new Properties ();
prop.put (oracle.net.ns.SQLnetDef.TCP_CONNTIMEOUT_STR,
"" + (1 * 1000)); // 1 second
dbPools[ poolIndex ].setConnectionProperties ( prop );
```

The parameter value is specified in milliseconds. Therefore, it is possible to reduce the timeout to 500Ms if the application retries connecting.

#### Oracle Call Interface Clients

For Oracle Call Interface clients, create a local `sqlnet.ora` file on the client side. Configure the connection timeout in this file by adding the following line:

```
sqlnet.outbound_connect_timeout = 1
```

The granularity of the timeout value for the Oracle Call Interface client is in seconds. The `sqlnet.ora` file affects all connections using this client.

Note:

Do not configure the connection timeout in the `sqlnet.ora` file on the server.

### Server-Side Load Balancing

When you create an Oracle RAC database with DBCA, it automatically:

- Configures and enables server-side load balancing
- Sets the remote listener parameter to the SCAN listener (Note: If you do not use DBCA, you should set the `REMOTE_LISTENER` database parameter to `scan_name``:``scan_port`.)
- Creates a sample client-side load balancing connection definition in the `tnsnames.ora` file on the server

FAN, Fast Connection Failover, and the load balancing advisory depend on an accurate connection load balancing configuration that includes setting the connection load balancing goal for the service. You can use a goal of either `LONG` or `SHORT` for connection load balancing. These goals have the following characteristics:

- LONG: Use the `LONG` connection load balancing method for applications that have long-lived connections. This is typical for connection pools and SQL\*Forms sessions. `LONG` is the default connection load balancing goal. The following is an example of modifying a service, `batchconn`, with the `srvctl` utility to define the connection load balancing goal for long-lived sessions:
	```
	srvctl modify service -d db_unique_name -s batchconn -j LONG
	```
- SHORT: Use the `SHORT` connection load balancing method for applications that have short-lived connections. When using connection pools that are integrated with FAN, set the `CLB_GOAL` to `SHORT`. The following example modifies the service known as `oltpapp`, using SRVCTL to set the connection load balancing goal to `SHORT`:
	```
	srvctl modify service -d db_unique_name -s oltpapp -j SHORT
	```

## Fast Application Notification

This section provides a detailed description of FAN under the following topics:

- Overview of Fast Application Notification
- Application High Availability with Services and FAN
- Managing Unplanned Outages
- Managing Planned Outages
- Fast Application Notification High Availability Events
- Using Fast Application Notification Callouts
	See Also:
	"Oracle Clients That Are Integrated with Fast Application Notification" for more information about specific client environments that you can use with FAN

### Overview of Fast Application Notification

FAN is a notification mechanism that Oracle RAC uses to notify other processes about configuration and service level information that includes service status changes, such as `UP` or `DOWN` events. Applications can respond to FAN events and take immediate action. FAN `UP` and `DOWN` events can apply to instances, services, and nodes.

For cluster configuration changes, the Oracle RAC high availability framework publishes a FAN event immediately when a state change occurs in the cluster. Instead of waiting for the application to poll the database and detect a problem, applications can receive FAN events and react immediately. With FAN, in-flight transactions can be immediately terminated and the client notified when the instance fails.

FAN also publishes load balancing advisory events. Applications can take advantage of the load balancing advisory FAN events to direct work requests to the instance in the cluster that is currently providing the best service quality. You can take advantage of FAN events in the following three ways:

1. Your application can use FAN without programmatic changes if you use an integrated Oracle client. The integrated clients for FAN events include Oracle Database JDBC, Oracle Database ODP.NET, and Oracle Database Oracle Call Interface. This includes applications that use TAF. The integrated Oracle clients must be Oracle Database 10g release 2 (10.2) or later to take advantage of the load balancing advisory FAN events. (See the [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about configuring TAF.)
2. Applications can use FAN programmatically by using the JDBC and Oracle RAC FAN application programming interface (API) or by using callbacks with Oracle Call Interface to subscribe to FAN events and to execute event handling actions upon the receipt of an event.
3. You can implement FAN with server-side callouts on your database tier.

For `DOWN` events, the disruption to the application can be minimized because sessions to the failed instance or node can be terminated. Incomplete transactions can be terminated and the application user is immediately notified. Application users who request connections are directed to available instances only. For `UP` events, when services and instances are started, new connections can be created so that the application can immediately take advantage of the extra resources. Through server-side callouts, you can also use FAN to:

- Log status information
- Page DBAs or to open support tickets when resources fail to start
- Automatically start dependent external applications that must be co-located with a service
- Change resource plans or shut down services when the number of available instances for a policy-managed database decreases, for example, if nodes fail
- Automate the fail back of a service to preferred instances for administrator-managed databases, if needed

FAN events are published using Oracle Notification Service and Oracle Streams Advanced Queuing. The publication mechanisms are automatically configured as part of your Oracle RAC installation.

Connection Manager (CMAN) and Oracle Net Services listeners are integrated with FAN events, enabling the listener and CMAN to immediately de-register services provided by the failed instance and to avoid erroneously sending connection requests to failed instances.

If you specify the connection load balancing goal `CLB_GOAL_SHORT` for the service, then the listener uses the load balancing advisory when the listener balances the connection loads. When load balancing advisory is enabled, the metrics used for the listener are finer grained.

### Application High Availability with Services and FAN

Oracle Database focuses on maintaining service availability. In Oracle RAC, Oracle services are designed to be continuously available with loads shared across one or more instances. The Oracle RAC high availability framework maintains service availability by using Oracle Clusterware and resource profiles.

The Oracle RAC high availability framework monitors the database and its services and sends event notifications using FAN. Oracle Clusterware recovers and balances services according to business rules and the service attributes.

### Managing Unplanned Outages

You can assign services to one or more instances in an administrator-managed Oracle RAC database or to server pools in a policy-managed database. If Oracle RAC detects an outage, then Oracle Clusterware isolates the failed component and recovers the dependent components. For services, if the failed component is an instance, then Oracle Clusterware relocates the service to an available instance in the cluster. FAN events can occur at various levels within the Oracle Database architecture and are published through Oracle Notification Service and Oracle Streams AQ. You can also program notification using FAN callouts.

Note:

Oracle Database does not run Oracle RAC callouts with guaranteed ordering. Callouts are run asynchronously and they are subject to scheduling variabilities.

Notification occurs from a surviving node when the failed node is out of service. The location and number of instances in an Oracle RAC environment that provide a service are transparent to applications. Restart and recovery are automatic, including the restarting of the subsystems, such as the listener and the Oracle Automatic Storage Management (Oracle ASM) processes, not just the database. You can use FAN callouts to report faults to your fault management system and to initiate repair jobs.

### Managing Planned Outages

For repairs, upgrades, and changes that require you to isolate one or more instances or nodes, Oracle RAC provides interfaces that relocate, disable, and enable services to minimize service disruption to application users. When you relocate a service, you indicate the service should run on another instance temporarily. If you disable a service, then the service is stopped on all database instances and is no longer available. Disabled services are not restarted automatically. Once you complete the operation, you can return the service to normal operation or enable the service and then restart it.

Due to dependencies, if you manually shutdown your database, then all of your services for that database automatically stop. If you want your services to automatically start when you manually restart the database, then you must set the management policy of the service to automatic. If you want to shut down only one instance of the database, but not the service, you can use the `srvctl stop instance` command with the `-f` option. When you use the `-f` option with this command, the database services that were running on that instance are failed over to another instance if possible.

See Also:

"Service Management Policy"

### Fast Application Notification High Availability Events

Table 5-1 lists the FAN event types and Table 5-2 describes name-value pairs for the event parameters. The event type is always the first entry and the timestamp is always the last entry, as in the following example:

```
FAN event type: SERVICEMEMBER VERSION=1.0
service=fantest database=ractest instance=rac1host=node01 status=up
reason=FAILURE card=1 timestamp=2010-07-02 22:06:02
```

Table 5-1 FAN Event Types

| Event Types | Notes |
| --- | --- |
| `DATABASE`, `INSTANCE`, `NODE`, `SERVICE`, `SERVICEMEMBER`, `SERVICEMETRICS`, `SRV_PRECONNECT`. | - `DATABASE` and `INSTANCE` types list the database service as `DB_UNIQUE_NAME`. - Events of `SERVICEMETRICS` type are load balancing advisory events. 	See Also: Table 5-4 for more information about load balancing events |

Table 5-2 Event Parameter Name-Value Pairs and Descriptions

| Parameter | Description |
| --- | --- |
| `VERSION` | Version of the event record. Used to identify release changes. |
| `DATABASE` | The unique name of the database supporting the service; matches the initialization parameter value for `DB_UNIQUE_NAME`, which defaults to the value of the `DB_NAME` initialization parameter. |
| `INSTANCE` | The name of the instance that supports the service; matches the `ORACLE_SID` value. |
| `HOST` | The name of the node that supports the service or the node that has stopped; matches the node name known to Cluster Synchronization Services (CSS). |
| `SERVICE` | The service name; matches the name of the service as listed in `DBA_SERVICES`. |
| `STATUS` | Values are `UP`, `DOWN`, `NODEDOWN` (this only applies to the `NODE` event type), `NOT_RESTARTING`, `PRECONN_UP`, `PRECONN_DOWN`, and `UNKNOWN`.  Notes:  - When the node is down, the status is `NODEDOWN`, as opposed to `DOWN` for other event types. - When `STATUS=NODEDOWN` and `REASON=MEMBER_LEAVE`, a node has failed and is no longer part of the cluster. - When `STATUS=NODEDOWN` and `REASON=PUBLIC_NW_DOWN`, the node is up but it is unreachable because the public network is down. |
| `REASON` | `AUTOSTART`, `BOOT`, `DEPENDENCY`, `FAILURE`, `MEMBER_LEAVE`, `PUBLIC_NW_DOWN`, `USER`.  Notes:  - For `DATABASE` and `SERVICE` event types, `REASON=AUTOSTART` if, when the node started, the `AUTO_START` resource attribute was set to `1`, and the resource was offline before the node started - For `DATABASE` and `SERVICE` event types, `REASON=BOOT` if, when the node started, the resource started because it was online before the node started |
| `CARDINALITY` | The number of service members that are currently active; included in all `SERVICEMEMBER UP` events.  Following is an example of `SERVICEMEMBER UP` event:  ``` SERVICEMEMBER VERSION=1.0 service=myServ.company.com database=prod instance=PROD1 host=stru09 status=up reason=USER card=1 timestamp=2010-07-27 14:43:03 ``` |
| `INCARNATION` | For `NODEDOWN` events; the new cluster incarnation.  Following is an example of `NODEDOWN` event:  ``` NODE VERSION=1.0 host=stru09 incarn=175615351 status=down reason=member_leave timestamp=27-Jul-2010 14:49:32 ``` |
| `TIMESTAMP` | The local time zone to use when ordering notification events. |

Some of the FAN event record parameters have values that correspond to values returned by the `SYS_CONTEXT` function using the default namespace `USERENV`, as shown in Table 5-3.

Table 5-3 FAN Parameters and Matching Session Information

| FAN Parameter | Matching Session Information |
| --- | --- |
| `SERVICE` | `sys_context('userenv', 'service_name')` |
| `DATABASE_UNIQUE_NAME` | `sys_context('userenv', 'db_unique_name')` |
| `INSTANCE` | `sys_context('userenv', 'instance_name')` |
| `CLUSTER_NODE_NAME` | `sys_context('userenv', 'server_host')` |

### Using Fast Application Notification Callouts

FAN callouts are server-side executables that Oracle RAC executes immediately when high availability events occur. You can use FAN callouts to automate activities when events occur in a cluster configuration, such as:

- Opening fault tracking tickets
- Sending messages to pagers
- Sending e-mail
- Starting and stopping server-side applications
- Maintaining an uptime log by logging each event as it occurs
- Relocating low-priority services when high priority services come online

To use FAN callouts, place an executable in the `Grid_home` `/racg/usrco` directory on every node that runs Oracle Clusterware. The executable must be able to run stand-alone when called, with optional arguments, from another program. The following is an example file for the `Grid_home` `/racg/usrco/callout.sh` callout:

```
#! /bin/ksh
FAN_LOGFILE= [your path name]/admin/log/'hostname\`_uptime'.log
echo $* "reported="'date' >> $FAN_LOGFILE &
```

The previous example produces output similar to the following:

```
NODE VERSION=1.0 host=sun880-2 incarn=23 status=nodedown reason=
timestamp=08-Oct-2004 04:02:14 reported=Fri Oct 8 04:02:14 PDT 2004
```

The contents of a FAN event record matches the current session of the user logged on to the database, as shown in Table 5-3. The user environment (`USERENV`) information is also available using Oracle Call Interface connection handle and descriptor attributes (using `OCIAttrGet()`). Use this information to take actions on sessions that match the FAN event data.

See Also:

- Table 5-2, "Event Parameter Name-Value Pairs and Descriptions" for information about the callout and event details
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci02bas.htm#LNOCI020) for more information about connection handle and descriptor attributes

#### User Callout Events

All user callout events originate from Oracle Clusterware. If a node goes down, or a resource (such as a VIP or a database) changes state or properties, then Oracle Clusterware sends out an Oracle Notification Service event to that effect. This event must always be pushed to at least one node in the cluster, and the best way to ensure that is to make the user callouts listen to Oracle Notification Service events from within the agent of the Oracle Notification Service resource.

If the Oracle Notification Service resource is down on a particular node, then the events on that node are lost, and so user callouts are not issued. The Oracle Notification Service event is read from within the agent of the Oracle Notification Service resource, is translated, and is posted to user callouts.

In general, events are only posted to user callouts on the node from which the event originated. For example, if the database on `node1` goes down, then the callout is posted to `node1`, only. The only exceptions to this are node down and VIP down events—these events are posted to all nodes, regardless of from where they originated.

Note:

In Oracle Database 11g release 2 (11.2.0.2), the two attributes service and database for event types of DATABASE or INSTANCE do not include the database domain name.

## Load Balancing Advisory

This section describes the load balancing advisory under the following topics:

- Overview of the Load Balancing Advisory
- Configuring Your Environment to Use the Load Balancing Advisory
- Load Balancing Advisory FAN Events
- Monitoring Load Balancing Advisory FAN Events

### Overview of the Load Balancing Advisory

Load balancing distributes work across all of the available Oracle RAC database instances. Oracle recommends that applications use persistent connections that span the instances that offer a particular service, such as when using connection pools. When using persistent connections, connections are created infrequently and exist for a long duration. Work comes into the system with high frequency, borrows these connections, and exists for a relatively short duration. The load balancing advisory provides advice about how to direct incoming work to the instances that provide the optimal quality of service for that work. This minimizes the need to relocate the work later.

By using the Load Balancing Advisory or runtime connection load balancing goals, feedback is built in to the system. Work is routed to provide the best service times globally, and routing responds gracefully to changing system conditions. In a steady state, the system approaches equilibrium with improved throughput across all of the Oracle RAC instances.

Standard architectures that can use the load balancing advisory include connection load balancing, transaction processing monitors, application servers, connection concentrators, hardware and software load balancers, job schedulers, batch schedulers, and message queuing systems. All of these applications can allocate work.

The load balancing advisory is deployed with key Oracle clients, such as a listener, the JDBC universal connection pool, and the ODP.NET Connection Pool. Third-party applications can also subscribe to load balancing advisory events by using JDBC and Oracle RAC FAN API or by using callbacks with Oracle Call Interface.

### Configuring Your Environment to Use the Load Balancing Advisory

You can configure your environment to use the load balancing advisory by defining service-level goals for each service for which you want to enable load balancing. Configuring a service-level goal enables the load balancing advisory and the publishing of FAN load balancing events for that service.

There are two types of service-level goals for runtime connection load balancing:

- `SERVICE_TIME`: Attempts to direct work requests to instances according to response time. Load balancing advisory data is based on elapsed time for work done in the service plus available bandwidth to the service. An example for the use of `SERVICE_TIME` is for workloads such as internet shopping where the rate of demand changes. The following example shows how to set the goal to `SERVICE_TIME` for connections using the `online` service:
	```
	srvctl modify service -d db_unique_name -s online -B SERVICE_TIME -j SHORT
	```
- `THROUGHPUT`: Attempts to direct work requests according to throughput. The load balancing advisory is based on the rate that work is completed in the service plus available bandwidth to the service. An example for the use of `THROUGHPUT` is for workloads such as batch processes, where the next job starts when the last job completes. The following example shows how to set the goal to `THROUGHPUT` for connections using the `sjob` service:
	```
	srvctl modify service -d db_unique_name -s sjob -B THROUGHPUT -j LONG
	```

Setting the runtime connection load balancing goal to `NONE` disables load balancing for the service. You can see the goal settings for a service in the data dictionary by querying the `DBA_SERVICES`, `V$SERVICES`, and `V$ACTIVE_SERVICES` views. You can also review the load balancing settings for a service using Oracle Enterprise Manager.

See Also:

- "Administering Services" for more information about administering services and adding goals to services
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/configwlm.htm#TDPRC307) for more information about managing services using Oracle Enterprise Manager

### Load Balancing Advisory FAN Events

The load balancing advisory FAN events provide metrics for load balancing algorithms. The easiest way to take advantage of these events is to use the runtime connection load balancing feature of an Oracle integrated client such as JDBC, ODP.NET, or Oracle Call Interface. Other client applications can take advantage of FAN programatically by using the Oracle Notification Service application programming interface (ONS API) to subscribe to FAN events and execute event-handling actions upon receipt. Table 5-4 describes the load balancing advisory FAN event parameters.

Table 5-4 Load Balancing Advisory FAN Events

| Parameter | Description |
| --- | --- |
| `VERSION` | Version of the event record. Used to identify release changes. |
| `EVENT_TYPE` | A load balancing advisory event is always of the `SERVICEMETRICS` event type. |
| `SERVICE` | The service name; matches the value of `NAME` in `DBA_SERVICES`. |
| `DATABASE_UNIQUE_NAME` | The unique database supporting the service; matches the initialization parameter value for `DB_UNIQUE_NAME`, which defaults to the value of the initialization parameter `DB_NAME`. |
| `INSTANCE` | The name of the instance that supports the service; matches the `ORACLE_SID` value. |
| `PERCENT` | The percentage of work requests to send to this database instance. |
| `FLAG` | Indication of the service quality relative to the service goal. Valid values are `GOOD`, `VIOLATING`, `NO DATA`, and `BLOCKED`. |
| `TIMESTAMP` | The local time zone to use when ordering notification events. |

See Also:

[Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for more information about the Oracle RAC FAN API

### Monitoring Load Balancing Advisory FAN Events

You can use the following query against the internal queue table for load balancing advisory FAN events to monitor load balancing advisory events generated for an instance:

```
SET PAGES 60 COLSEP '|' LINES 132 NUM 8 VERIFY OFF FEEDBACK OFF
COLUMN user_data HEADING "AQ Service Metrics" FORMAT A60 WRAP
BREAK ON service_name SKIP 1
SELECT
 TO_CHAR(enq_time, 'HH:MI:SS') Enq_time, user_data
 FROM sys.sys$service_metrics_tab
 ORDER BY 1 ;
```

The results of this query contain rows similar to the following:

```
02:56:05|SYS$RLBTYP('hr', 'VERSION=1.0 database=sales service=hr { {in
        |stance=sales_4 percent=38 flag=GOOD aff=TRUE}{instance=sales_1
        | percent=62 flag=GOOD aff=TRUE} } timestamp=2010-07-16 07:56
        |:05')
```

## Oracle Clients That Are Integrated with Fast Application Notification

Oracle has integrated FAN with many of the common client application environments that are used to connect to Oracle RAC databases. Therefore, the easiest way to use FAN is to use an integrated Oracle Client.

The following sections discuss how FAN is integrated with Oracle Clients and how to enable FAN events for the several specific client development environments:

- Overview of Oracle Integrated Clients and FAN
- Enabling JDBC Clients for Fast Connection Failover
- Enabling JDBC Clients for Runtime Connection Load Balancing
- Enabling Oracle Call Interface Clients for Fast Connection Failover
- Enabling Oracle Call Interface Clients for Runtime Connection Load Balancing
- Enabling ODP.NET Clients to Receive FAN High Availability Events
- Enabling ODP.NET Clients to Receive FAN Load Balancing Advisory Events

### Overview of Oracle Integrated Clients and FAN

The overall goal when using FAN is to enable applications to consistently obtain connections to available instances that provide the best service. The Oracle integrated clients you can use are Oracle Call Interface Session Pools, CMAN session pools, and JDBC and ODP.NET connection pools. The Fast Connection Failover (FCF) feature is a FAN client implemented through a connection pool.

Due to the integration with FAN, Oracle integrated clients are more aware of the current status of an Oracle RAC cluster. This prevents client connections from waiting or trying to connect to an instance that is no longer available. When instances start, Oracle RAC uses FAN to notify the connection pool so that the connection pool can create connections to the recently started instance and take advantage of the additional resources that this instance provides.

Oracle connection pools that are integrated with FAN can:

- Balance connections across all of the Oracle RAC instances when a service starts; this is preferable to directing the sessions that are defined for the connection pool to the first Oracle RAC instance that supports the service
- Remove terminated connections immediately when a service is declared `DOWN` at an instance, and immediately when nodes are declared `DOWN`
- Report errors to clients immediately when Oracle Database detects the `NOT RESTARTING` state, instead of making the client wait while the service repeatedly attempts to restart
- Balance work requests at runtime using load balancing advisory events

The use of connection pools and FAN requires that you have properly configured database connection load balancing across all of the instances that provide the services used by the connection pool. Oracle recommends that you configure both client-side and server-side load balancing with Oracle Net Services. If you use DBCA to create your database, then both client-side and server-side load balancing are configured by default.

See Also:

"Connection Load Balancing"

### Enabling JDBC Clients for Fast Connection Failover

Enabling Fast Connection Failover (FCF) for the Oracle JDBC Universal Connection Pool (UCP) enables the use of FAN high availability and load balancing advisory events. To use FAN, your application can use the JDBC development environment for either thick or thin JDBC clients. The Java Database Connectivity Oracle Call Interface (JDBC/OCI) driver connection pooling functionality is part of the JDBC client. This functionality is provided by the `OracleOCIConnectionPool` class.

The UCP is integrated to take advantage of Load Balancing Advisory information. Oracle introduced the Universal Connection Pool for JDBC in Oracle Database 11g release 11.1.0.7.0. Consequently, Oracle deprecated the existing JDBC connection pool, the Implicit Connection Cache, that was introduced in Oracle Database 10g release 1, for use with Oracle RAC databases. You can use the UCP with Oracle Database 10g or Oracle Database 11g.

To enable FCF for the JDBC client, set the `fastConnectionFailoverEnabled` property of the `OracleDataSource` class in the `oracle.jdbc.pool` package before making the first `getConnection()` request. When you enable FCF for the JDBC client, the failover property applies to every connection in the connection pool. Enabling FCF with JDBC Thin Driver (Thin driver) or JDBC/OCI clients enables the connection pool to receive and react to all FAN events.

JDBC application developers can now programatically integrate with FAN by using a set of APIs introduced in Oracle Database 11g release 2 (11.2). The Oracle RAC FAN APIs enable application code to receive and respond to FAN event notifications sent by Oracle RAC in the following ways:

- Listening for Oracle RAC service down, service up, and node down events
- Listening for load balancing advisory events and responding to them

See Also:

- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for more information about using APIs, configuring the JDBC universal connection pool, and Oracle Notification Service
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for more information about configuring JDBC clients

#### Oracle Notification Service for JDBC Clients

FCF relies on Oracle Notification Service to propagate database events between the connection pool and the Oracle RAC database. At runtime, the connection pool must be able to setup an Oracle Notification Service environment. Oracle Notification Service (`ons.jar`) is included as part of the Oracle Client software. Oracle Notification Service can be configured using either remote configuration or client-side Oracle Notification Service daemon configuration. Remote Oracle Notification Service subscription offers the following advantages:

- Support for an All Java mid-tier software
- An Oracle Notification Service daemon is not necessary on the client system, so you do not have to manage this process
- Simple configuration by way of a `DataSource` property

#### Configuring FCF for JDBC/OCI and JDBC Thin Driver Clients

You can enable FCF for Oracle's Implicit Connection Cache or UCP. Oracle recommends using the UCP for Java. The Implicit Connection Cache is deprecated.

This procedure explains how to enable FCF for JDBC. For JDBC/OCI clients, if you enable FCF, do not enable TAF, either on the client or for the service. To enable FCF, you must first enable the UCP, as described in the following procedure:

1. Create the connection pool and set `FastConnectionFailoverEnabled`.
	The following example creates a connection pool and enables FCF. The `ucp.jar` library must be included in the classpath of an application to use this example.
	```
	PoolDataSource pds = PoolDataSourceFactory.getPoolDataSource();
	pds.setFastConnectionFailoverEnabled(true);
	```
2. Determine the ports to use for Oracle Notification Service remote subscriptions.
	Use the following command to view the Oracle Notification Service configuration on each node that is running Oracle Clusterware as in the following example:
	```
	srvctl config nodeapps -s
	```
	The output of this command lists the local and remote ports configured for Oracle Notification Service.
	Note:
	Oracle Notification Service configuration should have been automatically completed during the Oracle Clusterware installation.
3. Add Oracle Notification Service daemons to remote nodes for upgraded Oracle9i databases.
	The information in the Oracle Cluster Registry (OCR) for Oracle Notification Service daemons is automatically configured for Oracle Database 10g and higher. If you are upgrading from an Oracle9i version of the database, then add Oracle Notification Service daemons to remote nodes (nodes outside the cluster), with the following command:
	```
	srvctl modify nodeapps -t host_port_list
	```
4. Configure the remote Oracle Notification Service subscription.
	When using the Universal Connection Pool, an application calls `setONSConfiguration` for an `OracleDataSource` instance and specifies the nodes and port numbers to use. The port numbers used for each node are the same as the remote port displayed for each node in Step 2, as shown in the following example. The `ons.jar` library must be included in the classpath of an application to use this example.
	```
	pds.setONSConfiguration("nodes=racnode1:6200,racnode2:6200");
	```
	Applications that use remote Oracle Notification Service configuration must set the `oracle.ons.oraclehome` system property to the location of `ORACLE_HOME` before starting the application, for example:
	```
	java -Doracle.ons.oraclehome=$ORACLE_HOME ...
	```
5. Configure the connection URL.
	A connection factory's connection URL must use the service name syntax when using FCF. The service name is used to map the connection pool to the service. The following example demonstrates configuring the connection URL:
	```
	pds.setConnectionFactoryClassName("oracle.jdbc.pool.OracleDataSource");
	pds.setURL("jdbc:oracle:thin@//SCAN_name:1521/service_name");......
	```

See Also:

- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for more information about JDBC
- [Oracle Universal Connection Pool for JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e12265/rac.htm#JJUCP08100) for more information about configuring FCF

### Enabling JDBC Clients for Runtime Connection Load Balancing

UCP JDBC connection pools leverage the load balancing functionality provided by an Oracle RAC database. Runtime connection load balancing requires the use of an Oracle JDBC driver and an Oracle RAC database.

Runtime connection load balancing requires that FCF is enabled and configured properly. See "Configuring FCF for JDBC/OCI and JDBC Thin Driver Clients". In addition, the Oracle RAC load balancing advisory must be configured with service-level goals for each service used by the connection pool. The connection load balancing goal should be set to `SHORT`, for example:

```
srvctl modify service -d db_unique_name -s service_name -B SERVICE_TIME -j SHORT
```

See Also:

[Oracle Universal Connection Pool for JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e12265/rac.htm#JJUCP08100) for more information about configuring runtime connection load balancing for UCP JDBC connection pools

### Enabling Oracle Call Interface Clients for Fast Connection Failover

Oracle Call Interface (OCI) clients can enable FCF by registering to receive notifications for Oracle RAC high availability FAN events and responding when events occur. Using FCF improves the session failover response time in OCI applications and also removes connections to nonfunctioning instances from connection and session pools. FCF can be used in OCI applications that also use TAF, connection pools, or session pools.

To use FCF, you must use a service with the load balancing advisory goal and the connection load balancing goal configured. The service metrics received from the Oracle RAC load balancing advisory through FAN events for the service are automatically placed in the Oracle Streams AQ queue table, `ALERT_QUEUE`. Client applications can register callbacks that are used whenever an event occurs. This reduces the time that it takes to detect a connection failure.

During `DOWN` event processing, OCI:

- Terminates affected connections at the client and returns an error
- Removes connections from the OCI connection pool and the OCI session pool—the session pool maps each session to a physical connection in the connection pool, and there can be multiple sessions for each connection
- Fails over the connection if you have configured TAF. If TAF is not configured, then the client only receives an error if the instance it is connected to fails.

If your application is using TAF, then you must enable the TAF properties for the service using SRVCTL or Oracle Enterprise Manager. Configure your OCI client applications to connect to an Oracle RAC database using the configured service.

Note:

Oracle Call Interface does not manage `UP` events.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about configuring TAF

Configuring FCF for OCI Clients

OCI applications must connect to an Oracle RAC instance to enable HA event notification. Furthermore, these applications must perform the following steps to configure FCF for an OCI client:

1. Configure the service for your OCI connection pool to enable connection load balancing and runtime connection load balancing. Also configure the service to have Advanced Queuing notifications enabled, as shown in the following example:
	```
	$ srvctl modify service -d crm -s ociapp.example.com -q TRUE 
	   -B THROUGHPUT -j LONG
	```
2. Set the context of the environment for OCI calls on the client to enable subscriptions by using the `OCIEnvCreate()` call, setting the `MODE` parameter value to `OCI_EVENTS`, as follows:
	```
	(void) OCIEnvCreate(&myenvhp, OCI_EVENTS|OCI_OBJECT, ...);
	```
3. Link the application with a thread library.
4. After linking with the thread library, the applications can register a callback that is invoked whenever a FAN event occurs.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for more information about Oracle Call Interface

### Enabling Oracle Call Interface Clients for Runtime Connection Load Balancing

As of Oracle Database 11g release 2 (11.2), OCI session pooling enables multiple threads of an application to use a dynamically managed set of pre-created database sessions. In connection pooling, the pool element is a connection, but in session pooling, the pool element is a session. Oracle Database continually reuses the sessions in the session pool to form nearly permanent channels to the instances, thus saving the overhead of creating and closing sessions every time applications need them.

Runtime connection load balancing is enabled by default in a release 11.1 or higher client talking to a server of 10.2 or higher. For Oracle RAC environments, session pools use service metrics received from the Oracle RAC load balancing advisory <sup>Foot 1</sup> through Fast Application Notification (FAN) events to balance application session requests. The work requests coming into the session pool can be distributed across the instances of Oracle RAC offering a service, using the current service performance.

Runtime connection load balancing is basically routing work requests to sessions in a session pool that best serve the work. It comes into effect when selecting a session from an existing session pool and thus is a very frequent activity. For session pools that support services at one instance only, the first available session in the pool is adequate. When the pool supports services that span multiple instances, there is a need to distribute the work requests across instances so that the instances that are providing better service or have greater capacity get more requests.

Connect time load balancing occurs when a session is first created by the application. It is necessary that the sessions that are part of the pool be well distributed across Oracle RAC instances, at the time they are first created. This ensures that sessions on each of the instances get a chance to execute work.

Configuring OCI Clients to Receive Load Balancing Advisory FAN Events

For Oracle RAC environments, session pools use service metrics received from the Oracle RAC load balancing advisory through Fast Application Notification (FAN) events to balance application session requests. To enable your application to receive the service metrics based on the service time, ensure you have met the following conditions:

1. Link the application with the threads library.
2. Create the OCI environment in `OCI_EVENTS` and `OCI_THREADED` mode.
3. Configure the load balancing advisory goal (`-B` option) and connection load balancing goal (`-j` option) for a service that is used by the session pool, as shown in the following example:
	```
	srvctl modify service -d crm -s ociapps -B SERVICE_TIME -j SHORT
	```

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for more information about Oracle Call Interface

### Enabling ODP.NET Clients to Receive FAN High Availability Events

ODP.NET connection pools can subscribe to notifications that indicate when nodes, services, and service members are down. After a `DOWN` event, Oracle Database cleans up sessions in the connection pool that go to the instance and ODP.NET proactively removes connections that are no longer valid. ODP.NET establishes additional connections to existing Oracle RAC instances if the removal of invalid connections reduces the total number of connections to below the value for the `MIN_POOL_SIZE` parameter.

Perform the following steps to enable FAN for ODP.NET clients:

1. Enable Advanced Queuing notifications for a service by using SRVCTL as shown in the following example:
	```
	srvctl modify service -d crm -s odpnet.example.com -q TRUE
	```
2. Grant permissions on the internal event queue table by executing the following command for the users that will be connecting by way of the ODP.NET application, where `user_name` is the database user name:
	```
	EXECUTE DBMS_AQADM.GRANT_QUEUE_PRIVILEGE('DEQUEUE','SYS.SYS$SERVICE_METR
	ICS', user_name);
	```
3. Enable Fast Connection Failover for ODP.NET connection pools by subscribing to FAN high availability events. To enable FCF, include " `HA Events=true` " and " `pooling=true` " (the default value) in the connection string, as shown in the following example where `user_name` is the name of the database user and `password` is the password for that user:
	```
	con.ConnectionString =
	   "User Id=user_name;Password=password;Data Source=odpnet;" +
	   "Min Pool Size=10;Connection Lifetime=120;Connection Timeout=60;" +
	   "HA Events=true;Incr Pool Size=5;Decr Pool Size=2";
	```
	See Also:
	[Oracle Data Provider for.NET Developer's Guide](https://docs.oracle.com/cd/E11882_01/win.112/e23174/toc.htm) for more information about using FAN events in ODP.NET applications

### Enabling ODP.NET Clients to Receive FAN Load Balancing Advisory Events

Use the following procedures to enable ODP.NET clients or applications to receive FAN load balancing advisory events:

1. Enable Advanced Queuing notifications by using SRVCTL, and set the connection load balancing goal as shown in the following example:
	```
	srvctl modify service -d crm -s odpapp.example.com -q TRUE -j LONG
	```
2. Ensure Oracle Net Services is configured for connection load balancing.
3. Grant permissions on the internal event queue table by executing the following command for the users that will be connecting by way of the ODP.NET application, where `user_name` is the name of the database user:
	```
	EXECUTE DBMS_AQADM.GRANT_QUEUE_PRIVILEGE('DEQUEUE','SYS.SYS$SERVICE_METR
	ICS', user_name);
	```
4. To take advantage of load balancing events with ODP.NET connection pools, set the load balancing attribute in the ConnectionString to `TRUE` (the default is `FALSE`). You can do this at connect time. This only works if you are using connection pools, or when the pooling attribute is set to `TRUE` which is the default.
	The following example demonstrates how to configure the ConnectionString to enable load balancing, where `user_name` is the name of the user and `password` is the password:
	```
	con.ConnectionString =
	  "User Id=user_name;Password=password;Data Source=odpapp;" +
	  "Min Pool Size=10;Connection Lifetime=120;Connection Timeout=60;" +
	  "Load Balancing=true;Incr Pool Size=5;Decr Pool Size=2";
	```

Note:

ODP.NET does not support connection redistribution when a node starts (UP events). However, if you have enabled failover on the server-side, then ODP.NET can migrate connections to newly available instances.

See Also:

- [Oracle Data Provider for.NET Developer's Guide](https://docs.oracle.com/cd/E11882_01/win.112/e23174/toc.htm) for more information about ODP. NET
- ["srvctl modify service"](srvctladmin.md) in [Appendix A, "Server Control Utility Reference"](srvctladmin.md).

## Services and Distributed Transaction Processing in Oracle RAC

The X/Open Distributed Transaction Processing (DTP) architecture defines a standard architecture or interface that enables multiple application programs (APs) to share resources provided by multiple, and possibly different, resource managers (RMs). It coordinates the work between APs and RMs into global transactions.

The following sections discuss how Oracle RAC supports XA transactions and DTP processing:

- Overview of XA Transactions and DTP Services
- Benefits of DTP Services for XA Transactions
- Using DTP Services with Oracle RAC
- Configuring DTP Services
- Relocating DTP Services in Administrator-Managed Databases

### Overview of XA Transactions and DTP Services

An XA transaction can span Oracle RAC instances by default, allowing any application that uses the Oracle XA library to take full advantage of the Oracle RAC environment to enhance the availability and scalability of the application.

GTXn background processes support global (XA) transactions in an Oracle RAC environment. The `GLOBAL_TXN_PROCESSES` initialization parameter, which is set to `1` by default, specifies the initial number of GTXn background processes for each Oracle RAC instance. Use the default value for this parameter clusterwide to allow distributed transactions to span multiple Oracle RAC instances. Using the default value allows the units of work performed across these Oracle RAC instances to share resources and act as a single transaction (that is, the units of work are tightly coupled). It also allows 2PC requests to be sent to any node in the cluster.

Before Oracle RAC 11g release 1 (11.1), the way to achieve tight coupling in Oracle RAC was to use Distributed Transaction Processing (DTP) services, that is, services whose cardinality (one) ensured that all tightly-coupled branches landed on the same instance—regardless of whether load balancing was enabled. Tightly coupled XA transactions no longer require the special type of singleton services to be deployed on Oracle RAC databases if the XA application does not join or resume XA transaction branches. XA transactions are transparently supported on Oracle RAC databases with any type of service configuration.

Note:

Oracle RAC 11g release 1 (11.1) and later does not require a DTP service but performance might be improved if you use a DTP service, as described in "Benefits of DTP Services for XA Transactions".

An external transaction manager, such as Oracle Services for Microsoft Transaction Server (OraMTS), coordinates DTP/XA transactions. However, an internal Oracle transaction manager coordinates distributed SQL transactions. Both DTP/XA and distributed SQL transactions must use the DTP service in Oracle RAC.

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_xa.htm#ADFNS1505) for complete information about using Oracle XA with Oracle RAC
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams099.htm#REFRN10291) for information about the `GLOBAL_TXN_PROCESSES` initialization parameter

### Benefits of DTP Services for XA Transactions

To provide improved application performance with distributed transaction processing in Oracle RAC, you may want to take advantage of DTP services. Using DTP services, you can direct all branches of a distributed transaction to a single instance in the cluster. To load balance across the cluster, it is better to have several groups of smaller application servers with each group directing its transactions to a single service, or set of services, than to have one or two larger application servers.

In addition, connection pools at the application server tier that load balance across multiple connections to an Oracle RAC database can use this method to ensure that all tightly-coupled branches of a global distributed transaction run on only one Oracle RAC instance. This is also true in distributed transaction environments using protocols such as X/Open Distributed Transaction Processing (DTP) or the Microsoft Distributed Transaction Coordinator (DTC).

To enhance the performance of distributed transactions, you can use services to manage DTP environments. By defining the DTP property of a service, the service is guaranteed to run on one instance at a time in an Oracle RAC database. All global distributed transactions performed through the DTP service are ensured to have their tightly-coupled branches running on a single Oracle RAC instance. This has the following benefits:

- The changes are available locally within one Oracle RAC instance when tightly coupled branches need information about changes made by each other
- Relocation and failover of services are fully supported for DTP
- By using more DTP services than there are Oracle RAC instances, Oracle Database can balance the load by services across all of the Oracle RAC database instances

### Using DTP Services with Oracle RAC

To leverage all of the instances in a cluster, create one or more DTP services for each Oracle RAC instance that hosts distributed transactions. Choose one DTP service for one distributed transaction. Choose different DTP services for different distributed transactions to balance the workload among the Oracle RAC database instances. Because all of the branches of a distributed transaction are on one instance, you can leverage all of the instances to balance the load of many DTP transactions through multiple singleton services, thereby maximizing application throughput.

If you add or delete nodes from your cluster database, then you may have to identify and relocate services that you are using for DTP transactions to ensure that you maintain optimum performance levels.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) for more information about transaction branch management in Oracle RAC

### Configuring DTP Services

To create DTP services for distributed transaction processing, perform the following steps:

1. Create a singleton service using Oracle Enterprise Manager or SRVCTL.
	For an administrator-managed database, define only one instance as the preferred instance. You can have as many available instances as you want, for example:
	```
	srvctl add service -d crm -s xa_01.example.com -r RAC01 -a RAC02,RAC03
	```
	For a policy-managed database, specify the server pool to use, and set the cardinality of the service to `SINGLETON`, for example:
	```
	srvctl add service -d crm -s xa_01.example.com -g dtp_pool -c SINGLETON
	```
2. Set the DTP option (`-x`) for the service to `TRUE` (the default value is `FALSE)`. You can use Oracle Enterprise Manager or SRVCTL to modify the DTP property of the singleton service. The following example shows how to modify the `xa_01.example.com` service using SRVCTL:
	```
	srvctl modify service -d crm -s xa_01.example.com -x TRUE
	```

### Relocating DTP Services in Administrator-Managed Databases

If the instance that provides a DTP service, for example `XA_01`, fails, then the singleton service fails over to an available instance, such as `RAC02` or `RAC03`.

If services migrate to other instances, then you might have to force the relocation of the service back to the preferred instance after it is restarted to evenly re-balance the load on all of the available hardware. You can use data from the `GV$ACTIVE_SERVICES` view to determine whether you need to relocate the STP service.

## Administering Services

You can create and administer services with Oracle Enterprise Manager and the SRVCTL utility. The following sections describe how to perform service-related tasks using these tools:

- Overview of Service Administration
- Administering Services with Oracle Enterprise Manager
- Administering Services with SRVCTL

Note:

You can also use the DBMS\_SERVICE package to create or modify services and service attributes, but SRVCTL or Oracle Enterprise Manager will override any settings made using this package. The DBMS\_SERVICE package is not recommended for use with services used by an Oracle RAC database.

### Overview of Service Administration

When you create and administer services, you are dividing the work that your database performs into manageable units. The goal of using services is to achieve optimal utilization of your database infrastructure. You can create and deploy services based on business requirements. Oracle Database can measure the performance for each service. Using the `DBMS_MONITOR` package, you can define both the application modules within a service and the individual actions for a module and monitor thresholds for these actions, enabling you to manage workloads to deliver capacity on demand.

To create a service, you can use either Oracle Enterprise Manager, or SRVCTL. When you create new services for your database, you should define the automatic workload management characteristics for each service, as described in "Service Characteristics".

See Also:

- [Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/wlm_strats.htm#APQOS144) if you are using Oracle Database QoS Management with your Oracle cluster for details on how to configure the database services
- "Oracle Clients That Are Integrated with Fast Application Notification" for more details

In addition to creating services, you can:

- Delete a service. You can delete services that you created. However, you cannot delete or modify the properties of the default database service that Oracle Database created.
- Check the status of a service. A service can be assigned different roles among the available instances. In a complex database with many services, you may not remember the details of every service. Therefore, you may have to check the status on an instance or service basis. For example, you may have to know the status of a service for a particular instance before you make modifications to that instance or to the Oracle home from which it runs.
- Start or stop a service for a database or an instance. A service must be started before it can be used for client connections to that instance. If you shut down your database, for example, by running the SRVCTL command `srvctl stop database -d` `db_unique_name` where `db_unique_name` is the name of the database you want to stop, then Oracle Database stops all services to that database. Depending on the service management policy, you may have to manually restart the services when you start the database.
	Note:
	If Oracle Database QoS Management is enabled for the Oracle RAC database, then the services are automatically restarted after they are stopped.
- Map a service to a consumer group. Oracle Database can automatically map services to Resource Manager Consumer groups to limit the amount of resources that services can use in an instance. You must create the consumer group and then map the service to the consumer group.
	See Also:
	[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_resmgr.htm#ARPLS050) for information about the `DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING_PRI` procedure
- Enable or disable a service for a database or an instance. By default, Oracle Clusterware attempts to restart a service automatically after failures. You can prevent this behavior by disabling a service. Disabling a service is useful when you must perform database or instance maintenance, for example, if you are performing an upgrade and you want to prevent connection requests.
- Relocate a service to a different instance. You can move a service from one instance to another instance to re-balance workloads, for example, after adding or deleting cluster nodes.

Notes:

- When you use services, do not set a value for the `SERVICE_NAMES` parameter; Oracle Database controls the setting for this parameter for the services that you create and for the default database service. The service features that this chapter describes are not directly related to the features that Oracle Database provides when you set `SERVICE_NAMES`. In addition, setting a value for this parameter may override some benefits of using services.
- If you specify a service using the `DISPATCHERS` initialization parameter, it overrides any service in the `SERVICE_NAMES` parameter, and cannot be managed. (For example, stopping the service with a SRVCTL command does not stop users connecting with the service.)

### Administering Services with Oracle Enterprise Manager

The Cluster Managed Database Services page is the master page for beginning all tasks related to services. To access this page, go to the Cluster Database Availability page, then click Cluster Managed Database Services in the Services section. You can use this page and drill down from this page to perform the following tasks:

- View a list of services for the cluster
- View the instances on which each service is currently running
- View the status for each service
- Create or edit a service
- Start or stop a service
- Enable or disable a service
- Perform instance-level tasks for a service
- Delete a service

Note:

You must have `SYSDBA` credentials to access a cluster database. Cluster Managed Database Services does not permit you to connect as anything other than `SYSDBA`.

See Also:

- Oracle Enterprise Manager online help for more information about administering services with Oracle Enterprise Manager
- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/configwlm.htm#TDPRC307) for more information about using Oracle Enterprise Manager to manage services

### Administering Services with SRVCTL

When you create a service by using SRVCTL, you must start the service with a separate SRVCTL command. However, you may later have to manually stop or restart the service. You may also have to disable the service to prevent automatic restarts, to manually relocate the service, or obtain status information about the service. The following sections explain how to use SRVCTL to perform the following administrative tasks:

- Creating Services with SRVCTL
- Starting and Stopping Services with SRVCTL
- Enabling and Disabling Services with SRVCTL
- Relocating Services with SRVCTL
- Obtaining the Statuses of Services with SRVCTL
- Obtaining the Configuration of Services with SRVCTL

See Also:

[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for more information about SRVCTL commands that you can use to manage services, including descriptions of options

#### Creating Services with SRVCTL

To create a service with SRVCTL, enter a command from the command line using the following syntax:

```
srvctl add service -d db_unique_name
 -s service_name
 -t edition_name
{-r preferred_list
 [-a available_list
]} | {-g server_pool
[-c {UNIFORM | SINGLETON}] [-k net_number]}
[-P {BASIC | NONE}] [-l {[PRIMARY] | [PHYSICAL_STANDBY] | [LOGICAL_STANDBY] |
[SNAPSHOT_STANDBY]}] [-y {AUTOMATIC | MANUAL}] [-q {TRUE | FALSE}]
[-x {TRUE | FALSE}] [-j {SHORT | LONG}] [-B {NONE | SERVICE_TIME | THROUGHPUT}]
 [-e {NONE |SESSION | SELECT}] [-m {NONE | BASIC}] [-z failover_retries]
 [-w failover_delay]
```

Note:

The `service_name` initialization parameter has a 4 kilobyte (KB) limit for its value. Therefore, the total length of the names of all services assigned to an instance cannot exceed 4 KB.

#### Starting and Stopping Services with SRVCTL

For applications to connect using a server, the service must be started. If you stop a service, then it is temporarily unavailable, but is still subject to automatic restart and failover.

Enter the following SRVCTL syntax from the command line to stop or start a service:

```
srvctl start service -d database_unique_name [-s service_name_list
] [-i inst_name
]
[-o start_options
]
```
```
srvctl stop service -d database_unique_name -s service_name_list
 [-i inst_name
]
[-o start_options
]
```

#### Enabling and Disabling Services with SRVCTL

If you disable a service, then Oracle Clusterware does not consider the service for automatic startup, failover, or restart. You might disable a service when performing application maintenance, to ensure the service is not accidentally restarted by Oracle Clusterware until your maintenance operations are complete. To make the service available for normal operation again, you enable the service.

Use the following SRVCTL syntax from the command line to enable and disable services:

```
srvctl enable service -d database_unique_name
 -s service_name_list
 [-i inst_name
]
```
```
srvctl disable service -d database_unique_name
 -s service_name_list
 [-i inst_name
]
```

#### Relocating Services with SRVCTL

Run the `srvctl relocate service` command from the command line to relocate a service. You might use this command when a service has failed over to an available instance, but you want to move it back to the preferred instance after that instance is restarted.

The following command relocates the `crm` service from instance `apps1` to instance `apps3`:

```
srvctl relocate service -d apps -s crm -i apps1 -t apps3
```

#### Obtaining the Statuses of Services with SRVCTL

Run the `srvctl status service` command from the command line to obtain the status of a service. For example, the following command returns the status of the services that are running on the `apps` database:

```
srvctl status service -d apps

Service erp is running on nodes: apps02,apps03
Service hr is running on nodes: apps02,apps03
Service sales is running on nodes: apps01,apps04
```

#### Obtaining the Configuration of Services with SRVCTL

Run the `srvctl config service` command from the command line to obtain the high availability configuration of a service. For example, the following command returns the configuration of the `erp` service that is running on the `apps` database:

```
srvctl config service -d apps -s erp

Service name: erp
Service is enabled
Server pool: sp1
Cardinality: UNIFORM
Disconnect: false
Service role: PRIMARY
Management policy: AUTOMATIC
DTP transaction: false
AQ HA notificaitons: false
Failover type: NONE
Failover method: NONE
TAF failover retries: 0
TAF failover delay: 0
Connection Load Balancing Goal: LONG
Runtime Load Balancing Goal: SERVICE_TIME
TAF policy specification: NONE
Edition:
Service is enabled on nodes:
Service is disabled on nodes:
```

See Also:

[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for information about other administrative tasks that you can perform with SRVCTL

## Measuring Performance by Service Using the Automatic Workload Repository

Services add a new dimension for performance tuning. With services, workloads are visible and measurable, and therefore resource consumption and wait times are attributable by application. Tuning by using 'service and SQL' replaces tuning by 'session and SQL' in the majority of systems where all sessions are anonymous and shared.

The Automatic Workload Repository (AWR) maintains performance statistics that include information about response time, throughput, resource consumption, and wait events for all services and work that a database performs. Oracle Database also maintains metrics, statistics, wait events, wait classes, and SQL-level traces for services. You can optionally augment these statistics by defining modules within your application to monitor certain statistics. You can also define the actions within those modules that business critical transactions should execute in response to particular statistical values.

Enable module and action monitoring using the `DBMS_MONTIOR` PL/SQL package. For example, for connections that use the `erp` service, the following command enables monitoring for the `exceptions pay` action in the `payroll` module:

```
EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(SERVICE_NAME => 'ERP', 
MODULE_NAME=> 'PAYROLL', ACTION_NAME => 'EXCEPTIONS PAY');
```

For connections that use the `erp` service, the following command enables monitoring for all actions in the `payroll` module:

```
EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(SERVICE_NAME => 'ERP', 
MODULE_NAME=> 'PAYROLL', ACTION_NAME => NULL);
```

Use the `DBA_ENABLED_AGGREGATIONS` view to verify that you have enabled monitoring for application modules and actions.

Statistics aggregation and tracing by service are global in scope for Oracle RAC databases. In addition, these statistic aggregations are persistent across instance restarts and service relocations for both Oracle RAC and noncluster Oracle databases.

The service, module, and action names are visible in `V$SESSION`, `V$ACTIVE_SESSION_HISTORY`, and `V$SQL` views. The call times and performance statistics are visible in `V$SERVICE_STATS`, `V$SERVICE_EVENT`, `V$SERVICE_WAIT_CLASS`, `V$SERVICEMETRIC`, and `V$SERVICEMETRIC_HISTORY`. When you enable statistics collection for an important transaction, you can see the call speed for each service, module, and action name at each database instance using the `V$SERV_MOD_ACT_STATS` view.

The following sample SQL\*Plus script provides service quality statistics for a five second interval. You can use these service quality statistics to monitor the quality of a service, to direct work, and to balance services across Oracle RAC instances:

```
SET PAGESIZE 60 COLSEP '|' NUMWIDTH 8 LINESIZE 132 VERIFY OFF FEEDBACK OFF
COLUMN service_name FORMAT A20 TRUNCATED HEADING 'Service'
COLUMN begin_time HEADING 'Begin Time' FORMAT A10
COLUMN end_time HEADING 'End Time' FORMAT A10
COLUMN instance_name HEADING 'Instance' FORMAT A10
COLUMN service_time HEADING 'Service Time|mSec/Call' FORMAT 999999999
COLUMN throughput HEADING 'Calls/sec'FORMAT 99.99 
BREAK ON service_name SKIP 1 
SELECT 
    service_name 
  , TO_CHAR(begin_time, 'HH:MI:SS') begin_time 
  , TO_CHAR(end_time, 'HH:MI:SS') end_time 
  , instance_name 
  , elapsedpercall  service_time
  ,  callspersec  throughput
FROM  
    gv$instance i     
  , gv$active_services s     
  , gv$servicemetric m 
WHERE s.inst_id = m.inst_id  
  AND s.name_hash = m.service_name_hash
  AND i.inst_id = m.inst_id
  AND m.group_id = 10
ORDER BY
   service_name
 , i.inst_id
 , begin_time ;
```

## Automatic Workload Repository Service Thresholds and Alerts

Service level thresholds enable you to compare actual service levels against required levels of service. This provides accountability for the delivery or the failure to deliver an agreed service level. The end goal is a predictable system that achieves service levels. There is no requirement to perform as fast as possible with minimum resource consumption; the requirement is to meet the quality of service.

AWR allows you to explicitly specify two performance thresholds for each service: the response time for calls (`ELAPSED_TIME_PER_CALL`), and the CPU time for calls (`CPU_TIME_PER_CALL`). The response time threshold indicates that the elapsed time for each user call for each service should not exceed a certain value, and the CPU time for calls threshold indicates that the time spent using the CPU for each call for each service should not exceed a certain value. Response time is a fundamental measure that reflects all delays and faults that might be blocking the call from running on behalf of the user. Response time can also indicate differences in node power across the nodes of an Oracle RAC database.

You must set these thresholds on each instance of an Oracle RAC database. The elapsed time and CPU time are calculated as the moving average of the elapsed, server-side call time. The AWR monitors the elapsed time and CPU time and publishes AWR alerts when the performance exceeds the thresholds. You can schedule actions using Oracle Enterprise Manager jobs for these alerts, or you can schedule actions to occur programmatically when the alert is received. You can respond to these alerts by changing the priority of a job, stopping overloaded processes, or by relocating, starting or stopping a service. This permits you to maintain service availability despite changes in demand.

This section includes the following topics:

- Example of Services and Thresholds Alerts
- Enable Service, Module, and Action Monitoring

### Example of Services and Thresholds Alerts

In this scenario, you need to check the thresholds for the payroll service. You can use the AWR report to get this information. You should compare the results from reports run over several successive intervals during which time the system is running optimally. For example, assume that for servers accessed by a payroll application, the AWR report runs each Thursday during the peak usage times of 1:00 p.m. to 5:00 p.m. The AWR report contains the response time, or elapsed database time, and the CPU consumption time, or CPU time, for calls for each server, including the `payroll` service. The AWR report also provides a breakdown of the work done and the wait times that are contributing to the response times.

Using `DBMS_MONITOR`, you set a warning threshold for the elapsed time per call for the `payroll` service at 0.5 seconds (500000 microseconds). You also set a critical threshold for the elapsed time per call for the `payroll` service at 0.75 seconds (750000 microseconds).

In this example, thresholds are added for the `payroll` service as follows:

```
EXECUTE DBMS_SERVER_ALERT.SET_THRESHOLD( 
METRICS_ID => DBMS_SERVER_ALERT.ELAPSED_TIME_PER_CALL 
, warning_operator => DBMS_SERVER_ALERT.OPERATOR_GE 
, warning_value => '500000' 
, critical_operator => DBMS_SERVER_ALERT.OPERATOR_GE 
, critical_value => '750000' 
, observation_period => 30 
, consecutive_occurrences => 5 
, instance_name => NULL 
, object_type => DBMS_SERVER_ALERT.OBJECT_TYPE_SERVICE 
, object_name => 'payroll');
```

You can verify the threshold configuration is set on all the instances using the following `SELECT` statement:

```
SELECT METRICS_NAME, INSTANCE_NAME, WARNING_VALUE, CRITICAL_VALUE, 
OBSERVATION_PERIOD FROM dba_thresholds ;
```

### Enable Service, Module, and Action Monitoring

You can enable performance data tracing for important modules and actions within each service. The performance statistics are available in the `V$SERV_MOD_ACT_STATS` view. For example, you might decide to set the following:

- For the `ERP` service, enable monitoring for the `exceptions pay` action in the `payroll` module.
- For the `ERP` service, enable monitoring for the all actions in the `payroll` module.
- For the `HOT_BATCH` service, enable monitoring for all actions in the `posting` module.

The following commands show how to enable the module and action monitoring for the services:

```
EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(service_name => 'erp', module_name=>
 'payroll', action_name => 'exceptions pay');
EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(service_name => 'erp', module_name=>
 'payroll', action_name => NULL);
EXECUTE DBMS_MONITOR.SERV_MOD_ACT_STAT_ENABLE(service_name => 'hot_batch', 
module_name =>'posting', action_name => NULL);
```

To verify monitoring is enabled for the service, module, and actions, use the following `SELECT` statement:

```
COLUMN AGGREGATION_TYPE FORMAT A21 TRUNCATED HEADING 'AGGREGATION'
COLUMN PRIMARY_ID FORMAT A20 TRUNCATED HEADING 'SERVICE'
COLUMN QUALIFIER_ID1 FORMAT A20 TRUNCATED HEADING 'MODULE'
COLUMN QUALIFIER_ID2 FORMAT A20 TRUNCATED HEADING 'ACTION'
SELECT * FROM DBA_ENABLED_AGGREGATIONS ;
```

The output might appear as follows:

```
AGGREGATION           SERVICE                MODULE        ACTION
------------           --------------------   ----------    -------------
SERVICE_MODULE_ACTION  ERP                    PAYROLL       EXCEPTIONS PAY
SERVICE_MODULE_ACTION  ERP                    PAYROLL
SERVICE_MODULE_ACTION  HOT_BATCH              POSTING
```

---

Footnote Legend

Footnote 1: Runtime connection load balancing is basically routing work requests to sessions in a session pool that can best serve the work. It comes into effect when selecting a session from an existing session pool. Thus, runtime connection load balancing is a very frequent activity.
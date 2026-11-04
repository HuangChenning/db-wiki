---
title: Configuring Fast Connection Failover
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_fcf.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 11 Configuring Fast Connection Failover

The steps described in this chapter assume that the client version and database version are 11.2.0.1 or higher. The 11.2.0.1 release provides for the following features when compared to 11.1.0.7 or below:

- Role based services
- Data Guard broker sending FAN ONS events to JDBC clients
- Support for SCAN addresses

While previous versions do not have the above features it is possible to achieve similar results with manual configuration. For example:

- Create triggers that manage stopping and starting a service based on the database role.
- Utilize an external ONS publisher to send FAN events after a failover has occurred.
- Creating Oracle Net aliases that include all hosts with the potential to become a primary.

The steps for configuring versions earlier than 11.2.0.1 are in the MAA white paper "Client Failover Best Practices for Highly Available Oracle Databases: Oracle Database 10g Release 2" at

`http://www.oracle.com/goto/maa`

Types of Failures

Unplanned failures of an Oracle Database instance fall into the general categories:

- A server failure or other fault that causes the crash of an individual Oracle instance in an Oracle RAC database. To maintain availability, application clients connected to the failed instance must quickly be notified of the failure and immediately establish a new connection to the surviving instances of the Oracle RAC database.
- A complete-site failure that results in both the application and database tiers being unavailable. To maintain availability users must be redirected to a secondary site that hosts a redundant application tier and a synchronized copy of the production database.
- A partial-site failure where the primary database, a single-instance database, or all nodes in an Oracle RAC database become unavailable but the application tier at the primary site remains intact.

Configure Fast Connection Failover as a best practice to fully benefit from fast instance and database failover and switchover with Oracle RAC and Oracle Data Guard. Fast Connection Failover enables clients, mid-tier applications, or any program that connects directly to a database to failover quickly and seamlessly to an available database service when a database service becomes unavailable.

This chapter contains the following topics:

See Also:

- The MAA white paper "Client Failover Best Practices for Highly Available Oracle Databases: Oracle Database 11g Release 2" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- "Application High Availability with Services and FAN" in [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13180)

## 11.1 Configure JDBC and OCI Clients for Failover

The best practices for configuration to enable fast connection failover differs, depending on the type of your client: JDBC or OCI.

Fast Connection Failover for JDBC Clients

For JDBC clients, follow these best practices:

1. Enable Fast Connection Failover for JDBC clients by setting the `DataSource` property `FastConnectionFailoverEnabled` to `TRUE`.
2. Configure JDBC clients to use a connect descriptor that includes an address list that in turn includes the SCAN address for each site and connects to an existing service.
3. The JDBC client must set the `oracle.net.ns.SQLnetDef.TCP_CONNTIMEOUT_STR` property. This property enables the JDBC client to quickly traverse an `ADDRESS_LIST` in the event of a failure.
4. Configure a remote Oracle Notification Service (ONS) subscription on the JDBC client so that an ONS daemon is not required on the client.
5. By default the JDBC application randomly picks three hosts from the `setONSConfiguration` property and creates connections to those three ONS daemons. You must change this default so that connections are made to all ONS daemons. This is done by setting the following property when the JDBC application is invoked to the total number of ONS daemons in the configuration:
	`java - oracle.ons.maxconnections=4`

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13194) for more information about Enabling Fast Connection Failover for JDBC Clients
- "Application High Availability with Services and FAN" in [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13180)

Fast Connection Failover for OCI Clients

For OCI clients, follow these best practices:

1. Enable Fast Application Notification (FAN) for OCI clients by initializing the environment with the `OCI_EVENTS` parameter.
2. Link the OCI client applications with the thread library.
3. Set the `AQ_HA_NOTIFICATIONS` parameter to `TRUE` and configure the transparent application failover (TAF) attributes for services.
4. Configure an Oracle Net alias that the OCI application uses to connect to the database. The Oracle Net alias should specify both the primary and standby SCAN hostnames. For best performance while creating new connections the Oracle Net alias should have `LOAD_BALANCE=OFF` for the `DESCRIPTION_LIST` so that `DESCRIPTIONs` are tried in an ordered list, top to bottom. With this configuration the second `DESCRIPTION` is only attempted if all connection attempts to the first `DESCRIPTION` have failed.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN13195) for more information about Enabling Fast Connection Failover for Oracle Call Interface Clients
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci09adv.htm#LNOCI16679) for more information about Transparent Application Failover in OCI

## 11.2 Configure Oracle RAC Databases for Failover

Oracle Database 11g provides the infrastructure to make your application data highly available with Oracle Real Application Clusters (Oracle RAC) and with the Oracle Data Guard. At the database tier you must configure fast application failover.

### 11.2.1 Configure Database Services

At a high level, automating client failover in an Oracle RAC configuration includes relocating database services to new or surviving instances, notifying clients that a failure has occurred to break the clients out of TCP timeout, and redirecting clients to a surviving instance (Oracle Clusterware sends FAN messages to applications; applications can respond to FAN events and take immediate action). For more information about FAN, see [Section 6.1.1, "Client Configuration and Migration Concepts"](config_cw.md).

For services on an Oracle RAC database, Oracle Enterprise Manager or the SRVCTL utility are the recommended tools to manage services. A service can span one or more instances of an Oracle database and a single instance can support multiple services. The number of instances offering the service is managed by the DBA independent of the application.

See Also:

- [Section 6.1.1, "Client Configuration and Migration Concepts"](config_cw.md)
- [Section 6.2.5, "Connect to Database Using Services and Single Client Access Name (SCAN)"](config_cw.md)

### 11.2.2 Optionally Configure FAN Server Side Callouts

Server-side callouts provide a simple, yet powerful integration mechanism with the High Availability Framework that is part of Oracle Clusterware. You can use server side callouts to log trouble tickets or page Administrators to alert them of a failure. For Up events, when services and instances are started, new connections can be created so the application can immediately take advantage of the extra resources

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) for an Introduction to Automatic Workload Management.
- For more information about client failover best practices and details on deploying FAN server side callouts, see the Technical Article, "Automatic Workload Management with Oracle Real Application Clusters 11g Release 2" on the Oracle Technology Network at
	`http://www.oracle.com/technetwork/database/clustering/overview/index.html`

## 11.3 Configure the Oracle Data Guard Environment

To configure the Oracle Data Guard environment, do the following:

- Configure Database Services
- Use Data Guard Broker
	See Also:
	The MAA white paper "Client Failover Best Practices for Data Guard 11g Release 2" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

### 11.3.1 Configure Database Services

In an Oracle Data Guard configuration you should only run primary application services on the primary database and run standby application services on the standby database. Beginning with Data Guard 11g Release 2, you can automatically control the startup of database services on primary and standby databases by assigning a database role to each service (roles include: `PRIMARY`, `PHYSICAL_STANDBY`, `LOGICAL_STANDBY`, and `SNAPSHOT_STANDBY`).

A database service automatically starts upon database startup if the management policy for the service is `AUTOMATIC` and if a role assigned to that service matches the current role of the database.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12738) for information about Creating and Deleting Database Services with SRVCTL
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN12830) for information About Automatic Startup of Database Services

### 11.3.2 Use Data Guard Broker

The best practice is to configure Oracle Data Guard to manage the configuration with Oracle Data Guard Broker. Oracle Data Guard Broker is responsible for sending FAN events to client applications to clean up their connections to the down database and reconnect to the new production database. For more information about FAN, see [Section 6.1.1, "Client Configuration and Migration Concepts"](config_cw.md).

Oracle Clusterware must be installed and active on the primary and standby sites for both single instance (using Oracle Restart) and Oracle RAC databases. Oracle Data Guard broker coordinates with Oracle Clusterware to properly fail over role-based services to a new primary database after a Data Guard failover has occurred. For more information, see

See Also:

[Section 9.3.1, "Use Oracle Data Guard Broker with Oracle Data Guard"](config_dg.md)

## 11.4 Client Transition During Switchover Operations

In Oracle Data Guard, the term switchover describes a planned event where a primary and standby database switch roles, usually to minimize the downtime while performing planned maintenance. The configuration best practices to address unplanned failovers also address most of the requirements for a planned switchover, except for several additional manual steps that apply to logical standby databases (SQL Apply).

Note:

There are no additional considerations for switchovers using Oracle Active Data Guard.

The following steps describe the additional manual switchover steps for Oracle Data Guard 11g Release 2:

1. The primary database is converted to a standby database. This disconnects all sessions and brings the database to the mount state. Oracle Data Guard Broker shuts down any read/write services.
2. Client sessions receive a ORA-3113 and begin going through their retry logic (TAF for OCI and application code logic for JDBC).
3. The standby database is converted to a primary database and any existing sessions are disconnected. Oracle Data Guard Broker shuts down read-only services.
4. Read-only connections receive an ORA-3113 and begin going through their retry logic (TAF for OCI and application code logic for JDBC).
5. As the new primary and the new standby are opened, the respective services are started for each role and clients performing retries now see the services available and connect.

For logical standby switchover:

1. Ensure that the proper reconnection logic has been configured (for more information, see Section 11.1, "Configure JDBC and OCI Clients for Failover" and Section 11.2, "Configure Oracle RAC Databases for Failover"). For example, configure `TAF` and `RETRY_COUNT` for OCI applications and code retry logic for JDBC applications.
2. Stop the services that the primary application uses and the read-only applications enabled on the standby database.
3. Disconnect or shutdown the primary and read-only application sessions.
4. Once the switchover has completed, restart the services used by the primary application and the read-only application.
5. Sessions that were terminated reconnect once the service becomes available as part of the retry mechanism.
6. Restart the application if an application shuts down.

Note that FAN is not needed to transition clients during a switchover operation if the application performs retries. FAN is only needed to break clients out of TCP timeout, a state that should only occur during unplanned outages.

See Also:

[Section 14.2.1.3, "How to Perform Data Guard Switchover"](schedule_outage.md)

## 11.5 Preventing Login Storms

The process of failing over an application that has a large number of connections may create a login storm. A login storm is a sudden spike in the number of connections to a database instance, which drains CPU resources. As CPU resources are depleted, application timeouts and application response times are likely to increase.

To control login storms:

- Implement the Connection Rate Limiter
	The primary method of controlling login storms is to implement the Connection Rate Limiter feature of the Oracle listener. This feature limits the number of connections that can be processed in seconds. Slowing down the rate of connections ensures that CPU resources remain available and that the system remains responsive.
- Configure Oracle Database for shared server operations
	In addition to implementing the Connection Rate Limiter, some applications can control login storms by configuring Oracle Database for shared server operations. By using shared server, the number of processes that must be created at failover time are greatly reduced, thereby avoiding a login storm.
- Adjust the maximum number of connections in the mid tier connection pool
	If such a capability is available in your application mid tier, try limiting the number of connections by adjusting the maximum number of connections in the mid tier connection pool.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN00502) for more information about configuring and controlling shared server operations
- The "Oracle Net Listener Connection Rate Limiter" white paper for information about the Connection Rate Limiter at
	`http://www.oracle.com/technetwork/database/enterprise-edition/oraclenetservices-connectionratelim-133050.pdf`
- The "Best Practices for Optimizing Availability During Unplanned Outages Using Oracle Clusterware and Oracle Real Application Clusters" white paper for information and examples about listener connection rate throttling from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

## 11.6 Application support

Currently, PeopleSoft Enterprise and Oracle WebLogic Server have support for FAN events.

PeopleSoft PeopleTools version 8.50.09 and higher supports FAN. This enables PeopleSoft applications to automatically failover database connections to a surviving instance in an Oracle RAC cluster or to a new primary database in an Oracle Data Guard configuration should its database connection be lost. If an Oracle RAC instance fails, a primary database fails, or the Oracle Database is shutdown or restarted, PeopleSoft servers and clients continue running and users are not required to login a second time.

In Oracle WebLogic Server 10.3.4, a single data source implementation has been introduced to support an Oracle RAC cluster. It responds to FAN events to provide Fast Connection Failover (FCF), run-time connection load-balancing (RCLB), and Oracle RAC instance graceful shutdown. XA affinity is supported at the global transaction ID level. The new feature is called WebLogic Active GridLink for Oracle RAC, which is implemented as the GridLink data source within Oracle WebLogic Server.

For applications that do not support FAN events, this includes a number of applications from Oracle (for example, Siebel and Oracle E-Business Suite), all of the steps described in this section should be completed for the fastest client failover possible. Even though FAN events cannot be used in such cases, applications can still be configured for efficient failover by using timeouts and application retries.

For more information see the MAA white paper "Client Failover Best Practices for Highly Available Oracle Databases: Oracle Database 11g Release 2" at

`http://www.oracle.com/goto/maa`
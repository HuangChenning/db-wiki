---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/configuring-level-1-basic-application-high-availability.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Configuring Level 1: Basic Application High Availability

Implement a level of high availability that allows applications to immediately react to instance, node, or database failures, and quickly establish new connections to surviving database instances.

With application HA Level 1, downtime is minimized for unplanned and planned outages. You get these benefits by ensuring that the application configuration implements these recommendations. No code changes are required.

At a high level, the steps to implement Level 1 are:

### Step 1: Configure High Availability Database Services

Create a non-default, role-based database service to use high-availability features.

A database service is a logical abstraction for managing workloads or a group of applications sharing similar SLAs or types of workloads (for example, OLTP vs. batch). Database services provide location transparency and hide complex aspects of the underlying system from the client.

Your application must connect to a non-default database service to use high-availability features. You must explicitly create a service (or several services as needed for different application workloads) instead of using the default database service or the default PDB service (that is, the service with the same name as the database or PDB).

On Oracle Autonomous Database, services are created for you using recommended attributes.

About Server-Side Configuration for Services

These services are configured by a database administrator to set up services through Oracle Clusterware.

When using Oracle Data Guard and standby databases, create services using the primary role to ensure that applications connect to the primary database for read/write operations, and standby role for services to optionally offload read-only and small infrequent writes to the standby database.

Services start and stop automatically after a Data Guard role transition (for example, switchover or failover) based on their roles.

Configure your services according to your architecture in one of the following sections:

- Configure High Availability Services
- Configure High Availability Services for Oracle Active Data Guard or Standby Roles

Note:

Services must be started so that they can be used after creating them. Use a command like this:

`$ srvctl start service -db mydb -service                     my_service`

See also:

[Using Oracle Services](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-4CC2D344-02D6-40E7-85B6-BB3AA7D6461A) in Oracle Real Application Clusters Administration and Deployment Guide

#### Configure High Availability Services

Create a non-default, role-based database service to use high-availability features.

A service may be configured to direct connections to a single preferred instance, or alternatively, if the preferred instance is down, to an available instance. When a service is available only on one instance, it is called a singleton service. This allows you to isolate workloads among instances in a cluster.

You could also configure a service to put connections on multiple instances of a cluster, to spread work across all instances. Also, if one instance is down, connections can be made on the surviving instances.

There are other combinations where you can configure a subset of instances as "preferred" and another subset of instances as "available". These subsets provide for spreading load across some instances while isolating work from others (and still have instances available in case of a failure).

See Considerations for Oracle Cloud Database Services if your database is running on the Oracle Cloud.

Example 1: Singleton Service

This example creates a singleton service called `my_service` for the primary role, where the connections are made on instance `inst1`, unless that instance is not available. If the instance is not available, connections are made on `inst2`.

The example also configures a default drain timeout of 300 seconds to wait for sessions to drain; at the end of that time any remaining sessions are terminated because of the `IMMEDIATE` option.

```
$ srvctl add service -db mydb -service my_service -pdb mypdb –preferred inst1
 -available inst2 -notification TRUE -drain_timeout 300 -stopoption IMMEDIATE
 -role PRIMARY
```

If you want your application to gracefully switch to another Oracle RAC instance with no application blackout, set the `drain_timeout` interval to a sufficient timeout that allows your applications to close their connections between transactions and gracefully stop or move to another instance. The `drain_timeout` interval is best leveraged for short OLTP applications. For large batch operations, it's best defer or suspend these operations before a planned maintenance window.

Example 2: Service with Multiple Instances

This example creates a service that is similar to the singleton above but spreads connections across multiple instances in this cluster:

```
$ srvctl add service -db mydb -service my_service -pdb mypdb
 –preferred inst1,inst2 -notification TRUE -drain_timeout 300 -stopoption IMMEDIATE
 -clbgoal LONG -rlbgoal SERVICE_TIME -role PRIMARY
```

#### Configure High Availability Services for Oracle Active Data Guard or Standby Roles

A service used to connect to a standby database (read-only physical standby) is created as follows:

```
$ srvctl add service -db mydb -service my_standby_service -pdb mypdb
 –preferred inst1 -available inst2 -notification TRUE -drain_timeout 300
 -stopoption IMMEDIATE -clbgoal LONG -rlbgoal SERVICE_TIME -role PHYSICAL_STANDBY
```

#### Considerations for Oracle Cloud Database Services

A default service is created along with every PDB that is provisioned in the Oracle cloud.

Note the following considerations depending on the type of cloud service you have.

Autonomous Database Serverless

For Autonomous Database Serverless, database services are pre-configured to support different performance and concurrency characteristics. You can modify the services to enable certain availability features using the `DBMS_APP_CONT_ADMIN` package.

Specifically:

- To set the drain timeout attributes, use `DBMS_APP_CONT_ADMIN.SET_DRAINING`. See [DBMS\_APP\_CONT\_ADMIN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ARPLS-GUID-6DC025A4-D5FF-4EEC-98B1-DED51ED8FC8B) for details.
- To set TAC or AC attributes, use `DBMS_APP_CONT_ADMIN.ENABLE_TAC` or `DBMS_APP_CONT_ADMIN.ENABLE_AC`
	This sets the associated service attributes to their recommended values to support TAC or AC
- To set specific attributes, use `DBMS_APP_CONT_ADMIN.MODIFY_SERVICE`
	The extent to which the `DBMS_APP_CONT_ADMIN` package supports changes to the service depends on the database version.

Availability aspects of services in Autonomous Database Serverless, such as preferred and available instances are configured automatically. See [Database Service Names for Autonomous Database](https://docs.oracle.com/iaas/autonomous-database-serverless/doc/predefined-database-services-names.html#GUID-6CEFC4B7-6EF8-4237-A004-C88F570A480B) for more details and other options.

Autonomous Database on Dedicated Exadata Infrastructure

For Autonomous Database on Dedicated Exadata Infrastructure, database services are pre-configured with TAC, AC, and support for various degrees of parallelism. Use the service name that meets the needs of your application.

Availability aspects of services in Autonomous Database, such as preferred and available instances, are configured automatically. See [Predefined Database Service Names for Autonomous Databases](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbbd/#GUID-07401C82-6A01-4CDF-AAE5-54B78B50CA0A) for more details and other options.

Oracle Exadata Database Service on Dedicated Infrastructure and Oracle Base Database

Do not use the default PDB or CDB service.

The service in the connect string provided by the UI is for administrative purposes, not for client application connections. You must create a database service for your applications by following the recommendations in Configure High Availability Services.

" You must create a database service for your applications by following the recommendations in the above section, "Configure High Availability Services".

### Step 2: Configure the Connection String for High Availability

Oracle recommends that your application use the connection string configuration shown here to connect successfully during various scenarios including database switchover and failover to other sites.

Example 1: Connect string with Oracle RAC primary database and no standby

```
Alias = (DESCRIPTION =
(CONNECT_TIMEOUT= 90)(RETRY_COUNT=20)(RETRY_DELAY=3)(TRANSPORT_CONNECT_TIMEOUT=1000ms)
    (ADDRESS_LIST =
        (LOAD_BALANCE=on)
        (ADDRESS = (PROTOCOL = TCP)(HOST=clu_site1-scan)(PORT=1521))) 
    (CONNECT_DATA=(SERVICE_NAME = my_service)))
```

Example 2: Connect string with Oracle RAC primary and standby databases

This example makes connections to an Oracle RAC primary database or a standby database, depending on which one is available.

```
Alias = (DESCRIPTION =
(CONNECT_TIMEOUT= 90)(RETRY_COUNT=100)(RETRY_DELAY=3)(TRANSPORT_CONNECT_TIMEOUT=1000ms)
    (ADDRESS_LIST =
        (LOAD_BALANCE=on)
        (ADDRESS = (PROTOCOL = TCP)(HOST=clu_site1-scan)(PORT=1521)))
    (ADDRESS_LIST =
        (LOAD_BALANCE=on)
        (ADDRESS = (PROTOCOL = TCP)(HOST=clu_site2-scan)(PORT=1521)))      
    (CONNECT_DATA=(SERVICE_NAME = my_service)))
```

Note:

clu\_site1-scan and clu\_site2-scan refer to SCAN listeners in a cluster on site1 and site2, respectively.

It's recommended that you use the most recent drivers, but all Oracle drivers from release 12.2 and later should use the example connection strings above. Specific values can be tuned, but the values shown in this example are reasonable starting points, and so usable for almost all cases.

It is highly recommended that you maintain your connect string or URL in a central location, such as LDAP or `tnsnames.ora`. Do not scatter the connect string or URL in property files or private locations, as doing so makes it extremely difficult to maintain. Using a centralized location helps you preserve standard format, tuning, and service settings. Oracle's solution for this is to use LDAP with the Oracle Unified Directory product.

For JDBC, the connection strings listed above would be implemented as shown in these examples.

Example 1. Oracle RAC with no standby

```
jdbc:oracle:thin:@(DESCRIPTION =(CONNECT_TIMEOUT= 90)(RETRY_COUNT=20)(RETRY_DELAY=3)
(TRANSPORT_CONNECT_TIMEOUT=1000ms)(ADDRESS_LIST=(LOAD_BALANCE=on)(ADDRESS = (PROTOCOL = TCP)
(HOST=clu_site1-scan)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME = my_service)))
```

Example 2. Oracle RAC with standby

```
jdbc:oracle:thin:@(DESCRIPTION =(CONNECT_TIMEOUT= 90)(RETRY_COUNT=100)(RETRY_DELAY=3)
(TRANSPORT_CONNECT_TIMEOUT=1000ms)(ADDRESS_LIST=(LOAD_BALANCE=on)(ADDRESS = (PROTOCOL = TCP)
(HOST=clu_site1-scan)(PORT=1521)))(ADDRESS_LIST=(LOAD_BALANCE=on)(ADDRESS = (PROTOCOL = TCP)
(HOST=clu_site2-scan)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME = my_service)))
```

For other clients, refer to your client's documentation.

See also:

- [Connection Time Estimates During Data Guard Switchover or Failover](connection-time-estimates-data-guard-switchover-or-failover.md)
- [Oracle Net TNS String Parameters](oracle-net-tns-string-parameters.md)
- [Oracle Unified Directory](https://docs.oracle.com/en/middleware/idm/unified-directory/12.2.1.4/oudag/introduction-oracle-unified-directory.html#GUID-53DE34B1-370C-4C09-93EB-F5FAE76CCA02) in Administering Oracle Unified Directory
- [Overview of Local Naming Parameters](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=NETRF-GUID-12C94B15-2CE1-4B98-9D0C-8226A9DDF4CB) in Oracle Database Net Services Reference

Oracle Cloud Considerations for Connection Strings

Oracle Cloud provides sample connection strings for CDBs and PDBs that are provisioned.

For Cloud services such as Exadata Database Services on Dedicated Infrastructure or Oracle Base Database Service, you must change the connection string that is provided to include the new service you added in step 1, instead of the default service in the provided connect string.

If your database has a Data Guard association, then you may want to use the connection string format in step 2 that includes the primary and standby entries, if you require your existing application to fail over to the standby automatically after a primary database failure.

For a standby in the same region, you should typically add the standby in the connect string, but for a cross-region standby, evaluate the OCI Full Stack Disaster Recovery service to orchestrate application, database, and client failover. See [Full Stack Disaster Recovery on Oracle.com](https://www.oracle.com/cloud/full-stack-disaster-recovery/).

### Step 3: Use Fast Application Notification

When a service needs to drain for routine maintenance, or experiences unplanned failures (such as node or network outages), the application needs to be informed in real time so that it can quickly move connections to another instance or site. This is accomplished using Oracle's Fast Application Notification (FAN) feature, which enables applications and connection pools to receive event notifications from one or more clusters.

The ability to receive FAN events is enabled automatically when using the recommended service and connect string in steps 1 and 2 above, along with Oracle JDBC drivers (the latest version is recommended, but not earlier than Oracle release 12.2).

The ONS port (by default, 6200) needs to be opened on all of your database servers, the firewall, and Oracle Active Data Guard nodes.

The use of FAN is not mandatory, but is highly desirable because it can detect many types of unplanned outage scenarios and enable applications to handle these scenarios gracefully to maintain high availability.

FAN uses Oracle Clusterware's Oracle Notification Service (ONS) to receive events from the cluster. ONS requires ports to be available between the client and the servers, and in some cases this requires a firewall port to be opened (6200 by default) on all of your database servers, the firewall, and Oracle Active Data Guard nodes.

Alternative if you can't use ONS FAN: In-Band Notification

When port 6200 cannot be opened or is not available, Oracle's connection drivers will enable "in-band" notifications automatically using the database connections themselves. In-band notifications are received on the next round-trip to the database.

This notification simply tells the driver that the service is draining and the client should close the connection. Clients will not receive events for an instance or node failure to advise a client to disconnect immediately, because those kinds of failures will terminate connections ungracefully, removing the ability to see any notification because the connection would be gone.

In-band notification is for planned maintenance and does not apply to unplanned outages.

Oracle cloud normally has port 6200 enabled, but if you have blocked port 6200, then in-band notification is automatically used to initiate draining of connections to other nodes during planned maintenance.

See [In-Band Draining Notification Application Requirements](band-draining-notification-application-requirements.md) to ensure that your client is properly configured to use in-band FAN.

Oracle Autonomous Database Serverless

In-band notifications are used with Autonomous Database Serverless so clients can drain their connections during planned maintenance operations.

To ensure your clients are ready to use In-band notifications, see specific recommendations for Autonomous Database Serverless in [Best Practices to Maintain Application Availability During Maintenance Windows](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/maintenance-windows-patching.html#GUID-B5DB6887-AAAE-43F4-BDF7-73299328CB7E).

Enabling ONS/FAN for Clients

There are no application code changes to use FAN. FAN only requires an Oracle driver and the recommended database connect strings in step 2 above.

By default, starting with 19c, ONS is auto-configured by leveraging the recommended database connect strings (in step 2 above), when those strings are used to connect to a cluster using the cluster's SCAN listeners. ONS will automatically determine which nodes it should establish connections to, including nodes in standby clusters (as long as the standby clusters are in the connect string).

It is important to use the TNS formats shown in Step 2 for auto-configuration of FAN; using a different format syntax can prevent FAN from being auto-configured.

If you are not able to use the recommended connect URL/string (in step 2), configure your clients to subscribe to ONS manually by setting the list of ONS nodes and ports.

For example, in UCP, ONS endpoints could be configured like the following example (other pools would use something similar; check your pool's documentation):

```
pds.setONSConfiguration("nodes=racnode1:4200,racnode2:4200\nwalletfile=/oracle11/onswalletfile");
```

This example shows an ONS configuration using a wallet file, which is typically required with Oracle Cloud but should not be used in other environments.

If you need to configure ONS explicitly as shown above, it is recommended that you create a property file and reference that file to obtain ONS configuration values instead of hard-coding values. See [Remote Configuration of ONS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=JJUCP-GUID-C8D5FF91-6333-4E7F-BC81-CF7B93D56BEE) for details.

Ensure that your application server and drivers are compatible with ONS/FAN by reviewing [ONS FAN Application Requirements](ons-fan-application-requirements.md) and [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md).

Developer Actions to Enable High Availability

There are simple configuration changes for your application developers to make to enable application failover HA and draining. See [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md) for details.

See also:

[Overview of Oracle Integrated Clients and FAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-8CA1B780-FC7E-4050-8A11-468D27CBD308) in Oracle Real Application Clusters Administration and Deployment Guide

### Step 4: Developer Determines if the Application Should Implement Reconnection Logic

Applications can be written to catch connection failure exceptions and errors during database calls so that they can obtain new connections and continue with new work, if it is reasonable to continue.

There are many factors to take into account to determine if it is reasonable for an application to continue and how it should proceed after losing connections. In [Configuring Level 3: Mask Unplanned and Planned Failovers from Applications](configuring-level-3-mask-unplanned-and-planned-failovers-applications.md), a robust solution is presented for masking failures from your application transparently using AC and TAC.

For JDBC-based applications, the `SQLRecoverableException` can be caught to distinguish connection errors from typical application or SQL errors. If a connection error is caught, then a new connection should be obtained. This is simpler and more robust than checking for individual Oracle errors (which can adjust by Oracle Database release) in the `SQLException` class.

See also:

[Connection Retry Logic Examples](connection-retry-logic-examples.md)
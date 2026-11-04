---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/configuring-level-2-prepare-applications-planned-maintenance.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Configuring Level 2: Prepare Applications for Planned Maintenance

Building on Level 1, Basic Application High Availability, Level 2 adds the ability to drain sessions for minimal application impact during planned maintenance.

After implementing Level 1, you are ready to implement a planned maintenance solution appropriate to your application from one of the choices below. You can use planned operations to relocate or stop services, or to switch over, allowing for graceful completion of the users' work.

The recommended approach to avoid impacting applications is drain work in an Oracle RAC rolling fashion. Typically a period of time is allocated to perform the draining. Our recommended choice is to use Oracle connection pools that are integrated with FAN to initiate draining.

If you are unable to drain automatically using the options listed below, an alternative approach is to ensure the application manages to stop and defer work before maintenance starts.

Employ the following practices to increase your application high availability to level 2:

### Recommended Option: Use an Oracle Connection Pool

Using a FAN-aware Oracle connection pool is the recommended solution for managing planned maintenance.

Oracle pools provide full lifecycle management: draining, reconnecting, and rebalancing across nodes and sites. When performing rolling maintenance across a cluster, as the maintenance progresses and completes (for each instance or node), sessions are moved and rebalanced across instances. There is no impact to users when your application uses an Oracle Pool with FAN and returns connections to the pool between requests since these connections will drain and move to other instances.

Supported Oracle Pools include:

- Java; Universal Connection Pool (UCP)
	- UCP documentation: [Introduction to UCP](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=JJUCP-GUID-82ACD002-4C5F-4BF7-99FF-46A2A97DD35D)
		- Springboot with UCP: [UCP Best Practices for Oracle Database 19c and Spring Boot](https://medium.com/oracledevs/ucp-best-practices-for-oracle-database-19c-and-spring-boot-fb837f8e195b)
- Java; WebLogic Active GridLink
- Tuxedo
- OCI Session Pool
- ODP.NET core, managed, and unmanaged providers
- Oracle Python driver connection pool
- Node.js Oracle driver connection pool
- Hikari Connection Pools: [HikariCP Best Practices for Oracle Database and Spring Boot](https://medium.com/oracledevs/hikaricp-best-practices-for-oracle-database-and-spring-boot-4d6723621c0b)

When using these pools, no application changes are needed other than ensuring that your connections are returned to the pool between requests.

It is a best practice that an application obtains a connection only for the time that it needs it, and then returns the connection to the pool as soon as it is finished making its database calls. Holding a connection instead of returning it to the pool prevents the pool from gracefully moving sessions to available instances, and it uses resources inefficiently, requiring many more connections than would otherwise be used. An application should, therefore, obtain a connection and then return that connection immediately after the work is complete. The connections are then available for later use by other threads, or your thread when needed again. Returning connections to a connection pool is a general recommendation regardless of how draining is implemented.

Note:

The syntax for obtaining and returning a connection varies by pool implementation. For example, in UCP you use the `getConnection()` method of the `PoolDataSource` object to obtain a connection and mark the beginning of the database request, and the `close()` method to return it, marking the end of the database request after you've done some work in the database.

Oracle Connection Pools validate a connection whenever a connection is borrowed to ensure that the connection can be used without any errors.

### Alternate Options

Only look at these alternate options if you cannot use the recommended option. The alternate options are listed in priority order.

#### Alternate Option 1: Use Request Boundaries

For existing applications, retrofit them by using session/connection pools or by wrapping operations within a `requestBegin` and `requestEnd` boundary. For example, for the Oracle Call Interface: `OCIRequestBegin` and `OCIRequestEnd`.

Request boundaries are visible to the database, and they enable functionality such as draining for planned maintenance, load balancing, and multiplexing to be isolated at the database layer. Sessions can be re-established with no visible disruption to the application layers above.

#### Alternate Option 2: Use Connection Validation or Tests

If you cannot use an Oracle Pool, or do not wish to implement request boundaries, then the Oracle client drivers (19c or later) or Oracle Database (19c or later) can drain the sessions for you.

When services are relocated or stopped, or there is a switchover to a standby site via Oracle Data Guard, the Oracle Database and Oracle client drivers are notified to look for safe places to release connections according to the following:

- Standard connection tests for connection validity (for example `isValid()` in JDBC)
- Custom SQL tests for connection validity

For custom batch applications, test the connection between batches. When the connection test fails, create or borrow another connection.

For third-party connection pools, enable connection tests offered by the vendor. When the connection test fails, the third-party pool will close the connection and allow you to borrow another one.

See [In-Band Draining Notification Application Requirements](band-draining-notification-application-requirements.md) for implementing connection validation and tests for your specific application or driver.

Note:

- When you use a connection test, the outcome of the connection test applies to that session only. Do not use connection tests to make general decisions about the instance and to make a determination to stop more than the session to which the test applies.
- Disable connection pool properties for flushing and destroying the pool on connection test failure when using Oracle WebLogic Server data sources.
- A monitor is functionality that makes a decision about the health of an instance. With FAN and Runtime Load Balancing such monitors are no longer needed and not susceptible to incorrect decisions. If you do want a monitor, SQL in that monitor must NOT be misinterpreted as a connection test for draining the application. There are a few ways to avoid this misinterpretation:
	- Disable a monitor's specific health query using the `dbms_app_cont_admin` package:
		```
		dbms_app_cont_admin.disable_connection_test(dbms_app_cont_admin.sql_test,'SELECT COUNT(1) FROM DUAL’);
		```
		Here, the query used by the monitor, `'SELECT COUNT(1)                                         FROM DUAL’`, is not considered a connection test. If there are any connection tests that also use this query, then they would be disabled and a different query would be needed.
		- Embed a comment into the monitor query to distinguish it from any of the registered connection tests:
		```
		SELECT /* My Health monitor query */ COUNT(1) monitor FROM DUAL
		```
- You may disable connection tests by using the `DBMS_APP_CONT_ADMIN.DISABLE_CONNECTION_TEST` procedure. You can also add, modify, or delete connection tests using the `DBMS_APP_CONT_ADMIN` package.

### Server-Side Operations for Planned Maintenance

Server-side operations are required to manage connections for planned maintenance.

The server side operations for planned maintenance are implicitly executed If you are using Oracle cloud software automation, or are in a cloud maintenance window that requires restarting the database instance.

Note that services connected to the Oracle Database are configured with connection tests and a drain timeout specifying how long to allow for draining, and the `stopoption` (typically `IMMEDIATE`), that applies after the drain timeout expires. The `stop`, `relocate`, and `switchover` commands managed by SRVCTL include a `drain_timeout` and `stopoption` switch to override values set on the service if needed.

Oracle recommends configuring services with the required drain timeout applicable to that service, so they are used automatically during maintenance operations.

Maintenance commands are similar to the commands described in the examples in [Server-Side Planned Maintenance Command Examples](server-side-planned-maintenance-command-examples.md). You can use these commands to start draining. Include additional options, if needed, as described in My Oracle Support (MOS) Note: Doc ID 1593712.1. Oracle tools, such as Fleet Patching and Provisioning (FPP) use these commands as well.

Oracle Clusterware can start instances that are not currently running, but can run a service that requires that instance. Services that cannot be relocated or do not need relocation, are stopped. If a singleton service is defined with no other available instances, then it may incur complete downtime, which is expected behavior. It is better to have preferred instances and at least one available instance always defined.

After the maintenance is complete and the instance is restarted, no additional SRVCTL action is required because the Oracle Clusterware service attribute automatically determines where services will end up.

See also:

[Server Draining Ahead of Planned Maintenance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-2DD974C8-94C2-446B-B2BD-81B8135A26C3) in Oracle Real Application Clusters Administration and Deployment Guide
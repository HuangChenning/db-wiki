---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/application-high-availability-levels.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 39 About Application High Availability Levels

Ensure that your applications are configured to quickly and automatically shift workload to available Oracle RAC instances or standby databases during planned maintenance and unplanned outages.

Depending on your application's high availability requirements, you can implement the level of high availability (HA) protection that you need.

Application up time is maximized by following these recommendations when there are outages.

The primary audience for this document is application developers and application owners. Operational examples are included for database administrators and PDB administrators.

HA protection levels are defined in the table below, and each increase in level builds upon the previous level.

| HA Level | Configuration | Experience | Benefits |
| --- | --- | --- | --- |
| Level 1: Basic Application High Availability  See [Configuring Level 1: Basic Application High Availability](configuring-level-1-basic-application-high-availability.md) | Database or Security Administrator:  - Configure role-based database services - Leverage recommended database connection string, and optionally configure LDAP and wallets - Enable Oracle Notification Service (ONS)/Fast Application Notification (FAN)  Application Developer:  - Use MAA recommended connect string - Use Basic exception handling  Implementation effort: Minimal - estimated 1 hour for administrator, and less than 1 hour for developers (assuming the application has connection failure exception logic already coded) | Implementing Level 1 protection provides significant benefits compared to third party application failover solutions due to application + Oracle integration and intelligence to reduce application impact.  - Reduced application downtime - Applications see errors during planned maintenance and unplanned outages; the application may trap the connection error and, if it is appropriate for the application, reconnect to another Oracle RAC instance or database with the target service - Applicable for unplanned outages and planned maintenance. In some cases, long running transactions should be deferred or suspended during planned maintenance. | High availability with application automatically failing over and reconnecting (if appropiate for the application)  - Quick timeouts and automated connection retry with database connect string - Location transparency with services: role-based services for standby and read-only databases so that applications are automatically routed to the proper instance with the correct role - ONS/FAN auto-configured with database connect string - Immediate interrupt on outages when using FAN (no need to tune timeouts and wait for them) - Clusterware is aware of RAC and VIP health, so there is no waiting on downed end points thanks to FAN |
| Level 2: Prepare Applications for Planned Maintenance  See [Configuring Level 2: Prepare Applications for Planned Maintenance](configuring-level-2-prepare-applications-planned-maintenance.md) | Level 1 configuration +  Application Developer:  - Use Oracle connection pools or connection tests and return your connection to the pool between uses  Additional implementation effort for developers: A few hours with minimal effort with Oracle Connection pools, including those in application servers - up to days when not using an application server, depending on application complexity. Developer may need to identify connection tests used in the application and possibly create new ones in the database | - Avoids errors during planned maintenance (errors still possible for unplanned outages) - Ability to drain and move workload gracefully without application interruption - Applicable for unplanned outages and planned maintenance events. For some cases, long running transactions should be staged with connection tests between batches. If this is not possible, the batch job should be deferred during planned maintenance. | Workload moves gracefully across instances with a slight delay and no errors during planned maintenance |
| Level 3: Mask Unplanned and Planned Failovers from Applications  See [Configuring Level 3: Mask Unplanned and Planned Failovers from Applications](configuring-level-3-mask-unplanned-and-planned-failovers-applications.md) | Level 1 and 2 configuration + "Application Continuity" Solution  Database or Security Administrator:  - Additional security and privileges required for PL/SQL aspects of the application  Application Developers:  - External actions (for example, side effects) outside the database need to be considered  Additional implementation effort: Days to weeks of collaboration between developers and database administrators to review protection coverage (depending on application complexity) | - In-flight transactions automatically acknowledge the commit or replay without application code changes - Database administrators and application developers coordinate to ensure readiness using AWR statistics to assess protection coverage, and use ACCHK (application continuity health check) to identify coverage or exceptions when transactions can or cannot be replayed | Masks unplanned and planned fail overs from applications  - Applications avoid seeing errors during planned maintenance and outages - In-flight uncommitted transactions are replayed; committed transactions are acknowledged and not replayed |

All of the HA Levels described in the table above are superior to connection management approaches using load balancers as single connection VIP endpoints for the following reasons:

- Smart Service Health and Intelligent Reconnect: Oracle Clusterware and Oracle Data Guard Broker closely monitor the health and state of the clusters and databases to ensure connections are routed to the database service that is opened on a primary.
- Transparent and Automatic Failover: There is no need to query the health of databases and decide which is the proper one to move a VIP; everything is transparent in the high availability approaches described in the table.
- Fast Notification and Automatic Connection Retries: The disconnection of already connected sessions is immediate, and happens intelligently when Oracle Clusterware and Data Guard Broker detect outages or role changes on the primary and standby databases.

Terms

The following terms are used throughout this document:

- Application Continuity: Application Continuity is an Oracle Database feature that masks interruptions at the database level for planned and unplanned events, improving the fault tolerance of applications that rely on Oracle Database.
- Transparent Application Continuity (TAC): Introduced with Oracle Database 18c, and enhanced in Oracle Database 19c and 23ai, extends support to application configurations that do not use Oracle connection pools (though they are still the preferred solution).
- Draining: Move a connection from one Oracle Real Application Clusters (RAC) instance to another available Oracle RAC instance.
	Draining to move sessions gracefully from one instance to another is used during planned maintenance and load rebalancing. The connection is moved when the application returns the connection to a pool and then obtains a new connection or another rule is satisfied.
- Fail over: Reestablish an equivalent session at a new instance that offers the service.
	Fail over occurs during unplanned outages and during planned maintenance when sessions do not drain within an allotted period of time. The application should not receive errors when Application Continuity is configured.
- Fast Application Notification (FAN): FAN is essential to break clients out of TCP/IP timeouts immediately following failures. FAN notifies clients immediately when resources become available, and initiates draining of database sessions so clients experience no outages during planned maintenance. FAN also includes notifying configuration-level and service-level information that includes changes in service status.
- Oracle Notification Service (ONS): A facility that creates a bridge with middle-tier servers or applications to transport cluster events to application logic for handling or reaction.

Software Recommendations

The following software is recommended for HA Level configurations:

- Oracle Real Application Clusters (Oracle RAC) and Oracle Clusterware (which provides services and infrastructure to efficiently manage outages), preferably with Oracle Grid Infrastructure (GI) release 19c or later
- Oracle Active Data Guard is recommended for protection from database, cluster, storage or site failures
- Oracle Database 19c client and database or a later long-term support version, with the most recent patch level
---
title: Database Development Guide
book: Database Development Guide
doc_id: E96334-10
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/high-availability.html
tags:
  - oracle
  - 19c
  - development-guide
---

## 6 High Availability

This chapter explains how to design high availability into the database and database applications.

Topics:

### 6.1 Transparent Application Failover (TAF)

This section describes what Transparent Application Failover (TAF) is, how to configure TAF, and using TAF callbacks to notify the application of events as they are generated.

Topics:

- About Transparent Application Failover
- Configuring Transparent Application Failover
- Using Transparent Application Failover Callbacks

#### 6.1.1 About Transparent Application Failover

Transparent Application Failover (TAF) is a client-side feature of OCI, OCCI, Java Database Connectivity (JDBC) OCI driver, and ODP.NET designed to minimize disruptions to end-user applications that occur when database connectivity fails because of instance or network failure. TAF can be implemented on a variety of system configurations including Oracle Real Application Clusters (Oracle RAC), Oracle Data Guard physical standby databases, and on a single instance system after it restarts (for example, when repairs are made).

TAF enables client applications to automatically (transparently) reconnect to a preconfigured secondary instance, creating a fresh connection, but identical to the connection that was established on the first original instance. That is, the connection properties are the same as that of the earlier connection, regardless of how the connection was lost. In this case, the active transactions roll back. Also, all statements that an application attempts to use after a failure attempt also failover.

See Also:

- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNOCI16679) for more information about OCI TAF
- [Oracle C++ Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNCPP20011) for more information about OCCI TAF
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC27000) for more information about JDBC TAF
- [Oracle Data Provider for.NET Developer's Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ODPNT-GUID-0A08E9F6-AE33-4AB0-B2D1-31EB263C3544) for more information about ODP.NET TAF
- [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=NETRF279) for more information about client-side configuration of TAF (Connect Data Section)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ARPLS092) for more information about the server-side configuration of TAF (`DBMS_SERVICE`)

#### 6.1.2 Configuring Transparent Application Failover

TAF can be configured on both the client side and server side with the server side taking precedence if both client and server sides are configured. On the client side, you configure TAF by including the `FAILOVER_MODE` parameter in the `CONNECT_DATA` portion of a connect descriptor. On the server side, you configure TAF by modifying the target service with the `DBMS_SERVICE.MODIFY_SERVICE` packaged procedure.

See Also:

- About Transparent Application Failover for more information about configuration

#### 6.1.3 Using Transparent Application Failover Callbacks

TAF callbacks are callbacks that are registered in case of failover and called during failover to notify the application of events as they are generated. They are called several times while reestablishing the user's session.

As the application developer you may want to inform the user that failover is in progress because there is a slight delay as failover proceeds. The first call to the callback carries out that function. Also, when failover is successful and the connection is reestablished, you may want to inform the user that failover has happened and then you may want to replay `ALTER SESSION` commands because these commands are not automatically replayed on the second instance. A subsequent call to the callback performs that function. Also, if failover is unsuccessful, then you want to inform the application that failover cannot occur. A third call to the callback performs this function as well.

Using TAF callbacks makes possible:

- Notifying users of the status of failover throughout the failover process; when failover is underway, when failover is successful, and when failover is unsuccessful
- Replaying of `ALTER SESSION` commands when that is needed
- Reauthenticating a user handle besides the primary handle for each time a session begins on the new connection. Because each user handle represents a server-side session, the client may want to replay `ALTER SESSION` commands for that session.

See Also:

Configuring Transparent Application Failover for specific callback registration information for each interface

### 6.2 Oracle Connection Manager in Traffic Director Mode

This feature allows the Oracle database Connection Manager (CMAN) to be configured in Traffic Director mode to serve clients connecting to different database services, with HA and performance features configurable at the router level, benefiting all the clients connecting..

Oracle Database 18.1 release onwards, Oracle Connection Manager in Traffic Director mode furnishes support for:

- Transparent performance enhancements and connection multiplexing
	- With multiple CMAN in Traffic Director mode instances, applications get increased scalability through client-side connection-time load balancing or with a load balancer (BIG-IP, NGINX, and others)
- Zero application downtime including: planned database maintenance or pluggable database (PDB) relocation and unplanned database outages for read-mostly workloads.
- High Availability of CMAN in Traffic Director mode to avoid a single point of failure.
- Security and isolation: CMAN in Traffic Director mode furnishes:
	- Database Proxy supporting transmission control protocol/transmission control protocol secure (TCP/TCPS) and protocol conversion
		- Firewall based on the IP address, service name, and secure socket layer/transport layer security (SSL/TLS) wallets
		- Tenant isolation in a multi-tenant environment
		- Protection against denial-of-service and fuzzing attacks
		- Secure tunneling of database traffic across Oracle Database on-premises and Oracle Cloud

### 6.3 Fast Application Notification (FAN) and Fast Connection Failover (FCF)

This section describes what Fast Application Notification (FAN) and Fast Connection Failover (FCF) are and how applications can respond to FAN events in a high availability environment and use FCF to relocate connections after a failover.

Topics:

- About Fast Application Notification (FAN)
- About Receiving FAN Event Notifications
- About Fast Connection Failover (FCF)

#### 6.3.1 About Fast Application Notification (FAN)

An important component of high availability is a notification mechanism called Fast Application Notification (FAN). FAN notifies other processes about configuration and service level information that includes service status changes, such as UP or DOWN events. Applications can respond to FAN events and take immediate action. FAN UP and DOWN events can apply to instances, services, and nodes.

FAN provides the ability to immediately terminate an active transaction when an instance or server fails. FAN integrated Oracle clients receive the events and respond. Applications can respond either by propagating the error to the user or by resubmitting the transactions and masking the error from the application user. When a DOWN event occurs, FAN integrated clients immediately clean up connections to the terminated database. When an UP event occurs, the FAN integrated clients create new connections to the new primary database instance.

Oracle has integrated FAN with many of the common Oracle client drivers. Therefore, the easiest way to use FAN is to use one of the following integrated Oracle clients:

- OCI session pools
- Universal Connection Pool for Java
- Thin JDBC Driver (12.2 and later)
- ODP.NET managed and un-managed providers
- All WebLogic server data sources, and Oracle Tuxedo

The overall goal is to enable applications to consistently obtain connections to the available primary database at anytime.

FAN events are published using Oracle Notification Service. The publication mechanisms are automatically configured as part of an Oracle RAC installation. Here, an Oracle RAC installation means any installation of Oracle Clusterware with Oracle RAC, Oracle RAC One Node, Oracle Data Guard (fast-start-failover), or Oracle Data Guard single instance with Oracle Clusterware). Beginning with Oracle Database 12c Release 1 (12.1), ONS is the primary notification mechanism for a new client (Oracle Database 12c Release 1 (12.1)) and a new server (Oracle Database 12c Release 1 (12.1)), while the AQ HA notification feature is deprecated and maintained only or backward compatibility when there is an older OCI or ODP.NET unmanaged client (pre-Oracle Database 12c Release 1 (12.1)) or old server (pre-Oracle Database 12c Release 1 (12.1)).

When you use JDBC or Oracle Database 12 c Release 1 (12.1.0.1) OCI or ODP.NET clients, the Oracle Notification Service is automatically configured using your TNS. When you use OCI-based clients, set HA notifications (`-notification = TRUE`) for your services and set EVENTS in `oraccess.xml`.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=RACAD7128) for more information about FAN
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ADMIN13312) for information about enabling FAN events in an Oracle Restart environment
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNOCI09100) for more information about receiving runtime connection load balancing advisory FAN events to balance application session requests in an Oracle RAC environment with Oracle Clusterware set up and enabled
- [Oracle C++ Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNCPP20028) for more information about runtime load balancing of the stateless connection pool by use of service metrics distributed by the Oracle RAC load-balancing advisory
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC26000) for more information about fast connection failover

#### 6.3.2 About Receiving FAN Event Notifications

Starting from Oracle Database 12c Release 2 (12.2), the Oracle RAC FAN APIs provide an alternative for taking advantage of the high-availability (HA) features of Oracle Database, if you do not use Universal Connection Pool or Oracle WebLogic Server with Active Grid Link (AGL). This feature depends on the Oracle Notification System (ONS) message transport mechanism.

This feature requires configuring your system, servers, and clients to use ONS. For using Oracle RAC Fast Application Notification, the `simplefan.jar` file must be present in the `CLASSPATH`, and either the `ons.jar` file must be present in the `CLASSPATH` or an Oracle Notification Services (ONS) client must be installed and running in the client system.

See Also:

[Oracle Database JDBC Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC-GUID-672941ED-9553-4779-B1AD-7FEBC07603D6) for more information about Oracle RAC FAN APIs.

#### 6.3.3 About Fast Connection Failover (FCF)

In a configuration with a standby database, after you have added Oracle Notification Services (ONS) to your Oracle Restart configurations and enabled Oracle Advanced Queuing (AQ) HA notifications for your services, you can enable clients for Fast Connection Failover (FCF). The clients then receive FAN events and can relocate connections to the current primary database after an Oracle Data Guard failover. Beginning with Oracle Database 12c Release 1 (12.1), ONS is the primary notification mechanism for a new client (Oracle Database 12c Release 1 (12.1)) and a new server (Oracle Database 12c Release 1 (12.1)), while the AQ HA notification feature is deprecated and maintained only for backward compatibility when there is an old client (pre-Oracle Database 12c Release 1 (12.1)) or old server (pre-Oracle Database 12c Release 1 (12.1)).

For databases with no standby database configured, you can still configure the client FAN events. When there is an outage (planned or unplanned), you can configure the client to retry the connection to the database. Because Oracle Restart restarts the failed database, the client can reconnect when the database restarts.

You must enable FAN events to provide FAN integrated clients support for FCF in an Oracle Data Guard or standalone environment with no standby database.

FCF offers a driver-independent way for your Java Database Connectivity (JDBC) application to take advantage of the connection failover facilities offered by Oracle Database. FCF is integrated with Universal Connection Pool (UCP) and Oracle RAC to provide high availability event notification.

OCI clients can enable FCF by registering to receive notifications about Oracle Restart high availability FAN events and respond when events occur. This improves the session failover response time in OCI and removes terminated connections from connection and session pools. This feature works on OCI applications, including those that use Transparent Application Failover (TAF), connection pools, or session pools.

See Also:

- [Oracle C++ Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNCPP20028) for more information about runtime load balancing of the stateless connection pool by use of service metrics distributed by the Oracle RAC load-balancing advisory
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC26000) for more information about fast connection failover
- [Oracle Universal Connection Pool for JDBC Java API Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJUAR)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ADMIN13194) for information about enabling FCF for JDBC clients
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ADMIN13195) for information about enabling FCF for OCI clients
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=ADMIN13196) for information about enabling FCF for ODP.NET clients

### 6.4 Application Continuity and Transaction Guard

Application Continuity is a DBA feature for failover. Transaction Guard is a developer feature for coding failover yourself.

In Oracle high availability framework, JDBC clients, OCI clients, and ODP.NET clients support fast application notification (FAN) messages. FAN is designed to quickly notify an application of outages at the node, database, instance, service, and public network levels. After being notified of the failure, an application can reestablish the failed connection on a surviving instance.

Application Continuity is transparent to the application. This functionality is provided by the Oracle Database 12c and the Oracle drivers. It is enabled by setting attributes on the database service.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=RACAD-GUID-BD699AEB-9F85-42A8-8687-5A979918938D) for more information about Application Continuity
- [Using Transaction Guard](transaction-guard.md) for more information about Transaction Guard
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNOCI80660) for more information about OCI, Transaction Guard, and Application Continuity
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC27000) for more information about JDBC, Transaction Guard, and Application Continuity

#### 6.4.1 Overview of Application Continuity

Application Continuity masks planned or unplanned outages (that cause database session unavailability) by attempting to rebuild the database session transactional and non-transactional states, so the outage appears to the user as no more than a delayed execution.

Application Continuity works with the Oracle Database 12c and later server to determine if the database session can be replayed. When a recoverable error occurs that makes the database session unavailable, an error message is sent back to the application. A driver receives the FAN message (down or interrupt) and aborts the dead session.

If the last submission has replay enabled, the `12c` driver prepares to replay the submission and replays the saved statements for the request. Application Continuity prepares replay by using Transaction Guard to determine the outcome of the last operation submitted by the session that received the error. If the submission committed and completed, the new session returns this result to the application and continues with the nontransactional state established if the `SESSION_STATE_CONSISTENCY` mode is `STATIC`, or exits if the `SESSION_STATE_CONSISTENCY` mode is `DYNAMIC`. `DYNAMIC` session state consistency is appropriate for most applications.

If `FAILOVER_RESTORE` is `LEVEL1` or a callback has been set, the client (JDBC replay driver, ODP.NET or OCI) initializes the connection to restore initial nontransactional session state (NTSS). When replaying, preserved mutable data are restored if permission has been granted. Validation is performed at the server to ensure that the client-visible results are identical to the original submission. When replay is complete, the application proceeds with its application logic returning to runtime mode as if all that occurred was a delay in execution similar to that which happens under load.

In some cases, replay cannot restore the data that the client potentially made decisions upon. The replay then returns the original error to the application and appears like a delayed error.

Application Continuity supports recovering any outage that is due to database unavailability against a copy of a database with the same DBID (forward in time) or within an Active Data Guard farm. This may be Oracle RAC One, Oracle Real Application Clusters, within an Active Data Guard, Multitenant using PDB relocate with a RAC or across RACs or across to Active Data Guard (ADG).

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=RACAD-GUID-BD699AEB-9F85-42A8-8687-5A979918938D) for more information about Application Continuity

#### 6.4.2 Overview of Transaction Guard

Transaction Guard is a reliable protocol and interface that returns the commit outcome of the current in-flight transaction when an error, or a time-out is returned to the client. Applications can leverage the Transaction Guard interface to code graceful recoverable error handling. Providing unambiguous message during an outage greatly improves the user experience.

Transaction Guard introduces the concept of at-most-once transaction semantics, also referred to as transaction idempotence. When an application opens a connection to the database using this service, the logical transaction ID (LTXID) is generated at authentication and stored in the session handle at the database and a copy at the client driver. This is a globally unique ID that identifies the database transaction from the application perspective. Applications use the Transaction Guard interface to obtain a known commit outcome following a recoverable error.

When there is an outage, an application using Transaction Guard can retrieve the LTXID from the previous failed session's handle and use it to determine the outcome of the transaction that was active prior to the session failure. If the LTXID is determined to be `UNCOMMITTED`, then the application can return the `UNCOMMITTED` outcome to the user to decide what action to take, or optionally, the application can replay an uncommitted transaction. If the LTXID is determined to be `COMMITTED`, then the transaction is committed and the application can return this outcome to the end user and might be able to take a new connection and continue. Transaction Guard also reports whether the last user call not only `COMMITTED`, but also whether it completed changing needed non-transactional states - see `USER_CALL_COMPLETED`.

See Also:

[Using Transaction Guard](transaction-guard.md)

### 6.5 Service and Load Management for Database Clouds

Topics:

About Service and Load Management for Database Clouds

#### 6.5.1 About Service and Load Management for Database Clouds

The database cloud is a self-contained system of databases integrated by the service and load management framework that ensures high performance, availability and optimal utilization of resources. This framework provides effective balancing of processing workload across distributed databases that maintain multiple synchronized replicas both locally and in geographically disparate regional data centers. Replicas may be instances in an Oracle RAC environment, or single instances interconnected using Oracle Data Guard, Oracle Golden Gate, or any combination that supports replication technology. Thus, the service and load management framework provides dynamic load balancing, failover, and centralized service management for these replicated databases.

A global service is a database service provided by multiple databases synchronized through some form of data replication that satisfies quality of service requirements for the service. This allows a client request for a service to be forwarded to any database that provides that service.

A database pool within a database cloud consists of all databases that provide the same global service that belong to the same administrative domain. The database cloud is partitioned into multiple database pools to simplify service management and to provide higher levels of security by allowing each pool to be administered by a different administrator.

A global service manager (GSM) is a software component that provides service-level load balancing and centralized management of services within the database cloud. Load balancing is done at connection and runtime. Other capabilities provided by GSM include creation, configuration, starting, stopping, and relocation of services and maintaining global service properties such as cardinality and region locality. A region is a logical boundary known as a data center that contains database clients and servers that are considered close enough to each other so as to reduce network latency to levels required by applications accessing these data centers.

The GSM can run on a separate host, or can be colocated with a database instance. Every region must have at least one GSM instance running. For high availability, Oracle recommends that you deploy multiple GSM instances in a region. A GSM instance belongs to only one particular region; however, it manages global services in all database pools associated with this region.

From an application developer's perspective, a client program connects to a regional global service manager (GSM) and requests a connection to a global service. The client need not specify which database or instance it requires. GSM forwards the client's request to the optimal instance within a database pool in the database cloud that offers the service.

Beginning with Oracle Database 12c Release 1 (12.1.0.1), the DBA can configure client-side connect strings for database services in a Global Data Services (GDS) framework using an Oracle Net string.

Introduced in Oracle Database 12c Release 1 (12.1.0.1), the logical transaction ID (LTXID) is initially generated at authentication and stored in the session handle and used to identify a database transaction from the application perspective. The logical transaction ID is globally unique and identifies the transaction within a highly available (HA) infrastructure.

Using the HA Framework, a client application (JDBC, OCI, and ODP.NET) supports fast application notification (FAN) messages. FAN is designed to quickly notify an application of outages at the node, database, instance, service, and public network levels. After being notified of the outage, an application can reestablish the failed connection on a surviving instance.

Beginning with Oracle Database 12c Release 1 (12.1.0.1), the DBA can configure server-side settings for the database services used by the applications to support Application Continuity for Java and Transaction Guard.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=CNCPT89330) for an overview of global service management and description of the physical and logical components of the service and load management framework
- [Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=GSMUG107) for more information about global service management in a database cloud
- [Oracle Database Global Data Services Concepts and Administration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=GSMUG650) for more information about configuring database clients for connectivity to the Global Data Services (GDS) framework.
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=LNOCI72990) for more information about OCI, Application Continuity, and Transaction Guard
- [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=JJDBC27000) for more information about JDBC, Application Continuity, and Transaction Guard
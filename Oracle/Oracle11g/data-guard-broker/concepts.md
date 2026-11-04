---
title: Oracle Data Guard Broker Concepts
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/concepts.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 1 Oracle Data Guard Broker Concepts

This chapter describes the Oracle Data Guard broker, its architecture and components, and how it automates the creation, control, and monitoring of a Data Guard configuration. The following topics are discussed:

See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/standby.htm#SBYDB00100) for the definition of a Data Guard configuration and for complete information about Oracle Data Guard concepts and terminology.

## 1.1 Overview of Oracle Data Guard and the Broker

Oracle Data Guard ensures high availability, data protection, and disaster recovery for enterprise data. Data Guard provides a comprehensive set of services that create, maintain, manage, and monitor one or more standby databases to enable production Oracle databases to survive disasters and data corruptions. Data Guard maintains these standby databases as transactionally consistent copies of the primary database. If the primary database becomes unavailable because of a planned or an unplanned outage, Data Guard can switch any standby database to the production role, thus minimizing the downtime associated with the outage. Data Guard can be used with traditional backup, recovery, and cluster techniques, as well as the Flashback Database feature to provide a high level of data protection and data availability.

### 1.1.1 Data Guard Configurations and Broker Configurations

A Data Guard configuration consists of one primary database and up to thirty standby databases. The databases in a Data Guard configuration are connected by Oracle Net and may be dispersed geographically. There are no restrictions on where the databases are located as long as they can communicate with each other. For example, you can have a standby database on the same system as the primary database, along with two standby databases on another system.

The Data Guard broker logically groups these primary and standby databases into a broker configuration that allows the broker to manage and monitor them together as an integrated unit. You can manage a broker configuration using either the Oracle Enterprise Manager graphical user interface or the Data Guard command-line interface.

### 1.1.2 Oracle Data Guard Broker

The Oracle Data Guard broker is a distributed management framework that automates and centralizes the creation, maintenance, and monitoring of Data Guard configurations. The following list describes some of the operations the broker automates and simplifies:

- Creating Data Guard configurations that incorporate a primary database, a new or existing (physical, logical, or snapshot) standby database, redo transport services, and log apply services, where any of the databases could be Oracle Real Application Clusters (Oracle RAC) databases.
- Adding additional new or existing (physical, snapshot, logical, Oracle RAC or non-Oracle RAC) standby databases to an existing Data Guard configuration, for a total of one primary database, and from 1 to 30 standby databases in the same configuration.
- Managing an entire Data Guard configuration, including all databases, redo transport services, and log apply services, through a client connection to any database in the configuration.
- Managing the protection mode for the broker configuration.
- Invoking switchover or failover with a single command to initiate and control complex role changes across all databases in the configuration.
- Configuring failover to occur automatically upon loss of the primary database, increasing availability without manual intervention.
- Monitoring the status of the entire configuration, capturing diagnostic information, reporting statistics such as the Redo Apply rate and the redo generation rate, and detecting problems quickly with centralized monitoring, testing, and performance tools.

You can perform all management operations locally or remotely through the broker's easy-to-use interfaces: the Data Guard management pages in Oracle Enterprise Manager, which is the broker's graphical user interface (GUI), and the Data Guard command-line interface called DGMGRL.

These interfaces simplify the configuration and management of a Data Guard configuration. Table 1-1 provides a comparison of configuration management using the broker's interfaces and using SQL\*Plus.

Table 1-1 Configuration Management With and Without the Broker

|  | With the Broker | Without the Broker |
| --- | --- | --- |
| General | Provides primary and standby database management as one unified configuration. | You must manage the primary and standby databases separately. |
| Standby Database Creation | Provides the Enterprise Manager wizards that automate and simplify the steps required to create a configuration with an Oracle database on each site, including creating the standby control file, online redo log files, datafiles, and server parameter files. | You must manually (using RMAN or other tools):  - Copy the database files to the standby database system. - Create a control file on the standby database system. - Create server parameter or initialization parameter files on the standby database system. - Copy the primary database password file to the standby database system. |
| Configuration and Management | Enables you to configure and manage multiple databases from a single location and automatically unifies all of the databases in the broker configuration. | You must manually:  - Set up redo transport services and log apply services on each database in the configuration. - Manage the primary database and standby databases individually. |
| Control | - Automatically sets up redo transport services and log apply services. Simplifies management of these services, especially in an Oracle RAC environment. - Simplifies switchovers, failovers, reinstatements, and conversions to and from a snapshot standby database, allowing you to invoke them through a single command. - Automates failover by allowing the broker to determine if failover is necessary and to initiate failover to a specified target standby database, with no need for DBA intervention and with either no loss of data or with a configurable amount of data loss. - Integrates role changes with Oracle Clusterware. - Manageable and monitorable through Enterprise Manager Grid Control | You must manually:  - Use multiple SQL statements to manage the database. - Coordinate sequences of multiple commands across multiple database sites to execute switchover and failover operations. - Coordinate sequences of multiple commands to manage services and instances during role transitions. |
| Monitoring | - Provides continuous monitoring of the configuration health, database health, and other runtime parameters. - Provides a unified updated status and detailed reports. - Provides integration with Oracle Enterprise Manager events. | You must manually:  - Monitor the status and runtime parameters using fixed views on each database—there is no unified view of status for all of the databases in the configuration. - Provide a custom method for monitoring Oracle Enterprise Manager events. |

## 1.2 Benefits of Data Guard Broker

The broker's interfaces improve usability and centralize management and monitoring of the Data Guard configuration. Available as a feature of the Enterprise Edition and Personal Edition of the Oracle database, the broker is also integrated with the Oracle database and Oracle Enterprise Manager. These broker attributes result in the following benefits:

Disaster protection: By automating many of the manual tasks required to configure and monitor a Data Guard configuration, the broker enhances the high availability, data protection, and disaster protection capabilities that are inherent in Oracle Data Guard. Access is possible through a client to any system in the Data Guard configuration, eliminating any single point of failure. If the primary database fails, the broker automates the process for any one of the standby databases to replace the primary database and take over production processing. The database availability that Data Guard provides makes it easier to protect your data.

Higher availability and scalability with Oracle Real Application Clusters (Oracle RAC) Databases: While Oracle Data Guard broker enhances disaster protection by maintaining transactionally consistent copies of the primary database, Data Guard, configured with Oracle high availability solutions such as Oracle Real Application Clusters (Oracle RAC) databases, further enhances the availability and scalability of any given copy of that database. The intrasite high availability of an Oracle RAC database complements the intersite protection that is provided by Data Guard broker.

Consider that you have a cluster system hosting a primary Oracle RAC database comprised of multiple instances sharing access to that database. Further consider that an unplanned failure has occurred. From a Data Guard broker perspective, the primary database remains available as long as at least one instance of the clustered database continues to be available for transporting redo data to the standby databases. Oracle Clusterware manages the availability of instances of an Oracle RAC database. It works to rapidly recover failed instances to keep the primary database available. If Oracle Clusterware is unable to recover a failed instance, the broker continues to run automatically with one less instance. If the last instance of the primary database fails, the broker provides a way to fail over to a specified standby database. If the last instance of the primary database fails, and fast-start failover is enabled, the broker can continue to provide high availability by automatically failing over to a pre-determined standby database.

The broker is integrated with Oracle Clusterware so that database role changes occur smoothly and seamlessly. This is especially apparent in the case of a planned role switchover (for example, when a physical standby database is directed to take over the primary role while the former primary database assumes the role of standby). The broker and Oracle Clusterware work together to temporarily suspend service availability on the primary database, accomplish the actual role change for both databases during which Oracle Clusterware works with the broker to properly restart the instances as necessary on the old primary database, and then start services defined on the new primary database. The broker manages the underlying Data Guard configuration and its database roles while Oracle Clusterware manages service availability that depends upon those roles. Applications that rely on Oracle Clusterware for managing service availability will see only a temporary suspension of service as the role change occurs in the Data Guard configuration.

Note that while Oracle Clusterware helps to maintain the availability of the individual instances of an Oracle RAC database, the broker coordinates actions that maintain one or more physical or logical copies of the database across multiple geographically dispersed locations to provide disaster protection. Together, the broker and Oracle Clusterware provide a strong foundation for Oracle's high-availability architecture.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about Oracle Clusterware

Automated creation of a Data Guard configuration: The broker helps you to logically define and create a Data Guard configuration consisting of a primary database and (physical or logical, snapshot, Oracle RAC or non-Oracle RAC) standby databases. The broker automatically communicates between the databases in a Data Guard configuration using Oracle Net Services. The databases can be local or remote, connected by a LAN or geographically dispersed over a WAN.

Oracle Enterprise Manager provides a wizard that automates the complex tasks involved in creating a broker configuration, including:

- Adding an existing standby database, or a new standby database created from existing backups taken through Enterprise Manager
- Configuring the standby control file, server parameter file, and datafiles
- Initializing communication with the standby databases
- Creating standby redo log files
- Enabling Flashback Database if you plan to use fast-start failover

Although DGMGRL cannot automatically create a new standby database, you can use DGMGRL commands to configure and monitor an existing standby database, including those created using Enterprise Manager.

Easy configuration of additional standby databases: After you create a Data Guard configuration consisting of a primary and a standby database, you can add up to 29 new or existing, physical, snapshot, or logical standby databases to each Data Guard configuration. Oracle Enterprise Manager provides an Add Standby Database wizard to guide you through the process of adding more databases.

Simplified, centralized, and extended management: You can issue commands to manage many aspects of the broker configuration. These include:

- Simplify the management of all components of the configuration, including the primary and standby databases, redo transport services, and log apply services.
- Coordinate database state transitions and update database properties dynamically with the broker recording the changes in a broker configuration file that includes profiles of all the databases in the configuration. The broker propagates the changes to all databases in the configuration and their server parameter files.
- Simplify the control of the configuration protection modes (to maximize protection, to maximize availability, or to maximize performance).
- Invoke the Enterprise Manager verify operation to ensure that redo transport services and log apply services are configured and functioning properly.

Simplified switchover and failover operations: The broker simplifies switchovers and failovers by allowing you to invoke them using a single key click in Oracle Enterprise Manager or a single command at the DGMGRL command-line interface (referred to in this documentation as manual failover). For lights-out administration, you can enable fast-start failover to allow the broker to determine if a failover is necessary and to initiate the failover to a pre-specified target standby database automatically, with no need for DBA intervention. Fast-start failover can be configured to occur with no data loss or with a configurable amount of data loss.

Fast-start failover allows you to increase availability with less need for manual intervention, thereby reducing management costs. Manual failover gives you control over exactly when a failover occurs and to which target standby database. Regardless of the method you choose, the broker coordinates the role transition on all databases in the configuration. Once failover is complete, the broker publishes a Fast Application Notification (FAN) event to notify applications that the new primary is available.

Note that you can use the `DBMS_DG` PL/SQL package to enable an application to initiate a fast-start failover when it encounters specific conditions. See [Section 4.7.3](dbresource.md) for more information.

Only one command is required to initiate complex role changes for switchover or failover operations across all databases in the configuration. The broker automates switchover and failover to a specified standby database in the broker configuration. Enterprise Manager enables you to select a new primary database from a set of viable standby databases (enabled and running, with normal status). The DGMGRL `SWITCHOVER` and `FAILOVER` commands only require you to specify the target standby database before automatically initiating and completing the many steps in switchover or failover operations across the multiple databases in the configuration.

Built-in monitoring and alert and control mechanisms: The broker provides built-in validation that monitors the health of all of the databases in the configuration. While connected to any database in the configuration, you can capture diagnostic information and detect obvious and subtle problems quickly with centralized monitoring, testing, and performance tools. Both Enterprise Manager and DGMGRL retrieve a complete configuration view of the progress of redo transport services on the primary database and the progress of Redo Apply or SQL Apply on the standby database.

The ability to monitor local and remote databases and respond to events is significantly enhanced by the broker's health check mechanism and tight integration with the Oracle Enterprise Manager event management system.

Transparent to application: Use of the broker is possible for any database because the broker works transparently with applications; no application code changes are required to accommodate a configuration that you manage with the broker.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for a complete description of the discrete steps that comprise the creation of standby databases and the other monitoring and control operations that have been automated or simplified by the broker

## 1.3 Data Guard Broker Management Model

The broker simplifies the management of a Data Guard environment by performing operations on the following logical objects:

- Configuration of databases
- A single database

The broker supports one or more Data Guard configurations, each of which includes a profile for the primary database and each standby database. A supported broker configuration consists of:

- A configuration object, which is a named collection of database profiles. A database profile is a description of a database object including its current state, current status, and properties. The configuration object profiles one primary database and its standby databases that can include a mix of physical, snapshot, and logical standby databases. The databases of a given configuration are typically distributed across multiple host systems.
- Database objects, corresponding to primary or standby databases. The broker uses a database object's profile to manage and control the state of a single database on a given system. The database object may be comprised of one or more instance objects if this is an Oracle RAC database.
- Instance objects. The broker treats a database as a collection of one or more named instances. The broker automatically discovers the instances and associates them with their database.

Figure 1-1 shows the relationship of these objects.

Figure 1-1 Relationship of Objects Managed by the Data Guard Broker

![Figure 1-1 Relationship of Objects Managed by the Data Guard Broker](img/dgbkr006.gif)

> This figure shows the hierarchy of components in a Data Guard broker configuration. In the figure, a rectangle representing the broker configuration contains one primary database and (up to) thirty standby databases. Each database may consist of one or more instances if it is a RAC database.
>
> [Copyright © 1999, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

See also:

[Chapter 3](configure.md), [Chapter 4](dbresource.md), and [Chapter 5](sofo.md) for more information about managing configuration and database objects

## 1.4 Data Guard Broker Components

The Oracle Data Guard broker consists of the following components:

- Oracle Enterprise Manager
- Data Guard Command-Line Interface (DGMGRL)
- Data Guard Monitor

Oracle Enterprise Manager and the Data Guard command-line interface (DGMGRL) are the broker client interfaces that help you define and manage a configuration consisting of a collection of primary and standby databases. DGMGRL also includes commands to create an observer, a process that facilitates fast-start failover. Section 1.5 describes these interfaces in more detail.

The Data Guard monitor is the broker server-side component that is integrated with the Oracle database. Data Guard monitor is composed of several processes, including the DMON process, and broker configuration files that allow you to control the databases of that configuration, modify their behavior at runtime, monitor the overall health of the configuration, and provide notification of other operational characteristics. Section 1.6 describes the Data Guard monitor in more detail.

Figure 1-2 shows these components of the broker.

Figure 1-2 Oracle Data Guard Broker

![Figure 1-2 Oracle Data Guard Broker](img/dgbkr008.gif)

> This figure shows the components of the broker architecture. On the client side, the broker architecture features two user interfaces: the Oracle Enterprise Manager GUI and the Data Guard command-line interface (DGMGRL). On the server side, the figure shows the Data Guard monitor which is implemented through the Data Guard monitor (DMON) process and the Data Guard configuration file. These components are described in more detail in the following sections.
  

## 1.5 Data Guard Broker User Interfaces

You can use either of the broker's user interfaces to create a broker configuration and to control and monitor the configuration. The following sections describe the broker's user interfaces:

- Oracle Enterprise Manager
- Data Guard Command-Line Interface (DGMGRL)

### 1.5.1 Oracle Enterprise Manager

Oracle Enterprise Manager works with the Data Guard monitor to automate and simplify the management of a Data Guard configuration.

With Enterprise Manager, the complex operations of creating and managing standby databases are simplified through Data Guard management pages and wizards, including:

- An Add Standby Database wizard that helps you to create a broker configuration, if one does not already exist, having a primary database and a local or remote standby database. The wizard can create a physical, snapshot, or logical standby database or import an existing physical, snapshot, or logical (Oracle RAC or non-Oracle RAC) standby database. If the wizard creates a physical, snapshot, or logical standby database, the wizard also automates the creation of the standby control file, server parameter file, online and standby redo log files, and the standby datafiles.
- A switchover operation that helps you switch roles between the primary database and a standby database.
- A failover operation that changes one of the standby databases to the role of a primary database.
- Performance tools and graphs that help you monitor and tune redo transport services and log apply services.
- Property pages that allow you to set database properties on any database and, if applicable, the settings are immediately propagated to all other databases and server parameter files in the configuration.
- Event reporting through e-mail.

In addition, it makes all Oracle Net Services configuration changes necessary to support redo transport services and log apply services.

See Also:

My Oracle Support note 787461.1 at `http://support.oracle.com` for information about which versions of Enterprise Manager Grid Control are required to manage the full set of Data Guard features in various Oracle Database releases

### 1.5.2 Data Guard Command-Line Interface (DGMGRL)

The Data Guard command-line interface (DGMGRL) enables you to control and monitor a Data Guard configuration from the DGMGRL prompt or within scripts. You can perform most of the activities required to manage and monitor the databases in the configuration using DGMGRL commands.

DGMGRL also includes commands to create an observer process that continuously monitors the primary and target standby databases and evaluates whether failover is necessary, and then initiates a fast-start failover when conditions warrant.

See Also:

[Chapter 7](dgmgrl.md) for complete reference information for the Data Guard command-line interface. [Table 7-1](dgmgrl.md) provides a summary of DGMGRL commands.

## 1.6 Data Guard Monitor

The configuration, control, and monitoring functions of the broker are implemented by server-side software and configuration files that are maintained for each database that the broker manages. The software is called the Data Guard monitor.

The following sections describe how the Data Guard monitor interacts with the Oracle database and with remote Data Guard monitors to manage the broker configuration.

### 1.6.1 Data Guard Monitor (DMON) Process

The Data Guard monitor process (DMON) is an Oracle background process that runs for every database instance that is managed by the broker. When you start the Data Guard broker, a DMON process is created.

See Also:

[Section 3.3](configure.md) for information on starting the broker

Whether you use Oracle Enterprise Manager or DGMGRL to manage a database, the DMON process is the server-side component that interacts with the local database and the DMON processes of the other databases to perform the requested function. The DMON process is also responsible for monitoring the health of the broker configuration and for ensuring that every database has a consistent description of the configuration.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about the memory structures and processes that are used with an Oracle database

Figure 1-3 shows the broker's DMON process as one of several background processes that constitute an instance of the Oracle database. Each database instance shown in the figure has its own DMON process.

Figure 1-3 Databases With Broker (DMON) Processes

![Figure 1-3 Databases With Broker (DMON) Processes](img/dgbkr003.gif)

> This figure emphasizes the discussion in the surrounding text that describes the DMON process as one of many Oracle background processes. The top half of the figure shows a primary database on which the Oracle database is interacting with the DMON process and many other background processes such as the Recoverer (RECO), Process Monitor (PMON), System Monitor (SMON), Database Writer (DBW0), Log Writer (LGWR), and the Archiver (ARC0). An elliptical series of dots indicates that the number of processes continues beyond the ones shown in this figure.
>
> The bottom half of the figure represents the standby database as a mirror image of the primary database, showing that there is a DMON process on the standby database along with a series of Oracle database processes as shown on the primary database.
>
> The figure also shows that two-way communication occurs between the DMON processes on the primary and standby databases over the Oracle Net communication channel.
  

The zigzag arrow in the center of Figure 1-3 represents the two-way Oracle Net Services communication channel that exists between the DMON processes of two databases in the same broker configuration.

This two-way communication channel is used to pass requests between databases and to monitor the health of all of the databases in the broker configuration.

### 1.6.2 Configuration Management

The broker's DMON process persistently maintains profiles about all database objects in the broker configuration in a binary configuration file. A copy of this file is maintained by the DMON process for each of the databases that belong to the broker configuration. If it is an Oracle RAC database, each database's copy of the file is shared by all instances of the database.

This configuration file contains profiles that describe the states and properties of the databases in the configuration. For example, the file records the databases that are part of the configuration, the roles and properties of each of the databases, and the state of each database in the configuration.

The configuration data is managed transparently by the DMON process to ensure that the configuration information is kept consistent across all of the databases. The broker uses the data in the configuration file to configure and start the databases, control each database's behavior, and provide information to DGMGRL and Oracle Enterprise Manager.

See Also:

[Section 4.3](dbresource.md) for more information

Whenever you add databases to a broker configuration, or make a change to an existing database's properties, each DMON process records the new information in its copy of the configuration file.

### 1.6.3 Database Property Management

Associated with each database are various properties that the DMON process uses to control the database's behavior. The properties are recorded in the configuration file as a part of the database's object profile that is stored there. Many database properties are used to control database initialization parameters related to the Data Guard environment.

To ensure that the broker can update the values of parameters in both the database itself and in the configuration file, you must use a server parameter file to control static and dynamic initialization parameters. The use of a server parameter file gives the broker a mechanism that allows it to reconcile property values selected by the database administrator (DBA) when using the broker with any related initialization parameter values recorded in the server parameter file.

When you set values for database properties in the broker configuration, the broker records the change in the configuration file and propagates the change to all of the databases in the Data Guard configuration.

Note:

The broker supports both the default and nondefault server parameter file filenames. If you use a nondefault server parameter filename, the initialization parameter file must include the complete filename and location of the server parameter file. If this is an Oracle RAC database, there must be one nondefault server parameter file for all instances.

See Also:

[Section 4.3.2](dbresource.md) for more information
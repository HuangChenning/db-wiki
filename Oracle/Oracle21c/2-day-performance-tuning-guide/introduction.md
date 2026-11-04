---
title: "2 Day + Performance Tuning Guide"
book: "2 Day + Performance Tuning Guide"
doc_id: F32092-02
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tdppt/introduction.html
tags:
  - oracle
  - 21c
  - 2-day-performance-tuning-guide
---

As an Oracle database administrator (DBA), you are responsible for the performance of your Oracle database. Tuning a database to reach a desirable performance level may be a daunting task, especially for DBAs who are new to Oracle Database. Oracle Database 2 Day + Performance Tuning Guide is a quick start guide that describes how to perform day-to-day database performance tuning tasks using features provided by Oracle Diagnostics Pack, Oracle Tuning Pack, and Oracle Enterprise Manager Cloud Control (Cloud Control).

This chapter contains the following sections:

### About This Guide

Before using this guide, you must do the following:

- Be familiar with Oracle Database administration. See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=ADMIN-GUID-EA8CC987-EF18-4434-B962-01312CD3A8AC) for more information.
- Obtain the necessary products and tools described in " Tools for Tuning the Database ".

Oracle Database 2 Day + Performance Tuning Guide is task-oriented. The objective is to describe why and when tuning tasks need to be performed.

This guide is not an exhaustive discussion of all Oracle Database concepts. For that type of information, see [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=CNCPT001).

This guide does not describe basic Oracle Database administrative tasks. For that type of information, see [Oracle Database Administrator's Guide.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=ADMIN11020)

The primary interface used in this guide is the Enterprise Manager Cloud Control console. This guide is not an exhaustive discussion of all Oracle Database performance tuning features. It does not cover available application programming interfaces (APIs) that provide comparable tuning options to those presented in this guide. For this type of information, see [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA) and [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGSQL).

### Common Oracle DBA Tasks

As an Oracle DBA, you can expect to be involved in the following tasks:

- Installing Oracle software
- Creating Oracle databases
- Upgrading the database software to new releases
- Starting up and shutting down the database
- Managing the storage structures of the database
- Managing user accounts and security
- Managing schema objects, such as tables, indexes, and views
- Making database backups and performing database recovery, when necessary
- Monitoring proactively the condition of the database and taking preventive or corrective actions, as required
- Monitoring and tuning database performance

This guide describes how to accomplish the last two tasks in the preceding list.

### Tools for Tuning the Database

The intent of this guide is to allow you to quickly and efficiently tune and optimize the performance of Oracle Database.

To achieve the goals of this guide, you must acquire the following products, tools, features, and utilities:

- Oracle Database 19c, Version 19.1 (Enterprise Edition)
	Oracle Database offers enterprise-class performance, scalability and reliability on clustered and single-server configurations. It includes many performance features that are used in this guide.
- Oracle Enterprise Manager Cloud Control
	The primary tool to manage the database is Enterprise Manager Cloud Control (Cloud Control), a web-based interface. After you install the Oracle software, create or upgrade a database, and configure the network, you can use Cloud Control to manage the database. In addition, Cloud Control provides an interface for performance advisors and for database utilities, such as SQL\*Loader and Recovery Manager (RMAN).
- Oracle Diagnostics Pack
	Oracle Diagnostics Pack offers a complete, cost-effective, and easy-to-use solution to manage the performance of Oracle Database environments by providing unique features, such as automatic identification of performance bottlenecks, guided problem resolution, and comprehensive system monitoring. Key features of Oracle Diagnostics Pack used in this guide include Automatic Workload Repository (AWR), Automatic Database Diagnostic Monitor (ADDM), and Active Session History (ASH).
- Oracle Tuning Pack
	Oracle Tuning Pack automates the database application tuning process, thereby significantly lowering database management costs while enhancing performance and reliability. Key features of Oracle Tuning Pack that are used in this guide include the following:
	- SQL Tuning Advisor
		This feature enables you to submit one or more SQL statements as input and receive output in the form of specific advice or recommendations for how to tune statements, along with a rationale for each recommendation and its expected benefit. A recommendation relates to collection of statistics on objects, creation of new indexes, restructuring of the SQL statements, or creation of SQL profiles.
		- SQL Access Advisor
		This feature enables you to optimize data access paths of SQL queries by recommending the proper set of materialized views and view logs, indexes, and partitions for a given SQL workload.
- Oracle Real Application Testing
	Oracle Real Application Testing consists of the following key features:
	- Database Replay
		This feature enables you to capture the database workload on a production system, and replay it on a test system with the exact same timing and concurrency as the production system on the same or later release of Oracle Database.
		- SQL Performance Analyzer
		This feature enables you to assess the effect of system changes on SQL performance by identifying SQL statements that have regressed, improved, or remained unchanged.
	See Also:
	[Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=RATUG101) for information about how to use the features Database Replay and SQL Performance Analyzer

Note:

Some of the products and tools in the preceding list, including Oracle Diagnostics Pack and Oracle Tuning Pack, require separate licenses. For more information, see [Oracle Database Licensing Information](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=DBLIC-GUID-B6113390-9586-46D7-9008-DCC9EDA45AB4).

### Accessing the Database Home Page

The Database Home page is the main database management page in Oracle Enterprise Manager Cloud Control (Cloud Control). After you log in to Cloud Control, you navigate to the Database Home page for the target database you want to manage in Cloud Control.

To access the Database Home page in Cloud Control:

1. Start Cloud Control.
	The URL for accessing Cloud Control has the following syntax:
	`http://` `hostname.domain:portnumber` `/em`
2. In the Welcome page, enter your Cloud Control user name and password, and then click Login.
3. From the Targets drop-down menu, select Databases.
	The Databases page appears with a list of the available target databases.
4. Select the database that you want to observe or modify from the Databases page.
	If the list of databases is long, use the Search functionality.
	The home page for the target database appears. The first time that you select an option from some of the menus, such as the Performance menu, the Database Login page appears.
5. In the login page for the target database, log in as a user with the appropriate privileges. For example, to log in as user `SYS` with the `SYSDBA` privilege:
	- User Name: Enter `SYS`.
	- Password: Enter the password for the `SYS` user.
	- Connect As: From the Role list, select SYSDBA.
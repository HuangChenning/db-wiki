---
title: Frequently Asked Questions About Installation
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/app_faq.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## D Frequently Asked Questions About Installation

Use the following guidelines to decide how to install Oracle Database Client components:

## D.1 Installing Oracle Database or Oracle Database Client

The following are frequently asked questions about installing Oracle Database Client:

- I only need one instance of Oracle Database or I just want to install a test database to get familiar with the product. How do I install Oracle Database for these situations?
- How can I create an Oracle database that can handle transaction-heavy or data warehousing applications?
- What's the best way to install multiple Oracle databases?
- How do I configure client connections to an Oracle database?
- What is the best way to install Oracle Database Client if my client nodes have limited disk space?
- How do I upgrade Oracle Database?
- The computers at my site have been configured to run as a cluster. How should I install Oracle Database?
- How do I migrate my non-Oracle databases to Oracle Database?

I only need one instance of Oracle Database or I just want to install a test database to get familiar with the product. How do I install Oracle Database for these situations?

- If you want a quick installation using the default installation settings, then refer to the platform-specific Oracle Database Quick Installation Guide.
- If your site has special requirements, then refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information.

How can I create an Oracle database that can handle transaction-heavy or data warehousing applications?

If you want to create a starter database designed for transaction-heavy or data warehousing applications, then refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more details. Select the Advanced Installation method, and then select the database type you want on the Select Database Configuration screen.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) after installation

Alternatively, you can install Oracle OLAP during the Oracle Database installation. Oracle OLAP provides optimal support for database environments that must meet OLAP requirements. To do so, in the Select Database Edition screen, select Enterprise Edition. Click the Select Options button, and from the Choose Components screen, select Oracle OLAP.

See Also:

- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm)
- [Oracle OLAP DML Reference](https://docs.oracle.com/cd/E11882_01/olap.112/e17122/toc.htm)
- [Oracle OLAP Java API Reference](https://docs.oracle.com/cd/E11882_01/olap.112/e10794/toc.htm)

What's the best way to install multiple Oracle databases?

Use [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to install Oracle Database using either of the following methods:

- Installing with response files: This method lets you run Oracle Universal Installer at a command line using a response file that contains settings specific to each computer.
- Cloning a Database: Install Oracle Database on one computer using interactive mode. You can also clone databases. Instructions for cloning databases are described in Oracle Database Administrator's Guide.

How do I configure client connections to an Oracle database?

1. Install Oracle Database on a server by using [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information.
2. Refer to [Chapter 3, "Installing Oracle Database Client"](inst_task.md) to install Oracle Database Client on each client node, and select the Instant Client installation type.
	If you have many client nodes, consider staging the software centrally, mapping the drive, and running Oracle Universal Installer in the response file mode.
	If the client nodes only require a default installation into a new Oracle home directory, consider using [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information.

What is the best way to install Oracle Database Client if my client nodes have limited disk space?

1. Install Oracle Database onto a server by using [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more details.
2. Refer to [Chapter 3, "Installing Oracle Database Client"](inst_task.md) to install Oracle Database Client on each client node, and select the Instant Client installation type.
	If you have many client nodes, then consider running Oracle Universal Installer in response file mode.

How do I upgrade Oracle Database?

Refer to [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) to use software cloning to upgrade Oracle Database

The computers at my site have been configured to run as a cluster. How should I install Oracle Database?

Use any of the following installation scenarios:

- If you want to run a single-instance Oracle Database in a clustered environment, then install Oracle Grid Infrastructure either before or after you install Oracle Database.
- If you want a consolidated pool of storage for all databases in a cluster, then install Oracle Grid Infrastructure and use Oracle Automatic Storage Management (Oracle ASM) to manage this storage. Afterwards, install Oracle Database (which can be either single instance or Real Application Clusters).
- If you plan to use Oracle Real Application Clusters, first install Oracle Grid Infrastructure, and then install Oracle Real Application Clusters.

Refer to [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) and [Oracle Real Application Clusters Installation Guide for Linux and UNIX](https://docs.oracle.com/cd/E11882_01/install.112/e41962/toc.htm) to install Oracle Grid Infrastructure or Oracle Real Application Clusters respectively. See this guide for information about how to install Oracle ASM and Oracle Database.

Oracle Clusterware is a key component required by Oracle Real Application Clusters installations. Oracle Clusterware is an integrated cluster management solution that can bind multiple servers to act as a single system. This is referred to as a cluster. It performs workload management and component restart. For example, when an instance supporting a particular service fails, Oracle Clusterware restarts the service on the next available instance that you have configured for that service. Oracle Clusterware can monitor non-Oracle programs, if they are defined within the Oracle Clusterware environment using the High Availability API.

How do I migrate my non-Oracle databases to Oracle Database?

Use Oracle SQL Developer to migrate your non-Oracle databases and applications to Oracle. Oracle SQL Developer software and documentation is available at:

`http://www.oracle.com/technetwork/developer-tools/sql-developer/overview/index.html`

## D.2 Installing Oracle Database Tools

The following are frequently asked questions about installing Oracle database tools:

- How do I install Oracle WebLogic Server?
- How can I administer and monitor my Oracle Database products?
- How do I manage security for my Oracle Database products?
- How do I use Oracle Database to manage my XML data?
- Does Oracle Database provide OLAP tools so that I can analyze data such as trends and time series in my database?
- Does Oracle Database provide data mining tools that I can use to discover hidden meaning in my data and predict likely outcomes based on my data?
- How do I perform backup and recovery operations for Oracle Database?
- Is Oracle Workflow included with Oracle Database 11g?
- Is there a migration plan for customers that have built solutions using Oracle Workflow?

How do I install Oracle WebLogic Server?

Refer to [Oracle Fusion Middleware Installation Guide for Oracle WebLogic Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=WLSIG).

For more information on Oracle WebLogic Server refer to the product documentation at:

`http://www.oracle.com/technetwork/middleware/weblogic/documentation/index.html`

How can I administer and monitor my Oracle Database products?

To perform regular administrative functions such as creating, configuring, or deleting databases, or managing database templates, use one of the following methods:

To manage only the single database and listener that you are installing:

1. Use [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to install Oracle Database.
2. From Oracle Database, use Database Configuration Assistant to manage your databases.
	You can also administer and monitor the database with Oracle Enterprise Manager Grid Control, which is installed by default with Oracle Database. Oracle Enterprise Manager Grid Control requires an agent which is not installed by default.
	Oracle Enterprise Manager Grid Control includes the Oracle Management Agent, Oracle Management Service, and Oracle Management Repository, and also Grid Control, a browser-based central console through which administrators can perform all monitoring, administration, and configuration tasks for the enterprise.
	See Also:
	Oracle Enterprise Manager Grid Control Basic Installation Guide available on the Enterprise Manager Grid Control installation media

To perform advanced administration tasks, such as monitoring Oracle Database and managing multiple hosts, application servers, and databases including the one that you are installing, install Oracle Enterprise Manager as follows:

1. Use [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to install Oracle Database.
	If you plan to use Oracle Real Application Clusters, then install Oracle Database by using [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) and [Oracle Real Application Clusters Installation Guide for Linux and UNIX](https://docs.oracle.com/cd/E11882_01/install.112/e41962/toc.htm).
2. Use Oracle Enterprise Manager Grid Control Basic Installation Guide to install and configure Oracle Enterprise Manager. For postconfiguration tasks, use Oracle Enterprise Manager Advanced Configuration. Refer to documentation available on the Enterprise Manager Grid Control installation media, or at:
	```
	http://docs.oracle.com/
	```

How do I manage security for my Oracle Database products?

Oracle provides a wide range of security solutions for your enterprise environment, including centralized administration and security features integrated with Oracle Internet Directory. The set of Oracle security services called Oracle Platform Security integrates the security features built into Oracle Database, Oracle WebLogic Server, and the Oracle Identity Management infrastructure. Combined, these features enable the development and deployment of secure e-business applications.

Oracle Identity Management includes Oracle Internet Directory, a centralized repository that simplifies administration of users and applications in the Oracle environment with the following components:

- Oracle Internet Directory client tools, including LDAP command-line tools, the Oracle Internet Directory SDK, and Oracle Directory Manager.
- Oracle Internet Directory server components, including the directory server, the directory replication server, the directory integration server, and various tools for starting and stopping them.

Oracle Database includes the Oracle Internet Directory client tools, but not the Oracle Internet Directory server components. To install the Oracle Internet Directory server components, see Oracle Fusion Middleware Installation Guide for Oracle Identity and Access Management and the Oracle Identity Management documentation at:

```
http://www.oracle.com/technetwork/middleware/id-mgmt/overview/index.html
```

How do I use Oracle Database to manage my XML data?

Use Oracle XML DB, which is installed as part of Oracle Database. Oracle XML DB enables you to efficiently store, generate, retrieve, query, and manage XML data on your site. Oracle XML DB provides all the advantages of a relational database, for example, allowing you to control the referential integrity of XML data with constraints and triggers. It works well with large amounts of XML data by storing it in a parsed, relational form, which improves access performance.

Oracle XML DB supports XML Type, which is a native data type for XML data, for which you can choose various storage options depending on your needs. In addition, Oracle XML DB supports XML Schema processing, structured and unstructured storage, a content repository that you can access by using common protocols (FTP, HTTP(S), and WebDAV), and SQL/XML, which is a standard for SQL with XML. For Oracle Database 11g Release 2 (11.2), Oracle XML DB introduced support for the XQuery language for querying, transforming, and constructing XML; the ability for users to define their own metadata for schema-based XML; a set of new SQL functions for DML operations on XML data; and more.

You can use Oracle XML DB with Oracle XML Developer's Kit (XDK) to build applications that run on either Oracle Database or Oracle WebLogic Server.

See Also:

- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)
- [Oracle XML Developer's Kit Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23582/toc.htm)

Does Oracle Database provide OLAP tools so that I can analyze data such as trends and time series in my database?

Yes, install Oracle OLAP, which is provided in the Oracle Database installation. Oracle OLAP provides optimal support for database environments that must meet OLAP requirements.

Use either of the following methods in Oracle Database Installation Guide to install Oracle OLAP:

- When you run Oracle Universal Installer, in the Select Database Edition screen, select Enterprise Edition. Click the Select Options button, and from the Choose Components screen, select Oracle OLAP.
	See Also:
	- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/toc.htm)
	- [Oracle OLAP DML Reference](https://docs.oracle.com/cd/E11882_01/olap.112/e17122/toc.htm)
	- [Oracle OLAP Java API Reference](https://docs.oracle.com/cd/E11882_01/olap.112/e10794/toc.htm)
- Select the Enterprise Edition installation type, and then on the Select Database Configuration screen, select the Data Warehouse configuration.
	See Also:
	[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) after installation

Does Oracle Database provide data mining tools that I can use to discover hidden meaning in my data and predict likely outcomes based on my data?

Yes, you must have an Enterprise Edition licence for the database installation. Install Oracle Data Mining, which is provided in the Oracle Database installation. With the Oracle Data Mining option, you can create and execute predictive and descriptive data mining models that use a variety of algorithms.

Use the following method in [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to install Oracle Data Mining:

1. When you run Oracle Universal Installer, select the Enterprise Edition installation type.
2. In the Select Database Configuration screen, select the General Purpose/Transaction Processing configuration.

See Also:

The following manuals after you have installed Oracle Data Mining:
- [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/toc.htm)
- [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/toc.htm)
- [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/toc.htm)
- [Oracle Data Mining Java API Reference](https://docs.oracle.com/cd/E11882_01/datamine.112/e12219/toc.htm)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) (search for Data Mining)

How do I perform backup and recovery operations for Oracle Database?

Use Oracle Database Recovery Manager (RMAN), which is a backup and recovery tool integrated into Oracle Database. This tool satisfies the pressing demands of high-performance, manageable backup, and recovery. Recovery Manager is native to the database server, automatically tracks database structure changes, and optimizes operations accordingly. In addition, Recovery Manager is integrated with leading tape media management products, so that Oracle database backups can be integrated with your existing networked data protection infrastructure.

Is Oracle Workflow included with Oracle Database 11g?

Starting with Oracle Database 11g, Oracle Workflow is no longer released with the database. Oracle Workflow is available with the Oracle E-Business Suite releases.

See Also:

Oracle Workflow statement of direction:

`http://www.oracle.com/technetwork/middleware/ias/overview/index.html`

Is there a migration plan for customers that have built solutions using Oracle Workflow?

Starting January 2006, customers are encouraged to re-create and implement workflows using Oracle BPEL Process Manager. Oracle is in the process of creating a technical migration to provide detailed recommendations for migrating Oracle Workflow processes to Oracle BPEL Process Manager.

See Also:

Oracle Workflow statement of direction:

`http://www.oracle.com/technetwork/middleware/ias/overview/index.html`

## D.3 Installing Oracle Database with Oracle Applications

The following are frequently asked questions about installing Oracle database with Oracle applications:

- How do I install my Oracle applications with Oracle Database?
- How can I create web applications that communicate with Oracle Database?
- Which web server can my Oracle applications use?
- How can I migrate my non-Oracle applications to Oracle?

How do I install my Oracle applications with Oracle Database?

In most cases, install Oracle Database itself, then install the Oracle application. The Oracle Universal Installer for that application prompts you for the connection information. Check the application documentation requirements.

If you must implement your applications with Oracle Real Applications Clusters databases, refer to [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) and [Oracle Real Application Clusters Installation Guide for Linux and UNIX.](https://docs.oracle.com/cd/E11882_01/install.112/e41962/toc.htm)

How can I create web applications that communicate with Oracle Database?

Install Oracle Application Express and a web server:

Use [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to install Oracle Database. Oracle Application Express is automatically installed, when you install Oracle database.

Which web server can my Oracle applications use?

Install Oracle HTTP Server, which ships on separate media, or use the XML DB HTTP Protocol Server and the embedded PL/SQL Gateway that installs with Oracle Database 11g Release 2.

How can I migrate my non-Oracle applications to Oracle?

Use Oracle SQL Developer to migrate your non-Oracle applications to Oracle. Oracle SQL Developer software and documentation is available at:

`http://www.oracle.com/technetwork/developer-tools/sql-developer/overview/index.html`

## D.4 Installing Oracle Database Heterogeneous Connectivity Tools (Gateways)

The following section discusses the Gateway products:

How can my Oracle applications access data in a non-Oracle database system?

How can my Oracle applications access data in a non-Oracle database system?

You can use Oracle Database Gateway as the connectivity tool to enable Oracle applications to access data in non-Oracle databases. The following are the functions of Oracle Database Gateway:

- Integrates a non-Oracle database into your Oracle Database environment.
- Enables Oracle PL/SQL applications to integrate with APPC-enabled transactions, or access messages in IBM Websphere MQ.

You can install the Gateway product on a computer independent of the Oracle application, Oracle database, and non-Oracle database.

For example, suppose you have the following scenario:

- Oracle Database is installed on an UNIX computer.
- The Oracle application is installed on a Microsoft Windows computer and accesses data from the Oracle database on the UNIX computer.
- The Oracle application must join data in a DB2 database on Oracle Solaris and an Oracle Database on UNIX.

You have the option of installing the Database Gateway for DRDA on the Oracle Solaris computer where DB2 is running, on UNIX where Oracle is running, or on a third computer.

Table D-1 lists the non-Oracle database systems that you can access from Oracle applications, and the Gateways products that are available for those systems.

Table D-1 Oracle Gateway Products

| Non-Oracle Database | Oracle Gateway Products and Documentation |
| --- | --- |
| IBM DB2 Universal Database (UDB) | Oracle Database Gateway for DRDA.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for DRDA User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12014/toc.htm). |
| IBM DB2 z/OS | Oracle Database Gateway for DRDA.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for DRDA User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12014/toc.htm). |
| IBM DB2/400 | Oracle Database Gateway for DRDA.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for DRDA User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12014/toc.htm). |
| WebSphere MQ | Oracle Database Gateway for WebSphere MQ.  [Oracle Database Gateway for WebSphere MQ Installation and User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12417/toc.htm). |
| CICS/TS  IMSTM | Oracle Database Gateway for APPC.  Use [Oracle Database Gateway for APPC Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12078/toc.htm).  Use [Oracle Database Gateway for APPC User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12071/toc.htm) |
| SQL Server | Oracle Database Gateway for SQL Server.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for SQL Server User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12069/toc.htm). |
| Sybase Adaptive Server | Oracle Database Gateway for Sybase.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for Sybase User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12067/toc.htm). |
| Teradata | Oracle Database Gateway for Teradata.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for Teradata User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12068/toc.htm). |
| Informix Server | Oracle Database Gateway for Informix.  Use [Oracle Database Gateway Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12013/toc.htm) and [Oracle Database Gateway for Informix User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12066/toc.htm). |
| IMS | Oracle Database Gateway for IMS.  Use [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm), [Oracle Database Gateway for IMS User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12072/toc.htm) and [Oracle Connect for IMS, VSAM, and Adabas Gateways Installation and Configuration Guide for IBM z/OS](https://docs.oracle.com/cd/E11882_01/gateways.112/e12075/toc.htm) |
| VSAM | Oracle Database Gateway for VSAM.  Use [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm), [Oracle Database Gateway for VSAM User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12073/toc.htm) and [Oracle Connect for IMS, VSAM, and Adabas Gateways Installation and Configuration Guide for IBM z/OS](https://docs.oracle.com/cd/E11882_01/gateways.112/e12075/toc.htm). |
| Adabas | Oracle Database Gateway for Adabas.  Use [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm), [Oracle Database Gateway for Adabas User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/toc.htm) and [Oracle Connect for IMS, VSAM, and Adabas Gateways Installation and Configuration Guide for IBM z/OS](https://docs.oracle.com/cd/E11882_01/gateways.112/e12075/toc.htm). |
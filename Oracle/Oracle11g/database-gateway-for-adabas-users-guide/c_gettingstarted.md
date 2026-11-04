---
title: Getting Started with Oracle Database Gateways
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/c_gettingstarted.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## 1 Getting Started with Oracle Database Gateways

This chapter contains the following sections:

## Overview

Heterogeneous data access is a problem that affects a lot of companies. A lot of companies run several different database systems. Each of these systems stores data and has a set of applications that run against it. Consolidation of this data in one database system is often hard—in large part because many of the applications that run against one database may not have an equivalent that runs against another. Until such time as migration to one consolidated database system is made feasible, it is necessary for the various heterogeneous database systems to interoperate.

Oracle Database Gateways provide the ability to transparently access data located in a non-Oracle system from an Oracle environment. This transparency eliminates the need for application developers to customize their applications to access data from different non-Oracle systems, thus decreasing development efforts and increasing the mobility of the application. Applications can be developed using a consistent Oracle interface for both Oracle and Adabas.

Gateway technology is composed of two parts: a component that has the generic technology to connect to a non-Oracle system, which is common to all the non-Oracle systems, called Heterogeneous Services, and a component that is specific to the non-Oracle system that the gateway connects to. Heterogeneous Services, in conjunction with the Database Gateway agent and Oracle Connect for IMS, VSAM, and Adabas Gateways, enables transparent access to non-Oracle systems from an Oracle environment.

## Oracle Heterogeneous Services

Heterogeneous Services provides the generic technology for connecting to non-Oracle systems. As an integrated component of the database, Heterogeneous Services can exploit features of the database, such as the powerful SQL parsing and distributed optimization capabilities.

Heterogeneous Services extend the Oracle SQL engine to recognize the SQL and procedural capabilities of the remote non-Oracle system and the mappings required to obtain necessary data dictionary information. Heterogeneous Services provides two types of translations: the ability to translate Oracle SQL into the proper dialect of the non-Oracle system and the ability to handle data dictionary translations so that the metadata of the non-Oracle system is displayed in the local format. For situations where no translations are available, native SQL can be issued to the non-Oracle system using the pass-through feature of Heterogeneous Services.

Heterogeneous Services also maintains the transaction coordination between Oracle and the remote non-Oracle system, such as providing the global transaction protocol to ensure distributed transaction integrity, even for non-Oracle systems that do not natively support global transactions.

See Also:

Oracle Database Heterogeneous Connectivity User's Guide for more information about Heterogeneous Services.

## Oracle Database Gateways

Oracle Database Gateway for Adabas allows Oracle client applications to access Adabas data through Structured Query Language (SQL). The gateway, with the Oracle database server, creates the appearance that all data resides on a local Oracle database server, even though data might be widely distributed. If data is moved from this data source to an Oracle database, no changes in the client application's design or function are needed because the gateway handles all differences in data types or SQL functions between the applications and the database.

Using Oracle SQL, Oracle client applications can access the Adabas data source as if the data was stored in an Oracle table. A single SQL statement can access data residing in Oracle and Adabas data sources, performing heterogeneous joins and subselects. This means that you can develop one set of portable applications to use against Oracle and these non-relational data sources. You can continue to develop new information systems without losing your investment in existing data and applications.

Transactions updating Oracle and this non-relational data source are automatically protected by the Oracle global transactions feature. Use of synonyms is another Oracle feature. By setting up synonyms in the Oracle database server that point to database links to Adabas files, the physical location of the data is transparent to the client application. This allows future migration of data from Adabas to Oracle to be transparent to the client applications.

The gateway requires the Oracle database server, Oracle Connect for IMS, VSAM, and Adabas Gateways, and Oracle Studio for IMS, VSAM, and Adabas Gateways. All other Oracle products are optional. However, using other Oracle products with the gateway can greatly extend the gateway's capabilities.

The gateway can be installed on a computer where the Oracle database is installed, or on a second, standalone machine. Each configuration has its advantages and disadvantages. The issues to consider when you determine where to install the gateway are network traffic, availability of the operating system platform, hardware resources, and storage.

Oracle Connect for IMS, VSAM, and Adabas Gateways must be installed on the z/OS system where the Adabas data source is installed. To be able to configure and manage Oracle Connect for IMS, VSAM, and Adabas Gateways, you need to install Oracle Studio for IMS, VSAM, and Adabas Gateways on a computer running Windows or Linux.

## Gateway Architecture

The gateway is invoked by the listener. The gateway is not multi-threaded and cannot support shared database links. Each gateway session spawns a separate gateway process, and connections cannot be shared.

The gateway is located on a Windows or UNIX computer. The non-relational data source resides on a computer running IBM z/OS. The Oracle database server can reside on the same machine as the gateway or on another machine.

The gateway interacts with the Oracle database server to interface between client applications and the Adabas data source, as shown in Figure 1-1.

Note:

The non-Oracle system in Figure 1-1 and Figure 1-2 represents the Adabas data source.

Figure 1-1 Gateway Processing

![This figure illustrates the gateway processing.](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img/gateway_processing.gif "This figure illustrates the gateway processing.")  
[Description of "Figure 1-1 Gateway Processing"](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img_text/gateway_processing.htm)  

- Client applications, such as Developer, connect to the Oracle database server by using Oracle Net.
- The Oracle database server, which includes Heterogeneous Services and the database itself, resides on a single system. This Oracle database server also stores definitions of database links for the non-Oracle system.
- The gateway to Adabas resides on a second system.
- The Adabas data source, together with Oracle Connect for IMS, VSAM, and Adabas Gateways, resides on a third system, which is an IBM z/OS platform.
- Oracle Studio for IMS, VSAM, and Adabas Gateways, which is used to configure Oracle Connect for IMS, VSAM, and Adabas Gateways, resides on a fourth system, which can be running a Windows or Linux operating system.
- The Oracle database server on the first system uses Oracle Net to connect directly to the Adabas gateway on the second system. The gateway itself uses the Oracle Connect for IMS, VSAM, and Adabas Gateways protocol to connect to Oracle Connect for IMS, VSAM, and Adabas Gateways, which then connects to the non-Oracle system using the same protocol.

The Oracle database server and the gateway work together to present the appearance of a single Oracle database to the client. All data accessed by the client appears to reside in a single Oracle database. The client application sends a request to the Oracle database server, and the Oracle database server sends the request to the gateway.

For the first transaction in a session, the gateway logs into the Adabas data source using a username and password that is valid in the respective data source. The gateway converts the SQL statement to a native Adabas statement, and the Adabas data source performs the request. The gateway converts the retrieved data to a format compatible with the Oracle database server and returns the results to the Oracle database server, which returns the results to the client application.

## Gateway Process Flow

Figure 1-2 shows a typical gateway process flow. The steps explain the sequence of the events that occurs when a client application queries the Adabas data source through the gateway.

Figure 1-2 Gateway Process Flow

![This figure illustrates the gateway process flow](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img/gateway_process_flow.gif "This figure illustrates the gateway process flow")  
[Description of "Figure 1-2 Gateway Process Flow"](https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/img_text/gateway_process_flow.htm)  

1. The client application sends a query over Oracle Net to the Oracle database server.
2. The Oracle database server sends the query over to the gateway, again using Oracle Net.
3. The gateway passes the query on to Oracle Connect for IMS, VSAM, and Adabas Gateways.
4. For the first transaction in a session, Oracle Connect for IMS, VSAM, and Adabas Gateways logs into the Adabas data source using a user name and password that is valid in the respective data source.
5. Oracle Connect for IMS, VSAM, and Adabas Gateways converts the Oracle SQL statement into a data access operation understood by the data source.
6. Oracle Connect for IMS, VSAM, and Adabas Gateways retrieves the data.
7. Oracle Connect for IMS, VSAM, and Adabas Gateways converts the retrieved data into a format compatible with the Oracle database server.
8. Oracle Connect for IMS, VSAM, and Adabas Gateways passes the data to the gateway using the Oracle Connect for IMS, VSAM, and Adabas Gateways protocol.
9. The gateway returns the query results to the Oracle database server, again using Oracle Net.
10. The Oracle database server passes the query results to the client application by using Oracle Net. The database link remains open until the gateway session is finished or the database link is explicitly closed.

## Setup Flow

To be able to access Adabas data, you need to perform the tasks described in the following list, in the specified order. Each step in the list directs you to the relevant manual or chapter.

1. Install Oracle Connect for IMS, VSAM, and Adabas Gateways
	See:
	[Oracle Connect for IMS, VSAM, and Adabas Gateways Installation and Configuration Guide for IBM z/OS](https://docs.oracle.com/cd/E11882_01/gateways.112/e12075/toc.htm) for information on installing Oracle Connect for IMS, VSAM, and Adabas Gateways
2. Install Oracle Studio for IMS, VSAM, and Adabas Gateways
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
3. Configure Oracle Connect for IMS, VSAM, and Adabas Gateways
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
4. Set up the connection to Oracle Connect for IMS, VSAM, and Adabas Gateways
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
5. Set up the Adabas data source
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
6. Set up the data source metadata
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
7. Install Oracle Database Gateway for Adabas
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
8. Configure Oracle Database Gateway for Adabas
	See:
	[Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/gateways.112/e12077/toc.htm) or [Oracle Database Gateway for IMS, VSAM, and Adabas Installation and Configuration Guide for AIX 5L Based Systems (64-Bit), HP-UX Itanium, Solaris Operating System (SPARC 64-Bit), Linux x86, and Linux x86-64](https://docs.oracle.com/cd/E11882_01/gateways.112/e12076/toc.htm)
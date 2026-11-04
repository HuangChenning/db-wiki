---
title: Quick Start to Oracle Net Services
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/gettingstart.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 6 Quick Start to Oracle Net Services

This chapter is designed to help novice users set up and test a simple but common network configuration, such as one between a client application and a database over a TCP/IP network.

This chapter contains the following topics:

## Prerequisites for Establishing Connectivity

The tasks in this chapter show a TCP/IP connection between a client computer and a database server. The following conditions are assumed about the database server and client computers:

- Database server computer
	- It is running on a network that can access the client.
		- An Oracle database is installed.
		- TCP/IP protocol support is installed.
		- A listener is configured.
- Client computer
	- It is running on a network that can access the database server.
		- Oracle Client is installed.
		- TCP/IP protocol support is installed.

## Confirming Network Availability

Before using Oracle Net to connect a client computer to a database server, confirm that the client computer can successfully communicate with the database server computer. Evaluating network connectivity can eliminate network-based errors.

To confirm network connectivity, do the following:

1. Confirm that the database server computer can communicate with itself with a [loopback test](glossary.md).
	A loopback test is a connection from the database server back to itself. Many network protocols provide a means of testing network connections. The PING utility can be used with a TCP/IP network.
	In a TCP/IP network, each computer has a unique [IP address](glossary.md). A name resolution service, such as [Domain Name System (DNS)](glossary.md), can be used to map the IP address of a computer with its host name. If a name resolution service is not used, then the mapping is typically stored in a centrally maintained file called `hosts`. This file is located in the `/etc` directory on Linux and the `\windows\system32\drivers\etc` directory on Microsoft Windows. For example, an entry for a database server computer named `sales-server` may look like the following:
	```
	#IP address of server     host name       alias
	192.168.2.203             sales-server    sales.us.example.com
	```
	1. To confirm hardware connectivity, enter the following command at the command line:
		```
		ping ip_address
		```
		In the preceding command, ip\_address is the IP address of the database server computer, such as the following:
		```
		ping 192.168.2.203
		```
		2. To confirm the DNS or host name is configured properly, enter the following command at the command line:
		```
		ping host_name
		```
		in the preceding command, host\_name is the host name of the server.
		3. To test the TCP/IP setup for the server, enter the following command:
		```
		ping 127.0.0.1
		```
2. Verify the client computer can successfully communicate with the database server computer.
	This varies according to the network protocol. For TCP/IP, you can use PING, FTP or TELNET utilities.
	If the client computer cannot reach the server, then verify that the network cabling and network interface cards are correctly connected. Contact your network administrator to correct these problems.

## Starting Oracle Net Listener and the Oracle Database Server

Oracle Net Listener and the Oracle Database server must be running in order for the database server to receive connections. To start Oracle Net Listener, do the following:

1. Start the listener with the Listener Control utility. From the command line, enter the following:
	```
	lsnrctl
	LSNRCTL> START [listener_name
	]
	```
	In the preceding command, listener\_name is the name of the listener defined in the `listener.ora` file. It is not necessary to identify the listener if you are using the default name `LISTENER`.
	A status message indicating that the listener has successfully started displays.
2. Start the database, as follows:
	1. Start SQL\*Plus without connecting to the database using the following command:
		```
		sqlplus /nolog
		```
		2. Connect to the database as SYSDBA using the following command:
		```
		SQL> CONNECT username
		 as sysdba
		```
		For example, `SYS` is a SYSDBA user. You will be prompted to enter a password.
		Note:
		For simplicity, this example does not perform the password management techniques that a deployed system normally uses. In a production environment, follow the Oracle Database password management guidelines, and disable any sample accounts. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/app_devs.htm#DBSEG50053) for password management guidelines and other security recommendations.
		3. Start the database using the following command:
		```
		SQL> STARTUP OPEN database_name
		```
		See Also:
		- [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for additional information about the STARTUP command
		- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for additional information about starting the database
3. Confirm that database [service registration](glossary.md) with the listener has completed using the Listener Control utility using the following command:
	```
	LSNRCTL> SERVICES [listener_name
	]
	```
	The `SERVICES` command lists the services supported by the database, along with at least one available [service handler](glossary.md). If the database service registration is not listed, then enter the following SQL command:
	```
	SQL> ALTER SYSTEM REGISTER
	```
	See Also:
	["Monitoring Services of a Listener"](listenercfg.md) for additional information about the `SERVICES` command

## Starting Oracle Connection Manager

If you have installed Oracle Connection Manager, then start Oracle Connection Manager as follows:

1. Start Oracle Connection Manager Control utility (CMCTL) using the following commands:
	```
	cmctl
	CMCTL> ADMINISTER [instance_name
	]
	```
	In the preceding commands, instance\_name is the name of Oracle Connection Manager to administer. You can determine the name by viewing the `cman.ora` file. The file is located on the Oracle Connection Manager computer in the `ORACLE_HOME/network/admin` directory.
	Oracle Connection Manager displays a status message indicating the name of the instance and informing you that the instance has not yet been started.
	Note:
	If you do not provide an instance name as an argument, then provide Oracle Connection Manager with a fully qualified host name. This is the default. After you issue the `ADMINISTER` command, CMCTL displays the instance name as follows:
	```
	CMAN_fully_qualified_host_name
	```
2. Start the Oracle Connection Manager that you have chosen to administer using the following command:
	```
	cmctl> STARTUP
	```
	Oracle Connection Manager confirms that the instance has been started, and provides status for the instance.
	Note:
	On Microsoft Windows, Oracle Connection Manager can also be started through the Control Panel, as follows:
	1. Select Services in the Control Panel.
	2. Select the `Oracle` `HOME_NAME` `CMan` service, and then click Start.
	3. In the Services window, click Close.
3. Exit from the Oracle Connection Manager Control utility using the following command:
	```
	cmctl> EXIT
	```

## Connecting to the Database

There are several methods to connect to an Oracle database. Table 6-1 lists syntax to connect to a database.

Table 6-1 Connecting to a Database

| Type of Connection | Connection Syntax | Description |
| --- | --- | --- |
| From the command line | The general form of connecting an application to a database server from the command line is:  ``` tool  username@connect_identifier Enter password: password ```  You will be prompted to enter your password which will be encrypted.  For example:  ``` SQLPLUS system@sales Enter password: password ``` | Most Oracle tools can use the operating system command line to connect, and some provide alternatives. |
| From a login screen | ``` username @connect_identifier ``` | Some tools provide a logon screen as an alternative form to log on. A user can log on to a database server by identifying both the username and connect identifier in the username field of the tool logon screen, and entering the password as usual in the password field. |
| From a 3GL application | ``` exec sql connect :username  identified by :password ```  In the preceding connection request,:username and:password are 3GL variables that can be set within the program either statically or by prompting the user. When connecting to a database server, the value of the:username variable is in the form:  ``` username@net_service_name ```  The:password variable contains the password for the database account to which you are connecting. | Applications written in 3GL, such as OCI and pre-compilers, are used by middle-tier and database application developers for direct database access from a client program. |
| From within SQL\*Plus | ``` sqlplus /nolog SQL> CONNECT username@net_service_name  Enter password: password ```  For example:  ``` sqlplus /nolog SQL> CONNECT scott@serverx Enter password: password ```  In the preceding commands, username and password are the database user and password, and net\_service\_name is the net service name. | Some Oracle tools have commands for database connections to allow an alternative username to be specified without leaving the tool.  Other Oracle tools use slightly different methods specific to their function or interface. For example, Oracle CDE tools use logon buttons and a window with fields for the username, password, and remote database ID. |

## Using Easy Connect to Connect to a Database

After network connectivity has been verified as described in "Confirming Network Availability", you can use the Easy Connect naming method to connect to the database. This naming method provides out-of-the-box TCP/IP connectivity to databases. It extends the functionality of the [host naming](glossary.md) method by enabling clients to connect to a database server with an optional port and service name in addition to the host name of the database. The following is the syntax to connect using Easy Connect:

```
CONNECT username
/password
@host
[:port
][/service_name
][:server
][/instance_name
]
```

Note:

In Oracle Call Interface documentation, server is referred to as `connect_type`.

If you have performed Oracle Database server installation in Typical mode, then the default service name used by the Oracle instance is `ORCL`, and the following Easy Connect syntax can be used to connect to that instance:

```
sqlplus /nolog
SQL> CONNECT username
@"host
/ORCL"
SQL> Enter password: password
```

NOTE:

Starting with Oracle Database 10g, Oracle Database does not support the use of Oracle Names. Oracle Database 11g clients and databases cannot use Oracle Names, including those from an LDAP proxy, to resolve naming. Oracle9i clients can still use Oracle Names to resolve naming for an Oracle Database 11g database. However, customers are strongly encouraged to migrate to LDAP to take advantage of the new features of Oracle Database 11g.

See Also:

["Using the Easy Connect Naming Method"](naming.md) for additional information about this method
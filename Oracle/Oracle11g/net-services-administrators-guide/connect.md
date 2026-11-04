---
title: Testing Connections
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/connect.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 15 Testing Connections

After you have configured the network, you should connect and test each component to ensure that the network is functioning properly. Oracle Net Services provides tools to help you test the listener, database, and Oracle Connection Manager.

This chapter contains the following topics:

## Testing the Network

The following is the recommended sequence for testing the network:

1. Start and test each listener. To start the listener, use the procedure described in ["Starting Oracle Net Listener and the Oracle Database Server"](gettingstart.md). To test a listener, initiate a connection from a client to any active database controlled by that listener.
2. Start and test each Oracle Connection Manager, if included in your network. To start Oracle Connection Manager, use the procedure described in ["Starting Oracle Connection Manager"](gettingstart.md).
	To test Oracle Connection Manager, initiate a connection from a client to any active database that has been registered with Oracle Connection Manager.
3. Test the server with a loopback test or Oracle Net Manager.
	A [loopback test](glossary.md) uses Oracle Net to go from the database server back to itself, bypassing the Interprocess Communication (IPC). Performing a successful loopback verifies that Oracle Net is functioning on the database server. The following procedure describes how to perform a loopback test using Oracle Net Manager:
	1. Start Oracle Net Manager.
		See Also:
		["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
		2. In the navigator, expand Directory or Local, and then select Service Naming.
		3. Select the net service name or database service.
		4. Choose Command, and then select Test Net Service.
		Testing assumes the listener and database are running. If they are not, then see ["Starting Oracle Net Listener and the Oracle Database Server"](gettingstart.md) to start components.
		During testing, a Connection Test dialog box appears, providing status and test results. A successful test results in the following message:
		```
		The connection test was successful.
		```
		If the test was successful, then proceed to Step 5.
		If the test was not successful, then use the error message to determine further action. For example, if the error message is the following:
		```
		Initializing first test to use userid: scott, password: tiger
		Attempting to connect using userid:  scott
		The test did not succeed.
		ORA-28000: the account is locked
		 
		There may be an error in the fields entered,
		or the server may not be ready for a connection.
		```
		Change the user name to an account known to be unlocked. To change the user name, click Change Login. You will be prompted for the password.
		5. Click Close to close the Connect Test dialog box.
4. Test client with a connection.
	To test several different clients in your network, initiate a connection to a database server from each of them using the following command:
	```
	CONNECT username
	@connect_identifier
	```

## Using the TNSPING Utility to Test Connectivity from the Client

The TNSPING utility determines whether the listener for a service on an Oracle Net network can be reached successfully.

If you can connect successfully from a client to a server (or a server to another server) using the TNSPING utility, then it displays an estimate of the round trip time (in milliseconds) it takes to reach the Oracle Net service.

If it fails, then it displays a message describing the error that occurred. This enables you to see the network error that is occurring without the overhead of a database connection.

Use the following command to test connectivity:

```
tnsping net_service_name
 count
```

In the preceding command, the following arguments are used:

- net\_service\_name must exist in `tnsnames.ora` file or the name service in use, such as NIS.
- count determines how many times the program attempts to reach the server. This argument is optional.

If the net service name specified is a database name, then TNSPING attempts to contact the corresponding listener. It does not actually determine whether the database is running. Use SQL\*Plus to attempt a connection to the database.

Following are some examples of TNSPING.

Note:

Different platforms may have different interfaces, but the program accepts the same arguments. Invoke TNSPING for the display of the proper interface requirements.

Example 15-1 is an example of checking a listener for a database using a net service name of `sales` using the `TNSPING` command.

Example 15-1 Checking a Listener with TNSPING

```
TNSPING sales
```

This produces the following message:

```
TNS Ping Utility for Linux: Version 11.1.0.0.2 on 15-FEB-2009 14:46:28

Copyright (c) 1997, 2009 Oracle Corporation.  All rights reserved.

Used parameter files:
Used TNSNAMES adapter to resolve the alias
Attempting to contact (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL =
TCP)(HOST = sales-server)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME =
sales.us.example.com)))
OK (10 msec)
```

To determine whether the listener for the `sales` database is available, and to specify that TNSPING try to connect eight times and then give up, use the following syntax:

```
tnsping sales 8
```

This command produces the following message:

```
TNS Ping Utility for Linux: Version 11.1.0.0.2 on 15-FEB-2009 14:48:28

Copyright (c) 1997, 2009 Oracle Corporation.  All rights reserved.

Used parameter files:

Used TNSNAMES adapter to resolve the alias
Attempting to contact (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL =
TCP)(HOST = sales-server)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME =
sales.us.example.com)))
OK (10 msec)
OK (0 msec)
OK (10 msec)
OK (0 msec)
OK (10 msec)
OK (10 msec)
OK (10 msec)
OK (0 msec)
```

Example 15-2 is an example of TNSPING attempting to check using an invalid net service name.

Example 15-2 Checking an Invalid Net Service Name with TNSPING

```
tnsping badname
```

This attempt produces the following message:

```
TNS Ping Utility for Linux: Version 11.1.0.0.2 on 15-FEB-2009 14:50:28

Copyright (c) 1997, 2009 Oracle Corporation.  All rights reserved.

Used parameter files:

TNS-03505: Failed to resolve name
```

Example 15-3 is an example of output when using TNSPING to check a name that is valid, but that resolves to an address where no listener is located (for example, the listener may not be started).

Example 15-3 Checking Valid Net Service Name but No Listener with TNSPING

```
TNS Ping Utility for Linux: Version 11.1.0.0.2 on 15-FEB-2009 14:52:28

Copyright (c) 1997, 2009 Oracle Corporation.  All rights reserved.

Used parameter files:
Used TNSNAMES adapter to resolve the alias
Attempting to contact (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL =
TCP)(HOST = sales-server)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME =
sales.us.example.com)))
TNS-12541: TNS:no listener
```

## Using the TRCROUTE Utility to Test Connectivity from the Client

The Trace Route Utility (TRCROUTE), in Linux and UNIX environments, enables administrators to discover the path or route a connection is taking from a client to a server. If TRCROUTE encounters a problem, then it returns an error stack to the client instead of a single error. These additional error messages make troubleshooting easier.

TRCROUTE is different from TNSPING in that it travels as a special type of connect packet, and is routed as such. As it travels toward its destination, the TRCROUTE connect packet collects the TNS addresses of every node it travels through. If an error occurs, then TRCROUTE collects error information that shows where the error occurred. The TRCROUTE displays the information collected on the client screen. You can redirect the TRCROUTE output to a file, and print it if you want.

The TRCROUTE uses minimal resources. It gathers information in the connect data of a special connect packet; standard connect packets are not affected.

The server is not affected by TRCROUTE. The listener receives and processes the TRCROUTE connect packet. It returns the information to the client by putting it into a refuse packet. The server does not need to start any new processes or deal with dummy connections.

To use the TRCROUTE utility, enter the following command:

```
trcroute net_service_name
```

Example 15-4 shows a successful trace route packet that traveled from a client to a listener.

Example 15-4 Successful Trace Route

```
trcroute sales
Trace Route Utility for Linux: Version 11.2.0.0.2 on 15-FEB-2009 14:35:05

Copyright (c) 1999, 2009 Oracle Corporation.  All rights reserved.

Route of TrcRoute:
------------------
 
Node: Client            Time and address of entry into node:
-------------------------------------------------------------
09-NOV-2008 21:48:48 ADDRESS= PROTOCOL=TCP  HOST=10.150.21.136  PORT=14001
 
Node: Server            Time and address of entry into node:
-------------------------------------------------------------
09-NOV-2008 21:48:05 ADDRESS= PROTOCOL=TCP  HOST=10.150.21.136  PORT=14001
```

Example 15-5 shows an unsuccessful trace route packet that could not reach the listener because the listener was not up.

Example 15-5 Trace Route with Error

```
Trace Route Utility for Linux: Version 11.2.0.0.2 on 15-FEB-2009 14:35:05

Copyright (c) 1999, 2009 Oracle Corporation.  All rights reserved.

Route of TrcRoute:
------------------

Node: Client            Time and address of entry into node:
-------------------------------------------------------------
25-FEB-2002 14:43:05 ADDRESS= PROTOCOL=TCP  HOST=sales-server  PORT=1521

TNS-12543: TNS:unable to connect to destination
TNS-12541: TNS:no listener
TNS-12560: TNS:protocol adapter error
TNS-03601: Failed in route information collection
```
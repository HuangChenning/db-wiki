---
title: Configuring Profiles
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 12 Configuring Profiles

This chapter describes how to configure client and server configuration parameters in [profile](glossary.md) s. A profile is a collection of parameters that specifies preferences for enabling and configuring Oracle Net features on the client or database server. A profile is stored and implemented through the `sqlnet.ora` file.

This chapter contains the following topics:

## Overview of Profile Configuration

You can use a profile to:

- Specify the client domain to append to unqualified names
- Prioritize [naming method](glossary.md) s
- Enable logging and tracing features
- Route connections through specific processes
- Configure parameters for an [external procedure](glossary.md)
- Configure [Oracle Advanced Security](glossary.md)
- Use protocol-specific parameters to restrict access to the database

## Configuring the Profile During Installation

Oracle Universal Installer launches [Oracle Net Configuration Assistant](glossary.md) after software installation on the client and server. Oracle Net Configuration Assistant configures the order of the naming methods that the computer uses to resolve a [connect identifier](glossary.md) to a [connect descriptor](glossary.md)

Configuration with the Oracle Net Configuration Assistant during installation results in an entry in the `sqlnet.ora` file similar to the following:

```
NAMES.DIRECTORY_PATH=(ezconnect,tnsnames)
```

`NAMES.DIRECTORY_PATH` specifies the priority order of the naming methods to use to resolve connect identifiers. If the installed configuration is not adequate, then use [Oracle Net Manager](glossary.md) to change the `sqlnet.ora` configuration.

## Configuring Client Attributes for Names Resolution

The following sections describe available client configuration options:

- Specifying a Default Domain for Clients
- Prioritizing Naming Methods
- Routing Connection Requests to a Process

### Specifying a Default Domain for Clients

In environments where the client often requests names from a specific domain, it is appropriate to set a default domain in the client `sqlnet.ora` file with the `NAMES.DEFAULT_DOMAIN` parameter. This parameter is available to local and external naming methods.

When a default domain is set, it is automatically appended to any unqualified net service name given in the connect string, and then compared to net service names stored in a `tnsnames.ora` file.

For example, if the client `tnsnames.ora` file contains a net service name of `sales.us.example.com`, and the default domain is `us.example.com`, then the user can enter the following connect string:

```
CONNECT scott@sales
Enter password: password
```

In the preceding example, `sales` gets searched as `sales.us.example.com`.

If the connect string includes the domain extension, such as in `CONNECT scott@sales.us.example.com`, then the domain is not appended.

If a net service name in a `tnsnames.ora` file is not domain qualified and the `NAMES.DEFAULT_DOMAIN` parameter is set, then the net service name must be entered with a period (`.`) at the end of the name. For example, if the domain is set to `us.example.com` and the client `tnsnames.ora` file contains a net service name of `sales2`, then the user would enter the following connect string:

```
CONNECT scott@sales2.
Enter password: password
```

In the preceding example, the client would connect to `sales2`, not `sales2.us.example.com`.

The following procedure describes how to specify a default domain:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the Local menu.
3. From the list in the right pane, select Naming.
4. Click the Methods tab.
5. In the Default Domain field, enter the domain.
6. Select Save Network Configuration from the File menu.
	The `sqlnet.ora` file should contain an entry that looks similar to the following:
	```
	NAMES.DEFAULT_DOMAIN=us.example.com
	```

### Prioritizing Naming Methods

After naming methods are configured, as described in [Chapter 8, "Configuring Naming Methods"](naming.md), they must be prioritized. Naming methods to resolve a connect identifier are tried in the order they appear in the list. If the first naming method in the list cannot resolve the connect identifier, then the second method in the list is used, and so on.

The following procedure describes how to specify the order of naming methods:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the Local menu.
3. From the list in the right pane, select Naming.
4. Click the Methods tab.
	Table 12-1 describes the naming method values listed in the Methods tab.
	Table 12-1 Naming Method Values
	| Naming Method Value | Description |
	| --- | --- |
	| TNSNAMES | Resolve a [net service name](glossary.md) through the `tnsnames.ora` file on the client.  See Also: ["Configuring the Local Naming Method"](naming.md) |
	| LDAP | Resolve a database service name, net service name, or [net service alias](glossary.md) through a [directory server](glossary.md).  See Also: ["Configuring the Directory Naming Method"](naming.md) |
	| EZCONNECT | Enable clients to use a TCP/IP connect identifier, consisting of a host name and optional port and service name, or resolve a host name alias through an existing names resolution service or centrally maintained set of `/etc/hosts` files.  See Also: ["Using the Easy Connect Naming Method"](naming.md) |
	| NIS | Resolve service information through an existing network information service (NIS). |
5. Select naming methods from the Available Methods list, and then click the right-arrow button.
	The selected naming methods move to the Selected Methods list.
6. Order the naming methods according to the order in which you want Oracle Net to try to resolve the net service name or database service name. Select a naming method in the Selected Methods list, and then click Promote or Demote to move the selection up or down in the list.
7. Select Save Network Configuration from the File menu.
	The `sqlnet.ora` file updates with the `NAMES.DIRECTORY_PATH` parameter:
	```
	NAMES.DIRECTORY_PATH=(ldap, tnsnames)
	```

### Routing Connection Requests to a Process

Clients and servers can be configured so connection requests are directed to a specific process. The following procedure describes how to route connection requests to a process:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the Local menu.
3. From the list in the right pane, select General.
4. Click the Routing tab.
5. Select the preferred way for routing connections.
	Note:
	To configure all connections to use a particular server, you select the Always Use Dedicated Server option in Oracle Net Manager. This sets the `USE_DEDICATED_SERVER` parameter in the `sqlnet.ora` file to force the listener to spawn a dedicated server for all network sessions from the client. The result is a dedicated server connection, even if a shared server is configured.
6. Choose File > Save Network Configuration.

See Also:

Table 12-3, "Advanced Settings in sqlnet.ora" for a description of the fields and options

## Configuring Database Access Control

You can configure the `sqlnet.ora` file to allow access to some clients and deny access to others. Table 12-2 describes the available settings.

Table 12-2 Access Control Settings in sqlnet.ora

| Oracle Net Manager Field/Option | sqlnet.ora File Parameter | Description |
| --- | --- | --- |
| Check TCP/IP client access rights | TCP.VALIDNODE\_CHECKING | Specify whether to screen access to the database.  If this field is selected, then Oracle Net Manager checks the parameters `TCP.EXCLUDED_NODES` and `TCP.VALIDNODE_CHECKING` to determine which clients to allow access to the database. If this field is deselected, then Oracle Net Manager does not screen clients. |
| Clients denied access | TCP.EXCLUDED\_NODES | Specify which clients using the TCP/IP protocol are denied access to the database. |
| Clients allowed access | TCP.INVITED\_NODES | Specify which clients using the TCP/IP protocol are allowed access to the database. |

If the TCP.INVITED\_NODES parameter does not include the listener node, then the Listener Control utility cannot connect to the listener. This will prevent start, stop and administration commands from being performed on the listener.

If there are invalid host names or IP addresses listed in the TCP.INVITED\_NODES parameter or the TCP.EXCLUDED\_NODES parameter, then the Listener Control utility cannot contact the listener.

The following procedure describes how to configure database access control:

1. Start Oracle Net Manager.

See Also:

["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)

1. In the navigator pane, select Profile from the Local menu.
2. From the list in the right pane, select General.
3. Click the Access Rights tab.
4. Select the Check TCP/IP client access rights option.
5. In the Clients allowed to access fields and Clients excluded from access, enter either a host name or an IP address for a client that you want to include or exclude, using commas to delimit entries placed on the same line.

## Configuring Advanced Profile Information

Table 12-3 describes the advanced `sqlnet.ora` file settings that you can set.

Table 12-3 Advanced Settings in sqlnet.ora

| Oracle Net Manager Field/Option | sqlnet.ora File Parameter | Description |
| --- | --- | --- |
| Send operation Time Out | SQLNET.SEND\_TIMEOUT | Specify the time, in seconds, for a database server to complete a send operation to clients to complete after connection establishment.  Setting this parameter is recommended for environments in which clients shut down on occasion or abnormally. If the database server cannot complete a send operation in the time specified, then it logs `ORA-12535: TNS:operation timed out` and `ORA-12608: TNS: Send timeout occurred` errors in the `sqlnet.log` file.  Without this parameter, the database server continues to send responses to clients that are unable to receive data.  You can also set this parameter on the client side to specify the time, in seconds, for a client to complete send operations to the database server after connection establishment. Without this parameter, the client may continue to send requests to a database server already overwhelmed with requests. |
| Receive operation Time Out | SQLNET.RECV\_TIMEOUT | Specify the time, in seconds, for a database server to wait for client data after connection establishment. A client must send some data within the specified time interval.  Setting this parameter is recommended for environments in which clients shut down on occasion or abnormally. If a client does not send any data in the time specified, then the database server logs `ORA-12535: TNS:operation timed out` and `ORA-12609: TNS: Receive timeout occurred` errors to the `sqlnet.log` file.  Without this parameter, the database server continues to wait for data from clients that may be down or are experiencing difficulties.  You can also use this setting on the client side to specify the time, in seconds, for a client to wait for response data from the database server after connection establishment. Without this parameter, the client may wait for a long period of time for a response from a database server overwhelmed with requests. |
| Connection Time Out | SQLNET.INBOUND\_CONNECT\_TIMEOUT | Specify the time, in seconds, for a client to connect with the database server and provide the necessary authentication information. |
| Total Send Buffer Size | SEND\_BUF\_SIZE | Specify the buffer space limit for send operations of sessions. |
| Total Receive Buffer Size | RECV\_BUF\_SIZE | Specify the buffer space limit for receive operations of sessions. |
| TNS Time Out Value | SQLNET.EXPIRE\_TIME | Specify the time interval, in minutes, to send a probe to verify that client/server connections are active. Setting a value greater than 0 ensures that connections are not left open indefinitely, due to an abnormal client termination. If the probe finds a terminated connection, or a connection that is no longer in use, then it returns an error, causing the server process to exit. This setting is intended for the database server, which typically handles multiple connections at any one time.  Limitations on using this terminated connection detection feature are:  - It is not allowed on bequeathed connections. - Though very small, a probe packet generates additional traffic that may downgrade network performance. - Depending on which operating system is in use, the server may need to perform additional processing to distinguish the connection probing event from other events that occur. This can also result in downgrading network performance. |
| Client Registration ID | SQLNET.CLIENT\_REGISTRATION | Specify a unique identifier for a client. This identifier is passed to the listener with any connection request. The identifier can be any string up to 128 characters long. |
| Logon Authentication Protocol Version | SQLNET.ALLOWED\_LOGON\_VERSION | Define the minimum Oracle Database client release that is allowed to attempt connections to database instances under the control of the given code tree. Each connection attempt is tested. If the client or server does not meet the minimum release specified by its partner, then authentication fails with an `ORA-28040` error.  Supported values include:  - `11` for Oracle Database 11g authentication protocols (recommended for strongest protection) - `10` for Oracle Database 10g authentication protocols - `9` for Oracle9i authentication protocols - `8` for Oracle8i authentication protocols  The default value is `8`. Note the following implications of setting the value to `11`:  - To take advantage of the password protections introduced in Oracle Database 11g, users must change their passwords. - Releases of OCI clients before Oracle Database 10g and all versions of JDBC thin clients cannot authenticate to the Oracle database using password-based authentication. |
| Turn Off UNIX Signal Handling | BEQUEATH\_DETACH | Turn on or off UNIX signal handling.  Because the client application spawns a server process internally through the Bequeath protocol as a child process, then the client application becomes responsible for cleaning up the child process when it completes. When the server process completes its connection responsibilities, it becomes a terminated process. Signal handlers are responsible for cleaning up these terminated processes. Setting this parameter configures the client profile to pass this process to the UNIX initialization process by disabling signal handlers. |
| Disable Out-of-Band Break | DISABLE\_OOB | Turn on or off out-of-band breaks.  If deselected or set to `off`, then Oracle Net can send and receive break messages using urgent data requests provided by the underlying protocol. Once enabled, this feature applies to all protocols used by this client.  If selected or set to `on`, then it disables the ability to send and receive break messages using urgent data requests of the underlying protocol. |

See Also:

- ["Limiting Resource Consumption by Unauthorized Users"](performance.md) for complete information about configuring the SQLNET.INBOUND\_CONNECT\_TIMEOUT setting
- ["Configuring I/O Buffer Space"](performance.md) for complete information about configuring the SEND\_BUF\_SIZE and RECV\_BUF\_SIZE settings
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)
- Oracle operating system-specific documentation to determine if the protocol supports urgent data requests. TCP/IP is an example of a protocol that supports this feature.

The following procedure describes how to set advanced features in the `sqlnet.ora` file:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the Local menu.
3. From the list in the right pane, select General.
4. Click the Advanced tab.
5. Enter the values for the fields or options you want to set.
6. Select Save Network Configuration from the File menu.

## Configuring External Naming Methods

The `sqlnet.ora` file is used to configure required client parameters needed for Network Information Service (NIS) external naming. The following procedure describes how to configure the NIS parameter in the `sqlnet.ora` file:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the File menu.
3. From the list in the right pane, select Naming.
4. Click the External tab.
5. Select Save Network Configuration from the File menu.

## Configuring Oracle Advanced Security

[Oracle Advanced Security](glossary.md) enables data encryption and integrity checking, enhanced authentication, and single sign-on. Oracle Advanced Security also provides centralized user management on LDAP-compliant directory servers and certificate-based single sign-on. This functionality relies on the [Secure Sockets Layer (SSL)](glossary.md).

The following procedure describes how to configure a client or server to use Oracle Advanced Security features:

1. Start Oracle Net Manager.
	See Also:
	["Using Oracle Net Manager to Configure Oracle Net Services"](admintools.md)
2. In the navigator pane, select Profile from the Local menu.
3. From the list in the right pane, select Oracle Advanced Security.
	Each Oracle Advanced Security tab page enables you to configure a separate set of parameters.
4. Select or edit options as applicable.
5. Select Save Network Configuration from the File menu.

See Also:

- Choose the Help button on the particular tab page
- Oracle Advanced Security procedural topics in the Oracle Net Manager online help. To access these topics in the online help, select Oracle Advanced Security, and then select the How To option
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for additional information about configuration
---
title: Local Naming Parameters (tnsnames.ora)
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/tnsnames.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 6 Local Naming Parameters (tnsnames.ora)

This chapter provides a complete listing of the `tnsnames.ora` file configuration parameters.

This chapter contains the following topics:

## Overview of Local Naming Parameters

This `tnsnames.ora` file is a configuration file that contains [net service name](glossary.md) s mapped to [connect descriptor](glossary.md) s for the [local naming](glossary.md) method, or net service names mapped to listener protocol addresses.

A net service name is an alias mapped to a database network address contained in a connect descriptor. A connect descriptor contains the location of the listener through a protocol address and the service name of the database to which to connect. Clients and database servers (that are clients of other database servers) use the net service name when making a connection with an application.

By default, the `tnsnames.ora` file is located in the `ORACLE_HOME/network/admin` directory. Oracle Net will check the other directories for the configuration files. For example, the order checking the `tnsnames.ora` file is as follows:

1. The directory specified by the `TNS_ADMIN` environment variable. If the file is not found in the directory specified, then it is assumed that the file does not exist.
2. If the `TNS_ADMIN` environment variable is not set, then Oracle Net will check the `ORACLE_HOME/network/admin` directory.

Note:

On Microsoft Windows, the `TNS_ADMIN` environment variable is used if it is set in the environment of the process. If the `TNS_ADMIN` environment variable is not defined in the environment, or the process is a service which does not have an environment, then Microsoft Windows scans the registry for a `TNS_ADMIN` parameter.

See Also:

Oracle operating system-specific documentation

## General Syntax of tnsnames.ora

The basic syntax for a `tnsnames.ora` file is shown in Example 6-1.

Example 6-1 Basic Format of tnsnames.ora File

```
net_service_name= 
 (DESCRIPTION= 
   (ADDRESS=(protocol_address_information
))
   (CONNECT_DATA= 
     (SERVICE_NAME=service_name
)))
```

In the preceding example, `DESCRIPTION` contains the connect descriptor, `ADDRESS` contains the protocol address, and `CONNECT_DATA` contains the database service identification information.

## Multiple Descriptions in tnsnames.ora

A `tnsnames.ora` file can contain net service names with one or more connect descriptors. Each connect descriptor can contain one or more protocol addresses. Example 6-2 shows two connect descriptors with multiple addresses. `DESCRIPTION_LIST` defines a list of connect descriptors.

Example 6-2 Net Service Name with Multiple Connect Descriptors in tnsnames.ora

```
net_service_name= 
 (DESCRIPTION_LIST=
  (DESCRIPTION= 
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
))
   (CONNECT_DATA= 
     (SERVICE_NAME=service_name
)))
  (DESCRIPTION= 
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
))
   (CONNECT_DATA= 
     (SERVICE_NAME=service_name))))
```

Note:

Oracle Net Manager does not support the creation of multiple connect descriptors for a net service name when using Oracle Connection Manager.

## Multiple Address Lists in tnsnames.ora

The `tnsnames.ora` file also supports connect descriptors with multiple lists of addresses, each with its own characteristics. In Example 6-3, two address lists are presented. The first address list features [client load balancing](glossary.md) and no [connect-time failover](glossary.md), affecting only those protocol addresses within the `ADDRESS_LIST`. The second protocol address list features connect-time failover and no client load loading balancing, affecting only those protocol addresses within the `ADDRESS_LIST`. The client first tries the first or second protocol address at random, then tries protocol addresses three and four sequentially.

Example 6-3 Multiple Address Lists in tnsnames.ora

```
net_service_name= 
 (DESCRIPTION= 
  (ADDRESS_LIST= 
   (LOAD_BALANCE=on)
   (FAILOVER=off)
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
)))
  (ADDRESS_LIST= 
   (LOAD_BALANCE=off)
   (FAILOVER=on)
   (ADDRESS=(protocol_address_information
))
   (ADDRESS=(protocol_address_information
)))
  (CONNECT_DATA=
   (SERVICE_NAME=service_name
)))
```

Note:

[Oracle Net Manager](glossary.md) supports only the creation of one protocol address list for a connect descriptor.

## Connect-Time Failover and Client Load Balancing with Oracle Connection Managers

When a connect descriptor in a `tnsnames.ora` file contains at least two protocol addresses for [Oracle Connection Manager](glossary.md), parameters for connect-time failover and load balancing can be included in the file.

Example 6-4 illustrates failover of multiple Oracle Connection Manager protocol addresses.

Example 6-4 Multiple Oracle Connection Manager Addresses in tnsnames.ora

```
sample1=
 (DESCRIPTION= 
   (SOURCE_ROUTE=yes) 
   (ADDRESS=(PROTOCOL=tcp)(HOST=host1)(PORT=1630))    # 1 
   (ADDRESS_LIST=  
     (FAILOVER=on) 
     (LOAD_BALANCE=off)                               #  2 
     (ADDRESS=(PROTOCOL=tcp)(HOST=host2a)(PORT=1630)) 
     (ADDRESS=(PROTOCOL=tcp)(HOST=host2b)(PORT=1630)))
   (ADDRESS=(PROTOCOL=tcp)(HOST=host3)(PORT=1521))    #  3
   (CONNECT_DATA=(SERVICE_NAME=Sales.us.example.com)))
```

In Example 6-4, the syntax does the following:

1. The client is instructed to connect to an protocol address of the first Oracle Connection Manager, as indicated by:
	```
	(ADDRESS=(PROTOCOL=tcp)(HOST=host1)(PORT=1630))
	```
2. The first Oracle Connection Manager is instructed to connect to the first protocol address of another Oracle Connection Manager. If the first protocol address fails, then it tries the second protocol address. This sequence is specified with the following configuration:
	```
	(ADDRESS_LIST=  
	  (FAILOVER=ON) 
	  (LOAD_BALANCE=off)
	  (ADDRESS=(PROTOCOL=tcp)(HOST=host2a)(PORT=1630)) 
	  (ADDRESS=(PROTOCOL=tcp)(HOST=host2b)(PORT=1630))
	```
3. The Oracle Connection Manager connects to the database service using the following protocol address:
	```
	(ADDRESS=(PROTOCOL=tcp)(HOST=host3)(PORT=1521))
	```

Example 6-5 illustrates client load balancing among two Oracle Connection Managers and two protocol addresses:

Example 6-5 Client Load Balancing in tnsnames.ora

```
sample2=
 (DESCRIPTION= 
   (LOAD_BALANCE=on)                                    # 1
   (FAILOVER=on)
   (ADDRESS_LIST= 
     (SOURCE_ROUTE=yes) 
     (ADDRESS=(PROTOCOL=tcp)(HOST=host1)(PORT=1630))    # 2
     (ADDRESS=(PROTOCOL=tcp)(HOST=host2)(PORT=1521)))
  (ADDRESS_LIST= 
     (SOURCE_ROUTE=yes) 
     (ADDRESS=(PROTOCOL=tcp)(HOST=host3)(port=1630)) 
     (ADDRESS=(PROTOCOL=tcp)(HOST=host4)(port=1521)))
   (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com)))  # 3
```

In Example 6-5, the syntax does the following:

1. The client is instructed to pick an `ADDRESS_LIST` at random and to failover to the other if the chosen `ADDRESS_LIST` fails. This is indicated by the `LOAD_BALANCE` and `FAILOVER` parameters being set to `on`.
2. When an `ADDRESS_LIST` is chosen, the client first connects to the Oracle Connection Manager, using the Oracle Connection Manager protocol address that uses port 1630 indicated for the `ADDRESS_LIST`.
3. The Oracle Connection Manager then connects to the database service, using the protocol address indicated for the `ADDRESS_LIST`.

## Connect Descriptor Descriptions

Each connect descriptor is contained within the DESCRIPTION parameter. Multiple connect descriptors are characterized by the DESCRIPTION\_LIST parameter. These parameters are described in this section.

### DESCRIPTION

Purpose

To specify a container for a connect descriptor. Put this parameter under the `DESCRIPTION_LIST` parameter.

Example

```
net_service_name=
(DESCRIPTION=
  (ADDRESS=...)
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com)))
```

### DESCRIPTION\_LIST

Purpose

To define a list of connect descriptors for a particular net service name.

Example

```
net_service_name= 
(DESCRIPTION_LIST=
 (DESCRIPTION=
  (ADDRESS=...)
  (CONNECT_DATA=(SERVICE_NAME=sales.example.com)))
 (DESCRIPTION=
  (ADDRESS=...)
  (CONNECT_DATA=(SERVICE_NAME=sales2.us.example.com))))
```

## Protocol Address Section

The protocol address section of the `tnsnames.ora` file specifies the protocol addresses of the listener. If there is only one listener protocol address, then use the ADDRESS parameter. If there is more than one address, then use the ADDRESS\_LIST parameter.

### ADDRESS

Purpose

To define a single listener protocol address. Put this parameter under either the `ADDRESS_LIST` parameter or the `DESCRIPTION` parameter.

Example

```
net_service_name=
(DESCRIPTION= 
 (ADDRESS=(PROTOCOL=tcp)(HOST=sales-svr)(PORT=1521))
 (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com))
```

See Also:

[Chapter 4, "Protocol Address Configuration"](protocoladd.md) for descriptions of the correct parameters to use for each protocol

### ADDRESS\_LIST

Purpose

To define a list of protocol addresses. If there is only one listener protocol address, then `ADDRESS_LIST` is not necessary. Put this parameter under either the `DESCRIPTION` parameter or the `DESCRIPTION_LIST` parameter.

Example

```
net_service_name=
 (DESCRIPTION= 
  (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com)))
```

## Optional Parameters for Address Lists

For multiple addresses, the following parameters are available:

- ENABLE
- FAILOVER
- LOAD\_BALANCE
- RECV\_BUF\_SIZE
- SDU
- SEND\_BUF\_SIZE
- SOURCE\_ROUTE
- TYPE\_OF\_SERVICE

### ENABLE

Purpose

The keepalive feature on the supported TCP transports can be enabled for a net service client by putting `(ENABLE=broken)` under the DESCRIPTION parameter in the connect string. The keepalive feature allows the caller to detect a terminated remote server, although typically it takes 2 hours or more to notice. On the client side, the default for `tcp_keepalive` is `off`. Operating system TCP configurables, which vary by platform, define the actual keepalive timing details.

Values

```
BROKEN
```

Example

```
net_service_name=
 (DESCRIPTION= 
  (ENABLE=broken)
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com))
```

### FAILOVER

Purpose

To enable or disable connect-time failover for multiple protocol addresses.

When you set the parameter to `on`, `yes`, or `true`, Oracle Net, at connect time, fails over to a different address if the first protocol address fails. When you set the parameter to `off`, `no`, or `false`, Oracle Net tries one protocol address.

Put this parameter under the `DESCRIPTION_LIST` parameter, the `DESCRIPTION` parameter, or the `ADDRESS_LIST` parameter.

Important:

Do not set the `GLOBAL_DBNAME` parameter in the `SID_LIST_` `listener_name` section of the `listener.ora`. A statically configured global database name disables connect-time failover.

Default

`on` for `DESCRIPTION_LIST`, `DESCRIPTION`, and `ADDRESS_LIST`.

Values

- `yes` | `on` | `true`
- `no` | `off` | `false`

Example

```
net_service_name=
 (DESCRIPTION= 
  (FAILOVER=on)
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com)))
```

### LOAD\_BALANCE

Purpose

To enable or disable client load balancing for multiple protocol addresses.

When you set the parameter to `on`, `yes`, or `true`, Oracle Net progresses the list of addresses in a random sequence, balancing the load on the various listener or Oracle Connection Manager protocol addresses. When you set the parameter to `off`, `no`, or `false`, Oracle Net tries the first address in the address list. If the connection fails and the failover parameter is enabled, then Oracle Net tries the addresses sequentially until one succeeds.

Put this parameter under either the `DESCRIPTION_LIST` parameter, the `DESCRIPTION` parameter, or the `ADDRESS_LIST` parameter.

Default

on for `DESCRIPTION_LIST`

Values

- `yes` | `on` | `true`
- `no` | `off` | `false`

Example

```
net_service_name=
 (DESCRIPTION= 
  (LOAD_BALANCE=on)
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com))
```

### RECV\_BUF\_SIZE

Purpose

To specify, in bytes, the buffer space for receive operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Put this parameter under the `DESCRIPTION` parameter or at the end of the protocol address.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to the operating system-specific documentation for additional information about additional protocols.

Default

The default value for this parameter is specific to the operating system.

Usage

Setting this parameter in the connect descriptor for a client overrides the [RECV\_BUF\_SIZE](sqlnet.md) parameter at the client-side `sqlnet.ora` file.

Example

```
net_service_name
= 
 (DESCRIPTION= 
   (ADDRESS_LIST=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-server)(PORT=1521)
        (RECV_BUF_SIZE=11784))
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-server)(PORT=1521)
        (RECV_BUF_SIZE=11784))
   (CONNECT_DATA=
     (SERVICE_NAME=sales.us.example.com)))
net_service_name
= 
 (DESCRIPTION= 
   (RECV_BUF_SIZE=11784)
   (ADDRESS_LIST=
     (ADDRESS=(PROTOCOL=tcp)(HOST=hr1-server)(PORT=1521)
     (ADDRESS=(PROTOCOL=tcp)(HOST=hr2-server)(PORT=1521))
   (CONNECT_DATA=
     (SERVICE_NAME=hr.us.example.com)))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

### SDU

Purpose

To instruct Oracle Net to optimize the transfer rate of data packets being sent across the network with a specified [session data unit (SDU)](glossary.md) size.

Put this parameter under the `DESCRIPTION` parameter.

Default

8192 bytes (8 KB).

Values

512 to 65535 bytes.

Usage

Setting this parameter in the connect descriptor for a client overrides the [DEFAULT\_SDU\_SIZE](sqlnet.md) parameter at client-side `sqlnet.ora` file.

Example

```
net_service_name
= 
 (DESCRIPTION=
  (SDU=8192)
   (ADDRESS_LIST=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-server)(PORT=1521)))
  (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com))
```

See Also:

Oracle Database Net Services Administrator's Guide for complete SDU usage and configuration information

### SEND\_BUF\_SIZE

Purpose

To specify, in bytes, the buffer space for send operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to the operating system-specific documentation for additional information about additional protocols.

Put this parameter under the `DESCRIPTION` parameter or at the end of the protocol address.

Default

The default value for this parameter is operating system-specific.

Usage

Setting this parameter in the connect descriptor for a client overrides the [SEND\_BUF\_SIZE](sqlnet.md) parameter at the client-side `sqlnet.ora` file.

Example

```
net_service_name
= 
 (DESCRIPTION= 
   (ADDRESS_LIST=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-server)(PORT=1521)
        (SEND_BUF_SIZE=11784))
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-server)(PORT=1521)
        (SEND_BUF_SIZE=11784))
   (CONNECT_DATA=
     (SERVICE_NAME=sales.us.example.com)))
net_service_name
= 
 (DESCRIPTION= 
   (SEND_BUF_SIZE=11784)
   (ADDRESS_LIST=
     (ADDRESS=(PROTOCOL=tcp)(HOST=hr1-server)(PORT=1521)
     (ADDRESS=(PROTOCOL=tcp)(HOST=hr2-server)(PORT=1521))
   (CONNECT_DATA=
     (SERVICE_NAME=hr.us.example.com)))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

### SOURCE\_ROUTE

Purpose

To enable routing through multiple protocol addresses.

When you set to `on` or `yes`, Oracle Net uses each address in order until the destination is reached.

To use Oracle Connection Manager, an initial connection from the client to Oracle Connection Manager is required, and a second connection from Oracle Connection Manager to the listener is required.

Put this parameter under either the `DESCRIPTION_LIST` parameter, the `DESCRIPTION` parameter, or the `ADDRESS_LIST` parameter.

Default

off

Values

- `yes` | `on`
- `no` | `off`

Example

```
net_service_name=
 (DESCRIPTION= 
  (SOURCE_ROUTE=on)
  (ADDRESS=(PROTOCOL=tcp)(HOST=cman-pc)(PORT=1630))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales.us.example.com))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/advcfg.htm#NETAG013) for complete configuration information

### TYPE\_OF\_SERVICE

Purpose

To specify the type of service to use for an Oracle Rdb database. This parameter should only be used if the application supports both an Oracle Rdb and Oracle database service, and you want the application to load balance between the two.

Put this parameter under the `DESCRIPTION` parameter.

Example

```
net_service_name=
 (DESCRIPTION_LIST=
  (DESCRIPTION=
   (ADDRESS=...)
   (CONNECT_DATA= 
    (SERVICE_NAME=generic)
    (RDB_DATABASE=[.mf]mf_personal.rdb)
    (GLOBAL_NAME=alpha5))
   (TYPE_OF_SERVICE=rdb_database))
  (DESCRIPTION=
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com))
   (TYPE_OF_SERVICE=oracle11_database)))
```

## Connection Data Section

The connection data section of the `tnsnames.or` a file specifies the name of the destination service. The following parameters are available:

- CONNECT\_DATA
- FAILOVER\_MODE
- GLOBAL\_NAME
- HS
- INSTANCE\_NAME
- RDB\_DATABASE
- SERVER
- SERVICE\_NAME

### CONNECT\_DATA

Purpose

To define the service to which to connect, such as `SERVICE_NAME`.

Put this parameter under the `DESCRIPTION` parameter.

Usage Notes

`CONNECT_DATA` permits the following additional parameters:

- FAILOVER\_MODE
- GLOBAL\_NAME
- HS
- INSTANCE\_NAME
- RDB\_DATABASE
- SERVER
- SERVICE\_NAME

Example

```
net_service_name=
 (DESCRIPTION= 
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521))
  (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com)))
```

### FAILOVER\_MODE

Purpose

To instruct Oracle Net to fail over to a different listener if the first listener fails during run time. Depending upon the configuration, session or any `SELECT` statements which were in progress are automatically failed over.

This type of failover is called [Transparent Application Failover (TAF)](glossary.md) and should not be confused with the connect-time failover FAILOVER parameter.

Put this parameter under the `CONNECT_DATA` parameter.

Additional Parameters

`FAILOVER_MODE` supports the following parameters:

- `BACKUP`: Specify the failover node by its net service name. A separate net service name must be created for the failover node.
- `TYPE`: Specify the type of failover. Three types of Oracle Net failover functionality are available by default to [Oracle Call Interface (OCI)](glossary.md) applications:
	- `SESSION`: Fails over the session. For example, if a user's connection is lost, then a new session is automatically created for the user on the backup. This type of failover does not attempt to recover selects.
		- `SELECT`: Allows users with open cursors to continue fetching them after failure. However, this mode involves overhead on the client side in normal select operations.
		- `NONE`: This is the default, in which no failover functionality is used. This can also be explicitly specified to prevent failover from happening.
- `METHOD`: Specify how fast failover is to occur from the primary node to the backup node:
	- `BASIC`: Establishes connections at failover time. This option requires almost no work on the backup database server until failover time.
		- `PRECONNECT`: Pre-establishes connections. This provides faster failover but requires that the backup instance be able to support all connections from every supported instance.
- `RETRIES`: Specify the number of times to attempt to connect after a failover. If `DELAY` is specified, then `RETRIES` defaults to five retry attempts.
- `DELAY`: Specify the amount of time in seconds to wait between connect attempts. If `RETRIES` is specified, then `DELAY` defaults to one second.

Note:

If a callback function is registered, then `RETRIES` and `DELAY` parameters are ignored.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/advcfg.htm#NETAG455) for additional configuration information

### GLOBAL\_NAME

Purpose

To identify the Oracle Rdb database.

Put this parameter under the `CONNECT_DATA` parameter.

Example

```
net_service_name
= 
 (DESCRIPTION= 
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=generic)
    (RDB_DATABASE=[.mf]mf_personal.rdb)
    (GLOBAL_NAME=alpha5)))
```

### HS

Purpose

To direct Oracle Net to connect to a non-Oracle system through [Heterogeneous Services](glossary.md).

Put this parameter under the `CONNECT_DATA` parameter.

Default

None

Values

```
ok
```

Example

```
net_service_name
= 
 (DESCRIPTION=
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SID=sales6)
    (HS=ok)))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/advcfg.htm#NETAG0131) for complete configuration information

### INSTANCE\_NAME

Purpose

To identify the database instance to access. Set the value to the value specified by the `INSTANCE_NAME` parameter in the initialization parameter file.

Put this parameter under the `CONNECT_DATA` parameter.

Example

```
net_service_name
= 
 (DESCRIPTION=
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com)
    (INSTANCE_NAME=sales1)))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm#NETAG009) for additional information about the use of `INSTANCE_NAME`

### RDB\_DATABASE

Purpose

To specify the file name of an Oracle Rdb database.

Put this parameter under the `CONNECT_DATA` parameter.

Example

```
net_service_name
= 
 (DESCRIPTION= 
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com)
    (RDB_DATABASE= [.mf]mf_personal.rdb)))
```

### SERVER

Purpose

To direct the listener to connect the client to a specific type of [service handler](glossary.md).

Put this parameter under the `CONNECT_DATA` parameter.

Values

- `dedicated` to specify whether client requests be served by [dedicated server](glossary.md)
- `shared` to specify whether client request be served by [shared server](glossary.md)
- `pooled` to get a connection from the connection pool if database resident connection pooling is enabled on the server

Notes:

Shared server must be configured in the database initialization file in order for the client to connect to the database with a shared server process.

The [USE\_DEDICATED\_SERVER](sqlnet.md) parameter in the `sqlnet.ora` file overrides this parameter.

Example

```
net_service_name
= 
 (DESCRIPTION=
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com)
    (SERVER=dedicated)))
```

See Also:

- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/concepts.htm#NETAG454) for additional information about database resident connection pooling
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci09adv.htm#LNOCI090) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN12349) for additional information about enabling and configuring database resident connection pooling

### SERVICE\_NAME

Purpose

To identify the Oracle Database database service to access. Set the value to a value specified by the `SERVICE_NAMES` parameter in the initialization parameter file.

Put this parameter under the `CONNECT_DATA` parameter.

Example

```
net_service_name
= 
 (DESCRIPTION=
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=sales.us.example.com)))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm#NETAG009) for additional information about the use of the `SERVICE_NAME` parameter

## Security Section

The security section of the `tnsnames.or` a file specifies the following security-related parameters for use with Oracle Advanced Security features:

- SECURITY
- SSL\_SERVER\_CERT\_DN

### SECURITY

Purpose

To enable secure connections. Put this parameter under the `DESCRIPTION` parameter.

Usage Notes

`SECURITY` permits the SSL\_SERVER\_CERT\_DN parameter.

Example

```
net_service_name
=
 (DESCRIPTION= 
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521))
  (CONNECT_DATA=
   (SERVICE_NAME=sales.us.example.com))
   (SECURITY=
    (SSL_SERVER_CERT_DN="cn=sales,cn=OracleContext,dc=us,dc=acme,dc=com")))
```

### SSL\_SERVER\_CERT\_DN

Purpose

To specify the [distinguished name (DN)](glossary.md) of the database server. The client uses this information to obtain the list of DNs it expects for each of the servers, enforcing the database server DN to match its service name.

Usage Notes

Use this parameter with the `sqlnet.ora` parameter [SSL\_SERVER\_DN\_MATCH](sqlnet.md) to enable server DN matching.

Example

```
net_service_name
= 
 (DESCRIPTION=
   (ADDRESS=...)
   (ADDRESS=...)
   (CONNECT_DATA=
    (SERVICE_NAME=finance.us.example.com))
   (SECURITY=
    (SSL_SERVER_CERT_DN="cn=finance,cn=OracleContext,dc=us,dc=acme,dc=com")))
```

See Also:

[Oracle Database Security Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=DBSEG070)

## Timeout Parameters

The timeout section of the `tnsnames.or` a file provides the ability to specify timeout and retry configuration through the TNS connect string. The following parameters can now be set at the `DESCRIPTION` level of a connect string:

- CONNECT\_TIMEOUT
- RETRY\_COUNT
- TRANSPORT\_CONNECT\_TIMEOUT

### CONNECT\_TIMEOUT

Purpose

To specify the timeout duration in seconds for a client to establish an Oracle Net connection to an Oracle database. Put this parameter under the `DESCRIPTION` parameter.

Usage Notes

The timeout interval specified by `CONNECT_TIMEOUT` is a superset of the TCP connect timeout interval. It includes the time to be connected to the database instance providing the requested service, not just the duration of the TCP connection.

The default value of `CONNECT_TIMEOUT` is dependent on the `TCP_CONNECT_TIMEOUT` parameter. Oracle recommends setting the `CONNECT_TIMEOUT` value slightly greater than the `TCP_CONNECT_TIMEOUT` value.

The timeout interval is applicable for each `ADDRESS` in an `ADDRESS_LIST`, and each IP address to which a host name is mapped.

The `CONNECT_TIMEOUT` parameter is equivalent to the `sqlnet.ora` parameter `SQLNET.OUTBOUND_CONNECT_TIMEOUT` and overrides it.

Example

```
net_service_name
=
 (DESCRIPTION= 
  (CONNECT_TIMEOUT=10)(RETRY_COUNT=3)
  (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521)))
  (CONNECT_DATA=
   (SERVICE_NAME=sales.us.example.com)))
```

### RETRY\_COUNT

Purpose

To specify the number of times an `ADDRESS` list is traversed before the connection attempt is terminated. The default value is 0.

Put this parameter under the `DESCRIPTION` parameter.

Usage Notes

When a `DESCRIPTION_LIST` is specified, each `DESCRIPTION` is traversed multiple times based on the specified number of retries. `RETRY_COUNT` is only supported at `DESCRIPTION` level in connect string.

When using SCAN listeners in an Oracle Real Application Clusters environment, with `FAILOVER = on`, setting the `RETRY_COUNT` parameter to `2` means the three SCAN IP addresses are traversed three times each, such that there are nine connect attempts (3 \* 3).

Example

```
net_service_name
= 
(DESCRIPTION_LIST=
 (DESCRIPTION=
  (CONNECT_TIMEOUT=10)(RETRY_COUNT=3)
  (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales1a-svr)(PORT=1521))
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales1b-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales1.example.com)))
 (DESCRIPTION=
  (CONNECT_TIMEOUT=60)(RETRY_COUNT=1)
  (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales2a-svr)(PORT=1521))
   (ADDRESS=(PROTOCOL=tcp)(HOST=sales2b-svr)(PORT=1521)))
  (CONNECT_DATA=(SERVICE_NAME=sales2.us.example.com))))
```

### TRANSPORT\_CONNECT\_TIMEOUT

Purpose

To specify the transportation timeout duration in seconds for a client to establish an Oracle Net connection to an Oracle Database.

This parameter is put under the `DESCRIPTION` parameter.

Usage Notes

The `TRANSPORT_CONNECT_TIMEOUT` parameter specifies the time, in seconds, for a client to establish a TCP connection to the database server. The default value is 60 seconds.

The timeout interval is applicable for each `ADDRESS` in an `ADDRESS_LIST` description, and each IP address that a host name is mapped. The `TRANSPORT_CONNECT_TIMEOUT` parameter is equivalent to the sqlnet.ora parameter `TCP.CONNECT_TIMEOUT`, and overrides it.

Example

```
net_service_name =
  (DESCRIPTION=
    (TRANSPORT_CONNECT_TIMEOUT=10)
    (ADDRESS_LIST=
      (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-svr)(PORT=1521))
      (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-svr)(PORT=1521))
    (CONNECT_DATA=
      (SERVICE_NAME=sales.us.example.com)))
```
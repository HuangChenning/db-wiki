---
title: Oracle Net Listener Parameters (listener.ora)
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/listener.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 7 Oracle Net Listener Parameters (listener.ora)

This chapter provides a complete listing of the `listener.ora` file configuration parameters.

This chapter contains the following topics:

## Overview of Oracle Net Listener Configuration File

Oracle Net Listener configuration, stored in the `listener.ora` file, consists of the following elements:

- Name of the listener
- Protocol addresses that the listener is accepting connection requests on
- Database services
- Control parameters

Dynamic [service registration](glossary.md), eliminates the need for static configuration of supported services. However, static service configuration is required if you plan to use Oracle Enterprise Manager.

By default, the `listener.ora` file is located in the `ORACLE_HOME/network/admin` directory. The `listener.ora` file can also be stored the following locations:

- The directory specified by the `TNS_ADMIN` environment variable or registry value
- On Linux and UNIX operating systems, the global configuration directory. For example, on the Solaris Operating System, this directory is `/var/opt/oracle`.
	See Also:
	Oracle operating system-specific documentation

It is possible to configure multiple listeners, each with unique name, in one `listener.ora` file. Multiple listener configurations are possible because each of the top-level configuration parameters has a suffix of the listener name or is the listener name itself.

Note:

It is often useful to configure multiple listeners in one `listener.ora` file. However, Oracle recommends running only one listener for each node in most customer environments.

Example 7-1 shows a `listener.ora` file for a listener named `LISTENER`, which is the default name of the listener.

Example 7-1 listener.ora File

```
LISTENER=
  (DESCRIPTION=
    (ADDRESS_LIST=
      (ADDRESS=(PROTOCOL=tcp)(HOST=sale-server)(PORT=1521))
      (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))))
SID_LIST_LISTENER=
  (SID_LIST=
    (SID_DESC=
      (GLOBAL_DBNAME=sales.us.example.com)
      (ORACLE_HOME=/oracle11g)
      (SID_NAME=sales))
    (SID_DESC=
      (SID_NAME=plsextproc)
      (ORACLE_HOME=/oracle11g)
      (PROGRAM=extproc)))
```

## Protocol Address Parameters

The [protocol address](glossary.md) section of the `listener.ora` file defines the protocol addresses on which the listener is accepting connection requests. This section describes the most common parameters used in protocol addresses. The `ADDRESS_LIST` parameter is also supported.

See Also:

[Chapter 4, "Protocol Address Configuration"](protocoladd.md) for additional information about the `ADDRESS_LIST` parameter

This section lists and describes the following parameters:

- ADDRESS
- DESCRIPTION
- IP
- QUEUESIZE
- RECV\_BUF\_SIZE
- SEND\_BUF\_SIZE

### ADDRESS

Purpose

To specify a single listener protocol address.

Put this parameter under the `DESCRIPTION` parameter.

Example

```
listener_name=
 (DESCRIPTION=
  (ADDRESS=(PROTOCOL=tcp)(HOST=hr-server)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))
```

See Also:

[Chapter 4, "Protocol Address Configuration"](protocoladd.md) for descriptions of the correct parameters to use for each type of support protocol

### DESCRIPTION

Purpose

To contain listener protocol addresses.

Example

```
listener_name=
 (DESCRIPTION=
  (ADDRESS=(PROTOCOL=tcp)(HOST=hr-server)(PORT=1521))
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))
```

### IP

Purpose

To determine which IP address the listener listens on when a host name is specified. This parameter is only applicable when the `HOST` parameter specifies a host name.

Values

- `FIRST`
	Listen on the first IP address returned by the DNS resolution of the host name. If the user wants the listener to listen on the first IP to which the specified host name resolves, then the address must be qualified with `(IP=FIRST)`.
- `V4_ONLY`
	List only on IPv4 addresses.
- `V6_ONLY`
	Listen only on IPv6 addresses.

Default

This feature is disabled by default.

Example

```
listener_name=
 (DESCRIPTION=
  (ADDRESS=(PROTOCOL=tcp)(HOST=rancode1-vip)(PORT=1522)(IP=V6_ONLY))
```

### QUEUESIZE

Purpose

To specify the number of concurrent connection requests that the listener can accept on a TCP/IP or IPC listening endpoint (protocol address).

Put this parameter at the end of the protocol address with its value set to the expected number of concurrent connection requests.

Default

The default number of concurrent connection requests is operating system specific.

Usage Notes

The number of concurrent connection requests is dependent on the platform and listener usage scenarios. If the listener is heavily-loaded, then set the parameter to a higher number.

Example

```
listener_name=
 (DESCRIPTION=
  (ADDRESS=(PROTOCOL=tcp)(HOST=hr-server)(PORT=1521)(QUEUESIZE=20)))
```

See Also:

[Oracle Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG0101) for additional information about configuring this parameter

### RECV\_BUF\_SIZE

Purpose

To specify, in bytes, the buffer space for receive operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to the operating system-specific documentation for additional information about additional protocols that support this parameter.

Put this parameter under the `DESCRIPTION` parameter or at the end of the protocol address with its value set to the expected number of bytes.

Default

The default value for this parameter is operating system-specific.

Example

```
listener_name=
  (DESCRIPTION=
    (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)
       (RECV_BUF_SIZE=11784))
    (ADDRESS=(PROTOCOL=ipc)(KEY=extproc)
       (RECV_BUF_SIZE=11784)))
listener_name=
  (DESCRIPTION=
    (RECV_BUF_SIZE=11784))
    (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)
    (ADDRESS=(PROTOCOL=ipc)(KEY=extproc)))
```

See Also:

[Oracle Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

### SEND\_BUF\_SIZE

Purpose

To specify, in bytes, the buffer space for send operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to operating system-specific documentation for additional information about additional protocols that support this parameter.

Put this parameter under the `DESCRIPTION` parameter or at the end of the protocol address.

Default

The default value for this parameter is operating system-specific.

Example

```
listener_name=
  (DESCRIPTION=
    (ADDRESS_LIST=
      (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)
       (SEND_BUF_SIZE=11280))
      (ADDRESS=(PROTOCOL=ipc)(KEY=extproc)
       (SEND_BUF_SIZE=11280))))
listener_name=
  (DESCRIPTION=
    (ADDRESS_LIST=
      (SEND_BUF_SIZE=11280))
      (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)
      (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))))
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

## Connection Rate Limiter Parameters

The connection rate limiter feature in the Oracle Net Listener enables a DBA to limit the number of new connections handled by the listener. When this feature is enabled, Oracle Net Listener imposes a user-specified maximum limit on the number of new connections handled by the listener every second.

Depending on the configuration, the rate can be applied to a collection of endpoints, or to a specific endpoint.

This feature is controlled through the following two `listener.ora` configuration parameters:

- CONNECTION\_RATE\_listener name
- RATE\_LIMIT

### CONNECTION\_RATE\_listener name

Purpose

To specify a global rate that is enforced across all listening endpoints that are rate-limited. When this parameter is specified, it overrides any endpoint-level numeric rate values that might be specified.

Syntax

```
CONNECTION_RATE_listener_name=number_of_connections_per_second
```

### RATE\_LIMIT

Purpose

To indicate that a particular listening endpoint is rate limited. The parameter is specified in the `ADDRESS` section of the listener endpoint configuration.

Syntax

```
LISTENER= (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=yes))
   )
```
- When the `RATE_LIMIT` parameter is set to `yes`, the end-point is included in the enforcement of a listener-wide connection rate. This is used with the `CONNECTION_RATE_` `listener_name` parameter.
- When the `RATE_LIMIT` parameter is set to a value greater than `0`, the rate limit is enforced at that endpoint level.

Examples

The following examples use the `CONNECTION_RATE_` `listener name` and `RATE_LIMIT` parameters.

Example 1

```
CONNECTION_RATE_LISTENER=10

LISTENER= 
  (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=yes))
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=yes))
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1523))
   )
```

In the preceding example, the total number of new connections through ports 1521 and 1522 is limited at 10 every second. Connections through port 1523 are not limited and do not count towards the overall rate of 10 connections every second.

Example 2

```
LISTENER= (ADDRESS_LIST=
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=5))
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=10))
   (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1523))
   )
```

In the preceding example, the connection rates are enforced at the endpoint level. A maximum of 5 connections are processed through port 1521 every second. The limit for connections through port 1522 is 10 every second. Connections through port 1523 are not limited.

Note:

The global `CONNECTON_RATE_` `listener_name` parameter is not specified in the preceding configuration. If it is specified, then the limits on ports 1521 and 1522 are ignored, and the global value is used instead.

## Control Parameters

This section describes the following parameters that control the behavior of the listener:

- ADMIN\_RESTRICTIONS\_listener\_name
- CRS\_NOTIFICATION\_listener\_name
- DEFAULT\_SERVICE\_listener\_name
- INBOUND\_CONNECT\_TIMEOUT\_listener\_name
- REGISTRATION\_EXCLUDED\_NODES\_listener\_name
- REGISTRATION\_INVITED\_NODES\_listener\_name
- SAVE\_CONFIG\_ON\_STOP\_listener\_name
- SSL\_CLIENT\_AUTHENTICATION
- SUBSCRIBE\_FOR\_NODE\_DOWN\_EVENT\_listener\_name
- VALID\_NODE\_CHECKING\_REGISTRATION\_listener\_name
- WALLET\_LOCATION

### ADMIN\_RESTRICTIONS\_listener\_name

Purpose

To restrict run-time administration of the listener.

Setting `ADMIN_RESTRICTIONS_` `listener_name` `=on` disables the run-time modification of parameters in `listener.ora`. That is, the listener refuses to accept [SET](lsnrctl.md) commands that alter its parameters. To change any of the parameters in `listener.ora`, including `ADMIN_RESTRICTIONS_` `listener_name` itself, modify the `listener.ora` file manually and reload its parameters (using the [RELOAD](lsnrctl.md) command) for the new changes to take effect without explicitly stopping and restarting the listener.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/dispatcher.htm#NETAG012) for additional information about password security of the listener

Default

off

Example

```
ADMIN_RESTRICTIONS_listener=on
```

### CRS\_NOTIFICATION\_listener\_name

Purpose

To set notification. By default, the Oracle Net listener notifies Cluster Ready Services (CRS) when it is started or stopped. These notifications allow CRS to manage the listener in an Oracle Real Application Clusters environment. This behavior can be prevented by setting the `CRS_NOTIFICATION_` `listener_name` parameter to `off`.

Default

on

Values

```
on | off
```

### DEFAULT\_SERVICE\_listener\_name

Purpose

To enable users to connect to the database without having to specify a service name from the client side.

In Oracle Database 11g, when a client tries to connect to the database the connection request passes through the listener. The listener may be servicing several different databases. If a service name is configured in this parameter, then users may not necessarily need to specify a service name in the connect syntax. If a user specifies a service name, then the listener connects the user to that specific database, otherwise the listener connects to the service name specified by the `DEFAULT_SERVICE_` `listener_name` parameter.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG255) for additional information about the Easy Connect naming method

Default

There is no default value for the `DEFAULT_SERVICE_` `listener_name` parameter. If this parameter is not configured and a user does not specify a fully-qualified service name in the connect syntax, then the connection attempt fails. This parameter only accepts one value.

Example

```
DEFAULT_SERVICE_LISTENER=sales.us.example.com
```

### INBOUND\_CONNECT\_TIMEOUT\_listener\_name

Purpose

To specify the time, in seconds, for the client to complete its connect request to the listener after the network connection had been established.

If the listener does not receive the client request in the time specified, then it terminates the connection. In addition, the listener logs the IP address of the client and an `ORA-12525:TNS: listener has not received client's request in time allowed` error message to the `listener.log` file.

To protect both the listener and the database server, Oracle recommends setting this parameter in combination with the [SQLNET.INBOUND\_CONNECT\_TIMEOUT](sqlnet.md) parameter in the `sqlnet.ora` file. When specifying values for these parameters, consider the following recommendations:

- Set both parameters to an initial low value.
- Set the value of the `INBOUND_CONNECT_TIMEOUT_` `listener_name` parameter to a lower value than the `SQLNET.INBOUND_CONNECT_TIMEOUT` parameter.

For example, you can set the `INBOUND_CONNECT_TIMEOUT_` `listener_name` parameter to 2 seconds and the `INBOUND_CONNECT_TIMEOUT` parameter to 3 seconds. If clients are unable to complete connections within the specified time due to system or network delays that are normal for the particular environment, then increment the time as needed.

Default

60 seconds

Example

```
INBOUND_CONNECT_TIMEOUT_listener=2
```

See Also:

Oracle Database Net Services Administrator's Guide for additional information about configuring these parameters

### REGISTRATION\_EXCLUDED\_NODES\_listener\_name

Purpose

To specify the list of nodes that cannot register with the listener. The list can include host names or CIDR notation for IPv4 and IPv6 addresses. The wildcard format (`*`) is supported for IPv4 addresses. The presence of a host name in the list results in the inclusion of all IP addresses mapped to the host name. The host name should be consistent with the public network interface.

Values

Valid nodes and subnet IP addresses or names.

Usage Notes

If the `REGISTRATION_INVITED_NODES_` `listener_name` parameter and the `REGISTRATION_EXCLUDED_NODES` `_listener_name` parameter are set, then the `REGISTRATION_EXCLUDED_NODES_` `listener_name` parameter is ignored.

Example

```
REGISTRATION_EXCLUDED_NODES_listener= (10.1.26.*, 10.16.40.0/24, \
                                       2001:DB8:3eff:fe38, node2)
```

### REGISTRATION\_INVITED\_NODES\_listener\_name

Purpose

To specify the list of node that can register with the listener. The list can include host names or CIDR notation for IPv4 and IPv6 addresses. The wildcard format (`*`) is supported for IPv4 addresses. The presence of a host name in the list results in the inclusion of all IP addresses mapped to the host name. The host name should be consistent with the public network interface.

Values

Valid nodes and subnet IP addresses or names.

Usage Notes

If the `REGISTRATION_INVITED_NODES_` `listener_name` parameter and the `REGISTRATION_EXCLUDED_NODES` `_listener_name` parameter are set, then the `REGISTRATION_EXCLUDED_NODES_` `listener_name` parameter is ignored.

Example

```
REGISTRATION_INVITED_NODES_listener= (10.1.35.*, 10.1.34.0/24, \
                                      2001:DB8:fe38:7303, node1)
```

### SAVE\_CONFIG\_ON\_STOP\_listener\_name

Purpose

To specify whether run-time configuration changes are saved into the `listener.ora` file.

When you set the parameter to `true`, any parameters that were modified while the listener was running using the Listener Control utility [SET](lsnrctl.md) command are saved to the `listener.ora` file when the [STOP](lsnrctl.md) command is issued. When you set the parameter to `false`, the Listener Control utility does not save the run-time configuration changes to the `listener.ora` file.

Default

false

Values

```
true | false
```

Example

```
SAVE_CONFIG_ON_STOP_listener=true
```

### SSL\_CLIENT\_AUTHENTICATION

Purpose

To specify whether a client is authenticated using the [Secure Sockets Layer (SSL)](glossary.md).

Default

true

Values

```
true | false
```

Usage Notes

The database server authenticates the client. Therefore, this value should be set to `false.` If this parameter is set to `true`, then the listener attempts to authenticate the client, which can result in a failure.

Example

```
SSL_CLIENT_AUTHENTICATION=false
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SUBSCRIBE\_FOR\_NODE\_DOWN\_EVENT\_listener\_name

Purpose

To subscribe to Oracle Notification Service (ONS) notifications for downed events. By default, the listener subscribes to the ONS node down event on startup, if ONS is available. This subscription enables the listener to remove the affected service when it receives node down event notification from ONS. The listener uses asynchronous subscription for the event notification. Alter this behavior setting `SUBSCRIBE_FOR_NODE_DOWN_EVENT_` `listener_name` `=off` in `listener.ora`.

Default

on

Values

```
on | off
```

### VALID\_NODE\_CHECKING\_REGISTRATION\_listener\_name

Purpose

To determine whether valid node checking registration is performed, or the subnet is allowed. When set to `on`, valid node checking registration is performed at the listener for any incoming registration request, and only local IP addresses are allowed.

Default

off

Values

- `off | 0` to specify valid node checking registration is off, and no checking is performed.
- `on | 1 | local` to specify valid node checking registration is on, and all local IP addresses can register. If a list of invited nodes is set, then all IP addresses, host names, or subnets in the list as well as local IP addresses are allowed.
- `subnet | 2` to specify valid node checking registration is on, and all machines in the local subnets are allowed to register. If a list of invited nodes is set, then all nodes in the local subnets as well as all IP addresses, host names and subnets in the list are allowed.

Example

```
VALID_NODE_CHECKING_REGISTRATION_listener=on
```

### WALLET\_LOCATION

Purpose

To specify the location of wallets. Wallets are certificates, keys, and trustpoints processed by SSL that allow for secure connections.

Syntax

Oracle wallets on file system:

```
WALLET_LOCATION=
  (SOURCE=
    (METHOD=file)
    (METHOD_DATA=
       (DIRECTORY=directory)
       [(PKCS11=TRUE/FALSE)]))
```

Microsoft certificate store:

```
WALLET_LOCATION=
  (SOURCE=
     (METHOD=mcs))
```

Oracle wallets in the Microsoft Windows registry:

```
WALLET_LOCATION=
   (SOURCE=
      (METHOD=reg)
      (METHOD_DATA=
         (KEY=registry_key)))
```

Entrust wallets:

```
WALLET_LOCATION=
   (SOURCE=
      (METHOD=entr)
      (METHOD_DATA=
         (PROFILE=file.epf)
         (INIFILE=file.ini)))
```

Additional Parameters

The following additional parameters are available for `WALLET_LOCATION`:

- `SOURCE`: Type of storage for wallets and storage location.
- `METHOD`: Type of storage.
- `METHOD_DATA`: Storage location.
- `DIRECTORY`: Location of Oracle wallets on file system.
- `KEY`: Wallet type and location in the Microsoft Windows registry.
- `PROFILE`: Entrust profile file (`.epf`).
- `INIFILE`: Entrust initialization file (`.ini`).

Default

None

Usage Notes

- The key/value pair for Microsoft certificate store (MCS) omits the `METHOD_DATA` parameter because MCS does not use wallets. Instead, Oracle PKI (public key infrastructure) applications obtain certificates, trustpoints and private keys directly from the user's profile.
- If an Oracle wallet is stored in the Microsoft Windows registry and the wallet's `key` (`KEY)` is `SALESAPP`, then the storage location of the encrypted wallet is `HKEY_CURRENT_USER\SOFTWARE\ORACLE\WALLETS\SALESAPP\EWALLET.P12`. The storage location of the decrypted wallet is `HKEY_CURRENT_USER\SOFTWARE\ORACLE\WALLETS\SALESAPP\CWALLET.SSO.`

Examples

Oracle wallets on file system:

```
WALLET_LOCATION=  
  (SOURCE=
      (METHOD=file)
      (METHOD_DATA=  
         (DIRECTORY=/etc/oracle/wallets/databases)))
```

Microsoft certificate store:

```
WALLET_LOCATION=
   (SOURCE=
     (METHOD=mcs))
```

Oracle Wallets in the Microsoft Windows registry:

```
WALLET_LOCATION=
   (SOURCE=
     (METHOD=REG)
     (METHOD_DATA=
        (KEY=SALESAPP)))
```

Entrust Wallets:

```
WALLET_LOCATION=
   (SOURCE=
     (METHOD=entr)
     (METHOD_DATA=
       (PROFILE=/etc/oracle/wallets/test.epf)
       (INIFILE=/etc/oracle/wallets/test.ini)))
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

## ADR Diagnostic Parameters for Oracle Net Listener

Beginning with Oracle Database 11g, Oracle Database includes an advanced fault diagnosability infrastructure for preventing, detecting, diagnosing, and resolving problems. The problems are critical errors such as those caused by database code bugs, metadata corruption, and customer data corruption.

When a critical error occurs, it is assigned an incident number, and diagnostic data for the error, such as traces and dumps, are immediately captured and tagged with the incident number. The data is then stored in the [Automatic Diagnostic Repository (ADR)](glossary.md), a file-based repository outside the database.

This section includes the parameters used when [ADR](glossary.md) is enabled (when `DIAG_ADR_ENABLED_` `listener_name` is set to `on`). "Non-ADR Diagnostic Parameters for Oracle Net Listener" includes those used when ADR is disabled (when `DIAG_ADR_ENABLED_` `listener_name` is set to `off`). Non-ADR parameters listed in the `listener.ora` file are ignored when ADR is enabled.

- ADR\_BASE\_listener\_name
- DIAG\_ADR\_ENABLED\_listener\_name
- LOGGING\_listener\_name
- TRACE\_LEVEL\_listener\_name
- TRACE\_TIMESTAMP\_listener\_name

### ADR\_BASE\_listener\_name

Purpose

To specify the base directory in to which tracing and logging incidents are stored when ADR is enabled.

Default

The default is `ORACLE_BASE`, or `ORACLE_HOME/log` if `ORACLE_BASE` is not defined.

Values

Any valid directory path to a directory with write permission.

Example

```
ADR_BASE=/oracle/network/trace
```

### DIAG\_ADR\_ENABLED\_listener\_name

Purpose

To indicate whether ADR tracing is enabled.

Usage Notes

When the `DIAG_ADR_ENABLED_` `listener_name` parameter is set to `on`, then ADR file tracing is used. When the `DIAG_ADR_ENABLED_` `listener_name` parameter is set to `off`, then non-ADR file tracing is used.

Default

on

Values

`on` | `off`

Example

```
DIAG_ADR_ENABLED=on
```

### LOGGING\_listener\_name

Purpose

To turn logging on or off. This parameter is also applicable when non-ADR tracing is used.

Default

on

Values

`on` | `off`

Example

```
LOGGING_listener=on
```

### TRACE\_LEVEL\_listener\_name

Purpose

To turn listener tracing on, at a specific level, or off. This parameter is also applicable when non-ADR tracing is used.

Default

off | 0

Values

- `off` or `0` for no trace output
- `user` or `4` for user trace information
- `admin` or `10` for administration trace information
- `support` or `16` for Oracle Support Services trace information

Example

```
TRACE_LEVEL_listener=admin
```

### TRACE\_TIMESTAMP\_listener\_name

Purpose

To add a time stamp in the form of `dd-mon-yyyy hh:mi:ss:mil` to every trace event in the trace file for the listener. This parameter is used with the TRACE\_LEVEL\_listener\_name parameter. This parameter is also applicable when non-ADR tracing is used.

Default

on

Values

- `on` | `true`
- `off` | `false`

Example

```
TRACE_TIMESTAMP_listener=true
```

## Non-ADR Diagnostic Parameters for Oracle Net Listener

This section lists the parameters used when ADR is disabled (when `DIAG_ADR_ENABLED` `listener_name` is set to `off`). "ADR Diagnostic Parameters for Oracle Net Listener" includes the parameters when ADR is enabled.

Notes:

The default value of DIAG\_ADR\_ENABLED\_listener\_name is `on`. Therefore, the `DIAG_ADR_ENABLED_` `listener_name` parameter must explicitly be set to `off` to use non-ADR tracing.

- LOG\_DIRECTORY\_listener\_name
- LOG\_FILE\_listener\_name
- TRACE\_FILELEN\_listener\_name
- TRACE\_FILENO\_listener\_name

### LOG\_DIRECTORY\_listener\_name

Purpose

To specify the destination directory of the listener log file. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/log
```

Example

```
LOG_DIRECTORY_listener=/oracle/network/admin/log
```

### LOG\_FILE\_listener\_name

Purpose

To specify the name of the log file for the listener. Use this parameter when ADR is not enabled.

Default

`listener.log`

Example

```
LOG_FILE_listener=list.log
```

### TRACE\_DIRECTORY\_listener\_name

Purpose

To specify the destination directory of the listener trace file. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/trace
```

Example

```
TRACE_DIRECTORY_listener=/oracle/network/admin/trace
```

### TRACE\_FILE\_listener\_name

Purpose

To specify the name of the trace file for the listener. Use this parameter when ADR is not enabled.

Default

```
listener.trc
```

Example

```
TRACE_FILE_listener=list.trc
```

### TRACE\_FILELEN\_listener\_name

Purpose

To specify the size of the listener trace files in kilobytes (KB). When the size is met, the trace information is written to the next file. The number of files is specified using the TRACE\_FILENO\_listener\_name parameter. Use this parameter when ADR is not enabled.

Default

Unlimited

Example

```
TRACE_FILELEN_listener=100
```

### TRACE\_FILENO\_listener\_name

Purpose

To specify the number of trace files for listener tracing. When this parameter is set along with the TRACE\_FILELEN\_listener\_name parameter, trace files are used in a cyclical fashion. The first file is filled first, then the second file, and so on. When the last file has been filled, the first file is re-used, and so on.

The trace file names are distinguished from one another by their sequence number. For example, if the default trace file of `listener.trc` is used, and this parameter is set to 3, then the trace files would be named `listener1.trc`, `listener2.trc` and `listener3.trc`.

In addition, trace events in the trace files are preceded by the sequence number of the file. Use this parameter when ADR is not enabled.

Default

1

Example

```
TRACE_FILENO_listener=3
```

## Class of Secure Transports Parameters

The class of secure transports (COST) parameters specify a list of transports that are considered secure for administration and registration of a particular listener. The COST parameters identify which transports are considered secure for that installation and whether the administration of a listener requires secure transports. Configuring these parameters is optional.

The following are the COST parameters:

- DYNAMIC\_REGISTRATION\_listener\_name
- SECURE\_CONTROL\_listener\_name
- SECURE\_REGISTER\_listener\_name
- SECURE\_PROTOCOL\_listener\_name

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG0102) for additional information about COST parameters and listener security

### DYNAMIC\_REGISTRATION\_listener\_name

Purpose

To enable or disable dynamic registration. When set to `on`, the listener accepts dynamic registration. When set to `off`, the listener refuses dynamic registration. Static registrations are not affected by this parameter.

Syntax

```
DYNAMIC_REGISTRATION_listener_name={on|off}
```

Default

The default value is `on`. Unless this parameter is explicitly set to `off`, all registration connections are accepted.

### SECURE\_CONTROL\_listener\_name

Purpose

To specify the transports on which control commands are to be serviced.

Syntax

```
SECURE_CONTROL_listener_name = 
[(]transport1[,transport2, ....,transportn)]
```

In the preceding syntax, `transport1`, `transport2`, and `transport` `n` are valid, installed transport protocol names.

Configuration

If the `SECURE_CONTROL_` `listener_name` parameter is configured with the list of transport names, then the control commands will be serviced only if the connection is one of the listed transports. Connections arriving by other transport protocols are refused. For example:

```
SECURE_CONTROL_listener1 = (TCPS, IPC)
```

In the preceding example, administration requests are accepted only on TCPS and IPC transports.

If no values are entered for this parameter, then the listener accepts any connection on any endpoint.

Example

```
LISTENER1=
 (DESCRIPTION=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))
     (ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=1522))   )
  SECURE_CONTROL_LISTENER1=tcps
```

### SECURE\_REGISTER\_listener\_name

Purpose

To specify the transports on which registration requests are to be accepted.

Syntax

```
SECURE_REGISTER_listener_name = 
[(]transport1[,transport2, ....,transportn)]
```

In the preceding example, `transport1`, `transport2`, and `transport` `n` are valid, installed transport protocol names.

Configuration

If the `SECURE_REGISTER_` `listener_name` parameter is configured with the list of transport names, then only the connections arriving on the specified transports will be able to register the service with the listener. Connections arriving by other transport protocols are refused. For example:

```
SECURE_REGISTER_listener1 = (TCPS, IPC)
```

In the preceding example, registration requests are accepted only on TCPS and IPC transports.

If no values are entered for this parameter, then the listener accepts registration requests from any transport.

If this parameter and SECURE\_CONTROL\_listener\_name are configured, then they override the SECURE\_PROTOCOL\_listener\_name parameter.

Example

```
LISTENER1=
 (DESCRIPTION=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))
     (ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=1522))   )
  SECURE_REGISTER_LISTENER1=tcps
```

### SECURE\_PROTOCOL\_listener\_name

Purpose

To specify the transports on which administration and registration requests are to be accepted.

Syntax

```
SECURE_PROTOCOL_listener_name = 
[(]transport1[,transport2, ....,transportn)]
```

In the preceding example, `transport1`, `transport2`, and `transport` `n` are valid, installed transport protocol names.

Configuration

If this parameter is configured with the list of transport names, then the control commands and service registration can happen only if the connection belongs to the list of transports configured.

If this parameter is not present and neither SECURE\_CONTROL\_listener\_name or SECURE\_REGISTER\_listener\_name are configured, then all supported transports accept control and registration requests.

If the SECURE\_CONTROL\_listener\_name and SECURE\_REGISTER\_listener\_name parameters are configured, then they override the `SECURE_PROTOCOL_` `listener_name` parameter.

Example

```
LISTENER1=
 (DESCRIPTION=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))
     (ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=1522))   )
  SECURE_PROTOCOL_LISTENER1=tcps
```

### Using COST Parameters in Combination

COST parameters can also be used in combination to further control which transports accept service registration and control commands.

In Example 7-2, control commands are accepted only on the IPC channel and the TCPS transport, and service registrations are accepted only on an IPC channel.

Example 7-2 Combining COST Parameters

```
LISTENER1=
 (DESCRIPTION=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))
     (ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=1522))   )
  SECURE_CONTROL_LISTENER1=(tcps,ipc)
  SECURE_REGISTER_LISTENER1=ipc
```

In Example 7-3, control commands are accepted only on the TCPS transport and service registrations are accepted only on the IPC channel.

Example 7-3 Combining COST Parameters

```
LISTENER1=
 (DESCRIPTION=
     (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
     (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))
     (ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=1522))   )
  SECURE_CONTROL_LISTENER1=tcps
  SECURE_PROTOCOL_LISTENER1=ipc
```
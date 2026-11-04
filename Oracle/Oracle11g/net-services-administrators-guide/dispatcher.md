---
title: Configuring Dispatchers
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/dispatcher.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 11 Configuring Dispatchers

The [shared server](glossary.md) architecture enables a database server to allow many user processes to share very few server processes, so the number of users that can be supported is increased. With the shared server architecture, many user processes connect to a [dispatcher](glossary.md). The dispatcher directs multiple incoming network session requests to a common queue. An idle shared server process from a shared pool of server processes picks up a request from the queue. This means a small pool of server processes can serve a large number of clients. Dispatchers reduce server processes. This is useful when a system is overloaded or has limited memory.

This chapter contains the following topics:

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN11166) for additional information about shared server configuration

## Configuring Dispatchers

Shared memory resources for dispatchers, virtual circuits, and shared servers are preconfigured to allow the enabling of shared servers at run time. Database administrators can start dispatchers and shared servers with the SQL `ALTER SYSTEM` statement without having to restart the instance. A dispatcher is started automatically on the TCP/IP protocol when shared server mode is turned on and the dispatchers parameter has not been set. The default configuration for the dispatcher is equivalent to the following `DISPATCHERS` parameter setting in the database initialization parameter file.

```
dispatchers="(PROTOCOL=tcp)"
```

In configurations in which client load is causing a strain on memory and other system resources, database administrators can alleviate load issues by starting shared server resources.

Use the following views to check configurations and monitor dispatchers:

- `V$QUEUE`: This view contains information about the shared server message queues. This view is only available to the `SYS` user, and users who have `SELECT ANY TABLE` system privilege, such as `SYSTEM`.
- `V$DISPATCHER`: This view provides information about the dispatcher processes, including name, network address, status, various usage statistics, and index number.
- `V$DISPATCHER_CONFIG`: This view provides configuration information about the dispatchers.
- `V$DISPATCHER_RATE`: This view provides rate statistics for the dispatcher processes.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/build_db.htm#PFGRF021) and [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for additional information these views

Configure the `DISPATCHERS` parameter if either of the following conditions apply:

- You need to configure a protocol other than TCP/IP
- You want to configure one or more of the optional dispatcher attributes, such as multiplexing.

You can specify the following attributes for the `DISPATCHERS` parameter. The `PROTOCOL` attribute is required, and the others are optional. The `ADDRESS` attribute is used when you need to set a specify port number, such as when using a firewall.

- `ADDRESS`
- `CONNECTIONS`
- `DESCRIPTION`
- `DISPATCHERS`
- `LISTENER`
- `MULTIPLEX`
- `POOL`
- `PROTOCOL`
- `SERVICE`
- `SESSIONS`
- `TICKS`

You alter dispatchers configurations with the SQL statement `ALTER SYSTEM`, or with [Database Configuration Assistant](glossary.md). After setting this parameter, you do not need to restart the instance.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN11166) for additional information about shared server configuration
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams080.htm#REFRN10049) for additional information about configuring the `DISPATCHERS` parameter and supported attributes
- [Oracle Database SQL Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2.htm#SQLRF009) for additional information about the `ALTER` `SYSTEM` statement

## Grouping Services by Dispatcher

An Oracle database can be represented by multiple service names. A pool of dispatchers can be allocated exclusively for clients requesting a particular service. This way, the mission critical requests may be given more resources and in effect increase their priority.

For example, the following initialization parameter file sample shows two dispatchers. The first dispatcher services requests for clients requesting `sales.us.example.com.` The other dispatcher services requests only for clients requesting `adminsales.us.example.com`.

```
SERVICE_NAMES=sales.us.example.com
INSTANCE_NAME=sales
DISPATCHERS="(PROTOCOL=tcp)" 
DISPATCHERS="(PROTOCOL=tcp)(SERVICE=adminsales.us.example.com)"
```

## Enabling Connection Pooling

Connection pooling is a resource utilization feature that enables you to reduce the number of physical network connections to a dispatcher. This is achieved by sharing or pooling a set of connections among the client processes.

To configure connection pooling, set the `DISPATCHERS` parameter in the initialization parameter file with the `POOL` attribute and the following optional attributes:

- `CONNECTIONS`
- `SESSIONS`
- `TICKS`

Consider a system that can support 200 connections for each dispatcher process and has the following:

- 2500 users concurrently connected through TCP/IP
- 1000 sessions concurrently connected through TCP/IP with SSL

To determine the number of dispatchers, use the following formula:

```
CEIL ( maximum concurrent sessions / connections for each dispatcher )
```

In this case, the `DISPATCHERS` attribute for TCP/IP should be set to a minimum of thirteen dispatchers and TCP/IP with SSL should be set to five dispatchers:

```
DISPATCHERS="(PROTOCOL=tcp)(DISPATCHERS=13)"
DISPATCHERS="(PROTOCOL=tcps)(DISPATCHERS=5)"
```

The number of dispatchers can be reduced by implementing connection pooling. Connection pooling allows each dispatcher to handle more sessions. For example, suppose that clients are idle most of the time and one dispatcher can route requests and responses for 2500 TCP/IP sessions, or 1000 TCP/IP with SSL sessions. The following configuration reduces the number of dispatchers required for each protocol and allows the dispatchers to be more fully utilized:

```
DISPATCHERS="(PROTOCOL=tcp)(DISPATCHERS=2)(POOL=on)(TICK=1) (CONNECTIONS=200)(SESSIONS=2500)" 
 
DISPATCHERS="(PROTOCOL=tcps)(DISPATCHERS=1)(POOL=on)(TICK=1) 
(CONNECTIONS=200)(SESSIONS=1000)"
```

In the preceding example, the `DISPATCHERS` attribute does not have to be specified for the TCP/IP with SSL sessions because the default for `DISPATCHERS` is 1. The default for `CONNECTIONS` is the maximum number of connections for each process, which is operating system dependent.

See Also:

["Connection Pooling"](intro.md)

## Enabling Session Multiplexing

Session multiplexing, available with Oracle Connection Manager, enables multiple client sessions to funnel through a single protocol connection. For example, several user processes can connect to one dispatcher by way of a single connection from Oracle Connection Manager.

Oracle Connection Manager allows communication by users to the dispatcher by way of a shared connection. At any one time, users might need the connection, while other user processes linked to the dispatcher by way of the connection manager process are idle. Session multiplexing is beneficial because it maximizes use of the dispatcher process connections.

Session multiplexing is also useful for database link connections between dispatchers. The limit on the number of sessions for each dispatcher is operating system specific.

To enable session multiplexing, set the attribute `MULTIPLEX` in the `DISPATCHERS` parameter to `on` or an equivalent value.

```
DISPATCHERS="(PROTOCOL=tcp)(MULTIPLEX=on)"
```

See Also:

["Enabling Session Multiplexing"](cman.md) for configuration details and "Enabling Connection Pooling"

## Configuring Clients for Environments Using Both Shared Server and Dedicated Server

If a shared server is configured on the server side, and a client connection request arrives when no dispatchers are registered, then the request is processed by a dedicated server process. If you want a particular client always to use a dispatcher, then configure `(``SERVER` `=shared)` in the `CONNECT_DATA` section of the connect descriptor. For example:

```
sales= 
(DESCRIPTION= 
  (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
  (CONNECT_DATA=
     (SERVICE_NAME=sales.us.example.com)
     (SERVER=shared)))
```

When the `(SERVER=shared)` attribute is configured and a dispatcher is not available, then the client connection request is rejected, and a message is sent to the client.

If the database is configured for a shared server and a particular client requires a dedicated server, then you can configure the client to use a dedicated server in one of the following ways:

- You can configure a net service name with a connect descriptor that contains `(``SERVER` `=dedicated)` in the `CONNECT_DATA` section. For example:
	```
	sales= 
	(DESCRIPTION= 
	  (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
	  (CONNECT_DATA=
	     (SERVICE_NAME=sales.us.example.com)
	     (SERVER=dedicated)))
	```
- You can configure the client profile file, `sqlnet.ora`, with `USE_DEDICATED_SERVER=on`. This adds `(SERVER=dedicated)` to the `CONNECT_DATA` section of the connect descriptor the client uses.
	Note:
	If `USE_DEDICATED_SERVER` is set to `ON`, then existing `(SERVER=` `value``)` entries in connect descriptors are overwritten with `(SERVER=dedicated)`.

See Also:

- ["Configuring Advanced Connect Data Parameters"](advcfg.md) to set the `SERVER` parameter
- ["Routing Connection Requests to a Process"](profile.md) to set the `USE_DEDICATED_SERVER` parameter
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci09adv.htm#LNOCI090) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/manproc.htm#ADMIN12349) for additional information about enabling and configuring database resident connection pooling
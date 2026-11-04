---
title: Introducing Oracle Net Services
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/intro.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 1 Introducing Oracle Net Services

This chapter describes the basic elements of Oracle Net Services architecture and the Oracle Net foundation layer.

This chapter contains the following topics:

- About Oracle Net Services
- Oracle Net Services Components

## About Oracle Net Services

[Oracle Net Services](glossary.md) provides enterprise-wide connectivity solutions in distributed, heterogeneous computing environments. Oracle Net Services eases the complexities of network configuration and management, maximizes performance, and improves network diagnostic capabilities.

This section introduces the basic networking concepts involved in a typical network configuration. This section contains the following topics:

### Understanding Connectivity

[Oracle Net](glossary.md), a component of Oracle Net Services, enables a network session from a client application to an Oracle Database server. When a network session is established, Oracle Net acts as the data courier for both the client application and the database. It is responsible for establishing and maintaining the connection between the client application and database, as well as exchanging messages between them. Oracle Net is able to perform these jobs because it is located on each computer in the network.

This section contains the following connectivity topics:

- Client/Server Application Connections
- Web Client Application Connections

#### Client/Server Application Connections

Oracle Net enables connections from traditional client/server applications to Oracle Database servers. Figure 1-1 shows how Oracle Net enables a network connection between a client and a database server. Oracle Net is a software component that resides on both the client and the database server. Oracle Net is layered on top of network [Oracle protocol support](glossary.md), rules that determine how applications access the network and how data is subdivided into packets for transmission across the network. In Figure 1-1, Oracle Net communicates with [TCP/IP](glossary.md) to enable computer-level connectivity and data transfer between the client and the database.

Figure 1-1 Client/Server Application Connection

![Figure 1-1 Client/Server Application Connection](img/netag107.gif)

> This illustration shows a client/server application connection using Oracle Net. The client shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - Application
> - Oracle Net
>
> The database server also shows a communication stack. From the top down, the stack is constructed with the following layers.
>
> The TCP/IP network protocol resides between the client and the database server.
>
> During the connection, the client application communicates with the Oracle Net layer. In turn, Oracle Net communicates with the TCP/IP protocol, which passes the connection to the Oracle Net layer on the database server.
  

Specifically, Oracle Net is comprised of the [Oracle Net foundation layer](glossary.md), which establishes and maintains connections, and [Oracle protocol support](glossary.md), which maps the foundation layer technology to industry-standard protocols.

##### Java Client Application Connections

Java client applications access an Oracle Database through a [Java Database Connectivity (JDBC) Driver](glossary.md), a standard Java interface for connecting from Java to a relational database. Oracle offers the following drivers:

- [JDBC OCI Driver](glossary.md) for client side use with an Oracle client installation
- [JDBC Thin Driver](glossary.md), a pure Java driver for client side use without an Oracle installation, particularly with applets

These drivers use Oracle Net to enable connectivity between a client application and an Oracle Database.

Figure 1-2 shows a Java client application using a JDBC OCI driver and an Oracle Database server. The Java client application makes calls to the JDBC OCI driver, which translates the JDBC calls directly into the Oracle Net layer. The client then uses Oracle Net to communicate with the Oracle Database that is also configured with Oracle Net.

Figure 1-2 Java Application Connection

![Figure 1-2 Java Application Connection](img/netag106.gif)

> This illustration shows a Java application connection using a JDBC OCI driver. The client shows a communication stack. From the top down, this stack is constructed with the following layers:
>
> - Application layer
> - JDBC OCI Driver
> - Oracle Net
>
> The database server shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net
>
> The TCP/IP network protocol resides between the client and the database server.
  

See Also:

[Oracle Database JDBC Developer's Guide and Reference](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm).

#### Web Client Application Connections

Internet connections from client Web browsers to an Oracle Database server are similar to client/server applications, except that the connection request goes to an application Web server.

Figure 1-3 shows the basic architecture for Web client connections, including a client Web browser, an application Web server, and an Oracle Database server. The browser on the client communicates with [HTTP protocol](glossary.md) to the Web server to make a connection request. The Web server sends the request to an application where it is processed. The application then uses Oracle Net to communicate with the Oracle Database server that also is configured with Oracle Net.

Figure 1-3 Web Client Connections through Application Web Server

![Figure 1-3 Web Client Connections through Application Web Server](img/netag105.gif)

> This illustration shows a Web browser connection to an Oracle database through an application Web server.
>
> The application Web server shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - Web application
> - Oracle Net
>
> The database server shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net
>
> The HTTP protocol resides between the Web browser and the application Web server, and the TCP/IP network protocol resides between the application Web server and the database server.
  

The basic components have the following characteristics:

- HyperText Transport Protocol (HTTP)
	HTTP provides the language that enables Web browsers and application Web servers to communicate.
- Application Web Server
	An application Web server manages data for a Web site, controls access to that data, and responds to requests from Web browsers. The application on the Web server communicates with the database and performs the job requested by the Web server.

##### Web Client Connections Through Java Application Web Server

An application Web server can host Java applications and servlets, as shown in Figure 1-4. Web browsers make a connection request by communicating through HTTP to an application Web server. The application Web server sends the request to an application or a servlet, which uses a JDBC OCI or a JDBC Thin driver to process the request. The driver then uses Oracle Net to communicate with the Oracle Database server that also is configured with Oracle Net.

Figure 1-4 Web Client Connections Through Java Application Web Server

![Figure 1-4 Web Client Connections Through Java Application Web Server](img/netag074.gif)

> This illustration shows an application Web server hosting a Java servlet.
>
> The application Web server shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - Java Servlet
> - JDBC OCI or JDBC Thin driver
> - Oracle Net
>
> The database server shows a communication stack that includes two layers. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net
>
> The HTTP protocol resides between two Web browsers and the application Web server, and the TCP/IP network protocol resides between the application Web server and the database server.
  

##### Web Client Connections Without an Application Web Server

Web clients that do not require an application Web server to access applications can access the Oracle Database directly, for example, by using a Java applet. In addition to regular connections, the database can be configured to accept HTTP protocol, [FTP protocol](glossary.md), or [WebDAV protocol](glossary.md) connections. These protocols are used for connections to [Oracle XML DB](glossary.md) in the Oracle Database instance.

Figure 1-5 shows two different Web clients. The first Web client makes an HTTP connection to the database. The second Web client uses a Web browser with a JDBC Thin driver, which in turn uses a Java version of Oracle Net called JavaNet to communicate with the Oracle Database server that is configured with Oracle Net.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

Figure 1-5 Web Client Connection Scenarios

![Figure 1-5 Web Client Connection Scenarios](img/netag075.gif)

> This illustration depicts two Web browsers connecting to an Oracle database in two different ways. The database server shows a communication stack that includes two layers. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net
>
> The database server is also configured to support HTTP.
>
> One first Web browser uses the HTTP protocol to connect to the Oracle Net layer on the database server. The second Web browser shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - Java applet
> - JDBC thin driver
> - JavaNet
>
> This browser uses the TCP/IP protocol to connect to the Oracle Net layer on the database.
  

### Understanding Manageability

Oracle Net Services offers several manageability features that enable you to easily configure and manage networking components. These features are described in the following topics:

- Location Transparency
- Centralized Configuration and Management
- Quick Installation and Configuration

#### Location Transparency

Each database is represented by one or more services. A [service](glossary.md) is identified by a [service name](glossary.md), for example, `sales.us.example.com`. A client uses a service name to identify the database it must access. The information about the database service and its location in the network is transparent to the client because the information needed for a connection is stored in a repository.

The repository is represented by one or more [naming method](glossary.md) s. A naming method is a resolution method used by a client application to resolve a connect identifier to a connect descriptor when attempting to connect to a database service. Oracle Net Services offers several types of naming methods that support localized configuration on each client, or centralized configuration that can be accessed by all clients in the network. GUIs enable you to manage data stored in the naming methods.

For example, in Figure 1-6, a company has three databases that clients can access. Each database has a distinct service name, such as `sales.us.example.com`, `hr.us.example.com`, and `mktg.us.example.com`.

1. The client uses the repository to find the information it needs for `sales.us.example.com`.
2. After the client has the information it needs, it connects to the database.

Figure 1-6 Service Information Repository

![Figure 1-6 Service Information Repository](img/netag076.gif)

> This illustration is described in the surrounding text.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

#### Centralized Configuration and Management

To manage large networking environments, administrators have to be able to easily access a centralized repository to specify and modify the network configuration. For this reason, the Oracle Net Services configuration can be stored in a LDAP-compliant directory server.

Support of LDAP-compliant directory servers provides a centralized vehicle for managing and configuring a distributed Oracle network. The directory can act as a central repository for all information about database network components, user and corporate policies, and user authentication and security, thus replacing client-side and server-side localized configuration files.

All computers on the network can refer to the directory for information. Figure 1-7 shows clients, other servers (such as application Web servers) and Oracle Database servers connecting to a centralized directory server.

Figure 1-7 Centralized Storage of Network Configuration with a Directory Server

![Figure 1-7 Centralized Storage of Network Configuration with a Directory Server](img/netag120.gif)

> This illustration shows an intranet network with two clients, an application Web server, and two databases, all connecting to a database server.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

See Also:

["Using a Directory Server for Centralized Management"](config_concepts.md) for an in-depth overview of directory server concepts

#### Quick Installation and Configuration

Networking elements for the Oracle Database server and clients are preconfigured for most environments. The Easy Connect naming method is enabled by default and does not require a repository. Clients connect simply using the hostname of the database. As a result, clients and servers are ready to connect out-of-the-box using Easy Connect, giving users the benefits of distributed computing.

### Understanding Shared Server Architecture

The Oracle Database [shared server](glossary.md) architecture increases the scalability of applications and the number of clients that can be simultaneously connected to the database. The shared server architecture also enables existing applications to scale up without making any changes to the application itself.

When using a shared server, clients do not communicate directly with a database [server process](glossary.md), a database process that handles a client's requests on behalf of a database. Instead, client requests are routed to one or more [dispatcher](glossary.md) s. The dispatchers place the client requests in a common queue. An idle [shared server](glossary.md) from the shared pool of server processes picks up and processes a request from the queue. This means a small pool of server processes can serve a large number of clients.

Figure 1-8 and Figure 1-9 show the basic difference between the shared server connection model and the traditional [dedicated server](glossary.md) connection model. In the shared server model, a dispatcher can support multiple client connections concurrently. In the dedicated server model, there is one server process for each client. Each time a connection request is received, a server process is started and dedicated to that connection until completed. This causes a processing delay.

Figure 1-8 Shared Server Architecture

![Figure 1-8 Shared Server Architecture](img/netag114.gif)

> This illustration shows a sample shared server connection, in which three Web browser connections are being routed to one dispatcher. Two shared server processes pick up the connection requests from the dispatcher, enabling the browser connections to an Oracle database.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Figure 1-9 Dedicated Server Architecture

![Figure 1-9 Dedicated Server Architecture](img/netag078.gif)

> This illustration shows three clients using individual dedicated server processes to connect to an Oracle database.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

A shared server is ideal for configurations with a large number of connections because it reduces the server memory requirements. A shared server is well suited for both Internet and intranet environments.

Utilization of server resources can be further enhanced with Oracle Net Services features that are configurable through a shared server. These features are discussed in the following sections:

- Connection Pooling
- Session Multiplexing

#### Connection Pooling

When a large number of clients run interactive Web applications, many of these sessions may be idle at a given time. The [connection pooling](glossary.md) feature enables the database server to timeout an idle session and use the connection to service an active session. The idle logical session remains open, and the physical connection is automatically reestablished when the next request comes from that session. Therefore, Web applications can allow larger numbers of concurrent users to be accommodated with existing hardware.

Figure 1-10 shows how connection pooling works. In this example, the Oracle Database server has been configured with 255 connections. One of the clients has been idle past a specified amount of time. Connection pooling makes this connection available to an incoming client connection, which is connection number 256. When the idle client has more work to do, the connection is reestablished for that client with another client's idle connection.

Figure 1-10 Connection Pooling

![Figure 1-10 Connection Pooling](img/netag117.gif)

> This illustration shows three clients connecting to an Oracle database. It is described in the surrounding text.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

#### Session Multiplexing

[Oracle Connection Manager](glossary.md), an Oracle Net Services component, enables multiple client network sessions to be multiplexed, or funneled, through a single network connection to a database.

The [session multiplexing](glossary.md) feature reduces the demand on resources needed to maintain multiple network sessions between two processes by enabling the server to use fewer network connection endpoints for incoming requests. In this way, the total number of network sessions that a server can handle is increased. One Oracle Connection Manager with multiple gateways enables thousands of concurrent users to connect to a server.

Figure 1-11 shows how session multiplexing can be used in a Web architecture. When Oracle Connection Manager is run on the same computer as an application Web server, the application Web server can route multiple client sessions through Oracle Connection Manager to ensure that those sessions have continuous access to an Oracle Database server. This functionality is especially useful for Web applications where session availability and response time are major concerns.

Figure 1-11 Session Multiplexing

![Figure 1-11 Session Multiplexing](img/netag080.gif)

> This illustration shows three Web clients connecting to an Oracle database through an application Web server configured with Oracle Connection Manager. The connections from the clients are funneled to a single network connection to an Oracle database.
>
> The database server shows a communication stack that includes two layers. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net
>
> Oracle Connection Manager users a single network connection to connect the clients to the Oracle Net layer on the database server.
  

Table 1-1 summarizes the differences between connection pooling and session multiplexing, and provides recommendations for using them in the network.

Table 1-1 Connection Pooling and Session Multiplexing

| Feature | Advantages | Disadvantages | Recommended for |
| --- | --- | --- | --- |
| Connection Pooling | - Reduces the number of network resources used for each process - Supports large client populations - Maximizes the number of client/server sessions over a limited number of process connections - Optimizes network traffic and network resource utilization, such as network connection bandwidth - Enables identification and monitoring of real users - Enables middle-tier application Web servers or applications that need to access back-end database to support additional services, such as Oracle Application Server - Requires only a single transport for clients with multiple applications - Requires only a single network connection for database links | Database sessions should use the `IDLE_TIME` resource parameter. | Networks where many clients run interactive "high think/search time" applications such as messaging and OLAP. |
| Session Multiplexing | - Limits the number of network resources used for each process - Supports large client populations - Maximizes the number of client/server sessions over a limited number of process connections - Optimizes resource utilization - Enables identification and monitoring of real users - Enables mid-tier applications to support additional services - Requires only a single transport for clients with multiple applications - Requires only a single network connection for database links | Clients must connect to Oracle Connection Manager. | Networks where continuous connectivity is required. |

### Understanding Performance

System performance is important to users. Users usually start to notice performance when a system takes longer than one second to respond. Oracle Net configuration can be modified to enhance system performance.

This section discusses performance considerations. It contains the following topics:

- Listener Queue Size
- Session Data Unit Size for Data Transfer Optimization
- Persistent Buffer Flushing for TCP/IP
- Sockets Direct Protocol
- Availability

#### Listener Queue Size

If you anticipate receiving a large number of connection requests for a listening process (such as a listener or Oracle Connection Manager) over TCP/IP, then Oracle Net enables you to configure the listening queue to be higher than the system default.

#### Session Data Unit Size for Data Transfer Optimization

Before sending data across the network, Oracle Net buffers and encapsulates data into the [session data unit (SDU)](glossary.md). Oracle Net sends the data stored in this buffer when the buffer is full, flushed, or when database server tries to read data. When large amounts of data are being transmitted or when the message size is consistent, adjusting the size of the SDU buffers can improve performance, network utilization, or memory consumption. You can deploy SDU at the client, application Web server, and database.

Tuning your application to reduce the number of round trips across the network is the best way to improve your network performance. If this is done, then it is also possible to optimize data transfer by adjusting the size of the SDU.

Table 1-2 outlines considerations for modifying the size of the SDU.

Table 1-2 SDU Considerations

| Modify SDU size when: | Do not modify SDU size when: |
| --- | --- |
| - The data coming back from the server is fragmented into separate packets - You are on a wide area network (WAN) that has long delays - The packet size is consistently the same - Large amounts of data are returned | - The application can be tuned to avoid the delays listed in the adjacent column - You have a high speed network where the effect of the data transmission is negligible - Your requests return small amounts of data from the server |

Note:

Starting with Oracle Database 11g, Oracle Net Services has optimized bulk data transfer for certain components, such as Oracle SecureFiles LOBs and Oracle Data Guard redo transport services. The SDU size limit, as specified in the network parameter files, does not apply to these bulk data transfers.

See Also:

["Configuring Session Data Unit"](performance.md)

#### Persistent Buffer Flushing for TCP/IP

Under certain conditions for some applications using TCP/IP, Oracle Net packets may not get flushed immediately to the network. Most often, this behavior occurs when large amounts of data are streamed. The implementation of TCP/IP itself is the reason for the lack of flushing, causing unacceptable delays. To remedy this problem, specify no delays in the buffer flushing process.

See Also:

[Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm#NETRF006) for additional information about the `TCP.NODELAY` parameter

#### Sockets Direct Protocol

Oracle Net Services provides support for InfiniBand high-speed networks. InfiniBand is a high-bandwidth I/O architecture designed to increase communication speed between CPUs, server-side devices, and network subsystems. Specifically, Oracle Net Services provides support for Sockets Direct Protocol ([SDP](glossary.md)). SDP is an industry-standard wire protocol intended for use between InfiniBand network peers.

SDP reduces the overhead of TCP/IP by eliminating intermediate replication of data and transferring most of the messaging burden away from the CPU and onto the network hardware. The result is a low- [latency](glossary.md), increased bandwidth, high-throughput connection that reduces the amount of CPU cycles dedicated to network processing.

The communication between clients, including Oracle Application Server or any other third-party middle-tier client, and Oracle Database 11g can take advantage of high-speed interconnect benefits. Oracle Application Server includes Oracle TCP/IP support as part of its installation.

A driver installed on the Oracle Application Server servers transparently converts TCP/IP support to SDP support. The SDP requests are then sent to an InfiniBand switch that processes and forwards the requests from the Oracle Application Server servers to the database server.

See Also:

["Configuring SDP Support for InfiniBand Connections"](performance.md)

#### Availability

Availability to the database is crucial for any network. You can configure multiple listeners to handle client connection requests for the same database service. This is beneficial in Oracle Real Application Clusters configurations, where each instance has a listener associated with it. Multiple listener configurations enable you to use the following features.

- Connect-time failover enables clients to request a different listener, usually on a different node, if the first listener fails.
- Client load balancing enables clients to randomize requests to the multiple listeners, usually on different nodes. These features can be used together or separately. Together, they ensure access to the database and distribute the load to not overburden a single listener.

### Understanding Network Security

Data access and secure transfer of data are important considerations when deploying Oracle Database. Granting and denying access to a database is crucial for a secure network environment. Oracle Net Services enables database access control using firewall access control.

#### Firewall Access Control

Oracle Connection Manager can be configured to grant or deny client access to a particular database service or a computer. By specifying filtering rules, you can allow or restrict specific client access to a server, based on the following criteria:

- Source host names or IP addresses for clients
- Destination host names or IP addresses for servers
- Destination database service names
- Client use of [Oracle Advanced Security](glossary.md)

Figure 1-12 shows an Oracle Connection Manager positioned between three clients and an Oracle Database server. Oracle Connection Manager is configured to allow access to the first two clients and to deny access to the third.

Figure 1-12 Intranet Network Access Control with Oracle Connection Manager

![Figure 1-12 Intranet Network Access Control with Oracle Connection Manager](img/netag082.gif)

> This illustration is described in the surrounding text.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Although Oracle Connection Manager cannot be integrated with third-party firewall products, vendors can package it with their own products in a way that enables this product to serve as an application gateway.

In general, firewalls should be set to receive incoming requests, and allow outbound calls from Oracle Database. By defining filtering rules, you can limit access to the network.

Caution:

Incorrectly setting your firewall options can cause security problems. Before changing your firewall settings, discuss the options and your network site policies with your system administrator.

Figure 1-13 shows an application gateway controlling traffic between internal and external networks and providing a single checkpoint for access control and auditing. As a result, unauthorized Internet hosts cannot directly access the database inside a corporation, but authorized users can still use Internet services outside the corporate network. This capability is critical in Internet environments to restrict remote access to sensitive data.

Figure 1-13 Internet Network Access Control with an Application Gateway

![Figure 1-13 Internet Network Access Control with an Application Gateway](img/netag083.gif)

> This illustration shows a demilitarized zone (DMZ) between an external internet network and a corporate network. The application gateway that connects to an application Web server resides in the DMZ. The application gateway controls access to the databases located inside the corporate network.
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

It is important to deploy at least two Oracle Connection Manager firewalls or Oracle Net Firewall proxies in an Internet network environment in the event that one firewall goes down.

## Oracle Net Services Components

The connectivity, manageability, scalability, and security features are described in the following sections:

- About Oracle Net
- About Oracle Net Listener
- About Oracle Connection Manager
- About Networking Tools
- About Oracle Advanced Security

### About Oracle Net

Oracle Net is a software layer that resides on the client and on the Oracle Database server. It is responsible for establishing and maintaining the connection between the client application and server, as well as exchanging messages between them, using industry-standard protocols. Oracle Net has two software components:

- Oracle Net Foundation Layer
- Oracle Protocol Support

#### Oracle Net Foundation Layer

On the client side, applications communicate with Oracle Net foundation layer to establish and maintain connections. The Oracle Net foundation layer uses Oracle protocol support that communicates with an industry-standard network protocol, such as TCP/IP, to communicate with the Oracle Database server.

Figure 1-14 illustrates the communication stack on the client.

Figure 1-14 Oracle Net on the Client

![Figure 1-14 Oracle Net on the Client](img/netag087.gif)

> This illustration shows the client communication stack. From the top down, the communication stack is constructed with the following layers:
>
> - Application
> - Oracle Net foundation layer
> - Oracle protocol support
> - Network protocol
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

The Oracle Database server side is similar to the client side as illustrated in Figure 1-15. A network protocol sends client request information to an Oracle protocol support layer, which then sends information to the Oracle Net foundation layer. The Oracle Net foundation layer then communicates with the Oracle Database server to process the client request.

Figure 1-15 Oracle Net on the Server

![Figure 1-15 Oracle Net on the Server](img/netag088.gif)

> This illustration shows the database server communication stack. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net foundation layer
> - Oracle protocol support
> - Network protocol
>
> [Copyright © 2002, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

#### Oracle Protocol Support

The Oracle Net foundation layer uses Oracle protocol support to communicate with the following industry-standard network protocols:

- TCP/IP (version 4 and version 6)
- TCP/IP with SSL
- Named Pipes
- SDP

Oracle protocol support maps Oracle Net foundation layer functionality to industry-standard protocols used in client/server connections.

See Also:

["Understanding Oracle Protocol Support Layer"](layers.md)

### About Oracle Net Listener

Oracle Database server receives the initial connection through [Oracle Net Listener](glossary.md). Oracle Net Listener, referred to in this document as the [listener](glossary.md), brokers a client request, handing off the request to the server. The listener is configured with a protocol address, and clients configured with the same protocol address can send connection requests to the listener. When a connection is established, the client and Oracle server communicate directly with one another.

Figure 1-16 shows the listener accepting a connection request from a client and forwarding that request to an Oracle server.

Figure 1-16 Listener in a Connection Request

![Figure 1-16 Listener in a Connection Request](img/netag089.gif)

> This illustration shows where the listener fits into a client/server application connection.
>
> The client shows a communication stack. From the top down, the stack is constructed with the following layers:
>
> - Application
> - Oracle Net foundation layer
> - Oracle protocol support
>
> The illustration shows the listener receiving the client connection on the database server. The database server shows a communication stack that includes three layers. From the top down, the stack is constructed with the following layers:
>
> - RDBMS
> - Oracle Net foundation layer
> - Oracle protocol support
>
> The TCP/IP network protocol resides between the client and the database server.
>
> During a connection, the client application communicates with the Oracle Net layer. In turn, Oracle Net communicates with the TCP/IP protocol, which passes the connection to the Oracle Net layer on the database server.
  

See Also:

[Chapter 9, "Configuring and Administering Oracle Net Listener"](listenercfg.md) for additional information about the listener

### About Oracle Connection Manager

Oracle Connection Manager is the software component that resides on its own computer, separate from a client or an Oracle Database server. It proxies and screens requests for the database server. In addition, it multiplexes database sessions.

In its session multiplexing role, Oracle Connection Manager funnels multiple sessions through a single transport protocol connection to a particular destination. In this way, Oracle Connection Manager reduces the demand on resources needed to maintain multiple sessions between two processes by enabling the Oracle Database server to use fewer connection end points for incoming requests.

As an access control filter, Oracle Connection Manager controls access to Oracle databases.

See Also:

- "Session Multiplexing"
- "Firewall Access Control" for a description of filtering

### About Networking Tools

Oracle Net Services provides user interface tools and command-line utilities that enable you to easily configure, manage, and monitor the network.

- [Oracle Net Configuration Assistant](glossary.md) is a standalone tool that enables you to configure listeners and naming methods.
- [Oracle Enterprise Manager](glossary.md) combines configuration functionality across multiple file systems, along with listener administrative control to provide an integrated environment for configuring and managing Oracle Net Services.
- [Oracle Net Manager](glossary.md) provides configuration functionality for an Oracle home on a local client or server host.
- Command-line control utilities enable you to configure, administer, and monitor network components, including listeners and Oracle Connection Managers.

With Oracle Enterprise Manager or Oracle Net Manager, you can fine-tune the listener and naming method configuration created with Oracle Net Configuration Assistant. In addition, Oracle Enterprise Manager and Oracle Net Manager offer built-in wizards and utilities that enable to you to test connectivity, migrate data from one naming method to another, and create additional network components.

See Also:

[Chapter 7, "Managing Oracle Net Services"](admintools.md)

### About Oracle Advanced Security

Oracle Advanced Security is a separately licensable product that provides a comprehensive suite of security features for the Oracle environment. This suite of security features protects enterprise networks and securely extends corporate networks to the Internet. It provides a single source of integration with network encryption and authentication solutions, single sign-on services, and security protocols. Oracle Advanced Security integrates industry standards and delivers unparalleled security to the Oracle network and other networks.

Oracle Advanced Security also includes Oracle Data Redaction, which enables you to redact (mask) column data, using the following types of redaction:

- Full redaction redacts all the contents of the column data. The redacted value returned to the querying user depends on the data type of the column. For example, columns of the NUMBER data type are redacted with a zero (0) and character data types are redacted with a single space by default.
- Partial redaction redacts a portion of the column data. For example, masking most of a credit card number with asterisks (\*), except for the last four digits.
- Regular expressions enable you to look for patterns of data to redact. For example, you can use regular expressions to redact email addresses, which can have varying character lengths. It is designed for use with character data only.
- Random redaction presents the redacted data to the querying user as randomly-generated values each time it is displayed.
- The None redaction type enables an administrator to test the internal operation of the redaction policies, with no effect on the results of queries against tables with policies defined on them.
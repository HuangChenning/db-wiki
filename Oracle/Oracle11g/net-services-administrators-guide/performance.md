---
title: Optimizing Performance
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 14 Optimizing Performance

This chapter describes how to optimize connection performance. This chapter contains the following topics:

## Configuring Session Data Unit

Under typical database configuration, Oracle Net encapsulates data into buffers the size of the [session data unit (SDU)](glossary.md) before sending the data across the network. Oracle Net sends each buffer when it is filled, flushed, or when an application tries to read data. Adjusting the size of the SDU buffers relative to the amount of data provided to Oracle Net to send at any one time can improve performance, network utilization, and memory consumption. When large amounts of data are being transmitted, increasing the SDU size can improve performance and network throughput.

The amount of data provided to Oracle Net to send at any one time is referred to as the message size. Oracle Net assumes by default that the message size will normally vary between 0 and 8192 bytes, and infrequently, be larger than 8192 bytes. If this assumption is true, then most of the time, the data is sent using one SDU buffer.

The SDU size can range from 512 bytes to 65535 bytes. The default SDU for the client and a dedicated server is 8192 bytes. The default SDU for a shared server is 65535 bytes.

The actual SDU size used is negotiated between the client and the server at connect time and is the smaller of the client and server values. Configuring an SDU size different from the default requires configuring the SDU on both the client and server computers, unless you are using shared servers. For shared servers, only the client value must be changed because the shared server defaults to the maximum value.

You should consider changing the SDU size when the predominant message size is smaller or larger than 8192. The SDU size should be 70 bytes larger than the predominant message size. If the predominant message size plus 70 bytes exceeds the maximum SDU, then the SDU should be set such that the message size is divided into the smallest number of equal parts where each part is 70 bytes less than the SDU size. To change the default, change the `DEFAULT_SDU_SIZE` parameter in the `sqlnet.ora` file.

For example, if the majority of the messages sent and received by the application are smaller than 8KB, taking into account the 70 bytes for overhead, then setting the SDU to 8KB will likely produce good results. If sufficient memory is available, then using the maximum value for the SDU minimizes the number of system calls and overhead for Oracle Net Services.

Note:

Starting with Oracle Database 11g, Oracle Net Services optimized bulk data transfer for components, such as Oracle SecureFiles LOBs and Oracle Data Guard redo transport services. The SDU size limit, as specified in the network parameter files, does not apply to these bulk data transfers.

See Also:

- ["Session Data Unit Size for Data Transfer Optimization"](intro.md)
- ["Statistics Example"](trouble.md)

### Setting the SDU Size for the Database

To set the SDU size for the database server, configure the following files:

- `sqlnet.ora`
	Configure the `DEFAULT_SDU_SIZE` parameter in the `sqlnet.ora` file, as follows:
	```
	DEFAULT_SDU_SIZE=8192
	```
- Initialization parameter file
	If using shared server processes, then set the SDU size in the `DISPATCHERS` parameter in the initialization parameter file, as follows:
	```
	DISPATCHERS="(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp))(SDU=8192))"
	```
- `listener.ora`
	If you have configured the listener with a list of targets in the `listener.ora` file, then the value for SDU in the `SID_LIST` element overrides the current setting in the `sqlnet.ora` file when using dedicated server processes.
	```
	SID_LIST_listener_name
	=
	  (SID_LIST= 
	    (SID_DESC=
	     (SDU=8192)
	     (SID_NAME=sales)))
	```
	The smaller value of the SDU size and the value configured for the client take precedence.

### Setting the SDU Size for the Client

To set the SDU size for the client, configure the following files:

- `sqlnet.ora`
	For global configuration on the client side, configure the `DEFAULT_SDU_SIZE` parameter in the `sqlnet.ora` file, as follows:
	```
	DEFAULT_SDU_SIZE=8192
	```
- `tnsnames.ora`
	For a particular connect descriptor, you can specify the `SDU` parameter in the `DESCRIPTION` parameter.
	```
	sales.us.example.com=
	(DESCRIPTION= 
	    (SDU=11280)
	 
	      (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
	    (CONNECT_DATA=
	     (SERVICE_NAME=sales.us.example.com))
	)
	```

The SDU size applies to all Oracle Net protocols for the particular connect descriptor.

## Determining Bandwidth-delay Product

Bandwidth-delay product is the product of network bandwidth and the round trip time of data going over the network. A simple way to determine the round trip time, is to use a command such as `ping` from one host to another and use the response times returned by `ping`.

For example, if a network has a bandwidth of 100 Mbps and a round trip time of 5ms, then the send and receive buffers should be at least (100\*10^6) \* (5/10^3) bits or approximately 62.5 Kilobytes.

The following equation shows the relationships between the units and factors involved:

```
100,000,000 bits   1 byte   5 seconds
---------------- x ------ x --------- = 62,500 bytes
 1 second          8 bits     1000
```

Setting the `SEND_BUF_SIZE` and `RECV_BUF_SIZE` to at least the bandwidth-delay product insures that when large amounts of data are being sent that the network bandwidth will be optimally utilized.

Based on the preceding equation, the bandwidth-delay product of this network link is approximately 64KB. If the largest message used to transfer redo data between a primary database and a standby database is 1MB, then the value for the `SEND_BUF_SIZE` and `RECV_BUF_SIZE` parameters could be 1MB. However, if the average message is less, then a setting of 64KB should be sufficient to optimize use of the available bandwidth.

See Also:

For information about determining messages sizes, refer to ["Statistics Example"](trouble.md)

For most network protocols, ensure that the `RECV_BUF_SIZE` parameter at one end of the network connection, typically at the client, equals the value of the `SEND_BUF_SIZE` parameter at the other end, typically at the server.

## Configuring I/O Buffer Space

Reliable network protocols, such as TCP/IP, buffer data into send and receive buffers while sending and receiving to or from lower and upper layer protocols. The sizes of these buffers affect network performance by influencing flow control decisions.

The `RECV_BUF_SIZE` and `SEND_BUF_SIZE` parameters specify sizes of socket buffers associated with an Oracle Net connection. To ensure the continuous flow of data and better utilization of network bandwidth, specify the I/O buffer space limit for receive and send operations of sessions with the `RECV_BUF_SIZE` and `SEND_BUF_SIZE` parameters. The `RECV_BUF_SIZE` and `SEND_BUF_SIZE` parameter values do not have to match, but should be set according to your environment.

For best performance, the size of the send and receive buffers should be set large enough to hold all the data that may be sent concurrently on the network connection. For a simple database connection, this typically maps to the `OCI_PREFETCH_MEMORY` size.

Use these parameters with caution as they affect network and system performance. The default values for these parameters are operating system-specific.

These parameters are supported for TCP, TCP/IP with SSL, and SDPs. Additional protocols may support these parameters on certain operating systems. The recommended values for these parameters are specified in the installation guide. Refer to operating system-specific documentation of Oracle Net for additional information.

Notes:

- The actual value of the `SEND_BUF_SIZE` and `RECV_BUF_SIZE` parameters may be less than the value specified because of limitations in the host operating system or due to memory constraints.
- It is important to consider the total number of concurrent connections that your system must support and the available memory resources. The total amount of memory consumed by these connections depends on the number of concurrent connections and the size of their respective buffers.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci04sql.htm#LNOCI16357) for additional information about the `OCI_PREFETCH_MEMORY` parameter

### Configuring I/O Buffer Space on the Client

To configure the client, set the buffer space size in the following locations in the specified file:

- Setting only the `RECV_BUF_SIZE` parameter is typically adequate. If the client is sending large requests, then also set the `SEND_BUF_SIZE` parameter. These parameters are set in the client's `sqlnet.ora` file.
- For a particular connect descriptor, you can override the current settings in the client `sqlnet.ora` file. You can specify the buffer space parameters for a particular protocol address or description in the `tnsnames.ora` file similar to the following:
	```
	sales.us.example.com=
	 (DESCRIPTION= 
	   (ADDRESS_LIST=
	     (ADDRESS=(PROTOCOL=tcp)(HOST=sales1-server)(PORT=1521)
	        (SEND_BUF_SIZE=11784)
	        (RECV_BUF_SIZE=11784))
	     (ADDRESS=(PROTOCOL=tcp)(HOST=sales2-server)(PORT=1521)
	        (SEND_BUF_SIZE=11784)
	        (RECV_BUF_SIZE=11784))
	   (CONNECT_DATA=
	     (SERVICE_NAME=sales.us.example.com)))
	hr.us.example.com=
	 (DESCRIPTION= 
	   (SEND_BUF_SIZE=8192)
	   (RECV_BUF_SIZE=8192)
	     (ADDRESS=(PROTOCOL=tcp)(HOST=hr1-server)(PORT=1521))
	   (CONNECT_DATA=
	     (SERVICE_NAME=hr.us.example.com)))
	```

### Configuring I/O Buffer Size on the Server

Because the database server writes data to clients, setting the `SEND_BUF_SIZE` parameter on the server-side is typically adequate. If the database server is receiving large requests, then also set the `RECV_BUF_SIZE` parameter.To configure the database server, set the buffer space size in the `listener.ora` and `sqlnet.ora` files.

In the `listener.ora` file, specify the buffer space parameters for a particular protocol address or for a description. The following is an example of the settings:

```
LISTENER=
(DESCRIPTION=
(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)
(SEND_BUF_SIZE=11784)

(RECV_BUF_SIZE=11784)
)
(ADDRESS=(PROTOCOL=ipc)(KEY=extproc)
(SEND_BUF_SIZE=11784)

(RECV_BUF_SIZE=11784)))

LISTENER2=
(DESCRIPTION=
(SEND_BUF_SIZE=8192)

(RECV_BUF_SIZE=16384)

(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))
```

The following is an example of the settings in the `sqlnet.ora` file:

```
RECV_BUF_SIZE=65536
SEND_BUF_SIZE=65536
```

#### Setting the Buffer Size Parameter for Shared Server Processes

If using shared server processes, then you can override the current settings obtained from the server `sqlnet.ora` file by setting the buffer space parameters in the `DISPATCHERS` initialization parameter as follows:

```
DISPATCHERS="(ADDRESS=(PROTOCOL=tcp)(SEND_BUF_SIZE=65536))"
```

## Configuring SDP Support for InfiniBand Connections

Oracle Net Services provides support for the Sockets Direct Protocol ([SDP](glossary.md)) for InfiniBand high-speed networks.

SDP is a standard communication protocol for clustered server environments. SDP is an interface between a network interface card and the application. By using SDP, applications place most of the messaging burden upon the network interface card, freeing the CPU for other tasks. As a result, SDP decreases network [latency](glossary.md) and CPU utilization.

SDP is designed specifically for System Area Networks (SANs). A SAN is characterized by short-distance, high-performance communications between multiple server systems, such as Oracle Application Server or any other third-party middle-tier client and database servers clustered on one switch.

Note:

Check with your individual vendor for their version compatibility with Oracle Database 11g.

Visit the Oracle Technology Network for additional information about SDP support at

`http://www.oracle.com/technetwork`

The following sections describe how to set up Oracle Net support of SDP for middle tier and database server communication. It contains the following topics:

- Prerequisites for Using SDP
- Configuring SDP on the Server
- Configuring SDP on the Client

See Also:

["Understanding Performance"](intro.md) for an overview of supported deployments

### Prerequisites for Using SDP

Prior to configuring support for SDP, install the required hardware, and set up InfiniBand hardware and software compatible with OpenFabrics Enterprise Distribution (OFED) 1.4 from a designated vendor on both the application Web server and database server.

During installation of the InfiniBand software, identify the constant that defines SDP or the address family for the system. This can be obtained from the operating system or OFED documentation.

See Also:

Vendor documentation for installation information.

### Configuring SDP on the Server

To configure the database server, configure an SDP address in the `listener.ora` file on the database server.

Note:

If the SDP or address protocol family constant is not 27, the default value for Oracle Net Services, then define the constant in the `SDP.PF_INET_SDP` parameter in the `sqlnet.ora` file.

The following example shows an SDP endpoint that uses port number 1521 on the computer `sales-server`.

```
LISTENER=
  (DESCRIPTION=
    (ADDRESS_LIST=
      (ADDRESS=(PROTOCOL=sdp)(HOST=sales-server)(PORT=1521))
      (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
      (ADDRESS=(PROTOCOL=ipc)(KEY=extproc))))
```

See Also:

["Creating a List of Listener Protocol Addresses"](advcfg.md)

### Configuring SDP on the Client

Note:

If the SDP or address protocol family constant is not 27, the default value for Oracle Net Services, then define the constant in the `SDP.PF_INET_SDP` parameter in the `sqlnet.ora` file.

The following procedure describes how to configure the Oracle Application Server servers or third-party middle-tier client:

1. If configuring third-party middle-tier client, then upgrade the clients to use Oracle Database 11g Client software, as follows:
	1. Run Oracle Universal Installer.
		2. Select Oracle Database 11g Client from the Available Products page.
2. For both Oracle Application Server servers and third-party middle-tier client, create a net service name to connect to the database server:
	- For Oracle Application Server servers, specify a net service name that uses the same TCP/IP protocol address configured in the `tnsnames.ora` file. For example:
		```
		sales=
		 (DESCRIPTION=
		   (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)))
		   (CONNECT_DATA=
		     (SERVICE_NAME=sales.us.example.com)))
		```
		- For third-party middle-tier clients, specify a net service name that uses the same SDP address configured in the `tnsnames.ora` file.
		For example:
		```
		sales=
		 (DESCRIPTION=
		   (ADDRESS=(PROTOCOL=sdp)(HOST=sales-server)))
		   (CONNECT_DATA=
		     (SERVICE_NAME=sales.us.example.com)))
		```
		See Also:
		[Chapter 8, "Configuring Naming Methods"](naming.md) for additional information about creating connect descriptors

## Limiting Resource Consumption by Unauthorized Users

Unauthorized access to the listener or database server can result in denial-of-service attacks, whereby an unauthorized client attempts to block authorized users' ability to access and use the system when needed. Malicious clients may attempt to flood the listener or database server with connect requests that have the sole purpose of consuming resources, such as connections, processes, or threads. To mitigate these types of attacks, configure limits that constrain the time in which resources can be held prior to authentication. Client attempts to exceed the configured limits result in connection terminations and an audit trail containing the IP address of the client being logged.

To limit the resource consumption by unauthorized users and enable the audit trail, set time-limit values for the parameters described in Table 14-1.

Table 14-1 Connect-Timeout Parameters

| Parameter | File | Description |
| --- | --- | --- |
| INBOUND\_CONNECT\_TIMEOUT\_listener\_name | listener.ora | The time, in seconds, for the client to complete its connect request to the listener after the network connection had been established.  If the listener does not receive the client request in the time specified, then it terminates the connection. In addition, the listener logs the IP address of the client and an [ORA-12525: TNS:listener has not received client's request in time allowed](trouble.md) error message to the `listener.log` file. |
| SQLNET.INBOUND\_CONNECT\_TIMEOUT | sqlnet.ora on the database server | The time, in seconds, for a client to connect with the database server and provide the necessary authentication information.  If the client fails to establish a connection and complete authentication in the time specified, then the database server terminates the connection. In addition, the database server logs the IP address of the client and an [ORA-12170: TNS:Connect timeout occurred](trouble.md) error message to the `sqlnet.log` file. The client receives either an `ORA-12547: TNS:lost contact` or an ORA-12637: Packet receive failed error message. |

When specifying values for these parameters, consider the following recommendations:

- Set both parameters to an initial low value.
- Set the value of the `INBOUND_CONNECT_TIMEOUT_` `listener_name` parameter to a lower value than the `SQLNET.INBOUND_CONNECT_TIMEOUT` parameter.

For example, you can set `INBOUND_CONNECT_TIMEOUT_` `listener_name` to 10 seconds and `SQLNET.INBOUND_CONNECT_TIMEOUT` parameter to 50 seconds. If clients are unable to complete connections within the specified time due to system or network delays that are normal for the particular environment, then increment the time as needed.

See Also:

- ["Resolving the Most Common Error Messages for Oracle Net Services"](trouble.md) for a description of error message workarounds
- ["Analyzing Listener Log Files"](trouble.md) for additional information about entries in the `listener.log` file
- ["Configuring Advanced Profile Information"](profile.md) for information about configuring these parameters
- ["Resolving the Most Common Error Messages for Oracle Net Services"](trouble.md) for a description of error message workarounds
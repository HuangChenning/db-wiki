---
title: Managing Oracle Database Port Numbers
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/ports.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## F Managing Oracle Database Port Numbers

This appendix lists the default port numbers and describes how to change the assigned port after installation. This appendix contains the following topics:

## F.1 About Managing Ports

During installation, Oracle Universal Installer (OUI) assigns port numbers to components from a set of default port numbers. Many Oracle RAC components and services use ports. As an administrator, it is important to know the port numbers used by these services, and to make sure that the same port number is not used by two services on your server.

Most port numbers are assigned during installation. Every component and service has an allotted port range, which is the set of port numbers Oracle RAC attempts to use when assigning a port. Oracle RAC starts with the lowest number in the range and performs the following checks:

- Is the port used by another Oracle Database installation on the host?
	The installation can be either active or inactive at the time; Oracle Database can still detect if the port is used.
- Is the port used by a process that is currently running?
	This could be any process on the host, including processes other than Oracle Database processes.

If the answer to any of the preceding questions is yes, then Oracle RAC moves to the next highest port in the allotted port range and continues checking until it finds a free port.

## F.2 Viewing Port Numbers and Access URLS

In most cases, the Oracle Database component's port number is listed in the tool used to configure the port. In addition, ports for some Oracle Database applications are listed in the `portlist.ini` file. This file is located in the directory `$` `ORACLE_HOME` `/install`.

If you change a port number after installation, then it is not updated in the `portlist.ini` file, so you can rely on this file only immediately after installation. To find or change a port number, use the methods described in this appendix.

## F.3 Port Numbers and Protocols of Oracle Components

Table F-1 lists the port numbers and protocols used by components that are configured during the installation. By default, the first port in the range is assigned to the component, if it is available.

Table F-1 Ports Used in Oracle Components

| Component and Description | Default Port Number | Port Range | Protocol | Used Only On Interconnect |
| --- | --- | --- | --- | --- |
| Cluster Manager  The port number is assigned automatically during installation. You cannot view or modify it afterward.  This port is used exclusively with the cluster interconnect, which is a private network that is physically separated from the public network, and uses dedicated hardware for the interconnect. | Dynamic | Dynamic | UDP | Yes |
| Cluster Synchronization Service (CSSD)  Node restart advisory messages fixed port.  This port is used on all interfaces that have broadcast capability. Broadcast occurs only when a node eviction restart is imminent. | 42424 | Dynamic | UDP | Yes |
| Event Manager (EVM)  The port number is assigned automatically during installation. You cannot view or modify it afterward.  This port is used exclusively with the cluster interconnect, which is a private network that is physically separated from the public network, and uses dedicated hardware for the interconnect. | Dynamic | Dynamic | UDP | Yes |
| Grid Plug and Play (GPNPD)  GPNPD provides access to the Grid Plug and Play profile, and coordinates updates to the profile among the nodes of the cluster to ensure that all of the nodes node have the most recent profile. | Dynamic | Dynamic | TCP | No |
| Multicast Domain Name Service (MDNSD)  Grid Plug and Play uses the mDNS process to locate profiles in the cluster, as well as by GNS to perform name resolution. The mDNS process is a background process on Linux and UNIX, and a service on Windows. | 5353 | Dynamic | UDP/TCP | No |
| Oracle Data Guard  Shares the Oracle Net port and is configured during installation. To reconfigure this port, use Net Configuration Assistant to reconfigure the Oracle Net listener. See:  [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/protocoladd.htm#NETRF180) | Default 1521, (same value as the listener) | modifiable manually to any available port | TCP | No |
| Oracle Connection Manager  Listening port for Oracle client connections to Oracle Connection Manager. You can configure Oracle Connection Manager after installation using Net Configuration Assistant. | 1630 | 1630 | TCP | No |
| Oracle Clusterware Daemon (CRSD)  CRS daemon (Oracle Cluster Ready Services Daemon) internode connection. The port number is assigned automatically during installation. You cannot view or modify it afterward.  This port is used exclusively with the cluster interconnect. | Dynamic | Dynamic | UDP | Yes |
| Oracle Cluster Registry  The port number is assigned automatically during installation. You cannot view or modify it afterward.  This port is used exclusively with the cluster interconnect. | Dynamic | Dynamic | UDP | Yes |
| Oracle Containers for J2EE (OC4J).  The CRS Agent uses port 8888 locally to manage the lifecycle of the container. | 8888  23944 (11.2.0.3 and earlier; removed 11.2.0.4) | 8888 | TCP | No |
| Oracle Enterprise Manager Database Console  HTTP port for Oracle Enterprise Manager Database Control. It is configured during installation. "Changing the Oracle Enterprise Manager Database Console Ports" explains how to modify its port number. | 1158 | 5500–5519 | TCP/HTTP | No |
| Oracle Enterprise Manager Database Console  RMI port for Oracle Enterprise Manager Database Control. It is configured during installation."Changing the Oracle Enterprise Manager Database Console Ports" explains how to modify its port number. | 5520 | 5520–5539 | TCP | No |
| Oracle Enterprise Manager Database Console  JMS port for Oracle Enterprise Manager Database Control. It is configured during installation. "Changing the Oracle Enterprise Manager Database Console Ports" explains how to modify its port number. | 5540 | 5540–5559 | TCP | No |
| Oracle Enterprise Manager  RMI port for Oracle Enterprise Manager to interact with QoS over the public interconnect. | 23792 | Configured manually | RMI | No |
| Oracle Grid Interprocess Communication (GIPCD)  A support daemon that enables Redundant Interconnect Usage. | 42424 | Dynamic | UDP | Yes |
| Oracle Grid Naming Service (GNSD)  The Oracle Grid Naming Service daemon provides a gateway between the cluster mDNS and external DNS servers. The `gnsd` process performs name resolution within the cluster. | 53 (public),  Dynamic (interconnect) | 53 (public),  Dynamic (interconnect) | UDP/TCP (public),  TCP interconnect | No |
| Oracle High Availability Services (OHASD)  The Oracle High Availability Services (OHAS) daemon starts the Oracle Clusterware stack.  This port is used exclusively with the cluster interconnect. | 42424 | Dynamic | UDP | Yes |
| Oracle Management Agent  HTTP port for Oracle Management Agent, which is part of Oracle Enterprise Manager. It is configured during installation.  "Changing the Oracle Management Agent Port" explains how to modify its port number | 3938 | 1830–1849 | HTTP | No |
| Oracle Notification Services (ONS)  Port for ONS, used to publish and subscribe service for communicating information about all Fast Application Notification (FAN) events. The FAN notification process uses system events that Oracle publishes when cluster servers become unreachable or if network interfaces fail. Use `srvctl` to modify ONS ports. If you do not specify the ONS port values, then the ONS daemon listener local port defaults to 6100, and the ONS daemon remote port defaults to 6200. | 6100 (local)  6200 (remote) | Configured manually | TCP | No |
| Oracle Real Application Clusters  The port number is assigned automatically during installation. You cannot view or modify it afterward.  This port is used exclusively with the cluster interconnect. | Dynamic | Dynamic | UDP | Yes |
| Oracle Net Listener  Allows Oracle client connections to the database over the protocol for Oracle Net. You can configure it during installation. To reconfigure this port, use Net Configuration Assistant. | 1521 | Port number changes to the next available port.  Modifiable manually to any available port. | TCP | No |
| Oracle XML DB  The Oracle XML DB HTTP port is used if Web-based applications need to access an Oracle database from an HTTP listener. It is configured during installation, but you cannot view it afterward. "Changing the Oracle XML DB Ports" explains how to change its port number. | 0 | Configured manually | HTTP | No |
| Oracle XML DB  The Oracle XML DB FTP is used when applications need to access an Oracle database from an FTP listener. It is configured during installation, but you cannot view it afterward. "Changing the Oracle XML DB Ports" explains how to change its port number. | 0 | Configured manually | FTP | No |

## F.4 Changing the Oracle Management Agent Port

To find the current setting for the Oracle Management Agent port, search for `EMD_URL` in the `ORACLE_HOME` `/` `host_sid` `/sysman/config/emd.properties` file, where `host_sid` is a string that contains the local host name and the SID for the Oracle RAC database.

To change the Oracle Management Agent HTTP port, use the `emca -reconfig` ports command:

```
emca -reconfig ports -AGENT_PORT 1831
```

## F.5 Changing the Oracle Enterprise Manager Database Console Ports

To find the current HTTP, RMI, and JMS port settings, search in the following files, where `host_sid` is a string that contains the local host name and the SID for the Oracle RAC database:

- HTTP port: Search for `REPOSITORY_URL` in the `ORACLE_HOME` `/host_sid` `/sysman/config/emd.properties` file.
- RMI port: Search for the `port` attribute in the `rmi-server` tag in the `ORACLE_HOME` `/` `oc4j/j2ee/OC4J_DBConsole_` `host_sid` `/config/rmi.xml` file.
- JMS port: Search for the `port` attribute in the `jms-server` tag in the `ORACLE_HOME` `/` `oc4j/j2ee/OC4J_DBConsole_` `host_sid` `/config/jms.xml` file.

To change the Oracle Enterprise Manager Database Control ports, use the `emca -reconfig` ports command:

```
ORACLE_HOME/bin> emca -reconfig ports option setting
```

In the previous example, `option` specifies one or more of the following ports and `setting` is the new port value:

| Option | Description | Example |
| --- | --- | --- |
| `DBCONTROL_HTTP_PORT` | Sets the HTTP port | `emca -reconfig ports -DBCONTROL_HTTP_PORT 1820` |
| `RMI_PORT` | Sets the RMI port | `emca -reconfig ports -RMI_PORT 5520` |
| `JMS_PORT` | Sets the JMS port | `emca -reconfig ports -JMS_PORT 5521` |

You can specify multiple `-reconfig port` settings in one line, for example:

```
emca -reconfig ports -DBCONTROL_HTTP_PORT 1820 -AGENT_PORT 1821 -RMI_PORT 5520
```

## F.6 Changing the Oracle XML DB Ports

By default, the FTP and HTTP (including HTTPS) ports for Oracle XML DB are set to 0, which disables FTP or HTTP access to Oracle XML DB.

To change the Oracle XML DB ports, you must run the `catxdbdbca.sql` script, which in a default installation is located in $ `ORACLE_HOME` `/rdbms/admin`.

To change the Oracle XML DB ports:

1. Check that the Oracle listener is running.
	If you cannot start the listener, then refer to Oracle Database Net Services Administrator's Guide.
2. log in to SQL\*Plus as `SYS` or `XDB` using the `SYSDBA` privileges.
	For example, to log in to SQL\*Plus as `SYS`:
	```
	SQL> sqlplus sys/ as sysdba
	```
3. Run the `catxdbdbca.sql` script.
	For example, to use `2200` for the FTP port and `8200` for the HTTP port, and assuming your Oracle home is in the location `/u01/app/oracle/product/11.2.0/dbhome_1/`, enter the following command:
	```
	SQL> /u01/app/oracle/product/11.2.0/dbhome_1/rdbms/admin/catxdbdbca.sql 2200 8200
	```
4. Exit SQL\*Plus.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN11141) for information about connecting to the database using SQL\*Plus
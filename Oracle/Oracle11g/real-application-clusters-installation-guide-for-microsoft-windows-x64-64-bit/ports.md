---
title: Managing Oracle Database Port Numbers
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/ports.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## F Managing Oracle Database Port Numbers

This appendix lists the default port numbers and describes how to change the assigned port after installation. This appendix contains the following topics:

## F.1 About Managing Ports

During installation, Oracle Universal Installer (OUI) assigns port numbers to components from a set of default port numbers. Many Oracle Real Application Clusters (Oracle RAC) components and services use ports. As an administrator, it is important to know the port numbers used by these services, and to ensure that the same port number is not used by two services on your system.

Most port numbers are assigned during installation. Every component and service has an allotted port range, which is the set of port numbers Oracle RAC attempts to use when assigning a port. Oracle RAC starts with the lowest number in the range and performs the following:

- Is the port used by another Oracle Database installation on the system?
	The installation can be either active or inactive at the time; Oracle Database can still detect if the port is used.
- Is the port used by a process that is currently running?
	This could be any process on the host, including processes other than Oracle Database processes.

If the answer to any of the preceding questions is yes, then Oracle RAC moves to the next highest port in the allotted port range and continues checking until it finds a free port.

## F.2 Viewing Port Numbers and Access URLS

In most cases, the Oracle Database component's port number is listed in the tool used to configure the port. In addition, ports for some Oracle Database applications are listed in the `portlist.ini` file. This file is located in the directory `%ORACLE_HOME` `%\install`.

If you change a port number after installation, then it is not updated in the `portlist.ini` file, so you can rely on this file only immediately after installation. To find or change a port number, use the methods described in this appendix.

## F.3 Port Numbers and Protocols of Oracle Components

Table F-1 lists the port numbers and protocols used by components that are configured during the installation. By default, the first port in the range is assigned to the component, if it is available.

Table F-1 Ports Used in Oracle Components

| Component and Description | Default Port Number | Port Range | Protocol | Used Only On Interconnect |
| --- | --- | --- | --- | --- |
| Cluster Manager  The port number is assigned automatically during installation. You cannot view or modify it afterward. | Dynamic | Dynamic | TCP | Yes |
| Cluster Synchronization Service daemon (CSSD)  The Cluster Synchronization Service (CSS) daemon uses a fixed port for node restart advisory messages.  This port is used on all interfaces that have broadcast capability. Broadcast occurs only when a node eviction restart is imminent. | 42424/   Dynamic | Dynamic | TCP | Yes |
| Oracle Data Guard  Shares the Oracle Net listener port and is configured during installation. To reconfigure this port, use Oracle Net Configuration Assistant (NETCA) to reconfigure the listener. | 1521 (same value as the listener) | 1521 | TCP | No |
| Oracle Connection Manager  Listening port for Oracle client connections to Oracle Connection Manager. You can configure Oracle Connection Manager after installation using NETCA. | 1630 | 1630 | TCP | No |
| Cluster Ready Services daemon (CRSD)  Oracle Clusterware Cluster Ready Services (CRS) daemon internode connection. The port number is assigned automatically during installation. You cannot view or modify it afterward. | Dynamic | Dynamic | TCP | Yes |
| Oracle Cluster Registry  The port number is assigned automatically during installation. You cannot view or modify it afterward. | Dynamic | Dynamic | TCP | Yes |
| Oracle EM Database Control - HTTP  HTTP port for Oracle Enterprise Manager Database Control. The port is configured during installation. Section F.5, "Changing the Oracle Enterprise Manager Database Control Ports" explains how to modify this port number. | 1158 | 5500–5519 | TCP/HTTP | No |
| Oracle EM Database Control - Java RMI  Java Remote Method Invocation (RMI) port for Oracle Enterprise Manager Database Control. The port is configured during installation. Section F.5, "Changing the Oracle Enterprise Manager Database Control Ports" explains how to modify this port number. | 5520 | 5520–5539 | TCP | No |
| Oracle EM Database Control - JMS  Oracle Java Message Service (JMS) port for Oracle Enterprise Manager Database Control. The port is configured during installation. Section F.5, "Changing the Oracle Enterprise Manager Database Control Ports" explains how to modify this port number. | 5540 | 5540–5559 | TCP | No |
| Oracle Event Manager (EVM)  Generates events for Oracle Clusterware. The port number is assigned automatically during installation. You cannot view or modify it afterward. | Dynamic | Dynamic | TCP | Yes |
| Oracle HA Services daemon (OHASD)  The Oracle High Availability Services (OHAS) daemon starts the Oracle Clusterware stack. | 42424 | Dynamic | TCP | Yes |
| Oracle Management Agent  HTTP port for Oracle Management Agent, which is part of Oracle Enterprise Manager. The port is configured during installation.  Section F.4, "Changing the Oracle Management Agent Port" explains how to modify this port number. | 3938 | 1830–1849 | HTTP | No |
| Oracle Net Listener  Allows Oracle clients to connect to the database by using Oracle Net Services. You can configure this port during installation. To reconfigure this port, use NETCA. | 1521 | 1024-65535 | TCP | No |
| Oracle Notification Services (ONS)  Port for ONS, used for the publish and subscribe service for communicating information about Fast Application Notification (FAN) events. The FAN notification process uses system events that Oracle Database publishes when cluster servers become unreachable or if network interfaces fail.  Use `srvctl` to modify ONS ports. | 6100 (local)  6200 (remote) | Configured manually | TCP | No |
| Oracle Real Application Clusters  The port number is assigned automatically during installation. You cannot view or modify it afterward. | Dynamic | Dynamic | TCP | Yes |
| Oracle Services for Microsoft Transaction Server  The port number for Microsoft Transaction Server is configured automatically by Oracle Universal Installer (OUI) the first time you install the software on a particular server. If you install the software in multiple Oracle homes on the same server, then OUI uses the same port number for all installations.  In most cases, you do not have to reconfigure the port number. Section F.7, "Changing the Oracle Services for Microsoft Transaction Server Port" explains how to change this port number. | Dynamic | 49152 to 65535 | TCP | No |
| Oracle XML DB - HTTP  The Oracle XML DB HTTP port is used if web-based applications must access an Oracle database from an HTTP listener. The port is configured during installation, and you cannot view it afterward.  Section F.6, "Changing the Oracle XML DB Ports" explains how to change this port number. | 0 | Configured manually | HTTP | No |
| Oracle XML DB - FTP  The Oracle XML DB FTP port is used when applications must access an Oracle database from an FTP listener. The port is configured during installation, and you cannot view it afterward.  Section F.6, "Changing the Oracle XML DB Ports" explains how to change this port number. | 0 | Configured manually | FTP | No |

## F.4 Changing the Oracle Management Agent Port

To find the current setting for the Management Agent port, search for `EMD_URL` in the file `%ORACLE_HOME%\` `host_sid` \\ `sysman` `\` `config` `\` `emd.properties`, where `host_sid` is a string that contains the local host name and the SID for the Oracle RAC database.

To change the Management Agent HTTP port, use the `emca -reconfig` `ports` command, as shown in this example:

```
emca -reconfig ports -AGENT_PORT 1831
```

## F.5 Changing the Oracle Enterprise Manager Database Control Ports

To find the current HTTP, RMI, and JMS port settings, search in the following files, where `host_sid` is a string that contains the local host name and the SID for the Oracle RAC database:

- HTTP port: Search for `REPOSITORY_URL` in the `%ORACLE_HOME%\` `host_sid` \\ `sysman` `\` `config` `\` `emd.properties` file
- RMI port: Search for the `port` attribute in the `rmi-server` tag in the file `%ORACLE_HOME%\` `oc4j` `\` `j2ee` `\` `OC4J_DBConsole_` `host_sid` `\` `config` `\` `rmi``.xml` file
- JMS port: Search for the `port` attribute in the `jms-server` tag in the `%ORACLE_HOME%\` `oc4j` `\` `j2ee` `\` `OC4J_DBConsole_` `host_sid` `\` `config` \\ `jms``.xml` file

To change the Oracle Enterprise Manager Database Control ports, use the `emca -reconfig` `ports` command:

```
C:\> %ORACLE_HOME%\bin\emca -reconfig ports option setting
```

In the previous example, `option` specifies one or more of the following ports and `setting` is the new port value:

| Option | Description | Example |
| --- | --- | --- |
| `DBCONTROL_HTTP_PORT` | Sets the HTTP port | `emca -reconfig ports -DBCONTROL_HTTP_PORT 1820` |
| `RMI_PORT` | Sets the RMI port | `emca -reconfig ports -RMI_PORT 5520` |
| `JMS_PORT` | Sets the JMS port | `emca -reconfig ports -JMS_PORT 5521` |

You can specify multiple port settings in one line, for example:

```
emca -reconfig ports -DBCONTROL_HTTP_PORT 1820 -AGENT_PORT 1831 -RMI_PORT 5520
```

## F.6 Changing the Oracle XML DB Ports

By default, the FTP and HTTP (including HTTPS) ports for Oracle XML DB are set to 0, which disables FTP or HTTP access to Oracle XML DB. To change the FTP and HTTP ports for Oracle XML DB, you must run the `catxdbdbca.sql` script, which in a default installation is located in `%ORACLE_HOME%\rdbms\admin`.

To change the Oracle XML DB ports:

1. Check that the Oracle listener is running. In the Windows Services Control Manager, ensure that the Oracle listener service (for example, `OracleOraDb11g_home1TNSListener`) is set to Started.
	If you cannot start the listener, then see [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm).
2. Log in to SQL\*Plus as the `SYS` or `XDB` user using the SYSDBA privilege. For example, to log in to SQL\*Plus as `SYS`:
	```
	SQL> sqlplus sys/ as sysdba
	```
3. Run the `catxdbdbca.sql` script.
	For example, assuming your Oracle home is located in the `C:\app\oracle\product\11.2.0\db_1` directory, to use `2200` for the FTP port and `8200` for the HTTP port, you would enter the following SQL statement:
	```
	SQL> @C:\app\oracle\product\11.2.0\db_1\rdbms\admin\catxdbdbca.sql 2200 8200
	```
4. Exit SQL\*Plus.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for information about connecting to the database using SQL\*Plus

## F.7 Changing the Oracle Services for Microsoft Transaction Server Port

In most cases, you are not required to reconfigure the port number for the Oracle Services for Microsoft Transaction Server. If you must change the port number, then you can use the Registry Editor to edit its value in the `HKEY_LOCAL_MACHINE\SOFTWARE\ORACLE\OracleMTSRecoveryService\Protid_0` Windows Registry key to any available port within the range 1024 to 65535.

During installation, Oracle Universal Installer takes the value for the port from the key, if it exists. Otherwise, a free port ranging from 49152 to 65535 is chosen automatically.
---
title: Configuring Oracle Net Services
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/cnfg_net_srv.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 5 Configuring Oracle Net Services

This chapter describes how to configure Oracle Net Services. It contains the following sections:

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about Oracle Net Services

## 5.1 Locating Oracle Net Services Configuration Files

Oracle Net Services configuration files are typically, but not always, located in the `$ORACLE_HOME/network/admin` directory. Depending on the type of file, Oracle Net uses a different search order to locate the file.

The search order for the `sqlnet.ora` and `ldap.ora` files is as follows:

1. The directory specified by the `TNS_ADMIN` environment variable, if this environment variable is set
2. The `$ORACLE_HOME/network/admin` directory

The search order for the `cman.ora`, `listener.ora`, and `tnsnames.ora` files is as follows:

1. The directory specified by the `TNS_ADMIN` environment variable, if this environment variable is set
2. One of the following directories:
	- On Solaris:
		```
		/var/opt/oracle
		```
		- On other platforms:
		```
		/etc
		```
3. The `$ORACLE_HOME/network/admin` directory

For some system-level configuration files, users may have a corresponding user-level configuration file stored in their home directory. The settings in the user-level file override the settings in the system-level file. The following table lists the system-level configuration files and the corresponding user-level configuration files:

| System-Level Configuration File | User-Level Configuration File |
| --- | --- |
| `sqlnet.ora` | `$HOME/.sqlnet.ora` |
| `tnsnames.ora` | `$HOME/.tnsnames.ora` |

Sample Configuration Files

The `$ORACLE_HOME/network/admin/samples` directory contains samples of the `cman.ora`, `listener.ora`, `sqlnet.ora`, and `tnsnames.ora` configuration files.

Note:

The `cman.ora` file is installed only if you select Connection Manager as part of a custom installation.

## 5.2 Adapters Utility

Use the `adapters` utility to display the transport protocols, naming methods, and Oracle Advanced Security options that Oracle Database supports on the system. To use the `adapters` utility, run the following commands:

```
$ cd $ORACLE_HOME/bin
$ adapters ./oracle
```

On an Oracle Database Client system, the `adapters` utility displays output similar to the following:

```
Oracle Net transport protocols linked with ./oracle are

         IPC
         BEQ
         TCP/IP
         SSL
         RAW

Oracle Net naming methods linked with ./oracle are:

         Local Naming (tnsnames.ora)
         Oracle Directory Naming
         Oracle Host Naming
         NIS Naming

Oracle Advanced Security options linked with ./oracle are:

         RC4 40-bit encryption
         RC4 128-bit encryption
         RC4 256-bit encryption
         DES40 40-bit encryption
         DES 56-bit encryption
         3DES 112-bit encryption
         3DES 168-bit encryption
         AES 128-bit encryption
         AES 192-bit encryption
         SHA crypto-checksumming (for FIPS)
         SHA-1 crypto-checksumming
         Kerberos v5 authentication
         RADIUS authentication
         ENTRUST authentication
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about the `adapters` utility

## 5.3 Oracle Protocol Support

Oracle protocol support is a component of Oracle Net. It includes the following:

- IPC Protocol Support
- TCP/IP Protocol Support
- TCP/IP with Secure Sockets Layer Protocol Support

The IPC, TCP/IP, and TCP/IP with Secure Sockets Layer protocol supports each have an address specification that is used in Oracle Net Services configuration files and in the `DISPATCHER` initialization parameter. The following sections describe the address specifications for each of the protocol supports.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about Oracle protocol support

### 5.3.1 IPC Protocol Support

The IPC protocol support can be used only when the client program and Oracle Database are installed on the same system. This protocol support requires a listener. It is installed and linked to all client tools and the `oracle` executable.

The IPC protocol support requires an address specification in the following format:

```
(ADDRESS = (PROTOCOL=IPC)(KEY=key))
```

The following table describes the parameters used in this address specification:

| Parameter | Description |
| --- | --- |
| PROTOCOL | The protocol to be used. The value is IPC. It is not case-sensitive. |
| KEY | Any name that is different from any other name used for an IPC KEY on the same system. |

The following is a sample IPC protocol address:

```
(ADDRESS= (PROTOCOL=IPC)(KEY=EXTPROC))
```

### 5.3.2 TCP/IP Protocol Support

TCP/IP is the standard communication protocol used for client/server communication over a network. The TCP/IP protocol support enables communication between client programs and Oracle Database, whether they are installed on the same or different systems. If the TCP/IP protocol is installed on the system, then the TCP/IP protocol support is installed and linked to all client tools and to the `oracle` executable.

The TCP/IP protocol support requires an address specification in the following format:

```
(ADDRESS = (PROTOCOL=TCP)(HOST=hostname)(PORT=port))
```

The following table describes the parameters used in this address specification:

| Parameter | Description |
| --- | --- |
| PROTOCOL | The protocol support to be used. The value is TCP. It is not case-sensitive. |
| HOST | The host name or the host IP address. |
| PORT | The TCP/IP port. Specify the port as either a number or the alias name mapped to the port in the `/etc/services` file. Oracle recommends a value of 1521. |

The following is a sample TCP/IP protocol address:

```
(ADDRESS= (PROTOCOL=TCP)(HOST=MADRID)(PORT=1521))
```

### 5.3.3 TCP/IP with Secure Sockets Layer Protocol Support

The TCP/IP with Secure Sockets Layer protocol support enables an Oracle application on a client to communicate with remote Oracle Database instances through TCP/IP and Secure Sockets Layer. To use TCP/IP with Secure Sockets Layer, you must install Oracle Advanced Security.

The TCP/IP with Secure Sockets Layer protocol support requires an address specification in the following format:

```
(ADDRESS = (PROTOCOL=TCPS)(HOST=hostname)(PORT=port))
```

The following table describes the parameters used in this address specification:

| Parameter | Description |
| --- | --- |
| PROTOCOL | The protocol to be used. The value is TCPS. It is not case-sensitive. |
| HOST | The host name or the host IP address. |
| PORT | The TCP/IP with Secure Sockets Layer port. Specify the port as either a number or the alias name mapped to the port in the `/etc/services` file. Oracle recommends a value of 2484. |

The following is a sample TCP/IP with Secure Sockets Layer protocol address:

```
(ADDRESS= (PROTOCOL=TCPS)(HOST=MADRID)(PORT=2484))
```

## 5.4 Setting Up the Listener for TCP/IP or TCP/IP with Secure Sockets Layer

Oracle recommends that you reserve a port for the listener in the `/etc/services` file of each Oracle Net Services node on the network. The default port is 1521. The entry lists the listener name and the port number. For example:

```
oraclelistener    1521/tcp
```

In this example, `oraclelistener` is the name of the listener as defined in the `listener.ora` file. Reserve multiple ports if you intend to start multiple listeners.

If you intend to use Secure Sockets Layer, then you should define a port for TCP/IP with Secure Sockets Layer in the `/etc/services` file. Oracle recommends a value of 2484. For example:

```
oraclelistenerssl     2484/tcps
```

In this example, `oraclelistenerssl` is the name of the listener as defined in the `listener.ora` file. Reserve multiple ports if you intend to start multiple listeners.
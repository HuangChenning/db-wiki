---
title: Parameters for the sqlnet.ora File
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 5 Parameters for the sqlnet.ora File

This chapter provides complete listing of the `sqlnet.ora` file configuration parameters.

This chapter includes the following topics:

## Overview of Profile Configuration File

The `sqlnet.ora` file is the profile configuration file. It resides on the client machines and the database server. Profiles are stored and implemented using this file. The database server can be configured with access control parameters in the `sqlnet.ora` file. These parameters specify whether clients are allowed or denied access based on the protocol.

The `sqlnet.ora` file enables you to do the following:

- Specify the client domain to append to unqualified names
- Prioritize [naming method](glossary.md) s
- Enable logging and tracing features
- Route connections through specific processes
- Configure parameters for [external naming](glossary.md)
- Configure [Oracle Advanced Security](glossary.md)
- Use protocol-specific parameters to restrict access to the database

By default, the `sqlnet.ora` file is located in the `ORACLE_HOME/network/admin` directory. The `sqlnet.ora` file can also be stored in the directory specified by the `TNS_ADMIN` environment variable.

## sqlnet.ora Profile Parameters

This section lists and describes the following `sqlnet.ora` file parameters:

- BEQUEATH\_DETACH
- DEFAULT\_SDU\_SIZE
- DISABLE\_OOB
- NAMES.DEFAULT\_DOMAIN
- NAMES.DIRECTORY\_PATH
- NAMES.LDAP\_AUTHENTICATE\_BIND
- NAMES.LDAP\_CONN\_TIMEOUT
- NAMES.LDAP\_PERSISTENT\_SESSION
- RECV\_BUF\_SIZE
- SDP.PF\_INET\_SDP
- SEC\_USER\_AUDIT\_ACTION\_BANNER
- SEC\_USER\_UNAUTHORIZED\_ACCESS\_BANNER
- SEND\_BUF\_SIZE
- SQLNET.ALLOWED\_LOGON\_VERSION
- SQLNET.AUTHENTICATION\_KERBEROS5\_SERVICE
- SQLNET.AUTHENTICATION\_SERVICES
- SQLNET.CLIENT\_REGISTRATION
- SQLNET.CRYPTO\_CHECKSUM\_CLIENT
- SQLNET.CRYPTO\_CHECKSUM\_SERVER
- SQLNET.CRYPTO\_CHECKSUM\_TYPES\_CLIENT
- SQLNET.CRYPTO\_CHECKSUM\_TYPES\_SERVER
- SQLNET.ENCRYPTION\_CLIENT
- SQLNET.ENCRYPTION\_SERVER
- SQLNET.ENCRYPTION\_TYPES\_CLIENT
- SQLNET.ENCRYPTION\_TYPES\_SERVER
- SQLNET.EXPIRE\_TIME
- SQLNET.INBOUND\_CONNECT\_TIMEOUT
- SQLNET.FALLBACK\_AUTHENTICATION
- SQLNET.KERBEROS5\_CC\_NAME
- SQLNET.KERBEROS5\_CLOCKSKEW
- SQLNET.KERBEROS5\_CONF
- SQLNET.KERBEROS5\_KEYTAB
- SQLNET.KERBEROS5\_REALMS
- SQLNET.OUTBOUND\_CONNECT\_TIMEOUT
- SQLNET.RADIUS\_ALTERNATE
- SQLNET.RADIUS\_ALTERNATE\_PORT
- SQLNET.RADIUS\_ALTERNATE\_RETRIES
- SQLNET.RADIUS\_AUTHENTICATION
- SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE
- SQLNET.RADIUS\_AUTHENTICATION\_PORT
- SQLNET.RADIUS\_AUTHENTICATION\_RETRIES
- SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT
- SQLNET.RADIUS\_CHALLENGE\_RESPONSE
- SQLNET.RADIUS\_SECRET
- SQLNET.RADIUS\_SEND\_ACCOUNTING
- SQLNET.RECV\_TIMEOUT
- SQLNET.SEND\_TIMEOUT
- WALLET\_OVERRIDE
- SSL\_CERT\_REVOCATION
- SSL\_CRL\_FILE
- SSL\_CRL\_PATH
- SSL\_CIPHER\_SUITES
- SSL\_CLIENT\_AUTHENTICATION
- SSL\_EXTENDED\_KEY\_USAGE
- SSL\_SERVER\_DN\_MATCH
- SSL\_VERSION
- TCP.CONNECT\_TIMEOUT
- TCP.EXCLUDED\_NODES
- TCP.INVITED\_NODES
- TCP.NODELAY
- TCP.VALIDNODE\_CHECKING
- TNSPING.TRACE\_DIRECTORY
- TNSPING.TRACE\_LEVEL
- USE\_CMAN
- USE\_DEDICATED\_SERVER
- WALLET\_LOCATION

### BEQUEATH\_DETACH

Purpose

To turn signal handling on or off for Linux and UNIX systems.

Default

NO

Values

- `yes` to turn signal handling off
- `no` to leave signal handling on

Example

```
BEQUEATH_DETACH=yes
```

### DEFAULT\_SDU\_SIZE

Purpose

To specify the [session data unit (SDU)](glossary.md) size, in bytes to connections.

Usage

Oracle recommends setting this parameter in both the client-side and server-side `sqlnet.ora` file to ensure the same SDU size is used throughout a connection. When the configured values of client and database server do not match for a session, the lower of the two values is used.

You can override this parameter for a particular client connection by specifying the [SDU](tnsnames.md) parameter in the connect descriptor for a client.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0141) for complete SDU usage and configuration information

Default

8192 bytes (8 KB)

Values

512 to 65535 bytes

Example

```
DEFAULT_SDU_SIZE=4096
```

### DISABLE\_OOB

Purpose

To enable or disable Oracle Net to send or receive out-of-band break messages using urgent data provided by the underlying protocol.

If turned `off`, then the parameter enables Oracle Net to send and receive break messages. If turned `on`, then the parameter disables the ability to send and receive break messages. Once enabled, this feature applies to all protocols used by this client.

Default

OFF

Example

```
DISABLE_OOB=on
```

See Also:

Operating system-specific documentation to determine if the protocols you are using support urgent data requests. TCP/IP is an example of a protocol that supports this feature.

### NAMES.DEFAULT\_DOMAIN

Purpose

To set the domain from which the client most often looks up names resolution requests. When this parameter is set, the default domain name is automatically appended to any unqualified net service name or service name.

For example, if the default domain is set to `us.example.com`, then the connect string `CONNECT scott@sales` gets searched as `sales.us.example.com`. If the connect string includes the domain extension, such as `CONNECT scott@sales.us.example.com`, then the domain is not appended to the string.

Default

None

Example

```
NAMES.DEFAULT_DOMAIN=example.com
```

### NAMES.DIRECTORY\_PATH

Purpose

To specify the order of the naming methods used for client name resolution lookups.

Default

NAMES.DIRECTORY\_PATH=(tnsnames, ldap, ezconnect)

Values

| Naming Method Value | Description |
| --- | --- |
| `tnsnames` ([local naming](glossary.md) method) | Set to resolve a [net service name](glossary.md) through the `tnsnames.ora` file on the client. |
| `ldap (`[directory naming](glossary.md) method) | Set to resolve a database service name, net service name, or [net service alias](glossary.md) through a [directory server](glossary.md). |
| `ezconnect` or `hostname` (Easy Connect naming method) | Select to enable clients to use a TCP/IP connect identifier, consisting of a host name and optional port and service name. |
| `nis` (external naming method) | Set to resolve service information through an existing [Network Information Service (NIS)](glossary.md). |

Example

```
NAMES.DIRECTORY_PATH=(tnsnames)
```

### NAMES.LDAP\_AUTHENTICATE\_BIND

Purpose

To specify whether the LDAP naming adapter should attempt to authenticate using a specified wallet when it connects to the LDAP directory to resolve the name in the connect string.

Usage

The parameter value is Boolean.

If the parameter is set to `TRUE`, then the LDAP connection is authenticated using a wallet whose location must be specified in the WALLET\_LOCATION parameter.

If the parameter is set to `FALSE`, then the LDAP connection is established using an anonymous bind.

Default

FALSE

Example

```
NAMES.LDAP_AUTHENTICATE_BIND=TRUE
```

### NAMES.LDAP\_CONN\_TIMEOUT

Purpose

To specify number of seconds for a non-blocking connect timeout to the LDAP server.

Usage

The parameter value -1 is for infinite timeout.

Default

15 seconds

Values

Values are in seconds. The range is `-1` to the number of seconds acceptable for your environment. There is no upper limit.

Example

```
names.ldap_conn_timeout = -1
```

### NAMES.LDAP\_PERSISTENT\_SESSION

Purpose

To specify whether the LDAP naming adapter should leave the session with the LDAP server open after name lookup is complete.

Usage

The parameter value is Boolean.

If the parameter is set to `TRUE`, then the connection to the LDAP server is left open after the name lookup is complete; the connection will effectively stay open for the duration of the process. If the connection is lost, then it will be re-established as needed.

If the parameter is set to `FALSE`, then the LDAP connection is terminated as soon as the name lookup completes. Every subsequent lookup opens the connection, performs the lookup, and closes the connection. This option prevents the LDAP server from having a large number of clients connected to it at any one time.

Default

FALSE

Example

```
NAMES.LDAP_PERSISTENT_SESSION=TRUE
```

### RECV\_BUF\_SIZE

Purpose

To specify the buffer space limit for receive operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to the operating system-specific documentation for additional information about additional protocols that support this parameter.

See Also:

[Oracle Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

Default

The default value for this parameter is operating system-specific.

Usage

You can override this parameter for a particular client connection by specifying the [RECV\_BUF\_SIZE](tnsnames.md) parameter in the connect descriptor for a client.

Example

```
RECV_BUF_SIZE=11784
```

### SDP.PF\_INET\_SDP

Purpose

To specify the protocol family or address family constant for the SDP protocol on your system.

Default

27

Values

Any positive integer

Example

```
SDP.PF_INET_SDP=30
```

### SEC\_USER\_AUDIT\_ACTION\_BANNER

Purpose

To specify a text file containing the banner contents that warn the user about possible user action auditing. The complete path of the text file must be specified in the `sqlnet.ora` file on the server. Oracle Call Interface (OCI) applications can make use of OCI features to retrieve this banner and display it to the user. The text file has a maximum limit of 512 bytes.

Default

None

Values

Name of the file for which the database owner has read permissions.

Example

```
SEC_USER_AUDIT_ACTION_BANNER=/opt/oracle/admin/data/auditwarning.txt
```

### SEC\_USER\_UNAUTHORIZED\_ACCESS\_BANNER

Purpose

To specify a text file containing the banner contents that warn the user about unauthorized access to the database. The complete path of the text file must be specified in the `sqlnet.ora` file on the server. OCI applications can make use of OCI features to retrieve this banner and display it to the user. The text file has a maximum limit of 512 bytes.

Default

None

Values

Name of the file for which the database owner has read permissions.

Example

```
SEC_USER_UNAUTHORIZED_ACCESS_BANNER=/opt/oracle/admin/data/unauthwarning.txt
```

### SEND\_BUF\_SIZE

Purpose

To specify the buffer space limit for send operations of sessions. This parameter is supported by the TCP/IP, TCP/IP with SSL, and SDP protocols.

Note:

Additional protocols might support this parameter on certain operating systems. Refer to the operating system-specific documentation for additional information about additional protocols that support this parameter.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0142) for additional information about configuring this parameter

Default

The default value for this parameter is operating system-specific.

Usage

You can override this parameter for a particular client connection by specifying the [SEND\_BUF\_SIZE](tnsnames.md) parameter in the connect descriptor for a client.

Example

```
SEND_BUF_SIZE=11784
```

### SQLNET.ALLOWED\_LOGON\_VERSION

Purpose

To set the minimum authentication protocol allowed when connecting to Oracle Database instances. The term `VERSION` in the parameter name refers to the version of the authentication protocol, not the Oracle Database release.

If the client release does not meet or exceed the value defined by this parameter, then authentication fails with an `ORA-28040: No matching authentication protocol` error or an `ORA-03134: Connections to this server version are no longer supported` error.

Usage Notes

A setting of `8` permits most password versions, and allows any combination of the `DBA_USERS.PASSWORD_VERSIONS` values `10G`, and `11G`.

A greater value means the server is less compatible in terms of the protocol that clients must understand in order to authenticate. The server is also more restrictive in terms of the password version that must exist to authenticate any specific account. The ability for a client to authenticate depends on the `DBA_USERS.PASSWORD_VERSIONS` value on the server for that account.

Note the following implications of setting the value to `12`:

- To take advantage of the password protections introduced in Oracle Database 11g, users must change their passwords. The new passwords are case sensitive. When an account password is changed, the earlier `10G` case-insensitive password version is automatically removed.
- Releases of OCI clients before Oracle Database 10g and all versions of JDBC thin clients cannot authenticate to the Oracle database using password-based authentication.
- If the client uses Oracle9i Database, then the client will receive an `ORA-03134` error message. To allow the connection, remove the `SQLNET.ALLOWED_LOGON_VERSION` setting to return to the default. Ensure the `DBA_USERS.PASSWORD_VERSIONS` value for the account contains the value `10G`. It may be necessary to reset the password for that account.

The client must support certain abilities of an authentication protocol before the server will authenticate. If the client does not support a specified authentication ability, then the server rejects the connection with an `ORA-28040: No matching authentication protocol` error message.

The following is the list of all client abilities. Some clients do not have all abilities. Clients that are more recent have all the capabilities of the older clients, but older clients tend to have less abilities than more recent clients.

- `O5L_NP`: The ability to perform the Oracle Database 10g authentication protocol using the `11G` password version, and generating a session key encrypted for critical patch update CPUOct2012.
- `O5L`: The ability to perform the Oracle Database 10g authentication protocol using the `10G` password version.
- `O4L`: The ability to perform the Oracle9i database authentication protocol using the `10G` password version.
- `O3L`: The ability to perform the Oracle8i database authentication protocol using the `10G` password version.

A higher ability value is more recent and secure than a lower ability value. Clients that are more recent have all the capabilities of the older clients.

The following table describes the allowed values, password versions, and descriptions:

| Value of the ALLOWED\_LOGON\_VERSION Parameter | Generated Password Version | Ability Required of the Client | Meaning for Clients |
| --- | --- | --- | --- |
|  |  |  |  |
| `12` <sup>Foot 1</sup> | `11G` | `O5L_NP` | Only clients which have applied critical patch update CPUOct2012 or later, or release 11.2.0.3 clients with an equivalent update can connect to the server. |
| `11` | `10G`, `11G` | `O5L` | Clients using Oracle Database 10g and later can connect to the server.  Clients using releases earlier than Oracle Database release 11.2.0.3 that have not applied critical patch update CPUOct2012 or later patches must use the `10G` password version. |
| `10` | `10G`, `11G` | `O5L` | Clients using Oracle Database 10g and later can connect to the server.  Clients using releases earlier than Oracle Database release 11.2.0.3 that have not applied critical patch update CPUOct2012 or later patches must use the `10G` password version. |
| `9` | `10G`, `11G` | `O4L` | Oracle9i Database or later clients can connect to the server. |
| `8` | `10G`, `11G` | `O3L` | Oracle8i Database and later clients can connect to the server. |

<sup>Footnote 1</sup> This is considered "Exclusive Mode" because it excludes the use of the `10G` password version.

Allowed Values

- `12` for the critical patch updates CPUOct2012 and later Oracle Database 11g authentication protocols (recommended)
- `11` for Oracle Database 11g authentication protocols
- `10` for Oracle Database 10g authentication protocols
- `9` for Oracle9i Database authentication protocols
- `8` for Oracle8i Database authentication protocols (default)

Default

8

Example

If both Oracle Database 11g and Oracle Database 10g are present, then set the parameter as follows:

```
SQLNET.ALLOWED_LOGON_VERSION=10
```

### SQLNET.AUTHENTICATION\_KERBEROS5\_SERVICE

Purpose

To define the name of the service used to obtain a Kerberos service ticket.

Default

None

Example

```
SQLNET.AUTHENTICATION_KERBEROS5_SERVICE=oracle
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.AUTHENTICATION\_SERVICES

Purpose

To enable one or more authentication services. If authentication has been installed, then it is recommended that this parameter be set to either `none` or to one of the listed authentication methods.

Usage Notes

When using the `SQLNET.AUTHENTICATION_SERVICES` value `all`, the server attempts to authenticate using each of the following methods. The server falls back to the ones lower on the list if the ones higher on the list were unsuccessful.

- Authentication based on a service external to the database, such as a service on the network layer, Kerberos, or RADIUS.
- Authentication based on the operating system user's membership in an administrative operating system group. Group names are platform-specific. This authentication is applicable to administrative connections only.
- Authentication performed by the database.
- Authentication based on credentials stored in a directory server.

Operating system authentication allows access to the database using any user name and any password when an administrative connection is attempted, such as using the `AS SYSDBA` clause when connecting using SQL\*Plus. An example of a connection is as follows.

```
sqlplus ignored_username/ignored_password AS SYSDBA
```

When the operating-system user who issued the preceding command is already a member of the appropriate administrative operating system group, then the connection is successful. This is because the user name and password are ignored by the server due to checking the group membership first.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG003) for additional information about authentication methods

Default

`all`

Note:

When installing the database with Database Configuration Assistant (DBCA), this parameter may be set to `nts` in the `sqlnet.ora` file.

Values

Authentication methods available with Oracle Net Services:

- `none` for no authentication methods, including Microsoft Windows native operating system authentication. When `SQLNET.AUTHENTICATION_SERVICES` is set to `none`, a valid user name and password can be used to access the database.
- `all` for all authentication methods.
- `beq` for native operating system authentication for operating systems other than Microsoft Windows
- `kerberos5` for Kerberos authentication
- `nts` for Microsoft Windows native operating system authentication
- `radius` for Remote Authentication Dial-In User Service (RADIUS) authentication
- `tcps` for SSL authentication

Example

```
SQLNET.AUTHENTICATION_SERVICES=(kerberos5)
```

See Also:

[Oracle Database Security Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=DBSEG9768)

### SQLNET.CLIENT\_REGISTRATION

Purpose

To set a unique identifier for the client computer. This identifier is passed to the listener with any connection request and is included in the Audit Trail. The identifier can be any alphanumeric string up to 128 characters long.

Default

None

Example

```
SQLNET.CLIENT_REGISTRATION=1432
```

### SQLNET.CRYPTO\_CHECKSUM\_CLIENT

Purpose

To specify the checksum behavior for the client.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

Default

accepted

Values

- `accepted` to enable the security service if required or requested by the other side.
- `rejected` to disable the security service, even if the required by the other side.
- `requested` to enable the security service if the other side allows it.
- `required` to enable the security service and disallow the connection if the other side is not enabled for the security service.

Example

```
SQLNET.CRYPTO_CHECKSUM_CLIENT=accepted
```

### SQLNET.CRYPTO\_CHECKSUM\_SERVER

Purpose

To specify the checksum behavior for the database server.

Default

accepted

Values

- `accepted` to enable the security service if required or requested by the other side.
- `rejected` to disable the security service, even if the required by the other side.
- `requested` to enable the security service if the other side allows it.
- `required` to enable the security service and disallow the connection if the other side is not enabled for the security service.

Example

```
SQLNET.CRYPTO_CHECKSUM_SERVER=accepted
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.CRYPTO\_CHECKSUM\_TYPES\_CLIENT

Purpose

To specify a list of crypto-checksum algorithms for the client to use.

Default

All available algorithms

Values

- `md5` for the RSA Data Security MD5 algorithm.
- `sha1` for the Secure Hash algorithm.

Example

```
SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT=(MD5)
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.CRYPTO\_CHECKSUM\_TYPES\_SERVER

Purpose

To specify a list of crypto-checksum algorithms for the database server to use.

Default

All available algorithms

Values

- `md5` for the RSA Data Security's MD5 algorithm
- `sha1` for the Secure Hash algorithm

Example

```
SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER=(md5)
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.ENCRYPTION\_CLIENT

Purpose

To turn encryption on for the client.

Default

accepted

Values

- `accepted` to enable the security service if required or requested by the other side.
- `rejected` to disable the security service, even if the required by the other side.
- `requested` to enable the security service if the other side allows it.
- `required` to enable the security service and disallow the connection if the other side is not enabled for the security service.

Example

```
SQLNET.ENCRYPTION_CLIENT=accepted
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.ENCRYPTION\_SERVER

Purpose

To turn encryption on for the database server.

Default

accepted

Values

- `accepted` to enable the security service if required or requested by the other side.
- `rejected` to disable the security service, even if the required by the other side.
- `requested` to enable the security service if the other side allows it.
- `required` to enable the security service and disallow the connection if the other side is not enabled for the security service.

Example

```
SQLNET.ENCRYPTION_SERVER=accepted
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.ENCRYPTION\_TYPES\_CLIENT

Purpose

To specify a list of encryption algorithms for the client to use.

Default

All available algorithms.

Values

One or more of the following:

- `3des112` for triple DES with a two-key (112-bit) option
- `3des168` for triple DES with a three-key (168-bit) option
- `des` for standard 56-bit key size
- `des40` for 40-bit key size
- `rc4_40` for 40-bit key size
- `rc4_56` for 56-bit key size
- `rc4_128` for 128-bit key size
- `rc4_256` for 256-bit key size

Example

```
SQLNET.ENCRYPTION_TYPES_CLIENT=(rc4_56)
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.ENCRYPTION\_TYPES\_SERVER

Purpose

To specify a list of encryption algorithms for the database server to use.

Default

All available algorithms.

Values

One or more of the following:

- `3des112` for triple DES with a two-key (112-bit) option
- `3des168` for triple DES with a three-key (168-bit) option
- `des` for standard 56-bit key size
- `des40` for 40-bit key size
- `rc4_40` for 40-bit key size
- `rc4_56` for 56-bit key size
- `rc4_128` for 128-bit key size
- `rc4_256` for 256-bit key size

Example

```
SQLNET.ENCRYPTION_TYPES_SERVER=(rc4_56, des, ...)
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.EXPIRE\_TIME

Purpose

To specify a time interval, in minutes, to send a check to verify that client/server connections are active. The following usage notes apply to this parameter:

- Setting a value greater than 0 ensures that connections are not left open indefinitely, due to an abnormal client termination.
- If the probe finds a terminated connection, or a connection that is no longer in use, then it returns an error, causing the server process to exit.
- This parameter is primarily intended for the database server, which typically handles multiple connections at any one time.
- Limitations on using this terminated connection detection feature are:
	- It is not allowed on bequeathed connections.
		- Though very small, a probe packet generates additional traffic that may downgrade network performance.
		- Depending on which operating system is in use, the server may need to perform additional processing to distinguish the connection probing event from other events that occur. This can also result in degraded network performance.

Default

0

Minimum Value

0

Recommended Value

10

Example

```
SQLNET.EXPIRE_TIME=10
```

### SQLNET.INBOUND\_CONNECT\_TIMEOUT

Purpose

To specify the time, in seconds, for a client to connect with the database server and provide the necessary authentication information.

If the client fails to establish a connection and complete authentication in the time specified, then the database server terminates the connection. In addition, the database server logs the IP address of the client and an `ORA-12170: TNS:Connect timeout occurred` error message to the `sqlnet.log` file. The client receives either an `ORA-12547: TNS:lost contact` or an `ORA-12637: Packet receive failed` error message.

The default value of this parameter is appropriate for typical usage scenarios. However, if you need to explicitly set a different value, then Oracle recommends setting this parameter in combination with the [INBOUND\_CONNECT\_TIMEOUT\_listener\_name](listener.md) parameter in the `listener.ora` file. When specifying the values for these parameters, note the following recommendations:

- Set both parameters to an initial low value.
- Set the value of the `INBOUND_CONNECT_TIMEOUT_` `listener_name` parameter to a lower value than the `SQLNET.INBOUND_CONNECT_TIMEOUT` parameter.

For example, you can set `INBOUND_CONNECT_TIMEOUT_` `listener_name` to 2 seconds and `SQLNET.INBOUND_CONNECT_TIMEOUT` parameter to 3 seconds. If clients are unable to complete connections within the specified time due to system or network delays that are normal for the particular environment, then increment the time as needed.

Default

60 seconds

Example

```
SQLNET.INBOUND_CONNECT_TIMEOUT=3
```

See Also:

- ["Control Parameters"](listener.md) for additional information about `INBOUND_CONNECT_TIMEOUT_` `listener_name`
- [Oracle Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0144) for additional information about configuring these parameters

### SQLNET.FALLBACK\_AUTHENTICATION

Purpose

To specify whether password-based authentication is going to be attempted if Kerberos authentication fails. This is relevant for direct connections as well as database link connections.

Default

`FALSE`

Example

```
SQLNET.FALLBACK_AUTHENTICATION=TRUE
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asokerb.htm#ASOAG10654)

### SQLNET.KERBEROS5\_CC\_NAME

Purpose

To specify the complete path name to the Kerberos credentials cache file.

Default

`/usr/tmp/krbcache` on Linux and UNIX operating systems, and `c:\tmp\krbcache` on Microsoft Windows operating systems

Example

```
SQLNET.KERBEROS5_CC_NAME=/usr/tmp/krbcache
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.KERBEROS5\_CLOCKSKEW

Purpose

To specify how many seconds can pass before a Kerberos credential is considered out of date.

Default

300

Example

```
SQLNET.KERBEROS5_CLOCKSKEW=1200
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.KERBEROS5\_CONF

Purpose

To specify the complete path name to the Kerberos configuration file, which contains the realm for the default Key Distribution Center (KDC) and maps realms to KDC hosts. The KDC maintains a list of user principals and is contacted through the `kinit` program for the user's initial ticket.

Default

`/krb5/krb.conf` on Linux and UNIX operating systems and `c:\krb5\krb.conf` on Microsoft Windows operating systems

Example

```
SQLNET.KERBEROS5_CONF=/krb5/krb.conf
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.KERBEROS5\_KEYTAB

Purpose

To specify the complete path name to the Kerberos principal/secret key mapping file, which is used to extract keys and decrypt incoming authentication information.

Default

`/etc/v5srvtab` on Linux and UNIX operating systems and `c:\krb5\v5srvtab` on Microsoft Windows operating systems

Example

```
SQLNET.KERBEROS5_KEYTAB=/etc/v5srvtab
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.KERBEROS5\_REALMS

Purpose

To specify the complete path name to the Kerberos realm translation file, which provides a mapping from a host name or domain name to a realm.

Default

`/krb5/krb.realms` on Linux and UNIX operating systems and `c:\krb5\krb.realms` on Microsoft Windows operating systems

Example

```
SQLNET.KERBEROS5_REALMS=/krb5/krb.realms
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.OUTBOUND\_CONNECT\_TIMEOUT

Purpose

To specify the time, in seconds, for a client to establish an Oracle Net connection to the database instance.

If an Oracle Net connection is not established in the time specified, then the connect attempt is terminated. The client receives an `ORA-12170: TNS:Connect timeout occurred` error.

The outbound connect timeout interval is a superset of the TCP connect timeout interval, which specifies a limit on the time taken to establish a TCP connection. Additionally, the outbound connect timeout interval includes the time taken to be connected to an Oracle instance providing the requested service.

Without this parameter, a client connection request to the database server may block for the default TCP connect timeout duration (60 seconds) when the database server host system is unreachable.

The outbound connect timeout interval is only applicable for TCP, TCP with SSL, and IPC transport connections.

Default

None

Usage Notes

This parameter is overridden by the `CONNECT_TIMEOUT` parameter in the address description.

Example

```
SQLNET.OUTBOUND_CONNECT_TIMEOUT=10
```

### SQLNET.RADIUS\_ALTERNATE

Purpose

To specify an alternate RADIUS server to use in case the primary server is unavailable. The value can be either the IP address or host name of the server.

Default

None

Example

```
SQLNET.RADIUS_ALTERNATE=radius2
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_ALTERNATE\_PORT

Purpose

To specify the listening port of the alternate RADIUS server.

Default

1645

Example

```
SQLNET.RADIUS_ALTERNATE_PORT=1667
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_ALTERNATE\_RETRIES

Purpose

To specify the number of times the database server should resend messages to the alternate RADIUS server.

Default

3

Example

```
SQLNET.RADIUS_ALTERNATE_RETRIES=4
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_AUTHENTICATION

Purpose

To specify the location of the primary RADIUS server, either by its host name or IP address.

Default

Local host

Example

```
SQLNET.RADIUS_AUTHENETICATION=officeacct
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE

Purpose

To specify the class containing the user interface used to interact with the user.

Default

DefaultRadiusInterface

Example

```
SQLNET.RADIUS_AUTHENTICATION_INTERFACE=DefaultRadiusInterface
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_AUTHENTICATION\_PORT

Purpose

Use the parameter `SQLNET.RADIUS_AUTHENTICATION_PORT` to specify the listening port of the primary RADIUS server.

Default

1645

Example

```
SQLNET.RADIUS_AUTHENTICATION_PORT= 1667
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_AUTHENTICATION\_RETRIES

Purpose

To specify the number of times the database server should resend messages to the primary RADIUS server.

Default

3

Example

```
SQLNET.RADIUS_AUTHENTICATION_RETRIES=4
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT

Purpose

To specify the time, in seconds, that the database server should wait for a response from the primary RADIUS server.

Default

5

Example

```
SQLNET.RADIUS_AUTHENTICATION_TIMEOUT=10
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_CHALLENGE\_RESPONSE

Purpose

To turn challenge response on or off.

Default

off

Values

```
on | off
```

Example

```
SQLNET.RADIUS_CHALLENGE_RESPONSE=on
```

### SQLNET.RADIUS\_SECRET

Purpose:

To specify the location of the RADIUS secret key.

Default

The `ORACLE_HOME/network/security/radius.key` file.

Example

```
SQLNET.RADIUS_SECRET=oracle/bin/admin/radiuskey
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RADIUS\_SEND\_ACCOUNTING

Purpose

To turn accounting `on` and `off`. If enabled, then packets are sent to the active RADIUS server at listening port plus one. The default port is 1646.

Default

off

Values

```
on | off
```

Example

```
SQLNET.RADIUS_SEND_ACCOUNTING=on
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SQLNET.RECV\_TIMEOUT

Purpose

To specify the time, in seconds, for a database server to wait for client data after establishing a connection. A client must send some data within the time interval.

For environments in which clients shut down on occasion or abnormally, setting this parameter is recommended. If a client does not send any data in time specified, then the database server logs `ORA-12535: TNS:operation timed out` and `ORA-12609: TNS: Receive timeout occurred` messages to the `sqlnet.log` file. Without this parameter, the database server may continue to wait for data from clients that may be down or are experiencing difficulties.

You can also set this parameter on the client-side to specify the time, in seconds, for a client to wait for response data from the database server after connection establishment. Without this parameter, the client may wait a long period of time for a response from a database server saturated with requests. If you choose to set the value, then set the value to an initial low value and adjust according to system and network capacity. If necessary, use this parameter with the SQLNET.SEND\_TIMEOUT parameter.

Default

None

Example

```
SQLNET.RECV_TIMEOUT=3
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm#NETAG091) for additional information about configuring these parameters

### SQLNET.SEND\_TIMEOUT

Purpose

To specify the time, in seconds, for a database server to complete a send operation to clients after establishing a connection. Setting this parameter is recommended for environments in which clients shut down occasionally or abnormally.

If the database server cannot complete a send operation in the time specified, then it logs `ORA-12535: TNS:operation timed out` and `ORA-12608: TNS: Send timeout occurred` messages to the `sqlnet.log` file. Without this parameter, the database server may continue to send responses to clients that are unable to receive data due to a downed computer or a busy state.

You can also set this parameter on the client-side to specify the time, in seconds, for a client to complete send operations to the database server after connection establishment. Without this parameter, the client may continue to send requests to a database server already saturated with requests. If you choose to set the value, then set the value to an initial low value and adjust according to system and network capacity. If necessary, use this parameter with the SQLNET.RECV\_TIMEOUT parameter.

Default

None

Example

```
SQLNET.SEND_TIMEOUT=3
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm#NETAG091) for additional information about configuring these parameters

### WALLET\_OVERRIDE

Purpose

To determine whether the client should override the strong authentication credential with the password credential in the stored wallet to log in to the database.

Usage Notes

- When wallets are used for authentication, the database credentials for user name and password are securely stored in an Oracle wallet. The auto-login feature of the wallet is turned on so the database does not need a password to open the wallet. From the wallet, the database gets the credentials to access the database for the user.
- Wallet usage can simplify large-scale deployments that rely on password credentials for connecting to databases. When this feature is configured, application code, batch jobs, and scripts do not need embedded user names and passwords. Risk is reduced because such passwords are no longer exposed in the clear, and password management policies are more easily enforced without changing application code whenever user names or passwords change.
- Users connect using the `connect /@` `database_name` command instead of specifying a user name and password explicitly. This simplifies the maintenance of the scripts and secures the password management for the applications.
- Middle-tier applications create an Oracle Applications wallet at installation time to store the application's specific identity. The password may be randomly generated rather than hardcoded. When an Oracle application accesses the database, it sets appropriate values for `SQLNET.AUTHENTICATION_SERVICES` and `WALLET_LOCATION`. The new wallet-based password authentication code uses the password credential in the Oracle Applications wallet to log on to the database.

Values

```
TRUE | FALSE
```

Examples

```
WALLET_OVERRIDE=TRUE
```

See Also:

In order to use wallets, a wallet must be configured on the client. Refer to [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG30253) for additional information about configuring the clients.

### SSL\_CERT\_REVOCATION

Purpose

To configure a revocation check for a certificate.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

Default

None

Values

- `none` to turn off certificate revocation checking. This is the default.
- `requested` to perform certificate revocation in case a Certificate Revocation List (CRL) is available. Reject SSL connection if the certificate is revoked. If no appropriate CRL is found to determine the revocation status of the certificate and the certificate is not revoked, then accept the SSL connection.
- `required` to perform certificate revocation when a certificate is available. If a certificate is revoked and no appropriate CRL is found, then reject the SSL connection. If no appropriate CRL is found to ascertain the revocation status of the certificate and the certificate is not revoked, then accept the SSL connection.

Example

```
SSL_CERT_REVOCATION=required
```

### SSL\_CRL\_FILE

Purpose

To specify the name of the file where you can assemble the certificate revocation list (CRL) for client authentication.

This file contains the PEM-encoded CRL files, in order of preference. You can use this file alternatively or in addition to the SSL\_CRL\_PATH parameter. This parameter is only valid if SSL\_CERT\_REVOCATION is set to either `requested` or `required`.

Default

None

Example

```
SSL_CRL_FILE=
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SSL\_CRL\_PATH

Purpose

To specify the destination directory of the CRL of CA. The files in this directory are hashed symbolic links created by Oracle Wallet Manager. This parameter is only valid if SSL\_CERT\_REVOCATION is set to either `requested` or `required`.

See Also:

[Oracle Database Security Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=DBSEG9701)

Default

None

Example

```
SSL_CRL_PATH=
```

### SSL\_CIPHER\_SUITES

Purpose

To control which combination of encryption and data integrity is used by the [Secure Sockets Layer (SSL)](glossary.md). Cipher suites that use Advanced Encryption Standard (AES) only work with Transport Layer Security (TLS 1.0).

Default

None

Values

- SSL\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- SSL\_RSA\_WITH\_RC4\_128\_SHA
- SSL\_RSA\_WITH\_RC4\_128\_MD5
- SSL\_RSA\_WITH\_DES\_CBC\_SHA
- SSL\_DH\_anon\_WITH\_3DES\_EDE\_CBC\_SHA
- SSL\_DH\_anon\_WITH\_RC4\_128\_MD5
- SSL\_DH\_anon\_WITH\_DES\_CBC\_SHA
- SSL\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5
- SSL\_RSA\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_RSA\_WITH\_AES\_128\_CBC\_SHA
- SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA

Example

```
SSL_CIPHER_SUITES=(ssl_rsa_with_rc4_138_md5)
```

See Also:

[Oracle Database Security Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=DBSEG9805) for additional information about cipher suite values

### SSL\_CLIENT\_AUTHENTICATION

Purpose

To specify whether a client, in addition to the database server, is authenticated using SSL.

Default

true

Values

```
true | false
```

Example

```
SSL_CLIENT_AUTHENTICATION=true
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SSL\_EXTENDED\_KEY\_USAGE

Purpose

To specify the purpose of the key in the certificate. When this parameter is specified, the certificate with the matching extended key is used.

Values

`client authentication`

Example

```
SSL_EXTENDED_KEY_USAGE="client authentication"
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asossl.htm#ASOAG10541)

### SSL\_SERVER\_DN\_MATCH

Purpose

To enforce that the [distinguished name (DN)](glossary.md) for the database server matches its service name. If you enforce the match verifications, then SSL ensures that the certificate is from the server. If you select to not enforce the match verification, then SSL performs the check but allows the connection, regardless if there is a match. Not enforcing the match allows the server to potentially fake its identify.

Default

no

Values

- `yes` | `on` | `true` to specify to enforce a match. If the DN matches the service name, then the connection succeeds. If the DN does not match the service name, then the connection fails.
- `no` | `off` | `false` to specify not to enforce a match. If the DN does not match the service name, then the connection is successful, but an error is logged to the `sqlnet.log` file.

Usage Notes

In addition to the `sqlnet.ora` file, configure the `tnsnames.ora` parameter [SSL\_SERVER\_CERT\_DN](tnsnames.md) to enable server DN matching.

Example

```
SSL_SERVER_DN_MATCH=yes
```

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### SSL\_VERSION

Purpose

To force the version of the SSL connection. Clients and database servers must use a compatible version.

Default

undetermined

Values

```
undetermined | 3.0 | 1.0 | 1.1 | 1.2
```

If you want to specify one version or another version, then use `or`. The following values are permitted:

```
1.0 or 3.0 | 1.2 or 3.0 | 1.1 or 1.0 | 1.2 or 1.0 | 1.2 or 1.1 | 1.1 or 1.0 or 3.0 | 
1.2 or 1.0 or 3.0 | 1.2 or 1.1 or 1.0 | 1.2 or 1.1 or 3.0 |1.2 or 1.1 or 1.0 or 3
```

Example

```
SSL_VERSION=3.0
```

The remaining version numbers correspond to the TLS versions, such as, TLSv1.0, TLSv1.1, and TLSv1.2.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### TCP.CONNECT\_TIMEOUT

Purpose

To specify the time, in seconds, for a client to establish a TCP connection (`PROTOCOL=tcp` in the TNS connect address) to the database server. If a TCP connection to the database host is not established in the time specified, then the connection attempt is terminated. The client receives an `ORA-12170: TNS:Connect timeout occurred` error.

The timeout applies to each IP address to which a host name resolves. For example, if a host name resolves to an IPv6 and an IPv4 address, and if the host is not reachable through the network, then the connection request times out twice the `TCP.CONNECT_TIMEOUT` setting because there are two IP addresses. In this example, the default timeout setting of 60 would cause a timeout in 120 seconds.

Default

60

Example

```
TCP.CONNECT_TIMEOUT=10
```

### TCP.EXCLUDED\_NODES

Purpose

To specify which clients are denied access to the database.

Syntax

```
TCP.EXCLUDED_NODES=(hostname | ip_address, hostname | ip_address, ...)
```

Usage Notes

- This parameter is only valid when the `TCP.VALIDNODE_CHECKING` parameter is set to `yes`.
- This parameter can use wildcards for IPv4 addresses and CIDR (Classless Inter-Domain Routing) notation for IPv4 and IPv6 addresses.

Example

```
TCP.EXCLUDED_NODES=(finance.us.example.com, mktg.us.example.com, 192.168.2.25, 172.30.*, 2001:DB8:200C:417A/32)
```

### TCP.INVITED\_NODES

Purpose

To specify which clients are allowed access to the database. This list takes precedence over the `TCP.EXCLUDED_NODES` parameter if both lists are present.

Syntax

```
TCP.INVITED_NODES=(hostname | ip_address, hostname | ip_address, ...)
```

Usage Notes

- This parameter is only valid when the `TCP.VALIDNODE_CHECKING` parameter is set to `yes`.
- This parameter can use wildcards for IPv4 addresses and CIDR notation for IPv4 and IPv6 addresses.

Example

```
TCP.INVITED_NODES=(sales.us.example.com, hr.us.example.com, 192.168.*, 2001:DB8:200C:433B/32)
```

### TCP.NODELAY

Purpose

To preempt delays in buffer flushing within the TCP/IP protocol stack.

Default

yes

Values

```
yes | no
```

Example

```
TCP.NODELAY=yes
```

### TCP.VALIDNODE\_CHECKING

Purpose

To enable and disable valid node checking for incoming connections. If this parameter is set to `yes`, then incoming connections are allowed only if they originate from a node that conforms to list specified by TCP.INVITED\_NODES or TCP.EXCLUDED\_NODES parameters.

Default

no

Values

```
yes | no
```

Usage Notes

The TCP.INVITED\_NODES and TCP.EXCLUDED\_NODES parameters are valid only when the TCP.VALIDNODE\_CHECKING parameter is set to `yes`.

Example

```
TCP.VALIDNODE_CHECKING=yes
```

### TNSPING.TRACE\_DIRECTORY

Purpose

To specify the destination directory for the TNSPING utility trace file, `tnsping.trc`.

Default

The `ORACLE_HOME/network/trace` directory.

Example

```
TNSPING.TRACE_DIRECTORY=/oracle/traces
```

### TNSPING.TRACE\_LEVEL

Purpose

To turn TNSPING utility tracing on at a specified level or to turn it off.

Default

off

Values

- `off` for no trace output
- `user` for user trace information
- `admin` for administration trace information
- `support` for Oracle Support Services trace information

Example

```
TNSPING.TRACE_LEVEL=admin
```

### USE\_CMAN

Purpose

To specify client routing to Oracle Connection Manager.

If set to `true`, then the parameter routes the client to a protocol address for an Oracle Connection Manager.

If set to `false`, then the client picks one of the address lists at random and fails over to the other address list if the chosen `ADDRESS_LIST` fails. With `USE_CMAN` = `true`, the client always uses the first address list.

If no Oracle Connection Manager addresses are available, then connections are routed through any available listener address.

Default

false

Values

```
true | false
```

Example

```
USE_CMAN=true
```

### USE\_DEDICATED\_SERVER

Purpose

To append `(SERVER=dedicated)` to the `CONNECT_DATA` section of the connect descriptor used by the client. It overrides the current value of the [SERVER](tnsnames.md) parameter in the `tnsnames.ora` file.

If set to `on`, then the parameter `USE_DEDICATED_SERVER` automatically appends `(SERVER=dedicated)` to the connect data for a connect descriptor. This way connections from this client use a [dedicated server](glossary.md) process, even if [shared server](glossary.md) is configured.

Default

off

Values

- `on` to append `(SERVER=dedicated)`
- `off` to send requests to existing server processes

Example

```
USE_DEDICATED_SERVER=on
```

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/profile.htm#NETAG092) for complete configuration information

### WALLET\_LOCATION

Purpose

To specify the location of wallets. Wallets are certificates, keys, and trustpoints processed by SSL.

Syntax

The syntax depends on the wallet, as follows:

- Oracle wallets on the file system:
	```
	WALLET_LOCATION=
	  (SOURCE=
	    (METHOD=file)
	    (METHOD_DATA=
	       (DIRECTORY=directory)
	       [(PKCS11=TRUE/FALSE)]))
	```
- Microsoft certificate store:
	```
	WALLET_LOCATION=
	  (SOURCE=
	     (METHOD=mcs))
	```
- Oracle wallets in the Microsoft Windows registry:
	```
	WALLET_LOCATION=
	   (SOURCE=
	      (METHOD=reg)
	      (METHOD_DATA=
	         (KEY=registry_key)))
	```
- Entrust wallets:
	```
	WALLET_LOCATION=
	   (SOURCE=
	      (METHOD=entr)
	      (METHOD_DATA=
	         (PROFILE=file.epf)
	         (INIFILE=file.ini)))
	```

Additional Parameters

`WALLET_LOCATION` supports the following parameters:

- `SOURCE`: The type of storage for wallets and storage location.
- `METHOD`: The type of storage.
- `METHOD_DATA`: The storage location.
- `DIRECTORY`: The location of Oracle wallets on file system.
- `KEY`: The wallet type and location in the Microsoft Windows registry.
- `PROFILE`: The Entrust profile file (`.epf`).
- `INIFILE`: The Entrust initialization file (`.ini`).

Default

None

Usage Notes

- The key/value pair for Microsoft certificate store (MCS) omits the `METHOD_DATA` parameter because MCS does not use wallets. Instead, Oracle PKI (public key infrastructure) applications obtain certificates, trustpoints and private keys directly from the user's profile.
- If an Oracle wallet is stored in the Microsoft Windows registry and the wallet's key `(KEY)` is `SALESAPP`, then the storage location of the password-protected wallet is `HKEY_CURRENT_USER\SOFTWARE\ORACLE\WALLETS\SALESAPP\EWALLET.P12`. The storage location of the local auto-open wallet is `HKEY_CURRENT_USER\SOFTWARE\ORACLE\WALLETS\SALESAPP\CWALLET.SSO.`

Values

```
true | false
```

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

## ADR Diagnostic Parameters in sqlnet.ora

Beginning with Oracle Database 11g, Oracle Database includes an advanced fault diagnosability infrastructure for preventing, detecting, diagnosing, and resolving problems. The problems are critical errors such as those caused by database code bugs, metadata corruption, and customer data corruption.

When a critical error occurs, it is assigned an incident number, and diagnostic data for the error, such as traces and dumps, is immediately captured and tagged with the incident number. The data is then stored in the [Automatic Diagnostic Repository (ADR)](glossary.md), a file-based repository outside the database.

This section describes the parameters used when ADR is enabled. "Non-ADR Diagnostic Parameters in sqlnet.ora" describes the parameters used when ADR is disabled. Non-ADR parameters listed in the `sqlnet.ora` file are ignored when ADR is enabled. ADR is enabled by default.

This section lists the parameters used when ADR is enabled (when `DIAG_ADR_ENABLED` is set to `on`):

- ADR\_BASE
- DIAG\_ADR\_ENABLED
- TRACE\_LEVEL\_CLIENT
- TRACE\_LEVEL\_SERVER
- TRACE\_TIMESTAMP\_CLIENT
- TRACE\_TIMESTAMP\_SERVER

### ADR\_BASE

Purpose

To specify the base directory into which tracing and logging incidents are stored when ADR is enabled.

Default

The default on the server side is `ORACLE_BASE`, or `ORACLE_HOME/log`, if `ORACLE_BASE` is not defined.

Values

Any valid directory path to a directory with write permission.

Example

```
ADR_BASE=/oracle/network/trace
```

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci10new.htm#LNOCI1020) for the default on the client side

### DIAG\_ADR\_ENABLED

Purpose

To specify whether ADR tracing is enabled.

Usage

If the `DIAG_ADR_ENABLED` parameter is set to `OFF`, then non-ADR file tracing is used.

Default

on

Values

`on` | `off`

Example

```
DIAG_ADR_ENABLED=on
```

### TRACE\_LEVEL\_CLIENT

Purpose

To turn client tracing on at a specified level or to turn it off. This parameter is also applicable when non-ADR tracing is used.

Default

off or 0

Values

- `off` or `0` for no trace output
- `user` or `4` for user trace information
- `admin` or `10` for administration trace information
- `support` or `16` for Oracle Support Services trace information

Example

```
TRACE_LEVEL_CLIENT=user
```

### TRACE\_LEVEL\_SERVER

Purpose

To turn server tracing on at a specified level or to turn it off. This parameter is also applicable when non-ADR tracing is used.

Default

off or 0

Values

- `off` or `0` for no trace output
- `user` or `4` for user trace information
- `admin` or `10` for administration trace information
- `support` or `16` for Oracle Support Services trace information

Example

```
TRACE_LEVEL_SERVER=admin
```

### TRACE\_TIMESTAMP\_CLIENT

Purpose

To add a time stamp in the form of `dd-mon-yyyy hh:mi:ss:mil` to every trace event in the client trace file, which has a default name of `sqlnet.trc`. This parameter is also applicable when non-ADR tracing is used.

Default

on

Values

`on` or `true` | `off` or `false`

Example

```
TRACE_TIMESTAMP_CLIENT=true
```

### TRACE\_TIMESTAMP\_SERVER

Purpose

To add a time stamp in the form of `dd-mon-yyyy hh:mi:ss:mil` to every trace event in the database server trace file, which has a default name of `svr_` `pid``.trc`. This parameter is also applicable when non-ADR tracing is used.

Default

on

Values

`on` or `true` | `off` or `false`

Example

```
TRACE_TIMESTAMP_SERVER=true
```

## Non-ADR Diagnostic Parameters in sqlnet.ora

This section lists the parameters used when ADR is disabled.

Notes:

The default value of DIAG\_ADR\_ENABLED is `on`. Therefore, the `DIAG_ADR_ENABLED` parameter must explicitly be set to `off` in order for non-ADR tracing to be used.

- LOG\_DIRECTORY\_CLIENT
- LOG\_DIRECTORY\_SERVER
- LOG\_FILE\_CLIENT
- LOG\_FILE\_SERVER
- TRACE\_DIRECTORY\_CLIENT
- TRACE\_DIRECTORY\_SERVER
- TRACE\_FILE\_CLIENT
- TRACE\_FILE\_SERVER
- TRACE\_FILELEN\_CLIENT
- TRACE\_FILELEN\_SERVER
- TRACE\_FILENO\_CLIENT
- TRACE\_FILENO\_SERVER
- TRACE\_UNIQUE\_CLIENT

### LOG\_DIRECTORY\_CLIENT

Purpose

To specify the destination directory for the client log file. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/log
```

Values

Any valid directory path.

Example

```
LOG_DIRECTORY_CLIENT=/oracle/network/log
```

### LOG\_DIRECTORY\_SERVER

Purpose

To specify the destination directory for the database server log file. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/trace
```

Values

Any valid directory path to a directory with write permission.

Example

```
LOG_DIRECTORY_SERVER=/oracle/network/trace
```

### LOG\_FILE\_CLIENT

Purpose

To specify the name of the log file for the client. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/log/sqlnet.log
```

Values

The default value cannot be changed.

### LOG\_FILE\_SERVER

Purpose

To specify the name of the log file for the database server. Use this parameter when ADR is not enabled.

Default

```
sqlnet.log
```

Example

```
LOG_FILE_SERVER=svr.log
```

### TRACE\_DIRECTORY\_CLIENT

Purpose

To specify the destination directory for the client trace file. Use this parameter when ADR is not enabled.

Default

The current working directory.

Values

Any valid directory path to a directory with write permission.

Example

```
TRACE_DIRECTORY_CLIENT=/oracle/traces
```

### TRACE\_DIRECTORY\_SERVER

Purpose

To specify the destination directory for the database server trace file. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/trace
```

Values

Any valid directory path to a directory with write permission.

Example

```
TRACE_DIRECTORY_SERVER=/oracle/traces
```

### TRACE\_FILE\_CLIENT

Purpose

To specify the name of the client trace file. Use this parameter when ADR is not enabled.

Values

Any valid file name.

Default

```
ORACLE_HOME/network/trace/cli.trc
```

Example

```
TRACE_FILE_CLIENT=clientsqlnet.trc
```

### TRACE\_FILE\_SERVER

Purpose

To specify the name of the file to which the execution trace of the server program is written. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/trace/svr_pid.trc
```

Values

Any valid file name. The pid is appended to the name automatically.

Example

```
TRACE_FILE_SERVER=svrsqlnet.trc
```

### TRACE\_FILELEN\_CLIENT

Purpose

To specify the size of the client trace files in kilobytes (KB). When the size is met, the trace information is written to the next file. The number of files is specified with the TRACE\_FILENO\_CLIENT parameter. Use this parameter when ADR is not enabled.

Example

```
TRACE_FILELEN_CLIENT=100
```

### TRACE\_FILELEN\_SERVER

Purpose

To specify the size of the database server trace files in kilobytes (KB). When the size is met, the trace information is written to the next file. The number of files is specified with the TRACE\_FILENO\_SERVER parameter. Use this parameter when ADR is not enabled.

Example

```
TRACE_FILELEN_SERVER=100
```

### TRACE\_FILENO\_CLIENT

Purpose

To specify the number of trace files for client tracing. When this parameter is set with the TRACE\_FILELEN\_CLIENT parameter, trace files are used in a cyclical fashion. The first file is filled first, then the second file, and so on. When the last file has been filled, the first file is re-used, and so on.

The trace file names are distinguished from one another by their sequence number. For example, if the default trace file of `sqlnet.trc` is used, and this parameter is set to 3, then the trace files would be named `sqlnet1.trc`, `sqlnet2.trc` and `sqlnet3.trc`.

In addition, trace events in the trace files are preceded by the sequence number of the file. Use this parameter when ADR is not enabled.

Default

None

Example

```
TRACE_FILENO_CLIENT=3
```

### TRACE\_FILENO\_SERVER

Purpose

To specify the number of trace files for database server tracing. When this parameter is set with the TRACE\_FILELEN\_SERVER parameter, trace files are used in a cyclical fashion. The first file is filled first, then the second file, and so on. When the last file has been filled, the first file is re-used, and so on.

The trace file names are distinguished from one another by their sequence number. For example, if the default trace file of `svr_` `pid``.trc` is used, and this parameter is set to 3, then the trace files would be named `svr1_` `pid``.trc`, `svr2_` `pid``.trc` and `svr3_` `pid``.trc`.

In addition, trace events in the trace files are preceded by the sequence number of the file. Use this parameter when ADR is not enabled.

Default

None

Example

```
TRACE_FILENO_SERVER=3
```

### TRACE\_UNIQUE\_CLIENT

Purpose

To specify whether a unique trace file is created for each client trace session. When the value is set to `on`, a process identifier is appended to the name of each trace file, enabling several files to coexist. For example, trace files named `sqlnet` `pid``.trc` are created if default trace file name `sqlnet.trc` is used. When the value is set to `off`, data from a new client trace session overwrites the existing file. Use this parameter when ADR is not enabled.

Default

on

Values

`on` or `off`

Example

```
TRACE_UNIQUE_CLIENT=on
```
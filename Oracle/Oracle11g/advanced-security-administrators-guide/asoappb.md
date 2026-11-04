---
title: Authentication Parameters
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoappb.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## B Authentication Parameters

This appendix illustrates some sample configuration files with the profile file (`sqlnet.ora`) and the database initialization file authentication parameters, when using Kerberos, RADIUS, or SSL authentication.

This appendix contains the following topics:

## B.1 Parameters for Clients and Servers using Kerberos Authentication

Following is a list of parameters to insert into the configuration files for clients and servers using Kerberos.

Table B-1 Kerberos Authentication Parameters

| File Name | Configuration Parameters |
| --- | --- |
| `sqlnet.ora` | ``` SQLNET.AUTHENTICATION_SERVICES=(KERBEROS5)         SQLNET.AUTHENTICATION_KERBEROS5_SERVICE=oracle      SQLNET.KERBEROS5_CC_NAME=/usr/tmp/DCE-CC    SQLNET.KERBEROS5_CLOCKSKEW=1200    SQLNET.KERBEROS5_CONF=/krb5/krb.conf       SQLNET.KERBEROS5_CONF_MIT=(FALSE) SQLNET.KERBEROS5_REALMS=/krb5/krb.realms   SQLNET.KERBEROS5_KEYTAB=/krb5/v5sLrvtab SQLNET.FALLBACK_AUTHENTICATION=FALSE ``` |
| `initialization parameter file` | ``` OS_AUTHENT_PREFIX="" ``` |

## B.2 Parameters for Clients and Servers using RADIUS Authentication

The following sections describe the parameters for RADIUS authentication

- sqlnet.ora File Parameters
- Minimum RADIUS Parameters
- Initialization File Parameters

### B.2.1 sqlnet.ora File Parameters

The following sections describe the `sqlnet.ora` parameters that are used to specify RADIUS authentication.

#### B.2.1.1 SQLNET.AUTHENTICATION\_SERVICES Parameter

This parameter configures the client or the server to use the RADIUS adapter. Table B-2 describes this parameter's attributes.

Table B-2 SQLNET.AUTHENTICATION\_SERVICES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.AUTHENTICATION_SERVICES=(radius)` |
| Default setting | None |

#### B.2.1.2 SQLNET.RADIUS\_AUTHENTICATION Parameter

This parameter sets the location of the primary RADIUS server, either host name or dotted decimal format. If the RADIUS server is on a different computer from the Oracle server, you must specify either the host name or the IP address of that computer. Table B-3 describes this parameter's attributes.

Table B-3 SQLNET.RADIUS\_AUTHENTICATION Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION=` `RADIUS_server_IP_address` |
| Default setting | `localhost` |

#### B.2.1.3 SQLNET.RADIUS\_AUTHENTICATION\_PORT Parameter

This parameter sets the listening port of the primary RADIUS server. Table B-4 describes this parameter's attributes.

Table B-4 SQLNET.RADIUS\_AUTHENTICATION\_PORT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_PORT=` `port_number` |
| Default setting | `1645` |

#### B.2.1.4 SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT Parameter

This parameter sets the time to wait for response. Table B-5 describes this parameter's attributes.

Table B-5 SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_TIMEOUT=` `time_in_seconds` |
| Default setting | `5` |

#### B.2.1.5 SQLNET.RADIUS\_AUTHENTICATION\_RETRIES Parameter

This parameter sets the number of times to resend authentication information. Table B-6 describes this parameter's attributes.

Table B-6 SQLNET.RADIUS\_AUTHENTICATION\_RETRIES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_RETRIES=` `n_times_to_resend` |
| Default setting | `3` |

#### B.2.1.6 SQLNET.RADIUS\_SEND\_ACCOUNTING Parameter

This parameter turns accounting on and off. If you enable accounting, packets will be sent to the active RADIUS server at the listening port plus one. By default, packets are sent to port 1646. You need to turn this feature on only when your RADIUS server supports accounting and you want to keep track of the number of times the user is logging on to the system. Table B-7 describes this parameter's attributes.

Table B-7 SQLNET.RADIUS\_SEND\_ACCOUNTING Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_SEND_ACCOUNTING=` `on` |
| Default setting | `off` |

#### B.2.1.7 SQLNET.RADIUS\_SECRET Parameter

This parameter specifies the file name and location of the RADIUS secret key. Table B-8 describes this parameter's attributes.

Table B-8 SQLNET.RADIUS\_SECRET Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_SECRET=` `path_to_RADIUS_secret_key` |
| Default setting | `$ORACLE_HOME/network/security/radius.key` |

#### B.2.1.8 SQLNET.RADIUS\_ALTERNATE Parameter

This parameter sets the location of an alternate RADIUS server to be used in case the primary server becomes unavailable for fault tolerance. Table B-9 describes this parameter's attributes.

Table B-9 SQLNET.RADIUS\_ALTERNATE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE=` `alternate_RADIUS_server_hostname_or_IP_address` |
| Default setting | `off` |

#### B.2.1.9 SQLNET.RADIUS\_ALTERNATE\_PORT Parameter

This parameter sets the listening port for the alternate RADIUS server. Table B-10 describes this parameter's attributes.

Table B-10 SQLNET.RADIUS\_ALTERNATE\_PORT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_PORT=` `alternate_RADIUS_server_listening_port_number` |
| Default setting | `1645` |

#### B.2.1.10 SQLNET.RADIUS\_ALTERNATE\_TIMEOUT Parameter

This parameter sets the time to wait for response for the alternate RADIUS server. Table B-11 describes this parameter's attributes.

Table B-11 SQLNET.RADIUS\_ALTERNATE\_TIMEOUT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_TIMEOUT=` `time_in_seconds` |
| Default setting | `5` |

#### B.2.1.11 SQLNET.RADIUS\_ALTERNATE\_RETRIES Parameter

This parameter sets the number of times that the alternate RADIUS server resends messages. Table B-12 describes this parameter's attributes.

Table B-12 SQLNET.RADIUS\_ALTERNATE\_RETRIES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_RETRIES=` `n_times_to_resend` |
| Default setting | `3` |

#### B.2.1.12 SQLNET.RADIUS\_CHALLENGE\_RESPONSE Parameter

This parameter turns on or turns off the challenge-response or asynchronous mode support. Table B-13 describes this parameter's attributes.

Table B-13 SQLNET.RADIUS\_CHALLENGE\_RESPONSE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CHALLENGE_RESPONSE=` `on` |
| Default setting | `off` |

#### B.2.1.13 SQLNET.RADIUS\_CHALLENGE\_KEYWORD Parameter

This parameter sets the keyword to request a challenge from the RADIUS server. User types no password on the client. Table B-14 describes this parameter's attributes.

Table B-14 SQLNET.RADIUS\_CHALLENGE\_KEYWORD Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CHALLENGE_KEYWORD=` `keyword` |
| Default setting | `challenge` |

#### B.2.1.14 SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE Parameter

This parameter sets the name of the Java class that contains the graphical user interface when RADIUS is in the challenge-response (asynchronous) mode. Table B-15 describes this parameter's attributes.

Table B-15 SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_INTERFACE=` `Java_class_name` |
| Default setting | `DefaultRadiusInterface (oracle/net/radius/DefaultRadiusInterface)` |

#### B.2.1.15 SQLNET.RADIUS\_CLASSPATH Parameter

If you decide to use the challenge-response authentication mode, RADIUS presents the user with a Java-based graphical interface requesting first a password, then additional information, for example, a dynamic password that the user obtains from a token card. Add the `SQLNET.RADIUS_CLASSPATH` parameter in the `sqlnet.ora` file to set the path for the Java classes for that graphical interface, and to set the path to the JDK Java libraries. Table B-16 describes this parameter's attributes.

Table B-16 SQLNET.RADIUS\_CLASSPATH Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CLASSPATH=` `path_to_GUI_Java_classes` |
| Default setting | `$ORACLE_HOME/jlib/netradius.jar:$ORACLE_HOME/JRE/lib/sparc/native_threads` |

### B.2.2 Minimum RADIUS Parameters

```
sqlnet.authentication_services = (radius)
sqlnet.radius.authentication = IP-address-of-RADIUS-server
```

### B.2.3 Initialization File Parameters

```
OS_AUTHENT_PREFIX=""
```

## B.3 Parameters for Clients and Servers Using Secure Sockets Layer

There are two ways to configure a parameter:

- Static: The name of the parameter that exists in the `sqlnet.ora` file. Parameters like `SSL_CIPHER_SUITES` and `SSL_VERSION` can also be configured using the `listener.ora` file.
- Dynamic: The name of the parameter used in the security subsection of the Oracle Net address.

### B.3.1 Secure Sockets Layer Authentication Parameters

This section describes the static and dynamic parameters for configuring SSL on the server.

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | SQLNET.AUTHENTICATION\_SERVICES |
| Parameter Name (dynamic) | AUTHENTICATION |
| Parameter Type | String LIST |
| Parameter Class | Static |
| Permitted Values | Add TCPS to the list of available authentication services. |
| Default Value | No default value. |
| Description | To control which authentication services a user wants to use.  Note: The dynamic version supports only the setting of one type. |
| Existing/New Parameter | Existing |
| Syntax (static) | SQLNET.AUTHENTICATION\_SERVICES = (TCPS, selected\_method\_1, selected\_method\_2) |
| Example (static) | SQLNET.AUTHENTICATION\_SERVICES = (TCPS, radius) |
| Syntax (dynamic) | AUTHENTICATION = string |
| Example (dynamic) | AUTHENTICATION = (TCPS) |

### B.3.2 Cipher Suite Parameters

This section describes the static and dynamic parameters for configuring cipher suites.

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | SSL\_CIPHER\_SUITES |
| Parameter Name (dynamic) | SSL\_CIPHER\_SUITES |
| Parameter Type | String LIST |
| Parameter Class | Static |
| Permitted Values | Any known SSL cipher suite |
| Default Value | No default |
| Description | Controls the combination of encryption and data integrity used by SSL. |
| Existing/New Parameter | Existing |
| Syntax (static) | SSL\_CIPHER\_SUITES=(SSL\_cipher\_suite1\[, SSL\_cipher\_suite2,... SSL\_cipher\_suiteN\]) |
| Example (static) | SSL\_CIPHER\_SUITES=(SSL\_DH\_DSS\_WITH\_DES\_CBC\_SHA) |
| Syntax (dynamic) | SSL\_CIPHER\_SUITES=(SSL\_cipher\_suite1  \[, SSL\_cipher\_suite2,...SSL\_cipher\_suiteN\]) |
| Example (dynamic) | SSL\_CIPHER\_SUITES=(SSL\_DH\_DSS\_WITH\_DES\_CBC\_SHA) |

#### B.3.2.1 Supported SSL Cipher Suites

Oracle Advanced Security supports the following cipher suites:

- SSL\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- SSL\_DH\_anon\_WITH\_3DES\_EDE\_CBC\_SHA
- SSL\_RSA\_WITH\_AES\_128\_CBC\_SHA
- SSL\_RSA\_WITH\_AES\_256\_CBC\_SHA

Note that the cipher suites that use Advanced Encryption Standard (`AES`) work with Transport Layer Security (TLS 1.0) only.

### B.3.3 Secure Sockets Layer Version Parameters

This section describes the static and dynamic parameters for configuring the version of SSL to be used.

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | SSL\_VERSION |
| Parameter Name (dynamic) | SSL\_VERSION |
| Parameter Type | string |
| Parameter Class | Static |
| Permitted Values | Any version that is valid to SSL. Values are as follows:  `undetermined \| 3.0 \| 1.0 \| 1.1 \| 1.2`  If you want to specify one version or another version, then use "or". The following values are permitted:  `1.0 or 3.0 \| 1.2 or 3.0 \| 1.1 or 1.0 \| 1.2 or 1.0 \| 1.2 or 1.1 \| 1.1 or 1.0 or 3.0 \| 1.2 or 1.0 or 3.0 \| 1.2 or 1.1 or 1.0 \| 1.2 or 1.1 or 3.0 \| 1.2 or 1.1 or 1.0 or 3.0` |
| Default Value | "0" |
| Description | To force the version of the SSL connection. |
| Existing/New Parameter | New |
| Syntax (static) | SSL\_VERSION=version |
| Example (static) | SSL\_VERSION=1.0 or 3.0 |
| Syntax (dynamic) | SSL\_VERSION=version |
| Example (dynamic) | SSL\_VERSION=3.0 |

### B.3.4 Secure Sockets Layer Client Authentication Parameters

This section describes the static and dynamic parameters for configuring SSL on the client.

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | SSL\_CLIENT\_AUTHENTICATION |
| Parameter Name (dynamic) | SSL\_CLIENT\_AUTHENTICATION |
| Parameter Type | Boolean |
| Parameter Class | Static |
| Permitted Values | TRUE/FALSE |
| Default Value | TRUE |
| Description | To control whether a client, in addition to the server, is authenticated using SSL. |
| Existing/New Parameter | New |
| Syntax (static) | SSL\_CLIENT\_AUTHENTICATION={TRUE \| FALSE} |
| Example (static) | SSL\_CLIENT\_AUTHENTICATION=FALSE |
| Syntax (dynamic) | SSL\_CLIENT\_AUTHENTICATION={TRUE \| FALSE} |
| Example (dynamic) | SSL\_CLIENT\_AUTHENTICATION=FALSE |

#### B.3.4.1 SSL X.509 Server Match Parameters

This section describes the parameters that are used to validate the identity of a server that the client connects to.

##### B.3.4.1.1 SSL\_SERVER\_DN\_MATCH

| Attribute | Description |
| --- | --- |
| Parameter Name | SSL\_SERVER\_DN\_MATCH |
| Where stored | `sqlnet.ora` |
| Purpose | Use this parameter to force the server's [distinguished name (DN)](asogls.md) to match its service name. If you force the match verifications, SSL ensures that the certificate is from the server. If you choose not to enforce the match verification, SSL performs the check but permits the connection, regardless of whether there is a match. Not forcing the match lets the server potentially fake its identity. |
| Values | `yes\|on\|true`. Specify to enforce a match. If the DN matches the service name, the connection succeeds; otherwise, the connection fails.  `no\|off\|false`. Specify to not enforce a match. If the DN does not match the service name, the connection is successful, but an error is logged to the `sqlnet.log` file. |
| Default | Oracle8i, or later:.FALSE. SSL client (always) checks server DN. If it does not match the service name, the connection succeeds but an error is logged to `sqlnet.log` file. |
| Usage Notes | Additionally configure the `tnsnames.ora` parameter `SSL_SERVER_CERT_DN` to enable server DN matching. |

##### B.3.4.1.2 SSL\_SERVER\_CERT\_DN

| Attribute | Description |
| --- | --- |
| Parameter Name | SSL\_SERVER\_CERT\_DN |
| Where stored | `tnsnames.ora`. It can be stored on the client, for every server it connects to, or it can be stored in the LDAP directory, for every server it connects to, updated centrally. |
| Purpose | This parameter specifies the [distinguished name (DN)](asogls.md) of the server. The client uses this information to obtain the list of DNs it expects for each of the servers to force the server's DN to match its service name. |
| Values | Set equal to [distinguished name (DN)](asogls.md) of the server. |
| Default | n/a |
| Usage Notes | Additionally configure the `sqlnet.ora` parameter `SSL_SERVER_DN_MATCH` to enable server DN matching. |
| Example | `dbalias=(description=address_list=(address=(protocol=tcps)(host=hostname)(port=portnum)))(connect_data=(sid=Finance))(security=(SSL_SERVER_CERT_DN="CN=Finance,CN=OracleContext,C=US,O=Acme"))` |

### B.3.5 Wallet Location

For any application that must access a wallet for loading the security credentials into the process space, you must specify the wallet location parameters defined by Table B-17 in each of the following configuration files:

- `sqlnet.ora`
- `listener.ora`

Table B-17 Wallet Location Parameters

| Static Configuration | Dynamic Configuration |
| --- | --- |
| `WALLET_LOCATION =`  `(SOURCE=`  `(METHOD=File)`  `(METHOD_DATA=`  `(DIRECTORY=your wallet location)`  `)`  `)` | `MY_WALLET_DIRECTORY`  `= your_wallet_dir` |

The default wallet location is the `ORACLE_HOME` directory.
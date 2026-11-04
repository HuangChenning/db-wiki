---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/kerberos-ssl-and-radius-authentication-parameters.html
tags:
  - oracle
  - 21c
  - security-guide
---

**Parent topic:** [Appendixes](part_7.md)

### C.1 Parameters for Clients and Servers Using Kerberos Authentication

Oracle Database provides client and server parameters for using Kerberos authentication.

Table C-1 lists parameters to insert into the configuration files for clients and servers using Kerberos.

Table C-1 Kerberos Authentication Parameters

| File Name | Configuration Parameters |
| --- | --- |
| `sqlnet.ora` | `SQLNET.AUTHENTICATION_SERVICES=(KERBEROS5)`: Set on both client and server.  ` SQLNET.AUTHENTICATION_KERBEROS5_SERVICE=oracle`: Set on both client and server.  `SQLNET.KERBEROS5_CC_NAME=/usr/tmp/DCE-CC`: Not normally required on the server. If your client is on Microsoft Windows and is part of a domain, you may want to consider using the in-memory ticket cache and set this parameter to `OSMSFT://` or `MSLSA:`.  `SQLNET.KERBEROS5_CLOCKSKEW=1200`: Set on both client and server.  `SQLNET.KERBEROS5_CONF=/krb5/krb.conf`: Set on both client and server. (Normally, this path in the client is different from the path in the server.)  ` SQLNET.KERBEROS5_CONF_MIT=(TRUE)`: Set this to `TRUE` on both the client and the server.  `SQLNET.KERBEROS5_REALMS=/krb5/krb.realms`: This setting is not usually required for the client or the server.  `SQLNET.KERBEROS5_KEYTAB=/krb5/v5srvtab`: Only set this parameter on the server, not the client.  `SQLNET.FALLBACK_AUTHENTICATION=FALSE`: Set on both client and server. |
| `initialization parameter file` | `OS_AUTHENT_PREFIX=""`: Set this parameter only on the server, not the client. |

### C.2 Parameters for Clients and Servers Using Transport Layer Security

Oracle provides parameters to control Transport Layer Security authentication.

- Ways to Configure a Parameter for Transport Layer Security  
	There are two ways to configure a parameter for Transport Layer Security (TLS).
- Transport Layer Security Authentication Parameters for Clients and Servers  
	Oracle provides both static and dynamic Transport Layer Security (TLS) authentication parameters.
- Cipher Suite Parameters for Transport Layer Security  
	You can configure cipher suite parameters for Transport Layer Security (TLS).
- Supported Transport Layer Security Cipher Suites  
	Oracle Database supports a large number of cipher suites for Transport Layer Security (TLS).
- Transport Layer Security Version Parameters  
	You can set a range of Transport Layer Security (TLS) parameters to configure the version of TLS to use.
- Transport Layer Security Client Authentication Parameters  
	You can configure static and dynamic parameters for Secure Sockes Layer (TLS) on the client.
- Transport Layer Security X.509 Server Match Parameters  
	The `SSL_SERVER_DN_MATCH` and `SSL_SERVER_CERT_DN` parameters validate the identity of the server to which a client connects.
- Oracle Wallet Location  
	You must specify wallet location parameters for applications that must access an Oracle wallet for loading the security credentials into the process space.

**Parent topic:** Kerberos, TLS, and RADIUS Authentication Parameters

#### C.2.1 Ways to Configure a Parameter for Transport Layer Security

There are two ways to configure a parameter for Transport Layer Security (TLS).

- Static: The name of the parameter that exists in the `sqlnet.ora` file. Parameters like `SSL_CIPHER_SUITES` and `SSL_VERSION` can also be configured using the `listener.ora` file.
- Dynamic: The name of the parameter used in the security subsection of the Oracle Net address.

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

#### C.2.2 Transport Layer Security Authentication Parameters for Clients and Servers

Oracle provides both static and dynamic Transport Layer Security (TLS) authentication parameters.

Table C-2 describes the static and dynamic parameters for configuring TLS on the server.

Table C-2 TLS Authentication Parameters for Clients and Servers

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | `SQLNET.AUTHENTICATION_SERVICES` |
| Parameter Name (dynamic) | `AUTHENTICATION` |
| Parameter Type | String `LIST` |
| Parameter Class | Static |
| Permitted Values | Add TCPS to the list of available authentication services. |
| Default Value | No default value. |
| Description | To control which authentication services a user wants to use.  Note: The dynamic version supports only the setting of one type. |
| Existing/New Parameter | Existing |
| Syntax (static) | `SQLNET.AUTHENTICATION_SERVICES = (TCPS, ``selected_method_1``,` `selected_method_2``)` |
| Example (static) | `SQLNET.AUTHENTICATION_SERVICES = (TCPS, radius)` |
| Syntax (dynamic) | `AUTHENTICATION = ` `string` |
| Example (dynamic) | `AUTHENTICATION = (TCPS)` |

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

#### C.2.3 Cipher Suite Parameters for Transport Layer Security

You can configure cipher suite parameters for Transport Layer Security (TLS).

Table C-3 describes the static and dynamic parameters for configuring cipher suites.

Table C-3 Cipher Suite Parameters for Transport Layer Security

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | `SSL_CIPHER_SUITES` |
| Parameter Name (dynamic) | `SSL_CIPHER_SUITES` |
| Parameter Type | String `LIST` |
| Parameter Class | Static |
| Permitted Values | Any known TLS cipher suite |
| Default Value | No default |
| Description | Controls the combination of encryption and data integrity used by TLS. |
| Existing/New Parameter | Existing |
| Syntax (static) | `SSL_CIPHER_SUITES=(``SSL_cipher_suite1` `[,` `SSL_cipher_suite2``,` `...`` SSL_cipher_suiteN``])` |
| Example (static) | `SSL_CIPHER_SUITES=(SSL_DH_DSS_WITH_DES_CBC_SHA)` |
| Syntax (dynamic) | `SSL_CIPHER_SUITES=(``SSL_cipher_suite1`  `[, ``SSL_cipher_suite2`, `...``SSL_cipher_suiteN``])` |
| Example (dynamic) | `SSL_CIPHER_SUITES=(SSL_DH_DSS_WITH_DES_CBC_SHA)` |

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

#### C.2.4 Supported Transport Layer Security Cipher Suites

Oracle Database supports a large number of cipher suites for Transport Layer Security (TLS).

The cipher suites are as follows:

- `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`
- `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`
- `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`
- `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`
- `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`

#### C.2.5 Transport Layer Security Version Parameters

You can set a range of Transport Layer Security (TLS) parameters to configure the version of TLS to use.

Table C-4 describes the `SSL_VERSION` static and dynamic parameters for configuring the version of TLS to be used.

Table C-4 Transport Layer Security Version Parameters

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | `SSL_VERSION` |
| Parameter Name (dynamic) | `SSL_VERSION` |
| Parameter Type | string |
| Parameter Class | Static |
| Permitted Values | Any version which is valid to TLS. Values are as follows:  `undetermined \| 1.0 \| 1.1 \| 1.2 \| 3.0`  If you want to specify one version or another version, then use "or". The following values are permitted:  ``` 1.0 or 3.0 \| 1.2 or 3.0 \| 1.1 or 1.0 \| 1.2 or 1.0 \| 1.2 or 1.1 \| 1.1 or 1.0 or 3.0 \|  1.2 or 1.0 or 3.0 \| 1.2 or 1.1 or 1.0 \| 1.2 or 1.1 or 3.0 \|1.2 or 1.1 or 1.0 or 3 ``` |
| Default Value | `1.2`, `1.1`, or `1.0`  If you want to use a specific value (such as `1.2`), then you must set it explicitly. |
| Description | To force the version of the TLS connection. |
| Existing/New Parameter | New |
| Syntax (static) | `SSL_VERSION=` `version` |
| Example (static) | `SSL_VERSION=1.1` |
| Syntax (dynamic) | `SSL_VERSION=` `version` |
| Example (dynamic) | `SSL_VERSION=1.1 or 1.2` |

Note:

The `ADD_SSLv3_IMPLICITLY` initialization parameter has no effect on the `SSL_VERSION` parameter.

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

#### C.2.6 Transport Layer Security Client Authentication Parameters

You can configure static and dynamic parameters for Secure Sockes Layer (TLS) on the client.

Table C-5 describes the `SSL_CLIENT_AUTHENTICATION` parameters.

Table C-5 Transport Layer Security Client Authentication Parameters

| Attribute | Description |
| --- | --- |
| Parameter Name (static) | `SSL_CLIENT_AUTHENTICATION` |
| Parameter Name (dynamic) | `SSL_CLIENT_AUTHENTICATION` |
| Parameter Type | Boolean |
| Parameter Class | Static |
| Permitted Values | `TRUE` or `FALSE` |
| Default Value | `TRUE` |
| Description | To control whether a client, in addition to the server, is authenticated using TLS. |
| Existing/New Parameter | New |
| Syntax (static) | `SSL_CLIENT_AUTHENTICATION={` `TRUE` `\|` `FALSE}` |
| Example (static) | `SSL_CLIENT_AUTHENTICATION=FALSE` |
| Syntax (dynamic) | `SSL_CLIENT_AUTHENTICATION={` `TRUE` `\|` `FALSE}` |
| Example (dynamic) | `SSL_CLIENT_AUTHENTICATION=FALSE` |

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

#### C.2.7 Transport Layer Security X.509 Server Match Parameters

The `SSL_SERVER_DN_MATCH` and `SSL_SERVER_CERT_DN` parameters validate the identity of the server to which a client connects.

- SSL\_SERVER\_DN\_MATCH  
	The `SSL_SERVER_DN_MATCH` parameter forces the server’s distinguished name (DN) to match the name of the service.
- SSL\_SERVER\_CERT\_DN  
	The `SSL_SERVER_CERT_DN` specifies the distinguished name (DN) of a server.

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

##### C.2.7.1 SSL\_SERVER\_DN\_MATCH

The `SSL_SERVER_DN_MATCH` parameter forces the server’s distinguished name (DN) to match the name of the service.

Table C-6 describes the `SSL_SERVER_DN_MATCH` parameter.

Table C-6 SSL\_SERVER\_DN\_MATCH Parameter

| Attribute | Description |
| --- | --- |
| Parameter Name | `SSL_SERVER_DN_MATCH` |
| Where Stored | `sqlnet.ora` |
| Purpose | Use this parameter to force the server's distinguished name (DN) to match its service name. If you force the match verifications, TLS ensures that the certificate is from the server. If you choose not to enforce the match verification, TLS performs the check but permits the connection, regardless of whether there is a match. Not forcing the match lets the server potentially fake its identity. |
| Values | `yes\|on\|true`. Specify to enforce a match. If the DN matches the service name, the connection succeeds; otherwise, the connection fails.  `no\|off\|false`. Specify to not enforce a match. If the DN does not match the service name, the connection is successful, but an error is logged to the `sqlnet.log` file. |
| Default | Oracle8i, or later: `false`. TLS client (always) checks server DN. If it does not match the service name, the connection succeeds but an error is logged to `sqlnet.log` file. |
| Usage Notes | Additionally configure the `tnsnames.ora` parameter `SSL_SERVER_CERT_DN` to enable server DN matching. |

**Parent topic:** Transport Layer Security X.509 Server Match Parameters

##### C.2.7.2 SSL\_SERVER\_CERT\_DN

The `SSL_SERVER_CERT_DN` specifies the distinguished name (DN) of a server.

Table C-7 describes the `SSL_SERVER_CERT_DN` parameter.

Table C-7 SSL\_SERVER\_CERT\_DN Parameter

| Attribute | Description |
| --- | --- |
| Parameter Name | `SSL_SERVER_CERT_DN` |
| Where stored | `tnsnames.ora`. It can be stored on the client, for every server it connects to, or it can be stored in the LDAP directory, for every server it connects to, updated centrally. |
| Purpose | This parameter specifies the distinguished name (DN) of the server. The client uses this information to obtain the list of DNs it expects for each of the servers to force the server's DN to match its service name. |
| Values | Set equal to distinguished name (DN) of the server. |
| Default | N/A |
| Usage Notes | Additionally configure the `sqlnet.ora` parameter `SSL_SERVER_DN_MATCH` to enable server DN matching. |
| Example | `dbalias=(description=address_list=(address=(protocol=tcps)(host=hostname)(port=portnum)))(connect_data=(sid=Finance))(security=(SSL_SERVER_CERT_DN="CN=Finance,CN=OracleContext,C=US,O=Acme"))` |

**Parent topic:** Transport Layer Security X.509 Server Match Parameters

#### C.2.8 Oracle Wallet Location

You must specify wallet location parameters for applications that must access an Oracle wallet for loading the security credentials into the process space.

Table C-8 lists the configuration files in which you must specify the wallet locations.

- `sqlnet.ora`
- `listener.ora`

Table C-8 Wallet Location Parameters

| Static Configuration | Dynamic Configuration |
| --- | --- |
| ``` WALLET_LOCATION = (SOURCE=   (METHOD=File)   (METHOD_DATA=      (DIRECTORY=your_wallet_dir)       ) ```  ) | ``` MY_WALLET_DIRECTORY = your_wallet_dir ``` |

The default wallet location is the `ORACLE_HOME` directory.

**Parent topic:** Parameters for Clients and Servers Using Transport Layer Security

### C.3 Parameters for Clients and Servers Using RADIUS Authentication

Oracle provides parameters for RADIUS authentication.

- sqlnet.ora File Parameters  
	You can include RADIUS-specific parameters in the `sqlnet.ora` file.
- Minimum RADIUS Parameters  
	At minimum, you should use the `SQLNET.AUTHENTICATION_SERVICES` and `SQLNET.RADIUS.AUTHENTICATION` parameters.
- Initialization File Parameter for RADIUS  
	For RADIUS, you should set the `OS_AUTHENT_PREFIX` initialization parameter.

**Parent topic:** Kerberos, TLS, and RADIUS Authentication Parameters

#### C.3.1 sqlnet.ora File Parameters

You can include RADIUS-specific parameters in the `sqlnet.ora` file.

- SQLNET.AUTHENTICATION\_SERVICES  
	The `SQLNET.AUTHENTICATION_SERVICES` parameter configures the client or the server to use the RADIUS adapter.
- SQLNET.RADIUS\_ALTERNATE  
	The `SQLNET.RADIUS_ALTERNATE` parameter sets the location of an alternate RADIUS server to be used if the primary server is unavailable for fault tolerance.
- SQLNET.RADIUS\_ALTERNATE\_PORT  
	The `SQLNET.RADIUS_ALTERNATE_PORT` parameter sets the listening port for the alternate RADIUS server.
- SQLNET.RADIUS\_ALTERNATE\_TIMEOUT  
	The `SQLNET.RADIUS_ALTERNATE_TIMEOUT` parameter sets the time for an alternate RADIUS server to wait for a response.
- SQLNET.RADIUS\_ALTERNATE\_RETRIES  
	The `SQLNET.RADIUS_ALTERNATE_RETRIES` parameter sets the number of times that the alternate RADIUS server resends messages.
- SQLNET.RADIUS\_AUTHENTICATION  
	The `SQLNET.RADIUS_AUTHENTICATION` parameter sets the location of the primary RADIUS server, either host name or dotted decimal format.
- SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE  
	The `SQLNET.RADIUS_AUTHENTICATION_INTERFACE` parameter sets the name of the Java class that contains the GUI when RADIUS is in challenge-response (asynchronous) mode.
- SQLNET.RADIUS\_AUTHENTICATION\_PORT  
	The `SQLNET.RADIUS_AUTHENTICATION_PORT` parameter sets the listening port of the primary RADIUS server.
- SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT  
	The `SQLNET.RADIUS_AUTHENTICATION_TIMEOUT` parameter sets the time to wait for response.
- SQLNET.RADIUS\_AUTHENTICATION\_RETRIES  
	The `SQLNET.RADIUS_AUTHENTICATION_RETRIES` parameter sets the number of times to resend authentication information.
- SQLNET.RADIUS\_CHALLENGE\_RESPONSE  
	The `SQLNET.RADIUS_CHALLENGE_RESPONSE` parameter turns on or turns off the challenge-response or asynchronous mode support.
- SQLNET.RADIUS\_CHALLENGE\_KEYWORD  
	The `SQLNET.RADIUS_CHALLENGE_KEYWORD` parameter sets the keyword to request a challenge from the RADIUS server.
- SQLNET.RADIUS\_CLASSPATH  
	The `SQLNET.RADIUS_CLASSPATH` parameter sets the path for Java classes and the JDK Java libraries.
- SQLNET.RADIUS\_SECRET  
	The `SQLNET.RADIUS_SECRET` parameter specifies the file name and location of the RADIUS secret key.
- SQLNET.RADIUS\_SEND\_ACCOUNTING  
	The `SQLNET.RADIUS_SEND_ACCOUNTING` parameter turns accounting on or off.

**Parent topic:** Parameters for Clients and Servers Using RADIUS Authentication

##### C.3.1.1 SQLNET.AUTHENTICATION\_SERVICES

The `SQLNET.AUTHENTICATION_SERVICES` parameter configures the client or the server to use the RADIUS adapter.

Table C-9 describes the `SQLNET.AUTHENTICATION_SERVICES` parameter attributes.

Table C-9 SQLNET.AUTHENTICATION\_SERVICES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.AUTHENTICATION_SERVICES=(radius)` |
| Default setting | None |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.2 SQLNET.RADIUS\_ALTERNATE

The `SQLNET.RADIUS_ALTERNATE` parameter sets the location of an alternate RADIUS server to be used if the primary server is unavailable for fault tolerance.

Table C-10 describes the `SQLNET.RADIUS_ALTERNATE` parameter attributes.

Table C-10 SQLNET.RADIUS\_ALTERNATE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE=` `alternate_RADIUS_server_hostname_or_IP_address` |
| Default setting | `off` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.3 SQLNET.RADIUS\_ALTERNATE\_PORT

The `SQLNET.RADIUS_ALTERNATE_PORT` parameter sets the listening port for the alternate RADIUS server.

Table C-11 describes the `SQLNET.RADIUS_ALTERNATE_PORT` parameter attributes.

Table C-11 SQLNET.RADIUS\_ALTERNATE\_PORT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_PORT=` `alternate_RADIUS_server_listening_port_number` |
| Default setting | `1645` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.4 SQLNET.RADIUS\_ALTERNATE\_TIMEOUT

The `SQLNET.RADIUS_ALTERNATE_TIMEOUT` parameter sets the time for an alternate RADIUS server to wait for a response.

Table C-12 describes the `SQLNET.RADIUS_ALTERNATE_TIMEOUT` parameter attributes.

Table C-12 SQLNET.RADIUS\_ALTERNATE\_TIMEOUT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_TIMEOUT=` `time_in_seconds` |
| Default setting | `5` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.5 SQLNET.RADIUS\_ALTERNATE\_RETRIES

The `SQLNET.RADIUS_ALTERNATE_RETRIES` parameter sets the number of times that the alternate RADIUS server resends messages.

Table C-13 describes the `SQLNET.RADIUS_ALTERNATE_RETRIES` parameter attributes.

Table C-13 SQLNET.RADIUS\_ALTERNATE\_RETRIES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_ALTERNATE_RETRIES=` `n_times_to_resend` |
| Default setting | `3` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.6 SQLNET.RADIUS\_AUTHENTICATION

The `SQLNET.RADIUS_AUTHENTICATION` parameter sets the location of the primary RADIUS server, either host name or dotted decimal format.

If the RADIUS server is on a different computer from the Oracle server, you must specify either the host name or the IP address of that computer.

Table C-14 describes the `SQLNET.RADIUS_AUTHENTICATION` parameter attributes.

Table C-14 SQLNET.RADIUS\_AUTHENTICATION Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION=` `RADIUS_server_IP_address` |
| Default setting | `localhost` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.7 SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE

The `SQLNET.RADIUS_AUTHENTICATION_INTERFACE` parameter sets the name of the Java class that contains the GUI when RADIUS is in challenge-response (asynchronous) mode.

Table C-15 describes the `SQLNET.RADIUS_AUTHENTICATION_INTERFACE` parameter attributes.

Table C-15 SQLNET.RADIUS\_AUTHENTICATION\_INTERFACE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_INTERFACE=` `Java_class_name` |
| Default setting | `DefaultRadiusInterface (oracle/net/radius/DefaultRadiusInterface)` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.8 SQLNET.RADIUS\_AUTHENTICATION\_PORT

The `SQLNET.RADIUS_AUTHENTICATION_PORT` parameter sets the listening port of the primary RADIUS server.

Table C-16 describes the `SQLNET.RADIUS_AUTHENTICATION_PORT` parameter attributes.

Table C-16 SQLNET.RADIUS\_AUTHENTICATION\_PORT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_PORT=` `port_number` |
| Default setting | `1645` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.9 SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT

The `SQLNET.RADIUS_AUTHENTICATION_TIMEOUT` parameter sets the time to wait for response.

Table C-17 describes the `SQLNET.RADIUS_AUTHENTICATION_TIMEOUT` parameter attributes.

Table C-17 SQLNET.RADIUS\_AUTHENTICATION\_TIMEOUT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_TIMEOUT=` `time_in_seconds` |
| Default setting | `5` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.10 SQLNET.RADIUS\_AUTHENTICATION\_RETRIES

The `SQLNET.RADIUS_AUTHENTICATION_RETRIES` parameter sets the number of times to resend authentication information.

Table C-18 describes the `SQLNET.RADIUS_AUTHENTICATION_RETRIES` parameter attributes.

Table C-18 SQLNET.RADIUS\_AUTHENTICATION\_RETRIES Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_AUTHENTICATION_RETRIES=` `n_times_to_resend` |
| Default setting | `3` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.11 SQLNET.RADIUS\_CHALLENGE\_RESPONSE

The `SQLNET.RADIUS_CHALLENGE_RESPONSE` parameter turns on or turns off the challenge-response or asynchronous mode support.

Table C-19 describes the `SQLNET.RADIUS_CHALLENGE_RESPONSE` parameter attributes.

Table C-19 SQLNET.RADIUS\_CHALLENGE\_RESPONSE Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CHALLENGE_RESPONSE=` `on` |
| Default setting | `off` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.12 SQLNET.RADIUS\_CHALLENGE\_KEYWORD

The `SQLNET.RADIUS_CHALLENGE_KEYWORD` parameter sets the keyword to request a challenge from the RADIUS server.

The user types no password on the client.

Table C-20 describes the `SQLNET.RADIUS_CHALLENGE_KEYWORD` parameter attributes.

Table C-20 SQLNET.RADIUS\_CHALLENGE\_KEYWORD Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CHALLENGE_KEYWORD=` `keyword` |
| Default setting | `challenge` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.13 SQLNET.RADIUS\_CLASSPATH

The `SQLNET.RADIUS_CLASSPATH` parameter sets the path for Java classes and the JDK Java libraries.

If you decide to use the challenge-response authentication mode, then RADIUS presents the user with a Java-based graphical interface requesting first a password, then additional information, for example, a dynamic password that the user obtains from a token card.

Add the `SQLNET.RADIUS_CLASSPATH` parameter in the `sqlnet.ora` file to set the path for the Java classes for that graphical interface, and to set the path to the JDK Java libraries.

Table C-21 describes the `SQLNET.RADIUS_CLASSPATH` parameter attributes.

Table C-21 SQLNET.RADIUS\_CLASSPATH Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_CLASSPATH=` `path_to_GUI_Java_classes` |
| Default setting | `$ORACLE_HOME/jlib/netradius.jar:$ORACLE_HOME/JRE/lib/sparc/native_threads` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.14 SQLNET.RADIUS\_SECRET

The `SQLNET.RADIUS_SECRET` parameter specifies the file name and location of the RADIUS secret key.

Table C-22 describes the `SQLNET.RADIUS_SECRET` parameter attributes.

Table C-22 SQLNET.RADIUS\_SECRET Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_SECRET=` `path_to_RADIUS_secret_key` |
| Default setting | `$ORACLE_HOME/network/security/radius.key` |

**Parent topic:** sqlnet.ora File Parameters

##### C.3.1.15 SQLNET.RADIUS\_SEND\_ACCOUNTING

The `SQLNET.RADIUS_SEND_ACCOUNTING` parameter turns accounting on or off.

If you enable accounting, packets will be sent to the active RADIUS server at the listening port plus one. By default, packets are sent to port 1646. You need to turn this feature on only when your RADIUS server supports accounting and you want to keep track of the number of times the user is logging on to the system.

Table C-23 describes the `SQLNET.RADIUS_SEND_ACCOUNTING` parameter attributes.

Table C-23 SQLNET.RADIUS\_SEND\_ACCOUNTING Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.RADIUS_SEND_ACCOUNTING=` `on` |
| Default setting | `off` |

**Parent topic:** sqlnet.ora File Parameters

#### C.3.2 Minimum RADIUS Parameters

At minimum, you should use the `SQLNET.AUTHENTICATION_SERVICES` and `SQLNET.RADIUS.AUTHENTICATION` parameters.

Use the following settings:

```
sqlnet.authentication_services = (radius)
sqlnet.radius.authentication   = IP-address-of-RADIUS-server
```

**Parent topic:** Parameters for Clients and Servers Using RADIUS Authentication

#### C.3.3 Initialization File Parameter for RADIUS

For RADIUS, you should set the `OS_AUTHENT_PREFIX` initialization parameter.

For example:

```
OS_AUTHENT_PREFIX=""
```

**Parent topic:** Parameters for Clients and Servers Using RADIUS Authentication
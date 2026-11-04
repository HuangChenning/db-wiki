---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/data-encryption-and-integrity-parameters.html
tags:
  - oracle
  - 21c
  - security-guide
---

- About Using sqlnet.ora for Data Encryption and Integrity  
	You can use the default parameter settings as a guideline for configuring data encryption and integrity.
- Sample sqlnet.ora File  
	The sample `sqlnet.ora` configuration file is based on a set of clients with similar characteristics and a set of servers with similar characteristics.
- Data Encryption and Integrity Parameters  
	Oracle provides data and integrity parameters that you can set in the `sqlnet.ora` file.

**Parent topic:** [Appendixes](part_7.md)

### B.1 About Using sqlnet.ora for Data Encryption and Integrity

You can use the default parameter settings as a guideline for configuring data encryption and integrity.

This `sqlnet.ora` file is generated when you perform the network configuration. Also provided in this process are encryption and data integrity parameters.

**Parent topic:** Data Encryption and Integrity Parameters

### B.2 Sample sqlnet.ora File

The sample `sqlnet.ora` configuration file is based on a set of clients with similar characteristics and a set of servers with similar characteristics.

The file includes examples of Oracle Database encryption and data integrity parameters.

By default, the `sqlnet.ora` file is located in the `ORACLE_HOME` `/network/admin` directory or in the location set by the `TNS_ADMIN` environment variable. Ensure that you have properly set the `TNS_ADMIN` variable to point to the correct `sqlnet.ora` file.

Trace File Setup

```
#Trace file setup 
trace_level_server=16 
trace_level_client=16  
trace_directory_server=/orant/network/trace 
trace_directory_client=/orant/network/trace 
trace_file_client=cli  
trace_file_server=srv 
trace_unique_client=true
```

Oracle Database Native Network Encryption

```
sqlnet.encryption_server=accepted 
sqlnet.encryption_client=requested 
sqlnet.encryption_types_server=(RC4_40) 
sqlnet.encryption_types_client=(RC4_40)
```

Note:

The RC4\_40 algorithm is deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).

Oracle Database Network Data Integrity

```
#ASO Checksum 
sqlnet.crypto_checksum_server=requested 
sqlnet.crypto_checksum_client=requested  
sqlnet.crypto_checksum_types_server = (SHA256) 
sqlnet.crypto_checksum_types_client = (SHA256)
```

Transport Layer Security

```
#SSL 
WALLET_LOCATION = (SOURCE=
                   (METHOD = FILE) 
                      (METHOD_DATA = 
                         DIRECTORY=/wallet) 

SSL_CIPHER_SUITES=(SSL_DH_anon_WITH_RC4_128_MD5) 
SSL_VERSION= 3 
SSL_CLIENT_AUTHENTICATION=FALSE
```

Common

```
#Common
automatic_ipc = off
sqlnet.authentication_services = (beq)
names.directory_path = (TNSNAMES)
```

Kerberos

```
#Kerberos 
sqlnet.authentication_services = (beq, kerberos5)
sqlnet.authentication_kerberos5_service = oracle
sqlnet.kerberos5_conf= /krb5/krb.conf
sqlnet.kerberos5_keytab= /krb5/v5srvtab
sqlnet.kerberos5_realms= /krb5/krb.realm
sqlnet.kerberos5_cc_name = /krb5/krb5.cc
sqlnet.kerberos5_clockskew=900
sqlnet.kerberos5_conf_mit=false
```

RADIUS

```
#Radius
sqlnet.authentication_services = (beq, RADIUS )
sqlnet.radius_authentication_timeout = (10)
sqlnet.radius_authentication_retries = (2)
sqlnet.radius_authentication_port = (1645)
sqlnet.radius_send_accounting = OFF
sqlnet.radius_secret = /orant/network/admin/radius.key
sqlnet.radius_authentication = radius.us.example.com
sqlnet.radius_challenge_response = OFF
sqlnet.radius_challenge_keyword = challenge
sqlnet.radius_challenge_interface =
oracle/net/radius/DefaultRadiusInterface
sqlnet.radius_classpath = /jre1.1/
```

**Parent topic:** Data Encryption and Integrity Parameters

### B.3 Data Encryption and Integrity Parameters

Oracle provides data and integrity parameters that you can set in the `sqlnet.ora` file.

- About the Data Encryption and Integrity Parameters  
	The data encryption and integrity parameters control the type of encryption algorithm you are using.
- SQLNET.ENCRYPTION\_SERVER  
	The `SQLNET.ENCRYPTION_SERVER` parameter specifies the encryption behavior when a client or a server acting as a client connects to this server.
- SQLNET.ENCRYPTION\_CLIENT  
	The `SQLNET.ENCRYPTION_CLIENT` parameter specifies the encryption behavior when this client or server acting as a client connects to a server.
- SQLNET.CRYPTO\_CHECKSUM\_SERVER  
	The `SQLNET.CRYPTO_CHECKSUM_SERVER` parameter specifies the data integrity behavior when a client or another server acting as a client connects to this server.
- SQLNET.CRYPTO\_CHECKSUM\_CLIENT  
	The `SQLNET.CRYPTO_CHECKSUM_CLIENT` parameter specifies the desired data integrity behavior when this client or server acting as a client connects to a server.
- SQLNET.ENCRYPTION\_TYPES\_SERVER  
	The `SQLNET.ENCRYPTION_TYPES_SERVER` parameter specifies encryption algorithms this server uses in the order of the intended use.
- SQLNET.ENCRYPTION\_TYPES\_CLIENT  
	The `SQLNET.ENCRYPTION_TYPES_CLIENT` parameter specifies encryption algorithms this client or the server acting as a client uses.
- SQLNET.CRYPTO\_CHECKSUM\_TYPES\_SERVER  
	The `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` parameter specifies data integrity algorithms that this server or client to another server uses, in order of intended use.
- SQLNET.CRYPTO\_CHECKSUM\_TYPES\_CLIENT  
	The `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` parameter specifies a list of data integrity algorithms that this client or server acting as a client uses.

**Parent topic:** Data Encryption and Integrity Parameters

#### B.3.1 About the Data Encryption and Integrity Parameters

The data encryption and integrity parameters control the type of encryption algorithm you are using.

If you do not specify any values for Server Encryption, Client Encryption, Server Checksum, or Client Checksum, the corresponding configuration parameters do not appear in the `sqlnet.ora` file. However, the defaults are `ACCEPTED`.

For both data encryption and integrity algorithms, the server selects the first algorithm listed in its `sqlnet.ora ` file that matches an algorithm listed in the client `sqlnet.ora` file, or in the client installed list if the client lists no algorithms in its `sqlnet.ora` file. If there are no entries in the server `sqlnet.ora` file, the server sequentially searches its installed list to match an item on the client side—either in the client `sqlnet.ora ` file or in the client installed list. If no match can be made and one side of the connection REQUIRED the algorithm type (data encryption or integrity), then the connection fails. Otherwise, the connection succeeds with the algorithm type `inactive`.

Data encryption and integrity algorithms are selected independently of each other. Encryption can be activated without integrity, and integrity can be activated without encryption, as shown by Table B-1:

Table B-1 Algorithm Type Selection

| Encryption Selected? | Integrity Selected? |
| --- | --- |
| Yes | No |
| Yes | Yes |
| No | Yes |
| No | No |

#### B.3.2 SQLNET.ENCRYPTION\_SERVER

The `SQLNET.ENCRYPTION_SERVER` parameter specifies the encryption behavior when a client or a server acting as a client connects to this server.

The behavior of the server partially depends on the `SQLNET.ENCRYPTION_CLIENT` setting at the other end of the connection.

Table B-2 describes the `SQLNET.ENCRYPTION_SERVER` parameter attributes.

Table B-2 SQLNET.ENCRYPTION\_SERVER Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.ENCRYPTION_SERVER = ` `valid_value` |
| Valid Values | `ACCEPTED`, `REJECTED`, `REQUESTED`, `REQUIRED` |
| Default Setting | `ACCEPTED` |

#### B.3.3 SQLNET.ENCRYPTION\_CLIENT

The `SQLNET.ENCRYPTION_CLIENT` parameter specifies the encryption behavior when this client or server acting as a client connects to a server.

The behavior of the client partially depends on the value set for `SQLNET.ENCRYPTION_SERVER` at the other end of the connection.

Table B-3 describes the `SQLNET.ENCRYPTION_CLIENT` parameter attributes.

Table B-3 SQLNET.ENCRYPTION\_CLIENT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.ENCRYPTION_CLIENT = ` `valid_value` |
| Valid Values | `ACCEPTED`, `REJECTED`, `REQUESTED`, `REQUIRED` |
| Default Setting | `ACCEPTED` |

#### B.3.4 SQLNET.CRYPTO\_CHECKSUM\_SERVER

The `SQLNET.CRYPTO_CHECKSUM_SERVER` parameter specifies the data integrity behavior when a client or another server acting as a client connects to this server.

The behavior partially depends on the `SQLNET.CRYPTO_CHECKSUM_CLIENT` setting at the other end of the connection.

Table B-4 describes the `SQLNET.CRYPTO_CHECKSUM_SERVER` parameter attributes.

Table B-4 SQLNET.CRYPTO\_CHECKSUM\_SERVER Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.CRYPTO_CHECKSUM_SERVER = ` `valid_value` |
| Valid Values | `ACCEPTED`, `REJECTED`, `REQUESTED`, `REQUIRED` |
| Default Setting | `ACCEPTED` |

#### B.3.5 SQLNET.CRYPTO\_CHECKSUM\_CLIENT

The `SQLNET.CRYPTO_CHECKSUM_CLIENT` parameter specifies the desired data integrity behavior when this client or server acting as a client connects to a server.

The behavior partially depends on the `SQLNET.CRYPTO_CHECKSUM_SERVER` setting at the other end of the connection.

Table B-5 describes the `SQLNET.CRYPTO_CHECKSUM_CLIENT` parameter attributes.

Table B-5 SQLNET.CRYPTO\_CHECKSUM\_CLIENT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.CRYPTO_CHECKSUM_CLIENT = ` `valid_value` |
| Valid Values | `ACCEPTED`, `REJECTED`, `REQUESTED`, `REQUIRED` |
| Default Setting | `ACCEPTED` |

#### B.3.6 SQLNET.ENCRYPTION\_TYPES\_SERVER

The `SQLNET.ENCRYPTION_TYPES_SERVER` parameter specifies encryption algorithms this server uses in the order of the intended use.

This list is used to negotiate a mutually acceptable algorithm with the client end of the connection. Each algorithm is checked against the list of available client algorithm types until a match is found. If an algorithm that is not installed is specified on this side, the connection terminates with the error message `ORA-12650: No common encryption or data integrity algorithm.`

Table B-6 describes the `SQLNET.ENCRYPTION_TYPES_SERVER` parameter attributes.

Table B-6 SQLNET.ENCRYPTION\_TYPES\_SERVER Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.ENCRYPTION_TYPES_SERVER = (``valid_encryption_algorithm` ` [,``valid_encryption_algorithm``])` |
| Valid Values | - `AES256`: AES (256-bit key size) - `AES192`: AES (192-bit key size) - `AES128`: AES (128-bit key size) |
| Default Setting | If no algorithms are defined in the local `sqlnet.ora` file, then all installed algorithms are used in a negotiation in the preceding sequence. |
| Usage Notes | You can specify multiple encryption algorithms. It can be either a single value or a list of algorithm names. For example, either of the following encryption parameters is acceptable:  `SQLNET.ENCRYPTION_TYPES_SERVER=(AES256)`  `SQLNET.ENCRYPTION_TYPES_SERVER=(AES256,AES192,AES128)` |

#### B.3.7 SQLNET.ENCRYPTION\_TYPES\_CLIENT

The `SQLNET.ENCRYPTION_TYPES_CLIENT` parameter specifies encryption algorithms this client or the server acting as a client uses.

This list is used to negotiate a mutually acceptable algorithm with the other end of the connection. If an algorithm that is not installed is specified on this side, the connection terminates with the `ORA-12650: No common encryption or data integrity algorithm error` message.

Table B-7 describes the `SQLNET.ENCRYPTION_TYPES_CLIENT` parameter attributes.

Table B-7 SQLNET.ENCRYPTION\_TYPES\_CLIENT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.ENCRYPTION_TYPES_CLIENT = (``valid_encryption_algorithm` ` [,``valid_encryption_algorithm``])` |
| Valid Values | - `AES256`: AES (256-bit key size). - `AES192`: AES (192-bit key size). - `AES128`: AES (128-bit key size). |
| Default Setting | If no algorithms are defined in the local `sqlnet.ora` file, all installed algorithms are used in a negotiation. |
| Usage Notes | You can specify multiple encryption algorithms by separating each one with a comma. For example:  `SQLNET.ENCRYPTION_TYPES_CLIENT=(AES256,AES192,AES128)` |

#### B.3.8 SQLNET.CRYPTO\_CHECKSUM\_TYPES\_SERVER

The `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` parameter specifies data integrity algorithms that this server or client to another server uses, in order of intended use.

This list is used to negotiate a mutually acceptable algorithm with the other end of the connection. Each algorithm is checked against the list of available client algorithm types until a match is found. If an algorithm is specified that is not installed on this side, the connection terminates with the `ORA-12650: No common encryption or data integrity algorithm error` error message.

Table B-8 describes the `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER` parameter attributes.

Table B-8 SQLNET.CRYPTO\_CHECKSUM\_TYPES\_SERVER Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (``valid_crypto_checksum_algorithm` ` [,``valid_crypto_checksum_algorithm``])` |
| Valid Values | - `SHA512`: SHA-2, produces a 512-bit hash. - `SHA384`: SHA-2, produces a 384-bit hash. - `SHA256`: SHA-2, produces a 256-bit hash. This is the default value. - `SHA1`: Secure Hash Algorithm - `MD5`: Message Digest 5 	Note: 	MD5 is deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2). |
| Default Setting | All available algorithms |

#### B.3.9 SQLNET.CRYPTO\_CHECKSUM\_TYPES\_CLIENT

The `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` parameter specifies a list of data integrity algorithms that this client or server acting as a client uses.

This list is used to negotiate a mutually acceptable algorithm with the other end of the connection. If an algorithm that is not installed on this side is specified, the connection terminates with the `ORA-12650: No common encryption or data integrity algorithm error` error message.

Table B-9 describes the `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` parameter attributes.

Table B-9 SQLNET.CRYPTO\_CHECKSUM\_TYPES\_CLIENT Parameter Attributes

| Attribute | Description |
| --- | --- |
| Syntax | `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT = (``valid_crypto_checksum_algorithm` ` [,``valid_crypto_checksum_algorithm``])` |
| Valid Values | - `SHA512`: SHA-2, produces a 512-bit hash. - `SHA384`: SHA-2, produces a 384-bit hash. - `SHA256`: SHA-2, produces a 256-bit hash. This is the default value. - `SHA1`: Secure Hash Algorithm - `MD5`: Message Digest 5 	Note: 	MD5 is deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2). |
| Default Setting | If no algorithms are defined in the local `sqlnet.ora` file, all installed algorithms are used in a negotiation starting with `SHA256.` |
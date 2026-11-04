---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-secure-sockets-layer-authentication.html
tags:
  - oracle
  - 21c
  - security-guide
---

- Transport Layer Security and Secure Sockets Layer  
	Netscape Communications Corporation designed Transport Layer Security (TLS), previously called Secure Sockets Layer (SSL), to secure network connections.
- How Oracle Database Uses Transport Layer Security for Authentication  
	Transport Layer Security works with the core Oracle Database features such as encryption and data access controls.
- How Transport Layer Security Works in an Oracle Environment: The TLS Handshake  
	When a network connection over Transport Layer Security is initiated, the client and server perform a TLS handshake before performing the authentication.
- Public Key Infrastructure in an Oracle Environment  
	A public key infrastructure (PKI) is a substrate of network components that provide a security underpinning, based on trust assertions, for an entire organization.
- Transport Layer Security Combined with Other Authentication Methods  
	You can configure Oracle Database to use TLS concurrently with database user names and passwords, RADIUS, and Kerberos.
- Transport Layer Security and Firewalls  
	Oracle Database supports two application proxy-based and stateful packet inspection of firewalls.
- Transport Layer Security Usage Issues  
	You should be aware of TLS usage issues, such as communication with other Oracle products and types of supported authentication and encryption methods.
- Transport Layer Security Connection without a Client Wallet  
	A Transport Layer Security (TLS) connection that uses a common root certificate for the database server does not require a client wallet.
- Transport Layer Security Connection with a Client Wallet  
	You must configure Transport Layer Security on the server, and then the client.
- Transport Layer Security Connections in an Oracle Real Application Clusters Environment  
	You can configure Transport Layer Security (TLS) connections in an Oracle Real Application Clusters (Oracle RAC) environment by using Oracle RAC tools and modifying Oracle Database configuration files.
- Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store  
	To perform this configuration with Microsoft Certificate Store (MCS), you use the `orapki` command-line tool to generate certificates and manipulate the Oracle wallets.
- Troubleshooting the Transport Layer Security Configuration  
	Common errors may occur while you use the Oracle Database SSL adapter.
- Certificate Validation with Certificate Revocation Lists  
	Oracle provides tools that enable you to validate certificates using certificate revocation lists.
- Configuring Your System to Use Hardware Security Modules  
	Oracle Database supports hardware security modules that use APIs that conform to the RSA Security, Inc., PKCS #11 specification.

**Parent topic:** [Managing Strong Authentication](part_5.md)

### 22.1 Transport Layer Security and Secure Sockets Layer

Netscape Communications Corporation designed Transport Layer Security (TLS), previously called Secure Sockets Layer (SSL), to secure network connections.

- The Difference Between Transport Layer Security and Secure Sockets Layer  
	Transport Layer Security (TLS) is an incremental version of Secure Sockets Layer (SSL) version 3.0.
- Using Transport Layer Security in a Multitenant Environment  
	Transport Layer Security (TLS) can be used for application containers.
- Enabling Oracle Internet Directory to Use Transport Layer Security Authentication  
	To enable Oracle Internet Directory (OID) to use Transport Layer Security (TLS), create a wallet and certificates, and modify `tnsnames.ora` and `sqlnet.ora`.
- Improving Native Network Encryption Security  
	Oracle provides a patch that will strengthen native network encryption security for both Oracle Database servers and clients.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.1.1 The Difference Between Transport Layer Security and Secure Sockets Layer

Transport Layer Security (TLS) is an incremental version of Secure Sockets Layer (SSL) version 3.0.

Although SSL was primarily developed by Netscape Communications Corporation, the Internet Engineering Task Force (IETF) took over development of it, and renamed it Transport Layer Security (TLS). TLS is an IETF standard.

Oracle Database Security Guide uses the terms Transport Layer Security and TLS instead of Secure Sockets Layer and SSL since the Oracle Database has implemented TLS. However, other documentation in the Oracle Database library may still use the earlier terms Secure Socket Layer and SSL. Where distinctions occur between how you use or configure these protocols, Oracle Database Security Guide specifies what is appropriate for either SSL or TLS.

The Oracle Database software still uses some of the older terminology. For example, the `netmgr` tool still uses the terms Secure Socket Layer and SSL. Many SSL parameters, such as `SSL_SERVER_CERT_DN`, use the older terminology. The names of cipher suites and the wording in error messages also use the SSL terminology. However, all these features work with and apply to Transport Layer Security.

**Parent topic:** Transport Layer Security and Secure Sockets Layer

#### 22.1.2 Using Transport Layer Security in a Multitenant Environment

Transport Layer Security (TLS) can be used for application containers.

If you want to use Transport Layer Security (TLS) for an application container, then you must ensure that each PDB is able to use its own wallet with its own certificates for TLS authentication.

1. Connect to the PDB that uses the wallet.
2. Place the wallet in a subdirectory of the `wallet` directory where the name of the subdirectory is the GUID of the PDB that uses the wallet.
	You must do this because there is no individual `sqlnet.ora` file for each PDB. For example, suppose the `WALLET_LOCATION` parameter in `sqlnet.ora` is set as follows:
	```
	(SOURCE=(METHOD=FILE)(METHOD_DATA=
	   (DIRECTORY=/home/oracle/wallet)))
	```
	Place each PDB’s wallet in the `/home/oracle/wallet/PDB_GUID` directory. You can find the existing PDBs and their GUIDs by querying the `DBA_PDBS` data dictionary view.
	If the `WALLET_LOCATION` parameter is not specified, then you must place the PDB wallet in a leaf subdirectory of the default wallet path where the name of the subdirectory is the GUID of the PDB, and the name of the leaf subdirectory is `TLS`. For example:
	```
	$ORACLE_BASE/admin/db_unique_name/PDB_GUID/TLS
	```
	Or if the `ORACLE_BASE` environment variable is not set, then you can use the Oracle home:
	```
	$ORACLE_HOME/admin/db_unique_name/PDB_GUID/TLS
	```
	These default locations correspond to the default that is used by Oracle Enterprise User Security to locate wallets for authentication to LDAP.
	To enable the PDB to use separate certificates, create a subdirectory under the `$WALLET_LOCATION/PDB_GUID/TLS` directory, and then copy the wallets to this subdirectory.
3. ```
	ALTER PLUGGABLE DATABASE pdb_name CLOSE IMMEDIATE;
	ALTER PLUGGABLE DATABASE pdb_name OPEN;
	```

**Parent topic:** Transport Layer Security and Secure Sockets Layer

#### 22.1.3 Enabling Oracle Internet Directory to Use Transport Layer Security Authentication

To enable Oracle Internet Directory (OID) to use Transport Layer Security (TLS), create a wallet and certificates, and modify `tnsnames.ora` and `sqlnet.ora`.

1. Log in to the database client server that has Oracle Internet Directory (OID) installed.
2. In the home directory for OID, apply the database client patch.
3. Go to the `$ORACLE_HOME/ldap/lib` directory
4. ```
	make -f ins_ldap.mk install
	```
5. Go to the directory where the OID `tnsnames.ora` file is located.
	By default, this directory is `$ORACLE_HOME/network/admin`.
6. Edit the `tnsnames.ora` file to include the following OID settings, which will specify the TCPS port.
	For example:
	```
	OIDDB=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCPS)
	   (HOST=sales_db.us.example.com)(PORT=5500))
	    (CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl.us.example.com)))
	     (SECURITY=(SSL_SERVER_CERT_DN="CN=Server,OU=ST,O=Example,ST=California,C=US"))
	```
	In this example, `SSL_SERVER_CERT_DN` points to the DN of the database server certificate.
7. Configure the wallet location in the `sqlnet.ora` file.
	For example:
	```
	ENCRYPTION_WALLET_LOCATION=
	 (SOURCE=
	  (METHOD=FILE)
	   (METHOD_DATA=
	    (DIRECTORY=/etc/ORACLE/WALLETS/$ORACLE_SID/)))
	```
8. Ensure that the `sqlnet.ora` file has the following settings:
	```
	SSL_CLIENT_AUTHENTICATION = FALSE
	SSL_SERVER_DN_MATCH=OFF
	```
9. Use the `orapki` utility to create a new wallet and add database certificates to it.
	For example:
	```
	orapki wallet create -wallet /etc/ORACLE/WALLETS/$ORACLE_SID/oid_wallet
	-auto_login -pwd wallet_password
	orapki wallet add -wallet /etc/ORACLE/WALLETS/$ORACLE_SID/oid_wallet
	-trusted_cert -cert /etc/ORACLE/certificates/dbssl/root/b64certificate.txt 
	-pwd wallet_password
	./orapki wallet add -wallet /etc/ORACLE/WALLETS/$ORACLE_SID/oid_gwallet
	-trusted_cert -cert /etc/ORACLE/certificates/dbssl/netadmin/cert.txt -pwd
	wallet_password
	```

**Parent topic:** Transport Layer Security and Secure Sockets Layer

#### 22.1.4 Improving Native Network Encryption Security

Oracle provides a patch that will strengthen native network encryption security for both Oracle Database servers and clients.

- About Improving Native Network Encryption Security  
	The Oracle patch will update encryption and checksumming algorithms and deprecate weak encryption and checksumming algorithms.
- Applying Security Improvement Updates to Native Network Encryption  
	In addition to applying a patch to the Oracle Database server and client, you must set the server and client `sqlnet.ora` parameters.

**Parent topic:** Transport Layer Security and Secure Sockets Layer

##### 22.1.4.1 About Improving Native Network Encryption Security

The Oracle patch will update encryption and checksumming algorithms and deprecate weak encryption and checksumming algorithms.

This patch, which you can download from My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2), strengthens the connection between servers and clients, fixing a vulnerability in native network encryption and checksumming algorithms. It adds two parameters that make it easy to disable older, less secure encryption and checksumming algorithms. Oracle strongly recommends that you apply this patch to your Oracle Database server and clients.

This patch applies to Oracle Database releases 11.2 and later. You can apply this patch in the following environments: standalone, multitenant, primary-standby, Oracle Real Application Clusters (Oracle RAC), and environments that use database links.

The supported algorithms that have been improved are as follows:

- Encryption algorithms: AES128, AES192 and AES256
- Checksumming algorithms: SHA1, SHA256, SHA384, and SHA512

Weak algorithms that are deprecated and should not be used after you apply the patch are as follows:

- Encryption algorithms: DES, DES40, 3DES112, 3DES168, RC4\_40, RC4\_56, RC4\_128, and RC4\_256
- Checksumming algorithm: MD5

The general procedure that you will follow is to first replace references to desupported algorithms in your Oracle Database environment with supported algorithms, patch the server, patch the client, and finally, set `sqlnet.ora` parameters to re-enable a proper connection between the server and clients.

The patch affects the following areas including, but not limited to, the following:

- JDBC network encryption-related configuration settings
- Encryption and integrity parameters that you have configured using Oracle Net Manager
- Transport Layer Security (TLS) `SSL_CIPHER_SUITE` parameter settings
- SecureFiles LOB encrypted columns
- Database Resident Connection Pooling (DRCP) configurations
- Encryption settings used for the configuration of Oracle Call Interface (Oracle OCI), `ODP.NET`

**Parent topic:** Improving Native Network Encryption Security

##### 22.1.4.2 Applying Security Improvement Updates to Native Network Encryption

In addition to applying a patch to the Oracle Database server and client, you must set the server and client `sqlnet.ora` parameters.

Ensure that you perform the following steps in the order shown:

1. Back up the servers and clients to which you will install the patch.
2. Log in to My Oracle Support and then download patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).My Oracle Support is located at the following URL:
	[`https://support.oracle.com`](https://support.oracle.com/)
3. Patch the server.
	Follow the instructions in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2) to apply the patch to the server. You will apply the same patch to the client in a later step.
4. Patch the clients.
	Determine which clients you need to patch.
	Follow the instructions in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2) to apply the patch to each client.
5. In each client `sqlnet.ora` file, remove all deprecated algorithms if they are defined.
	You can bypass this step if the following parameters are not defined or have no algorithms listed.
	- `SQLNET.ENCRYPTION_TYPES_CLIENT`
	- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`
6. In the server `sqlnet.ora` file, remove all deprecated algorithms if they are defined.
	You can bypass this step if the following parameters are not defined or have no algorithms listed.
	- `SQLNET.ENCRYPTION_TYPES_SERVER`
	- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER`
7. For maximum security on the server, set the following `sqlnet.ora` parameters:
	- `SQLNET.ENCRYPTION_SERVER = REQUIRED`
	- `SQLNET.ENCRYPTION_TYPES_SERVER = (AES256)`
	- `SQLNET.CRYPTO_CHECKSUM_SERVER = REQUIRED`
	- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (SHA512)`
	- `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`
8. For maximum security on the client, set the following `sqlnet.ora` parameters:
	- `SQLNET.ENCRYPTION_CLIENT = REQUIRED`
	- `SQLNET.ENCRYPTION_TYPES_CLIENT = (AES256)`
	- `SQLNET.CRYPTO_CHECKSUM_CLIENT = REQUIRED`
	- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT = (SHA512)`
	- `SQLNET.ALLOW_WEAK_CRYPTO = FALSE`
9. In each client `sqlnet.ora` file, after you have removed all the deprecated algorithms from the server and the clients per steps [^1] and [^2], set the parameter `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` so that the clients can be prevented from communicating with unpatched servers.
	If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.
10. In the server `sqlnet.ora` file, after you have updated all the clients with `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` per step [^3], set the parameter `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`. This parameter prevents a patched server from communicating with unpatched clients.
	If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.
	If you use the database links, then the first database server acts as a client and connects to the second server. Therefore, ensure that all servers are fully patched and unsupported algorithms are removed before you set `SQLNET.ALLOW_WEAK_CRYPTO` to `FALSE`

**Parent topic:** Improving Native Network Encryption Security

### 22.2 How Oracle Database Uses Transport Layer Security for Authentication

Transport Layer Security works with the core Oracle Database features such as encryption and data access controls.

By using Oracle Database TLS functionality to secure communications between clients and servers, you can

- Use TLS to encrypt the connection between clients and servers
- Authenticate any client or server, such as Oracle Application Server 10g, to any Oracle database server that is configured to communicate over TLS

You can use TLS features by themselves or in combination with other authentication methods supported by Oracle Database. For example, you can use the encryption provided by TLS in combination with the authentication provided by Kerberos. TLS supports any of the following authentication modes:

- Only the server authenticates itself to the client
- Both client and server authenticate themselves to each other
- Neither the client nor the server authenticates itself to the other, thus using the TLS encryption feature by itself
	See Also:
	The TLS Protocol, version 3.0, published by the Internet Engineering Task Force, for a more detailed discussion of TLS

**Parent topic:** Configuring Transport Layer Security Authentication

### 22.3 How Transport Layer Security Works in an Oracle Environment: The TLS Handshake

When a network connection over Transport Layer Security is initiated, the client and server perform a TLS handshake before performing the authentication.

The handshake process is as follows:

1. The client and server establish which cipher suites to use. This includes which encryption algorithms are used for data transfers.
2. The server sends its certificate to the client, and the client verifies that the server's certificate was signed by a trusted CA. This step verifies the identity of the server.
3. Similarly, if client authentication is required, the client sends its own certificate to the server, and the server verifies that the client's certificate was signed by a trusted CA.
4. The client and server exchange key information using public key cryptography. Based on this information, each generates a session key. A key is shared by at least two parties (usually a client and a server) that is used for data encryption for the duration of a single communication session. Session keys are typically used to encrypt network traffic; a client and a server can negotiate a session key at the beginning of a session, and that key is used to encrypt all network traffic between the parties for that session. If the client and server communicate again in a new session, they negotiate a new session key. All subsequent communications between the client and the server is encrypted and decrypted by using this session key and the negotiated cipher suite.

The authentication process is as follows:

1. On a client, the user initiates an Oracle Net connection to the server by using TLS.
2. TLS performs the handshake between the client and the server.
3. If the handshake is successful, then the server verifies that the user has the appropriate authorization to access the database.

**Parent topic:** Configuring Transport Layer Security Authentication

### 22.4 Public Key Infrastructure in an Oracle Environment

A public key infrastructure (PKI) is a substrate of network components that provide a security underpinning, based on trust assertions, for an entire organization.

- About Public Key Cryptography  
	Traditional private-key or symmetric-key cryptography requires a single, secret key shared by two or more parties to establish a secure communication.
- Public Key Infrastructure Components in an Oracle Environment  
	Public key infrastructure (PKI) components in an Oracle environment include a certificate authority, certificates, certificate revocation lists, and wallets.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.4.1 About Public Key Cryptography

Traditional private-key or symmetric-key cryptography requires a single, secret key shared by two or more parties to establish a secure communication.

This key is used to both encrypt and decrypt secure messages sent between the parties, requiring prior, secure distribution of the key to each party. The problem with this method is that it is difficult to securely transmit and store the key.

Public-key cryptography provides a solution to this problem, by employing public and private key pairs and a secure method for key distribution. The freely available public key is used to encrypt messages that can only be decrypted by the holder of the associated private key. The private key is securely stored, together with other security credentials, in an encrypted container called a wallet.

Public-key algorithms can guarantee the secrecy of a message, but they do not necessarily guarantee secure communications because they do not verify the identities of the communicating parties. To establish secure communications, it is important to verify that the public key used to encrypt a message does in fact belong to the target recipient. Otherwise, a third party can potentially eavesdrop on the communication and intercept public key requests, substituting its own public key for a legitimate key (the third-party attack).

In order to avoid such an attack, it is necessary to verify the owner of the public key, a process called authentication. Authentication can be accomplished through a certificate authority (CA), which is a third party that is trusted by both of the communicating parties.

The CA issues public key certificates that contain an entity's name, public key, and certain other security credentials. Such credentials typically include the CA name, the CA signature, and the certificate effective dates (From Date, To Date).

The CA uses its private key to encrypt a message, while the public key is used to decrypt it, thus verifying that the message was encrypted by the CA. The CA public key is well known and does not have to be authenticated each time it is accessed. Such CA public keys are stored in wallets.

**Parent topic:** Public Key Infrastructure in an Oracle Environment

#### 22.4.2 Public Key Infrastructure Components in an Oracle Environment

Public key infrastructure (PKI) components in an Oracle environment include a certificate authority, certificates, certificate revocation lists, and wallets.

**Parent topic:** Public Key Infrastructure in an Oracle Environment

##### 22.4.2.1 Certificate Authority

A certificate authority (CA) is a trusted third party that certifies the identity of entities, such as users, databases, administrators, clients, and servers.

When an entity requests certification, the CA verifies its identity and grants a certificate, which is signed with the CA's private key.

Different CAs may have different identification requirements when issuing certificates. Some CAs may verify a requester's identity with a driver's license, some may verify identity with the requester's fingerprints, while others may require that requesters have their certificate request form notarized.

The CA publishes its own certificate, which includes its public key. Each network entity has a list of trusted CA certificates. Before communicating, network entities exchange certificates and check that each other's certificate is signed by one of the CAs on their respective trusted CA certificate lists.

Network entities can obtain their certificates from the same or different CAs.

##### 22.4.2.2 Certificates

A certificate is created when an entity's public key is signed by a trusted certificate authority (CA).

A certificate ensures that an entity's identification information is correct and that the public key actually belongs to that entity.

A certificate contains the entity's name, public key, and an expiration date, as well as a serial number and certificate chain information. (A certificate chain is an ordered list of certificates containing an end-user or subscriber certificate and its certificate authority certificate.) It can also contain information about the privileges associated with the certificate.

When a network entity receives a certificate, it verifies that it is a trusted certificate, that is, one that has been issued and signed by a trusted certificate authority. A certificate remains valid until it expires or until it is revoked.

**Parent topic:** Public Key Infrastructure Components in an Oracle Environment

##### 22.4.2.3 Certificate Revocation Lists

When a CA signs a certificate binding a public key pair to a user identity, the certificate is valid for a specified time.

However, certain events, such as user name changes or compromised private keys, can render a certificate invalid before the validity period expires. When this happens, the CA revokes the certificate and adds its serial number to a Certificate Revocation List (CRL). The CA periodically publishes CRLs to alert the user population when it is no longer acceptable to use a particular public key to verify its associated user identity.

When servers or clients receive user certificates in an Oracle environment, they can validate the certificate by checking its expiration date, signature, and revocation status. Certificate revocation status is checked by validating it against published CRLs. If certificate revocation status checking is turned on, then the server searches for the appropriate CRL depending on how this feature has been configured. The server searches for CRLs in the following locations in this order:

1. Local file system
2. Oracle Internet Directory
3. CRL Distribution Point (CRL DP), a location specified in the CRL Distribution Point (CRL DP) X.509, version 3, certificate extension when the certificate is issued. A CRL DP is an optional extension specified by the X.509 version 3 certificate standard, which indicates the location of the Partitioned CRL where revocation information for a certificate is stored. Typically, the value in this extension is in the form of a URL. CRL DPs allow revocation information within a single certificate authority domain to be posted in multiple CRLs. CRL DPs subdivide revocation information into more manageable pieces to avoid proliferating voluminous CRLs, thereby providing performance benefits. For example, a CRL DP is specified in the certificate and can point to a file on a Web server from which that certificate's revocation information can be downloaded.

Note:

To use CRLs with other Oracle products, refer to the specific product documentation. This implementation of certificate validation with CRLs is only available in the Oracle Database 12c release 1 (12.1) and later SSL adapter.

##### 22.4.2.4 Wallets

A wallet is a container that stores authentication and signing credentials, including private keys, certificates, and trusted certificates TLS needs.

In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates, with the exception of Diffie-Hellman.

Security administrators use Oracle Wallet Manager to manage security credentials on the server. Wallet owners use it to manage security credentials on clients. Specifically, you use Oracle Wallet Manager to do the following:

- Generate a public-private key pair and create a certificate request
- Store a user certificate that matches with the private key
- Configure trusted certificates
	See Also:
	- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI160) for information about Oracle Wallet Manager
	- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9731) for information about creating a new Oracle wallet
	- [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9757) for information about managing trusted certificates in Oracle wallets

Note:

Oracle Wallet Manager (OWM) is deprecated with Oracle Database 21c.

Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

**Parent topic:** Public Key Infrastructure Components in an Oracle Environment

##### 22.4.2.5 Hardware Security Modules

The hardware security modules for SSL include devices to handle various functions and hardware devices to store cryptographic information.

Oracle Database uses these devices for the following functions:

- Store cryptographic information, such as private keys
- Perform cryptographic operations to off load RSA operations from the server, freeing the CPU to respond to other transactions

Cryptographic information can be stored on two types of hardware devices:

- (Server-side) Hardware boxes where keys are stored in the box, but managed by using tokens.
- (Client-side) Smart card readers, which support storing private keys on tokens.

An Oracle environment supports hardware devices using APIs that conform to the RSA Security, Inc., Public-Key Cryptography Standards (PKCS) #11 specification.

Note:

Currently, SafeNET, nCipher, and Utimaco devices are certified with Oracle Database

### 22.5 Transport Layer Security Combined with Other Authentication Methods

You can configure Oracle Database to use TLS concurrently with database user names and passwords, RADIUS, and Kerberos.

- Architecture: Oracle Database and Transport Layer Security  
	It is important to understand the architecture of how Oracle Database works with TLS.
- How Transport Layer Security Works with Other Authentication Methods  
	Transport Layer Security can be used with other authentication methods that Oracle Database supports.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.5.1 Architecture: Oracle Database and Transport Layer Security

It is important to understand the architecture of how Oracle Database works with TLS.

[Figure 19-4](introduction-to-strong-authentication.md), which displays the Oracle Database implementation of Transport Layer Security architecture, shows that Oracle Databases operates at the session layer on top of TLS and uses TCP/IP at the transport layer. The session layer is a network layer that provides the services needed by the presentation layer entities that enable them to organize and synchronize their dialogue and manage their data exchange. This layer establishes, manages, and terminates network sessions between the client and server. The transport layer is a networking layer that maintains end-to-end reliability through data flow control and error recovery methods. Oracle Net Services uses Oracle protocol supports for the transport layer.

This separation of functionality lets you employ TLS concurrently with other supported protocols.

#### 22.5.2 How Transport Layer Security Works with Other Authentication Methods

Transport Layer Security can be used with other authentication methods that Oracle Database supports.

Figure 22-1 illustrates a configuration in which Transport Layer Security is used in combination with another authentication method.

Figure 22-1 Transport Layer Security in Relation to Other Authentication Methods

![Figure 22-1 Transport Layer Security in Relation to Other Authentication Methods](img/asoag018.gif)

> This is a text description of asoag018.gif, an image which shows the steps to authenticate clients when SSL is used with other authentication methods as follows:
>
> 1. A client seeks to connect to an Oracle server.
> 2. SSL performs a handshake during which the server authenticates itself to the client and both the client and server establish which cipher suite to use.
> 3. Once the SSL handshake is successfully completed, the user seeks access to the database.
> 4. The Oracle server authenticates the user with the authentication server using a non-SSL authentication method such as Kerberos or RADIUS.
> 5. Upon validation by the authentication server, the Oracle server grants access and authorization to the user. Then the user can access the database securely by using SSL.


In this example, Transport Layer Security is used to establish the initial handshake (server authentication), and an alternative authentication method is used to authenticate the client. The process is as follows:

1. The client seeks to connect to the Oracle database server.
2. Transport Layer Security performs a handshake during which the server authenticates itself to the client and both the client and server establish which cipher suite to use.
3. Once the Transport Layer Security handshake is successfully completed, the user seeks access to the database.
4. The Oracle database server authenticates the user with the authentication server using a non-TLS authentication method such as Kerberos or RADIUS.
5. Upon validation by the authentication server, the Oracle database server grants access and authorization to the user, and then the user can access the database securely by using TLS.

### 22.6 Transport Layer Security and Firewalls

Oracle Database supports two application proxy-based and stateful packet inspection of firewalls.

These firewalls are as follows:

- Application proxy-based firewalls: Examples are Network Associates Gauntlet, or Axent Raptor.
- Stateful packet inspection firewalls: Examples are Check Point Firewall-1, or Cisco PIX Firewall.

When you enable TLS, stateful inspection firewalls behave like application proxy firewalls because they do not decrypt encrypted packets.

Firewalls do not inspect encrypted traffic. When a firewall encounters data addressed to a TLS port on an intranet server, it checks the target IP address against its access rules and lets the TLS packet pass through to permitted TLS ports, rejecting all others.

**Parent topic:** Configuring Transport Layer Security Authentication

### 22.7 Transport Layer Security Usage Issues

You should be aware of TLS usage issues, such as communication with other Oracle products and types of supported authentication and encryption methods.

Consider the following issues when using TLS:

- TLS use enables secure communication with other Oracle products, such as Oracle Internet Directory.
- Because TLS supports both authentication and encryption, the client/server connection is somewhat slower than the standard Oracle Net TCP/IP transport (using native encryption).
- Each TLS authentication mode requires configuration settings.

Note:

If you configure TLS encryption, you must disable non-TLS encryption.

### 22.8 Transport Layer Security Connection without a Client Wallet

A Transport Layer Security (TLS) connection that uses a common root certificate for the database server does not require a client wallet.

- About Transport Layer Security Connections without a Client Wallet  
	You can configure a Transport Layer Security (TLS) connection without a client wallet if your environment meets certain requirements.
- Configuring a Transport Layer Security Connection without a Client Wallet  
	Before you can configure Transport Layer Security (TLS) without using client wallets, you must ensure that the database does not require client authentication.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.8.1 About Transport Layer Security Connections without a Client Wallet

You can configure a Transport Layer Security (TLS) connection without a client wallet if your environment meets certain requirements.

Consider using a TLS connection without a client wallet if your environment meets these requirements:

- The client certificate is not used as a means of user authentication to the database. Only the server certificate is required to establish a TLS connection.
- The server certificate was issued by a certificate authority (CA) whose certificate is available in the system’s default certificate store (common root certificate).
- The Oracle database server is configured to allow TLS connections. (Set `SSL_CLIENT_AUTHENTICATION=FALSE`).

This is the most common type of configuration as long as the root certificate for the database server already exists in the local system certificate store. This configuration can be used for both cloud and on-premises databases. This configuration enables the client to verify server certificates without having to configure its own wallet.

Note the following:

- For the C and Instant Client database drivers (and therefore, SQL\*Plus), the walletless feature is only available on Microsoft Windows and Linux x64.
- For the JDBC-thin driver, the walletless feature is available on all platforms.

#### 22.8.2 Configuring a Transport Layer Security Connection without a Client Wallet

Before you can configure Transport Layer Security (TLS) without using client wallets, you must ensure that the database does not require client authentication.

For the C and Instant Client database drivers (and therefore, SQL\*Plus), the walletless feature is only available on Microsoft Windows and Linux x64. For the JDBC-thin driver, the walletless feature is available on all platforms.

1. Log in to the server where the Oracle database resides.
2. Check the `sqlnet.ora` file for the following settings:
	- `AUTHENTICATION_SERVICES=(tcps)`, which will require TLS for database connections.
	- `SSL_CLIENT_AUTHENTICATION=FALSE`, whose default is `TRUE`, which will require mTLS (mutual TLS requiring a client certificate in a client wallet). Setting this parameter to `FALSE` enables both TLS and mTLS connections from the client. If it is set to `TRUE`, then it is always mTLS.
	By default, the `sqlnet.ora` file is located in the `$ORACLE_HOME/dbs` directory or in the location set by the `TNS_ADMIN` environment variable.
3. Ensure that the server wallet exists in the default location, defined by the `WALLET_ROOT` system parameter, or in the `WALLET_LOCATION` `sqlnet.ora` parameter.
4. Check the `listener.ora` file to ensure TLS is specified.
	```
	LISTENER = (ADDRESS=(PROTOCOL=tcps)(HOST=)(PORT=1234))
	```
5. Ensure that the listener wallet also exists the default location, set by the `WALLET_ROOT` system parameter, or in the `WALLET_LOCATION` `sqlnet.ora` parameter.
	If you are creating a new client connection, then edit the `listener.ora` file to have the following setting:
	```
	ADDRESS=(PROTOCOL=tcps)
	```
	By default, `listener.ora` is located in the `$ORACLE_HOME/network/admin` directory.
6. Log in to the client for the Oracle database.
7. Modify the client `sqlnet.ora` and `tnsnames.ora` files.
	- Edit the `SQLNET.SSL_CLIENT_AUTHENTICATION` setting in the `sqlnet.ora` file.
		Set the `SQLNET.SSL_CLIENT_AUTHENTICATION=FALSE`, because the default is `TRUE`. `FALSE` enables the client to create the connection using either TLS or mTLS. A setting of `FALSE`, will not send information about the client side private certificate. Because this applies to every connection, you can change the `SSL_CLIENT_AUTHENTICATION` parameter in the `tnsnames.ora` connection string using the same parameter setting. If `SSL_CLIENT_AUTHENTICATION=TRUE`, then it can only configure mTLS. This setting is optional.
	- If you connect to multiple databases and some require mTLS with a client wallet, then you can have two options for setting different connections with and without a client wallet, as follows:
		- Option 1: Set `WALLET_LOCATION` in `sqlnet.ora` for a common wallet. Then use `WALLET_LOCATION` in your connect string (in ` tnsnames.ora` or directly on the command line) to override the setting in `sqlnet.ora`. You can specify a different wallet location for a connection or tell the connection to use the system default keystore instead. Use the following parameter to change wallet location to the system default keystore:
			```
			net_service_name = (DESCRIPTION=(ADDRESS = (PROTOCOL=tcps)
			(HOST=host_name)(PORT=port)) (SECURITY=(WALLET_LOCATION=SYSTEM)) 
			(CONNECT_DATA=(SERVICE_NAME=service_name)))
			```
			The default certificate store is located in `/etc/pki/tls/cert.pem` for Linux or in the Microsoft Certificate Store for Microsoft Windows. You cannot change the default location of the certificate store. By default, `tnsnames.ora` is located in the `$ORACLE_HOME/network/admin` directory.
			- Option 2: Only specify `WALLET_LOCATION` as part of the connections that need to use a client wallet. Do not specify `WALLET_LOCATION` in `sqlnet.ora`. Connections that do not need to use a client wallet will automatically use the local default system keystore if `WALLET_LOCATION` is not specified in the `sqlnet.ora` file. For example:
			```
			net_service_name = (DESCRIPTION=(ADDRESS = (PROTOCOL=tcps)
			(HOST=host_name)(PORT=port)) (SECURITY=(WALLET_LOCATION=wallet_file_directory))
			(CONNECT_DATA=(SERVICE_NAME=service_name)))
			```
8. In SQL\*Plus, to determine if the database connections are using TLS, check the connections by performing the following query.
	```
	SELECT SYS_CONTEXT ('USERENV', 'NETWORK_PROTOCOL') FROM DUAL;
	```
	Output similar to the following should appear:
	```
	SYS_CONTEXT('USERENV','NETWORK_PROTOCOL')
	-------------------------------------------------------------------
	tcps
	```

### 22.9 Transport Layer Security Connection with a Client Wallet

You must configure Transport Layer Security on the server, and then the client.

- Step 1: Configure Transport Layer Security on the Server  
	During installation, Oracle sets defaults on the Oracle database server and the Oracle client for TLS parameters, except the Oracle wallet location.
- Step 2: Configure Transport Layer Security on the Client  
	When you configure SSL on the client, you configure the server DNs and use TCP/IP with TLS on the client.
- Step 3: Log in to the Database Instance  
	After you have completed the configuration, you are ready to log in to the database.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.9.1 Step 1: Configure Transport Layer Security on the Server

During installation, Oracle sets defaults on the Oracle database server and the Oracle client for TLS parameters, except the Oracle wallet location.

- Step 1A: Confirm Wallet Creation on the Server  
	Before proceeding to the next step, confirm that a wallet has been created and that it has a certificate.
- Step 1B: Specify the Database Wallet Location on the Server  
	Next, you are ready to specify a location on the server for the wallet.
- Step 1C: Set the Transport Layer Security Cipher Suites on the Server (Optional)  
	Optionally, you can set the Transport Layer Security cipher suites.
- Step 1D: Set the Required Transport Layer Security Version on the Server (Optional)  
	The `SSL_VERSION` parameter defines the version of TLS that must run on the systems with which the server communicates.
- Step 1E: Set Transport Layer Security Client Authentication on the Server (Optional)  
	The `SSL_CLIENT_AUTHENTICATION` parameter controls whether the client is authenticated using TLS.
- Step 1F: Set Transport Layer Security as an Authentication Service on the Server (Optional)  
	The `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file sets the TLS authentication service.
- Step 1G: Disable SSLv3 on the Server and Client (Optional)  
	SSLv3 refers to Secure Sockets Layer version 3.
- Step 1H: Create a Listening Endpoint that Uses TCP/IP with Transport Layer Security on the Server  
	You can configure a listening endpoint to use TCP/IP with TLS on the server.
- Step 1I: Restart the Database  
	To complete the configuration of Transport Layer Security on the server, you must restart the database.

**Parent topic:** Transport Layer Security Connection with a Client Wallet

##### 22.9.1.1 Step 1A: Confirm Wallet Creation on the Server

Before proceeding to the next step, confirm that a wallet has been created and that it has a certificate.

1. Start Oracle Wallet Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command:
		```
		owm
		```
	- (Windows) Select Start, Programs, Oracle-HOME\_NAME, Integrated Management Tools, Wallet Manager
	Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.
2. From the Wallet menu, select Open.
	The wallet should contain a certificate with a status of `Ready` and auto-login turned on. If auto-login is not on, then select it from the Wallet menu and save the wallet again. This turns auto-login on.

##### 22.9.1.2 Step 1B: Specify the Database Wallet Location on the Server

Next, you are ready to specify a location on the server for the wallet.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab (which works for TLS) and then select Configure SSL for: Server.
5. In the Wallet Directory box, enter the directory in which the Oracle wallet is located or click Browse to find it by searching the file system.
	Note that if you are configuring the database-to-directory TLS connection for Enterprise User Security, then Database Configuration Assistant automatically creates a database wallet while registering the database with the directory. You must use that wallet to store the database PKI credentials for TLS-authenticated Enterprise User Security.
	Important:
	- Use Oracle Wallet Manager to create the wallet. (Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.)
	- Use Oracle Net Manager to set the wallet location in the `sqlnet.ora` file. Be aware that the settings in the `sqlnet.ora` file apply to all pluggable databases (PDBs).
	Ensure that you enter the same wallet location when you create it and when you set the location in the `sqlnet.ora` file.
6. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` and `listener.ora` files are updated with the following entries:
	```
	wallet_location = 
	 (SOURCE=
	  (METHOD=File)
	  (METHOD_DATA=
	   (DIRECTORY=wallet_location)))
	```

Note:

The listener uses the wallet defined in the `listener.ora` file. It can use any database wallet. When SSL is configured for a server using Net Manager, the wallet location is entered into the `listener.ora` and the `sqlnet.ora` files. The `listener.ora` file is not relevant to the Oracle client.

To change the listener wallet location so that the listener has its own wallet, you can edit `listener.ora` to enter the new location.

##### 22.9.1.3 Step 1C: Set the Transport Layer Security Cipher Suites on the Server (Optional)

Optionally, you can set the Transport Layer Security cipher suites.

- About the Transport Layer Security Cipher Suites  
	A cipher suite is a set of authentication, encryption, and data integrity algorithms used for exchanging messages between network entities.
- TLS Cipher Suite Authentication, Encryption, Integrity, and TLS Versions  
	Oracle Database supports a set of cipher suites that are set by default when you install Oracle Database.
- Specifying Transport Layer Security Cipher Suites for the Database Server  
	First, you must specify the Transport Layer Security cipher suites for the database server.

**Parent topic:** Step 1: Configure Transport Layer Security on the Server

###### 22.9.1.3.1 About the Transport Layer Security Cipher Suites

A cipher suite is a set of authentication, encryption, and data integrity algorithms used for exchanging messages between network entities.

During a Transport Layer Security handshake, two entities negotiate to see which cipher suite they will use when transmitting messages back and forth.

When you install Oracle Database, the Transport Layer Security cipher suites are set for you by default and negotiated in the order they are listed. You can override the default order by setting the `SSL_CIPHER_SUITES` parameter. Ensure that you enclose the `SSL_CIPHER_SUITES` parameter setting in parentheses (for example, `SSL_CIPHER_SUITES=(tls_rsa_with_aes_128_cbc_sha256)`). Otherwise, the cipher suite setting will not parse correctly.

You can prioritize the cipher suites. When the client negotiates with servers regarding which cipher suite to use, it follows the prioritization you set. When you prioritize the cipher suites, consider the following:

- Compatibility. Server and client must be configured to use compatible cipher suites for a successful connection.
- Cipher priority and strength. Prioritize cipher suites starting with the strongest and moving to the weakest to ensure the highest level of security possible.
- The level of security you want to use.
- The impact on performance.
	Note:
	Regarding Diffie-Hellman anonymous authentication:
	- If you set the server to employ this cipher suite, then you must also set the same cipher suite on the client. Otherwise, the connection fails.
	- If you use a cipher suite employing Diffie-Hellman anonymous, then you must configure the TLS client authentication on the server by setting the `SSL_CLIENT_AUTHENTICATION` parameter to `FALSE`.
	- There is a known bug in which an OCI client requires a wallet even when using a cipher suite with DH\_ANON, which does not authenticate the client.

**Parent topic:** Step 1C: Set the Transport Layer Security Cipher Suites on the Server (Optional)

###### 22.9.1.3.2 TLS Cipher Suite Authentication, Encryption, Integrity, and TLS Versions

Oracle Database supports a set of cipher suites that are set by default when you install Oracle Database.

Table 22-1 lists the authentication, encryption, and data integrity types each cipher suite uses.

In accordance with security best practices, Oracle has deprecated the use of TLS 1.0 and TLS 1.1. To meet your security requirements, Oracle strongly recommends that you use TLS 1.2 instead.

Table 22-1 Transport Layer Security Cipher Suites

| Cipher Suites | Authentication | Encryption | Data Integrity | TLS Compatibility (1.0/1.1 Deprecated) |
| --- | --- | --- | --- | --- |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | ECDHE\_ECDSA | AES 128 GCM | SHA256 (SHA-2) | TLS 1.2 only |
| `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA` | ECDHE\_ECDSA | AES 128 CBC | SHA-1  (deprecated) | TLS 1.0 and later |
| `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256` | ECDHE\_ECDSA | AES 128 CBC | SHA256 (SHA-2) | TLS 1.2 only |
| `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA` | ECDHE\_ECDSA | AES 256 CBC | SHA-1 (deprecated) | TLS 1.0 and later |
| `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384` | ECDHE\_ECDSA | AES 256 CBC | SHA384 (SHA-2) | TLS 1.2 only |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` | ECDHE\_ECDSA | AES 256 GCM | SHA384 (SHA-2) | TLS 1.2 only |
| `TLS_RSA_WITH_AES_128_CBC_SHA256` | RSA | AES 128 CBC | SHA256 (SHA-2) | TLS 1.2 only |
| `TLS_RSA_WITH_AES_128_GCM_SHA256` | RSA | AES 128 GCM | SHA256 (SHA-2) | TLS 1.2 only |
| `TLS_RSA_WITH_AES_128_CBC_SHA` | RSA | AES 128 CBC | SHA-1 (deprecated) | TLS 1.0 only |
| `TLS_RSA_WITH_AES_256_CBC_SHA` | RSA | AES 256 CBC | SHA-1 (deprecated) | TLS 1.0 and later |
| `TLS_RSA_WITH_AES_256_CBC_SHA256` | RSA | AES 256 CBC | SHA256 (SHA-2) | TLS 1.2 only |
| `TLS_RSA_WITH_AES_256_GCM_SHA384` | RSA | AES 256 GCM | SHA384 (SHA-2) | TLS 1.2 only |

Table 22-2 lists cipher suites that you can use, but be aware that they do not the provide authentication of the communicating parties, and hence can be vulnerable to third-party attacks. Oracle recommends that you do not use these cipher suites to protect sensitive data. However, they are useful if the communicating parties want to remain anonymous or simply do not want the overhead caused by mutual authentication.

Table 22-2 SSL\_DH Transport Layer Security Cipher Suites

| Cipher Suites | Authentication | Encryption | Data Integrity | TLS Compatibility |
| --- | --- | --- | --- | --- |
| `SSL_DH_ANON_WITH_3DES_EDE_CBC_SHA` (deprecated) | DH anon | 3DES EDE CBC | SHA-1 | TLS 3.0 and later |

**Parent topic:** Step 1C: Set the Transport Layer Security Cipher Suites on the Server (Optional)

###### 22.9.1.3.3 Specifying Transport Layer Security Cipher Suites for the Database Server

First, you must specify the Transport Layer Security cipher suites for the database server.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab and then select Configure SSL for: Server.
5. In the Cipher Suite Configuration area, click Add.
	A dialog box displays available cipher suites. To see the US domestic cipher suites, click the Show US Domestic Cipher Suites check box.
	Anonymous cipher suites for outbound TLS connections (Database to other services) are deprecated with Oracle Database 21c.
	Anonymous cipher suites only encrypt the connection between client and server without authenticating either party leaving it vulnerable to a person-in-the-middle attack. The following three anonymous cipher suites are deprecated with this release:
	- `NZTLS_DH_ANON_WITH_AES_256_GCM_SHA384`
	- `NZTLS_DH_ANON_WITH_AES_128_GCM_SHA256`
	- `NZSSL_DH_ANON_WITH_3DES_EDE_CBC_SHA`
	To provide better protection for your connections, Oracle recommends using the strongest possible non-anonymous TLS cipher suites.
6. Select a suite and click OK.
	The Cipher Suite Configuration list is updated:
	![ssl0004](img/ssl0004.gif)

> This is a text description of ssl0004.gif, which is an image of the SSL tab in the Oracle Advanced Security profile region of Oracle Net Manager when Configure SSL for the server is selected.
>
> This window has the following fields which you can use to configure SSL on your server:
>
> - Configure SSL for: (choose Server)
> - Wallet Directory (enter the path to the wallet directory--you can choose Browse if you need to browse the file system)
> - Cipher Suite Configuration (select a cipher suite and then click an up or down arrow at the right to change the precedence of when it is applied)
> - Add or Remove (under the Cipher Suite Configuration list, there are an Add and a Remove button that you can use to add or remove a cipher suite)
> - Revocation Check (where you can set whether certificate revocation status checking is performed)
> - Require SSL Version (choose an SSL version from the list--the default is ANY)
> - Require Client Authentication (a check box)
>
> Click the Help button at the bottom right corner of the window to access online help.

7. Use the up and down arrows to prioritize the cipher suites.
8. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` file is updated with the following entry:
	```
	SSL_CIPHER_SUITES= (SSL_cipher_suite1 [,SSL_cipher_suite2])
	```

**Parent topic:** Step 1C: Set the Transport Layer Security Cipher Suites on the Server (Optional)

##### 22.9.1.4 Step 1D: Set the Required Transport Layer Security Version on the Server (Optional)

The `SSL_VERSION` parameter defines the version of TLS that must run on the systems with which the server communicates.

Optionally, you can set the `SSL_VERSION` parameter in the `sqlnet.ora` or the `listener.ora` file.

You can require these systems to use any valid version. The default setting for this parameter in `sqlnet.ora` is `undetermined`, which is set by selecting Any from the list in the SSL tab of the Network Security window.

1. In the Require SSL Version list, the default is Any.
	Accept this default or select the SSL version you want to use.
2. From the File menu, select Save Network Configuration.
	If you chose Any, then the `sqlnet.ora` file is updated with the following entry:
	```
	SSL_VERSION=UNDETERMINED
	```

Note:

SSL 2.0 is not supported on the server side.

##### 22.9.1.5 Step 1E: Set Transport Layer Security Client Authentication on the Server (Optional)

The `SSL_CLIENT_AUTHENTICATION` parameter controls whether the client is authenticated using TLS.

You must set this parameter in the `sqlnet.ora` file on the server. The default value of `SSL_CLIENT_AUTHENTICATION` parameter is `TRUE`.

You can set the `SSL_CLIENT_AUTHENTICATION` to `FALSE` if you are using a cipher suite that contains Diffie-Hellman anonymous authentication (`DH_anon`).

Also, you can set this parameter to `FALSE` for the client to authenticate itself to the server by using any of the non-SSL authentication methods supported by Oracle Database, such as Kerberos or RADIUS.

Note:

There is a known bug in which an OCI client requires a wallet even when using a cipher suite with DH\_ANON, which does not authenticate the client.

To set `SSL_CLIENT_AUTHENTICATION` to `FALSE` on the server:

1. In the SSL page Oracle Net Manager, deselect Require Client Authentication.
	![ssl0005](img/ssl0005.gif)

> This is a text description of ssl0005.gif, which is an image of the SSL tab in the Oracle Advanced Security profile region of Oracle Net Manager when Configure SSL for the server is selected.
>
> You can use the Require Client Authentication check box at the bottom of this window to enable or disable client authentication for the server. Before you check or uncheck this box, ensure that you select Configure SSL for Server at the top of the window.
>
> Click the Help button at the bottom right corner of the window to access online help.

2. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` file is updated with the following entry:
	```
	SSL_CLIENT_AUTHENTICATION=FALSE
	```

**Parent topic:** Step 1: Configure Transport Layer Security on the Server

##### 22.9.1.6 Step 1F: Set Transport Layer Security as an Authentication Service on the Server (Optional)

The `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file sets the TLS authentication service.

Set this parameter if you want to use TLS authentication in conjunction with another authentication method supported by Oracle Database. For example, use this parameter if you want the server to authenticate itself to the client by using TLS and the client to authenticate itself to the server by using Kerberos.

- To set the `SQLNET.AUTHENTICATION_SERVICES` parameter on the server, add TCP/IP with TLS (TCPS) to this parameter in the `sqlnet.ora` file by using a text editor. For example, if you want to use SSL authentication in conjunction with RADIUS authentication, set this parameter as follows:
	```
	SQLNET.AUTHENTICATION_SERVICES = (TCPS, radius)
	```

If you do not want to use TLS authentication in conjunction with another authentication method, then do not set this parameter.

**Parent topic:** Step 1: Configure Transport Layer Security on the Server

##### 22.9.1.7 Step 1G: Disable SSLv3 on the Server and Client (Optional)

SSLv3 refers to Secure Sockets Layer version 3.

Applications that support Secure Sockets Layer version 3 (SSLv3) are vulnerable to Padding Oracle On Downgraded Legacy Encryption (POODLE) attacks, even if they use the most recent version of Transport Layer Security (TLS). To prevent POODLE attacks, you should set the `ADD_SSLV3_TO_DEFAULT` `sqlnet.ora` parameter to `FALSE` on both the server and the client. `ADD_SSLV3_TO_DEFAULT` only applies if the `SSL_VERSION` parameter is not set. (which means that you are using the default list of SSL versions).

1. Log in to the database server or the client server.
2. Edit the `sqlnet.ora` parameter file, which by default is located in the `$ORACLE_HOME/network/admin` directory, to include the `ADD_SSLV3_TO_DEFAULT` parameter, as follows:
	```
	ADD_SSLV3_TO_DEFAULT=false
	```
	`ADD_SSLV3_TO_DEFAULT` defaults to `FALSE`, and has no effect if `SSL_VERSION` is explicitly set. So, by default, without `SSL_VERSION` explicitly set, SSLv3 connections will not be allowed. Setting `ADD_SSLV3_TO_DEFAULT` to `TRUE` would allow SSLv3 connections to continue working by default.

**Parent topic:** Step 1: Configure Transport Layer Security on the Server

##### 22.9.1.8 Step 1H: Create a Listening Endpoint that Uses TCP/IP with Transport Layer Security on the Server

You can configure a listening endpoint to use TCP/IP with TLS on the server.

- Configure the listener in the `listener.ora` file. Oracle recommends using port number 2484 for typical Oracle Net clients.

##### 22.9.1.9 Step 1I: Restart the Database

To complete the configuration of Transport Layer Security on the server, you must restart the database.

- ```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

**Parent topic:** Step 1: Configure Transport Layer Security on the Server

#### 22.9.2 Step 2: Configure Transport Layer Security on the Client

When you configure SSL on the client, you configure the server DNs and use TCP/IP with TLS on the client.

- Step 2A: Confirm Client Wallet Creation  
	You must confirm that a wallet has been created on the client and that the client has a valid certificate.
- Step 2B: Configure Server DN Matching and Use TCP/IP with TLS on the Client  
	Next, you are ready to configure server DN matching and use TCP/IP with Transport Layer Security (TLS) on the client.
- Step 2C: Specify Required Client TLS Configuration (Wallet Location)  
	You can use Oracle Net Manager to specify the required client TLS configuration.
- Step 2D: Connect to Multiple Databases with Different Certificates from a Single Database Client  
	Optionally, you can configure a client configuration to connect with multiple Oracle Database servers using different certificates and wallets.
- Step 2E: Set the Client Transport Layer Security Cipher Suites (Optional)  
	Optionally, you can set the Transport Layer Security cipher suites. Oracle Database provides default cipher suite settings.
- Step 2F: Set the Required TLS Version on the Client (Optional)  
	The `SSL_VERSION` parameter defines the version of TLS that must run on the systems with which the client communicates.
- Step 2G: Set TLS as an Authentication Service on the Client (Optional)  
	The `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file sets the TLS authentication service.
- Step 2H: Specify the Certificate to Use for Authentication on the Client (Optional)  
	If you have multiple certificates, then you can set the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the `sqlnet.ora` file to specify the correct certificate.
- Step 2I: Check That the Connections Are Using Transport Layer Security  
	You can query the `V$SESSION` and `V$SESSION_CONNECT_INFO` dynamic views to ensure that the client connections are using Transport Layer Security (TLS).
- Step 2I: Restart the Database  
	To complete the configuration of Transport Layer Security on the client, you must restart the database.

**Parent topic:** Transport Layer Security Connection with a Client Wallet

##### 22.9.2.1 Step 2A: Confirm Client Wallet Creation

You must confirm that a wallet has been created on the client and that the client has a valid certificate.

- Use Oracle Wallet Manager to check that the wallet has been created by selecting the Wallet menu, then Open.
	Oracle recommends that you use Oracle Wallet Manager to remove the trusted certificate in your Oracle wallet that is associated with each certificate authority that you do not use. (Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.)

##### 22.9.2.2 Step 2B: Configure Server DN Matching and Use TCP/IP with TLS on the Client

Next, you are ready to configure server DN matching and use TCP/IP with Transport Layer Security (TLS) on the client.

- About Configuring the Server DN Matching and Using TCP/IP with TLS on the Client  
	In addition to validating the server certificate's certificate chain, you can perform an extra check through server DN matching.
- Configuring the Server DN Matching and Using TCP/IP with TLS on the Client  
	You must edit the `tnsnames.ora` and `listener.ora` files to configure the server DN matching and user TCP/IP with TLS on the client.

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

###### 22.9.2.2.1 About Configuring the Server DN Matching and Using TCP/IP with TLS on the Client

In addition to validating the server certificate's certificate chain, you can perform an extra check through server DN matching.

You can configure the Oracle Net Service name to include server DN matching and to use TCP/IP with TLS on the client. To accomplish this, you must specify the server's distinguished name (DN) and `TCPS` as the protocol in the client network configuration files to enable server DN matching and TCP/IP with TLS connections. Server DN matching is optional, but Oracle recommends it because it adds a layer of security to the client: the client can then perform this check against the server.

Due to changes in the CA certificate format where the Organization Unit (`OU`) field will be removed starting in 2022, you may need to update your server certificate DN if you have set `SSL_SERVER_DN_MATCH` to `TRUE`. After you receive the new server certificate with the OU removed from the DN, you must update the client `SSL_SERVER_CERT_DN` parameter to match the new DN.

You can configure either partial DN matching or full DN matching. After you set the `SSL_SERVER_DN_MATCH` parameter to `TRUE`, then partial DN matching is performed automatically. The client will then check the server certificate for the DN information. Full DN matching enables the client to match against the complete DN of the server. If you want to perform a full DN match, then you must specify the server's DN in the `SSL_SERVER_CERT_DN` parameter.

The ability to use either partial or full DN matching enables more flexibility based on how you create and manage host certificates. For example, suppose the client tries to connect to a server with `hostname=finance.us.example.com`. With partial DN matching, the client checks the server's certificate to verify that `CN=finance` is the server's DN. Also for partial DN matching, only the host name (`finance`) is checked, not the fully qualified domain name (`finance.us.example.com`). For both full and partial DN matching, you must set the `SSL_SERVER_DN_MATCH` parameter `TRUE`.

You must manually edit the `tnsnames.ora` client network configuration file to specify the server's DN and the TCP/IP with SSL protocol. The `tnsnames.ora` file can be located on the client or in the LDAP directory. If it is located on the server, then it typically resides in the same directory as the `listener.ora` file. The `tnsnames.ora` file is typically located in the setting specified by the `TNS_ADMIN` environment variable. If `TNS_ADMIN` is not set, then `tnsnames.ora` resides in the following directory locations:

- (UNIX) `$ORACLE_HOME` `/network/admin/`
- (Windows) `ORACLE_BASE` `\` `ORACLE_HOME` `\network\admin\`

**Parent topic:** Step 2B: Configure Server DN Matching and Use TCP/IP with TLS on the Client

###### 22.9.2.2.2 Configuring the Server DN Matching and Using TCP/IP with TLS on the Client

You must edit the `tnsnames.ora` and `listener.ora` files to configure the server DN matching and user TCP/IP with TLS on the client.

1. In the client `tnsnames.ora` file, search for the `SSL_SERVER_CERT_DN` parameter and do the following:
	- If you want to use full DN matching, then set `SSL_SERVER_CERT_DN` to the complete DN, similar to the following:
		```
		(SECURITY=
		(SSL_SERVER_CERT_DN="finance,cn=OracleContext,c=us,o=example"))
		```
		The client uses this information to obtain the list of DNs it expects for each of the servers, enforcing the server's DN to match its service name. The following example shows an entry for the `finance` database in the `tnsnames.ora` file.
		```
		finance=
		(DESCRIPTION=
		(ADDRESS_LIST=
		(ADDRESS= (PROTOCOL = tcps) (HOST = finance) (PORT = 1575)))
		(CONNECT_DATA=
		(SERVICE_NAME= finance.us.example.com))
		(SECURITY=
		(SSL_SERVER_CERT_DN="cn=finance,cn=OracleContext,c=us,o=example"))
		```
		By default, the `tnsnames.ora` and `listener.ora` files are in the `$ORACLE_HOME/network/admin` directory on UNIX systems and in `ORACLE_HOME` `\network\admin` on Windows.
		- If you plan to use partial DN matching, then do not include the `SSL_SERVER_CERT_DN` parameter in `tnsnames.ora`.
2. In the client `tnsnames.ora` file, enter `tcps` as the `PROTOCOL` in the `ADDRESS` parameter.
	This specifies that the client will use TCP/IP with TLS to connect to the database that is identified in the `SERVICE_NAME` parameter. The following also shows an entry that specifies TCP/IP with TLS as the connecting protocol in the `tnsnames.ora` file.
	```
	LISTENER=
	(DESCRIPTION_LIST=
	(DESCRIPTION=
	(ADDRESS= (PROTOCOL = tcps) (HOST = finance) (PORT = 1575))))
	```
3. In the `listener.ora` file, enter `tcps` as the `PROTOCOL` in the `ADDRESS` parameter.

**Parent topic:** Step 2B: Configure Server DN Matching and Use TCP/IP with TLS on the Client

##### 22.9.2.3 Step 2C: Specify Required Client TLS Configuration (Wallet Location)

You can use Oracle Net Manager to specify the required client TLS configuration.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab.
5. Select Configure SSL for: Client.
	![ssl0001](img/ssl0001.gif)

> This is a text description of ssl0001.gif, which is an image of the SSL tab in the Oracle Advanced Security profile region of Oracle Net Manager when Configure SSL for the client is selected.
>
> This window has the following fields which you can use to configure SSL on your client:
>
> - Wallet Configuration Method (by default this is set to File System)
> - Wallet Directory (enter the path to the wallet directory--you can choose Browse if you need to browse the file system)
> - Configure SSL for: (choose Client)
> - Cipher Suite Configuration (select a cipher suite and then click an up or down arrow at the right to change the precedence of when it is applied)
> - Add or Remove (under the Cipher Suite Configuration list, there are an Add and a Remove button that you can use to add or remove a cipher suite)
> - Revocation Check (choose whether to configure certificate validation)
> - Require SSL Version (choose an SSL version from the list--the default is ANY)
> - Match server X.509 name (choose Yes or No from the list--refer to the surrounding text for information about this field)
>
> Click the Help button at the bottom right corner of the window to access online help.

6. In the Wallet Directory box, enter the directory in which the Oracle wallet is located, or click Browse to find it by searching the file system.
7. From the Match server X.509 name list, select one of the following options:
	- Yes: Requires that the server's distinguished name (DN) match its service name. TLS ensures that the certificate is from the server and connections succeed only if there is a match.
		This check can be made only when RSA ciphers are selected, which is the default setting.
	- No (default): TLS checks for a match between the DN and the service name, but does not enforce it. Connections succeed regardless of the outcome but an error is logged if the match fails.
	- Let Client Decide: Enables the default.
		The following alert is displayed when you select No:
		```
		Security Alert
		Not enforcing the server X.509 name match allows a server to potentially fake its identity. Oracle recommends selecting YES for this option so that connections are refused when there is a mismatch.
		```
8. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` file on the client is updated with the following entries:
	```
	SSL_CLIENT_AUTHENTICATION =TRUE
	wallet_location = 
	 (SOURCE=
	  (METHOD=File)
	  (METHOD_DATA=
	   (DIRECTORY=wallet_location)))
	SSL_SERVER_DN_MATCH=(ON/OFF)
	```

##### 22.9.2.4 Step 2D: Connect to Multiple Databases with Different Certificates from a Single Database Client

Optionally, you can configure a client configuration to connect with multiple Oracle Database servers using different certificates and wallets.

- About Connecting to Multiple Databases with Different Certificates from a Single Database Client  
	This feature enables multi-threaded clients to use multiple wallets that have different certificates for simultaneous Transport Layer Security (TLS) sessions.
- Enabling the Client Connection to Have Distinct TLS Sessions  
	You can configure the `tnsnames.ora` file `WALLET_LOCATION` parameter to enable a client connection to have distinct Transport Layer Security (TLS) sessions.

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

###### 22.9.2.4.1 About Connecting to Multiple Databases with Different Certificates from a Single Database Client

This feature enables multi-threaded clients to use multiple wallets that have different certificates for simultaneous Transport Layer Security (TLS) sessions.

Use this feature if you have a single client that must connect to different Oracle Databases using different wallets and certificates. An example would be for a client that requires access to multiple pluggable databases (PDBs), each with its own identity (certificate). This feature enables you to configure the client to connect to the correct identity for each PDB. After the configuration is complete, multi-threaded clients will be able to access more than one wallet with different certificates in simultaneous TLS sessions.

**Parent topic:** Step 2D: Connect to Multiple Databases with Different Certificates from a Single Database Client

###### 22.9.2.4.2 Enabling the Client Connection to Have Distinct TLS Sessions

You can configure the `tnsnames.ora` file `WALLET_LOCATION` parameter to enable a client connection to have distinct Transport Layer Security (TLS) sessions.

1. Log in to the database server where the PDB is located.
2. Locate the `tnsnames.ora` file.
	By default, the `tnsnames.ora` file is in the `ORACLE_HOME/network/admin` directory. The `tnsnames.ora` file can also be stored in the directory specified by the `TNS_ADMIN` environment variable.
3. Edit the `tnsnames.ora` file to include the `WALLET_LOCATION` parameter.
	For example:
	```
	ssl_certs = 
	    (DESCRIPTION = 
	       (ADDRESS=(PROTOCOL=tcps)(HOST=shobeen.us.example.com) (PORT=1750))
	       (CONNECT_DATA=(SID=hr_pdb)) 
	       (SECURITY=(WALLET_LOCATION=/oracle/wallets/certificates/hr_cert))
	     )
	```
	In this example, `WALLET_LOCATION` points to a directory that contains an TLS certificate called `hr_cert`.
	You can use `WALLET_LOCATION` in both `tnsnames.ora` and `sqlnet.ora`. `WALLET_LOCATION` in `tnsnames.ora` will overide the `WALLET_LOCATION` in `sqlnet.ora` for that `tnsnames.ora` service.
	The following example shows how multiple wallets with certificates can be configured in `tnsnames.ora`. Note that the SIDs and wallet locations are different.
	```
	ssl_certs1 = 
	    (DESCRIPTION = 
	       (ADDRESS=(PROTOCOL=tcps)(HOST=shobeen.us.example.com) (PORT=1750))
	       (CONNECT_DATA=(SID=sales_pdb)) 
	       (SECURITY=(WALLET_LOCATION=/oracle/wallets/certificates/sales_cert))
	     )
	ssl_certs2 = 
	    (DESCRIPTION = 
	       (ADDRESS=(PROTOCOL=tcps)(HOST=shobeen.us.example.com) (PORT=1750))
	       (CONNECT_DATA=(SID=marketing_pdb)) 
	       (SECURITY=(WALLET_LOCATION=/oracle/wallets/certificates/marketing_cert))
	     )
	```

**Parent topic:** Step 2D: Connect to Multiple Databases with Different Certificates from a Single Database Client

##### 22.9.2.5 Step 2E: Set the Client Transport Layer Security Cipher Suites (Optional)

Optionally, you can set the Transport Layer Security cipher suites. Oracle Database provides default cipher suite settings.

- About Setting the Client Transport Layer Security Cipher Suites  
	A cipher suite is a set of authentication, encryption, and data integrity algorithms used for exchanging messages between network entities.
- Setting the Client Transport Layer Security Cipher Suites  
	You can use Oracle Net Manager to set the client TLS cipher suites.

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

###### 22.9.2.5.1 About Setting the Client Transport Layer Security Cipher Suites

A cipher suite is a set of authentication, encryption, and data integrity algorithms used for exchanging messages between network entities.

During an SSL handshake, two entities negotiate to see which cipher suite they will use when transmitting messages back and forth.

When you install Oracle Database, the TLS cipher suites are set for you by default. This table lists them in the order they are tried when two entities are negotiating a connection. You can override the default by setting the `SSL_CIPHER_SUITES` parameter. For example, if you use Oracle Net Manager to add the cipher suite `SSL_RSA_WITH_RC4_128_SHA`, all other cipher suites in the default setting are ignored.

You can prioritize the cipher suites. When the client negotiates with servers regarding which cipher suite to use, it follows the prioritization you set. When you prioritize the cipher suites, consider the following:

- The level of security you want to use. For example, AES encryption is stronger than DES.
- The impact on performance. For example, triple-DES encryption is slower than DES.
- Administrative requirements. The cipher suites selected for a client must be compatible with those required by the server. For example, in the case of an Oracle Call Interface (OCI) user, the server requires the client to authenticate itself. You cannot, in this case, use a cipher suite employing Diffie-Hellman anonymous authentication, which disallows the exchange of certificates.

You typically prioritize cipher suites starting with the strongest and moving to the weakest.

The currently supported Transport Layer Security cipher suites are set by default when you install Oracle Database. The table also lists the authentication, encryption, and data integrity types each cipher suite uses.

Note:

If the `SSL_CLIENT_AUTHENTICATION` parameter is set to `true` in the `sqlnet.ora` file, then disable all cipher suites that use Diffie-Hellman anonymous authentication. Otherwise, the connection fails.

###### 22.9.2.5.2 Setting the Client Transport Layer Security Cipher Suites

You can use Oracle Net Manager to set the client TLS cipher suites.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab.
5. In the Cipher Suite Configuration region, click Add.
	A dialog box displays available cipher suites.
6. Select a suite and click OK.
	The Cipher Suite Configuration list is updated as shown as follows:
	![ssl0003](img/ssl0003.gif)

> This is a text description of ssl0003.gif, which is an image of the SSL tab in the Oracle Advanced Security profile region of Oracle Net Manager.
>
> This window has a Cipher Suite Configuraton region where you can prioritize the cipher suites by clicking an up or a down arrow on the right side of the cipher suite list. Click a cipher suite to select it, then click the up or the down arrow to determine which cipher suite is applied first.
>
> Click the Help button at the bottom right corner of the window to access online help.

7. Use the up and down arrows to prioritize the cipher suites.
8. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` file is updated with the following entry:
	```
	SSL_CIPHER_SUITES= (SSL_cipher_suite1 [,SSL_cipher_suite2])
	```

**Parent topic:** Step 2E: Set the Client Transport Layer Security Cipher Suites (Optional)

##### 22.9.2.6 Step 2F: Set the Required TLS Version on the Client (Optional)

The `SSL_VERSION` parameter defines the version of TLS that must run on the systems with which the client communicates.

You must set the `SSL_VERSION` parameter in the `sqlnet.ora` file. You can require these systems to use any valid version.

The default setting for this parameter in `sqlnet.ora` is `undetermined`, which is set by selecting Any from the list in the SSL tab of the Network Security window. When Any is selected, TLS versions will be tried from higher version to lower version. TLS 1.2 first, TLS 1.1, then TLS 1.0.

In accordance with security best practices, Oracle has deprecated the use of TLS 1.0 and TLS 1.1. To meet your security requirements, Oracle strongly recommends that you use TLS 1.2 instead.

1. In the Require SSL Version list, select the TLS version that you want to configure.
	The default setting is Any.
2. From the File menu, select, Save Network Configuration.
	The `sqlnet.ora` file is updated. If you selected Any, then it is updated with the following entry:
	```
	SSL_VERSION=UNDETERMINED
	```

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

##### 22.9.2.7 Step 2G: Set TLS as an Authentication Service on the Client (Optional)

The `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file sets the TLS authentication service.

- About the SQLNET.AUTHENTICATION\_SERVICES Parameter  
	The `SQLNET.AUTHENTICATION_SERVICES` parameter enables TLS authentication in conjunction with another authentication method supported by Oracle Database.
- Setting the SQLNET.AUTHENTICATION\_SERVICES Parameter  
	You can set the `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file.

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

###### 22.9.2.7.1 About the SQLNET.AUTHENTICATION\_SERVICES Parameter

The `SQLNET.AUTHENTICATION_SERVICES` parameter enables TLS authentication in conjunction with another authentication method supported by Oracle Database.

For example, use this parameter if you want the server to authenticate itself to the client by using TLS and the client to authenticate itself to the server by using RADIUS.

To set the `SQLNET.AUTHENTICATION_SERVICES` parameter, you must edit the `sqlnet.ora` file, which is located in the same directory as the other network configuration files.

Depending on the platform, the `sqlnet.ora` file is in the following directory location:

- (UNIX) `$ORACLE_HOME` `/network/admin`
- (Windows) `ORACLE_BASE` `\` `ORACLE_HOME` `\network\admin\`

**Parent topic:** Step 2G: Set TLS as an Authentication Service on the Client (Optional)

###### 22.9.2.7.2 Setting the SQLNET.AUTHENTICATION\_SERVICES Parameter

You can set the `SQLNET.AUTHENTICATION_SERVICES` parameter in the `sqlnet.ora` file.

- To set the client `SQLNET.AUTHENTICATION_SERVICES` parameter, add TCP/IP with TLS (`TCPS`) to this parameter in the `sqlnet.ora` file by using a text editor.
	For example, if you want to use TLS authentication in conjunction with RADIUS authentication, then set this parameter as follows:
	```
	SQLNET.AUTHENTICATION_SERVICES = (TCPS, radius)
	```

If you do not want to use TLS authentication in conjunction with another authentication method, then do not set this parameter.

**Parent topic:** Step 2G: Set TLS as an Authentication Service on the Client (Optional)

##### 22.9.2.8 Step 2H: Specify the Certificate to Use for Authentication on the Client (Optional)

If you have multiple certificates, then you can set the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the `sqlnet.ora` file to specify the correct certificate.

- About the SQLNET.SSL\_EXTENDED\_KEY\_USAGE Parameter  
	The `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the sqlnet.ora file specifies which certificate to use in authenticating to the database server
- Setting the SQLNET.SSL\_EXTENDED\_KEY\_USAGE Parameter  
	You can set the `SQLNET.SSL_EXTENDED_KEY_USAGE` to set the client authentication.

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

###### 22.9.2.8.1 About the SQLNET.SSL\_EXTENDED\_KEY\_USAGE Parameter

The `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the sqlnet.ora file specifies which certificate to use in authenticating to the database server

You should set the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter if you have multiple certificates in the security module, but there is only one certificate with extended key usage field of `client authentication`, and this certificate is exactly the one you want to use to authenticate to the database.

For example, use this parameter if you have multiple certificates in a smart card, only one of which has an extended key usage field of `client authentication`, and you want to use this certificate `C` to authenticate to the database. By setting this parameter on a Windows client to `client authentication`, the MSCAPI certificate selection box will not appear, and the certificate `C` is automatically used for the Transport Layer Security authentication of the client to the server.

**Parent topic:** Step 2H: Specify the Certificate to Use for Authentication on the Client (Optional)

###### 22.9.2.8.2 Setting the SQLNET.SSL\_EXTENDED\_KEY\_USAGE Parameter

You can set the `SQLNET.SSL_EXTENDED_KEY_USAGE` to set the client authentication.

- To set the client `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter, edit the `sqlnet.ora` file to have the following line:
	```
	SQLNET.SSL_EXTENDED_KEY_USAGE = "client authentication"
	```

If you do not want to use the certificate filtering, then remove the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter setting from the `sqlnet.ora` file.

**Parent topic:** Step 2H: Specify the Certificate to Use for Authentication on the Client (Optional)

##### 22.9.2.9 Step 2I: Check That the Connections Are Using Transport Layer Security

You can query the `V$SESSION` and `V$SESSION_CONNECT_INFO` dynamic views to ensure that the client connections are using Transport Layer Security (TLS).

- In SQL\*Plus, perform the following query.
	```
	SELECT SYS_CONTEXT ('USERENV', 'NETWORK_PROTOCOL') FROM DUAL;
	```
	Output similar to the following should appear:
	```
	SYS_CONTEXT('USERENV','NETWORK_PROTOCOL')
	-------------------------------------------------------------------
	tcps
	```

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

##### 22.9.2.10 Step 2I: Restart the Database

To complete the configuration of Transport Layer Security on the client, you must restart the database.

- ```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

**Parent topic:** Step 2: Configure Transport Layer Security on the Client

#### 22.9.3 Step 3: Log in to the Database Instance

After you have completed the configuration, you are ready to log in to the database.

- Start SQL\*Plus and then enter one of the following connection commands:
	- If you are using Transport Layer Security authentication for the client (`SSL_CLIENT_AUTHENTICATION=true` in the `sqlnet.ora` file):
		```
		CONNECT/@net_service_name
		```
		- If you are not using Transport Layer Security authentication (`SSL_CLIENT_AUTHENTICATION=false` in the `sqlnet.ora` file):
		```
		CONNECT username@net_service_name
		Enter password: password
		```

### 22.10 Transport Layer Security Connections in an Oracle Real Application Clusters Environment

You can configure Transport Layer Security (TLS) connections in an Oracle Real Application Clusters (Oracle RAC) environment by using Oracle RAC tools and modifying Oracle Database configuration files.

- Step 1: Configure TCPS Protocol Endpoints  
	In Oracle Real Application Clusters (Oracle RAC), clients access one of three scan listeners and are then routed to database listeners. To support Transport Layer Security (TLS), all of these listeners must have TCPS protocol endpoints.
- Step 2: Ensure That the LOCAL\_LISTENER Parameter Is Correctly Set on Each Node  
	The Oracle Agent automatically sets the `LOCAL_LISTENER` parameter on each node, but you should double-check to ensure that it is correct.
- Step 3: Create Transport Layer Security Wallets and Certificates  
	You must create Transport Layer Security (TLS) wallets and certificates for the cluster and also for clients that will connect to the cluster over TLS.
- Step 4: Create a Wallet in Each Node of the Oracle RAC Cluster  
	After you have created the cluster wallet, you can copy it to each node of the Oracle Real Applications (Oracle RAC) cluster.
- Step 5: Define Wallet Locations in the listener.ora and sqlnet.ora Files  
	To enable the database server and listeners to access the wallets, you must define the wallet locations in the `listener.ora` and `sqlnet.ora` files.
- Step 6: Restart the Database Instances and Listeners  
	With the wallets in place and the `*.ora` files edited, you must restart the database server and listener processes so that they pick up the new settings.
- Step 7: Test the Cluster Node Configuration  
	To test the cluster node configuration, you can create a connect descriptor for the node and then try to connect to this node.
- Step 8: Test the Remote Client Configuration  
	After you have tested the wallet on the Oracle Real Applications (Oracle RAC) cluster nodes, you area ready to test the remote client configuration.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.10.1 Step 1: Configure TCPS Protocol Endpoints

In Oracle Real Application Clusters (Oracle RAC), clients access one of three scan listeners and are then routed to database listeners. To support Transport Layer Security (TLS), all of these listeners must have TCPS protocol endpoints.

1. Log in to the cluster that hosts the Oracle RAC database.
2. Check the listener resources to find if they support TCP endpoints.
	For example:
	```
	$ srvctl config listener -h
	```
	Output similar to the following appears:
	```
	Name: LISTENER
	Subnet: 192.0.2.195
	Type: type
	Owner: pfitch
	Home: Grid_home
	End points: TCP:1521
	```
	The following command displays information about the scan listener:
	```
	$ srvctl config scan_listener -h
	```
	Output similar to the following appears:
	```
	SCAN Listener LISTENER_SCAN1 exists. Port: TCP:1529
	Registration invited nodes:
	Registration invited subnets:
	SCAN Listener is enabled.
	SCAN Listener is individually enabled on nodes:
	SCAN Listener is individually disabled on nodes:
	```
3. Add TCPS endpoints to the database listeners.
	For example:
	```
	$ srvctl modify listener -endpoints "TCP:port_1/TCPS:port_2"
	```
4. ```
	$ srvctl config listener
	Name: LISTENER
	Network: 1, Owner: oracle
	Home: CRS_home
	End points: TCP:port_1/TCPS:port_2
	$ lsnrctl status
	Listening Endpoints Summary...
	(DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=LISTENER)))
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=IP_address)(PORT=port_2)))
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=IP_address)(PORT=port_1)))
	```
5. Add TCPS endpoints to the scan listeners.
	For example:
	```
	$ srvctl modify scan_listener -endpoints "TCP:port_1/TCPS:port_2"
	```
6. For example:
	```
	$ srvctl config scan_listener
	SCAN Listener LISTENER_SCAN1 exists. Port: TCP:port_1/TCPS:port_2
	SCAN Listener LISTENER_SCAN2 exists. Port: TCP:port_1/TCPS:port_2
	SCAN Listener LISTENER_SCAN3 exists. Port: TCP:port_1/TCPS:port_2
	$ lsnrctl status listener_scan3
	Listening Endpoints Summary...
	(DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=LISTENER_SCAN3)))
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=IP_address)(PORT=port_1)))
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=IP_address)(PORT=port_2)))
	```

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

#### 22.10.2 Step 2: Ensure That the LOCAL\_LISTENER Parameter Is Correctly Set on Each Node

The Oracle Agent automatically sets the `LOCAL_LISTENER` parameter on each node, but you should double-check to ensure that it is correct.

1. Log in any Oracle Real Application Clusters (Oracle RAC) node.
2. In SQL\*Plus, as a user with the `SYSDBA` administrative privilege, check the `LOCAL_LISTENER` parameter.
	```
	show parameter local_listener;
	```
	Output similar to the following appears:
	```
	NAME                                 TYPE        VALUE
	------------------------------------ ----------- ------------------------------
	local_listener                       string      (DESCRIPTION=(ADDRESS_LIST=
	                                                 (ADDRESS=(PROTOCOL=TCPS)(HOST=IP_address)
	                                                 (PORT=port_2))))
	```
3. If the output is not what you want, then restart each Oracle RAC instance.

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

#### 22.10.3 Step 3: Create Transport Layer Security Wallets and Certificates

You must create Transport Layer Security (TLS) wallets and certificates for the cluster and also for clients that will connect to the cluster over TLS.

- Oracle Real Application Clusters Components That Need Certificates  
	Specific components in Oracle Real Application Clusters (Oracle RAC) need certificates when you configure Transport Layer Security (TLS) connections.
- Creating Transport Layer Security Wallets and Certificates  
	To create the Transport Layer Security wallets and certificates, you first create the root CA certificate, followed by the cluster and client wallets.

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

##### 22.10.3.1 Oracle Real Application Clusters Components That Need Certificates

Specific components in Oracle Real Application Clusters (Oracle RAC) need certificates when you configure Transport Layer Security (TLS) connections.

- Each cluster node (server) and listener must have a wallet with the user certificate and CA certificates.
- The client only needs CA certificates of the listeners and servers (either in wallet or system’s certificate store) if one-way TLS is configured.
- The client needs a wallet with its user certificate and CA certificates of the listeners and servers if mTLS is configured.

**Parent topic:** Step 3: Create Transport Layer Security Wallets and Certificates

##### 22.10.3.2 Creating Transport Layer Security Wallets and Certificates

To create the Transport Layer Security wallets and certificates, you first create the root CA certificate, followed by the cluster and client wallets.

1. Create the root CA certificate.
	1. Log in to any Oracle Real Application Clusters (Oracle RAC) cluster node.
		2. Use the `orapki` utility to create the CA wallet in a directory for the CA.
		```
		$ orapki wallet create -wallet CA_home_wallet_file_directory
		```
		3. Create a self-signed root certificate for the CA wallet.
		For example:
		```
		$ orapki wallet add -wallet CA_home_wallet_file_directory -self_signed -dn "CN=test CA,O=test,C=c" -keysize 2048 -validity 3650 -sign_alg sha256
		Enter wallet password: password
		```
		4. Extract the root CA certificate from the wallet.
		This root certificate will be used as the trusted CA certificate in cluster and client wallets and can be distributed or published for users who are building PKCS#12 wallets. For example:
		```
		$ orapki wallet export -wallet CA_home_wallet_file_directory -dn "CN=test CA,O=test,C=c" -cert testCAroot.cer
		Enter wallet password: password
		```
		At this stage, the `CA_home_wallet_file_directory` directory will contain the new wallet (`ewallet.p12`) and certificate (`testCAroot.cer`).
		To check the configuration:
		```
		$ orapki wallet display -wallet CA_home_wallet_file_directory -summary
		```
		Output similar to the following appears:
		```
		Requested Certificates:
		User Certificates:
		Subject:        CN=test CA,O=test,C=c
		Trusted Certificates:
		Subject:        CN=test CA,O=test,C=c
		```
2. Create the cluster wallet.
	Next, you are ready follow the remaining steps in this procedure to sign the user certificate requests and provide authorized digital user certificates for different entities and processes in your environments. Repeat this process for each entity in the test environment that participates in the public key infrastructure functionality. A valid wallet consists of a root CA certificate and the signed user certificate.
	1. Create a wallet that is in a different location from the from the CA home directory.
		For example:
		```
		$ orapki wallet create -wallet cluster_wallet_file_directory
		Enter password: password
		Enter password again: password
		```
		2. Create a user identity (user `dn`) and then a certificate request.
		For example:
		```
		$ orapki wallet add -wallet cluster_wallet_file_directory -dn "CN=testuser" -keysize 2048
		Enter wallet password: password
		$ orapki wallet export -wallet cluster_wallet_file_directory -dn "CN=testuser" -request cluster_wallet_file_directory/testuser.req
		Enter wallet password: password
		```
		At this stage, the `cluster_wallet_file_directory` directory will contain the SSO wallet (`cwallet.sso`), the wallet (`ewallet.p12`) and the certificate request (`testuser.req`). The certificate request can be signed by the CA generated above.
		For example:
		```
		$ orapki cert create -wallet cluster_wallet_file_directory -request cluster_wallet_file_directory/testuser.req -cert user_wallet_file_directory/testuser.cer -validity 3650 -sign_alg sha256
		Enter wallet password: password
		```
		The `cluster_wallet_file_directory` directory now has the `testuser.req` certificate request file.
		3. Import the root certificate (`testCAroot.cer`) and the signed user certificate (`testuser.cer`) into the user wallet.
		For example:
		```
		$ orapki wallet add -wallet cluster_wallet_file_directory -trusted_cert -cert CA_home_wallet_file_directory/testCAroot.cer -pwd
		Enter wallet password: user_password
		$ orapki wallet add -wallet cluster_wallet_file_directory -user_cert -cert cluster_wallet_file_directory/testuser.cer
		Enter wallet password: user_password
		```
		4. For example:
		```
		$ orapki wallet display -wallet cluster_wallet_file_directory -summary
		Requested Certificates:
		User Certificates:
		Subject:        CN=testuser
		Trusted Certificates:
		Subject:        CN=test CA,O=test,C=c
		```
		At this point, you are ready to copy the finished cluster wallet to each node of the cluster.
3. Create the client wallet.
	1. Create a client wallet with the root certificate (`testCAroot.cer`).
		To make a successful TLS connection, the client only requires the CA certificates of the server's certificate.
		For example:
		```
		$ orapki wallet create -wallet client_wallet_file_directory -auto_login
		$ orapki wallet add -wallet client_wallet_file_directory -trusted_cert -cert CA_home_wallet_file_directory/testCAroot.cer
		```
		2. For example:
		```
		$ orapki wallet display -wallet client_wallet_file_directory -summary
		Requested Certificates:
		User Certificates:
		Trusted Certificates:
		Subject:        CN=test CA,O=test,C=c
		```

**Parent topic:** Step 3: Create Transport Layer Security Wallets and Certificates

#### 22.10.4 Step 4: Create a Wallet in Each Node of the Oracle RAC Cluster

After you have created the cluster wallet, you can copy it to each node of the Oracle Real Applications (Oracle RAC) cluster.

Ensure that each node is accessible by both the Oracle Real Application Clusters (Oracle RAC) database server (process monitor) and by the scan and local listeners that normally run from the GI home.

1. Copy the PKCS#12 wallet (`ewallet.p12`) file that you created in the previous section to each node in the cluster.
2. In each node, create an auto-login wallet (`cwallet.sso`).
	The `cwallet.sso` file is an obfuscated mirror copy of the `ewallet.p12` and is the file that the database server and its listeners accesses. If you create the `cwallet.sso` on the Oracle RAC cluster, then you can copy it along with the `ewallet.p12` file to the wallet directory on each node. You can also create the `cwallet.sso` file on each node separately if `ewallet.p12` file is already in place. Run the following command in the same location as the `ewallet.p12` file:
	```
	$ orapki wallet create -wallet wallet_file_location -auto_login
	Enter wallet password: ewallet_password
	```

#### 22.10.5 Step 5: Define Wallet Locations in the listener.ora and sqlnet.ora Files

To enable the database server and listeners to access the wallets, you must define the wallet locations in the `listener.ora` and `sqlnet.ora` files.

1. Modify the `listener.ora` file in the Grid home of every node.
	```
	SSL_CLIENT_AUTHENTICATION = FALSE
	WALLET_LOCATION =
	  (SOURCE =
	    (METHOD = FILE)
	    (METHOD_DATA =
	      (DIRECTORY = wallet_file_location)
	```
2. In the `sqlnet.ora` file in the Oracle Database home, and the Grid home, of each cluster node, add the following information:
	```
	SQLNET.AUTHENTICATION_SERVICES = (BEQ, TCP, TCPS)
	SSL_CLIENT_AUTHENTICATION = FALSE
	WALLET_LOCATION =
	  (SOURCE =
	    (METHOD = FILE)
	    (METHOD_DATA =
	      (DIRECTORY = wallet_file_location)
	    )
	  )
	```

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

#### 22.10.6 Step 6: Restart the Database Instances and Listeners

With the wallets in place and the `*.ora` files edited, you must restart the database server and listener processes so that they pick up the new settings.

The restart process will also enable the Oracle Real Application Clusters (Oracle RAC) instances where you set the `LOCAL_LISTENER` parameter earlier.

- In any cluster node, use the `srvctl` utility to restart the database server and listener processes.
	For example:
	```
	$ srvctl stop listener
	$ srvctl start listener
	$ srvctl stop scan_listener
	$ srvctl start scan_listener
	$ srvctl stop database -d db_name 
	$ srvctl start database -d db_name
	```

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

#### 22.10.7 Step 7: Test the Cluster Node Configuration

To test the cluster node configuration, you can create a connect descriptor for the node and then try to connect to this node.

1. In any cluster node, create a connect descriptor in the `tnsnames.ora` file that uses the scan listener TCPS endpoint.
	For example, for a TCPS endpoint called `dbssl`:
	```
	DBSSL =
	  (DESCRIPTION =
	    (ADDRESS = (PROTOCOL = TCPS)(HOST = scan_name)(PORT = port_2))
	    (CONNECT_DATA =
	      (SERVER = DEDICATED)
	      (SERVICE_NAME = service_name)
	    )
	  )
	```
2. Use SQL\*Plus to try to connect to this TCPS endpoint.
	For example:
	```
	sqlplus user_name/@dbssl
	Enter password: password
	```

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

#### 22.10.8 Step 8: Test the Remote Client Configuration

After you have tested the wallet on the Oracle Real Applications (Oracle RAC) cluster nodes, you area ready to test the remote client configuration.

1. In every remote client `sqlnet.ora` file on the cluster node, define a wallet directory.
	```
	WALLET_LOCATION =
	  (SOURCE =
	    (METHOD = FILE)
	    (METHOD_DATA =
	      (DIRECTORY = wallet_file_location)
	    )
	  )
	```
2. Move the client wallet that you created earlier, when you created the SSL wallets and certificates, to the client wallet directory.
	```
	$ wallet create -wallet wallet_file_location -auto_login
	Enter wallet password: password
	```
	The `wallet_file_location` should have an `ewallet.p12` file and a `cwallet.sso` file.
3. In the `tnsnames.ora` file, create a connect descriptor that uses the scan listener TCPS endpoint.
	For example:
	```
	DBSSL =
	  (DESCRIPTION =
	    (ADDRESS = (PROTOCOL = TCPS)(HOST = scan_name)(PORT = port_2))
	    (CONNECT_DATA =
	      (SERVER = DEDICATED)
	      (SERVICE_NAME = service_name)
	    )
	  )
	```
4. Use SQL\*Plus to try to connect to this TCPS endpoint.
	For example:
	```
	sqlplus user_name/@dbssl
	Enter password: password
	```

**Parent topic:** Transport Layer Security Connections in an Oracle Real Application Clusters Environment

### 22.11 Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

To perform this configuration with Microsoft Certificate Store (MCS), you use the `orapki` command-line tool to generate certificates and manipulate the Oracle wallets.

- About Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store  
	This type of configuration is the foundation of the Common Access Cards and PIV cards authentication.
- Step 1: Create and Configure the Server Wallet  
	You must use `orapki` to create a server wallet and the server's self-signed certificate.
- Step 2: Create and Configure the Client Wallet  
	You must use `orapki` to create a client wallet and a certificate request.
- Step 3: Create an External User in the Oracle Database  
	You must create an external user to be used with the client and server connection.
- Step 4: Configure the Server listener.ora File  
	Next, you must check and then restart the server `listener.ora` file.
- Step 5: Configure the Server sqlnet.ora File  
	You must ensure that the `sqlnet.ora` file points to the server wallet that you created earlier.
- Step 6: Import the Client Wallet into the Microsoft Certificate Store  
	You must use the Microsoft Management Console (MMC) to perform this import operation.
- Step 7: Configure the Client sqlnet.ora File  
	You must configure the client `sqlnet.ora` file to use Microsoft Certificate Store for the client wallet.
- Step 8: Configure the Oracle Database  
	In the Oracle database, configure the `OS_AUTHENT_PRE` and `REMOTE_OS_AUTH` parameters.
- Step 9: Test the Client and Server Connection  
	After you complete the Microsoft Certificate Store configuration, you should test the and server connection.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.11.1 About Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

This type of configuration is the foundation of the Common Access Cards and PIV cards authentication.

As long as the software libraries that are delivered with the Common Access Cards and PIV cards are capable of transparently loading the necessary certificates into the Microsoft Certificate Store, then the Transport Layer Security (TLS) authentication that you configure will be transparently performed.

It is important to note that all the signing certificates of the user certificate that is loaded to the PIV card must be manually loaded into the server's wallet as part of the TLS configuration at the server level.

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.2 Step 1: Create and Configure the Server Wallet

You must use `orapki` to create a server wallet and the server's self-signed certificate.

1. Log in to the Oracle Database server.
2. Create a directory for the server wallet.
	For example:
	```
	mkdir /home/oracle/wallet_tls/server
	```
3. ```
	cd /home/oracle/wallet_tls/server
	```
4. ```
	orapki wallet create -wallet . -auto_login -pwd password
	```
5. For example:
	```
	ls -la
	```
	Output similar to the following appears:
	```
	total 16
	drwxr-xr-x. 2 oracle oinstall 4096 Oct 28 07:18 .
	drwxr-xr-x. 6 oracle oinstall 4096 Oct 28 07:17 ..
	-rw-------. 1 oracle oinstall 120 Oct 28 07:18 cwallet.sso
	-rw-rw-rw-. 1 oracle oinstall 0 Oct 28 07:18 cwallet.sso.lck
	-rw-------. 1 oracle oinstall 75 Oct 28 07:18 ewallet.p12
	-rw-rw-rw-. 1 oracle oinstall 0 Oct 28 07:18 ewallet.p12.lck
	```
6. ```
	orapki wallet add -wallet . -dn "cn=server" -self_signed -keysize 2048 -sign_alg sha256 -validity 365 -pwd password
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.3 Step 2: Create and Configure the Client Wallet

You must use `orapki` to create a client wallet and a certificate request.

1. Log in to the Oracle Database client.
2. Create a directory for the client wallet.
	For example:
	```
	mkdir /home/oracle/wallet_tls/client
	```
3. ```
	cd /home/oracle/wallet_tls/client
	```
4. ```
	orapki wallet create -wallet . -auto_login -pwd password
	```
5. Create a request for a user certificate and export the request.
	```
	orapki wallet add -wallet . -dn "cn=client" -keysize 2048 -sign_alg sha256 -pwd password
	orapki wallet export -wallet . -dn "cn=client" -request req.txt -pwd password
	```
6. Copy the certificate request from the client directory to the server directory.
	For example:
	```
	cp req.txt ../server/
	cd ../server/
	```
7. Sign the certificate of the client and also export server's CA certificate.
	For example:
	```
	orapki cert create -wallet . -request req.txt -cert sign.txt -validity 1000 -pwd password
	orapki wallet export -wallet . -dn "cn=server" -cert server.txt
	cp server.txt ../client
	cp sign.txt ../client
	orapki wallet add -wallet . -trusted_cert -cert server.txt -pwd password
	orapki wallet add -wallet . -user_cert -cert sign.txt -pwd password
	cp sign.txt server.txt ../client/
	cd ../client
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.4 Step 3: Create an External User in the Oracle Database

You must create an external user to be used with the client and server connection.

1. As a user who can create users and grant them privileges, log in to the PDB that will use this external user account.
2. For example:
	```
	CREATE USER tlsuser IDENTIFIED EXTERNALLY AS 'cn=client';
	```
3. Grant this account the `CONNECT` privilege.
	```
	GRANT CONNECT TO tlsuser;
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.5 Step 4: Configure the Server listener.ora File

Next, you must check and then restart the server `listener.ora` file.

1. Log in to the Oracle Database server.
2. Check the server `listener.ora` file to ensure that it is correctly configured.
	For example:
	```
	cat /u01/app/oracle/product/release/dbhome_1/network/admin/listener.or
	```
	Output similar to the following appears:
	```
	LISTENERBOS =
	     (DESCRIPTION_LIST =
	       (DESCRIPTION =
	         (ADDRESS = (PROTOCOL = TCP)(HOST = domain.com)(PORT = 1529))
	        )
	       (DESCRIPTION =
	         (ADDRESS = (PROTOCOL = TCPS)(HOST = domain.com)(PORT = 1530))
	         )
	       )
	WALLET_LOCATION =
	      (SOURCE =
	        (METHOD = File)
	          (METHOD_DATA =
	           (DIRECTORY = /home/oracle/wallet_tls/server))
	```
3. Restart the listener and check if the database is registered to this listener.
	```
	su - oracle
	./lsnrctl start
	```
	Output similar to the following appears:
	```
	Listener Parameter File /u01/app/oracle/product/release/dbhome_1/network/admin/listener.ora
	Listener Log File /u01/app/oracle/diag/tnslsnr/service/instance/alert/log.xml
	Listening Endpoints Summary...
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=domain.com)(PORT=1523)))
	(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=domain.com)(PORT=1525)))
	  Services Summary...
	   Service "service" has 1 instance(s).
	    Instance "instance", status READY, has 1 handler(s) for this service...
	   Service "serviceDB" has 1 instance(s).
	    Instance "instance", status READY, has 1 handler(s) for this service...
	 The command completed successful
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.6 Step 5: Configure the Server sqlnet.ora File

You must ensure that the `sqlnet.ora` file points to the server wallet that you created earlier.

1. Log in to the Oracle Database server.
2. Check the `sqlnet.ora` file to ensure that it points to the server wallet.
	For example:
	```
	NAMES.DIRECTORY_PATH=(TNSNAMES)
	SQLNET.AUTHENTICATION_SERVICES=(BEQ,TCPS)
	SSL_CLIENT_AUTHENTICATION = TRUE 
	WALLET_LOCATION =
	 (SOURCE =
	  (METHOD = FILE)
	    (METHOD_DATA =
	      (DIRECTORY = /home/oracle/wallet_tls/server)
	    )
	)
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.7 Step 6: Import the Client Wallet into the Microsoft Certificate Store

You must use the Microsoft Management Console (MMC) to perform this import operation.

1. Start the MMC (`mmc.exe`).
2. Select File, then add/remove snap-in.
3. Select Certificates, then Add.
4. Select My user account, then Finish, and then OK.
5. Go to the Console Root, then Certificates Current User, then Personal, then Certificates.
6. Right-click All Tasks, then select Import, then Next, then Browse.
7. Select the certificate file that contains the certificate needed for the connection (for example, `ewallet.p12`).
8. Select Open, then Next.
9. Enter the wallet password.
10. Select the Mark this as exportable checkbox.
11. Select the Include all extended properties checkbox.
12. Select Place all certificates in the following store: Personal.
13. Select Next, then Finish.
14. Ensure that the client's certificate was added to the MY store, by going to Console Root, and then selecting Certificates Current User, then Personal, then Certificates.
15. Ensure that the CA certificates were added to the ROOT store by going to Console Root, and then selecting Certificates Current User, then Trusted Root Certification Authorities, then Certificates.

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.8 Step 7: Configure the Client sqlnet.ora File

You must configure the client `sqlnet.ora` file to use Microsoft Certificate Store for the client wallet.

1. Log in to the Oracle Database client.
2. Check the client side `sqlnet.ora` file.
	For example:
	```
	WALLET_LOCATION = (SOURCE = (METHOD=MCS))
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.9 Step 8: Configure the Oracle Database

In the Oracle database, configure the `OS_AUTHENT_PRE` and `REMOTE_OS_AUTH` parameters.

1. Log in SQL\*Plus on the Oracle Database server as a user who has the `ALTER SYSTEM` system privilege.
2. Set the `OS_AUTHENT_PRE` and `REMOTE_OS_AUTH` parameters.
	```
	ALTER SYSTEM SET REMOTE_OS_AUTHENT=FALSE SCOPE=SPFILE;
	ALTER SYSTEM SET OS_AUTHENT_PREFIX='' SCOPE=SPFILE;
	```
3. Restart the database instance.

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

#### 22.11.10 Step 9: Test the Client and Server Connection

After you complete the Microsoft Certificate Store configuration, you should test the and server connection.

1. To verify that the MCS is used for the TLS connection, enable the client trace by adding the following lines in the client's `sqlnet.ora` file.
	```
	trace_level_client=16
	trace_directory_client=trace_directory
	DIAG_ADR_ENABLED=OFF
	```
2. Make a connection to the server using SQL\*Plus and then ensure that the certificates are loaded successfully from MCS.
	```
	nztwOpenWallet: [enter]
	nztwOpenWallet: WRL mcs:, type = 24
	nztwOpenWallet: Loading the EXTKS provider for MCS type wallet
	nztwOpenWallet: [exit] OK
	```

**Parent topic:** Configuring Transport Layer Security for Client Authentication and Encryption Using Microsoft Certificate Store

### 22.12 Troubleshooting the Transport Layer Security Configuration

Common errors may occur while you use the Oracle Database SSL adapter.

It may be necessary to enable Oracle Net tracing to determine the cause of an error. For information about setting tracing parameters to enable Oracle Net tracing, refer to [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=NETAG429).

ORA-28759: Failure to Open File

Cause: The system could not open the specified file. Typically, this error occurs because the wallet cannot be found.

Action: Check the following:

- Ensure that the correct wallet location is specified in the `sqlnet.ora` file. This should be the same directory location where you saved the wallet.
- Enable Oracle Net tracing to determine the name of the file that cannot be opened and the reason.
- Ensure that auto-login was enabled when you saved the wallet. See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI161).

ORA-28786: Decryption of Encrypted Private Key Failure

Cause: An incorrect password was used to decrypt an encrypted private key. Frequently, this happens because an auto-login wallet is not being used.

Action: Use Oracle Wallet Manager to turn the auto-login feature on for the wallet. Then save the wallet again. See [Oracle Database Enterprise User Security Administrator's Guide.](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI161)

If the auto-login feature is not being used, then enter the correct password.

Note: Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

ORA-28858: SSL Protocol Error

Cause: This is a generic error that can occur during TLS handshake negotiation between two processes.

Action: Enable Oracle Net tracing and attempt the connection again to produce trace output. Then contact Oracle customer support with the trace output.

ORA-28859 SSL Negotiation Failure

Cause: An error occurred during the negotiation between two processes as part of the TLS protocol. This error can occur when two sides of the connection do not support a common cipher suite.

Action: Check the following:

- Use Oracle Net Manager to ensure that the TLS versions on both the client and the server match, or are compatible. For example, if the server accepts only TLS 3.0 and the client accepts only TLS 1.1, then the TLS connection will fail.
- Use Oracle Net Manager to check what cipher suites are configured on the client and the server, and ensure that compatible cipher suites are set on both.
	If the error still persists, then enable Oracle Net tracing and attempt the connection again. Contact Oracle customer support with the trace output.
	See Also:
	Step 2E: Set the Client Transport Layer Security Cipher Suites (Optional) for details about setting compatible cipher suites on the client and the server
	Note:
	If you do not configure any cipher suites, then all available cipher suites are enabled.

ORA-28862: SSL Connection Failed

Cause: This error occurred because the peer closed the connection.

Action: Check the following:

- Ensure that the correct wallet location is specified in the `sqlnet.ora` file so the system can find the wallet.
- Use Oracle Net Manager to ensure that cipher suites are set correctly in the `sqlnet.ora` file. Sometimes this error occurs because the `sqlnet.ora` has been manually edited and the cipher suite names are misspelled. Ensure that case sensitive string matching is used with cipher suite names.
- Use Oracle Net Manager to ensure that the TLS versions on both the client and the server match or are compatible. Sometimes this error occurs because the TLS version specified on the server and client do not match. For example, if the server accepts only TLS 3.0 and the client accepts only TLS 1.0, then the TLS connection will fail.
- For more diagnostic information, enable Oracle Net tracing on the peer.

ORA-28865: SSL Connection Closed

Cause: The TLS connection closed because of an error in the underlying transport layer, or because the peer process quit unexpectedly.

Action: Check the following:

- Use Oracle Net Manager to ensure that the TLS versions on both the client and the server match, or are compatible. Sometimes this error occurs because the TLS version specified on the server and client do not match. For example, if the server accepts only TLS 3.0 and the client accepts only TLS 1.0, then the TLS connection will fail.
- If you are using a Diffie-Hellman anonymous cipher suite and the `SSL_CLIENT_AUTHENTICATION` parameter is set to `true` in the server's `listener.ora` file, then the client does not pass its certificate to the server. When the server does not receive the client's certificate, it (the server) cannot authenticate the client so the connection is closed. To resolve this use another cipher suite, or set this `listener.ora` parameter to false.
- Enable Oracle Net tracing and check the trace output for network errors.

ORA-28868: Peer Certificate Chain Check Failed

Cause: When the peer presented the certificate chain, it was checked and that check failed. This failure can be caused by a number of problems, including:

- One of the certificates in the chain has expired.
- A certificate authority for one of the certificates in the chain is not recognized as a [trust point](glossary.md).
- The signature in one of the certificates cannot be verified.

Action: See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9734) to use Oracle Wallet Manager to open your wallet and check the following:

- Ensure that all of the certificates installed in your wallet are current (not expired).
- Ensure that a certificate authority's certificate from your peer's certificate chain is added as a trusted certificate in your wallet. See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9758) to use Oracle Wallet Manager to import a trusted certificate.

ORA-28885: No certificate with the required key usage found.

Cause: Your certificate was not created with the appropriate X.509 version 3 key usage extension.

Action: Use Oracle Wallet Manager to check the certificate's key usage. See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI10217) for information about key usage values.

ORA-29024: Certificate Validation Failure

Cause: The certificate sent by the other side could not be validated. This may occur if the certificate has expired, has been revoked, or is invalid for any other reason.

Action: Check the following:

- Check the certificate to determine whether it is valid. If necessary, get a new certificate, inform the sender that her certificate has failed, or resend.
- Check to ensure that the server's wallet has the appropriate trust points to validate the client's certificate. If it does not, then use Oracle Wallet Manager to import the appropriate trust point into the wallet. See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9758) for details about importing a trusted certificate.
- Ensure that the certificate has not been revoked and that certificate revocation list (CRL) checking is turned on. For details, refer to Configuring Certificate Validation with Certificate Revocation Lists

ORA-29223: Cannot Create Certificate Chain

Cause: A certificate chain cannot be created with the existing trust points for the certificate being installed. Typically, this error is returned when the peer does not give the complete chain and you do not have the appropriate trust points to complete it.

Action: Use Oracle Wallet Manager to install the trust points that are required to complete the chain. See [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9758) for details about importing a trusted certificate.

**Parent topic:** Configuring Transport Layer Security Authentication

### 22.13 Certificate Validation with Certificate Revocation Lists

Oracle provides tools that enable you to validate certificates using certificate revocation lists.

- About Certificate Validation with Certificate Revocation Lists  
	The process of determining whether a given certificate can be used in a given context is referred to as certificate validation.
- What CRLs Should You Use?  
	You should have CRLs for all of the trust points that you honor.
- How CRL Checking Works  
	Oracle Database checks the certificate revocation status against CRLs.
- Configuring Certificate Validation with Certificate Revocation Lists  
	You can edit the `sqlnet.ora` file to configure certificate validation with certificate revocation lists.
- Certificate Revocation List Management  
	Certificate revocation list management entails ensuring that the CRLs are the correct format before you enable certificate revocation checking.
- Troubleshooting CRL Certificate Validation  
	To determine whether certificates are being validated against CRLs, you can enable Oracle Net tracing.
- Oracle Net Tracing File Error Messages Associated with Certificate Validation  
	Oracle generates trace messages that are relevant to certificate validation.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.13.1 About Certificate Validation with Certificate Revocation Lists

The process of determining whether a given certificate can be used in a given context is referred to as certificate validation.

Certificate validation includes determining that the following takes place:

- A trusted certificate authority (CA) has digitally signed the certificate
- The certificate's digital signature corresponds to the independently-calculated hash value of the certificate itself and the certificate signer's (CA's) public key
- The certificate has not expired
- The certificate has not been revoked

The Transport Layer Security network layer automatically performs the first three validation checks, but you must configure certificate revocation list (CRL) checking to ensure that certificates have not been revoked. CRLs are signed data structures that contain a list of revoked certificates. They are usually issued and signed by the same entity who issued the original certificate.

**Parent topic:** Certificate Validation with Certificate Revocation Lists

#### 22.13.2 What CRLs Should You Use?

You should have CRLs for all of the trust points that you honor.

The trust points are the trusted certificates from a third party identity that is qualified with a level of trust.

Typically, the certificate authorities you trust are called trust points.

**Parent topic:** Certificate Validation with Certificate Revocation Lists

#### 22.13.3 How CRL Checking Works

Oracle Database checks the certificate revocation status against CRLs.

These CRLs are located in file system directories, Oracle Internet Directory, or downloaded from the location specified in the CRL Distribution Point (CRL DP) extension on the certificate.

Typically, CRL definitions are valid for a few days. If you store your CRLs on the local file system or in the directory, then you must update them regularly. If you use a CRL Distribution Point (CRL DP), then CRLs are downloaded each time a certificate is used, so there is no need to regularly refresh the CRLs.

The server searches for CRLs in the following locations in the order listed. When the system finds a CRL that matches the certificate CA's DN, it stops searching.

1. Local file system
	The system checks the `sqlnet.ora` file for the `SSL_CRL_FILE` parameter first, followed by the `SSL_CRL_PATH` parameter. If these two parameters are not specified, then the system checks the wallet location for any CRLs.
	Note: if you store CRLs on your local file system, then you must use the `orapki` utility to periodically update them (for example, renaming CRLs with a hash value for certificate validation).
2. Oracle Internet Directory
	If the server cannot locate the CRL on the local file system and directory connection information has been configured in an `ldap.ora` file, then the server searches in the directory. It searches the CRL subtree by using the CA's distinguished name (DN) and the DN of the CRL subtree.
	The server must have a properly configured `ldap.ora` file to search for CRLs in the directory. It cannot use the Domain Name System (DNS) discovery feature of Oracle Internet Directory. Also note that if you store CRLs in the directory, then you must use the `orapki` utility to periodically update them.
3. CRL DP
	If the CA specifies a location in the CRL DP X.509, version 3, certificate extension when the certificate is issued, then the appropriate CRL that contains revocation information for that certificate is downloaded. Currently, Oracle Database supports downloading CRLs over LDAP.
	Note the following:
	- For performance reasons, only user certificates are checked.
		- Oracle recommends that you store CRLs in the directory rather than the local file system.

#### 22.13.4 Configuring Certificate Validation with Certificate Revocation Lists

You can edit the `sqlnet.ora` file to configure certificate validation with certificate revocation lists.

- About Configuring Certificate Validation with Certificate Revocation Lists  
	The `SSL_CERT_REVOCATION` parameter must be set to `REQUIRED` or `REQUESTED` in the `sqlnet.ora` file to enable certificate revocation status checking.
- Enabling Certificate Revocation Status Checking for the Client or Server  
	You can enable certificate the revocation status checking for a client or a server.
- Disabling Certificate Revocation Status Checking  
	You can disable certificate revocation status checking.

**Parent topic:** Certificate Validation with Certificate Revocation Lists

##### 22.13.4.1 About Configuring Certificate Validation with Certificate Revocation Lists

The `SSL_CERT_REVOCATION` parameter must be set to `REQUIRED` or `REQUESTED` in the `sqlnet.ora` file to enable certificate revocation status checking.

The `SSL_CERT_REVOCATION` parameter must be set to `REQUIRED` or `REQUESTED` in the `sqlnet.ora` file to enable certificate revocation status checking.

By default this parameter is set to `NONE` indicating that certificate revocation status checking is turned off.

Note:

If you want to store CRLs on your local file system or in Oracle Internet Directory, then you must use the command line utility, `orapki`, to rename CRLs in your file system or upload them to the directory.

##### 22.13.4.2 Enabling Certificate Revocation Status Checking for the Client or Server

You can enable certificate the revocation status checking for a client or a server.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab.
5. Select one of the following options from the Revocation Check list:
	![ssl0006](img/ssl0006.gif)

> This is a text description of ssl0006.gif, which is an image of the SSL tab in the Oracle Advanced Security profile region of Oracle Net Manager when Configure SSL for the client is selected.
>
> This window has the following fields which you can use to configure SSL on your server:
>
> - Configure SSL for: (choose either Client or Server)
> - Wallet Directory (enter the path to the wallet directory--you can choose Browse if you need to browse the file system)
> - Cipher Suite Configuration (select a cipher suite and then click an up or down arrow at the right to change the precedence of when it is applied)
> - Add or Remove (under the Cipher Suite Configuration list, there are an Add and a Remove button that you can use to add or remove a cipher suite)
> - Revocation Check (where you can set whether certificate revocation status checking is performed by selecting from None, Required, or Requested from a drop-down list)
> - Certificate Revocation Lists Path (where you can enter a path to the directory where your CRLs are stored)
> - Certificate Revocation Lists File (where you can enter the path to a comprehensive CRL file)
> - Require SSL Version (choose an SSL version from the list--the default is ANY)
> - Match server X.509 name (choose whether you want your system to check the server's distinguished name)
>
> Click the Help button at the bottom left corner of the window to access online help.

	- Required: Requires certificate revocation status checking. The TLS connection is rejected if a certificate is revoked or no CRL is found. TLS connections are accepted only if it can be verified that the certificate has not been revoked.
	- Requested: Performs certificate revocation status checking if a CRL is available. The TLS connection is rejected if a certificate is revoked. TLS connections are accepted if no CRL is found or if the certificate has not been revoked.
		For performance reasons, only user certificates are checked for revocation.
6. (Optional) If CRLs are stored on your local file system, then set one or both of the following fields that specify where they are stored. These fields are available only when Revocation Check is set to Required or REQUESTED.
	- Certificate Revocation Lists Path: Enter the path to the directory where CRLs are stored or click Browse to find it by searching the file system. Specifying this path sets the `SSL_CRL_PATH` parameter in the `sqlnet.ora` file. If a path is not specified for this parameter, then the default is the wallet directory. Both DER-encoded (binary format) and PEM-encoded (BASE64) CRLs are supported.
	- Certificate Revocation Lists File: Enter the path to a comprehensive CRL file (where PEM-encoded (BASE64) CRLs are concatenated in order of preference in one file) or click Browse to find it by searching the file system. Specifying this file sets the `SSL_CRL_FILE` parameter in the `sqlnet.ora` file. If this parameter is set, then the file must be present in the specified location, or else the application will error out during startup.
		If you want to store CRLs in a local file system directory by setting the Certificate Revocation Lists Path, then you must use the `orapki` utility to rename them so the system can locate them.
7. (Optional) If CRLs are fetched from Oracle Internet Directory, then directory server and port information must be specified in an `ldap.ora` file.
	When configuring your `ldap.ora` file, you should specify only a non-TLS port for the directory. CRL download is done as part of the TLS protocol, and making a TLS connection within a TLS connection is not supported.
	Oracle Database CRL functionality will not work if the Oracle Internet Directory non-TLS port is disabled.
8. Select File, Save Network Configuration. The `sqlnet.ora` file is updated.

##### 22.13.4.3 Disabling Certificate Revocation Status Checking

You can disable certificate revocation status checking.

1. Start Oracle Net Manager.
	- (UNIX) From `$ORACLE_HOME` `/bin`, enter the following command at the command line:
		```
		netmgr
		```
	- (Windows) Select Start, Programs, Oracle - HOME\_NAME, Configuration and Migration Tools, then Net Manager.
2. Expand Oracle Net Configuration, and from Local, select Profile.
3. From the Naming list, select Network Security.
	The Network Security tabbed window appears.
4. Select the SSL tab.
5. Select NONE from the Revocation Check list.
6. From the File menu, select Save Network Configuration.
	The `sqlnet.ora` file is updated with the following entry:
	```
	SSL_CERT_REVOCATION=NONE
	```

#### 22.13.5 Certificate Revocation List Management

Certificate revocation list management entails ensuring that the CRLs are the correct format before you enable certificate revocation checking.

- About Certificate Revocation List Management  
	Oracle Database provides a command-line utility, `orapki`, that you can use to manage certificates.
- Displaying orapki Help for Commands That Manage CRLs  
	You can display all the `orapki` commands that are available for managing CRLs.
- Renaming CRLs with a Hash Value for Certificate Validation  
	When the system validates a certificate, it must locate the CRL issued by the CA who created the certificate.
- Uploading CRLs to Oracle Internet Directory  
	Publishing CRLs in the directory enables CRL validation throughout your enterprise, eliminating the need for individual applications to configure their own CRLs.
- Listing CRLs Stored in Oracle Internet Directory  
	You can display a list of all CRLs stored in the directory with `orapki`, which is useful for browsing to locate a particular CRL to view or download to your local computer.
- Viewing CRLs in Oracle Internet Directory  
	Oracle Internet Directory CRLS are available in a summarized format; you also can request a listing of revoked certificates for a CRL.
- Deleting CRLs from Oracle Internet Directory  
	The user who deletes CRLs from the directory by using `orapki` must be a member of the directory group `CRLAdmins`.

**Parent topic:** Certificate Validation with Certificate Revocation Lists

##### 22.13.5.1 About Certificate Revocation List Management

Oracle Database provides a command-line utility, `orapki`, that you can use to manage certificates.

Before you can enable certificate revocation status checking, you must ensure that the CRLs you receive from the CAs you use are in a form (renamed with a hash value) or in a location (uploaded to the directory) where your computer can use them.

You can also use LDAP command-line tools to manage CRLs in Oracle Internet Directory.

Note:

CRLs must be updated at regular intervals (before they expire) for successful validation. You can automate this task by using `orapki` commands in a script

**Parent topic:** Certificate Revocation List Management

##### 22.13.5.2 Displaying orapki Help for Commands That Manage CRLs

You can display all the `orapki` commands that are available for managing CRLs.

- To display all the `orapki` available CRL management commands and their options, enter the following at the command line:
	```
	orapki crl help
	```

Note:

Using the `-summary`, `-complete`, or `-wallet` command options is always optional. A command will still run if these command options are not specified.

**Parent topic:** Certificate Revocation List Management

##### 22.13.5.3 Renaming CRLs with a Hash Value for Certificate Validation

When the system validates a certificate, it must locate the CRL issued by the CA who created the certificate.

The system locates the appropriate CRL by matching the issuer name in the certificate with the issuer name in the CRL.

When you specify a CRL storage location for the Certificate Revocation Lists Path field in Oracle Net Manager, which sets the `SSL_CRL_PATH` parameter in the `sqlnet.ora` file, use the `orapki` utility to rename CRLs with a hash value that represents the issuer's name. Creating the hash value enables the server to load the CRLs.

On UNIX operating systems, `orapki` creates a symbolic link to the CRL. On Windows operating systems, it creates a copy of the CRL file. In either case, the symbolic link or the copy created by `orapki` are named with a hash value of the issuer's name. Then when the system validates a certificate, the same hash function is used to calculate the link (or copy) name so the appropriate CRL can be loaded.

- Depending on the operating system, enter one of the following commands to rename CRLs stored in the file system:
	- To rename CRLs stored in UNIX file systems:
		```
		orapki crl hash -crl crl_filename [-wallet wallet_location] -symlink crl_directory [-summary]
		```
		- To rename CRLs stored in Windows file systems:
		```
		orapki crl hash -crl crl_filename [-wallet wallet_location] -copy crl_directory [-summary]
		```

In this specification, `crl_filename` is the name of the CRL file, `wallet_location` is the location of a wallet that contains the certificate of the CA that issued the CRL, and `crl_directory` is the directory where the CRL is located.

Using `-wallet` and `-summary` are optional. Specifying `-wallet` causes the tool to verify the validity of the CRL against the CA's certificate prior to renaming the CRL. Specifying the `-summary` option causes the tool to display the CRL issuer's name.

**Parent topic:** Certificate Revocation List Management

##### 22.13.5.4 Uploading CRLs to Oracle Internet Directory

Publishing CRLs in the directory enables CRL validation throughout your enterprise, eliminating the need for individual applications to configure their own CRLs.

All applications can use the CRLs stored in the directory where they can be centrally managed, greatly reducing the administrative overhead of CRL management and use. The user who uploads CRLs to the directory by using `orapki` must be a member of the directory group `CRLAdmins` (`cn=CRLAdmins,cn=groups,%s_OracleContextDN%`). This is a privileged operation because these CRLs are accessible to the entire enterprise. Contact your directory administrator to get added to this administrative directory group.

- To upload CRLs to the directory, enter the following at the command line:
	```
	orapki crl upload -crl crl_location -ldap hostname:ssl_port -user username [-wallet wallet_location] [-summary]
	```
	In this specification, `crl_location` is the file name or URL where the CRL is located, `hostname` and `ssl_port` (TLS port with no authentication) are for the system on which your directory is installed, `username` is the directory user who has permission to add CRLs to the CRL subtree, and `wallet_location` is the location of a wallet that contains the certificate of the CA that issued the CRL.

Using `-wallet` and `-summary` are optional. Specifying `-wallet` causes the tool to verify the validity of the CRL against the CA's certificate prior to uploading it to the directory. Specifying the `-summary` option causes the tool to print the CRL issuer's name and the LDAP entry where the CRL is stored in the directory.

The following example illustrates uploading a CRL with the `orapki` utility:

```
orapki crl upload -crl /home/user1/wallet/crldir/crl.txt -ldap host1.example.com:3533 -user cn=orcladmin
```

Note:

- The `orapki` utility will prompt you for the directory password when you perform this operation.
- Ensure that you specify the directory SSL port on which the Diffie-Hellman-based TLS server is running. This is the TLS port that does not perform authentication. Neither the server authentication nor the mutual authentication TLS ports are supported by the `orapki` utility.

**Parent topic:** Certificate Revocation List Management

##### 22.13.5.5 Listing CRLs Stored in Oracle Internet Directory

You can display a list of all CRLs stored in the directory with `orapki`, which is useful for browsing to locate a particular CRL to view or download to your local computer.

This command displays the CA who issued the CRL (Issuer) and its location (DN) in the CRL subtree of your directory.

- To list CRLs in Oracle Internet Directory, enter the following at the command line:
	```
	orapki crl list -ldap hostname:ssl_port
	```
	where the `hostname` and `ssl_port` are for the system on which your directory is installed. Note that this is the directory SSL port with no authentication as described in the preceding section.

**Parent topic:** Certificate Revocation List Management

##### 22.13.5.6 Viewing CRLs in Oracle Internet Directory

Oracle Internet Directory CRLS are available in a summarized format; you also can request a listing of revoked certificates for a CRL.

You can view CRLs stored in Oracle Internet Directory in a summarized format or you can request a complete listing of revoked certificates for a CRL. A summary listing provides the CRL issuer's name and its validity period. A complete listing provides a list of all revoked certificates contained in the CRL.

- To view a summary listing of a CRL in Oracle Internet Directory, enter the following at the command line:
	```
	orapki crl display -crl crl_location [-wallet wallet_location] -summary
	```
	In this specification, `crl_location` is the location of the CRL in the directory. It is convenient to paste the CRL location from the list that displays when you use the `orapki crl list` command.
	To view a list of all revoked certificates contained in a specified CRL, which is stored in Oracle Internet Directory, you can enter the following at the command line:
	```
	orapki crl display -crl crl_location [-wallet wallet_location] -complete
	```
	For example, the following `orapki` command:
	```
	orapki crl display -crl $T_WORK/pki/wlt_crl/nzcrl.txt -wallet $T_WORK/pki/wlt_crl -complete
	```
	produces the following output, which lists the CRL issuer's DN, its publication date, date of its next update, and the revoked certificates it contains:
	```
	issuer = CN=root,C=us, thisUpdate = Sun Nov 16 10:56:58 PST 2003, nextUpdate = Mon Sep 30 11:56:58 PDT 2013, revokedCertificates = {(serialNo = 153328337133459399575438325845117876415, revocationDate - Sun Nov 16 10:56:58 PST 2003)}
	CRL is valid
	```
	Using the `-wallet` option causes the `orapki crl display` command to validate the CRL against the CA's certificate.
	Depending on the size of your CRL, choosing the `-complete` option may take a long time to display.
	You can also use Oracle Directory Manager, a graphical user interface tool that is provided with Oracle Internet Directory, to view CRLs in the directory. CRLs are stored in the following directory location:
	```
	cn=CRLValidation,cn=Validation,cn=PKI,cn=Products,cn=OracleContext
	```

##### 22.13.5.7 Deleting CRLs from Oracle Internet Directory

The user who deletes CRLs from the directory by using `orapki` must be a member of the directory group `CRLAdmins`.

- To delete CRLs from the directory, enter the following at the command line:
	```
	orapki crl delete -issuer issuer_name -ldap host:ssl_port -user username [-summary]
	```
	In this specification, `issuer_name` is the name of the CA who issued the CRL, the `hostname` and `ssl_port` are for the system on which your directory is installed, and `username` is the directory user who has permission to delete CRLs from the CRL subtree. Ensure that this must be a directory SSL port with no authentication.
	Using the `-summary` option causes the tool to print the CRL LDAP entry that was deleted.
	For example, the following `orapki` command:
	```
	orapki crl delete -issuer "CN=root,C=us" -ldap machine1:3500 -user cn=orcladmin -summary
	```
	produces the following output, which lists the location of the deleted CRL in the directory:
	```
	Deleted CRL at cn=root cd45860c.rN,cn=CRLValidation,cn=Validation,cn=PKI,cn=Products,cn=OracleContext
	```

#### 22.13.6 Troubleshooting CRL Certificate Validation

To determine whether certificates are being validated against CRLs, you can enable Oracle Net tracing.

When a revoked certificate is validated by using CRLs, then you will see the following entries in the Oracle Net tracing file without error messages logged between `entry` and `exit`:

```
nzcrlVCS_VerifyCRLSignature: entry
nzcrlVCS_VerifyCRLSignature: exit

nzcrlVCD_VerifyCRLDate: entry
nzcrlVCD_VerifyCRLDate: exit

nzcrlCCS_CheckCertStatus: entry
nzcrlCCS_CheckCertStatus: Certificate is listed in CRL
nzcrlCCS_CheckCertStatus: exit
```

Note:

Note that when certificate validation fails, the peer in the SSL handshake sees an `ORA-29024: Certificate Validation Failure`.

#### 22.13.7 Oracle Net Tracing File Error Messages Associated with Certificate Validation

Oracle generates trace messages that are relevant to certificate validation.

These trace messages may be logged between the `entry` and `exit` entries in the Oracle Net tracing file. Oracle SSL looks for CRLs in multiple locations, so there may be multiple errors in the trace.

You can check the following list of possible error messages for information about how to resolve them.

CRL signature verification failed with RSA status

Cause: The CRL signature cannot be verified.

Action: Ensure that the downloaded CRL is issued by the peer's CA and that the CRL was not corrupted when it was downloaded. Note that the `orapki` utility verifies the CRL before renaming it with a hash value or before uploading it to the directory.

See Certificate Revocation List Management for information about using `orapki` for CRL management.

CRL date verification failed with RSA status

Cause: The current time is later than the time listed in the next update field. You should not see this error if CRL DP is used. The systems searches for the CRL in the following order:

1. File system
2. Oracle Internet Directory
3. CRL DP

The first CRL found in this search may not be the latest.

Action: Update the CRL with the most recent copy.

CRL could not be found

Cause: The CRL could not be found at the configured locations. This will return error ORA-29024 if the configuration specifies that certificate validation is require.

Action: Ensure that the CRL locations specified in the configuration are correct by performing the following steps:

1. Use Oracle Net Manager to check if the correct CRL location is configured. Refer to Configuring Certificate Validation with Certificate Revocation Lists
2. If necessary, use the `orapki` utility to configure CRLs for system use as follows:
	- For CRLs stored on your local file system, refer to Renaming CRLs with a Hash Value for Certificate Validation
		- CRLs stored in the directory, refer to Uploading CRLs to Oracle Internet Directory

Oracle Internet Directory host name or port number not set

Cause: Oracle Internet Directory connection information is not set. Note that this is not a fatal error. The search continues with CRL DP.

Action: If you want to store the CRLs in Oracle Internet Directory, then use Oracle Net Configuration Assistant to create and configure an `ldap.ora` file for your Oracle home.

Fetch CRL from CRL DP: No CRLs found

Cause: The CRL could not be fetched by using the CRL Distribution Point (CRL DP). This happens if the certificate does not have a location specified in its CRL DP extension, or if the URL specified in the CRL DP extension is incorrect.

Action: Ensure that your certificate authority publishes the CRL to the URL that is specified in the certificate's CRL DP extension.

Manually download the CRL. Then depending on whether you want to store it on your local file system or in Oracle Internet Directory, perform the following steps:

If you want to store the CRL on your local file system:

1. Use Oracle Net Manager to specify the path to the CRL directory or file. Refer to Configuring Certificate Validation with Certificate Revocation Lists
2. Use the `orapki` utility to configure the CRL for system use. Refer to Renaming CRLs with a Hash Value for Certificate Validation

If you want to store the CRL in Oracle Internet Directory:

1. Use Oracle Net Configuration Assistant to create and configure an `ldap.ora` file with directory connection information.
2. Use the `orapki` utility to upload the CRL to the directory. Refer to Uploading CRLs to Oracle Internet Directory

**Parent topic:** Certificate Validation with Certificate Revocation Lists

### 22.14 Configuring Your System to Use Hardware Security Modules

Oracle Database supports hardware security modules that use APIs that conform to the RSA Security, Inc., PKCS #11 specification.

Typically, these hardware devices are used to securely store and manage private keys in tokens or smart cards, or to accelerate cryptographic processing.

- General Guidelines for Using Hardware Security Modules for TLS  
	Oracle provides a set of guidelines to follow if you are using a hardware security module with Oracle Database.
- Configuring Your System to Use nCipher Hardware Security Modules  
	You can configure your system to use nCipher hardware security modules for cryptographic processing.
- Configuring Your System to Use SafeNET Hardware Security Modules  
	You can configure your system to use SafeNET hardware security modules for cryptographic processing.
- Troubleshooting Using Hardware Security Modules  
	Oracle provides troubleshooting advice for hardware security modules.

**Parent topic:** Configuring Transport Layer Security Authentication

#### 22.14.1 General Guidelines for Using Hardware Security Modules for TLS

Oracle provides a set of guidelines to follow if you are using a hardware security module with Oracle Database.

1. Contact your hardware device vendor to obtain the necessary hardware, software, and PKCS #11 libraries.
2. Install the hardware, software, and libraries where appropriate for the hardware security module you are using.
3. Test your hardware security module installation to ensure that it is operating correctly. Refer to your device documentation for instructions.
4. Create a wallet of the type `PKCS11` by using Oracle Wallet Manager and specify the absolute path to the PKCS #11 library (including the library name) if you wish to store the private key in the token. Oracle `PKCS11` wallets contain information that points to the token for private key access.
	Note that starting in Oracle Database 21c, Oracle Wallet Manager is deprecated. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

You can use the wallet containing PKCS #11 information just as you would use any Oracle wallet, except the private keys are stored on the hardware device and the cryptographic operations are performed on the device as well.

#### 22.14.2 Configuring Your System to Use nCipher Hardware Security Modules

You can configure your system to use nCipher hardware security modules for cryptographic processing.

- About Configuring Your System to Use nCipher Hardware Security Modules  
	Hardware security modules made by nCipher Corporation are certified to operate with Oracle Database.
- Oracle Components Required To Use an nCipher Hardware Security Module  
	To use an nCipher hardware security module, you must have a special set of components.
- Directory Path Requirements for Installing an nCipher Hardware Security Module  
	The nCipher hardware security module uses the nCipher PKCS #11 library.

**Parent topic:** Configuring Your System to Use Hardware Security Modules

##### 22.14.2.1 About Configuring Your System to Use nCipher Hardware Security Modules

Hardware security modules made by nCipher Corporation are certified to operate with Oracle Database.

These modules provide a secure way to store keys and off-load cryptographic processing. Primarily, these devices provide the following benefits:

- Off-load cryptographic processing that frees your server to respond to other requests
- Secure private key storage on the device
- Allow key administration through the use of smart cards

Note:

You must contact your nCipher representative to obtain certified hardware and software to use with Oracle Database.

**Parent topic:** Configuring Your System to Use nCipher Hardware Security Modules

##### 22.14.2.2 Oracle Components Required To Use an nCipher Hardware Security Module

To use an nCipher hardware security module, you must have a special set of components.

These components are as follows:

- nCipher Hardware Security Module
- Supporting nCipher PKCS #11 library
	The following platform-specific PKCS#11 library is required:
	- `libcknfast.so` library for UNIX 32-Bit
		- `libcknfast-64.so` library for UNIX 64-Bit
		- `cknfast.dll` library for Windows

Note:

You must contact your nCipher representative to have the hardware security module or the secure accelerator installed, and to acquire the necessary library.

These tasks must be performed before you can use an nCipher hardware security module with Oracle Database.

**Parent topic:** Configuring Your System to Use nCipher Hardware Security Modules

##### 22.14.2.3 Directory Path Requirements for Installing an nCipher Hardware Security Module

The nCipher hardware security module uses the nCipher PKCS #11 library.

To use the secure accelerator, you must provide the absolute path to the directory that contains the nCipher PKCS #11 library (including the library name) when you create the wallet by using Oracle Wallet Manager. This enables the library to be loaded at runtime.

Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

Typically, the nCipher card is installed at the following locations:

- `/opt/nfast` for UNIX
- `C:\nfast` for Windows

The nCipher PKCS #11 library is located at the following location for typical installations:

- `/opt/nfast/toolkits/pkcs11/libcknfast.so` for UNIX 32-Bit
- `/opt/nfast/toolkits/pkcs11/libcknfast-64.so` for UNIX 64-Bit
- `C:\nfast\toolkits\pkcs11\cknfast.dll` for Windows

Note:

Use the 32-bit library version when using the 32-bit release of Oracle Database and use the 64-bit library version when using the 64-bit release of Oracle Database. For example, use the 64-bit nCipher PKCS #11 library for the Oracle Database for Solaris Operating System (SPARC 64-bit).

**Parent topic:** Configuring Your System to Use nCipher Hardware Security Modules

#### 22.14.3 Configuring Your System to Use SafeNET Hardware Security Modules

You can configure your system to use SafeNET hardware security modules for cryptographic processing.

- About Configuring Your System to Use SafeNET Hardware Security Modules  
	Hardware security modules made by SafeNET Incorporated are certified to operate with Oracle Database.
- Oracle Components Required for SafeNET Luna SA Hardware Security Modules  
	To use a SafeNET Luna SA hardware security module, you must have a special set of components.
- Directory Path Requirements for Installing a SafeNET Hardware Security Module  
	The SafeNET hardware security module uses the SafeNET PKCS #11 library.

**Parent topic:** Configuring Your System to Use Hardware Security Modules

##### 22.14.3.1 About Configuring Your System to Use SafeNET Hardware Security Modules

Hardware security modules made by SafeNET Incorporated are certified to operate with Oracle Database.

These modules provide a secure way to store keys and off-load cryptographic processing. Primarily, these devices provide the following benefits:

- Off-load of cryptographic processing to free your server to respond to more requests
- Secure private key storage on the device

Note:

You must contact your SafeNET representative to obtain certified hardware and software to use with Oracle Database.

**Parent topic:** Configuring Your System to Use SafeNET Hardware Security Modules

##### 22.14.3.2 Oracle Components Required for SafeNET Luna SA Hardware Security Modules

To use a SafeNET Luna SA hardware security module, you must have a special set of components.

These components are as follows:

- SafeNET Luna SA Hardware Security Module
- Supporting SafeNET Luna SA PKCS #11 library
	The following platform-specific PKCS#11 library is required:
	- `libCryptoki2.so` library for UNIX
		- `cryptoki.dll` library for Windows

Note:

You must contact your SafeNET representative to have the hardware security module or the secure accelerator installed, and to acquire the necessary library.

These tasks must be performed before you can use a SafeNET hardware security module with Oracle Database.

**Parent topic:** Configuring Your System to Use SafeNET Hardware Security Modules

##### 22.14.3.3 Directory Path Requirements for Installing a SafeNET Hardware Security Module

The SafeNET hardware security module uses the SafeNET PKCS #11 library.

To use the secure accelerator, you must provide the absolute path to the directory that contains the SafeNET PKCS #11 library (including the library name) when you create the wallet using Oracle Wallet Manager. This enables the library to be loaded at runtime.

Oracle Wallet Manager is deprecated with Oracle Database 21c. Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

Typically, the SafeNET Luna SA client is installed at the following location:

- `/usr/lunasa` for UNIX
- `C:\Program Files\LunaSA` for Windows

The SafeNET Luna SA PKCS #11 library is located at the following location for typical installations:

- `/usr/lunasa/lib/libCryptoki2.so` for UNIX
- `C:\Program Files\LunaSA\cryptoki2.dll` for Windows

**Parent topic:** Configuring Your System to Use SafeNET Hardware Security Modules

#### 22.14.4 Troubleshooting Using Hardware Security Modules

Oracle provides troubleshooting advice for hardware security modules.

- Errors in the Oracle Net Trace Files  
	To detect whether the module is being used, you can turn on Oracle Net tracing.
- Error Messages Associated with Using Hardware Security Modules  
	Errors that are associated with using PKCS #11 hardware security modules can appear.

**Parent topic:** Configuring Your System to Use Hardware Security Modules

##### 22.14.4.1 Errors in the Oracle Net Trace Files

To detect whether the module is being used, you can turn on Oracle Net tracing.

If the wallet contains PKCS #11 information and the private key on the module is being used, then you will see the following entries in the Oracle Net tracing file without error messages logged between `entry` and `exit`:

```
nzpkcs11_Init: entry
nzpkcs11CP_ChangeProviders: entry
nzpkcs11CP_ChangeProviders: exit
nzpkcs11GPK_GetPrivateKey: entry
nzpkcs11GPK_GetPrivateKey: exit
nzpkcs11_Init: exit
...
nzpkcs11_Decrypt: entry
nzpkcs11_Decrypt: exit

nzpkcs11_Sign: entry
nzpkcs11_Sign: exit
```

##### 22.14.4.2 Error Messages Associated with Using Hardware Security Modules

Errors that are associated with using PKCS #11 hardware security modules can appear.

ORA-43000: PKCS11: library not found

Cause: The system cannot locate the PKCS #11 library at the location specified when the wallet was created. This happens only when the library is moved after the wallet is created.

Action: Copy the PKCS #11 library back to its original location where it was when the wallet was created.

ORA-43001: PKCS11: token not found

Cause: The smart card that was used to create the wallet is not present in the hardware security module slot.

Action: Ensure that the smart card that was used when the wallet was created is present in the hardware security module slot.

ORA-43002: PKCS11: passphrase is wrong

Cause: This can occur when an incorrect password is specified at wallet creation, or the PKCS #11 device password is changed after the wallet is created and not updated in the wallet by using Oracle Wallet Manager.

Action: Depending on the cause, take one of the following actions:

If you see this error during wallet creation, then check to ensure that you have the correct password and reenter it.

If the password changed after wallet creation, then use Oracle Wallet Manager to open the wallet and enter a new password.

See Also:

[Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9733) about creating an Oracle wallet to store hardware security credentials

Note:

The nCipher log file is in the directory where the module is installed at the following location:

`/log/logfile`

See Also:

nCipher and SafeNET documentation for more information about troubleshooting nCipher and SafeNET devices

**Parent topic:** Troubleshooting Using Hardware Security Modules

[^1]: In each client `sqlnet.ora` file, remove all deprecated algorithms if they are defined.

You can bypass this step if the following parameters are not defined or have no algorithms listed.
- `SQLNET.ENCRYPTION_TYPES_CLIENT`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`

[^2]: In the server `sqlnet.ora` file, remove all deprecated algorithms if they are defined.

You can bypass this step if the following parameters are not defined or have no algorithms listed.
- `SQLNET.ENCRYPTION_TYPES_SERVER`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER`

[^undefined]: For maximum security on the server, set the following `sqlnet.ora` parameters:

- `SQLNET.ENCRYPTION_SERVER = REQUIRED`
- `SQLNET.ENCRYPTION_TYPES_SERVER = (AES256)`
- `SQLNET.CRYPTO_CHECKSUM_SERVER = REQUIRED`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (SHA512)`
- `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`

[^undefined]: For maximum security on the client, set the following `sqlnet.ora` parameters:

- `SQLNET.ENCRYPTION_CLIENT = REQUIRED`
- `SQLNET.ENCRYPTION_TYPES_CLIENT = (AES256)`
- `SQLNET.CRYPTO_CHECKSUM_CLIENT = REQUIRED`
- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT = (SHA512)`
- `SQLNET.ALLOW_WEAK_CRYPTO = FALSE`

[^undefined]: ↩

[^3]: In each client `sqlnet.ora` file, after you have removed all the deprecated algorithms from the server and the clients per steps 5 and 6, set the parameter `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` so that the clients can be prevented from communicating with unpatched servers.

If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.

[^undefined]: In the server `sqlnet.ora` file, after you have updated all the clients with `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` per step 9, set the parameter `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`. This parameter prevents a patched server from communicating with unpatched clients.

If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.

If you use the database links, then the first database server acts as a client and connects to the second server. Therefore, ensure that all servers are fully patched and unsupported algorithms are removed before you set `SQLNET.ALLOW_WEAK_CRYPTO` to `FALSE`
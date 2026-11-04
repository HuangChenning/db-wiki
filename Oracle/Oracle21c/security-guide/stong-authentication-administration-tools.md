---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/stong-authentication-administration-tools.html
tags:
  - oracle
  - 21c
  - security-guide
---

You can use a set of strong authentication administration tools for native network encryption and public key infrastructure credentials.

**Parent topic:** [Managing Strong Authentication](part_5.md)

### 20.1 About the Configuration and Administration Tools

The configuration and administration tools manage the encryption, integrity (checksumming), and strong authentication methods for Oracle Net Services.

Strong authentication method configuration can include third-party software, as is the case for Kerberos or RADIUS, or it may entail configuring and managing a public key infrastructure for using digital certificates with Transport Layer Security (TLS).

**Parent topic:** Strong Authentication Administration Tools

### 20.2 Native Network Encryption and Strong Authentication Configuration Tools

Oracle Net Services can encrypt data using standard encryption algorithms, and for strong authentication methods, such as Kerberos, RADIUS, and SSL.

- About Oracle Net Manager  
	Oracle Net Manager configures Oracle Net Services for an Oracle home on a local client or server host.
- Kerberos Adapter Command-Line Utilities  
	The Kerberos adapter provides command-line utilities that obtain, cache, display, and remove Kerberos credentials.

**Parent topic:** Strong Authentication Administration Tools

#### 20.2.1 About Oracle Net Manager

Oracle Net Manager configures Oracle Net Services for an Oracle home on a local client or server host.

Although you can use Oracle Net Manager, a graphical user interface tool, to configure Oracle Net Services, such as naming, listeners, and general network settings, it also enables you to configure the following features, which use the Oracle Net protocol:

- Strong authentication (Kerberos, RADIUS, and Transport Layer Security)
- Native network encryption (RC4, DES, 3DES, and AES)
- Checksumming for data integrity (MD5, SHA-1, SHA-2)

Note:

The DES, 3DES112, 3DES168, MD5, and RC4 algorithms are deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).

**Parent topic:** Native Network Encryption and Strong Authentication Configuration Tools

#### 20.2.2 Kerberos Adapter Command-Line Utilities

The Kerberos adapter provides command-line utilities that obtain, cache, display, and remove Kerberos credentials.

The following table briefly describes these utilities.

Table 20-1 Kerberos Adapter Command-Line Utilities

| Utility Name | Description |
| --- | --- |
| `okinit` | Obtains Kerberos tickets from the Key Distribution Center (KDC) and caches them in the user's credential cache |
| `oklist` | Displays a list of Kerberos tickets in the specified credential cache |
| `okdstry` | Removes Kerberos credentials from the specified credential cache |
| `okcreate` | Automates the creation of keytabs from either the KDC or a service endpoint |

Note:

The Cybersafe adapter is not supported beginning with this release. You should use Oracle's Kerberos adapter in its place. Kerberos authentication with the Cybersafe KDC (Trust Broker) continues to be supported when using the Kerberos adapter.

### 20.3 Public Key Infrastructure Credentials Management Tools

The security provided by a public key infrastructure (PKI) depends on how effectively you store, manage, and validate your PKI credentials.

- About Oracle Wallet Manager  
	Wallet owners and security administrators use Oracle Wallet Manager to manage and edit the security credentials in their Oracle wallets.
- About the orapki Utility  
	The `orapki` utility manages certificate revocation lists (CRLs), creates and manages Oracle wallets, and creates signed certificates.

**Parent topic:** Strong Authentication Administration Tools

#### 20.3.1 About Oracle Wallet Manager

Wallet owners and security administrators use Oracle Wallet Manager to manage and edit the security credentials in their Oracle wallets.

A wallet is a password-protected container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by SSL. You can use Oracle Wallet Manager to perform the following tasks:

- Create public and private key pairs
- Store and manage user credentials
- Generate certificate requests
- Store and manage certificate authority certificates (root key certificate and certificate chain)
- Upload and download wallets to and from an LDAP directory
- Create wallets to store hardware security module credentials

Note:

In previous releases of Oracle Database, you could use Oracle Wallet Manager to configure wallets for Transparent Data Encryption. In this release, you can use the `ADMINISTER KEY MANAGEMENT SQL` statement instead.

Note:

Oracle Wallet Manager (OWM) is deprecated with Oracle Database 21c.

Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

#### 20.3.2 About the orapki Utility

The `orapki` utility manages certificate revocation lists (CRLs), creates and manages Oracle wallets, and creates signed certificates.

The basic syntax for this command-line utility is as follows:

```
orapki module command -option_1 argument ... -option_n argument
```

For example, the following command lists all certificate revocation lists (CRLs) in the CRL subtree in an instance of Oracle Internet Directory that is installed on `machine1.us.example.com` and that uses port 389:

```
orapki crl list -ldap machine1.us.example.com:389
```

Note:

The use of `orapki` to configure Transparent Data Encryption has been deprecated. Instead, use the `ADMINISTER KEY MANAGEMENT` SQL statement.

### 20.4 Duties of Strong Authentication Administrators

Most of the tasks of a security administrator involve ensuring that the connections to and from Oracle databases are secure.

The following table describes the primary tasks of security administrators who are responsible for strong authentication, the tools used to perform the tasks, and links to where the tasks are documented.

Table 20-2 Common Security Administrator/DBA Configuration and Administrative Tasks

| Task | Tools Used | See Also |
| --- | --- | --- |
| Configure encrypted Oracle Net connections between database servers and clients | Oracle Net Manager | [Configuring Encryption on the Client and the Server](configuring-network-data-encryption-and-integrity.md) |
| Configure checksumming on Oracle Net connections between database servers and clients | Oracle Net Manager | [Configuring Integrity on the Client and the Server](configuring-network-data-encryption-and-integrity.md) |
| Configure database clients to accept RADIUS authentication | Oracle Net Manager | [Step 1A: Configure RADIUS on the Oracle Client](configuring-radius-authentication.md) |
| Configure a database to accept RADIUS authentication | Oracle Net Manager | [Step 1B: Configure RADIUS on the Oracle Database Server](configuring-radius-authentication.md) |
| Create a RADIUS user and grant them access to a database session | SQL\*Plus | [Step 2: Create a User and Grant Access](configuring-radius-authentication.md) |
| Configure Kerberos authentication on a database client and server | Oracle Net Manager | [Step 6: Configure Kerberos Authentication](configuring-kerberos-authentication.md) |
| Create a Kerberos database user | - `kadmin.local` - Oracle Net Manager | - [Step 7: Create a Kerberos User](configuring-kerberos-authentication.md) - [Step 8: Create an Externally Authenticated Oracle User](configuring-kerberos-authentication.md) |
| Manage Kerberos credentials in the credential cache | - `okinit` - `oklist` - `okdstry` - `okcreate` | - [okinit Utility Options for Obtaining the Initial Ticket](configuring-kerberos-authentication.md) - [oklist Utility Options for Displaying Credentials](configuring-kerberos-authentication.md) - [okdstry Utility Options for Removing Credentials from the Cache File](configuring-kerberos-authentication.md) |
| Create a wallet for a database client or server | Oracle Wallet Manager \* | [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9731) |
| Request a user certificate from a certificate authority (CA) for SSL authentication | Oracle Wallet Manager \* | - [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9747) to add a certificate request - [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9748) to import a user certificate into an Oracle wallet |
| Import a user certificate and its associated trusted certificate (CA certificate) into a wallet | Oracle Wallet Manager \* | - [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9758) to import a trusted certificate - [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=DBIMI9748) to import a user certificate into an Oracle wallet |
| Configuring SSL connections for a database client | Oracle Net Manager | [Step 2: Configure Transport Layer Security on the Client](configuring-secure-sockets-layer-authentication.md) |
| Configuring SSL connections for a database server | Oracle Net Manager | [Step 1: Configure Transport Layer Security on the Server](configuring-secure-sockets-layer-authentication.md) |
| Enabling certificate validation with a certificate revocation list (CRL) | Oracle Net Manager | [Configuring Certificate Validation with Certificate Revocation Lists](configuring-secure-sockets-layer-authentication.md) |

Note:

Oracle Wallet Manager (OWM) is deprecated with Oracle Database 21c.

Instead of using Oracle Wallet Manager, Oracle recommends that you use the command line tools `orapki` and `mkstore`.

**Parent topic:** Strong Authentication Administration Tools
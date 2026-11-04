---
title: Oracle Advanced Security FIPS 140 Settings
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoappe.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## D Oracle Advanced Security FIPS 140 Settings

This appendix contains:

## D.1 About the FIPS 140 Settings

This appendix describes how to configure Oracle Database for the [Federal Information Processing Standard (FIPS)](asogls.md), for the current standard, 140-2, and for 140-1. To verify the current status of the certification, you can find information at the Computer Security Resource Center (CSRC) Web site address from the National Institute of Standards and Technology:

`http://csrc.nist.gov/`

To find information specific to FIPS, you can search for `Validated FIPS 140 Cryptographic Modules`. The security policy, which is available on this site upon successful certification, includes requirements for secure configuration of the host operating system.

## D.2 Configuring Oracle Database for FIPS 140-2

This section contains:

- About the FIPS 140-2 Settings
- Configuring the SSLFIPS\_140 Parameter
- Selecting Cipher Suites
- Post-Installation Checks
- Verifying FIPS Connections

### D.2.1 About the FIPS 140-2 Settings

The cryptographic libraries for SSL included in Oracle Database 10g are designed to meet FIPS 140-2 Level 2 certification. Oracle Advanced Security makes use of these cryptographic libraries for SSL authentication.

The instructions in this appendix apply to Oracle Database Release 11.2.0.4 and later. For more information about upgrading to Release 11.2.0.4, visit the following Oracle Technology Network site:

`http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index-092322.html`

### D.2.2 Configuring the SSLFIPS\_140 Parameter

Oracle Advanced Security SSL adapter can be configured to run in FIPS mode by setting the `SSLFIPS_140` parameter to `TRUE` in the `fips.ora` file.

```
SSLFIPS_140=TRUE
```

This parameter is set to `FALSE` by default. It must be set to `TRUE` on both the client and the server for FIPS mode operation.

Make sure that the `fips.ora` file is either located in the `$ORACLE_HOME` `/ldap/admin` directory, or is pointed to by the `FIPS_HOME` environment variable. This procedure can be repeated in any Oracle home for any database server or client.

Note:

The `SSLFIPS_140` parameter replaces the `SQLNET.SSLFIPS_140` parameter used in Oracle Database 10g Release 2 (10.2). The parameter needs to be set in the `fips.ora` file, and not the `sqlnet.ora` file.

### D.2.3 Selecting Cipher Suites

A cipher suite is a set of authentication, encryption and data integrity algorithms used for exchanging messages between network nodes. During an SSL handshake, for example, the two nodes negotiate to see as to which cipher suite they will use when transmitting messages back and forth.

Only the following cipher suites are approved for FIPS validation:

- `SSL_DH_anon_WITH_3DES_EDE_CBC_SHA`
- `SSL_RSA_WITH_AES_256_CBC_SHA`
- `SSL_RSA_WITH_AES_128_CBC_SHA`
- `SSL_RSA_WITH_3DES_EDE_CBC_SHA`

Oracle Advanced Security SSL cipher suites are automatically set to FIPS approved cipher suites. If you wish to configure specific cipher suites, you can do so by editing the `SSL_CIPHER_SUITES` parameter in the `sqlnet.ora` or the `listener.ora` file.

```
SSL_CIPHER_SUITES=(SSL_cipher_suite1[,SSL_cipher_suite2[,..]])
```

You can also use Oracle Net Manager to set this parameter on the server and the client.

See Also:

["Step 2C: Set the Secure Sockets Layer Cipher Suites on the Server (Optional)"](asossl.md) and ["Step 3D: Set the Client Secure Sockets Layer Cipher Suites (Optional)"](asossl.md) for more information on setting cipher suites.

### D.2.4 Post-Installation Checks

After installation, the following permissions must be verified in the operating system:

- Execute permissions must be set on all Oracle executable files so as to prevent execution of Oracle Cryptographic Libraries by users who are unauthorized to do so in accordance with the system security policy.
- Read and write permissions must be set on all Oracle executable files so as to prevent accidental or deliberate reading or modification of Oracle Cryptographic Libraries by any user.

To comply with FIPS 140-2 Level 2 requirements, the security policy must include procedures to prevent unauthorized users from reading, modifying or executing Oracle Cryptographic Libraries processes and the memory they are using in the operating system.

### D.2.5 Verifying FIPS Connections

To check if FIPS mode is enabled, tracing can be added to the `sqlnet.ora` file. FIPS self-test messages can be found in the trace file. Add the following lines to `sqlnet.ora` to enable tracing:

```
trace_directory_server=trace_dir
trace_file_server=trace_file
trace_level_server=trace_level
```

For example:

```
trace_directory=/private/oracle/owm
trace_file_server=fips_trace.trc
trace_level_server=6
```

Trace level 6 is the minimum trace level required to check the results of the FIPS self-tests.

## D.3 Configuring Oracle Database for FIPS 140-1

This section contains:

- About the FIPS 140-1 Settings
- sqlnet.ora FIPS 140-1 Configuration Parameters
- Post Installation Checks
- Status Information Physical Security

Note:

The information contained in this section should be used with the information provided in [Appendix A, "Data Encryption and Integrity Parameters"](asoappa.md).

### D.3.1 About the FIPS 140-1 Settings

The Oracle Database FIP 140-1 implementation has been validated under Federal Information Processing Standard (FIPS) 140-1 at the Level 2 security level. This appendix describes the formal configuration required to comply with the FIPS 140-1 standard. Refer to the NIST Cryptographic Modules Validation list at the following Web site address:

```
http://csrc.nist.gov/cryptval/140-1/1401val.htm
```

### D.3.2 sqlnet.ora FIPS 140-1 Configuration Parameters

This appendix contains information on the Oracle Advanced Security parameters required in the `sqlnet.ora` files to ensure that any connections created between a client and server are encrypted under the control of the server.

Configuration parameters are contained in the `sqlnet.ora` file that is held locally for each of the client and server processes. The protection placed on these files should be equivalent to the level of a DBA.

The following configuration parameters are described in this appendix:

- `ENCRYPTION_SERVER`
- `ENCRYPTION_CLIENT`
- `ENCRYPTION_TYPES_SERVER`
- `ENCRYPTION_TYPES_CLIENT`
- `FIPS_140`

#### D.3.2.1 Server Encryption Level Setting

The server side of the negotiation notionally controls the connection settings. The following parameter in the server file is mandatory:

```
SQLNET.ENCRYPTION_SERVER=REQUIRED
```

Setting the encryption as `REQUIRED` on the server side of the connection ensures that a connection is only permitted if encryption is used, irrespective of the parameter value on the client.

#### D.3.2.2 Client Encryption Level Setting

The `ENCRYPTION_CLIENT` parameter specifies the connection behavior for the client. One of the following parameter settings in the client file is mandatory:

```
SQLNET.ENCRYPTION_CLIENT=(ACCEPTED|REQUESTED|REQUIRED)
```

A connection to the server is only possible if there is agreement between client and server for the connection encryption. The server has this set to `REQUIRED`, therefore the client must not reject encryption for a valid connection to be the result. Failure to specify one of these values results in error when attempting to connect to a FIPS 140-1 compliant server.

#### D.3.2.3 Server Encryption Selection List

The `ENCRYPTION_TYPES_SERVER` parameter specifies a list of encryption algorithms that the server is permitted to use when acting as a server in the order of required usage. The specified algorithm must be installed or the connection terminates. For FIPS 140-1 compliance, only DES encryption is permitted and therefore the following parameter setting is mandatory:

```
SQLNET.ENCRYPTION_TYPES_SERVER=(DES,DES40)
```

#### D.3.2.4 Client Encryption Selection List

The `ENCRYPTION_TYPES_CLIENT` parameter specifies the list of encryption algorithms which the client is prepared to use for the connection with the server. In order for a connection to be successful, the algorithm must first be installed and the encryption type must be mutually acceptable to the server.

To create a connection with a server that is configured for FIPS 140-1, the following parameter setting is mandatory:

```
SQLNET.ENCRYPTION_TYPES_CLIENT=(DES,DES40)
```

#### D.3.2.5 FIPS Parameter

The default setting of the `FIPS_140` parameter is `FALSE`. Setting the parameter to `TRUE` is mandatory for both client and server to ensure Oracle Advanced Security complies with the standards defined in FIPS 140-1 as follows:

```
SQLNET.FIPS_140=TRUE
```

Note:

Use a text editor to set the `FIPS_140` parameter in the `sqlnet.ora` file. You cannot use Oracle Net Manager to set this parameter.

### D.3.3 Post Installation Checks

After the installation, the following permissions must be verified in the operating system:

- Execute permissions must be set on all Oracle Advanced Security executable files so as to prevent execution of Oracle Advanced Security by users who are unauthorized to do so in accordance with the system security policy.
- Read and write permissions must be set on all executable files so as to prevent accidental or deliberate reading or modification of Oracle Advanced Security files by any user.

To comply with FIPS 140-1 Level 2 requirements, the security policy must include procedures to prevent unauthorized users from reading or modifying Oracle Advanced Security processes and the memory they are using in the operating system.

### D.3.4 Status Information

Status information for Oracle Advanced Security is available after the connection has been established. The information is contained in the RDBMS virtual table `v$session_connect_info`.

Running the query `SELECT * from V$SESSION_CONNECT_INFO` displays all of the product banner information for the active connection. Table D-1 shows an example of a connection configuration where the DES encryption data integrity is defined:

Table D-1 Sample Output from v$session\_connect\_info

| SID | AUTHENTICATION | OSUSER | NETWORK\_SERVICE\_BANNER |
| --- | --- | --- | --- |
| 7 | `DATABASE` | `oracle` | Oracle Bequeath operating system adapter for Solaris, v8.1.6.0.0 |
| 7 | `DATABASE` | `oracle` | Oracle Advanced Security: encryption service for Solaris |
| 7 | `DATABASE` | `oracle` | Oracle Advanced Security: DES encryption service adapter |
| 7 | `DATABASE` | `oracle` | Oracle Advanced Security: crypto-checksumming service |
| 7 | `DATABASE` | `oracle` | Oracle Advanced Security: SHA-1 crypto-checksumming service adapter. |

### D.3.5 Physical Security

To comply with FIPS 140-1 Level 2 requirements, tamper-evident seals must be applied to the cover of each computer to ensure that removal of the cover is detectable.
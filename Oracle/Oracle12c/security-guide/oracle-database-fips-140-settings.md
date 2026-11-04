---
title: Database Security Guide
book: Database Security Guide
doc_id: E85682-14
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dbseg/oracle-database-fips-140-settings.html
tags:
  - oracle
  - 12c
  - security-guide
---

- About the Oracle Database FIPS 140-2 Settings  
	The Federal Information Processing Standard (FIPS) standard, 140-2, is a U.S. government standard that defines cryptographic module security requirements.
- Configuring FIPS 140-2 for Transparent Data Encryption and DBMS\_CRYPTO  
	The `DBFIPS_140` initialization parameter configures FIPS mode.
- Configuration of FIPS 140-2 for Secure Sockets Layer  
	The `SSLFIPS_140` parameter configures Secure Sockets Layer (SSL).
- Postinstallation Checks for FIPS 140-2  
	After you configure the FIPS 140-2 settings, you must verify permissions in the operating system.
- Verifying FIPS 140-2 Connections  
	To check if FIPS mode is enabled for SSL, you can enable tracing in the `sqlnet.ora` file.

**Parent topic:** [Appendixes](part_7.md)

### E.1 About the Oracle Database FIPS 140-2 Settings

The Federal Information Processing Standard (FIPS) standard, 140-2, is a U.S. government standard that defines cryptographic module security requirements.

The FIPS 140-2 cryptographic libraries are designed to protect data at rest and in transit over the network.

Oracle Database uses these cryptographic libraries for Secure Sockets Layer (SSL), Transparent Data Encryption (TDE), and `DBMS_CRYPTO` PL/SQL package.

To verify the current status of the certification, you can find information at the Computer Security Resource Center (CSRC) Web site address from the National Institute of Standards and Technology:

[`http://csrc.nist.gov/groups/STM/cmvp/validation.html `](http://csrc.nist.gov/groups/STM/cmvp/validation.html) 

You can find information specific to FIPS by searching for `Validated FIPS 140 Cryptographic Modules`. The security policy, which is available on this site upon successful certification, includes requirements for secure configuration of the host operating system.

The Oracle Database FIPS settings are meant to enforce the use of FIPS-approved algorithms for the Oracle database only. The use of third-party vendor software with Oracle Database running in FIPS mode must use FIPS-approved algorithms or else the vendor software will encounter failures.

**Parent topic:** Oracle Database FIPS 140-2 Settings

### E.2 Configuring FIPS 140-2 for Transparent Data Encryption and DBMS\_CRYPTO

The `DBFIPS_140` initialization parameter configures FIPS mode.

1. To configure Transparent Data Encryption and the `DBMS_CRYPTO` PL/SQL package program units to run in FIPS mode, set the `DBFIPS_140` initialization parameter to `TRUE`.
	The effect of this parameter depends on the platform.
2. Restart the database.

Table E-1 describes how the `DBFIPS_140` parameter affects various platforms.

Table E-1 How the DBFIPS\_140 Initialization Parameter Affects Platforms

| Platform | Effect of Setting DBFIPS\_140 to TRUE or FALSE |
| --- | --- |
| Linux or Windows on Intel x86\_64 | - `TRUE`: TDE and `DBMS_CRYPTO` program units use Micro Edition Suite (MES) 4.1.5 FIPS mode, which uses RSA BSAFE Crypto-C Micro Edition (CCME) 4.1.2 - `FALSE`: TDE and `DBMS_CRYPTO` program units use Intel Performance Primitives (IPP) |
| Solaris 11.1+ on either SPARC T-series or Intel x86\_64 | - `TRUE`: TDE and `DBMS_CRYPTO` program units use MES 4.1.5 FIPS mode, which uses RSA BSAFE Crypto-C Micro Edition (CCME) 4.1.2 - `FALSE`: TDE and `DBMS_CRYPTO` program units use Solaris Cryptographic Framework (SCF)/UCrypto (separately validated for FIPS 140) |
| Other operating systems or hardware | - `TRUE`: TDE and `DBMS_CRYPTO` program units use MES 4.1.5 FIPS mode, which uses RSA BSAFE Crypto-C Micro Edition (CCME) 4.1.2 - `FALSE`: TDE and `DBMS_CRYPTO` program units use MES 4.1.5 non-FIPS mode |

Be aware that setting `DBFIPS_140` to `TRUE` and thus using the underlying library in FIPS mode incurs a certain amount of overhead when the library is first loaded. This is due to the verification of the signature and the execution of the self tests on the library. Once the library is loaded, then there is no other impact on performance.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=REFRN10356) for more information about the `DBFIPS_140` initialization parameter

**Parent topic:** Oracle Database FIPS 140-2 Settings

### E.3 Configuration of FIPS 140-2 for Secure Sockets Layer

The `SSLFIPS_140` parameter configures Secure Sockets Layer (SSL).

- Configuring the SSLFIPS\_140 and SSLFIPS\_LIB Parameters for Secure Sockets Layer  
	To configure FIPS 140-2 for SSL, you must set the `SSLFIPS_140` parameter. If you are using the Oracle Instant Client, then you must set the `SSLFIPS_LIB` parameter as well.
- Approved SSL Cipher Suites for FIPS 140-2  
	A cipher suite is a set of authentication, encryption, and data integrity algorithms that exchange messages between network nodes.

**Parent topic:** Oracle Database FIPS 140-2 Settings

#### E.3.1 Configuring the SSLFIPS\_140 and SSLFIPS\_LIB Parameters for Secure Sockets Layer

To configure FIPS 140-2 for SSL, you must set the `SSLFIPS_140` parameter. If you are using the Oracle Instant Client, then you must set the `SSLFIPS_LIB` parameter as well.

The `SSLFIPS_140` parameter configures the Secure Sockets Layer (SSL) adapter to run in FIPS mode. `SSLFIPS_LIB` sets the location of the FIPS library.

1. Ensure that the `fips.ora` file is either located in the `$ORACLE_HOME` `/ldap/admin` directory, or is in a location pointed to by the `FIPS_HOME` environment variable.
2. In the `fips.ora` file, set the `SSLFIPS_140` and `SSLFIPS_LIB` parameters.
	- Set `SSLFIPS_140` to `TRUE` so that the SSL adapter can run in FIPS mode. For example:
		```
		SSLFIPS_140=TRUE
		```
		This parameter is `FALSE` by default.
		- If you are using Oracle Instant Client, then set `SSLFIPS_LIB` to the location of the FIPS library. For example:
		```
		SSLFIPS_LIB=$ORACLE_HOME/lib
		```
3. Repeat this procedure in any Oracle Database home for any database server or client.

When you set `SSLFIPS_140` to `TRUE`, Secure Sockets Layer cryptographic operations take place in the embedded RSA/Micro Edition Suite (MES) library in FIPS mode. These cryptographic operations are accelerated by the CPU when hardware acceleration is available and properly configured in the host hardware and software.

If you set `SSLFIPS_140` to `FALSE`, then Secure Sockets Layer cryptographic operations take place in the embedded RSA/Micro Edition Suite (MES) library in non-FIPS mode, and as with the `TRUE` setting, the operations are accelerated if possible.

For native encryption, this behavior of cryptographic operations landing in RSA/Micro Edition Suite (MES) and being accelerated is similar to the above, except that it is determined by the `FIPS_140` setting in `sqlnet.ora` (instead of the `SSL_FIPS140` setting in `fips.ora`).

Note:

The `SSLFIPS_140` parameter replaces the `SQLNET.SSLFIPS_140` parameter used in Oracle Database 10g release 2 (10.2). You must set the parameter in the `fips.ora` file, and not the `sqlnet.ora` file.

**Parent topic:** Configuration of FIPS 140-2 for Secure Sockets Layer

#### E.3.2 Approved SSL Cipher Suites for FIPS 140-2

A cipher suite is a set of authentication, encryption, and data integrity algorithms that exchange messages between network nodes.

During an SSL handshake, for example, the two nodes negotiate to see as to which cipher suite they will use when transmitting messages back and forth.

Only the following cipher suites are approved for FIPS validation:

- `SSL_DH_anon_WITH_3DES_EDE_CBC_SHA`
- `SSL_RSA_WITH_AES_256_CBC_SHA`
- `SSL_RSA_WITH_AES_128_CBC_SHA`
- `SSL_RSA_WITH_AES_256_GCM_SHA384`
- `SSL_RSA_WITH_3DES_EDE_CBC_SHA`

Oracle Database SSL cipher suites are automatically set to FIPS approved cipher suites. If you wish to configure specific cipher suites, you can do so by editing the `SSL_CIPHER_SUITES` parameter in the `sqlnet.ora` or the `listener.ora` file.

```
SSL_CIPHER_SUITES=(SSL_cipher_suite1[,SSL_cipher_suite2[,..]])
```

You can also use Oracle Net Manager to set this parameter on the server and the client.

**Parent topic:** Configuration of FIPS 140-2 for Secure Sockets Layer

### E.4 Postinstallation Checks for FIPS 140-2

After you configure the FIPS 140-2 settings, you must verify permissions in the operating system.

The permissions are as follows:

- Set execute permissions on all Oracle executable files to prevent the execution of Oracle Cryptographic Libraries by users who are unauthorized to do so, in accordance with the system security policy.
- Set read and write permissions on all Oracle executable files to prevent accidental or deliberate reading or modification of Oracle Cryptographic Libraries by any user.

To comply with FIPS 140-2 Level 2 requirements, in the security policy, include procedures to prevent unauthorized users from reading, modifying or executing Oracle Cryptographic Libraries processes and the memory they are using in the operating system.

**Parent topic:** Oracle Database FIPS 140-2 Settings

### E.5 Verifying FIPS 140-2 Connections

To check if FIPS mode is enabled for SSL, you can enable tracing in the `sqlnet.ora` file.

You can find FIPS self-test messages in the trace file.

1. Add the following lines to `sqlnet.ora` to enable tracing:
	```
	trace_directory_server=trace_directory
	trace_file_server=trace_file
	trace_level_server=trace_level
	```
	For example:
	```
	trace_directory=/private/oracle/owm
	trace_file_server=fips_trace.trc
	trace_level_server=6
	```
2. To check if FIPS mode is enabled for TDE and `DBMS_CRYPTO`, log into SQL\*Plus and run the following command:
	```
	SHOW PARAMETER DBFIPS_140
	```

Trace level 6 is the minimum trace level required to check the results of the FIPS self-tests.

**Parent topic:** Oracle Database FIPS 140-2 Settings
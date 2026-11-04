---
title: JDBC Client-Side Security Features
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/clntsec.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 9 JDBC Client-Side Security Features

This chapter discusses support in the Oracle Java Database Connectivity (JDBC) Oracle Call Interface (OCI) and JDBC Thin drivers for login authentication, data encryption, and data integrity, particularly, with respect to features of the Oracle Advanced Security option.

Oracle Advanced Security, previously known as the Advanced Networking Option (ANO) or Advanced Security Option (ASO), provides industry standards-based data encryption, data integrity, third-party authentication, single sign-on, and access authorization. In 11g release 2 (11.2), both the JDBC OCI and thin drivers support all the Oracle Advanced Security features. Earlier releases of the JDBC drivers did not support some of the ASO features.

Note:

This discussion is not relevant to the server-side internal driver because all communication through server-side internal driver is completely internal to the server.

This chapter contains the following sections:

## Support for Oracle Advanced Security

Oracle Advanced Security provides the following security features:

- Data Encryption
	Sensitive information communicated over enterprise networks and the Internet can be protected by using encryption algorithms, which transform information into a form that can be deciphered only with a decryption key. Some of the supported encryption algorithms are RC4, DES, 3DES, and AES.
	To ensure data integrity during transmission, Oracle Advanced Security generates a cryptographically secure message digest, using MD5 or SHA-1 hashing algorithms, and includes it with each message sent across a network. This protects the communicated data from attacks, such as data modification, deleted packets, and replay attacks.
- Strong Authentication
	To ensure network security in distributed environments, it is necessary to authenticate the user and check his credentials. Password authentication is the most common means of authentication. Oracle Advanced Security enables strong authentication with Oracle authentication adapters, which support various third-party authentication services, including SSL with digital certificates. Oracle Advanced Security supports the following industry-standard authentication methods:
	- Kerberos
		- Remote Authentication Dial-In User Service (RADIUS)
		- Secure Sockets Layer (SSL)

Tip:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

JDBC OCI Driver Support for Oracle Advanced Security

If you are using the JDBC OCI driver, which presumes you are running from a computer with an Oracle client installation, then support for Oracle Advanced Security and incorporated third-party features is fairly similar to the support provided by in any Oracle client situation. Your use of Advanced Security features is determined by related settings in the `sqlnet.ora` file on the client computer.

Starting from Oracle Database 11g Release 1 (11.1), the JDBC OCI driver attempts to use external authentication if you try connecting to a database without providing a password. The following are some examples using the JDBC OCI driver to connect to a database without providing a password:

SSL Authentication

Example 9-1 Using SSL authentication to connect to the database.

Example 9-1 Using SSL Authentication to Connect to the Database

```
import java.sql.*;
import java.util.Properties;
 
public class test
{
    public static void main( String [] args ) throws Exception
    {
        String url = "jdbc:oracle:oci:@"
         +"(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=stadh25)(PORT=1529))"
         +"(CONNECT_DATA=(SERVICE_NAME=mydatabaseinstance)))";
        Driver driver = new oracle.jdbc.OracleDriver();
        Properties props = new Properties();
        Connection conn = driver.connect( url, props );
        conn.close();
    }
}
```

Using Data Source

Example 9-2 uses a data source to connect to the database.

Example 9-2 Using a Data Source to Connect to the Database

```
import java.sql.*; 
import javax.sql.*; 
import java.util.Properties; 
import oracle.jdbc.pool.*; 
 
public class testpool { 
    public static void main( String args ) throws Exception 
    { String url = "jdbc:oracle:oci:@" +"(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=stadh25)(PORT=1529))"
 +"(CONNECT_DATA=(SERVICE_NAME=mydatabaseinstance)))"; 
    OracleConnectionPoolDataSource ocpds = new OracleConnectionPoolDataSource(); 
    ocpds.setURL(url); 
    PooledConnection pc = ocpds.getPooledConnection(); 
    Connection conn = pc.getConnection(); 
    } 
    }
```

JDBC Thin Driver Support for Oracle Advanced Security

The JDBC Thin driver cannot assume the existence of an Oracle client installation or the presence of the `sqlnet.ora` file. Therefore, it uses a Java approach to support Oracle Advanced Security. Java classes that implement Oracle Advanced Security are included in the `ojdbc5.jar` and `ojdbc6.jar` files. Security parameters for encryption and integrity, usually set in `sqlnet.ora`, are set using a Java `Properties` object or through system properties.

## Support for Strong Authentication

Oracle Advanced Security enables Oracle Database users to authenticate externally. External authentication can be with RADIUS, KERBEROS, Certificate-Based Authentication, Token Cards, and Smart Cards. This is called strong authentication. Oracle JDBC drivers provide support for the following strong authentication methods:

- Kerberos
- RADIUS
- SSL (certificate-based authentication)

## Support for OS Authentication

Operating System (OS) authentication allows Oracle to pass control of user authentication to the operating system. It allows the users to connect to the database by authenticating their OS user name in the database. No password is associated with the account since it is assumed that OS authentication is sufficient. In other words, the server delegates the authentication to the client OS. You need to perform the following steps to achieve this:

- Use the following command to check the value of the Oracle `OS_AUTHENT_PREFIX` initialization parameter:
	```
	SQL> SHOW PARAMETER os_authent_prefix
	NAME                                 TYPE        VALUE
	------------------------------------ ----------- ------------------------------
	os_authent_prefix                    string      ops$
	SQL>
	```
	Note:
	Remember the OS authentication prefix. You need to create a database user to allow an OS authenticated connection, where the user name must be the prefix value concatenated to the OS user name.
- Add the following line in the `t_init1.ora` file:
	```
	REMOTE_OS_AUTHENT = TRUE
	```

When a connection is attempted from the local database server, the OS user name is passed to the Oracle server. If the user name is recognized, the Oracle the connection is accepted, otherwise the connection is rejected.

### Configuration Steps for Linux

The configuration steps necessary to set up OS authentication on Linux are the following:

1. Use the following commands to create an OS user `w_rose`:
	```
	# useradd w_rose
	# passwd w_rose
	Changing password for w_rose
	New password: password
	Retype new password: password
	```
2. Use the following command to create a database user to allow an OS authenticated connection:
	```
	CREATE USER ops$w_rose IDENTIFIED EXTERNALLY;
	GRANT CONNECT TO ops$w_rose;
	```
3. Use the following commands to test the OS authentication connection:
	```
	su - w_rose
	export ORACLE_HOME=/u01/app/oracle/product/10.1.0/db_1
	export PATH=$PATH:$ORACLE_HOME/bin
	export ORACLE_SID=DEV1
	sqlplus /
	SQL*Plus: Release 10.1.0.3.0 - Production on Wed Jun 7 08:41:15 2006
	Copyright (c) 1982, 2004, Oracle.  All rights reserved.
	Connected to:
	Oracle Database 10g Enterprise Edition Release 10.1.0.3.0 - Production
	With the Partitioning, Oracle Label Security, OLAP and Data Mining options
	SQL>
	```

### Configuration Steps for Windows

The configuration steps necessary to set up OS authentication on Windows are the following:

Note:

Oracle JDBC Thin drivers do not support NTS.
1. Create a local user, say, `w_rose`, using the Computer Management dialog box. For this you have to do the following:
	1. Click Start.
		2. From the Start menu, select Programs, then select Administrative Tools and then select Computer Management.
		3. Expand Local Users and Groups by clicking on the Plus ("+") sign.
		4. Click Users.
		5. Select New User from the Action menu.
		6. Enter details of the user in the New User dialog box and click Create.
	Note:
	The preceding steps are only for creating a local user. Domain users can be created in Active Directory.
2. Use the following command to create a database user to allow an OS authenticated connection:
	```
	CREATE USER "OPS$yourdomain.com\p_floyd" IDENTIFIED EXTERNALLY;
	GRANT CONNECT TO "OPS$yourdomain.com\p_floyd";
	```
	Note:
	When you create the database user in Windows environment, the user name should be in the following format:
	```
	<OS_authentication_prefix_parameter>$<DOMAIN>\<OS_user_name>
	```
	When using a Windows server, there is an additional consideration. The following option must be set in the `%ORACLE_HOME%\network\admin\sqlnet.ora` file:
	```
	SQLNET.AUTHENTICATION_SERVICES= (NTS)
	```
3. Use the following commands to test the OS authentication connection:
	```
	C:\> set ORACLE_SID=DB11G
	C:\> sqlplus /
	SQL*Plus: Release 11.2.0.1.0 - Production on Thu July 12 11:47:01 2007
	Copyright (c) 1982, 2008, Oracle.  All rights reserved.
	Connected to:
	Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - Production
	With the Partitioning, OLAP, Data Mining and Real Application Testing options
	SQL>
	```

### JDBC Code Using OS Authentication

Now that you have set up OS authentication to connect to the database, you can use the following JDBC code for connecting to the database:

```
String url = "jdbc:oracle:thin:@oracleserver.mydomain.com:5521:dbja"
Driver driver = new oracle.jdbc.OracleDriver();
DriverManager.registerDriver(driver);
Properties props = new Properties();
Connection conn = DriverManager.getConnection( url, props);
```

The preceding code assumes that it is executed by `p_floyd` on the client machine. The JDBC drivers retrieve the OS user name from the `user.name` system property that is set by the JVM. As a result, the following thin driver-specific error no longer exists:

```
ORA-17443=Null user or password not supported in THIN driver
```

Note:

By default, the JDBC driver retrieves the OS user name from the `user.name` system property, which is set by the JVM. If the JDBC driver is unable to retrieve this system property or if you want to override the value of this system property, then you can use the `OracleConnection.CONNECTION_PROPERTY_THIN_VSESSION_OSUSER` connection property. For more information, see Oracle Javadoc at
```
http://download.oracle.com/otn/utilities_drivers/jdbc/111060/doc/javadoc/index.html
```

## Support for Data Encryption and Integrity

You can use Oracle Advanced Security data encryption and integrity features in your Java database applications, depending on related settings in the server. When using the JDBC OCI driver, set parameters as you would in any Oracle client situation. When using the Thin driver, set parameters through a Java properties object.

Encryption is enabled or disabled based on a combination of the client-side encryption-level setting and the server-side encryption-level setting. Similarly, integrity is enabled or disabled based on a combination of the client-side integrity-level setting and the server-side integrity-level setting.

Encryption and integrity support the same setting levels, `REJECTED`, `ACCEPTED`, `REQUESTED`, and `REQUIRED`. Table 9-1 shows how these possible settings on the client-side and server-side combine to either enable or disable the feature. By default, remote OS authentication (through TCP) is disabled in the database for security reasons.

Table 9-1 Client/Server Negotiations for Encryption or Integrity

|  | Client Rejected | Client Accepted (default) | Client Requested | Client Required |
| --- | --- | --- | --- | --- |
| Server Rejected | OFF | OFF | OFF | connection fails |
| Server Accepted (default) | OFF | OFF | ON | ON |
| Server Requested | OFF | ON | ON | ON |
| Server Required | connection fails | ON | ON | ON |

Table 9-1 shows, for example, that if encryption is requested by the client, but rejected by the server, it is disabled. The same is true for integrity. As another example, if encryption is accepted by the client and requested by the server, it is enabled. And, again, the same is true for integrity.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

Note:

The term checksum still appears in integrity parameter names, but is no longer used otherwise. For all intents and purposes, checksum and integrity are synonymous.

This section covers the following topics:

- JDBC OCI Driver Support for Encryption and Integrity
- JDBC Thin Driver Support for Encryption and Integrity
- Setting Encryption and Integrity Parameters in Java

### JDBC OCI Driver Support for Encryption and Integrity

If you are using the JDBC OCI driver, which presumes an Oracle-client setting with an Oracle client installation, then you can enable or disable data encryption or integrity and set related parameters as you would in any Oracle client situation, through settings in the `SQLNET.ORA` file on the client.

To summarize, the client parameters are shown in Table 9-2:

Table 9-2 OCI Driver Client Parameters for Encryption and Integrity

| Parameter Description | Parameter Name | Possible Settings |
| --- | --- | --- |
| Client encryption level | `SQLNET.ENCRYPTION_CLIENT` | `REJECTED ACCEPTED REQUESTED REQUIRED` |
| Client encryption selected list | `SQLNET.ENCRYPTION_TYPES_CLIENT` | `RC4_40`, `RC4_56`, `DES`, `DES40`, `AES128`, `AES192`, `AES256`, `3DES112`, `3DES168`  (see Note) |
| Client integrity level | `SQLNET.CRYPTO_CHECKSUM_CLIENT` | `REJECTED ACCEPTED REQUESTED REQUIRED` |
| Client integrity selected list | `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT` | `MD5`, `SHA-1` |

Note:

For the Oracle Advanced Security domestic edition only, settings of `RC4_128` and `RC4_256` are also possible.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)

### JDBC Thin Driver Support for Encryption and Integrity

The JDBC Thin driver support for data encryption and integrity parameter settings parallels the JDBC OCI driver support discussed in the preceding section. Corresponding parameters can be set through a Java properties object that you would then be used when opening a database connection.

Table 9-3 lists the parameter information for the JDBC Thin driver. These parameters are defined in the `oracle.jdbc.OracleConnection` interface.

Table 9-3 Thin Driver Client Parameters for Encryption and Integrity

| Parameter Name | Parameter Type | Possible Settings |
| --- | --- | --- |
| `CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL` | `String` | `REJECTED ACCEPTED REQUESTED REQUIRED` |
| `CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES` | `String` | `AES256`, `AES192`, `AES128`, `3DES168`, `3DES112`, `DES56C`, `DES40C`, `RC4_256`, `RC4_128`, `RC4_40`, `RC4_56` |
| `CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL` | `String` | `REJECTED ACCEPTED REQUESTED REQUIRED` |
| `CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES` | `String` | `MD5`, `SHA1` |

Note:

- Because Oracle Advanced Security support for the Thin driver is incorporated directly into the JDBC classes JAR file, there is only one version, not separate domestic and export editions. Only parameter settings that would be suitable for an export edition are possible.
- The letter C in `DES40C` and `DES56C` refers to Cipher Block Chaining (CBC) mode.

### Setting Encryption and Integrity Parameters in Java

Use a Java properties object, that is, an instance of `java.util.Properties`, to set the data encryption and integrity parameters supported by the JDBC Thin driver.

The following example instantiates a Java properties object, uses it to set each of the parameters in Table 9-3, and then uses the properties object in opening a connection to the database:

```
...
Properties prop = new Properties();
prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL, "REQUIRED");
prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES, "( DES40C )");
prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL, "REQUESTED");
prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES, "( MD5 )");

OracleDataSource ods = new OracleDataSource();
ods.setProperties(prop);
ods.setURL("jdbc:oracle:thin:@localhost:1521:main");
Connection conn = ods.getConnection();
...
```

The parentheses around the values encryption type and checksum type allow for lists of values. When multiple values are supplied, the server and the client negotiate to determine which value is to be actually used.

Example

Example 9-3 is a complete class that sets data encryption and integrity parameters before connecting to a database to perform a query.

Note:

In the example, the string "REQUIRED" is retrieved dynamically through functionality of the `AnoServices` and `Service` classes. You have the option of retrieving the strings in this manner or including them in the software code as shown in the previous examples

Before running this example, you must turn on encryption in the `sqlnet.ora` file. For example, the following lines will turn on AES256, AES192, and AES128 for the encryption and MD5 and SHA1 for the checksum:

```
SQLNET.ENCRYPTION_SERVER = ACCEPTED 
SQLNET.CRYPTO_CHECKSUM_SERVER = ACCEPTED 
SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER= (MD5, SHA1) 
SQLNET.ENCRYPTION_TYPES_SERVER= (AES256, AES192, AES128)
SQLNET.CRYPTO_SEED = 2z0hslkdharUJCFtkwbjOLbgwsj7vkqt3bGoUylihnvkhgkdsbdskkKGhdk
```

Example 9-3 Setting Data Encryption and Integrity Parameters

```
import java.sql.*;
import java.util.Properties;
import oracle.net.ano.AnoServices;
import oracle.jdbc.*;
 
public class DemoAESAndSHA1
{
  static final String USERNAME= "scott";
  static final String PASSWORD= "tiger";
  static final String URL = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=WXYZ)(PORT=5561))"
  +"(CONNECT_DATA=(SERVICE_NAME=mydatabaseinstance)))";
 
  public static final void main(String[] argv)
  {
    DemoAESAndSHA1 demo = new DemoAESAndSHA1();
    try
    {
      demo.run();
    }catch(SQLException ex)
    {
      ex.printStackTrace();
    }
  }
 
  void run() throws SQLException
  {
    OracleDriver dr = new OracleDriver();
    Properties prop = new Properties();
 
    // We require the connection to be encrypted with either AES256 or AES192.
    // If the database doesn't accept such a security level, then the connection attempt will fail.
    
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL,AnoServices.ANO_REQUIRED);
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES,"( " + AnoServices.ENCRYPTION_AES256
     + "," + AnoServices.ENCRYPTION_AES192 + ")");
 
    // We also require the use of the SHA1 algorithm for data integrity checking.
    
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL,AnoServices.ANO_REQUIRED);
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES,
"( " + AnoServices.CHECKSUM_SHA1 + " )");
    prop.setProperty("user",DemoAESAndSHA1.USERNAME);
    prop.setProperty("password",DemoAESAndSHA1.PASSWORD);
    OracleConnection oraConn = (OracleConnection)dr.connect(DemoAESAndSHA1.URL,prop);
    System.out.println("Connection created! Encryption algorithm is: " + oraConn.getEncryptionAlgorithmName() + ", data 
    integrity algorithm is: " + oraConn.getDataIntegrityAlgorithmName());    
    oraConn.close();
  }
  
}
```

## Support for SSL

Oracle Database 11g provides support for the Secure Sockets Layer (SSL) protocol. SSL is a widely used industry standard protocol that provides secure communication over a network. SSL provides authentication, data encryption, and data integrity. It provides a secure enhancement to the standard TCP/IP protocol, which is used for Internet communication.

SSL uses digital certificates that comply with the X.509v3 standard for authentication and a public and private key pair for encryption. SSL also uses secret key cryptography and digital signatures to ensure privacy and integrity of data. When a network connection over SSL is initiated, the client and server perform an SSL handshake that includes the following steps:

- Client and server negotiate about the cipher suites to use. This includes deciding on the encryption algorithms to be used for data transfer.
- Server sends its certificate to the client, and the client verifies that the certificate was signed by a trusted certification authority (CA). This step verifies the identity of the server.
- If client authentication is required, the client sends its own certificate to the server, and the server verifies that the certificate was signed by a trusted CA.
- Client and server exchange key information using public key cryptography. Based on this information, each generates a session key. All subsequent communications between the client and the server is encrypted and decrypted by using this set of session keys and the negotiated cipher suite.

Note:

In Oracle Database 11g Release 1 (11.1), SSL authentication is supported in the thin driver. So, you do not need to provide a user name/password pair if you are using SSL authentication.

SSL Terminology

The following terms are commonly used in the SSL context:

- certificate: A certificate is a digitally signed document that binds a public key with an entity. The certificate can be used to verify that the public key belongs to that individual.
- certification authority: A certification authority (CA), also known as certificate authority, is an entity which issues digitally signed certificates for use by other parties.
- cipher suite: A cipher suite is a set of cryptographic algorithms and key sizes used to encrypt data sent over an SSL-enabled network.
- private key: A private key is a secret key, which is never transmitted over a network. The private key is used to decrypt a message that has been encrypted using the corresponding public key. It is also used to sign certificates. The certificate is verified using the corresponding public key.
- public key: A public key is an encryption key that can be made public or sent by ordinary means such as an e-mail message. The public key is used for encrypting the message sent over SSL. It is also used to verify a certificate signed by the corresponding private key.
- wallet: A wallet is a password-protected container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates required by SSL.

Java Version of SSL

The Java Secure Socket Extension (JSSE) provides a framework and an implementation for a Java version of the SSL and TLS protocols. JSSE provides support for data encryption, server and client authentication, and message integrity. It abstracts the complex security algorithms and handshaking mechanisms and simplifies application development by providing a building block for application developers, which they can directly integrate into their applications. JSSE is integrated into Java Development Kit (JDK) 1.4 and later, and supports SSL version 2.0 and 3.0.

Oracle strongly recommends that you have a clear understanding of the JavaTM Secure Socket Extension (JSSE) framework by Sun Microsystems before using SSL in the Oracle JDBC drivers.

The JSSE standard application programming interface (API) is available in the `javax.net`, `javax.net.ssl`, and `javax.security.cert` packages. These packages provide classes for creating and configuring sockets, server sockets, SSL sockets, and SSL server sockets. The packages also provide a class for secure HTTP connections, a public key certificate API compatible with JDK1.1-based platforms, and interfaces for key and trust managers.

SSL works the same way, as in any networking environment, in Oracle Database 11g. This section covers the following:

- Managing Certificates and Wallets
- Keys and certificates containers

### Managing Certificates and Wallets

To establish an SSL connection with a JDBC client, Thin or OCI, Oracle database server sends its certificate, which is stored in its wallet. The client may or may not need a certificate or wallet depending on the server configuration.

The Oracle JDBC Thin driver uses the JSSE framework to create an SSL connection. It uses the default provider (SunJSSE) to create an SSL context. However you can provide your own provider.

You do not need a certificate for the client, unless the `SSL_CLIENT_AUTHENTICATION` parameter is set on the server.

### Keys and certificates containers

Java clients can use multiple types of containers such as Oracle wallets, JKS, PKCS12, and so on, as long as a provider is available. For Oracle wallets, OraclePKI provider must be used because the PKCS12 support provided by SunJSSE provider does not support all the features of PKCS12. In order to use OraclePKI provider, the following JARs are required:

- `oraclepki.jar`
- `osdt_cert.jar`
- `osdt_core.jar`

All these JAR files should be under `$ORACLE_HOME/jlib directory`.

## Support for Kerberos

Since Oracle Database 11g Release 1 (11.1) support for Kerberos has been introduced. Kerberos is a network authentication protocol that provides the tools of authentication and strong cryptography over the network. Kerberos helps you secure your information systems across your entire enterprise by using secret-key cryptography. The Kerberos protocol uses strong cryptography so that a client or a server can prove its identity to its server or client across an insecure network connection. After a client and server have used Kerberos to prove their identity, they can also encrypt all of their communications to assure privacy and data integrity as they go about their business.

The Kerberos architecture is centered around a trusted authentication service called the key distribution center, or KDC. Users and services in a Kerberos environment are referred to as principals; each principal shares a secret, such as a password, with the KDC. A principal can be a user such as `scott` or a database server instance.

### Configuring Windows to Use Kerberos

A good Kerberos client providing `klist, kinit,` and other tools, can be found at the following link:

```
http://web.mit.edu/kerberos/dist/index.html
```

This client also provides a nice GUI.

You need to make the following changes to configure Kerberos on your Windows machine:

1. Right-click the My Computer icon on your desktop.
2. Select Properties. The System Properties dialog box is displayed.
3. Select the Advanced tab.
4. Click Environment Variables. The Environment Variables dialog box is displayed.
5. Click New to add a new user variable. The New User Variable dialog box is displayed.
6. Enter `KRB5CCNAME` in the Variable name field.
7. Enter `FILE:C:\Documents and Settings\` `<user_name>` `\krb5cc` in the Variable value field.
8. Click OK to close the New User Variable dialog box.
9. Click OK to close the Environment Variables dialog box.
10. Click OK to close the System Properties dialog box.

Note:

`C:\WINDOWS\krb5.ini` file has the same content as `krb5.conf` file.

### Configuring Oracle Database to Use Kerberos

Perform the following steps to configure Oracle Database to use Kerberos:

1. Use the following command to connect to the database:
	```
	SQL> connect system
	Enter password: password
	```
2. Use the following commands to create a user `CLIENT@US.ORACLE.COM` that is identified externally:
	```
	SQL> create user "CLIENT@US.ORACLE.COM" identified externally;
	SQL> grant create session to "CLIENT@US.ORACLE.COM";
	```
3. Use the following commands to connect to the database as `sysdba` and dismount it:
	```
	SQL> connect / as sysdba
	SQL> shutdown immediate;
	```
4. Add the following line to `$T_WORK/t_init1.ora` file:
	```
	OS_AUTHENT_PREFIX=""
	```
5. Use the following command to restart the database:
	```
	SQL> startup pfile=t_init1.ora
	```
6. Modify the `sqlnet.ora` file to include the following lines:
	```
	names.directory_path = (tnsnames)
	#Kerberos
	sqlnet.authentication_services = (beq,kerberos5)
	sqlnet.authentication_kerberos5_service = dbji
	sqlnet.kerberos5_conf = /home/Jdbc/Security/kerberos/krb5.conf
	sqlnet.kerberos5_keytab = /home/Jdbc/Security/kerberos/dbji.oracleserver
	sqlnet.kerberos5_conf_mit = true
	sqlnet.kerberos_cc_name = /tmp/krb5cc_5088
	# logging (optional):
	trace_level_server=16 
	trace_directory_server=/scratch/sqlnet/
	```
7. Use the following commands to verify that you can connect through SQL\*Plus:
	```
	> kinit client
	> klist
	     Ticket cache: FILE:/tmp/krb5cc_5088
	     Default principal: client@US.ORACLE.COM
	    
	     Valid starting     Expires            Service principal
	     06/22/06 07:13:29  06/22/06 17:13:29  krbtgt/US.ORACLE.COM@US.ORACLE.COM
	    
	    
	     Kerberos 4 ticket cache: /tmp/tkt5088
	     klist: You have no tickets cached
	> sqlplus '/@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=oracleserver.mydomain.com)(PORT=5529))
	(CONNECT_DATA=(SERVICE_NAME=mydatabaseinstance)))'
	```

Note:

For information about using Kerberos, refer to the following web sites
```
http://www.microsoft.com/windowsserver2003/technologies/security/kerberos/default.mspx
http://redhatpartnerweb.com/docs/manuals/linux/RHL-7.3-Manual/ref-guide/s1-kerberos-server.html
```

### Code Example

This following example demonstrates the new Kerberos authentication feature that is part of Oracle Database 11g Release 2 (11.2) JDBC thin driver. This demo covers two scenarios:

- In the first scenario, the OS maintains the user name and credentials. The credentials are stored in the cache and the driver retrieves the credentials before trying to authenticate to the server. This scenario is in the module `connectWithDefaultUser()`.
	Note:
	1. Before you run this part of the demo, use the following command to verify that you have valid credentials:
		```
		> /usr/kerberos/bin/kinit client
		where, the password is welcome.
		```
	2. Use the following command to list your tickets:
		```
		> /usr/kerberos/bin/klist
		```
- The second scenario covers the case where the application wants to control the user credentials. This is the case of the application server where multiple web users have their own credentials. This scenario is in the module `connectWithSpecificUser().`
	Note:
	To run this demo, you need to have a working setup, that is, a Kerberos server up and running, and an Oracle database server that is configured to use Kerberos authentication. You then need to change the URLs used in the example to compile and run it.

Example 9-4 Using Kerberos Authentication to Connect to the Database

```
import com.sun.security.auth.module.Krb5LoginModule;
import java.io.IOException;
 
import java.security.PrivilegedExceptionAction;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
 
import java.util.HashMap;
import java.util.Properties;
import javax.security.auth.Subject;
import javax.security.auth.callback.Callback;
import javax.security.auth.callback.CallbackHandler;
import javax.security.auth.callback.PasswordCallback;
import javax.security.auth.callback.UnsupportedCallbackException;
 
import oracle.jdbc.OracleConnection;
import oracle.jdbc.OracleDriver;
import oracle.net.ano.AnoServices;
public class KerberosJdbcDemo
{
  String url ="jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)"+
    "(HOST=oracleserver.mydomain.com)(PORT=5561))(CONNECT_DATA=" +
    "(SERVICE_NAME=mydatabaseinstance)))";
 
  public static void main(String[] arv)
  {
    /* If you see the following error message [Mechanism level: Could not load
     * configuration file c:\winnt\krb5.ini (The system cannot find the path 
     * specified] it's because the JVM cannot locate your kerberos config file.
     * You have to provide the location of the file. For example, on Windows,
     * the MIT Kerberos client uses the config file: C\WINDOWS\krb5.ini:
     */
    // System.setProperty("java.security.krb5.conf","C:\\WINDOWS\\krb5.ini");
    System.setProperty("java.security.krb5.conf","/home/Jdbc/Security/kerberos/krb5.conf");
    
    KerberosJdbcDemo kerberosDemo = new KerberosJdbcDemo();
    try
    {
      System.out.println("Attempt to connect with the default user:");
      kerberosDemo.connectWithDefaultUser();
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
    try
    {
      System.out.println("Attempt to connect with a specific user:");
      kerberosDemo.connectWithSpecificUser();
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
  
 
  void connectWithDefaultUser() throws SQLException
  {
    OracleDriver driver = new OracleDriver();
    Properties prop = new Properties();
    
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_SERVICES,
      "("+AnoServices.AUTHENTICATION_KERBEROS5+")");  
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_KRB5_MUTUAL,
      "true");    
 
    /* If you get the following error [Unable to obtain Princpal Name for 
     * authentication] although you know that you have the right TGT in your
     * credential cache, then it's probably because the JVM can't locate your
     * cache.
     *
     * Note that the default location on windows is "C:\Documents and Settings\krb5cc_username".
     */
 
    // prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_KRB5_CC_NAME,
    /*
      On linux:
         > which kinit
         /usr/kerberos/bin/kinit
         > ls -l /etc/krb5.conf 
         lrwxrwxrwx    1 root  root   47 Jun 22 06:56 /etc/krb5.conf -> /home/Jdbc/Security/kerberos/krb5.conf
    
         > kinit client
         Password for client@US.ORACLE.COM: 
         > klist
         Ticket cache: FILE:/tmp/krb5cc_5088
         Default principal: client@US.ORACLE.COM
 
         Valid starting     Expires            Service principal
         11/02/06 09:25:11  11/02/06 19:25:11  krbtgt/US.ORACLE.COM@US.ORACLE.COM
 
 
         Kerberos 4 ticket cache: /tmp/tkt5088
         klist: You have no tickets cached
    */
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_KRB5_CC_NAME,
                     "/tmp/krb5cc_5088");
    Connection conn  = driver.connect(url,prop);
    String auth = ((OracleConnection)conn).getAuthenticationAdaptorName();
    System.out.println("Authentication adaptor="+auth);
    printUserName(conn);
    conn.close();
  }
 
  
  void connectWithSpecificUser() throws Exception
  {
    Subject specificSubject = new Subject();
    
    // This first part isn't really meaningful to the sake of this demo. In
    // a real world scenario, you have a valid "specificSubject" Subject that
    // represents a web user that has valid Kerberos credentials.
    Krb5LoginModule krb5Module = new Krb5LoginModule();
    HashMap sharedState = new HashMap();
    HashMap options = new HashMap();
    options.put("doNotPrompt","false");
    options.put("useTicketCache","false");
    options.put("principal","client@US.ORACLE.COM");
    
    krb5Module.initialize(specificSubject,newKrbCallbackHandler(),sharedState,options);
    boolean retLogin = krb5Module.login();
    krb5Module.commit();
    if(!retLogin)
      throw new Exception("Kerberos5 adaptor couldn't retrieve credentials (TGT) from the cache"); 
      
    // to use the TGT from the cache:   
    // options.put("useTicketCache","true");
    // options.put("doNotPrompt","true");
    // options.put("ticketCache","C:\\Documents and Settings\\user\\krb5cc");
    // krb5Module.initialize(specificSubject,null,sharedState,options);
 
 
    // Now we have a valid Subject with Kerberos credentials. The second scenario
    // really starts here:
    // execute driver.connect(...) on behalf of the Subject 'specificSubject':
    Connection conn = 
      (Connection)Subject.doAs(specificSubject, new PrivilegedExceptionAction()
        {
          public Object run()
          {
            Connection con = null;
            Properties prop = new Properties();
            prop.setProperty(AnoServices.AUTHENTICATION_PROPERTY_SERVICES, 
                             "(" + AnoServices.AUTHENTICATION_KERBEROS5 + ")");
            try
            {
              OracleDriver driver = new OracleDriver();
              con = driver.connect(url, prop);
 
            } catch (Exception except)
            {
              except.printStackTrace();
            }
            return con;
          }
        });
 
    String auth = ((OracleConnection)conn).getAuthenticationAdaptorName();
    System.out.println("Authentication adaptor="+auth);
    printUserName(conn);
    conn.close();
  }
  
  void printUserName(Connection conn) throws SQLException
  {
    Statement stmt = null;
    try
    {
      stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery("select user from dual");
      while(rs.next())
        System.out.println("User is:"+rs.getString(1));
      rs.close();
    }
    finally
    {
      if(stmt != null)
        stmt.close();
    }
  }
}
 
class KrbCallbackHandler implements CallbackHandler
{
 public void handle(Callback[] callbacks) throws IOException, 
                                                 UnsupportedCallbackException
 {
   for (int i = 0; i < callbacks.length; i++)
   {
     if (callbacks[i] instanceof PasswordCallback)
     {
       PasswordCallback pc = (PasswordCallback)callbacks[i];
       System.out.println("set password to 'welcome'");
       pc.setPassword((new String("welcome")).toCharArray());
     } else
     {
       throw new UnsupportedCallbackException(callbacks[i], 
                                              "Unrecognized Callback");
     }
   }
 }
}
```

## Support for RADIUS

Since Oracle Database 11g Release 1 (11.1), support for Remote Authentication Dial-In User Service (RADIUS) has been introduced. RADIUS is a client/server security protocol that is most widely known for enabling remote authentication and access. Oracle Advanced Security uses this standard in a client/server network environment to enable use of any authentication method that supports the RADIUS protocol. RADIUS can be used with a variety of authentication mechanisms, including token cards and smart cards. This section contains the following sections:

- Configuring Oracle Database to Use RADIUS
- Code Example

### Configuring Oracle Database to Use RADIUS

Perform the following steps to configure Oracle Database to use RADIUS:

1. Use the following command to connect to the database:
	```
	SQL> connect system
	Enter password: password
	```
2. Use the following commands to create a new user `aso` from within a database:
	```
	SQL> create user aso identified externally;
	SQL> grant create session to aso;
	```
3. Use the following commands to connect to the database as `sysdba` and dismount it:
	```
	SQL> connect / as sysdba
	SQL> shutdown immediate;
	```
4. Add the following lines to the `t_init1.ora` file:
	```
	os_authent_prefix = ""
	```
	Note:
	Once the test is over, you need to revert the preceding changes made to the t\_init1.ora file.
5. Use the following command to restart the database:
	```
	SQL> startup pfile=?/work/t_init1.ora
	```
6. Modify the `sqlnet.ora` file so that it contains only these lines:
	```
	sqlnet.authentication_services = ( beq, radius)
	sqlnet.radius_authentication = <RADUIUS_SERVER_HOST_NAME>
	sqlnet.radius_authentication_port = 1812
	sqlnet.radius_authentication_timeout = 120
	sqlnet.radius_secret=/home/Jdbc/Security/radius/radius_key
	# logging (optional):
	trace_level_server=16
	trace_directory_server=/scratch/sqlnet/
	```
7. Use the following command to verify that you can connect through SQL\*Plus:
	```
	>sqlplus 'aso/1234@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=oracleserver.mydomain.com)(PORT=5529))
	(CONNECT_DATA=(SERVICE_NAME=mydatabaseinstance)))'
	```

### Code Example

This example demonstrates the new RADIUS authentication feature that is a part of Oracle Database 11g Release 2 (11.2) JDBC thin driver. You need to have a working setup, that is, a RADIUS server up and running, and an Oracle database server that is configured to use RADIUS authentication. You then need to change the URLs given in the example to compile and run it.

Example 9-5 Using RADIUS Authentication to Connect to the Database

```
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
import oracle.jdbc.OracleConnection;
import oracle.jdbc.OracleDriver;
import oracle.net.ano.AnoServices;
public class RadiusJdbcDemo
{  
  String url ="jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)"+
    "(HOST=oracleserver.mydomain.com)(PORT=5561))(CONNECT_DATA=" +
    "(SERVICE_NAME=mydatabaseinstance)))";
 
  public static void main(String[] arv)
  {
    RadiusJdbcDemo radiusDemo = new RadiusJdbcDemo();
    try
    {
      radiusDemo.connect();
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
  
  /*
   * This method attempts to logon to the database using the RADIUS
   * authentication protocol.
   * 
   * It should print the following output to stdout:
   * -----------------------------------------------------
   * Authentication adaptor=RADIUS
   * User is:ASO
   * -----------------------------------------------------
   */
  void connect() throws SQLException
  {
    OracleDriver driver = new OracleDriver();
    Properties prop = new Properties();
    
    prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_SERVICES,
      "("+AnoServices.AUTHENTICATION_RADIUS+")");
    // The user "aso" needs to be properly setup on the radius server with
    // password "1234".
    prop.setProperty("user","aso");
    prop.setProperty("password","1234");
    
    Connection conn  = driver.connect(url,prop);
    String auth = ((OracleConnection)conn).getAuthenticationAdaptorName();
    System.out.println("Authentication adaptor="+auth);
    printUserName(conn);
    conn.close();
  }
 
  
  void printUserName(Connection conn) throws SQLException
  {
    Statement stmt = null;
    try
    {
      stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery("select user from dual");
      while(rs.next())
        System.out.println("User is:"+rs.getString(1));
      rs.close();
    }
    finally
    {
      if(stmt != null)
        stmt.close();
    }
  }
}
```

## Secure External Password Store

As an alternative for large-scale deployments where applications use password credentials to connect to databases, it is possible to store such credentials in a client-side Oracle wallet. An Oracle wallet is a secure software container that is used to store authentication and signing credentials.

Storing database password credentials in a client-side Oracle wallet eliminates the need to embed user names and passwords in application code, batch jobs, or scripts. This reduces the risk of exposing passwords in the scripts and application code, and simplifies maintenance because you do not need to change your code each time user names and passwords change. In addition, if you do not have to change the application code, then it also becomes easier to enforce password management policies for these user accounts.

You can set the `oracle.net.wallet_location` connection property to specify the wallet location. The JDBC driver can then retrieve the user name and password pair from this wallet.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG9515) for information about configuring your client to use secure external password store and for information about managing credentials in it.
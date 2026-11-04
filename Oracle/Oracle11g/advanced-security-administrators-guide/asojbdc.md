---
title: "Configuring Network Authentication, Encryption, and Integrity for Thin JDBC Clients"
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asojbdc.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## 10 Configuring Network Authentication, Encryption, and Integrity for Thin JDBC Clients

This chapter describes the Java implementation of Oracle Advanced Security, which lets thin Java Database Connectivity (JDBC) clients securely connect to Oracle Databases. This chapter contains the following topics:

- About the Java Implementation
- Configuration Parameters
	See Also:
	[Oracle Database JDBC Developer's Guide and Reference](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm), for information about JDBC, including examples

## 10.1 About the Java Implementation

The Java implementation of Oracle Advanced Security provides network authentication, encryption and integrity protection for Thin JDBC clients communicating with Oracle Databases that have Oracle Advanced Security enabled.

This section contains the following topics:

### 10.1.1 Java Database Connectivity Support

[Java Database Connectivity (JDBC)](asogls.md), an industry-standard Java interface, is a Java standard for connecting to a relational database from a Java program. Sun Microsystems defined the JDBC standard and Oracle implements and extends the standard with its own JDBC drivers.

Oracle JDBC drivers are used to create JDBC applications to communicate with Oracle databases. Oracle implements two types of JDBC drivers: Thick JDBC drivers built on top of the C-based Oracle Net client, as well as a Thin (Pure Java) JDBC driver to support downloadable applets. Oracle extensions to JDBC include the following features:

- Data access and manipulation
- LOB access and manipulation
- Oracle object type mapping
- Object reference access and manipulation
- Array access and manipulation
- Application performance enhancement

### 10.1.2 Securing Thin JDBC

As the Thin JDBC driver is designed to be used with downloadable applets used over the Internet, Oracle designed a 100% Java implementation of Oracle Advanced Security authentication, encryption, and integrity algorithms, for use with thin clients. Oracle Advanced Security provides the following features for Thin JDBC:

- Strong Authentication
- Data encryption
- Data integrity checking
- Secure connections from Thin JDBC clients to the Oracle RDBMS
- Ability for developers to build applets that transmit data over a secure communication channel
- Secure connections from middle tier servers with Java Server Pages (JSP) to the Oracle RDBMS
- Secure connections from Oracle Database 11g Release 2 (11.2) to older versions of Oracle databases with Oracle Advanced Security installed

The Oracle JDBC Thin driver supports Oracle Advanced Security SSL implementation and third party authentication methods such as RADIUS and Kerberos. Thin JDBC support for authentication methods like RADIUS, Kerberos, and SSL were introduced in Oracle Database 11g Release 1 (11.1).

The Oracle Advanced Security Java implementation provides Java versions of the following encryption algorithms:

- `AES256`: AES 256-bit key
- `AES192`: AES 192-bit key
- `AES128`: AES 128-bit key
- `3DES168`: 3-key 3DES
- `3DES112`: 2-key 3DES

Note:

In the preceding list of algorithms, CBC refers to the Cipher Block Chaining mode.

Thin JDBC support for the Advanced Encryption Standard (AES) has been newly introduced in Oracle Database 11g Release 2 (11.2).

In addition, this implementation provides data integrity checking for Thin JDBC using Secure Hash Algorithm (`SHA1`). Thin JDBC support for `SHA1` was introduced in Oracle Database 11g Release 1 (11.1).

See Also:

[Oracle Database JDBC Developer's Guide and Reference](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for details on configuring authentication, encryption, and integrity for thin JDBC clients

### 10.1.3 Implementation Overview

On the server side, the negotiation of algorithms and the generation of keys function exactly the same as Oracle Advanced Security native encryption. This enables backward and forward compatibility of clients and servers.

On the client side, the algorithm negotiation and key generation occur in exactly the same manner as OCI clients. The client and server negotiate encryption algorithms, generate random numbers, use Diffie-Hellman to exchange session keys, and use the Oracle Password Protocol, in the same manner as the traditional Oracle Net clients. Thin JDBC contains a complete implementation of a Oracle Net client in pure Java.

### 10.1.4 Obfuscation

The Java cryptography code is obfuscated. Obfuscation protects Java classes and methods that contain encryption and decryption capabilities with obfuscation software.

Java byte code [obfuscation](asogls.md) is a process frequently used to protect intellectual property written in the form of Java programs. It mixes up Java symbols found in the code. The process leaves the original program structure intact, letting the program run correctly while changing the names of the classes, methods, and variables in order to hide the intended behavior. Although it is possible to decompile and read non-obfuscated Java code, obfuscated Java code is sufficiently difficult to decompile to satisfy U.S. government export controls.

## 10.2 Configuration Parameters

A properties class object containing several configuration parameters is passed to the Oracle Advanced Security interface.

All JDBC connection properties including the ones pertaining to Oracle Advanced Security are defined as constants in the `oracle.jdbc.OracleConnection` interface. The following list enumerates some of these connection properties:

- CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_LEVEL Parameter
- CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_TYPES Parameter
- CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_LEVEL Parameter
- CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_TYPES Parameter
- CONNECTION\_PROPERTY\_THIN\_NET\_AUTHENTICATION\_SERVICES Parameter

See Also:

[Oracle Database JDBC Developer's Guide and Reference](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for detailed information on configuration parameters and configuration examples

### 10.2.1 CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_LEVEL Parameter

This parameter defines the level of security that the client wants to negotiate with the server. Table 10-1 describes this parameters attributes.

Table 10-1 CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_LEVEL Attributes

| Attribute | Description |
| --- | --- |
| Parameter Type | String |
| Parameter Class | Static |
| Permitted Values | `REJECTED`; `ACCEPTED`; `REQUESTED`; `REQUIRED` |
| Default Value | `ACCEPTED` |
| Syntax | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL,``level``);`  where `prop` is an object of the `Properties` class |
| Example | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL,"REQUIRED");`  where `prop` is an object of the `Properties` class |

### 10.2.2 CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_TYPES Parameter

This parameter defines the encryption algorithm to be used. Table 10-2 describes this parameter's attributes.

Table 10-2 CONNECTION\_PROPERTY\_THIN\_NET\_ENCRYPTION\_TYPES Attributes

| Attribute | Description |
| --- | --- |
| Parameter Type | String |
| Parameter Class | Static |
| Permitted Values | `AES256`,`AES192`, `AES128`, `3DES168`, `3DES112` |
| Syntax | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES,``algorithm``);`  where `prop` is an object of the `Properties` class |
| Example | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES, "( AES256, AES192 )");`  where `prop` is an object of the `Properties` class |

### 10.2.3 CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_LEVEL Parameter

This parameter defines the level of security that it wants to negotiate with the server for data integrity. Table 10-3 describes this parameter's attributes.

Table 10-3 CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_LEVEL Attributes

| Attribute | Description |
| --- | --- |
| Parameter Type | String |
| Parameter Class | Static |
| Permitted Values | `REJECTED`; `ACCEPTED`; `REQUESTED`; `REQUIRED` |
| Default Value | `ACCEPTED` |
| Syntax | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL,``level``);`  where `prop` is an object of the `Properties` class |
| Example | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL,"REQUIRED");`  where `prop` is an object of the `Properties` class |

### 10.2.4 CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_TYPES Parameter

This parameter defines the data integrity algorithm to be used. Table 10-4 describes this parameter's attributes.

Table 10-4 CONNECTION\_PROPERTY\_THIN\_NET\_CHECKSUM\_TYPES Attributes

| Attribute | Description |
| --- | --- |
| Parameter Type | String |
| Parameter Class | Static |
| Permitted Values | `SHA1` |
| Syntax | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES,` `algorithm``);`  where `prop` is an object of the `Properties` class |
| Example | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES,"( SHA1 )");`  where `prop` is an object of the `Properties` class |

### 10.2.5 CONNECTION\_PROPERTY\_THIN\_NET\_AUTHENTICATION\_SERVICES Parameter

This parameter determines the authentication service to be used. Table 10-5 describes this parameter's attributes.

Table 10-5 CONNECTION\_PROPERTY\_THIN\_NET\_AUTHENTICATION\_SERVICES Attributes

| Attribute | Description |
| --- | --- |
| Parameter Type | String |
| Parameter Class | Static |
| Permitted Values | `RADIUS, KERBEROS, SSL` |
| Syntax | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_SERVICES,``authentication``);`  where `prop` is an object of the `Properties` class |
| Example | `prop.setProperty(OracleConnection.CONNECTION_PROPERTY_THIN_NET_AUTHENTICATION_SERVICES,"( RADIUS, KERBEROS, SSL)");`  where `prop` is an object of the `Properties` class |

### 10.2.6 AnoServices Constants

The `oracle.net.ano.AnoServices` interface has been updated in this release to include the names of all the encryption, authentication, and checksum algorithms supported by the JDBC Thin driver. The following constants have been added to the oracle.net.ano.AnoServices interface:

```
// ---- SUPPORTED ENCRYPTION ALG -----
public static final String ENCRYPTION_3DES112 = "3DES112";
public static final String ENCRYPTION_3DES168 = "3DES168";
public static final String ENCRYPTION_AES128 = "AES128";
public static final String ENCRYPTION_AES192 = "AES192";
public static final String ENCRYPTION_AES256 = "AES256";
// ---- SUPPORTED INTEGRITY ALG ----
public static final String CHECKSUM_SHA1 = "SHA1";
// ---- SUPPORTED AUTHENTICATION ADAPTORS ----
public static final String AUTHENTICATION_RADIUS = "RADIUS";
public static final String AUTHENTICATION_KERBEROS = "KERBEROS";
```

You can use these constants to set the encryption, integrity, and authentication parameters. Example 10-1 illustrates one such scenario.

Example 10-1 Using AnoServices Constants in JDBC Client Code

```
import java.sql.*;
import java.util.Properties;import oracle.jdbc.*;
import oracle.net.ano.AnoServices;
/**
 * JDBC thin driver demo: new security features in 11gR1.
 * 
 * This program attempts to connect to the database using the JDBC thin
 * driver and requires the connection to be encrypted with either AES256 or AES192
 * and the data integrity to be verified with SHA1.
 * 
 * In order to activate encryption and checksumming in the database you need to 
 * modify the sqlnet.ora file. For example:
 * 
 *   SQLNET.ENCRYPTION_TYPES_SERVER = (AES256,AES192,AES128)
 *   SQLNET.ENCRYPTION_SERVER = accepted
 *   SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER= (SHA1)
 *   SQLNET.CRYPTO_CHECKSUM_SERVER = accepted
 *
 * This output of this program is:
 *   Connection created! Encryption algorithm is: AES256, data integrity algorithm
 *   is: SHA1
 *
 */
public class DemoAESAndSHA1
{
  static final String USERNAME= "hr";
  static final String PASSWORD= "hr";
  static final String URL =
"jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=somehost.us.example.com)(PORT=5561))"  +"(CONNECT_DATA=(SERVICE_NAME=itydemo.regress.rdbms.dev.us.example.com)))";
  
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
    // If the database doesn't accept such a security level, then the connection
    // attempt will fail.
    prop.setProperty(
     
OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_LEVEL,AnoServices.ANO_REQUIRED);
    prop.setProperty(
      OracleConnection.CONNECTION_PROPERTY_THIN_NET_ENCRYPTION_TYPES,      "( " + AnoServices.ENCRYPTION_AES256 + "," +AnoServices.ENCRYPTION_AES192 + ")");
    // We also require the use of the SHA1 algorithm for data integrity checking.
    prop.setProperty(
     
OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_LEVEL,AnoServices.ANO_REQUIRED);
    prop.setProperty(
      OracleConnection.CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPES,      "( " + AnoServices.CHECKSUM_SHA1 + " )");
      
    prop.setProperty("user",DemoAESAndSHA1.USERNAME);
    prop.setProperty("password",DemoAESAndSHA1.PASSWORD);
    OracleConnection oraConn =
 (OracleConnection)dr.connect(DemoAESAndSHA1.URL,prop);
    
    System.out.println("Connection created! Encryption algorithm is: "+oraConn.getEncryptionAlgorithmName()    +", data integrity algorithm is: "+oraConn.getDataIntegrityAlgorithmName());
   
    oraConn.close();
  }
  
}
```
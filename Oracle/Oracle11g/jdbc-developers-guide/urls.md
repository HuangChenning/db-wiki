---
title: Data Sources and URLs
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/urls.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 8 Data Sources and URLs

This chapter discusses connecting applications to databases using Java Database Connectivity (JDBC) data sources, as well as the URLs that describe databases. This chapter contains the following sections:

- Data Sources
- Database URLs and Database Specifiers

## Data Sources

Data sources are standard, general-use objects for specifying databases or other resources to use. The JDBC 2.0 extension application programming interface (API) introduced the concept of data sources. For convenience and portability, data sources can be bound to Java Naming and Directory Interface (JNDI) entities, so that you can access databases by logical names.

The data source facility provides a complete replacement for the previous JDBC `DriverManager` facility. You can use both facilities in the same application, but it is recommended that you transition your application to data sources.

This section covers the following topics:

### Overview of Oracle Data Source Support for JNDI

The JNDI standard provides a way for applications to find and access remote services and resources. These services can be any enterprise services. However, for a JDBC application, these services would include database connections and services.

JNDI allows an application to use logical names in accessing these services, removing vendor-specific syntax from application code. JNDI has the functionality to associate a logical name with a particular source for a desired service.

All Oracle JDBC data sources are JNDI-referenceable. The developer is not required to use this functionality, but accessing databases through JNDI logical names makes the code more portable.

Note:

Using JNDI functionality requires the `jndi.jar` file to be in the `CLASSPATH` environment variable. This file is included with the Java products on the installation CD. You must add it to the `CLASSPATH` environment variable separately. You can also obtain it from the Sun Microsystems Web site, but it is advisable to use the version from Oracle, because it has been tested with the Oracle drivers.

### Features and Properties of Data Sources

By using the data source functionality with JNDI, you do not need to register the vendor-specific JDBC driver class name and you can use logical names for URLs and other properties. This ensures that the code for opening database connections is portable to other environments.

The DataSource Interface and Oracle Implementation

A JDBC data source is an instance of a class that implements the standard `javax.sql.DataSource` interface:

```
public interface DataSource
{
   Connection getConnection() throws SQLException;
   Connection getConnection(String username, String password)
      throws SQLException;
   ...
}
```

Oracle implements this interface with the `OracleDataSource` class in the `oracle.jdbc.pool` package. The overloaded `getConnection` method returns a connection to the database.

To use other values, you can set properties using appropriate setter methods. For alternative user names and passwords, you can also use the `getConnection` method that takes these parameters as input. This would take priority over the property settings.

Note:

The `OracleDataSource` class and all subclasses implement the `java.io.Serializable` and `javax.naming.Referenceable` interfaces.

Properties of DataSource

`The` `OracleDataSource` class, as with any class that implements the `DataSource` interface, provides a set of properties that can be used to specify a database to connect to. These properties follow the JavaBeans design pattern.

Table 8-1 and Table 8-2 list `OracleDataSource` properties. The properties in Table 8-1 are standard properties according to the Sun Microsystems specification. The properties in Table 8-2 are Oracle extensions.

Note:

Oracle does not implement the standard `roleName` property.

Table 8-1 Standard Data Source Properties

| Name | Type | Description |
| --- | --- | --- |
| `databaseName` | `String` | Name of the particular database on the server. Also known as the SID in Oracle terminology. |
| `dataSourceName` | `String` | Name of the underlying data source class. For connection pooling, this is an underlying pooled connection data source class. For distributed transactions, this is an underlying XA data source class. |
| `description` | `String` | Description of the data source. |
| `networkProtocol` | `String` | Network protocol for communicating with the server. For Oracle, this applies only to the JDBC Oracle Call Interface (OCI) drivers and defaults to `tcp`. |
| `password` | `String` | Password for the connecting user. |
| `portNumber` | `int` | Number of the port where the server listens for requests |
| `serverName` | `String` | Name of the database server |
| `user` | `String` | Name for the login |

Note:

For security reasons, there is no `getPassword()` method.

Table 8-2 Oracle Extended Data Source Properties

| Name | Type | Description |
| --- | --- | --- |
| `connectionCacheName` | `String` | Specifies the name of the cache. This cannot be changed after the cache has been created. |
| `connection­Cache­Properties` | `java.util.Properties` | Specifies properties for implicit connection cache. |
| `connectionCachingEnabled` | `Boolean` | Specifies whether implicit connection cache is in use. |
| `connectionProperties` | `java.util.Properties` | Specifies the connection properties. |
| `driverType` | `String` | Specifies Oracle JDBC driver type. It can be one of `oci`, `thin`, or `kprb`. |
| `fastConnectionFailoverEnabled` | `Boolean` | Specifies whether Fast Connection Failover is in use. |
| `implicitCachingEnabled` | `Boolean` | Specifies whether the implicit statement connection cache is enabled. |
| `loginTimeout` | `int` | Specifies the maximum time in seconds that this data source will wait while attempting to connect to a database. |
| `logWriter` | `java.io.PrintWriter` | Specifies the log writer for this data source. |
| `maxStatements` | `int` | Specifies the maximum number of statements in the application cache. |
| `serviceName` | `String` | Specifies the database service name for this data source. |
| `tnsEntry` | `String` | Specifies the TNS entry name. The TNS entry name corresponds to the TNS entry specified in the `tnsnames.ora` configuration file.  Enable this `OracleXADataSource` property when using the Native XA feature with the OCI driver, to access Oracle pre-8.1.6 databases and later. If the `tnsEntry` property is not set when using the Native XA feature, then a `SQLException` with error code ORA-17207 is thrown |
| `url` | `String` | Specifies the URL of the database connection string. Provided as a convenience, it can help you migrate from an older Oracle Database. You can use this property in place of the Oracle `tnsEntry` and `driverType` properties and the standard `portNumber`, `networkProtocol`, `serverName`, and `databaseName` properties. |
| `nativeXA` | `Boolean` | Allows an `OracleXADataSource` using the Native XA feature with the OCI driver, to access Oracle pre-8.1.6 databases and later. If the `nativeXA` property is enabled, be sure to set the `tnsEntry` property as well. This property is only for `OracleXADatasource`.  This `DataSource` property defaults to `false`. |
| `ONSConfiguration` | `String` | Specifies the ONS configuration string that is used to remotely subscribe to FAN/ONS events. |

Note:

- This table omits properties that supported the deprecated connection cache based on `OracleConnectionCache`.
- Because Native XA performs better than Java XA, use Native XA whenever possible.

Use the `setConnectionProperties` method to set the properties of the connection and the `setConnectionCacheProperties` method to set the properties of the connection cache.

For more information about the properties of the connection refer to "Supported Connection Properties".

For more information about the properties of the connection cache refer to ["Connection Cache Properties"](concache.md).

If you are using the server-side internal driver, that is, the `driverType` property is set to `kprb`, then any other property settings are ignored.

If you are using the JDBC Thin or OCI driver, then note the following:

- A URL setting can include settings for `user` and `password`, as in the following example, in which case this takes precedence over individual `user` and `password` property settings:
	```
	jdbc:oracle:thin:scott/tiger@localhost:1521:orcl
	```
- Settings for `user` and `password` are required, either directly through the URL setting or through the `getConnection` call. The `user` and `password` settings in a `getConnection` call take precedence over any property settings.
- If the `url` property is set, then any `tnsEntry`, `driverType`, `portNumber`, `networkProtocol`, `serverName`, and `databaseName` property settings are ignored.
- If the `tnsEntry` property is set, which presumes the `url` property is not set, then any `databaseName`, `serverName`, `portNumber`, and `networkProtocol` settings are ignored.
- If you are using an OCI driver, which presumes the `driverType` property is set to `oci`, and the `networkProtocol` is set to `ipc`, then any other property settings are ignored.

Also, note that `getConnectionCacheName()` will return the name of the cache only if the `ConnectionCacheName` property of the data source is set after caching is enabled on the data source.

### Creating a Data Source Instance and Connecting

This section shows an example of the most basic use of a data source to connect to a database, without using JNDI functionality. Note that this requires vendor-specific, hard-coded property settings.

Create an `OracleDataSource` instance, initialize its connection properties as appropriate, and get a connection instance, as in the following example:

```
OracleDataSource ods = new OracleDataSource();
ods.setDriverType("oci");
ods.setServerName("dlsun999");
ods.setNetworkProtocol("tcp");
ods.setDatabaseName("816");
ods.setPortNumber(1521);
ods.setUser("scott");
ods.setPassword("tiger");
Connection conn = ods.getConnection();
```

Or, optionally, override the user name and password, as follows:

```
Connection conn = ods.getConnection("bill", "lion");
```

### Creating a Data Source Instance, Registering with JNDI, and Connecting

This section exhibits JNDI functionality in using data sources to connect to a database. Vendor-specific, hard-coded property settings are required only in the portion of code that binds a data source instance to a JNDI logical name. From that point onward, you can create portable code by using the logical name in creating data sources from which you will get your connection instances.

Note:

Creating and registering data sources is typically handled by a JNDI administrator, not in a JDBC application.

Initialize Data Source Properties

Create an `OracleDataSource` instance, and then initialize its properties as appropriate, as in the following example:

```
OracleDataSource ods = new OracleDataSource();
ods.setDriverType("oci");
ods.setServerName("dlsun999");
ods.setNetworkProtocol("tcp");
ods.setDatabaseName("816");
ods.setPortNumber(1521);
ods.setUser("scott");
ods.setPassword("tiger");
```

Register the Data Source

Once you have initialized the connection properties of the `OracleDataSource` instance `ods`, as shown in the preceding example, you can register this data source instance with JNDI, as in the following example:

```
Context ctx = new InitialContext();
ctx.bind("jdbc/sampledb", ods);
```

Calling the JNDI `InitialContext()` constructor creates a Java object that references the initial JNDI naming context. System properties, which are not shown, instruct JNDI which service provider to use.

The `ctx.bind` call binds the `OracleDataSource` instance to a logical JNDI name. This means that anytime after the `ctx.bind` call, you can use the logical name `jdbc/sampledb` in opening a connection to the database described by the properties of the `OracleDataSource` instance `ods`. The logical name `jdbc/sampledb` is logically bound to this database.

The JNDI namespace has a hierarchy similar to that of a file system. In this example, the JNDI name specifies the subcontext `jdbc` under the root naming context and specifies the logical name `sampledb` within the `jdbc` subcontext.

The `Context` interface and `InitialContext` class are in the standard `javax.naming` package.

Note:

The JDBC 2.0 Specification requires that all JDBC data sources be registered in the `jdbc` naming subcontext of a JNDI namespace or in a child subcontext of the `jdbc` subcontext.

Open a Connection

To perform a lookup and open a connection to the database logically bound to the JNDI name, use the logical JNDI name. Doing this requires casting the lookup result, which is otherwise a Java `Object`, to `OracleDataSource` and then using its `getConnection` method to open the connection.

Here is an example:

```
OracleDataSource odsconn = (OracleDataSource)ctx.lookup("jdbc/sampledb");
Connection conn = odsconn.getConnection();
```

### Supported Connection Properties

For a detailed list of connection properties that Oracle JDBC drivers support, see the Javadoc.

### Configuring Database Remote Login

Before the JDBC Thin driver can connect to the database as `SYSDBA`, you must configure the user, because Oracle Database security system requires a password file for remote connections as an administrator. Perform the following:

1. Set a password file on the server-side or on the remote database, using the `orapwd` password utility. You can add a password file for user `sys` as follows:
	- In UNIX
		```
		orapwd file=$ORACLE_HOME/dbs/orapw entries=200
		Enter password: password
		```
		- In Microsoft Windows
		```
		orapwd file=%ORACLE_HOME%\database\PWDsid_name
		.ora entries=200
		Enter password: password
		```
	`file` must be the name of the password file. `password` is the password for the user `SYS`. It can be altered using the `ALTER USER` statement in SQL Plus. You should set `entries` to a value higher than the number of entries you expect.
	The syntax for the password file name is different on Microsoft Windows and UNIX.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
2. Enable remote login as `sysdba`. This step grants `SYSDBA` and `SYSOPER` system privileges to individual users and lets them connect as themselves.
	Stop the database, and add the following line to `init` `service_name``.ora`, in UNIX, or `init.ora`, in Microsoft Windows:
	```
	remote_login_passwordfile=exclusive
	```
	The `init` `service_name``.ora` file is located at `ORACLE_HOME` `/dbs/` and also at `ORACLE_HOME` `/admin/db_name/pfile/`. Ensure that you keep the two files synchronized.
	The `init.ora` file is located at `%ORACLE_BASE%\ADMIN\db_name\pfile\`.
3. Change the password for the `SYS` user. This is an optional step.
	```
	PASSWORD sys
	       Changing password for sys
	New password: password
	Retype new password: password
	```
4. Verify whether `SYS` has the `SYSDBA` privilege.
	```
	SQL> select * from v$pwfile_users;
	USERNAME                         SYSDB        SYSOP
	----------------------           ---------    ---------
	SYS                              TRUE         TRUE
	```
5. Restart the remote database.

Example 8-1 Using SYS Login To Make a Remote Connection

```
//This example works regardless of language settings of the database.
 /** case of remote connection using sys **/
import java.sql.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.*;
// create an OracleDataSource
OracleDataSource ods = new OracleDataSource();
// set connection properties
java.util.Properties prop = new java.util.Properties();
prop.put("user", "sys");
prop.put("password", "sys");
prop.put("internal_logon", "sysoper");
ods.setConnectionProperties(prop);
// set the url
// the url can use oci driver as well as:
// url = "jdbc:oracle:oci8:@inst1"; the inst1 is a remote database
String url = "jdbc:oracle:thin:@//myHost:1521/service_name";
ods.setURL(url);
// get the connection
Connection conn = ods.getConnection();
...
```

### Bequeath Connection and SYS Logon

The following example illustrates how to use the `internal_logon` and `SYSDBA` arguments to specify the `SYS` login. This example works regardless of the database's national-language settings of the database.

```
/** Example of bequeath connection **/
import java.sql.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.*;
 
// create an OracleDataSource instance
OracleDataSource ods = new OracleDataSource();
 
// set neccessary properties
java.util.Properties prop = new java.util.Properties();
prop.put("user", "sys");
prop.put("password", "sys");
prop.put("internal_logon", "sysdba");
ods.setConnectionProperties(prop);
 
// the url for bequeath connection
String url = "jdbc:oracle:oci8:@";
ods.setURL(url);
 
// retrieve the connection
Connection conn = ods.getConnection();
...
```

### Properties for Oracle Performance Extensions

Some of the connection properties are for use with Oracle performance extensions. Setting these properties is equivalent to using corresponding methods on the `OracleConnection` object, as follows:

- Setting the `defaultRowPrefetch` property is equivalent to calling `setDefaultRowPrefetch`.
- Setting the `remarksReporting` property is equivalent to calling `setRemarksReporting`.
	See Also:
	["Reporting DatabaseMetaData TABLE\_REMARKS"](oraperf.md)
- Setting the `defaultBatchValue` property is equivalent to calling `setDefaultExecuteBatch`
	See Also:
	["Oracle Update Batching"](oraperf.md)

Example

The following example shows how to use the `put` method of the `java.util.Properties` class, in this case, to set Oracle performance extension parameters.

```
//import packages and register the driver
import java.sql.*;
import java.math.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.OracleDataSource;

//specify the properties object
java.util.Properties info = new java.util.Properties();
info.put ("user", "scott");
info.put ("password", "tiger");
info.put ("defaultRowPrefetch","20");
info.put ("defaultBatchValue", "5");

//specify the datasource object 
OracleDataSource ods = new OracleDataSource();
ods.setURL("jdbc:oracle:thin:@//myhost:1521/orcl");
ods.setUser("scott");
ods.setPassword("tiger");
ods.setConnectionProperties(info);
...
```

## Database URLs and Database Specifiers

Database URLs are strings. The complete URL syntax is:

```
jdbc:oracle:driver_type:[username/password]@database_specifier
```

Note:

- The brackets indicate that the `username` `/` `password` pair is optional.
- `kprb`, the internal server-side driver, uses an implicit connection. Database URLs for the server-side driver end after the `driver_type`.

The first part of the URL specifies which JDBC driver is to be used. The supported `driver_type` values are `thin`, `oci`, and `kprb`.

The remainder of the URL contains an optional user name and password separated by a slash, an @, and the database specifier, which uniquely identifies the database to which the application is connected. Some database specifiers are valid only for the JDBC Thin driver, some only for the JDBC OCI driver, and some for both.

Internet Protocol Version 6 Support

This release of Oracle JDBC drivers supports Internet Protocol Version 6 (IPv6) addresses in the JDBC URL and machine names that resolve to IPv6 addresses. IPv6 is a new Network layer protocol designed by the Internet Engineering Task Force (IETF) to replace the current version of Internet Protocol, Internet Protocol Version 4 (IPv4). The primary benefit of IPv6 is a large address space, derived from the use of 128-bit addresses. IPv6 also improves upon IPv4 in areas such as routing, network autoconfiguration, security, quality of service, and so on.

If you want to use a literal IPv6 address in a URL, then you should enclose the literal address enclosed in a left bracket (`[`) and a right bracket (`]`). For example: `[2001:0db8:7654:3210:FEDC:BA98:7654:3210]`. So, a JDBC URL, using a IPv6 address will look like the following:

```
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
  (HOST=[2001:0db8:7654:3210:FEDC:BA98:7654:3210])(PORT=5521))
  (CONNECT_DATA=(SERVICE_NAME=sales.example.com))
```

Note:

All the new System classes that are required for IPv6 support are loaded when Java is enabled during database initialization. So, if your application does not have any IPv6 addressing, then you do not need to change your code to use IPv6 functionality. However, if your application has either IPv6 only or both IPv6 and IPv4 addressing, then you should set the java.net.preferIPv6Addresses system property in the command line. This enables the Oracle JVM to load appropriate libraries. These libraries are loaded once and cannot be reloaded without restarting the Java process. For more information about this system property, refer to [Oracle Database Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10588/chone.htm#JJDEV01410).

Database Specifiers

Table 8-3, shows the possible database specifiers, listing which JDBC drivers support each specifier.

Note:

- Starting Oracle Database 10g, Oracle Service IDs are not supported.
- Starting Oracle Database 10g, Oracle no longer supports Oracle Names as a naming method.

Table 8-3 Supported Database Specifiers

| Specifier | Supported Drivers | Example |
| --- | --- | --- |
| Oracle Net connection descriptor | Thin, OCI | Thin, using an address list:  ``` url="jdbc:oracle:thin:@(DESCRIPTION=   (LOAD_BALANCE=on) (ADDRESS_LIST=   (ADDRESS=(PROTOCOL=TCP)(HOST=host1) (PORT=1521))  (ADDRESS=(PROTOCOL=TCP)(HOST=host2)(PORT=1521)))  (CONNECT_DATA=(SERVICE_NAME=service_name)))" ```  OCI, using a cluster:  ``` "jdbc:oracle:oci:@(DESCRIPTION=   (ADDRESS=(PROTOCOL=TCP)(HOST=cluster_alias)     (PORT=1521))     (CONNECT_DATA=(SERVICE_NAME=service_name)))" ``` |
| Thin-style service name | Thin | Refer to "Thin-style Service Name Syntax" for details.  ``` "jdbc:oracle:thin:scott/tiger@//myhost:1521/myservicename" ``` |
| LDAP syntax | Thin | Refer to LDAP Syntax for details.  ``` "jdbc:oracle:thin:@ldap://ldap.example.com:7777/sales,cn=OracleContext,dc=com" ``` |
| Bequeath connection | OCI | Empty. That is, nothing after @  ``` "jdbc:oracle:oci:scott/tiger/@" ``` |
| TNSNames alias | Thin, OCI | Refer to "TNSNames Alias Syntax" for details.  ``` OracleDataSource ods = new OracleDataSource(); ods.setTNSEntryName("MyTNSAlias"); ``` |

Thin-style Service Name Syntax

Thin-style service names are supported only by the JDBC Thin driver. The syntax is:

```
@//host_name:port_number/service_name
```

For example:

```
jdbc:oracle:thin:scott/tiger@//myhost:1521/myservicename
```

Note:

The JDBC Thin driver supports only the TCP/IP protocol.

TNSNames Alias Syntax

You can find the available `TNSNAMES` entries listed in the `tnsnames.ora` file on the client computer from which you are connecting. On Windows, this file is located in the `ORACLE_HOME` `\NETWORK\ADMIN` directory. On UNIX systems, you can find it in the `ORACLE_HOME` directory or the directory indicated in your `TNS_ADMIN` environment variable.

For example, if you want to connect to the database on host `myhost` as user `scott` with password `tiger` that has a `TNSNAMES` entry of `MyHostString`, then write the following:

```
OracleDataSource ods = new OracleDataSource();
ods.setTNSEntryName("MyTNSAlias");
ods.setUser("scott");
ods.setPassword("tiger");
ods.setDriverType("oci");
Connection conn = ods.getConnection();
```

The `oracle.net.tns_admin` system property must be set to the location of the `tnsnames.ora` file so that the JDBC Thin driver can locate the `tnsnames.ora` file. For example:

```
System.setProperty("oracle.net.tns_admin", "c:\\Temp");
String url = "jdbc:oracle:thin:@tns_entry";
```

Note:

When using TNSNames with the JDBC Thin driver, you must set the `oracle.net.tns_admin` property to the directory that contains your `tnsnames.ora` file.
```
java -Doracle.net.tns_admin=$ORACLE_HOME/network/admin
```

LDAP Syntax

An example of database specifier using the Lightweight Directory Access Protocol (LDAP) syntax is as follows:

```
"jdbc:oracle:thin:@ldap://ldap.example.com:7777/sales,cn=OracleContext,dc=com"
```

When using SSL, change this to:

```
"jdbc:oracle:thin:@ldaps://ldap.example.com:7777/sales,cn=OracleContext,dc=com"
```

Note:

The JDBC Thin driver can use LDAP over SSL to communicate with Oracle Internet Directory if you substitute `ldaps:` for `ldap:` in the database specifier. The LDAP server must be configured to use SSL. If it is not, then the connection attempt will hang.

The JDBC Thin driver supports failover of a list of LDAP servers during the service name resolution process, without the need for a hardware load balancer. Also, client-side load balancing is supported for connecting to LDAP servers. A list of space separated LDAP URLs syntax is used to support failover and load balancing.

When a list of LDAP URLs is specified, both failover and load balancing are enabled by default. The `oracle.net.ldap_loadbalance` connection property can be used to disable load balancing, and the `oracle.net.ldap_failover` connection property can be used to disable failover.

An example, which uses failover, but with client-side load balancing disabled, is as follows:

```
Properties prop = new Properties();
String url = "jdbc:oracle:thin:@ldap://ldap1.example.com:3500/cn=salesdept,cn=OracleContext,dc=com/salesdb " +
"ldap://ldap2.example.com:3500/cn=salesdept,cn=OracleContext,dc=com/salesdb " +
"ldap://ldap3.example.com:3500/cn=salesdept,cn=OracleContext,dc=com/salesdb";

prop.put("oracle.net.ldap_loadbalance", "OFF" );
OracleDataSource ods = new OracleDataSource();
ods.setURL(url);
ods.setConnectionProperties(prop);
```

The JDBC Thin driver supports LDAP nonanonymous bind. A set of JNDI environment properties, which contains authentication information, can be specified for a data source. If a LDAP server is configured as not allowing anonymous bind, then authentication information must be provided to connect to the LDAP server. The following example shows a simple clear-text password authentication:

```
String url = "jdbc:oracle:thin:@ldap://ldap.example.com:7777/sales,cn=salesdept,cn=OracleContext,dc=com";

Properties prop = new Properties();
prop.put("java.naming.security.authentication", "simple");
prop.put("java.naming.security.principal","cn=salesdept,cn=OracleContext,dc=com");
prop.put("java.naming.security.credentials", "mysecret");

OracleDataSource ods = new OracleDataSource();
ods.setURL(url);
ods.setConnectionProperties(prop);
```

Since JDBC passes down the three properties to JNDI, the authentication mechanism chosen by client is consistent with how these properties are interpreted by JNDI. For example, if the client specifies authentication information without explicitly specifying the `java.naming.security.authentication` property, then the default authentication mechanism is "simple". Please refer to relevant JDNI documentation for details.
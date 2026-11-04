---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/ons-fan-application-requirements.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## ONS FAN Application Requirements

Ensure your application server, driver version, and connection pool are configured properly to enable sessions to drain when using ONS FAN.

Oracle UCP

| Connection Pool Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Earlier than Oracle 23ai | Earlier than Oracle 23ai | In your app server/container/framework's data source configuration file:  Set the UCP property: `"fastConnectionFailoverEnabled(true)"` | Include JDBC JAR files `ojdbcXXX.jar`, `ons.jar` on the `CLASSPATH`  Optional wallet jars, if needed: `osdt_cert.jar`, `osdt_core.jar`, and `oraclepki.jar` for Oracle Cloud Autonomous Database, or if you have set up wallets for database connections.  Ensure that all JAR files are from the same version (do not mix and match versions.  ONS FAN is auto-configured when using the MAA recommended TNS/URL |
| 23.5.0.24.7 or later | 23.5.0.24.7 or later | Use the default settings | Include JDBC JAR files `ojdbcXXX.jar`, `ons.jar` on the `CLASSPATH`  Optional wallet jars, if needed: `osdt_cert.jar`, `osdt_core.jar`, and `oraclepki.jar` for Oracle Cloud Autonomous Database, or if you have set up wallets for database connections.  Ensure that all JAR files are from the same version (do not mix and match versions)  ONS FAN is auto-configured when using the MAA recommended TNS/URL |

JDBC

Applies to JDBC used in third-party pools or directly in custom code.

| Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- |
| All supported driver versions | - Third-party pools should add pool property to validate connection at checkout (varies by pool; see examples for Hikari and Tomcat below), or applications directly calling the Oracle JDBC driver. 	- `java.sql.Connection.isValid(int                                                   timeout)` 		- `oracle.jdbc.OracleConnection.pingDatabase()` 		- `oracle.jdbc.OracleConnection.pingDatabase(int                                                   timeout)` 		- `oracle.jdbc.OracleConnection.endRequest()` 	List of APIs: [Safe Draining APIs for Planned Maintenance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=JJDBC-GUID-5C6B8DF7-8542-4533-9D68-0D2E6D1ACDA9) - Third-party pools or applications NOT calling Oracle JDBC driver: 	Execute SQL with `draining-hint` or in `DBA_CONNECTION_TESTS` | Include JDBC JAR files `ojdbcXXX.jar`, `ons.jar`, `simplefan.jar` on the `CLASSPATH`  If you have set up wallets for database connections in Oracle Cloud Autonomous Database, include wallet jars: `osdt_cert.jar`, `osdt_core.jar`, and `oraclepki.jar`  Ensure that all JAR files are from the same version (do not mix and match versions)  ONS FAN is auto-configured when using the MAA recommended TNS/URL |

WebLogic

Includes WebLogic Generic, WebLogic MDS, and WebLogic AGL.

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| 14.1.1 or later | All supported versions  Recommend upgrading JDBC driver to the latest version that WebLogic AGL supports | Upgrade to latest driver, or at a minimum driver version: 19.13  Enable FAN on AGL data source | By default, draining can happen at connection check-in with `endRequest`.  With the recommended settings, draining can also happen at connection check-out with `beginRequest`. |

Hikari

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Earlier than 6.0 | 19.21 or later | Upgrade to Hikari 6.0 | Not a recommended configuration  No request boundaries - no draining by default |
| 6.0 | 19.21 or later | With the following properties, draining occurs at `endRequest` (enabled by the following properties):  - `System.setProperty("com.zaxxer.hikari.aliveBypassWindowMs",                                                 "-1")`  Set the validation level using:  - `setProperty("oracle.jdbc.defaultConnectionValidation",                                                 "SOCKET");` - `com.zaxxer.hikari.enableRequestBoundaries` is set to `true` | See [HikariCP Best Practices for Oracle Database and Spring Boot](https://medium.com/oracledevs/hikaricp-best-practices-for-oracle-database-and-spring-boot-4d6723621c0b) for configuration using ONS/simplefan |

.NET

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings |
| --- | --- | --- |
| Any currently supported version | ODP.NET Core - Any currently supported version | On by default in ODP.NET  Pooling and HA Events connection string attributes must remain set to `true` |

.NET Framework

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings |
| --- | --- | --- |
| Any currently supported version | Managed ODP.NET - Any currently supported version  Unmanaged ODP.NET - Any currently supported version | On by default in ODP.NET  Pooling and HA Events connection string attributes must remain set to `true` |

JBOSS

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Versions earlier than EAP 7.3.9 | All supported driver versions, latest version recommended | - Validate connections on each check-out using “Validate on match” - Do not use background validation - Do not configure "purge pool disabled/abandon pool disable"  See also [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md) | Without `validation-SQL`, a properly configured native pool may drain on each checkout (by validating connection)  If the application is calling JDBC `endRequest` then it drains at check-in also, otherwise it will not.  See the requirements of the JDBC driver above for details. |
| Versions higher than EAP 7.3.9 | All supported driver versions, latest version recommended | - Validate connections on each check-out using “Validate on match” - Do not use background validation - Do not configure "purge pool disabled/abandon pool disable"  See also [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md) | Without `validation-SQL`, a properly configured native pool may drain on each check-out (by validating connection) and at check-in (automatically due to `endRequest` calls by JBOSS).  See the requirements of the JDBC driver above for details. |

Tomcat

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| 9.0, 10.0, 11.0 | Any version | If you are using Tomcat with UCP, follow the UCP recommendations above.  If you are using Tomcat with the Oracle JDBC driver or Oracle DBCP:  - Call any Oracle JDBC draining API (`isValid()`, `isUsable()`, `pingDatabase()`, `endRequest()`) at connection borrow and return. - Set the lightweight connection validation property to `SOCKET`: 	`setProperty("oracle.jdbc.defaultConnectionValidation",                                                 "SOCKET");` | With the recommended changes, draining occurs at connection check-out and check-in (`endRequest`) |
| 9.0, 10.0, 11.0 | Any version | Third-party pools or applications NOT calling Oracle JDBC driver:  - Enable connection validation at borrow and return - Use `isValid()`, or execute SQL with `draining-hint` or in `DBA_CONNECTION_TESTS` | Draining occurs at connection check-in (`endRequest`) with the recommended changes |

Long Running PL/SQL

| Application Server Version | Recommended Configuration Settings | Comments |
| --- | --- | --- |
| Oracle Database 19 or higher | Use the following SQL to test drain status between batches. If draining state is detected, then close the connection and obtain a new one.  - When draining is in progress: 	`SQL> select                                                 SYS_CONTEXT('USERENV', 'DRAIN_STATUS') from dual                                                 ;` 	Returns: `DRAINING` - When not draining: 	`SQL> select                                                 SYS_CONTEXT('USERENV', 'DRAIN_STATUS') from dual                                                 ;` 	Returns: `NONE` | No draining by default; must use recommended SQL at batch intervals.  This will work if the batch intervals are less than 1/2 of the drain timeout interval. |

OCI-Based Applications

Including Pro\*C/C++, Pro\*COBOL, and python-oracledb in Thick Mode

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Oracle Database 19 or higher | Oracle Database 19 or higher | OCI clients embed FAN at the driver level so that all clients can use them regardless of the pooling solution.  The database service must have the attribute `"-notification TRUE"` set  If `oraaccess.xml` is in use, ensure that the `events` tag is `TRUE`:  ``` <oraaccess> xmlns="http://xmlns.oracle.com/oci/oraaccess"  xmlns:oci="http://xmlns.oracle.com/oci/oraaccess"  schemaLocation="http://xmlns.oracle.com/oci/oraaccess  http://xmlns.oracle.com/oci/oraaccess.xsd">  <default_parameters>  <events>true</events>  </default_parameters> </oraaccess> ``` | Python must use the "thick" driver and make connections with the `events` property set to `TRUE` |
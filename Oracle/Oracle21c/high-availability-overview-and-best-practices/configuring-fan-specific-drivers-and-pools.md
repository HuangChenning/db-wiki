---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/configuring-fan-specific-drivers-and-pools.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Configuring FAN for Specific Drivers and Pools

Specific requirements and recommendations for configuring FAN with various database client drivers.

JDBC FAN Requirements

Oracle Universal Connection Pool (UCP)

- Use the recommended connection URL/string for auto-configuration of ONS.
- Include JDBC JAR files `ojdbcXXX.jar`, `ons.jar`, and `simplefan.jar`, on the `CLASSPATH`.
	Include optional wallet JARs, if needed: `osdt_cert.jar` (prior to Oracle 23ai only), `osdt_core.jar` (prior to Oracle 23ai only), and `oraclepki.jar` for Oracle Cloud Autonomous Database (Serverless or Dedicated Exadata Infrastructure) with mutual TLS, or if you have set up client-side wallets for database connections.
	Ensure that all JAR files are from the same version (do not mix and match versions).
- Set the pool or driver property to enable Fast Connection Failover.
	For example, in UCP it is set for the `PoolDataSource` using `setFastConnectionFailoverEnabled(true)`.
	For UCP and JDBC 23ai or later, this is done by default when connected to an Oracle RAC database.
- If you are using a third party pool:
	- Java-based application server, the most effective method to achieve draining and failover is to replace the pooled data source with UCP.
		This approach is supported by many application servers including Oracle WebLogic Server, IBM WebSphere, IBM Liberty (XA and non-XA usage), Apache Tomcat, Hikari CP, and others.
		If your application is using J2EE or Container Managed Transactions (CMT) with Red Hat JBoss, request boundaries are provided with version Red Hat JBoss EAP 7.4.
		This configuration supports draining with FAN (XA and non-XA usage).
```
<dependencies>

...
<dependency>
  <groupId>com.oracle.database.ha</groupId>
  <artifactId>ons</artifactId>
  <version>${oracle.jdbc.version}</version>
</dependency>
<dependency>
  <groupId>com.oracle.database.ha</groupId>
  <artifactId>simplefan</artifactId>
  <version>${oracle.jdbc.version}</version>
</dependency>

...
</dependencies>
```

Non-Oracle Connection Pools or Standalone JDBC Applications

For clients not using UCP, but using third-party connection pools or standalone JDBC you typically need to do the following:

- Configure the driver to handle FAN events by adding `simplefan` and `ons jar` files to your `CLASSPATH` or project’s `pom.xml`.
- Call any Oracle JDBC draining API (`isValid()`, `isUsable()`, `pingDatabase()`, `endRequest()`), and set the following Java system property for lightweight connection validation:
	```
	-Doracle.jdbc.defaultConnectionValidation=SOCKET
	```

OCI-Based Applications

- OCI-based clients embed FAN at the driver level. Pooling is not required to receive FAN notifications.
- The database service must have the attribute `"-notification                             TRUE"` set.
- If `oraaccess.xml` is in use, ensure that the `events` tag is `TRUE`:
	```
	<oraaccess> xmlns="http://xmlns.oracle.com/oci/oraaccess"
	 xmlns:oci="http://xmlns.oracle.com/oci/oraaccess"
	 schemaLocation="http://xmlns.oracle.com/oci/oraaccess
	 http://xmlns.oracle.com/oci/oraaccess.xsd">
	 <default_parameters>
	 <events>true</events>
	 </default_parameters>
	</oraaccess>
	```
- If you are not using `oraaccess.xml`, an alternative is to change the application code to use `OCI_EVENTS` mode. For example:
	```
	sword errcode = OCIEnvCreate(&envhp, OCI_EVENTS, 0, 0, 0, 0, 0, 0);
	if (errcode)
	```
- For Python, use the OCI "thick" drivers and make connections with the "events" property set to true; for example:
	```
	conn = oracledb.connect(dsn="localhost:1521/DB23PDB1", user="my_user", password="my_pw", events=True)
	```

ODP.NET FAN Requirements

All ODP.NET provider types (core, managed, and unmanaged) support FAN.

ODP.NET out-of-band FAN requires connection pooling and HA Events to be enabled, which they are by default. No code changes are necessary if these attributes are not changed.

The following is an example of a FAN-enabled ODP.NET connection string:

```
"user id=oracle; password=oracle; data source=HA; pooling=true; HA events=true;"
```

In-band FAN is enabled by default.

Read more about ODP.NET high availability in [Real Application Clusters and Global Data Services](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ODPNT-GUID-BAF145C1-33A9-45C7-9ED5-FB4563B274CA).

JBoss

Use ONS FAN (recommended) if possible, because it also covers unplanned outages. If ONS FAN fails, in-band is used instead. Both can also work at the same time.

For testing – update data source definition in standalone/domain configuration XML

For production – use JBoss management console or CLI commands to update DS definition

JBoss configuration settings

- Validate connections on each check-out using “Validate on match”
- Do not use background validation
- Do not configure "purge pool disabled/abandon pool disable"

Follow up with Redhat documentation for draining configuration: [https://access.redhat.com/solutions/42463](https://access.redhat.com/solutions/42463)

Also, see Redhat documentation for connection validation: [https://docs.redhat.com/en/documentation/red\_hat\_jboss\_enterprise\_application\_platform/7.4/html/configuration\_guide/datasource\_management#configure\_database\_connection\_validation\_settings](https://docs.redhat.com/en/documentation/red_hat_jboss_enterprise_application_platform/7.4/html/configuration_guide/datasource_management#configure_database_connection_validation_settings)

To specify additional JDBC driver connection properties:

```
<connection-property name="URL">
    jdbc:oracle:thin:@CURRENT_URL?TNS_ADMIN=/absolute_path/ojdbc.properties
</connection-property>
```

In `/absolute_path/ojdbc.properties`, include the following connection properties and values:

```
prop1=value1
prop2=value2
…
```

Other Pools and Drivers

- For Hikari connection pools, see the article [HikariCP Best Practices for Oracle Database and Spring Boot](https://medium.com/oracledevs/hikaricp-best-practices-for-oracle-database-and-spring-boot-4d6723621c0b).
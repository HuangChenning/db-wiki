---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/band-draining-notification-application-requirements.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## In-Band Draining Notification Application Requirements

Ensure your application server, driver version, and connection pool are configured properly to enable sessions to drain when using in-band notifications.

Oracle UCP

| Connection Pool Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| 23.5.0.24.7 or later | 23.5.0.24.7 or later | Use the default settings | Preferred version |
| 19.12 or later | 19.12 or later | Set the UCP property: `setValidateConnectionOnBorrow(true)`  Note that there are several validation modes, and a mode can be set using driver settings. | Draining occurs at connection check-out (`beginRequest`) and check-in (`endRequest`) with the recommended changes  UCP will use ensure that JDBC uses a lightweight connection check that doesn't require a network round trip when `setValidateConnectionOnBorrow(true)` is used. |
| 19.11 and earlier | 19.11 and earlier | Upgrade to latest driver, or at a minimum driver version 19.12 | Not a recommended configuration  No In-band notifications available; no draining possible unless ONS-based FAN is used |

WebLogic

Includes WebLogic Generic, WebLogic MDS, and WebLogic AGL.

| Application Server and Oracle Driver Version Combination | Recommended Configuration Settings | Comments |
| --- | --- | --- |
| 12.2.1.4 with 19.12 or later  12.1.1.6 with 19.12 or later  14.1.1 with 19.12 or later  14.1.2 with 23.5.0.24.7 or later | [All WLS versions require fix for bug 35731335](https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/14.1.2/wlapi/weblogic/j2ee/descriptor/wl/JDBCConnectionPoolParamsBean.html#isTestConnectionsOnReserve--)  The following parameters are needed:  `test-connections-on-reserve=true`  `test-table-name=SQL ISVALID` (default: null)  `seconds-to-trust-an-idle-pool-connection=0                                                   ` (default: 10)  `test-frequency-seconds` (default: 120 seconds, idle connections)  `count-of-refresh-failures-till-disable=0` (default: 2)  `count-of-test-failures-till-flush=0` (default: 2) | By default, draining can happen at connection check-in with `endRequest`.  With the recommended settings, draining can also happen at connection check-out with `beginRequest`. |
| 12.2.1.4 with Oracle 19.11 and earlier | Upgrade to latest Oracle driver, or at a minimum driver version: 19.12 | Not a recommended configuration  No In-band notifications available; no draining possible unless you have FAN |

JDBC

Applies to JDBC used in third-party pools or directly in custom code.

| Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- |
| 19.12 or later | - Because JDBC driver does not have knowledge of pooling actions, the only places it can drain safely are when any of the "safe-draining APIs" gets called. 	Third-party pools should add pool property to validate connection at checkout (varies by pool, see examples for Hikari and Tomcat below), or applications directly calling the Oracle JDBC driver: 	- `java.sql.Connection.isValid(int                                                   timeout)` 		- `oracle.jdbc.OracleConnection.pingDatabase()` 		- `oracle.jdbc.OracleConnection.pingDatabase(int                                                   timeout)` 		- `oracle.jdbc.OracleConnection.endRequest()` 	List of APIs: [Safe Draining APIs for Planned Maintenance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=JJDBC-GUID-5C6B8DF7-8542-4533-9D68-0D2E6D1ACDA9) - Alternatively, applications using `beginRequest` and `endRequest` will allow safe drain points to be used - Third-party pools or apps calling Oracle JDBC driver: 	Call any Oracle JDBC draining API (listed above) and set the lightweight connection validation property to `SOCKET` if applicable to the pool (see [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md)) - Third-party pools or apps NOT calling Oracle JDBC driver: 	Execute SQL with `draining-hint` or in `DBA_CONNECTION_TESTS` | Draining occurs at connection check-out and check-in (if `endRequest` is used) with the recommended changes  Oracle JDBC 19.15 is recommended if using AC or TAC so planned failover operates at `beginRequest` |
| 19.11 and earlier | Upgrade to latest driver, or at a minimum driver version 19.12 | Not a recommended configuration  No In-band notifications available; no draining possible |

Hikari

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| 6.0 | 19.21 or later | With the following properties, draining occurs at `endRequest` (enabled by the following properties):  `System.setProperty("com.zaxxer.hikari.aliveBypassWindowMs",                                                   "-1")`  and set the validation level using:  `setProperty("oracle.jdbc.defaultConnectionValidation",                                                   "SOCKET");`  `com.zaxxer.hikari.enableRequestBoundaries` is set to `true` | Draining occurs at connection check-out (`beginRequest`) and check-in (`endRequest`) with the recommended changes |
| earlier than 6.0 | 19.21 or later | Upgrade to Hikari 6.0 | Not a recommended configuration  No request boundaries - no draining by default |

.NET

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Any currently supported version | ODP.NET Core 19.9 or later | Use the default settings | ODP.NET in-band FAN notifications support the following usage scenarios:  - Pluggable database relocation - Database service relocation - Database rolling upgrade - Connection Manager planned maintenance  Supported with Oracle Database 18c and higher. |

.NET Framework

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Any currently supported version | Managed ODP.NET 19.9 or later  Unmanaged ODP.NET 19.10 or later | On by default in ODP.NET | ODP.NET in-band FAN notifications support the following usage scenarios:  - Pluggable database relocation - Database service relocation - Database rolling upgrade - Connection Manager planned maintenance  Supported with Oracle Database 18c and higher. |

Tomcat

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| 9.0, 10.0, 11.0 | Any version | If you are using Tomcat with UCP, follow the UCP recommendations above.  If you are using Tomcat with the Oracle JDBC driver or Oracle DBCP:  - Call any Oracle JDBC draining API (`isValid()`, `isUsable()`, `pingDatabase()`, `endRequest()`) at connection borrow and return. - Set the lightweight connection validation property to `SOCKET`: 	`setProperty("oracle.jdbc.defaultConnectionValidation",                                                   "SOCKET");` | With the recommended changes, draining occurs at connection check-out (`beginRequest`) and check-in (`endRequest`) with the recommended changes  UCP uses lightweight connection tests (`SOCKET`) by default. |
| 9.0, 10.0, 11.0 | Any version | Third-party pools or applications NOT calling Oracle JDBC driver:  - Enable connection validation at borrow and return - Use `isValid()`, or execute SQL with `draining-hint` or in `DBA_CONNECTION_TESTS` | Draining occurs at connection check-in (`endRequest`) with the recommended changes |

JBOSS

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| EAP 7.3.9 and later | 19.12 or later | - Validate connections on each check-out using “Validate on match” - Do not use background validation - Do not configure "purge pool disabled/abandon pool disable"  See also [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md) | Without `validation-SQL`, a properly configured native pool may drain on each checkout (by validating each connection) and at checkin (automatically due to `endRequest` calls by JBOSS). |
| Versions earlier than EAP 7.3.9 | 19.12 or later | - Validate connections on each check-out using “Validate on match” - Do not use background validation - Do not configure "purge pool disabled/abandon pool disable"  See also [Configuring FAN for Specific Drivers and Pools](configuring-fan-specific-drivers-and-pools.md) | Without `validation-SQL`, a properly configured native pool may drain on each checkout (by validating connection).  If the application is calling JDBC `endRequest`, then it may drain at checkin also, otherwise it will not.  See the requirements of the JDBC driver for detail. |

Long Running PL/SQL

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Oracle Database 19 or higher | NA | Use the following SQL to test drain status between batches.  The idea is to check the draining state. If draining state is detected, then close the connection and obtain a new one.  - When draining is in progress: 	`SQL> select                                                   SYS_CONTEXT('USERENV', 'DRAIN_STATUS') from dual                                                   ;` 	Returns: `DRAINING` - When not draining: 	`SQL> select                                                   SYS_CONTEXT('USERENV', 'DRAIN_STATUS') from dual                                                   ;` 	Returns: `NONE` | No draining by default; must use recommended SQL at batch intervals.  This will work if the batch intervals are less than 1/2 of the drain timeout interval. |

OCI-Based Applications

Pro\*C/C++, Pro\*COBOL and python-oracledb in Thick mode.

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings | Comments |
| --- | --- | --- | --- |
| Oracle Database 19 or higher | Oracle Database 19 or higher | - No additional configuration is needed for OLTP-style applications - Long running applications should use the following Oracle Call Interface `OCIAttrGet` example to test drain status between batches and obtain a new session when draining is detected. If not connected state is detected, then close the connection and obtain a new one. 	``` 	ub4 serverStatus = 0 	OCIAttrGet((dvoid *)srvhp, OCI_HTYPE_SERVER, 	   (dvoid *)&serverStatus, (ub4 *)0, OCI_ATTR_SERVER_STATUS, errhp); 	if (serverStatus == OCI_SERVER_NORMAL) 	   printf("Continue. Connection is up.\n"); 	else if (serverStatus == OCI_SERVER_NOT_CONNECTED) 	   printf("close your session and get another .\n"); 	``` 	This will work if the batch intervals are less than 1/2 of the drain timeout interval. | Draining occurs at checkout from the OCI Session Pool for OCI and python-oracledb in Thick mode. Draining occurs at an explicit request boundary (OCIRequestBegin for OCI applications and EXEC SQL REQUEST BEGIN for Pro\*/C++ and Pro\*COBOL applications).  Long running applications should test drain status as shown in the "Recommended Configuration Settings" here. |

Long Running JDBC

| Application Server Version | Oracle Driver Version | Recommended Configuration Settings |
| --- | --- | --- |
| Oracle Database 19 or higher | Oracle Database 19 or higher | - Use the following connection test to test drain status between batches. If draining state is detected, then close the session and obtain a new one, then continue processing the next batch. 	Call any Oracle JDBC draining API (`isValid()`, `isUsable()`, `pingDatabase()`, `endRequest()`) and set the lightweight connection validation property to `SOCKET`: 	`setProperty("oracle.jdbc.defaultConnectionValidation",                                                   "SOCKET");` - Alternatively, configure Transparent Application Continuity to do planned failover during draining (requires Oracle Database 19.15 or higher) |
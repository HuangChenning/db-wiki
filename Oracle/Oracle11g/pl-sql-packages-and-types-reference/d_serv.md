---
title: DBMS_SERVICE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_serv.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 131 DBMS\_SERVICE

The `DBMS_SERVICE` package lets you create, delete, activate, and deactivate services for a single instance.

The chapter contains the following topics:

- Using DBMS\_SERVICE
- Summary of DBMS\_SERVICE Subprograms
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) for administering services in Oracle Real Application Clusters.

---

## Using DBMS\_SERVICE

This section contains topics which relate to using the `DBMS_SERVICE` package.

---

### Overview

`DBMS_SERVICE` supports the management of services in the RDBMS for the purposes of workload measurement, management, prioritization, and XA/and distributed transaction management.

Oracle Real Application Clusters (Oracle RAC) has a functionality to manage service names across instances. This package allows the creation, deletion, starting and stopping of services in both Oracle RAC and a single instance. Additionally, it provides the ability to disconnect all sessions which connect to the instance with a service name when Oracle RAC removes that service name from the instance.

See Also:

For more information about Oracle Real Application Clusters, [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076).

---

### Security Model

Privileges

The client using this package must have the `ALTER` `SYSTEM` execution privilege and the `V$SESSION` table read privilege.

Schemas

This package must be installed under `SYS` schema.

Roles

The `EXECUTE` privilege of the package is granted to the `DBA` role only.

---

### Constants

The `DBMS_SERVICE` package uses the constants shown in following tables

- Constants used in calling arguments are described in Table 131-1, "Constants used in Calling Arguments"
- Constants used in connection balancing goal arguments are described in Table 131-2, "Constants used in Connection Balancing Goal Arguments"
- Constants used TAF failover attribute arguments are described in Table 131-3, "Constants used in TAF Failover Attribute Arguments"

Table 131-1 Constants used in Calling Arguments

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `GOAL_NONE` | `NUMBER` | `0` | Disables Load Balancing Advisory |
| `GOAL_SERVICE_TIME` | `NUMBER` | `1` | Load Balancing Advisory is based on elapsed time for work done in the service plus available bandwidth to the service |
| `GOAL_THROUGHPUT` | `NUMBER` | `2` | Load Balancing Advisory is based on the rate that work is completed in the service plus available bandwidth to the service |

Table 131-2 Constants used in Connection Balancing Goal Arguments

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `CLB_GOAL_SHORT` | `NUMBER` | `1` | Connection load balancing uses Load Balancing Advisory, when Load Balancing Advisory is enabled (either `goal_service_time` or `goal_throughput`). When `GOAL` = `NONE` (no load balancing advisory), connection load balancing uses an abridged advice based on CPU utilization. |
| `CLB_GOAL_LONG` | `NUMBER` | `2` | Balances the number of connections per instance using session count per service. This setting is recommended for applications with long connections such as forms. This setting can be used with Load Balancing Advisory when the connection pool is sized to accommodate gravitation within the pool itself (without adding or removing connections). The latter is the most efficient design. |

Table 131-3 Constants used in TAF Failover Attribute Arguments

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `FAILOVER_METHOD_NONE` | `VARCHAR2` | `0` | Server side TAF is not enabled for this service |
| `FAILOVER_METHOD_BASIC` | `VARCHAR2` | `1` | `Server side TAF method is BASIC. BASIC` is the only value currently supported. This means that a new connection is established at failure time. It is not possible to pre-establish a backup connection. (which is to say, `PRECONNECT` is not supported) |
| `FAILOVER_TYPE_NONE` | `NUMBER` |  | Server side TAF type is `NONE` |
| `FAILOVER_TYPE_SESSION` | `NUMBER` |  | Server side TAF failover type is `SESSION`. At failure time, if the failover type is `SESSION`, TAF will re-connect to a surviving node and re-establish a vanilla database session. Customizations (for example, `ALTER` `SESSION`) must be re-executed in a failover callback. |
| `FAILOVER_TYPE_SELECT` | `NUMBER` |  | Server side TAF failover type is `SELECT` |
| `FAILOVER_RETRIES` | `NUMBER` |  | Number of retries to use during a failover. Specifies the number of times for TAF to attempt the re-connect and re-authenticate pair. The value must be integral and greater than 0. The maximum value is `UB4MAXVAL` |
| `FAILOVER_DELAY` | `NUMBER` |  | Number of seconds delay before trying to fail over. Specifies the delay (in seconds) that TAF will incur if the re-connect / re-authentication fails. The value must be integral and greater than 0. The maximum value is `UB4MAXVAL`. |

Usage Notes

- If a TAF callback has been registered, then the failover retries and failover delay are ignored. If an error occurs, TAF will continue to re-attempt the connect and authentication as long as the callback returns a value of `OCI_FO_RETRY`. Any delay must be coded into the callback logic
- Server side TAF settings override client-side counterparts that might be configured in TNS connect descriptors. If TAF is not configured on the client side, then at a minimum, the failover type must be set to enable TAF. If the failover type is set on the server side, then the failover method will default to `BASIC`. Delay and retries are optional and may be specified independently.

---

### Operating Procedures

- You cannot use the following procedures with Oracle Real Applications Clusterware, Oracle Restart and Oracle Global Data Services:
	- CREATE\_SERVICE Procedure
		- DELETE\_SERVICE Procedure
		- MODIFY\_SERVICE Procedure
		- START\_SERVICE Procedure
		- STOP\_SERVICE Procedure
- With Oracle Database 12c Release 1, you are advised to use the parameter interface in all service -related subprorgrams.
- If you wish to use `DBMS_SERVICE` on a pluggable databas (PDB) in a single instance, you must connect to that PDB first.

---

### Exceptions

The following table lists the exceptions raised by `DBMS_SERVICE` package.

Table 131-4 DBMS\_SERVICE Exceptions

| Exception | Error Code | Description |
| --- | --- | --- |
| `NULL_SERVICE_NAME` | 44301 | The service name argument was found to be `NULL` |
| `NULL_NETWORK_NAME` | 44302 | The network name argument was found to be `NULL` |
| `SERVICE_EXISTS` | 44303 | This service name was already in existence |
| `SERVICE_DOES_NOT_EXIST` | 44304 | The specified service was not in existence |
| `SERVICE_IN_USE` | 44305 | The specified service was running |
| `SERVICE_NAME_TOO_LONG` | 44306 | The service name was too long |
| `NETWORK_PREFIX_TOO_LONG` | 44307 | The network name, excluding the domain, was too long |
| `NOT_INITIALIZED` | 44308 | The services layer was not yet initialized |
| `GENERAL_FAILURE` | 44309 | There was an unknown failure |
| `MAX_SERVICES_EXCEEDED` | 44310 | The maximum number of services has been reached |
| `SERVICE_NOT_RUNNING` | 44311 | The specified service was not running |
| `DATABASE_CLOSED` | 44312 | The database was closed |
| `INVALID_INSTANCE` | 44313 | The instance name argument was not valid |
| `NETWORK_EXISTS` | 44314 | The network name was already in existence |
| `NULL_ATTRIBUTES` | 44315 | All attributes specified were `NULL` |
| `INVALID_ARGUMENT` | 44316 | Invalid argument supplied |
| `DATABASE_READONLY` | 44317 | The database is open read-only |
| `MAX_SN_LENGTH` | 44318 | The total length of all running service network names exceeded the maximum allowable length |

---

## Summary of DBMS\_SERVICE Subprograms

Table 131-5 DBMS\_SERVICE Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_SERVICE Procedure | Creates service |
| DELETE\_SERVICE Procedure | Deletes service |
| DISCONNECT\_SESSION Procedure | Disconnects service |
| MODIFY\_SERVICE Procedure | Modifies service |
| START\_SERVICE Procedure | Activates service |
| STOP\_SERVICE Procedure | Stops service |

---

### CREATE\_SERVICE Procedure

This procedure creates a service name in the data dictionary. Services are also created in the data dictionary implicitly when you set the service in the `service_name` parameter or by means of the `ALTER` `SYSTEM` `SET` `SERVICE_NAMES` command.

Note:

You cannot use the second version of subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services. The version with the parameter array interface applies to databases that are not managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services. New attributes are only available using the parameter interface.

Note:

The functionality associated with the `edition` argument is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Syntax

```
DBMS_SERVICE.CREATE_SERVICE(
   service_name        IN VARCHAR2, 
   network_name        IN VARCHAR2,
   goal                IN NUMBER DEFAULT NULL,
   dtp                 IN BOOLEAN DEFAULT NULL,
   aq_ha_notifications IN BOOLEAN DEFAULT NULL,
   failover_method     IN VARCHAR2 DEFAULT NULL,
   failover_type       IN VARCHAR2 DEFAULT NULL,
   failover_retries    IN NUMBER DEFAULT NULL,
   failover_delay      IN NUMBER DEFAULT NULL,
   clb_goal            IN NUMBER DEFAULT NULL,
   edition             IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 131-6 CREATE\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |
| `network_name` | The network name of the service as used in SQLNet connect descriptors for client connections. This is limited to the NET `service_names` character set (see [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/syntax.htm#NETRF005)). |
| `goal` | The workload management goal directive for the service. Valid values:  - `DBMS_SERVICE`.`GOAL_SERVICE_TIME` - `DBMS_SERVICE`.`GOAL_THROUGHPUT` - `DBMS_SERVICE`.`GOAL_NONE` |
| `dtp` | Declares the service to be for DTP or distributed transactions including XA transactions |
| `aq_ha_notifications` | Determines whether HA events are sent through AQ for this service |
| `failover_method` | The TAF failover method for the service |
| `failover_type` | The TAF failover type for the service |
| `failover_retries` | The TAF failover retries for the service |
| `failover_delay` | The TAF failover delay for the service |
| `clb_goal` | Method used for Connection Load Balancing (see Table 131-2, "Constants used in Connection Balancing Goal Arguments") |
| `edition` | If this argument has a non- `NULL` value, this provides the initial session edition for subsequent database connections using this service that do not specify an edition. If no value is specified, this argument will have no effect.  During service creation or modification, no validation is performed on this parameter.  At connection time, if the connecting user does not have `USE` privilege on the edition, or the edition does not exist, this raises the error `ORA-38802` (edition does not exist). |

Examples

```
DBMS_SERVICE.CREATE_SERVICE('ernie.us.oracle.com','ernie.us.oracle.com');
```

---

### DELETE\_SERVICE Procedure

This procedure deletes a service from the data dictionary.

Note:

You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services.

Syntax

```
DBMS_SERVICE.DELETE_SERVICE(
   service_name   IN VARCHAR2);
```

Parameters

Table 131-7 DELETE\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |

Examples

```
DBMS_SERVICE.DELETE_SERVICE('ernie.us.oracle.com');
```

---

### DISCONNECT\_SESSION Procedure

This procedure disconnects sessions with the named service at the current instance.

Syntax

```
DBMS_SERVICE.DISCONNECT_SESSION(
   service_name         IN VARCHAR2,
   disconnect_option    IN NUMBER DEFAULT POST_TRANSACTION);
```

Parameters

Table 131-8 DISCONNECT\_SESSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |
| disconnect\_option | There are two options, package constants expressed as `NUMBER`:  - `POST_TRANSACTION` `=` `0`: the session will disconnect after the current transaction commits or rolls back - `IMMEDIATE` `=` `1`: sessions will be disconnected immediately  Note: `IMMEDIATE` or `POST_TRANSACTION` will be automatically translated as `1` and `0` respectively. However, passing-in a string literal (quoted using either the `'` or `"` characters, such as `"IMMEDIATE"` or `'POST_TRANSACTION'`) will raise an error. |

Usage Notes

- This procedure can be used in the context of a single instance as well as with Oracle Real Application Clusters.
- This subprogram does not return until all corresponding sessions are disconnected. Therefore, use the `DBMS_JOB` package or put the SQL session in background if the caller does not want to wait for all corresponding sessions to be disconnected.

Examples

This disconnects sessions with `service_name` `'ernie.us.oracle.com'`.

```
DBMS_SERVICE.DISCONNECT_SESSION('ernie.us.oracle.com');
```

---

### MODIFY\_SERVICE Procedure

This procedure modifies an existing service.

Note:

You cannot use the second version of subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services. The version with the parameter array interface applies to databases that are not managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services. New attributes are only available using the parameter interface.

Note:

The functionality associated with the `edition` and `modify_edition` arguments is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Syntax

```
DBMS_SERVICE.MODIFY_SERVICE(
   service_name        IN VARCHAR2, 
   goal                IN NUMBER DEFAULT NULL,
   dtp                 IN BOOLEAN DEFAULT NULL,
   aq_ha_notifications IN BOOLEAN DEFAULT NULL,
   failover_method     IN VARCHAR2 DEFAULT NULL,
   failover_type       IN VARCHAR2 DEFAULT NULL,
   failover_retries    IN NUMBER DEFAULT NULL,
   failover_delay      IN NUMBER DEFAULT NULL,
   clb_goal            IN NUMBER DEFAULT NULL,
   edition             IN VARCHAR2 DEFAULT NULL,
   modify_edition      IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 131-9 MODIFY\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |
| `goal` | The workload management goal directive for the service. Valid values:  - `DBMS_SERVICE`.`GOAL_SERVICE_TIME` - `DBMS_SERVICE`.`GOAL_THROUGHPUT` - `DBMS_SERVICE`.`GOAL_NONE` |
| `dtp` | Declares the service to be for DTP or distributed transactions including XA transactions |
| `aq_ha_notifications` | Determines whether HA events are sent through AQ for this service |
| `failover_method` | The TAF failover method for the service |
| `failover_type` | The TAF failover type for the service |
| `failover_retries` | The TAF failover retries for the service |
| `failover_delay` | The TAF failover delay for the service |
| `clb_goal` | Method used for Connection Load Balancing (see Table 131-2, "Constants used in Connection Balancing Goal Arguments") |
| `edition` | If this argument has a non- `NULL` value, this provides the initial session edition for subsequent database connections using this service that do not specify an edition. If no value is specified, this argument will have no effect.  During service creation or modification, no validation is performed on this parameter.  At connection time, if the connecting user does not have `USE` privilege on the edition, or the edition does not exist, this raises the error `ORA-38802` (edition does not exist). |
| `modify_edition` | If `TRUE`, the edition service attribute is updated to use the edition argument value. If `FALSE` or `NULL`, the edition attribute will not be updated. |

Usage Notes

- If you are using Clustered Managed Services with Oracle Clusterware, or using Oracle Restart with your single instance database, you must modify services using the `srvctl` command rather than `DBMS_SERVICE`. When the service is started by Oracle Clusterware or Oracle Restart, the service will be modified in the database to match the resource defined to either Oracle Clusterware or Oracle Restart. Any changes made with `DBMS_SERVICE` will be lost unless they are also made with the corresponding `srvctl` command. Service attribute modifications take effect immediately starting with 11.2.0.2 when the service is started or modified by `srvctl`.
- Although the edition attribute can be modified while the service is up and running, it may not be safe to do so. Users must proceed with caution since this will cause new connections to be connected at the new edition, while existing connection will not be affected. This can in turn cause mid-tier operations to connect to the wrong edition.

---

### START\_SERVICE Procedure

This procedure starts a service. This procedure alters the `service_name` IOP to contain this `service_name`. In Oracle RAC, implementing this option will act on the instance specified.

Note:

You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services.

Syntax

```
DBMS_SERVICE.START_SERVICE(
   service_name  IN VARCHAR2, 
   instance_name IN VARCHAR2);
```

Parameters

Table 131-10 START\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |
| `instance_name` | Name of the instance where the service must be activated (optional). The instance on which to start the service. `NULL` results in starting of the service on the local instance. In single instance this can only be the current instance or `NULL`. Specify `DBMS_SERVICE`.`ALL_INSTANCES` to start the service on all configured instances. |

Examples

```
DBMS_SERVICE.START_SERVICE('ernie.us.oracle.com');
```

---

### STOP\_SERVICE Procedure

This procedure stops a service, altering the `service_name` IOP to remove this `service_name`.

Note:

You cannot use this subprogram if your services are managed by Oracle Clusterware, Oracle Restart or Oracle GlobalData Services.

Syntax

```
DBMS_SERVICE.STOP_SERVICE(
   service_name   IN VARCHAR2,
   instance_name  IN VARCHAR2);
```

Parameters

Table 131-11 STOP\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `service_name` | Name of the service limited to 64 characters in the Data Dictionary |
| `instance_name` | Name of the instance where the service must be stopped (optional). The instance on which to stop the service. `NULL` results in stopping of the service locally. In single instance this can only be the current instance or `NULL`. The default in Oracle RAC and exclusive case is `NULL`. Specify `DBMS_SERVICE`.`ALL_INSTANCES` to stop the service on all configured instances. |

Examples

```
DBMS_SERVICE.STOP_SERVICE('ernie.us.oracle.com');
```
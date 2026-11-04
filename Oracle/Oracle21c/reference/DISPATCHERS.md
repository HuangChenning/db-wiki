---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DISPATCHERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.112 DISPATCHERS

`DISPATCHERS` configures dispatcher processes in the shared server architecture.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DISPATCHERS = '` `dispatch_clause` `'` |
| Syntax | dispatch\_clause::=  `(PROTOCOL = ` `protocol``) \|`  `(ADDRESS = ` `address``) \|`  `(DESCRIPTION = ` `description` ` )`  `[options_clause]` |
| Syntax | options\_clause::=  `(DISPATCHERS = ` `integer` ` \|`  `  SESSIONS =  ` `integer` ` \|`  `  CONNECTIONS =  ` `integer` ` \|`  ` MULTIPLEX = {1 \| ON \| YES \| TRUE \|`  `   0 \| OFF \| NO \| FALSE \| BOTH \| IN \| OUT} \|`  `  LISTENER =  ` `tnsname` ` \|`  `  SERVICE =  ` `service` ` \|`  `  INDEX =  ` `integer``)` |
| Default value | If `SHARED_SERVERS` is greater than `0`, then `DISPATCHERS` defaults to `'(PROTOCOL=tcp)'`, causing 1 TCP/IP dispatcher to be created. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

The parsing software supports a name-value syntax to enable the specification of attributes in a position-independent, case-insensitive manner. For example:

```
DISPATCHERS = '(PROTOCOL=TCP)(DISPATCHERS=3)'
```

Attributes may be specified using the full attribute name or any substring beginning with the first 3 characters. For example, `SESSIONS` can be specified as `SES`, `SESS`, `SESSI`, and so on.

Specify only one of the following attributes: `PROTOCOL`, `ADDRESS`, or `DESCRIPTION`. If you specify either `ADDRESS` or `DESCRIPTION`, then you can specify additional network attributes. Doing so supports multi-homed hosts.

dispatch\_clause

- `PROTOCOL`
	The network protocol for which the dispatcher generates a listening endpoint.
- `ADDRESS`
	The network protocol address of the endpoint on which the dispatchers listen.
- `DESCRIPTION`
	The network description of the endpoint on which the dispatchers listen, including the protocol address.

options\_clause

- `DISPATCHERS`
	The initial number of dispatchers to start. The default is 1.
- `SESSIONS`
	The maximum number of network sessions to allow for each dispatcher. The default is operating system-specific. Most operating systems have a default of 16 KB.
- `CONNECTIONS`
	The maximum number of network connections to allow for each dispatcher. The default is operating system-specific.
- `MULTIPLEX`
	Enables the Oracle Connection Manager session multiplexing feature.
	- The values `1`, `ON`, `YES`, `TRUE`, and `BOTH` indicate that Network Session Multiplex is enabled for both incoming and outgoing network connections.
		- The value `IN` indicates that Network Session Multiplex is enabled for incoming network connections.
		- The value `OUT` indicates that Network Session Multiplexing is enabled for outgoing network connections.
		- The values `0`, `NO`, `OFF`, and `FALSE` indicate that Network Session Multiplexing is disabled for both incoming and outgoing network connections. This is the default.
- `LISTENER`
	Specifies the network name of an address or address list of the Oracle Net listeners with which the dispatchers will register.
	The `LISTENER` attribute facilitates administration of multi-homed hosts. This attribute specifies the appropriate listeners with which the dispatchers will register. The `LISTENER` attribute takes precedence over the `LOCAL_LISTENER` and `REMOTE_LISTENER` parameters. See " [LOCAL\_LISTENER](LOCAL_LISTENER.md) " and " [REMOTE\_LISTENER](REMOTE_LISTENER.md) ".
- `SERVICE`
	Specifies one or more names by which clients can connect to the dispatchers. The `SERVICE` attribute takes precedence over any settings configured by using the `SRVCTL` command-line utility, the `GDSCTL` command-line utility, or the `DBMS_SERVICE` PL/SQL package.
- `INDEX`
	Use this attribute in an `ALTER SYSTEM SET DISPATCHERS` statement to indicate which dispatcher configuration you want to modify. (If you specify `INDEX` in the initialization parameter file, the Oracle Database ignores it.) In an `ALTER SYSTEM` statement, `INDEX` specifies the order in which the parameter's values were initialized. The value ranges from `0` (for the first dispatcher configuration) to one less than the total number of dispatcher configurations you define.
	For example, if you specify 3 dispatcher configurations in the initialization parameter file, you would modify the third dispatcher configuration by specifying `INDEX` = `2` in the `ALTER SYSTEM` statement. You could also add another dispatcher configuration in the `ALTER SYSTEM` statement by specifying `INDEX` = `3`.
	If `INDEX` is not specified in the `ALTER SYSTEM` statement, then the `PROTOCOL`, `ADDRESS`, or `DESCRIPTION` attributes must be specified, and if a dispatcher configuration matching this `PROTOCOL`, `ADDRESS`, or `DESCRIPTION` exists, then that configuration will be modified. Otherwise, a new configuration will be added.

See Also:

- " [SHARED\_SERVERS](SHARED_SERVERS.md) "
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NETAG323) and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11176) for more information on setting this parameter
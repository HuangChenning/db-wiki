---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SERVICE_NAMES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.327 SERVICE\_NAMES

`SERVICE_NAMES` specifies one or more names by which clients can connect to the instance.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SERVICE_NAMES =`  `db_service_name` `  [,  ``db_service_name` ` [ ... ] ]` |
| Default value | `DB_UNIQUE_NAME.DB_DOMAIN` if defined |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Any ASCII string or comma-separated list of string names |
| Basic | No |
| Oracle RAC | Do not set the `SERVICE_NAMES` parameter for Oracle RAC environments. Instead, define services using Oracle Enterprise Manager and manage those services using Server Control (SRVCTL) utility. |

The instance registers its service names with the listener. When a client requests a service, the listener determines which instances offer the requested service and routes the client to the appropriate instance.

You can specify multiple service names to distinguish among different uses of the same database. For example:

```
SERVICE_NAMES = sales.example.com, widgetsales.example.com
```

You can also use service names to identify a single service that is available from two different databases through the use of replication.

If you do not qualify the names in this parameter with a domain, Oracle qualifies them with the value of the `DB_DOMAIN` parameter. If `DB_DOMAIN` is not specified, then no domain will be applied to the non-qualified `SERVICE_NAMES` values.

When you specify additional service names with this parameter, the default service name is not overridden. The default service name plus the additional service names specified with this parameter are the service names that clients can use to connect to the database.

Note:

The `SERVICE_NAMES` initialization parameter is deprecated in Oracle Database 19c and may be desupported in a future release.

Use of the `SERVICE_NAMES` parameter is no longer actively supported. It must not be used for high availability (HA) deployments and it is not supported for HA operations. This restriction includes FAN, load balancing, `FAILOVER_TYPE`, `FAILOVER_RESTORE`, `SESSION_STATE_CONSISTENCY`, and any other uses.

To manage your services, Oracle recommends that you instead use the `SRVCTL` command-line utility, the `GDSCTL` command-line utility, or the `DBMS_SERVICE` PL/SQL package.

See Also:

- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NETAG299) for more information on this parameter and its settings
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD7124) for information about services administration in an Oracle RAC environment
- " [DB\_DOMAIN](DB_DOMAIN.md) "
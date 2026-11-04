---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SERVICE_NAMES.html
tags:
  - oracle
  - 12c
  - reference
---

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

See Also:

- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NETAG299) for more information on this parameter and its settings
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=RACAD7124) for information about services administration in an Oracle RAC environment
- " [DB\_DOMAIN](DB_DOMAIN.md) "
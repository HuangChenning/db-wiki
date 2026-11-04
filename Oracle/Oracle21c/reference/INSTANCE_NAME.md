---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.164 INSTANCE\_NAME

In an Oracle Real Application Clusters environment, multiple instances can be associated with a single database service. Clients can override Oracle's connection load balancing by specifying a particular instance by which to connect to the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_NAME = ` `instance_id` |
| Default value | The instance's SID  Note: The SID identifies the instance's shared memory on a host, but may not uniquely distinguish this instance from other instances. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Alphanumeric ASCII characters and the underscore (\_) character, up to a maximum of 255 characters |
| Basic | No |

In a single-instance database system, the instance name is usually the same as the database name.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD816) and [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NETAG299) for more information
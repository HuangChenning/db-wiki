---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/server-side-planned-maintenance-command-examples.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Server-Side Planned Maintenance Command Examples

Note:

- If you are using these commands in scripts, you may find it helpful to include `wait = yes`.
- The parameters, `-force -failover` cause the service to start on other available instances configured on each service.
- For more details see [Managing a Group of Services for Maintenance](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=RACAD-GUID-D7D9D76F-22DF-4603-B7DC-8D7FC88F32E6) in Oracle Real Application Clusters Administration and Deployment Guide.

Stop one instance (inst1) with all associated services' configured `-drain_timeout` and `-stopoption` parameters

```
srvctl stop instance -db myDB -instance inst1 -force -failover
 -role primary
```

Stop all instances with explicit draining parameters that override the parameters configured for associated services.

```
srvctl stop instance -db db_name -node node_name
 -stopoption IMMEDIATE -drain_timeout <#> -force -failover
```

Stop a service with explicit draining parameters.

```
srvctl stop service -db db_name -service service_name
 -instance instance_name -drain_timeout <#> -stopoption IMMEDIATE
 -force -failover
```

Stop a Data Guard instance with explicit draining parameters.

```
srvctl stop instance -db db_name -node node_name
 -stopoption IMMEDIATE -drain_timeout <#> -force -failover
 -role primary
```

Relocate all services by database, node, or PDB.

```
srvctl relocate service -database db_unique_name
  -pdb pluggable_database
 {-oldinst old_inst_name [-newinst new_inst_name] |
                          -currentnode current_node
                         [-targetnode target_node]}
  -drain_timeout timeout -stopoption stop_option -force

srvctl relocate service -database db_unique_name
 -oldinst old_inst_name [-newinst new_inst_name]
 -drain_timeout timeout -stopoption stop_option
 -force

srvctl relocate service -database db_unique_name
 -currentnode current_node [-targetnode target_node]
 -drain_timeout timeout -stopoption stop_option
 -force
```

Switch over to a Data Guard secondary site with a wait timeout of 60 seconds, using Data Guard Broker.

```
SWITCHOVER TO dg_south WAIT 60
```

Switch over to Data Guard secondary site with a wait timeout from the services, using Data Guard Broker.

```
SWITCHOVER TO dg_south WAIT
```
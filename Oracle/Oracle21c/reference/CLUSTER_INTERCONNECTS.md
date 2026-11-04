---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CLUSTER_INTERCONNECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.44 CLUSTER\_INTERCONNECTS

`CLUSTER_INTERCONNECTS` can be used in Oracle Real Application Clusters environments to indicate cluster interconnects available for use for the database traffic.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CLUSTER_INTERCONNECTS = ` `ifn` `  [:  ``ifn` ` ] ...` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | One or more IP addresses, separated by colons |
| Basic | No |

Use this parameter to override the default interconnect configured for the database traffic, which is stored in the cluster registry. This procedure also may be useful with Data Warehouse systems that have reduced availability requirements and high interconnect bandwidth demands.

`CLUSTER_INTERCONNECTS` specifically overrides the following:

- Network classifications stored by `oifcfg` in the OCR.
- The default interconnect chosen by Oracle.

If you want to load-balance the interconnect, then Oracle recommends that you use link-bonding at the operating system level, even if you have two databases on the same server, so that multiple interconnects use the same address. Note that multiple private addresses provide load balancing, but do not provide failover unless bonded. If you specify multiple addresses in init.ora using `CLUSTER_INTERCONNECTS`, instead of bonding multiple addresses at the operating system level, then typically availability is reduced, because each network interface card failure will take down that instance.

Refer to your vendor documentation for information about bonding interfaces. Some vendor bonding architectures may require the use of this parameter.

If you have multiple database instances on Oracle Real Application Clusters nodes and want to use a specific interface for each instance, then you can set the `CLUSTER_INTERCONNECTS` initialization parameter to the IP address for each database instance. For example:

```
hr1.init.ora.cluster_interconnects="192.0.2.111"
oltp3.init.ora.cluster_interconnects="192.0.2.112"
```

If the Oracle RAC interconnect is configured to run on a different interface than the Oracle Clusterware interconnect, then this configuration can cause reduced availability, as failovers or instance evictions can be delayed if the Oracle RAC interconnect fails while the Oracle Clusterware NIC remains up.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD7296) for additional information about using `CLUSTER_INTERCONNECTS`
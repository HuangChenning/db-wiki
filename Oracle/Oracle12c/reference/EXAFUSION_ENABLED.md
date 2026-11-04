---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/EXAFUSION_ENABLED.html
tags:
  - oracle
  - 12c
  - reference
---

`EXAFUSION_ENABLED` is used to enable or disable the Exafusion accelerate cache fusion protocol feature, which is available on the Linux operating system of Oracle Exadata Database Machine only.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 1 on supported Exadata systems, and 0 on other systems |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0, 1 |
| Basic | No |
| Oracle RAC | All of the instances in an Oracle RAC cluster must enable this parameter, or all of the instances in an Oracle RAC cluster must disable the parameter. |

Exafusion provides lower latency, higher throughput direct to wire block transfers between Oracle Real Application Clusters (Oracle RAC) instances. Data is transferred directly from user space to the Infiniband network, leading to reduced CPU utilization and better scale-out performance.

To enable Exafusion, set the `EXAFUSION_ENABLED` initialization parameter to 1. To disable Exafusion, set the `EXAFUSION_ENABLED` initialization parameter to 0. This parameter cannot be set dynamically. It must be set before instance startup.

These are the prerequisites before enabling Exafusion:

- Oracle Storage Server Software release 12.1.2.1.1 or later is required.
- Mellanox ConnectX-2 and ConnectX-3 Host Channel Adapters (HCAs) are required.
- Oracle Unbreakable Enterprise Kernel 2 Quarterly Update 5 (UEK2QU5) kernels (2.6.39-400.2nn) or later are required.

The Exafusion feature does not support mixed mode operation on an Oracle RAC cluster. Either all the instances in an Oracle RAC cluster must have the feature enabled or none. Rolling upgrades of a non-Exafusion enabled Oracle RAC cluster to Exafusion are not supported.

Note:

Exafusion is available only on the Linux operating system of Oracle Exadata Database Machine. It is not supported on any non-engineered system or SPARC SuperCluster (SSC). If you set the `EXAFUSION_ENABLED` parameter on a non-supported platform, then the instance will be prevented from starting up, and an ORA-00439: The specified feature is not enabled: string error message is generated.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 1 (12.1.0.2) Bundle Patch 11 (BP11).
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/GCS_SERVER_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.139 GCS\_SERVER\_PROCESSES

`GCS_SERVER_PROCESSES` specifies the number of background GCS server processes (LMSn and LMnn) to serve the inter-instance traffic among Oracle RAC instances.

If there is high Cache Fusion congestion on the system, the number of GCS server processes could be increased to reduce Cluster wait time. Additionally, the number of GCS server processes could be increased to reduce the application brownout time associated with Cluster reconfiguration and Dynamic Re-mastering (DRM).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Oracle calculates the default value as follows (in order of precedence):  1. If `CLUSTER_DATABASE` is set to `false`, then `0` 2. If Oracle ASM, then `1` 3. If 1 - 3 CPUS, then `1` 4. If 4 - 15 CPUs, then `2` 5. If 128 or more CPUs and SGA is 100 GB or more, then (CPUs / 6). If the result includes a fraction, then the fraction is disregarded. 6. Otherwise, the value is 2 + (CPUs / 32). If the result includes a fraction, then the fraction is disregarded. For example, if you have 20 CPUs, then 2 + (20 / 32) would equal 2 GCS processes. 7. On NUMA-enabled systems with 32 or more CPUs, the value is rounded up to a multiple of the number of NUMA processor groups, with a limit of (CPUs / 4) rounded down to a multiple of the number of NUMA processor groups. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `0` if Oracle RAC is disabled (`CLUSTER_DATABASE` is set to `false`)  `1` to `100` if Oracle RAC is enabled (`CLUSTER_DATABASE` is set to `true`) |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

GCS server processes are only seen in an Oracle RAC environment.
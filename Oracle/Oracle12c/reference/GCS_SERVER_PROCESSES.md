---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/GCS_SERVER_PROCESSES.html
tags:
  - oracle
  - 12c
  - reference
---

`GCS_SERVER_PROCESSES` specifies the number of background GCS server processes (LMSn and LMnn) to serve the inter-instance traffic among Oracle RAC instances.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If 1 - 3 CPUS, then `1`  If 4 - 15 CPUs, then `2`  If 16 or more CPUs, then `2` + (CPUs / 32). If the result includes a fraction, then the fraction is disregarded. For example, if you had 20 CPUs, then 2 + (20 / 32) would equal 2 GCS processes.<sup>Foot 1</sup>  If `CLUSTER_DATABASE` is set to `false`, then `0`  If Oracle ASM, then `1` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `0` if Oracle RAC is disabled (`CLUSTER_DATABASE` is set to `false`)  `1` to `100` if Oracle RAC is enabled (`CLUSTER_DATABASE` is set to `true`) |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

<sup>Footnote 1</sup>

On certain operating systems, the RDBMS optimizes the default allocation of background GCS server processes based on the core to thread ratio of the CPU.

GCS server processes are only seen in an Oracle RAC environment.
---
title: GCS_SERVER_PROCESSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams096.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If 1 - 3 CPUS, then `1`  If 4 - 15 CPUs, then `2`  If 16 or more CPUs, then `2` + (CPUs / 32). If the result includes a fraction, then the fraction is disregarded. For example, if you had 20 CPUs, then 2 + (20 / 32) would equal 2 GCS processes.<sup>Foot 1</sup>  If `CLUSTER_DATABASE` is set to `false`, then `0`  If ASM, then `1` |
| Modifiable | No |
| Range of values | `1` to `36` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

<sup>Footnote 1</sup> On certain operating systems, the RDBMS optimizes the default allocation of background GCS server processes based on the core to thread ratio of the CPU.

`GCS_SERVER_PROCESSES` specifies the number of background GCS server processes (LMS0,... LMS9 and LMSa,... LMSz) to serve the inter-instance traffic among Oracle RAC instances. GCS server processes are only seen in an Oracle RAC environment.
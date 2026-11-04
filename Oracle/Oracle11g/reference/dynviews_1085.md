---
title: "V$CONFIGURED_INTERCONNECTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1085.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CONFIGURED_INTERCONNECTS` displays all the interconnects that Oracle is aware of. This view attempts to answer the question of where Oracle found the information about a specific interconnect.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(15)` | Name of the interconnect (such as eth0) |
| `IP_ADDRESS` | `VARCHAR2(16)` | IP address of the interconnect |
| `IS_PUBLIC` | `VARCHAR2(4)` | If the value is `YES`, the interface is known to the public.  If the value is `NO`, the interface is known to be private. Note that if the `CLUSTER_INTERCONNETS` initialization parameter is also specified, then it is expected that the interconnect is private. Oracle expects cluster traffic to be run on private interconnects only.  If the value is empty, it is unknown whether the interface is public or private.  Oracle Corporation recommends that you set the interface for Oracle Real Application Clusters (Oracle RAC) communication in the Oracle Cluster Repository (OCR). |
| `SOURCE` | `VARCHAR2(31)` | Indicates where this interface was picked up from: - Oracle Cluster Registry - Interface was configured in the OCR and Oracle Database found the interface in the OCR - Operating-system dependent software - Oracle Database automatically detects this - `CLUSTER_INTERCONNECTS` parameter - This initialization parameter was set |
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CLUSTER_INTERCONNECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.128 V$CLUSTER\_INTERCONNECTS

`V$CLUSTER_INTERCONNECTS` displays one or more interconnects that are being used for cluster communication.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(15)` | Name of the interconnect (such as eth0) |
| `IP_ADDRESS` | `VARCHAR2(64)` | IP address of the interconnect |
| `IS_PUBLIC` | `VARCHAR2(3)` | If the value is `YES`, the interface is known to the public.  If the value is `NO`, the interface is known to be private. Note that if the `CLUSTER_INTERCONNETS` initialization parameter is also specified, then it is expected that the interconnect is private. Oracle expects cluster traffic to be run on private interconnects only.  If the value is empty, it is unknown whether the interface is public or private.  Oracle recommends that you set the interface for Oracle Real Application Clusters (Oracle RAC) communication in the Oracle Cluster Registry (OCR). |
| `SOURCE` | `VARCHAR2(31)` | Indicates where this interface was picked up from:  - Oracle Cluster Registry - Interface was configured in the OCR and Oracle Database found the interface in the OCR - Operating-system dependent software - Oracle Database automatically detects this - `CLUSTER_INTERCONNECTS` parameter - This initialization parameter was set |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
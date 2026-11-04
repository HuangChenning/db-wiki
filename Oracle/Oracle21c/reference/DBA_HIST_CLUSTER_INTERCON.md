---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CLUSTER_INTERCON.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.385 DBA\_HIST\_CLUSTER\_INTERCON

`DBA_HIST_CLUSTER_INTERCON` displays information about the devices used by the instance to access the interconnect (that is, communicate with other instances).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NAME` | `VARCHAR2(256)` | `NOT NULL` | Operating system name of the device |
| `IP_ADDRESS` | `VARCHAR2(64)` | `NOT NULL` | IP address of the device |
| `IS_PUBLIC` | `VARCHAR2(3)` |  | Indicates whether the device is a public interface (`YES`) or a private interface (`NO`)  Public interfaces can be listened to by outside applications, which may be a security problem. Oracle recommends using private interfaces for interconnect. |
| `SOURCE` | `VARCHAR2(31)` |  | Describes the type of device |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
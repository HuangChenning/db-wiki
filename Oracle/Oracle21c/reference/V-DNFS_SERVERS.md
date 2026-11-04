---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DNFS_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.190 V$DNFS\_SERVERS

`V$DNFS_SERVERS` displays information about the Direct NFS servers accessed by Direct NFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Direct NFS server identifier |
| `SVRNAME` | `VARCHAR2(255)` | NFS server name |
| `DIRNAME` | `VARCHAR2(1024)` | Mounted directory |
| `MNTPORT` | `NUMBER` | NFS mount port |
| `NFSPORT` | `NUMBER` | NFS port |
| `NFSVERSION` | `VARCHAR2(8)` | NFS version |
| `WTMAX` | `NUMBER` | WTMAX exported by the NFS server |
| `RTMAX` | `NUMBER` | RTMAX exported by the NFS server |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `RDMAENABLE` | `VARCHAR2(16)` | Indicates whether the server is RDMA enabled. Possible values:  - `YES`: The server is RDMA enabled. - `NO`: The server is not RDMA enabled. |
| `RDMAPORT` | `NUMBER` | The port number for RDMA communications on the server. The value is always 20049. |
| `SECURITY` | `VARCHAR2(32)` | NFS RPC authentication method used for the given NFS export |

Note:

RDMA functionality is enabled only for the Exadata environment
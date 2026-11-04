---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DNFS_CHANNELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.188 V$DNFS\_CHANNELS

`V$DNFS_CHANNELS` displays information about the Oracle process connections (channels) open to NFS servers.

| Column | Datatype | Description |
| --- | --- | --- |
| `PNUM` | `NUMBER` | Oracle process number |
| `SVRNAME` | `VARCHAR2(255)` | NFS server name |
| `PATH` | `VARCHAR2(255)` | Network path to the NFS server specified by IP address or by name |
| `LOCAL` | `VARCHAR2(255)` | Local path on the database host specified by IP address or by name |
| `CH_ID` | `NUMBER` | Direct NFS channel identifier |
| `SVR_ID` | `NUMBER` | Direct NFS server identifier |
| `SENDS` | `NUMBER` | Send operations over the channel since the last select |
| `RECVS` | `NUMBER` | Receive operations over the channel since the last select |
| `PINGS` | `NUMBER` | Ping operations over the channel since the last select |
| `SPRECO` | `NUMBER` | Reconnects for the channel on the same port since the last select, given that the reconnect occurred during the first series of reconnect attempts. If the first series of reconnect attempts fails and the reconnect process on that channel times out for 5 minutes, the next reconnect on that channel will not increment either the `SPRECO` or `DPRECO` columns, regardless of the port connected to. |
| `DPRECO` | `NUMBER` | Reconnects for the channel on a different port since the last select, given that the reconnect occurred during the first series of reconnect attempts. If the first series of reconnect attempts fails and the reconnect process on that channel times out for 5 minutes, the next reconnect on that channel will not increment either the `SPRECO` or `DPRECO` columns, regardless of the port connected to. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `RDMA` | `NUMBER` | Indicates whether RDMA is enabled for the channel or not. Possible values:  - `0`: RDMA is not enabled for the channel - `1`: RDMA is enabled for the channel |
| `RDMA_CREDITS` | `NUMBER` | The number of RDMA credits supported by the server |
| `CLIENTPORT` | `NUMBER` | The client port to which the channel is bounded |
| `ACTIVE_SPEED` | `NUMBER` | The active speed of the HCA card present (in Gb/second) |
| `PEAK_FMR` | `NUMBER` | The size of fast memory registration (FMR) memory registered by the channel (in bytes) |
| `CURRENT_FMR` | `NUMBER` | The current FMR memory registered (in bytes) |
| `FMRREG_COUNT` | `NUMBER` | The number of FMR memory registration calls for the channel |

Note:

RDMA functionality is enabled only for the Exadata environment
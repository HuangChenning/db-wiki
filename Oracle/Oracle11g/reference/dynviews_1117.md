---
title: "V$DNFS_CHANNELS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1117.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `RECO` <sup>Foot 1</sup> | `NUMBER` | Reconnects for the channel since the last select |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)
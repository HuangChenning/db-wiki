---
title: "V$DNFS_SERVERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1119.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DNFS_SERVERS` displays information about the Direct NFS servers accessed by Direct NFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Direct NFS server identifier |
| `SVRNAME` | `VARCHAR2(255)` | NFS server name |
| `DIRNAME` | `VARCHAR2(1024)` | Mounted directory |
| `MNTPORT` | `NUMBER` | NFS mount port |
| `NFSPORT` | `NUMBER` | NFS port |
| `WTMAX` | `NUMBER` | WTMAX exported by the NFS server |
| `RTMAX` | `NUMBER` | RTMAX exported by the NFS server |
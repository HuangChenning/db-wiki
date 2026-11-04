---
title: "V$NFS_LOCKS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2073.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$NFS_LOCKS` displays information about byte range locks held on different files by NFS clients.

| Column | Datatype | Description |
| --- | --- | --- |
| `OPENSTATEID` | `RAW(16)` | Open state ID of the open owner |
| `OPENSEQUENCEID` | `NUMBER` | Open Sequence ID of the open owner |
| `LOCKSTATEID` | `RAW(16)` | Lock state ID of the lock owner |
| `LOCKSEQUENCEID` | `NUMBER` | Lock sequence ID of the lock owner |
| `LOCKOWNER` | `VARCHAR2(2000)` | Opaque string presented as identification by the lock owner to the NFS server |
| `OFFSET` | `NUMBER` | Byte Offset from which lock starts |
| `LENGTH` | `NUMBER` | Length of the lock |
| `LOCKTYPE` | `VARCHAR2(20)` | Type of the lock |
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-NFS_LOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.90 V$NFS\_LOCKS

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
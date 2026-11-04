---
title: "V$NFS_OPEN_FILES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2074.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$NFS_OPEN_FILES` displays information about all the files currently opened by clients at the NFS server.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENTID` | `NUMBER` | Number identifying the client |
| `OPENOWNEROPAQUE` | `VARCHAR2(2000)` | All the files currently opened by clients at the NFS server |
| `OPENSTATEID` | `RAW(16)` | Open state ID of the open owner |
| `FILEHANDLE` | `RAW(32)` | FileHandle of the file that has been opened |
| `OPENSEQUENCEID` | `NUMBER` | Open sequence ID of open owner |
| `OPENREAD` | `VARCHAR2(5)` | `TRUE` if the file is open for READ operations; otherwise `FALSE` |
| `OPENWRITE` | `VARCHAR2(5)` | `TRUE` if the file is open for WRITE operations; otherwise `FALSE` |
| `SHAREACCESS` | `VARCHAR2(15)` | Sharing mode of the file (SharedReadWrite, SharedRead, SharedWrite) |
| `SHAREDENY` | `VARCHAR2(13)` | Deny mode of the file (DenyReadWrite, DenyRead, DenyWrite) |
| `CONFIRMED` | `VARCHAR2(5)` | `TRUE` if open is confirmed; otherwise `FALSE` |
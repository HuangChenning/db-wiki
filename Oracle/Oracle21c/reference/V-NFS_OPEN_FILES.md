---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-NFS_OPEN_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.91 V$NFS\_OPEN\_FILES

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
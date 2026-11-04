---
title: "V$DNFS_FILES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1118.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DNFS_FILES` displays information about the Oracle process files open through Direct NFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILENAME` | `VARCHAR2(513)` | File name |
| `FILESIZE` | `NUMBER` | File Size |
| `PNUM` | `NUMBER` | Oracle process number which opened the file |
| `SVR_ID` | `NUMBER` | Direct NFS server identifier which identifies the server the file is open on |
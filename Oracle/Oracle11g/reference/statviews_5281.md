---
title: USER_DBFS_HS_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5281.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_DBFS_HS_FILES` displays files in the DBFS hierarchical store owned by the current user and their location on the backend device.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH` | `VARCHAR2(1024)` |  | Path name of the file |
| `SEQUENCENUMBER` | `NUMBER` |  | Sequence number of this piece of the file |
| `STARTOFFSET` | `NUMBER` |  | Begin offset of this piece in the tarball |
| `ENDOFFSET` | `NUMBER` |  | End offset of this piece in the tarball |
| `TARBALLID` | `NUMBER` |  | Tarball ID |
| `BACKUPFILENAME` | `VARCHAR2(256)` |  | File on backend in which this tarball is located |
| `TARSTARTOFFSET` | `NUMBER` |  | Begin Offset of this tarball in the backup file |
| `TARENDOFFSET` | `NUMBER` |  | End Offset of this tarball in the backup file |
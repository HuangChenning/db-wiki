---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_DBFS_HS_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.442 USER\_DBFS\_HS\_FILES

`USER_DBFS_HS_FILES` displays files in the Database File System (DBFS) hierarchical store owned by the current user and their location on the back-end device.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH` | `VARCHAR2(1024)` |  | Path name of the file |
| `SEQUENCENUMBER` | `NUMBER` |  | Sequence number of this piece of the file |
| `STARTOFFSET` | `NUMBER` |  | Begin offset of this piece in the tarball |
| `ENDOFFSET` | `NUMBER` |  | End offset of this piece in the tarball |
| `TARBALLID` | `NUMBER` |  | Tarball ID |
| `BACKUPFILENAME` | `VARCHAR2(256)` |  | File on back end in which this tarball is located |
| `TARSTARTOFFSET` | `NUMBER` |  | Begin offset of this tarball in the backup file |
| `TARENDOFFSET` | `NUMBER` |  | End offset of this tarball in the backup file |
---
title: "V$ASM_ACFSSNAPSHOTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1019.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_ACFSSNAPSHOTS` displays snapshot information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `SNAP_NAME` | `VARCHAR2(1024)` | Name of the snapshot |
| `CREATE_TIME` | `DATE` | Time when the snapshot was created |
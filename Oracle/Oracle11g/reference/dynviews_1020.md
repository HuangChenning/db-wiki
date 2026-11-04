---
title: "V$ASM_ACFSVOLUMES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1020.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_ACFSVOLUMES` displays information about mounted Oracle ACFS volumes, correlated with `V$ASM_FILESYSTEM`.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `VOL_LABEL` | `VARCHAR2(64)` | Volume label (optional name) assigned through `mkfs` / `acfsformat`; NULL if no name exists |
| `PRIMARY_VOL` | `VARCHAR2(5)` | Indicates whether the volume is the primary volume for the file system (`TRUE`) or not (`FALSE`) |
| `TOTAL_MB` | `NUMBER` | Size of the volume device (in megabytes) |
| `FREE_MB` | `NUMBER` | Available space on the volume device (in megabytes) |
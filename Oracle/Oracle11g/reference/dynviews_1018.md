---
title: "V$ASM_ACFS_SECURITY_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1018.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_ACFS_SECURITY_INFO` displays security information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `PREPARED_STATUS` | `VARCHAR2(7)` | Indicates whether the file system is prepared for security (`YES`) or not (`NO`); otherwise `UNKNOWN`. |
| `ENABLED_STATUS` | `VARCHAR2(8)` | Indicates whether security is enabled for the file system (`ENABLED`) or not (`DISABLED`); otherwise `UNKNOWN`. |

Note:

The `V$ASM_ACFS_SECURITY_INFO` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).
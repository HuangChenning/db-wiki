---
title: "V$ASM_ACFS_ENCRYPTION_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1017.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_ACFS_ENCRYPTION_INFO` displays encryption information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `SET_STATUS` | `VARCHAR2(7)` | Indicates whether encryption parameters have been set on the file system (`YES`) or not (`NO`); otherwise `UNKNOWN`. |
| `ENABLED_STATUS` | `VARCHAR2(8)` | Indicates whether file system level encryption is enabled (`ENABLED`) or not (`DISABLED`); otherwise `UNKNOWN`. |
| `ALGORITHM` | `VARCHAR2(7)` | Encryption algorithm used. AES is the only supported algorithm. |
| `KEY_LENGTH` | `VARCHAR2(7)` | Key length used for the encryption key |
| `LAST_REKEY_TIME` | `DATE` | Time that the volume was last rekeyed |

Note:

The `V$ASM_ACFS_ENCRYPTION_INFO` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).
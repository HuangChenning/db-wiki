---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/deprecated-rman-syntax.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This appendix describes Recovery Manager syntax that is deprecated and describes preferred syntax if any exists.

Deprecated RMAN syntax continues to be supported in subsequent releases for backward compatibility. For example, the `SET AUXNAME` command replaced the `SET CLONENAME` command in Oracle8i, and the `CONFIGURE AUXNAME` command replaced the `SET AUXNAME` command in Oracle9i. However, you can continue to run both `SET CLONENAME` and `SET AUXNAME` in all subsequent RMAN releases.

Table C-1 Deprecated RMAN Syntax

| Deprecated in Release | Deprecated Syntax | Preferred Current Syntax |
| --- | --- | --- |
| 19c | `ADVISE FAILURE` | n/a |
| 19c | `CHANGE` `FAILURE` | n/a |
| 19c | `LIST` `FAILURE` | n/a |
| 19c | `REPAIR FAILURE` | n/a |
| 12.1 | `ALTER DATABASE` | n/a |
| 11.2.0 | [CONFIGURE](CONFIGURE.md) or [SET](SET.md) `COMPRESSION ALGORITHM 'ZLIB'` | [CONFIGURE](CONFIGURE.md) or [SET](SET.md) `COMPRESSION ALGORITHM 'MEDIUM'` |
| 11.2.0 | [CONFIGURE](CONFIGURE.md) or [SET](SET.md) `COMPRESSION ALGORITHM 'BZIP2'` | [CONFIGURE](CONFIGURE.md) or [SET](SET.md) `COMPRESSION ALGORITHM 'BASIC'` |
| 11.2.0 | `V$FLASH_RECOVERY_AREA_USAGE` | `V$RECOVERY_AREA_USAGE` |
| 11.1.0 | `CONVERT` `ON TARGET PLATFORM` | `CONVERT` `ON DESTINATION PLATFORM` |
| 11.1.0 | `UNTIL RESTORE POINT` | `TO RESTORE POINT` |
| 11.1.0 | `BACKUP` `... AS STANDBY` | n/a |
| 11.1.0 | `... KEEP [LOGS \| NOLOGS]` | `... KEEP` |
| 11.1.0 | `BLOCKRECOVER` | `RECOVER` |
| 10.0.1 | `BACKUP` `... INCREMENTAL LEVEL` `[2,3,4]` | Levels other than `0` and `1` are deprecated. |
| 10.0.1 | `BACKUP` `... PARMS` | `CONFIGURE` ` CHANNEL ... PARMS` |
| 10.0.1 | `COPY` | `BACKUP` `AS COPY` |
| 10.0.1 | `CREATE CATALOG` `TABLESPACE` | `CREATE CATALOG` |
| 10.0.1 | `LIST` `... BY BACKUP [SUMMARY]` | n/a |
| 10.0.1 | `LIST` `... VERBOSE` | n/a |
| 10.0.1 | `RESTORE` ` ... PARMS` | `CONFIGURE` `CHANNEL ... PARMS` |
| 10.0.1 | `SEND` `... PARMS` | `CONFIGURE` `CHANNEL ... PARMS` |
| 9.2 | `REPLICATE` | `RESTORE` `CONTROLFILE FROM ...` |
| 9.2 | `SET` `AUTOLOCATE` | Enabled by default |
| 9.0.1 | `ALLOCATE CHANNEL FOR DELETE` | n/a |
| 9.0.1 | `ALLOCATE CHANNEL` ` ... TYPE` | `CONFIGURE` `CHANNEL ... DEVICE TYPE` |
| 9.0.1 | `ALLOCATE CHANNEL` `... KBYTES` | `CONFIGURE` `CHANNEL ... MAXPIECESIZE` |
| 9.0.1 | `ALLOCATE CHANNEL` `... READRATE` | `CONFIGURE` `CHANNEL ... RATE` |
| 9.0.1 | `... ARCHIVELOG ... LOGSEQ` | `... ARCHIVELOG ... SEQUENCE` |
| 9.0.1 | `BACKUP` `... SETSIZE` | `BACKUP` `...` `MAXSETSIZE` |
| 9.0.1 | `CHANGE` `... CROSSCHECK` | `CROSSCHECK` |
| 9.0.1 | `CHANGE` `... DELETE` | `DELETE` |
| 9.0.1 | `REPORT` `... AT LOGSEQ` | `REPORT ... AT SEQUENCE` |
| 9.0.1 | `SET` `AUXNAME` | `CONFIGURE` `AUXNAME` |
| 9.0.1 | `SET` `DUPLEX` | `SET` `BACKUP COPIES`  `CONFIGURE` `BACKUP COPIES` |
| 9.0.1 | `SET` `LIMIT CHANNEL ...` | `ALLOCATE CHANNEL` `...`  `CONFIGURE` `CHANNEL ...` |
| 9.0.1 | `SET` `SNAPSHOT` | `CONFIGURE` `SNAPSHOT` |
| 9.0.1 | `UNTIL LOGSEQ` (see `untilClause`) | `UNTIL SEQUENCE` (see `untilClause`) |
| 8.1.7 | `CONFIGURE` `COMPATIBLE` | n/a |
| 8.1.5 | `ALLOCATE CHANNEL` `CLONE` | `CONFIGURE` `AUXILIARY CHANNEL` |
| 8.1.5 | `CHANGE` `... VALIDATE` | `CROSSCHECK` |
| 8.1.5 | `CLONE` (see `RMAN`) | `AUXILIARY` (see `RMAN`) |
| 8.1.5 | `CONFIGURE` `CLONE` | `CONFIGURE` `AUXILIARY` |
| 8.1.5 | `MSGLOG` (see `RMAN`) | `LOG` (see `RMAN`) |
| 8.1.5 | `RCVCAT` (see `RMAN`) | `CATALOG` (see `RMAN`) |
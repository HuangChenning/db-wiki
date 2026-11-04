---
title: RMAN Compatibility Matrix
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat003.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

In general, the rules of RMAN compatibility are as follows:

- You can create an 8.x or 9.x recovery catalog schema in any Oracle database release 8.1.x (or higher), and a 10.0.1 (or higher) recovery catalog schema in any Oracle database release 9.0.1 (or higher).
- The recovery catalog schema version must be greater than or equal to the RMAN client version.
- If the recovery catalog is a virtual private catalog (see `CREATE CATALOG`), then the RMAN client connecting to it must be at patch level 10.1.0.6 or 10.2.0.3. Oracle9i RMAN clients cannot connect to a virtual private catalog. This version restriction does not affect RMAN client connections to an Oracle Database 11g base recovery catalog, even if the base catalog has virtual private catalog users.
- Ideally, the versions of the RMAN client and the target database are the same (although there are other valid combinations, listed in Table B-2). The RMAN client cannot be a greater version than the target or auxiliary database.
- While backing up an Oracle Database 10g or later database with the Oracle9i RMAN client, you cannot include a control file that was created using `COMPATIBLE=10.0.0` in a data file backup set. The workaround is to turn control file autobackup `ON`.
- The version of an auxiliary database instance must be equal to the version of the RMAN client.
- Any release of Oracle database can restore backup sets and copies created by any prior release back to Oracle8i.

Table B-2 shows version requirements for RMAN components. The symbol `>=` before a release means all Oracle Database releases from this release or later along with their patches.

Table B-2 RMAN Compatibility Table

| Target/Auxiliary Database | RMAN client | Recovery Catalog Database | Recovery Catalog Schema |
| --- | --- | --- | --- |
| 8.0.6 | 8.0.6 | \>=8.1.7 | \>=8.0.6 |
| 8.1.7 | 8.0.6.1 | \>=8.1.7 | \>=8.1.7 |
| 8.1.7 | 8.1.7 | \>=8.1.7 | \>=RMAN client |
| 8.1.7.4 | 8.1.7.4 | \>=8.1.7 | 8.1.7.4 |
| 8.1.7.4 | 8.1.7.4 | \>=8.1.7 | \>= 9.0.1.4 |
| 9.0.1 | 9.0.1 | \>=8.1.7 | \>= RMAN client |
| 9.2.0 | \>=9.0.1.3 and <= target database executable | \>=8.1.7 | \>= RMAN client |
| 10.1.0 | \>=9.0.1.3 and <= target database executable | \>=9.0.1 | \>= RMAN client |
| 10.2.0 | \>=9.0.1.3 and <= target database executable | \>=9.0.1 | \>= RMAN client |
| 11.1.0 | \>=9.0.1.3 and <= target database executable | \>=10.2.0.3 | \>= RMAN client |
| 11.2.0 | \>=9.0.1.3 and <= target database executable | \>=10.2.0.3 | \>= RMAN client |

When using an older version of the RMAN client with a newer version of the database, you do not get the features of the newer version. For example, when using the Oracle9i RMAN client to back up an Oracle Release 10g database, you do not have access to features like the fast recovery area, flashback database, TSPITR with an RMAN-managed auxiliary instance, or recovery through `RESETLOGS`.
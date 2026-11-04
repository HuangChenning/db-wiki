---
title: foreignlogRecordSpecifier
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl009.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the foreignlogRecordSpecifier subclause to specify a set of foreign archived redo log files for use in RMAN operations.

Usage Notes

Foreign archived redo log files are received by a logical standby database for a LogMiner session. Unlike normal archived logs, foreign archived logs have a different DBID. For this reason, they cannot be backed up or restored on a logical standby database.

A logical standby database creates foreign archived logs in the fast recovery area if the following conditions are met:

- A fast recovery area is configured on the logical standby database.
- A `LOG_ARCHIVE_DEST_` `n` initialization parameter is set to `'LOCATION=USE_DB_RECOVERY_FILE_DEST'` with a proper `VALID_FOR` setting to receive foreign archived logs.
- The `COMPATIBLE` initialization parameter is set to a value greater than or equal to 11.0.0.

Semantics

The semantics are exactly the same as for `archivelogRecordSpecifier` except that the logs are foreign archived redo log files.

Examples

Example 4-20 Crosschecking Foreign Archived Redo Log Files

This example crosschecks all foreign archived redo log files:

```
RMAN> CROSSCHECK FOREIGN ARCHIVELOG ALL;
```
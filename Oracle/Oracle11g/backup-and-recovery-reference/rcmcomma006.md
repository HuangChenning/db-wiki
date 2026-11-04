---
title: Summary of RMAN Subclauses
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma006.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Subclauses that are used in multiple commands are documented in a separate chapter to avoid unnecessary duplication. The descriptions of commands that use these subclauses include a cross-reference to the subclause entry in [Chapter 4, "RMAN Subclauses"](rcmsubcl.md). Table 1-3 summarizes the RMAN subclauses.

Table 1-3 Recovery Manager Subclauses

| Subclause | Specifies... |
| --- | --- |
| `allocOperandList::=` | Channel control options such as `PARMS` and `FORMAT` |
| `archivelogRecordSpecifier` | A range of archived redo log files |
| `completedTimeSpec` | A time range during which the backup or copy completed |
| `connectStringSpec` | The user name, password, and net service name for connecting to a target, recovery catalog, or auxiliary database. The connection is necessary to authenticate the user and identify the database |
| `datafileSpec` | A dataflow by filename or absolute file number |
| `deviceSpecifier` | The type of storage device for a backup or copy |
| `fileNameConversionSpec` | Patterns to transform source to target filenames during `BACKUP AS COPY`, `CONVERT` and `DUPLICATE` |
| `forDbUniqueNameOption` | All databases in a Data Guard environment or a database with the specified `DB_UNIQUE_NAME` |
| `foreignlogRecordSpecifier` | A range of foreign archived redo log file |
| `formatSpec` | A filename format for a backup or copy |
| `keepOption` | A backup or copy should or should not be exempt from the current retention policy |
| `listObjList` | Items that are displayed by the `LIST` command |
| `maintQualifier` | Additional options for maintenance commands such as `DELETE` and `CHANGE` |
| `maintSpec` | Files operated on by maintenance commands such as `CHANGE`, `CROSSCHECK`, and `DELETE` |
| `obsOperandList` | Backups that are obsolete according to specified criteria |
| `recordSpec` | Objects that the maintenance commands should operate on |
| `tempfileSpec` | A temp file by path or by file number |
| `untilClause` | An upper limit by time, SCN, or log sequence number. This clause is usually used to specify the desired point in time for an incomplete recovery |
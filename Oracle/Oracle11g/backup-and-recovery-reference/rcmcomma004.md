---
title: RMAN Reserved Words
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma004.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

The RMAN language contains numerous reserved words, which are or have been used in RMAN commands. In general, avoid using reserved words in ways that conflict with their primary meaning in the RMAN command language.

If you must use a reserved word as an argument to an RMAN command (for example, as a filename, tablespace name, tag name, and so on), then surround it with single or double quotes. Otherwise, RMAN cannot parse your command correctly and generates an error. Example 1-1 shows correct and incorrect usage of RMAN reserved words in RMAN commands.

Example 1-1 Using Reserved Words as Arguments to RMAN Commands

```
ALLOCATE CHANNEL backup DEVICE TYPE DISK;         # incorrect
ALLOCATE CHANNEL "backup" DEVICE TYPE DISK;       # correct
BACKUP DATABASE TAG full;                         # incorrect
BACKUP DATABASE TAG 'full';                       # correct
```

Table 1-1 lists all of the current reserved words.

Table 1-1 RMAN Reserved Words

| A-C | C-D | D-L | L-P | P-S | S-W |
| --- | --- | --- | --- | --- | --- |
| `,` | `CHANGE` | `DURATION` | `LOGSEQ` | `PARALLELMEDIARESTORE` | `SECTION` |
| `#` | `CHANNEL` | `ECHO` | `LOGS` | `PARALLEL` | `SEND` |
| `(` | `CHECKSYNTAX` | `ENCRYPTION` | `LOG` | `PARAMETER` | `SEQUENCE` |
| `)` | `CHECK` | `EXCLUDE` | `LOGSCN` | `PARAMETER_VALUE_CONVERT` | `SETLIMIT` |
| `\` | `CLEAR` | `EXECUTE` | `LOW` | `PARMS` | `SETSIZE` |
| `{` | `CLONENAME` | `EXIT` | `MAINTENANCE` | `PARTIAL` | `SET` |
| `}` | `CLONE` | `EXPIRED` | `MASK` | `PASSWORD` | `SHIPPED` |
| `<<<` | `CLONE_CF` | `EXPORT` | `MAXCORRUPT` | `PFILE` | `SHOW` |
| `>>>` | `CLOSED` | `FAILOVER` | `MAXDAYS` | `PIPE` | `SHUTDOWN` |
| `;` | `CMDFILE` | `FAILURE` | `MAXOPENFILES` | `PLATFORM` | `SINCE` |
| `&` | `COMMAND` | `FILESPERSET` | `MAXPIECESIZE` | `PLSQL` | `SIZE` |
| `_` |  |  |  |  |  |
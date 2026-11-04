---
title: "V$ARCHIVE_PROCESSES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1015.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ARCHIVE_PROCESSES` displays the state of the various ARCH processes for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `PROCESS` | `NUMBER` | Identifier for the ARCH process for the instance, numbered from 0-9 |
| `STATUS` | `VARCHAR2(10)` | Status of the ARCH process, displayed as a keyword. Possible values are: `STOPPED`, `SCHEDULED`, `STARTING`, `ACTIVE`, `STOPPING`, and `TERMINATED`. |
| `LOG_SEQUENCE` | `NUMBER` | This is the online redo log sequence number currently being archived, if `STATE` =" `BUSY` " |
| `STATE` | `VARCHAR2(4)` | This is the current state of the ARCH process, displayed as a keyword. Possible keywords are `IDLE` or `BUSY`. |
| `ROLES` <sup>Foot 1</sup> | `VARCHAR2(36)` | The list of roles assigned to the archive process.  The roles include: `HEART_BEAT`, `NO_FAL`, `NO_SRL`, `CLEAR_LOGS` |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)
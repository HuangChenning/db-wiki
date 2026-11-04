---
title: "V$CONTROLFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1087.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CONTROLFILE` displays the names of the control files.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(7)` | `INVALID` if the name cannot be determined (which should not occur); NULL if the name can be determined |
| `NAME` | `VARCHAR2(513)` | Name of the control file |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `BLOCK_SIZE` | `NUMBER` | Control file block size |
| `FILE_SIZE_BLKS` | `NUMBER` | Control file size (in blocks) |
---
title: "V$DATAFILE_HEADER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1102.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAFILE_HEADER` displays datafile information from the datafile headers.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Datafile number (from control file) |
| `STATUS` | `VARCHAR2(7)` | `ONLINE` \| `OFFLINE` (from control file) |
| `ERROR` | `VARCHAR2(18)` | NULL if the datafile header read and validation were successful. If the read failed then the rest of the columns are NULL. If the validation failed then the rest of columns may display invalid data. If there is an error then usually the datafile must be restored from a backup before it can be recovered or used. |
| `FORMAT` | `NUMBER` | Indicates the format for the header block. The possible values are `6,` `7`, `8`, `10` or `0`.  `6` - indicates Oracle Version 6  `7` - indicates Oracle Version 7  `8` - indicates Oracle Version 8  `10` - indicates Oracle Version 10  `0` - indicates the format could not be determined (for example, the header could not be read) |
| `RECOVER` | `VARCHAR2(3)` | File needs media recovery (`YES` \| `NO`) |
| `FUZZY` | `VARCHAR2(3)` | File is fuzzy (`YES` \| `NO`) |
| `CREATION_CHANGE#` | `NUMBER` | Datafile creation change# |
| `CREATION_TIME` | `DATE` | Datafile creation timestamp |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Tablespace name |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Tablespace relative datafile number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change# |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Datafile checkpoint change# |
| `CHECKPOINT_TIME` | `DATE` | Datafile checkpoint timestamp |
| `CHECKPOINT_COUNT` | `NUMBER` | Datafile checkpoint count |
| `BYTES` | `NUMBER` | Current datafile size in bytes |
| `BLOCKS` | `NUMBER` | Current datafile size in blocks |
| `NAME` | `VARCHAR2(513)` | Datafile name |
| `SPACE_HEADER` | `VARCHAR2(40)` | Represents the block address of a space file header block of a locally managed datafile |
| `LAST_DEALLOC_SCN` | `VARCHAR2(16)` | Last deallocated SCN |
| `UNDO_OPT_CURRENT_CHANGE#` | `VARCHAR2(40)` | For internal use only |
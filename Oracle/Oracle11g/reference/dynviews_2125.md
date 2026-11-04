---
title: "V$RECOVERY_FILE_DEST"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2125.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_FILE_DEST` displays information about the disk quota and current disk usage in the fast recovery area.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(513)` | Location name. This is the value specified in the `DB_RECOVERY_FILE_DEST` initialization parameter. |
| `SPACE_LIMIT` | `NUMBER` | Maximum amount of disk space (in bytes) that the database can use for the fast recovery area. This is the value specified in the `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter. |
| `SPACE_USED` | `NUMBER` | Amount of disk space (in bytes) used by fast recovery area files created in current and all previous fast recovery areas. Changing fast recovery areas does not reset `SPACE_USED` to `0`. |
| `SPACE_RECLAIMABLE` | `NUMBER` | Total amount of disk space (in bytes) that can be created by deleting obsolete, redundant, and other low priority files from the fast recovery area |
| `NUMBER_OF_FILES` | `NUMBER` | Number of files in the fast recovery area |
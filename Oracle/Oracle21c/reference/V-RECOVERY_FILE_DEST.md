---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_FILE_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.158 V$RECOVERY\_FILE\_DEST

`V$RECOVERY_FILE_DEST` displays information about the disk quota and current disk usage in the fast recovery area.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(513)` | Location name. This is the value specified in the `DB_RECOVERY_FILE_DEST` initialization parameter. |
| `SPACE_LIMIT` | `NUMBER` | Maximum amount of disk space (in bytes) that the database can use for the fast recovery area. This is the value specified in the `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter. |
| `SPACE_USED` | `NUMBER` | Amount of disk space (in bytes) used by fast recovery area files created in current and all previous fast recovery areas. Changing fast recovery areas does not reset `SPACE_USED` to `0`. |
| `SPACE_RECLAIMABLE` | `NUMBER` | Total amount of disk space (in bytes) that can be created by deleting obsolete, redundant, and other low priority files from the fast recovery area |
| `NUMBER_OF_FILES` | `NUMBER` | Number of files in the fast recovery area |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DB\_RECOVERY\_FILE\_DEST](DB_RECOVERY_FILE_DEST.md) "
- " [DB\_RECOVERY\_FILE\_DEST\_SIZE](DB_RECOVERY_FILE_DEST_SIZE.md) "
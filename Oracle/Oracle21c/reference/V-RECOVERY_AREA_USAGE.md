---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_AREA_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.157 V$RECOVERY\_AREA\_USAGE

`V$RECOVERY_AREA_USAGE` displays usage information about recovery areas.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_TYPE` | `VARCHAR2(23)` | File type:  - `CONTROL FILE` - `REDO LOG` - `ARCHIVED LOG` - `BACKUP PIECE` - `IMAGE COPY` - `FLASHBACK LOG` - `REMOTE ARCHIVED LOG` |
| `PERCENT_SPACE_USED` | `NUMBER` | Percent of the recovery area that is in use |
| `PERCENT_SPACE_RECLAIMABLE` | `NUMBER` | Percent of the recovery area that is reclaimable |
| `NUMBER_OF_FILES` | `NUMBER` | Number of files in the recovery area |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
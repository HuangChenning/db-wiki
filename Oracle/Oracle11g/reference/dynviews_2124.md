---
title: "V$RECOVERY_AREA_USAGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2124.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_AREA_USAGE` displays usage information about recovery areas.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_TYPE` | `VARCHAR2(20)` | File type: - `CONTROL FILE` - `REDO LOG` - `ARCHIVED LOG` - `BACKUP PIECE` - `IMAGE COPY` - `FLASHBACK LOG` - `REMOTE ARCHIVED LOG` |
| `PERCENT_SPACE_USED` | `NUMBER` | Percent of the recovery area that is in use |
| `PERCENT_SPACE_RECLAIMABLE` | `NUMBER` | Percent of the recovery area that is reclaimable |
| `NUMBER_OF_FILES` | `NUMBER` | Number of files in the recovery area |
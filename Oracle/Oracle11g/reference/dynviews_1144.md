---
title: "V$FLASHBACK_DATABASE_LOG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1144.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FLASHBACK_DATABASE_LOG` displays information about the flashback data. Use this view to help estimate the amount of flashback space required for the current workload.

| Column | Datatype | Description |
| --- | --- | --- |
| `OLDEST_FLASHBACK_SCN` | `NUMBER` | Lowest system change number (SCN) in the flashback data, for any incarnation |
| `OLDEST_FLASHBACK_TIME` | `DATE` | Time of the lowest SCN in the flashback data, for any incarnation |
| `RETENTION_TARGET` | `NUMBER` | Target retention time (in minutes) |
| `FLASHBACK_SIZE` | `NUMBER` | Current size (in bytes) of the flashback data |
| `ESTIMATED_FLASHBACK_SIZE` | `NUMBER` | Estimated size of flashback data needed for the current target retention |
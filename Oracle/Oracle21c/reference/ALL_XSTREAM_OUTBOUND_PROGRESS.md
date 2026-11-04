---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XSTREAM_OUTBOUND_PROGRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.163 ALL\_XSTREAM\_OUTBOUND\_PROGRESS

`ALL_XSTREAM_OUTBOUND_PROGRESS` displays information about the progress made by the XStream outbound servers accessible to the current user.

Related View

`DBA_XSTREAM_OUTBOUND_PROGRESS` displays information about the progress made by all XStream outbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the outbound server |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the database where the transaction originated. For a PDB, this is the global name of the PDB. |
| `PROCESSED_LOW_POSITION` | `RAW(64)` |  | Position of the low-watermark transaction processed by the outbound server |
| `PROCESSED_LOW_TIME` | `DATE` |  | Time when the processed low position was last updated by the outbound server |
| `OLDEST_POSITION` | `RAW(64)` |  | The position of the earliest LCR that is required by the XStream client application |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database |
| `PROCESSED_LOW_SCN` | `NUMBER` | `NOT NULL` | SCN of the processed low transaction |
| `OLDEST_SCN` | `NUMBER` | `NOT NULL` | Oldest SCN of the transactions currently being captured |

See Also:

" [DBA\_XSTREAM\_OUTBOUND\_PROGRESS](DBA_XSTREAM_OUTBOUND_PROGRESS.md) "
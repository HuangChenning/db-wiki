---
title: ALL_XSTREAM_OUTBOUND_PROGRESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2145.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XSTREAM_OUTBOUND_PROGRESS` displays information about the progress made by the XStream outbound servers accessible to the current user.

Related View

`DBA_XSTREAM_OUTBOUND_PROGRESS` displays information about the progress made by all XStream outbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the outbound server |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Database where the transaction originated |
| `PROCESSED_LOW_POSITION` | `RAW(64)` |  | Position of the low-watermark transaction processed by the outbound server |
| `PROCESSED_LOW_TIME` | `DATE` |  | Time when the processed low position was last updated by the outbound server |
| `OLDEST_POSITION` <sup>Foot 1</sup> | `RAW(64)` |  | The position of the earliest LCR that is required by the XStream client application |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DBA\_XSTREAM\_OUTBOUND\_PROGRESS"](statviews_5111.md)
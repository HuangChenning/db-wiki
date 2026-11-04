---
title: ALL_XSTREAM_INBOUND_PROGRESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2143.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XSTREAM_INBOUND_PROGRESS` displays information about the progress made by the XStream inbound servers accessible to the current user.

Related View

`DBA_XSTREAM_INBOUND_PROGRESS` displays information about the progress made by all XStream inbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the inbound server |
| `PROCESSED_LOW_POSITION` | `RAW(64)` |  | Position of the processed low transaction |
| `APPLIED_LOW_POSITION` | `RAW(64)` |  | All messages with a commit position less than this value have been applied |
| `APPLIED_HIGH_POSITION` | `RAW(64)` |  | Highest commit position of a transaction that has been applied |
| `SPILL_POSITION` | `RAW(64)` |  | Position of the spill low watermark of the transactions currently being applied |
| `OLDEST_POSITION` <sup>Foot 1</sup> | `RAW(64)` |  | Earliest position of the transactions currently being applied |
| `OLDEST_MESSAGE_NUMBER` <sup>Footref 1</sup> | `NUMBER` | `NOT` `NULL` | Earliest message number of the transactions currently being applied |
| `APPLIED_MESSAGE_NUMBER` <sup>Footref 1</sup> | `NUMBER` | `NOT` `NULL` | Message number up to which all transactions have definitely been applied. This value is the low watermark for the inbound server. That is, messages with a commit message number less than or equal to this message number have definitely been applied, but some messages with a higher commit message number may also have been applied. |
| `APPLIED_TIME` <sup>Footref 1</sup> | `DATE` |  | Time at which the message with the message number displayed in the `APPLIED_MESSAGE_NUMBER` column was applied |
| `APPLIED_MESSAGE_CREATE_TIME` <sup>Footref 1</sup> | `DATE` |  | Time at which the message with the message number displayed in the `APPLIED_MESSAGE_NUMBER` column was created at its source database |
| `SPILL_MESSAGE_NUMBER` <sup>Footref 1</sup> | `NUMBER` |  | Spill low watermark. Any message with a lower SCN has either been applied or spilled to disk. The XStream client application does not need to send logical change records (LCRs) with a lower SCN than the spill low watermark. Spilled messages may not have been applied yet. |
| `SOURCE_DATABASE` <sup>Footref 1</sup> | `VARCHAR2(128)` | `NOT` `NULL` | Database where the transaction originated |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DBA\_XSTREAM\_INBOUND\_PROGRESS"](statviews_5108.md)
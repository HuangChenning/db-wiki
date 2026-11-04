---
title: ALL_GG_INBOUND_PROGRESS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1099.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_GG_INBOUND_PROGRESS` displays information about the progress made by the GoldenGate inbound servers accessible to the current user.

Related View

`DBA_GG_INBOUND_PROGRESS` displays information about the progress made by all GoldenGate inbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the inbound server |
| `PROCESSED_LOW_POSITION` | `VARCHAR2(4000)` |  | Position of the processed low transaction |
| `APPLIED_LOW_POSITION` | `VARCHAR2(4000)` |  | All messages with commit position less than this value have been applied.  This column should be used to view the progress of the GoldenGate apply. This column will hold an Oracle SCN numeric value in text format for an Oracle source database. For a non-Oracle source database, this column will hold the apply low position in GoldenGate CSN text format for that specific source database. |
| `APPLIED_HIGH_POSITION` | `VARCHAR2(4000)` |  | Highest commit position of a transaction that has been applied |
| `SPILL_POSITION` | `VARCHAR2(4000)` |  | Position of the spill low watermark of the transactions currently being applied |
| `OLDEST_POSITION` | `VARCHAR2(4000)` |  | Earliest position of the transactions currently being applied |
| `APPLIED_LOW_SCN` | `NUMBER` | `NOT NULL` | All SCN below or equal to this number have been successfully applied. This column is not applicable for GoldenGate replication since the source database may be non-Oracle. |
| `APPLIED_TIME` | `DATE` |  | Time at which the `APPLIED_MESSAGE_NUMBER` message was applied |
| `APPLIED_MESSAGE_CREATE_TIME` | `DATE` |  | Time at which the `APPLIED_MESSAGE_NUMBER` message was created |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Database where the transaction originated |
| `LOGBSN` | `VARCHAR2(4000)` |  | Log BSN value from the GoldenGate trail file. |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

["DBA\_GG\_INBOUND\_PROGRESS"](statviews_3196.md)
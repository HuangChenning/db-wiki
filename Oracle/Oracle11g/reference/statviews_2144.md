---
title: ALL_XSTREAM_OUTBOUND
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2144.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XSTREAM_OUTBOUND` displays information about the XStream outbound servers accessible to the current user.

Related View

`DBA_XSTREAM_OUTBOUND` displays information about all XStream outbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the outbound server |
| `CONNECT_USER` | `VARCHAR2(30)` |  | Name of the user who can connect to the outbound server and process the outbound LCRs |
| `CAPTURE_NAME` | `VARCHAR2(30)` |  | Name of the Streams capture process |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Database where the transaction originated |
| `CAPTURE_USER` | `VARCHAR2(30)` |  | Current user who is enqueuing captured messages |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue associated with the outbound server |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue associated with the outbound server |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment |
| `CREATE_DATE` | `TIMESTAMP(6)` |  | Date when the outbound server was created |
| `STATUS` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | Status of the inbound server: - `DISABLED` - The outbound server is not running. - `DETACHED` - The outbound server is running, but the XStream client application is not attached to it. - `ATTACHED` - The outbound server is running, and the XStream client application is attached to it. - `ABORTED` - The outbound server became disabled because it encountered an error. |
| `COMMITTED_DATA_ONLY` <sup>Footref 1</sup> | `VARCHAR2(3)` |  | `YES` if the outbound server can send only LCRs in committed transactions to the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks.  `NO` if the outbound server can send LCRs in transactions that have not yet committed to the XStream client application. This mode is for internal Oracle use only. |
| `START_SCN` <sup>Footref 1</sup> | `NUMBER` |  | The SCN from which the outbound server's capture process started capturing changes when it was last started |
| `START_TIME` <sup>Footref 1</sup> | `TIMESTAMP(6)` |  | The time from which the outbound server's capture process started capturing changes when it was last started |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DBA\_XSTREAM\_OUTBOUND"](statviews_5110.md)
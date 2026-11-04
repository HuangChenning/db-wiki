---
title: ALL_XSTREAM_INBOUND
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2142.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XSTREAM_INBOUND` displays information about the XStream inbound servers accessible to the current user.

Related View

`DBA_XSTREAM_INBOUND` displays information about all XStream inbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the inbound server |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue associated with the inbound server |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue associated with the inbound server |
| `APPLY_USER` | `VARCHAR2(30)` |  | Name of the user who can connect to the inbound server and apply messages |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment |
| `CREATE_DATE` | `TIMESTAMP(6)` |  | Date when the inbound server was created |
| `STATUS` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | Status of the inbound server: - `DISABLED` - The inbound server is not running. - `DETACHED` - The inbound server is running, but the XStream client application is not attached to it. - `ATTACHED` - The inbound server is running, and the XStream client application is attached to it. - `ABORTED` - The inbound server became disabled because it encountered an error. |
| `COMMITTED_DATA_ONLY` <sup>Footref 1</sup> | `VARCHAR2(3)` |  | `YES` if the inbound server can receive only LCRs in committed transactions from the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks.  `NO` if the inbound server can receive LCRs in transactions that have not yet committed. This mode is for internal Oracle use only. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DBA\_XSTREAM\_INBOUND"](statviews_5107.md)
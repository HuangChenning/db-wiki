---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XSTREAM_OUTBOUND.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.162 ALL\_XSTREAM\_OUTBOUND

`ALL_XSTREAM_OUTBOUND` displays information about the XStream outbound servers accessible to the current user.

Related View

`DBA_XSTREAM_OUTBOUND` displays information about all XStream outbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the outbound server |
| `CONNECT_USER` | `VARCHAR2(128)` |  | Name of the user who can connect to the outbound server and process the outbound LCRs |
| `CAPTURE_NAME` | `VARCHAR2(128)` |  | Name of the Replication capture process |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Database where the transaction originated |
| `CAPTURE_USER` | `VARCHAR2(128)` |  | Current user who is enqueuing captured messages |
| `QUEUE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue associated with the outbound server |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue associated with the outbound server |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment |
| `CREATE_DATE` | `TIMESTAMP(6)` |  | Date when the outbound server was created |
| `STATUS` | `VARCHAR2(8)` |  | Status of the outbound server:  - `DISABLED` - The outbound server is not running. - `DETACHED` - The outbound server is running, but the XStream client application is not attached to it. - `ATTACHED` - The outbound server is running, and the XStream client application is attached to it. - `ABORTED` - The outbound server became disabled because it encountered an error. |
| `COMMITTED_DATA_ONLY` | `VARCHAR2(3)` |  | `YES` if the outbound server can send only LCRs in committed transactions to the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks.  `NO` if the outbound server can send LCRs in transactions that have not yet committed to the XStream client application. This mode is for internal Oracle use only. |
| `START_SCN` | `NUMBER` |  | The SCN from which the outbound server's capture process started capturing changes when it was last started |
| `START_TIME` | `TIMESTAMP(6)` |  | The time from which the outbound server's capture process started capturing changes when it was last started |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database |
| `LCRID_VERSION` | `NUMBER` |  | LCR ID format currently being used |

See Also:

" [DBA\_XSTREAM\_OUTBOUND](DBA_XSTREAM_OUTBOUND.md) "
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XSTREAM_INBOUND.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.159 ALL\_XSTREAM\_INBOUND

`ALL_XSTREAM_INBOUND` displays information about the XStream inbound servers accessible to the current user.

Related View

`DBA_XSTREAM_INBOUND` displays information about all XStream inbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the inbound server |
| `QUEUE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue associated with the inbound server |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue associated with the inbound server |
| `APPLY_USER` | `VARCHAR2(128)` |  | Name of the user who can connect to the inbound server and apply messages |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment |
| `CREATE_DATE` | `TIMESTAMP(6)` |  | Date when the inbound server was created |
| `STATUS` | `VARCHAR2(8)` |  | Status of the inbound server:  - `DISABLED` - The inbound server is not running. - `DETACHED` - The inbound server is running, but the XStream client application is not attached to it. - `ATTACHED` - The inbound server is running, and the XStream client application is attached to it. - `ABORTED` - The inbound server became disabled because it encountered an error. |
| `COMMITTED_DATA_ONLY` | `VARCHAR2(3)` |  | `YES` - means the inbound server can receive only LCRs in committed transactions from the XStream client application. A committed transaction is an assembled, noninterleaving transaction with no rollbacks. |

See Also:

" [DBA\_XSTREAM\_INBOUND](DBA_XSTREAM_INBOUND.md) "
---
title: ALL_GOLDENGATE_INBOUND
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1100.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_GOLDENGATE_INBOUND` displays information about the GoldenGate inbound servers accessible to the current user.

Related View

`DBA_GOLDENGATE_INBOUND` displays information about all GoldenGate inbound servers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLICAT_NAME` | `VARCHAR2(4000)` |  | The name of the replicat group created from GGSCI using GoldenGate |
| `SERVER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the inbound server |
| `APPLY_USER` | `VARCHAR2(30)` |  | Name of the user who can connect to the inbound server and apply messages |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment |
| `CREATE_DATE` | `TIMESTAMP(6)` |  | Date when inbound server was created |
| `STATUS` | `VARCHAR2(8)` |  | Status of the inbound server: - `DISABLED` - The inbound server is not running. - `DETACHED` - The inbound server is running, but the GoldenGate client application is not attached to it. - `ATTACHED` - The inbound server is running, and the GoldenGate client application is attached to it. - `ABORTED` - The inbound server became disabled because it encountered an error. |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

["DBA\_GOLDENGATE\_INBOUND"](statviews_3198.md)
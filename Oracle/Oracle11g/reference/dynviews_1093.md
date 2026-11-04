---
title: "V$CPOOL_CONN_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1093.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CPOOL_CONN_INFO` displays connection information about each connection to the connection broker.

| Column | Datatype | Description |
| --- | --- | --- |
| `CMON_ADDR` | `RAW(4 \| 8)` | Address of the connection broker |
| `SESSION_ADDR` | `RAW(4 \| 8)` | Address of the session associated with the connection; NULL if the connection does not have an associated session |
| `CONNECTION_ADDR` | `RAW(4 \| 8)` | Address of the connection |
| `USERNAME` | `VARCHAR2(1024)` | Name of the user associated with the connection |
| `PROXY_USER` | `VARCHAR2(1024)` | Name of the proxy user |
| `CCLASS_NAME` | `VARCHAR2(1024)` | Connection class associated with the connection |
| `PURITY` | `VARCHAR2(1024)` | Purity used to create the connection (can be `SELF` or `NEW`) |
| `TAG` | `VARCHAR2(1024)` | Tag, if specified, at connection creation time |
| `SERVICE` | `VARCHAR2(64)` | TNS service name for the connection |
| `PROCESS_ID` | `VARCHAR2(24)` | Client process ID of the process which created the connection |
| `PROGRAM` | `VARCHAR2(48)` | Program name of the client process which created the connection |
| `MACHINE` | `VARCHAR2(64)` | Machine name of the client process which created the connection |
| `TERMINAL` | `VARCHAR2(30)` | Terminal identifier of the client process which created the connection |
| `CONNECTION_MODE` | `VARCHAR2(1024)` | Reserved for internal use |
| `CONNECTION_STATUS` | `VARCHAR2(10)` | Status of the connection: |
| `CLIENT_REGID` <sup>Foot 1</sup> | `NUMBER` | Query cache registration ID sent by the client |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).
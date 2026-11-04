---
title: "V$NFS_CLIENTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2072.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$NFS_CLIENTS` displays information about NFS clients currently connected to the XML DB NFS Server.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENTID` | `NUMBER` | A number identifying the client |
| `PRINCIPAL` | `VARCHAR2(2000)` | User string denoting the principal that set the client ID (`SetClientId`) |
| `CLIENTOPAQUEIDENTIFIER` | `VARCHAR2(1000)` | Opaque string presented as identification by the client to the NFS server |
| `VERIFIER` | `RAW(8)` | Verifier presented by the client |
| `LEASEEXPIRY` | `NUMBER` | Number of seconds in which the lease expires for the client |
| `CLIENTADDR` | `VARCHAR2(2000)` | Address of the client |
| `CONFIRMED` | `VARCHAR2(5)` | `TRUE` if the client is confirmed; otherwise `FALSE` |
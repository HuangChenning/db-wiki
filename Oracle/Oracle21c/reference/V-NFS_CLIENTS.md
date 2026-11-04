---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-NFS_CLIENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.89 V$NFS\_CLIENTS

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
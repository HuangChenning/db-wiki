---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DISPATCHER_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.186 V$DISPATCHER\_CONFIG

`V$DISPATCHER_CONFIG` displays information about the dispatcher configurations and their attributes.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONF_INDX` | `NUMBER` | Zero-based index of the `DISPATCHERS` configuration |
| `NETWORK` | `VARCHAR2(1024)` | Network protocol or listening address of dispatchers (may be truncated) |
| `DISPATCHERS` | `NUMBER` | Number of dispatchers to maintain for the configuration |
| `CONNECTIONS` | `NUMBER` | Maximum number of concurrent connections per dispatcher |
| `SESSIONS` | `NUMBER` | Maximum number of concurrent sessions per dispatcher |
| `MULTIPLEX` | `VARCHAR2(4)` | Indicates whether Session Multiplexing is on:  - `IN` - `OUT` - `BOTH` - `OFF` |
| `LISTENER` | `VARCHAR2(1200)` | Listeners to register dispatchers with (may be truncated) |
| `SERVICE` | `VARCHAR2(512)` | Service names supported (may be truncated) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
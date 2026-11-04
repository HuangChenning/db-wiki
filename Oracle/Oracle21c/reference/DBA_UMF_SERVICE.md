---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UMF_SERVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.77 DBA\_UMF\_SERVICE

`DBA_UMF_SERVICE` displays information about the registered services in the Remote Management Framework (RMF).

This view returns no rows if you are querying on an RMF source node. It returns all the registered services in the topology if you are querying on a target node

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TOPOLOGY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Topology name for the service |
| `NODE_ID` | `NUMBER` | `NOT NULL` | Node ID of the node providing the service |
| `SERVICE_ID` | `VARCHAR2(7)` |  | Service Identifier. Possible values:  - `1`: Automatic Workload Repository - `2`: SQL Tuning |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for information about configuring the Remote Management Framework (RMF) architecture
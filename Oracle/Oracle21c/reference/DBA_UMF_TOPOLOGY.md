---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UMF_TOPOLOGY.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.78 DBA\_UMF\_TOPOLOGY

`DBA_UMF_TOPOLOGY` displays information about the registered topologies in the Remote Management Framework (RMF).

This view returns no rows if you are querying on an RMF source node. It returns one row per registered topology if you are querying on a target node.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TOPOLOGY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Unique topology name |
| `TARGET_ID` | `NUMBER` |  | Node ID of the target node |
| `TOPOLOGY_VERSION` | `NUMBER` | `NOT NULL` | Topology version number |
| `TOPOLOGY_STATE` | `VARCHAR2(8)` |  | Possible values:  - `ACTIVE`: Topology can be used for RMF operations - `INACTIVE`: Topology cannot be used for RMF operations |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for information about configuring the Remote Management Framework (RMF) architecture
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UMF_LINK.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.75 DBA\_UMF\_LINK

`DBA_UMF_LINK` displays information about the registered database links in the Remote Management Framework (RMF).

This view returns no rows if you are querying on an RMF source node. It returns all the registered database links in the topology if you are querying on a target node.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TOPOLOGY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Topology name for the link |
| `FROM_NODE_ID` | `NUMBER` | `NOT NULL` | Node ID of the local node |
| `TO_NODE_ID` | `NUMBER` | `NOT NULL` | Node ID of the remote node |
| `LINK_NAME` | `VARCHAR2(128)` | `NOT NULL` | Fully qualified database link name |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for information about configuring the Remote Management Framework (RMF) architecture
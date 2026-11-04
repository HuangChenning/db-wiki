---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_UMF_LINK.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_UMF_LINK` displays information about the registered database links in the Remote Management Framework (RMF).

This view returns no rows if you are querying on an RMF source node. It returns all the registered database links in the topology if you are querying on a target node.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TOPOLOGY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Topology name for the link |
| `FROM_NODE_ID` | `NUMBER` | `NOT NULL` | Node ID of the local node |
| `TO_NODE_ID` | `NUMBER` | `NOT NULL` | Node ID of the remote node |
| `LINK_NAME` | `VARCHAR2(128)` | `NOT NULL` | Fully qualified database link name |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for information about configuring the Remote Management Framework (RMF) architecture
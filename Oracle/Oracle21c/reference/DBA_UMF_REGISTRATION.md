---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UMF_REGISTRATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.76 DBA\_UMF\_REGISTRATION

`DBA_UMF_REGISTRATION` displays information about the registered nodes in the Remote Management Framework (RMF).

This view returns no rows if you are querying on an RMF source node. It returns all the registered nodes in the topology if you are querying on a target node.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TOPOLOGY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Topology name for the node |
| `NODE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Unique node name in the topology |
| `NODE_ID` | `NUMBER` | `NOT NULL` | Unique node ID in the topology |
| `NODE_TYPE` | `NUMBER` | `NOT NULL` | Node type. Possible value:  - `0`: RDBMS node |
| `AS_SOURCE` | `VARCHAR2(5)` |  | Indicates whether the node is a source node. Possible values:  - `TRUE`: The node is a source node, and it can provide remote services - `FALSE`: The node is not a source node, and it cannot provide remote services |
| `AS_CANDIDATE_TARGET` | `VARCHAR2(5)` |  | Node is a candidate target. Possible values:  - `TRUE`: Node can be promoted to target role - `FALSE`: Node cannot be promoted to target role |
| `STATE` | `VARCHAR2(20)` |  | Current state of the node. Possible values:  - `OK`: Node is registered - `REGISTRATION_PENDING`: Node registration has started, but has not been completed - `SYNC_FAILED`: Unable to synchronize the topology with the node |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for information about configuring the Remote Management Framework (RMF) architecture
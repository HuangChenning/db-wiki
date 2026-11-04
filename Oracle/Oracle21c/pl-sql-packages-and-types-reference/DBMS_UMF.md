---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_UMF.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 191 DBMS\_UMF

The `DBMS_UMF` package provides an interface for deploying the Remote Management Framework (RMF) for an Oracle Database. The RMF is used for collecting performance statistics for an Oracle Database.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=TGDBA-GUID-E1369092-DA6B-4CF4-B286-69D4A3BDFA1E) for more information about configuring the RMF for an Oracle Database.

This chapter contains the following topic:

- Summary of DBMS\_UMF Subprograms

### 191.1 Summary of DBMS\_UMF Subprograms

This topic lists the `DBMS_UMF` subprograms in alphabetical order and briefly describes them.

Table 191-1 DBMS\_UMF Package Subprograms

| Subprogram | Description |
| --- | --- |
| CONFIGURE\_NODE Procedure | Configures a node in the RMF topology |
| CREATE\_LINK Procedure | Creates a database link between two nodes in the RMF topology |
| CREATE\_TOPOLOGY Procedure | Creates the RMF topology |
| DROP\_LINK Procedure | Removes a database link between two nodes in the RMF topology |
| DROP\_TOPOLOGY Procedure | Deletes the RMF topology |
| ENABLE\_SERVICE Procedure | Enables a service on a node in the RMF topology |
| GET\_NODE\_ID\_LOCAL Function | Returns the node ID of a node in the RMF topology |
| GET\_NODE\_NAME\_LOCAL Function | Returns the node name of a node in the RMF topology |
| GET\_TARGET\_ID Function | Returns the destination ID in the RMF topology |
| GET\_TOPOLOGY\_NAME\_LOCAL Function | Returns the RMF topology name of the local node |
| QUERY\_LINK\_INFO Procedure | Returns the information about a database link in the RMF topology |
| QUERY\_NODE\_INFO Procedures | Returns the information about a node in the RMF topology |
| REGISTER\_NODE Function and Procedure | Registers a node in the RMF topology |
| SWITCH\_DESTINATION Procedure | Designates a source node as a destination node in the RMF topology |
| UNCONFIGURE\_NODE Procedure | Resets the configuration of a node in the RMF topology |
| UNREGISTER\_NODE Procedure | Removes the registration of a node in the RMF topology |

#### 191.1.1 CONFIGURE\_NODE Procedure

This procedure configures a node that needs to be registered with the RMF topology. This procedure must be executed on the node that needs to be configured.

Syntax

```
DBMS_UMF.CONFIGURE_NODE(
   node_name          IN VARCHAR2 DEFAULT NULL,
   dblink_to_target   IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 191-2 CONFIGURE\_NODE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `node_name` | Name of the node.  Each node in the RMF topology must be assigned a unique name. If a name is not provided for a node in this procedure, then the value of the initialization parameter `DB_UNIQUE_NAME` is assigned as the name for the node by default. |
| `dblink_to_target` | Database link from this node to the destination node. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.2 CREATE\_LINK Procedure

This procedure creates database links between two nodes in the RMF topology. This procedure must be executed only on the destination node.

Syntax

```
DBMS_UMF.CREATE_LINK(
   topology_name      IN VARCHAR2,
   node_a_name        IN VARCHAR2,
   node_b_name        IN VARCHAR2,
   dblink_a_to_b      IN VARCHAR2,
   dblink_b_to_a      IN VARCHAR2);
```

Parameters

Table 191-3 CREATE\_LINK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `node_a_name` | Name of the first node. |
| `node_b_name` | Name of the second node. |
| `dblink_a_to_b` | Database link from the first node to the second node. |
| `dblink_b_to_b` | Database link from the second node to the first node. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.3 CREATE\_TOPOLOGY Procedure

This procedure creates the RMF topology and designates the node on which it is executed as the destination node for that topology.

Syntax

```
DBMS_UMF.CREATE_TOPOLOGY(
   topology_name IN VARCHAR2);
```

Parameters

Table 191-4 CREATE\_TOPOLOGY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.4 DROP\_LINK Procedure

This procedure removes the database links between two nodes in the RMF topology. This procedure must be executed only on the destination node.

Syntax

```
DBMS_UMF.DROP_LINK(
   topology_name  IN VARCHAR2,
   node_a_name    IN VARCHAR2,
   node_b_name    IN VARCHAR2);
```

Parameters

Table 191-5 DROP\_LINK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `node_a_name` | Name of the first node. |
| `node_b_name` | Name of the second node. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.5 DROP\_TOPOLOGY Procedure

This procedure deletes the RMF topology. This procedure must be executed only on the destination node.

Syntax

```
DBMS_UMF.DROP_TOPOLOGY(
   topology_name IN VARCHAR2);
```

Parameters

Table 191-6 DROP\_TOPOLOGY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the topology to delete. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.6 ENABLE\_SERVICE Procedure

This procedure enables a service, such as the AWR service, on a node in the RMF topology. This procedure must be executed only on the destination node.

Syntax

```
DBMS_UMF.ENABLE_SERVICE(
   topology_name      IN VARCHAR2,
   node_name          IN VARCHAR2,
   service_type       IN NUMBER);
```

Parameters

Table 191-7 ENABLE\_SERVICE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `node_name` | Name of the node on which a specific service needs to be enabled. |
| `service_type` | Numeric constant identifying the service. The only allowed value for this parameter is `UMF_SERVICE_TYPE_AWR`, which is Automatic Workload Repository (AWR) service. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.7 GET\_NODE\_ID\_LOCAL Function

This function returns the node ID of the node in the RMF topology on which this function is executed.

Syntax

```
DBMS_UMF.GET_NODE_ID_LOCAL(
   topology_name  IN  VARCHAR2 DEFAULT NULL)
 RETURN NUMBER;
```

Parameters

Table 191-8 GET\_NODE\_ID\_LOCAL Function Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology with which the node is registered. |

Return Value

Returns the node ID of the node in the RMF topology on which this function is executed.

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this function.

#### 191.1.8 GET\_NODE\_NAME\_LOCAL Function

This function returns the name of the node in the RMF topology on which this function is executed.

Syntax

```
DBMS_UMF.GET_NODE_NAME_LOCAL RETURN VARCHAR2;
```

Return Value

Returns the name of the node in the RMF topology on which this function is executed.

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.9 GET\_TARGET\_ID Function

This function returns the ID of the destination node in the RMF topology. This function can be executed on any node in the RMF topology.

Syntax

```
DBMS_UMF.GET_TARGET_ID(
   topology_name  IN  VARCHAR2)
 RETURN NUMBER;
```

Parameters

Table 191-9 GET\_TARGET\_ID Function Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |

Return Value

Returns the ID of the destination node in the RMF topology.

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.10 GET\_TOPOLOGY\_NAME\_LOCAL Function

This function returns the name of the active RMF topology of the node on which this function is executed.

Syntax

```
DBMS_UMF.GET_TOPOLOGY_NAME_LOCAL RETURN VARCHAR2;
```

Return Value

Returns the name of the active RMF topology of the node on which this function is executed.

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.11 QUERY\_LINK\_INFO Procedure

This procedure returns the name of the database link between two nodes in the RMF topology. This procedure can be executed on any node in the RMF topology.

Syntax

```
DBMS_UMF.QUERY_LINK_INFO(
   topology_name      IN   VARCHAR2,
   from_node_id       IN   NUMBER,
   to_node_id         IN   NUMBER,
   link_name          OUT  VARCHAR2);
```

Parameters

Table 191-10 QUERY\_LINK\_INFO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `from_node_id` | Node ID of the first node. |
| `to_node_id` | Node ID of the second node. |
| `link_name` | Name of the database link from the first node to the second node returned by the procedure. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.12 QUERY\_NODE\_INFO Procedures

This procedure returns information about a node in the RMF topology. This procedure can be executed on any node in the RMF topology.

Syntax

```
DBMS_UMF.QUERY_NODE_INFO(
   topology_name      IN    VARCHAR2  DEFAULT NULL,
   node_name          IN    VARCHAR2,
   node_id            OUT   NUMBER);

DBMS_UMF.QUERY_NODE_INFO(
   node_id            IN    NUMBER,
   topology_name      OUT   VARCHAR2,
   node_name          OUT   VARCHAR2);
```

Parameters

Table 191-11 QUERY\_NODE\_INFO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology with which the node is registered. |
| `node_name` | Name of the node. |
| `node_id` | Identifier of the node. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.13 REGISTER\_NODE Function and Procedure

This function and procedure registers a node with the RMF topology. This procedure and function must be executed only on the destination node in the RMF topology.

Syntax

```
DBMS_UMF.REGISTER_NODE(
   topology_name          IN  VARCHAR2,
   node_name              IN  VARCHAR2,
   dblink_to_node         IN  VARCHAR2 DEFAULT NULL,
   dblink_from_node       IN  VARCHAR2 DEFAULT NULL,
   as_source              IN  VARCHAR2 DEFAULT 'TRUE',
   as_candidate_target    IN  VARCHAR2 DEFAULT 'FALSE');

DBMS_UMF.REGISTER_NODE(
   topology_name          IN  VARCHAR2,
   node_name              IN  VARCHAR2,
   dblink_to_node         IN  VARCHAR2 DEFAULT NULL,
   dblink_from_node       IN  VARCHAR2 DEFAULT NULL,
   as_source              IN  VARCHAR2 DEFAULT 'TRUE',
   as_candidate_target    IN  VARCHAR2 DEFAULT 'FALSE');
   node_id                OUT VARCHAR2);

DBMS_UMF.REGISTER_NODE(
   topology_name          IN  VARCHAR2,
   node_name              IN  VARCHAR2,
   dblink_to_node         IN  VARCHAR2 DEFAULT NULL,
   dblink_from_node       IN  VARCHAR2 DEFAULT NULL,
   as_source              IN  VARCHAR2 DEFAULT 'TRUE',
   as_candidate_target    IN  VARCHAR2 DEFAULT 'FALSE')
 RETURN NUMBER;
```

Parameters

Table 191-12 REGISTER\_NODE Function and Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `node_name` | Name of the node to register. |
| `dblink_to_node` | Name for the database link from the destination to the node. |
| `dblink_from_node` | Name for the database link from the node to the destination. |
| `as_source` | Set to `TRUE`, if the node is a source, else set to `FALSE`. |
| `as_candidate_target` | Set to `TRUE`, if the node is a candidate destination, else set to `FALSE`. |
| `node_id` | Node ID returned by the procedure. |

Return Value

Returns the node ID of the registered node.

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.14 SWITCH\_DESTINATION Procedure

This procedure makes the candidate destination as the new destination in the RMF topology. This procedure must be executed only on the candidate destination node.

Syntax

```
DBMS_UMF.SWITCH_DESTINATION(
   topology_name      IN VARCHAR2,
   force_switch       IN BOOLEAN DEFAULT TRUE);
```

Parameters

Table 191-13 SWITCH\_DESTINATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `force_switch` | If set to `FALSE`, the execution of this procedure fails in the following situations:  - Candidate destination is a read-only database, and hence it cannot become the new destination. - Candidate destination does not have database links to one or more sources in the topology. - Candidate destination is unable to get the latest AWR data from the old destination.  If set to `TRUE`, the execution of this procedure fails in the following situation:  - Candidate destination is a read-only database, and hence it cannot become the new destination. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.15 UNCONFIGURE\_NODE Procedure

This procedure removes the configuration details of the node on which this procedure is executed.

Syntax

```
DBMS_UMF.UNCONFIGURE_NODE;
```

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.

#### 191.1.16 UNREGISTER\_NODE Procedure

This procedure removes a node for the RMF topology. This procedure must be executed only on the destination node.

Syntax

```
DBMS_UMF.UNREGISTER_NODE(
   topology_name    IN VARCHAR2,
   node_name        IN VARCHAR2);
```

Parameters

Table 191-14 UNREGISTER\_NODE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `topology_name` | Name of the RMF topology. |
| `node_name` | Name of the node which needs to be removed from the topology. |

Security Model

Only the database users `SYS` and `SYS$UMF` can execute this procedure.
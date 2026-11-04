---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESOURCE_LIMIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.168 V$RESOURCE\_LIMIT

`V$RESOURCE_LIMIT` displays information about global resource use for some of the system resources. Use this view to monitor the consumption of resources so that you can take corrective action, if necessary. Many of the resources correspond to initialization parameters listed in Table 9-5.

Some resources, those used by DLM for example, have an initial allocation (soft limit), and the hard limit, which is theoretically infinite (although in practice it is limited by SGA size). During SGA reservation/initialization, a place is reserved in SGA for the `INITIAL_ALLOCATION` of resources, but if this allocation is exceeded, additional resources are allocated up to the value indicated by `LIMIT_VALUE`. The `CURRENT_UTILIZATION` column indicates whether the initial allocation has been exceeded. When the initial allocation value is exceeded, the additional required resources are allocated from the shared pool, where they must compete for space with other resources.

A good choice for the value of `INITIAL_ALLOCATION` will avoid the contention for space. For most resources, the value for `INITIAL_ALLOCATION` is the same as the `LIMIT_VALUE`. Exceeding `LIMIT_VALUE` results in an error.

| Column | Datatype | Description |
| --- | --- | --- |
| `RESOURCE_NAME` | `VARCHAR2(128)` | Name of the resource (see Table 9-5) |
| `CURRENT_UTILIZATION` | `NUMBER` | Number of (resources, locks, or processes) currently being used |
| `MAX_UTILIZATION` | `NUMBER` | Maximum consumption of this resource since the last instance start-up |
| `INITIAL_ALLOCATION` | `VARCHAR2(40)` | Initial allocation. This will be equal to the value specified for the resource in the initialization parameter file (`UNLIMITED` for infinite allocation). |
| `LIMIT_VALUE` | `VARCHAR2(40)` | Unlimited for resources and locks. This can be greater than the initial allocation value (`UNLIMITED` for infinite limit). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 9-5 Values for the RESOURCE\_NAME Column

| Resource Name | Corresponds to |
| --- | --- |
| `DML_LOCKS` | See " [DML\_LOCKS](DML_LOCKS.md) " |
| `ENQUEUE_LOCKS` | This value is computed by the Oracle Database. See [V$ENQUEUE\_LOCK](V-ENQUEUE_LOCK.md) to obtain more information about the enqueue locks. |
| `GES_LOCKS` | Global Enqueue Service locks |
| `GES_PROCS` | Global Enqueue Service processes |
| `GES_RESS` | Global Enqueue Service resources |
| `MAX_SHARED_SERVERS` | See " [MAX\_SHARED\_SERVERS](MAX_SHARED_SERVERS.md) " |
| `PARALLEL_MAX_SERVERS` | See " [PARALLEL\_MAX\_SERVERS](PARALLEL_MAX_SERVERS.md) " |
| `PROCESSES` | See " [PROCESSES](PROCESSES.md) " |
| `SESSIONS` | See " [SESSIONS](SESSIONS.md) " |
| `SORT_SEGMENT_LOCKS` | This value is computed by the Oracle Database |
| `TEMPORARY_LOCKS` | This value is computed by the Oracle Database |
| `TRANSACTIONS` | See " [TRANSACTIONS](TRANSACTIONS.md) " |
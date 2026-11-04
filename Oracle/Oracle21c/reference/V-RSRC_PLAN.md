---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_PLAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.194 V$RSRC\_PLAN

`V$RSRC_PLAN` displays the names of all currently active resource plans.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Resource plan ID (a unique number, consistent across database shutdowns and startups). This is also the data dictionary object ID. |
| `NAME` | `VARCHAR2(32)` | Name of the resource plan |
| `IS_TOP_PLAN` | `VARCHAR2(5)` | Indicates whether the resource plan is the current top plan (`TRUE`) or whether the resource plan is a subplan of the current top plan (`FALSE`) |
| `CPU_MANAGED` | `VARCHAR2(3)` | Indicates whether the resource plan has parameters that specify a policy for how the Resource Manager should schedule sessions to manage CPU usage (`ON`) or whether Resource Manager is not managing CPU usage (`OFF`) |
| `CPU_SCOPE` | `VARCHAR2(13)` | Reserved for future use |
| `INSTANCE_CAGING` | `VARCHAR2(3)` | Indicates whether instance caging is enabled (`ON`) or disabled (`OFF`). Instance caging is enabled if the `CPU_COUNT` initialization parameter is explicitly modified to a value other than `0` and Resource Manager is enabled. |
| `PARALLEL_SERVERS_ACTIVE` | `NUMBER` | Total number of active parallel servers on the instance |
| `PARALLEL_SERVERS_TOTAL` | `NUMBER` | The value of `PARALLEL_SERVERS_TARGET` for the instance. Parallel statements are queued if the total number of active parallel servers exceeds this value. |
| `PARALLEL_EXECUTION_MANAGED` | `VARCHAR2(32)` | State of parallel statement queuing:  - `OFF` - Parallel statement queuing is disabled - `STARTUP` - Parallel statement queuing is enabled. This is a temporary state that can occur when an Oracle RAC database is undergoing configuration changes - `FIFO` - Parallel statement queuing is enabled. All parallel statements are managed in a single Oracle RAC FIFO queue - `FULL` - Parallel statement queuing is enabled. All parallel statements are managed in per-consumer group queues according to the current resource plan. This state is used when a resource plan that contains resource allocation directives (`MGMT_P*`) is enabled. - `DISABLED` - Parallel statement queuing is disabled. This state can occur when memory is unavailable for use by parallel statement queuing in the System Global Area (SGA). Restart the Oracle instance to re-enable parallel statement queuing.  For an Oracle RAC database, only the instance running as primary Database Resource Manager (DBRM) shows the correct state of parallel statement queuing. All other instances default to the value `FULL`. A single instance database always shows the correct value for this field. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `DIRECTIVE_TYPE` | `VARCHAR2(32)` | The type of directive used by this PDB:  - `DEFAULT_DIRECTIVE`: The default plan directive - `PDB`: A PDB directive - `PROFILE`: A profile directive |
| `SHARES` | `NUMBER` | Resource allocation for this PDB, expressed in shares |
| `UTILIZATION_LIMIT` | `NUMBER` | Maximum percentage of the container's resources allowed for this PDB |
| `PARALLEL_SERVER_LIMIT` | `NUMBER` | Maximum percentage of the parallel target the PDB can use before queuing subsequent parallel queries |
| `MEMORY_MIN` | `NUMBER` | The percentage of Exadata Smart Flash Cache and Exadata PMEM cache that is guaranteed to the PDB  This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache.  See [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SAGUG-GUID-ED342736-2423-4B58-B2F7-5CA833BC863E) for more information. |
| `MEMORY_LIMIT` | `NUMBER` | The maximum percentage of Exadata Smart Flash Cache and Exadata PMEM cache that the PDB can use  This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache.  See [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SAGUG-GUID-ED342736-2423-4B58-B2F7-5CA833BC863E) for more information. |
| `PROFILE` | `VARCHAR2(32)` | The value of the `DB_PERFORMANCE_PROFILE` initialization parameter for this PDB |
| `CPU_COUNT` | `NUMBER` | Value of the `CPU_COUNT` initialization parameter in the container to which the data pertains |
| `CPU_MIN_COUNT` | `NUMBER` | Value of the `CPU_MIN_COUNT` initialization parameter in the container to which the data pertains |

The resource plan with `CON_ID=ROOT` is the CDB resource plan.

See Also:

- " [DBA\_RSRC\_PLANS](DBA_RSRC_PLANS.md) " for a listing of all plans in the database
- " [DBA\_CDB\_RSRC\_PLANS](DBA_CDB_RSRC_PLANS.md) " for information about CDB resource plans
- " [DBA\_CDB\_RSRC\_PLAN\_DIRECTIVES](DBA_CDB_RSRC_PLAN_DIRECTIVES.md) " for information about CDB resource plan directives
- " [DB\_PERFORMANCE\_PROFILE](DB_PERFORMANCE_PROFILE.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11881) for information on resource plans
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS050) for information on defining resource allocation methods for consumer groups with the `DBMS_RESOURCE_MANAGER` package
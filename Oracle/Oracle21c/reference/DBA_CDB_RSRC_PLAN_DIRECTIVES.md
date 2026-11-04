---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_CDB_RSRC_PLAN_DIRECTIVES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.217 DBA\_CDB\_RSRC\_PLAN\_DIRECTIVES

`DBA_CDB_RSRC_PLAN_DIRECTIVES` provides information about all the CDB resource plan directives.

Note:

`ORA$DEFAULT_PDB_DIRECTIVE` is the default directive for PDBs. For more information about `ORA$DEFAULT_PDB_DIRECTIVE`, see [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13835).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN` | `VARCHAR2(128)` |  | Name of the CDB resource plan to which this directive belongs |
| `PLUGGABLE_DATABASE` | `VARCHAR2(128)` |  | Name of the PDB referred to. NULL for profile directives |
| `PROFILE` | `VARCHAR2(128)` |  | For internal use only |
| `DIRECTIVE_TYPE` | `VARCHAR2(30)` |  | For internal use only |
| `SHARES` | `NUMBER` |  | Resource allocation, expressed in shares |
| `UTILIZATION_LIMIT` | `NUMBER` |  | Maximum resource utilization allowed, expressed in percentage |
| `PARALLEL_SERVER_LIMIT` | `NUMBER` |  | Maximum percentage of the parallel target used before queueing subsequent parallel queries |
| `MEMORY_MIN` | `NUMBER` |  | The percentage of Exadata Smart Flash Cache and Exadata PMEM cache that is guaranteed to the PDB  This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache.  See [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SAGUG-GUID-ED342736-2423-4B58-B2F7-5CA833BC863E) for more information. |
| `MEMORY_LIMIT` | `NUMBER` |  | The maximum percentage of Exadata Smart Flash Cache and Exadata PMEM cache that the PDB can use  This percentage is based on the total amount of space allocated to the CDB for Exadata Smart Flash Cache and Exadata PMEM cache.  See [Oracle Exadata System Software User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SAGUG-GUID-ED342736-2423-4B58-B2F7-5CA833BC863E) for more information. |
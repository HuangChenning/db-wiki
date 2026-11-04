---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MAX_DATAPUMP_JOBS_PER_PDB.html
tags:
  - oracle
  - 12c
  - reference
---

`MAX_DATAPUMP_JOBS_PER_PDB` determines the maximum number of concurrent Oracle Data Pump jobs per PDB.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 100 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `2147483647` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The default value will not work for all databases. Database administrators will have to determine if the default value works well for their database.

A value that is too large could cause Oracle Data Pump to consume too many system resources, while a value that is too small could prevent users from performing their Oracle Data Pump tasks.

The main resource Oracle Data Pump uses is shared pool in the System Global Area (SGA) for the database. Parallel jobs increase the number of sessions and, depending on the job, the number of PQ slaves used.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SUTIL-GUID-45B17B65-20F2-4128-9A39-B1B0F5E323BB) for more information about using Oracle Data Pump with CDBs
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS-GUID-AEA7ED80-DB4A-4A70-B199-592287206348) for more information about the `DBMS_DATAPUMP` PL/SQL package
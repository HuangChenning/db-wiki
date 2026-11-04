---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_DATAPUMP_JOBS_PER_PDB.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.200 MAX\_DATAPUMP\_JOBS\_PER\_PDB

`MAX_DATAPUMP_JOBS_PER_PDB` determines the maximum number of concurrent Oracle Data Pump jobs per PDB.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MAX_DATAPUMP_JOBS_PER_PDB = { AUTO \| integer }` |
| Default value | 100 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `250` or `AUTO` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The default value will not work for all databases. Database administrators will have to determine if the default value works well for their database.

When this parameter has a value of `AUTO`, Oracle Data Pump will derive its actual value to be 50% of the `SESSIONS` initialization parameter.

A value that is too large could cause Oracle Data Pump to consume too many system resources, while a value that is too small could prevent users from performing their Oracle Data Pump tasks.

The main resource Oracle Data Pump uses is shared pool in the System Global Area (SGA) for the database. Parallel jobs increase the number of sessions and, depending on the job, the number of PX servers used.

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SUTIL-GUID-45B17B65-20F2-4128-9A39-B1B0F5E323BB) for more information about using Oracle Data Pump with CDBs
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-AEA7ED80-DB4A-4A70-B199-592287206348) for more information about the `DBMS_DATAPUMP` PL/SQL package
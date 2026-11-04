---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_USE_SQL_QUARANTINE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.260 OPTIMIZER\_USE\_SQL\_QUARANTINE

`OPTIMIZER_USE_SQL_QUARANTINE` determines whether the optimizer considers SQL Quarantine configurations when choosing an execution plan for a SQL statement.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Values:

- `true`
	The optimizer considers SQL Quarantine configurations when choosing an execution plan for a SQL statement. The statement will be terminated if it would otherwise use a quarantined execution plan.
- `false`
	The optimizer ignores SQL Quarantine configurations when choosing an execution plan for a SQL statement. It may use any execution plan, regardless of its quarantine status.

See Also:

- " [DBA\_SQL\_QUARANTINE](DBA_SQL_QUARANTINE.md) "
- " [OPTIMIZER\_CAPTURE\_SQL\_QUARANTINE](OPTIMIZER_CAPTURE_SQL_QUARANTINE.md) "
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL-GUID-E76CD42A-3D1B-4A0A-82F6-5270D3B32E7A) for more information about SQL Quarantine
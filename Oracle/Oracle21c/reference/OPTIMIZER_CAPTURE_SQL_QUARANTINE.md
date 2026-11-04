---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_CAPTURE_SQL_QUARANTINE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.244 OPTIMIZER\_CAPTURE\_SQL\_QUARANTINE

`OPTIMIZER_CAPTURE_SQL_QUARANTINE` enables or disables the automatic creation of SQL Quarantine configurations.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Values:

- `true`
	Enables the automatic creation of SQL Quarantine configurations. If the Resource Manager terminates a SQL statement because the statement has exceeded resource limits, then the database automatically creates a SQL Quarantine configuration for the execution plan used by the terminated SQL statement. Note that the plan for a terminated SQL statement is quarantined, not the statement itself.
- `false`
	Disables the automatic creation of SQL Quarantine configurations.

See Also:

- " [DBA\_SQL\_QUARANTINE](DBA_SQL_QUARANTINE.md) "
- " [OPTIMIZER\_USE\_SQL\_QUARANTINE](OPTIMIZER_USE_SQL_QUARANTINE.md) "
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL-GUID-E76CD42A-3D1B-4A0A-82F6-5270D3B32E7A) for more information about SQL Quarantine
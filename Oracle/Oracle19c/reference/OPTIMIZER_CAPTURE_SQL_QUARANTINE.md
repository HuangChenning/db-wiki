---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/OPTIMIZER_CAPTURE_SQL_QUARANTINE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.248 OPTIMIZER\_CAPTURE\_SQL\_QUARANTINE

`OPTIMIZER_CAPTURE_SQL_QUARANTINE` enables or disables the automatic creation of SQL Quarantine configurations.

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
	Enables the automatic creation of SQL Quarantine configurations. If the Resource Manager terminates a SQL statement because the statement has exceeded resource limits, then the database automatically creates a SQL Quarantine configuration for the execution plan used by the terminated SQL statement. Note that the plan for a terminated SQL statement is quarantined, not the statement itself.
- `false`
	Disables the automatic creation of SQL Quarantine configurations.

Note:

This parameter is available on Oracle Autonomous Database starting with Oracle Database 19c. It is available on other types of Oracle databases starting with Oracle Database 19c, Release Update 19.27.

See Also:

- " [DBA\_SQL\_QUARANTINE](DBA_SQL_QUARANTINE.md) "
- " [OPTIMIZER\_USE\_SQL\_QUARANTINE](OPTIMIZER_USE_SQL_QUARANTINE.md) "
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=TGSQL-GUID-E76CD42A-3D1B-4A0A-82F6-5270D3B32E7A) for more information about SQL Quarantine
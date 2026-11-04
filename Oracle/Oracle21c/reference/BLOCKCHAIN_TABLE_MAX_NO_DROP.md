---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/BLOCKCHAIN_TABLE_MAX_NO_DROP.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.36 BLOCKCHAIN\_TABLE\_MAX\_NO\_DROP

`BLOCKCHAIN_TABLE_MAX_NO_DROP` lets you control the maximum amount of idle time that can be specified when creating a blockchain table or an immutable table. The idle time represents the length of time the table must be inactive before it can be dropped. When explicitly set by a user, the only value allowed for this parameter is `0`.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | None |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | None or `0` |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

When creating a blockchain table or an immutable table with the SQL statement `CREATE` `TABLE`, you can specify the clause `NO` `DROP` `UNTIL` `number` `DAYS` `IDLE`. This clause specifies the number of days the table must be inactive before it can be dropped, that is, the number of days that must pass after the most recent row insertion before the table can be dropped.

- If `BLOCKCHAIN_TABLE_MAX_NO_DROP` is set to `0`, then when a user creates a blockchain table or an immutable table, and specifies the `NO` `DROP` `UNTIL` `number` `DAYS` `IDLE` clause, the value of `number` must be `0`:
	```
	CREATE BLOCKCHAIN TABLE ... NO DROP UNTIL 0 DAYS IDLE ...
	CREATE IMMUTABLE TABLE ... NO DROP UNTIL 0 DAYS IDLE ...
	```
	This allows the table to be dropped at any time, regardless of how long the table has been inactive.
- If `BLOCKCHAIN_TABLE_MAX_NO_DROP` is not set, then when a user creates a blockchain table or an immutable table, and specifies the `NO` `DROP` `UNTIL` `number` `DAYS` `IDLE` clause, any number value can be specified for `number`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6) for information about the `CREATE` `TABLE` statement
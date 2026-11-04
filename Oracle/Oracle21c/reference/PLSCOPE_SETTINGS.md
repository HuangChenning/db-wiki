---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PLSCOPE_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.284 PLSCOPE\_SETTINGS

`PLSCOPE_SETTINGS` controls the compile time collection, cross-reference, and storage of PL/SQL source code identifier data.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PLSCOPE_SETTINGS = ‘value_clause [, value_clause ]’`  value\_clause::=  `{ IDENTIFIERS \| STATEMENTS } : { ALL \| NONE \| PUBLIC (for IDENTIFIERS only) \| SQL (for IDENTIFIERS only) \| PLSQL (for IDENTIFIERS only) }` |
| Default value | `‘IDENTIFIERS:NONE’` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `IDENTIFIERS:ALL`
	Enables the collection of all source code identifier data.
- `IDENTIFIERS:NONE`
	Disables the collection of all source code identifier data.
- `IDENTIFIERS: PUBLIC`
	Enables the collection of all PUBLIC user identifier data (except for `DEFINITION`)
- `IDENTIFIERS:SQL`
	Enables the collection of all SQL identifier data.
- `IDENTIFIERS:PLSQL`
	Enables the collection of all PLSQL identifier data.
- `STATEMENTS:ALL`
	Enables the collection of all SQL statements used in PL/SQL.
- `STATEMENTS:NONE`
	Disables the collection of all statements.

`PLSCOPE_SETTINGS` can be set on a session, system, or per-library unit (`ALTER COMPILE`) basis. The current setting of `PLSCOPE_SETTINGS` for any library unit can be attained by querying the `*_PLSQL_OBJECT_SETTINGS` views. Any identifier data collected by setting this parameter can be accessed using the `*_IDENTIFIERS` views.

When a `STATEMENTS` setting is not specified, and `IDENTIFIERS` is specified but set to a value other than `NONE`, `STATEMENTS` defaults to a setting of `ALL`, which is equal to:
```
IDENTIFIERS: [ALL|PLSQL|PLSQL|PUBLIC]
```

Examples

The following parameter setting causes PL/SQL and SQL identifiers and statements to be collected:

```
PLSCOPE_SETTINGS = 'IDENTIFIERS:ALL, STATEMENTS:ALL'
```

The following parameter setting causes only SQL identifiers and statements to be collected:

```
PLSCOPE_SETTINGS = 'IDENTIFIERS:SQL, STATEMENTS:ALL'
```

The following parameter setting causes only PL/SQL identifiers to be collected:

```
PLSCOPE_SETTINGS = 'IDENTIFIERS:PLSQL, STATEMENTS:NONE'
```

The following parameter setting causes no identifier data to be collected, and drops any existing identifier data:

```
PLSCOPE_SETTINGS = 'IDENTIFIERS: NONE'
```
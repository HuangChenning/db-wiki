---
title: PLSQL_WARNINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams200.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PLSQL_WARNINGS = '` `value_clause` `' [, '` `value_clause` `' ] ...` |
|  | value\_clause::=  `{ ENABLE \| DISABLE \| ERROR }:`  `{ ALL`  `\| SEVERE`  `\| INFORMATIONAL`  `\| PERFORMANCE`  `\| {` `integer`  `\| (``integer` `[,` `integer` `] ...)`  `}`  `}` |
| Default value | `'DISABLE:ALL'` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Examples | ``` PLSQL_WARNINGS = 'ENABLE:SEVERE', 'DISABLE:INFORMATIONAL'; PLSQL_WARNINGS = 'DISABLE:ALL'; PLSQL_WARNINGS = 'DISABLE:5000', 'ENABLE:5001', 'ERROR:5002'; PLSQL_WARNINGS = 'ENABLE:(5000,5001,5002)', 'DISABLE:(6000,6001)'; ``` |

`PLSQL_WARNINGS` enables or disables the reporting of warning messages by the PL/SQL compiler, and specifies which warning messages to show as errors.

value\_clause

Multiple value clauses may be specified, enclosed in quotes and separated by commas. Each value clause is composed of a qualifier, a colon (`:`), and a modifier.

Qualifier values:

- `ENABLE`
	Enable a specific warning or a set of warnings
- `DISABLE`
	Disable a specific warning or a set of warnings
- `ERROR`
	Treat a specific warning or a set of warnings as errors

Modifier values:

- `ALL`
	Apply the qualifier to all warning messages
- `SEVERE`
	Apply the qualifier to only those warning messages in the `SEVERE` category
- `INFORMATIONAL`
	Apply the qualifier to only those warning messages in the `INFORMATIONAL` category
- `PERFORMANCE`
	Apply the qualifier to only those warning messages in the `PERFORMANCE` category
---
title: NLS_LENGTH_SEMANTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams152.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_LENGTH_SEMANTICS =` `string`  Example: `NLS_LENGTH_SEMANTICS = 'CHAR'` |
| Default value | `BYTE` |
| Modifiable | `ALTER SESSION` |
| Range of values | `BYTE \| CHAR` |

The session-level value of `NLS_LENGTH_SEMANTICS` specifies the default length semantics to use for `VARCHAR2` and `CHAR` table columns, user-defined object attributes, and PL/SQL variables in database objects created in the session. This default may be overridden by the explicit length semantics qualifiers `BYTE` and `CHAR` in column, attribute, and variable definitions.

The instance-level value of `NLS_LENGTH_SEMANTICS` provides a default for the session-level value if `NLS_LENGTH_SEMANTICS` it is not set explicitly by the database client through the `NLS_LENGTH_SEMANTICS` client environment variable (does not apply to JDBC Thin clients), or the `ALTER` `SESSION` `SET` `NLS_LENGTH_SEMANTICS` statement.

`NCHAR`, `NVARCHAR2`, `CLOB`, and `NCLOB` columns are always character-based.

Sessions logged in as `SYS` do not use the `NLS_LENGTH_SEMANTICS` parameter. They use `BYTE` length semantics for all created objects unless overridden by the explicit `BYTE` and `CHAR` qualifiers in object definitions (SQL DDL statements).

Caution:

Oracle strongly recommends that you do NOT set the `NLS_LENGTH_SEMANTICS` parameter to `CHAR` in the instance or server parameter file. This may cause many existing installation scripts to unexpectedly create columns with character length semantics, resulting in runtime errors, including buffer overflows.
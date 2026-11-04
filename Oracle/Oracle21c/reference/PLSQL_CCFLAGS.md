---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PLSQL_CCFLAGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.285 PLSQL\_CCFLAGS

`PLSQL_CCFLAGS` provides a mechanism that allows PL/SQL programmers to control conditional compilation of each PL/SQL library unit independently.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | PLSQL\_CCFLAGS = '< `v1` >:< `c1` >,< `v2` >:< `c2` >,...,< `vn` >:< `cn` >' |
| Default value | Empty string |
| Modifiable | `ALTER SESSION,` `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Any string literal that satisfies the internal syntax |
| Basic | No |
| Examples | `ALTER SESSION SET PLSQL_CCFLAGS = 'DeBug:TruE';`  `ALTER SESSION SET PLSQL_CCFLAGS = 'debug:TRUE';` |

Values

- < `vi` > has the form of an unquoted PL/SQL identifier. It is unrestricted and can be a reserved word or a keyword. The text is insensitive to case. Each one is known as a flag or flag name. Each < `vi` > can occur more than once in the string, each occurrence can have a different flag value, and the flag values can be of different kinds.
- < `ci` > is one of the following: a PL/SQL boolean literal, a `PLS_INTEGER` literal, or the literal NULL. The text is insensitive to case. Each one is known as a flag value and corresponds to a flag name.

You can define any allowable value for `PLSQL_CCFLAGS`. However, Oracle recommends that this parameter be used for controlling the conditional compilation of debugging or tracing code. It is recommended that the following identifiers not be used as flag name values:

- Names of Oracle parameters (for example, `NLS_LENGTH_SEMANTICS`)
- Identifiers with any of the following prefixes: `PLS_`, `PLSQL_`, `PLSCC_`, `ORA_`, `ORACLE_`, `DBMS_`, `SYS_`

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPLS188) for more information about this parameter
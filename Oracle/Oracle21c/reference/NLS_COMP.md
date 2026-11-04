---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_COMP.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.217 NLS\_COMP

`NLS_COMP` specifies the collation behavior of the database session.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_COMP = { BINARY \| LINGUISTIC \| ANSI }` |
| Default value | `BINARY` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `BINARY`
	Normally, comparisons in the `WHERE` clause and in PL/SQL blocks is binary unless you specify the `NLSSORT` function.
- `LINGUISTIC`
	Comparisons for all SQL operations in the `WHERE` clause and in PL/SQL blocks should use the linguistic sort specified in the `NLS_SORT` parameter. To improve the performance, you can also define a linguistic index on the column for which you want linguistic comparisons.
- `ANSI`
	A setting of `ANSI` is for backward compatibility; in general, you should set `NLS_COMP` to `LINGUISTIC`

Note:

Unless you explicitly set the value for `NLS_COMP` in your initialization parameter file, a default value of NULL is shown in the following views: `V$PARAMETER`, `V$SYSTEM_PARAMETER`, `V$PARAMETER2`, `V$SYSTEM_PARAMETER2`, and `NLS_INSTANCE_PARAMETERS`. However, the actual default value, and behavior, is `BINARY`. Note that you cannot change the default to NULL, because NULL is not among the valid values.

Examples

See [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG231) for examples of using this parameter.

Note:

The value of this initialization parameter `NLS_COMP` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.
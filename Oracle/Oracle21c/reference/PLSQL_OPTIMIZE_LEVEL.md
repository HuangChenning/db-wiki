---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PLSQL_OPTIMIZE_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.288 PLSQL\_OPTIMIZE\_LEVEL

`PLSQL_OPTIMIZE_LEVEL` specifies the optimization level that will be used to compile PL/SQL library units. The higher the setting of this parameter, the more effort the compiler makes to optimize PL/SQL library units.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `2` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `3` |
| Basic | No |

Values

- `0`
	Maintains the evaluation order and hence the pattern of side effects, exceptions, and package initializations of Oracle9i and earlier releases. Also removes the new semantic identity of `BINARY_INTEGER` and `PLS_INTEGER` and restores the earlier rules for the evaluation of integer expressions. Although code will run somewhat faster than it did in Oracle9i, use of level 0 will forfeit most of the performance gains of PL/SQL in Oracle Database 10g.
- `1`
	Applies a wide range of optimizations to PL/SQL programs including the elimination of unnecessary computations and exceptions, but generally does not move source code out of its original source order.
- `2`
	Applies a wide range of modern optimization techniques beyond those of level 1 including changes which may move source code relatively far from its original location.
- 3
	Applies a wide range of optimization techniques beyond those of level 2, automatically including techniques not specifically requested.

Generally, setting this parameter to `2` pays off in better execution performance. If, however, the compiler runs slowly on a particular source module or if optimization does not make sense for some reason (for example, during rapid turnaround development), then setting this parameter to `1` will result in almost as good a compilation with less use of compile-time resources.

The value of this parameter is stored persistently with the library unit.

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPLS188) for more information about this parameter
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADFNS1423) for an example of using this parameter
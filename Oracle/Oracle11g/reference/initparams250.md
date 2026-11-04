---
title: SQLTUNE_CATEGORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams250.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SQLTUNE_CATEGORY =` `category_name` |
| Default value | `DEFAULT` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`SQLTUNE_CATEGORY` specifies the category name for use by sessions to qualify the lookup of SQL profiles during SQL compilation.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on the `DBMS_SQLTUNE` package
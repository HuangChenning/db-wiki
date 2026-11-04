---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/SQLTUNE_CATEGORY.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.350 SQLTUNE\_CATEGORY

`SQLTUNE_CATEGORY` specifies the category name for use by sessions to qualify the lookup of SQL profiles during SQL compilation.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SQLTUNE_CATEGORY = ` `category_name` |
| Default value | `DEFAULT` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ARPLS220) for information on the `DBMS_SQLTUNE` package
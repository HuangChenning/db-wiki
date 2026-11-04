---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SQLTUNE_CATEGORY.html
tags:
  - oracle
  - 12c
  - reference
---

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

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS220) for information on the `DBMS_SQLTUNE` package
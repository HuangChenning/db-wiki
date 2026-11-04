---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/NLS_NCHAR_CONV_EXCP.html
tags:
  - oracle
  - 12c
  - reference
---

`NLS_NCHAR_CONV_EXCP` determines whether an error is reported when there is data loss during an implicit or explicit character type conversion between NCHAR/NVARCHAR2 and CHAR/VARCHAR2.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_NCHAR_CONV_EXCP = { TRUE \| FALSE }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

The default value results in no error being reported.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NLSPG233) for more information about this parameter
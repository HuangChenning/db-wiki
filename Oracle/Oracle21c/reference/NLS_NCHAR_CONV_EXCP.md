---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_NCHAR_CONV_EXCP.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.225 NLS\_NCHAR\_CONV\_EXCP

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

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG233) for more information about this parameter
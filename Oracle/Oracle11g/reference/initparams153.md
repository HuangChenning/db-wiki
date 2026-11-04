---
title: NLS_NCHAR_CONV_EXCP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams153.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_NCHAR_CONV_EXCP = { TRUE \| FALSE }` |
| Default value | `FALSE` |
| Modifiable | `ALTER SESSION` |

`NLS_NCHAR_CONV_EXCP` determines whether an error is reported when there is data loss during an implicit or explicit character type conversion between NCHAR/NVARCHAR2 and CHAR/VARCHAR2. The default value results in no error being reported.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information on setting this parameter
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_DATE_LANGUAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.220 NLS\_DATE\_LANGUAGE

`NLS_DATE_LANGUAGE` specifies the language to use for the spelling of day and month names and date abbreviations (a.m., p.m., AD, BC) returned by the `TO_DATE` and `TO_CHAR` functions.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_DATE_LANGUAGE = ` `language` |
| Default value | Derived from `NLS_LANGUAGE` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid `NLS_LANGUAGE` value |
| Basic | No |

Note:

The value of this initialization parameter `NLS_DATE_LANGUAGE` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG205) for more information about this parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF06132) for information on the `TO_DATE` function.
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF06129) for information on the `TO_CHAR` function.
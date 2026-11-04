---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_CURRENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.218 NLS\_CURRENCY

`NLS_CURRENCY` specifies the string to use as the local currency symbol for the L number format element. The default value of this parameter is determined by `NLS_TERRITORY`.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_CURRENCY = ` `currency_symbol` |
| Default value | Derived from `NLS_TERRITORY` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid character string, with a maximum of 10 bytes (not including null) |
| Basic | No |

Note:

The value of this initialization parameter `NLS_CURRENCY` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG222) for more information about this parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF51073) for information on number format elements
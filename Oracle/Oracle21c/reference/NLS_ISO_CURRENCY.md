---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_ISO_CURRENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.222 NLS\_ISO\_CURRENCY

`NLS_ISO_CURRENCY` determines the string to use as the international currency symbol corresponding to the C number format element in a call to the `TO_CHAR` function.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_ISO_CURRENCY = ` `territory` |
| Default value | Derived from `NLS_TERRITORY` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid `NLS_TERRITORY` value |
| Basic | No |

Local currency symbols can be ambiguous. For example, a dollar sign ($) can refer to U.S. dollars or Australian dollars. ISO Specification 4217 defines unique "international" currency symbols for the currencies of specific territories or countries. The value of the `NLS_ISO_CURRENCY` parameter is the Oracle name of the territory whose ISO currency symbol is returned in place of the C number format element. For example, if `NLS_ISO_CURRENCY` is set to `AMERICA`, the string 'USD' is returned by `TO_CHAR` where the C element is specified in the format.

Note:

The value of this initialization parameter `NLS_ISO_CURRENCY` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG223) for more information about this parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF51073) for information on number format elements
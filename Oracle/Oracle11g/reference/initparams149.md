---
title: NLS_DUAL_CURRENCY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams149.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_DUAL_CURRENCY =` `currency_symbol` |
| Default value | Derived from `NLS_TERRITORY` |
| Modifiable | `ALTER SESSION` |
| Range of values | Any valid format name up to 10 characters |

`NLS_DUAL_CURRENCY` specifies the dual currency symbol (such as "Euro") for the territory. The default is the dual currency symbol defined in the territory of your current language environment.

Note:

The value of this initialization parameter `NLS_DUAL_CURRENCY` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information on setting this parameter
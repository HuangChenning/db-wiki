---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_TIMESTAMP_FORMAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.229 NLS\_TIMESTAMP\_FORMAT

`NLS_TIMESTAMP_FORMAT` defines the datetime format model to use with the `TO_CHAR` and `TO_TIMESTAMP` functions.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_TIMESTAMP_FORMAT = "` `format` `"` |
| Default value | Derived from `NLS_TERRITORY` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid datetime format model |
| Basic | No |

The value must be surrounded by quotation marks as follows:

```
NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH:MI:SS.FF'
```

You can specify the value of `NLS_TIMESTAMP_FORMAT` by setting it in the initialization parameter file. You can specify its value for a client as a client environment variable.

You can also alter the value of `NLS_TIMESTAMP_FORMAT` by changing its value in the initialization parameter and then restarting the instance. To alter the value during a session use the `ALTER SESSION SET` statement.

Note:

The value of this initialization parameter `NLS_TIMESTAMP_FORMAT` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-49B32A81-0904-433E-B7FE-51606672183A) for more information on datetime format models
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG207) for more information about this parameter
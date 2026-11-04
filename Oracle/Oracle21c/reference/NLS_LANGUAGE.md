---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_LANGUAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.223 NLS\_LANGUAGE

`NLS_LANGUAGE` specifies the default language of the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_LANGUAGE = ` `language` |
| Default value | Operating system-dependent, derived from the `NLS_LANG` environment variable |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid language name |
| Basic | Yes |

This language specified by `NLS_LANGUAGE` is used for messages, day and month names, symbols for AD, BC, a.m., and p.m., and the default sorting mechanism. This parameter also determines the default values of the parameters `NLS_DATE_LANGUAGE` and `NLS_SORT`.

Note:

The value of this initialization parameter `NLS_LANGUAGE` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

Examples

See these examples of using the `NLS_LANGUAGE` parameter:

- For an example of setting `NLS_LANGUAGE` to Italian, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG724).
- For an example of overriding default values for `NLS_LANGUAGE` and `NLS_TERRITORY` during a session, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG201).

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG199) for more information about this parameter.
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG947) for a complete list of languages that can be specified using this parameter
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG201) for information on overriding the default values for this parameter
- Your operating system-specific Oracle documentation and the release notes for your country
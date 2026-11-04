---
title: NLS_TERRITORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams156.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_TERRITORY =` `territory` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SESSION` |
| Range of values | Any valid territory name |
| Basic | Yes |

`NLS_TERRITORY` specifies the name of the territory whose conventions are to be followed for day and week numbering.

This parameter also establishes the default date format, the default decimal character and group separator, and the default ISO and local currency symbols.

For information on these settings, see ["NLS\_DATE\_FORMAT"](initparams147.md), ["NLS\_NUMERIC\_CHARACTERS"](initparams154.md), ["NLS\_CURRENCY"](initparams146.md), and ["NLS\_ISO\_CURRENCY"](initparams150.md).

Note:

The value of this initialization parameter `NLS_TERRITORY` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for a complete list of territories
- Your operating system-specific Oracle documentation for the territory-dependent default values for these parameters
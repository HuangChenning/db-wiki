---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_TERRITORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.228 NLS\_TERRITORY

`NLS_TERRITORY` specifies the name of the territory whose conventions are to be followed for day and week numbering.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_TERRITORY = ` `territory` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid territory name |
| Basic | Yes |

This parameter also establishes the default date format, the default decimal character and group separator, and the default ISO and local currency symbols.

For information on these settings, see " [NLS\_DATE\_FORMAT](NLS_DATE_FORMAT.md) ", " [NLS\_NUMERIC\_CHARACTERS](NLS_NUMERIC_CHARACTERS.md) ", " [NLS\_CURRENCY](NLS_CURRENCY.md) ", and " [NLS\_ISO\_CURRENCY](NLS_ISO_CURRENCY.md) ".

Note:

The value of this initialization parameter `NLS_TERRITORY` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

Examples

For an example of overriding the default value for the `NLS_TERRITORY` parameter, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG201).

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG-GUID-550D6A25-DB53-4911-9419-8065A73FFB06) for a complete list of territories
- Your operating system-specific Oracle documentation for the territory-dependent default values for these parameters
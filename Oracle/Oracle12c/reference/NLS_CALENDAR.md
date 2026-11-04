---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/NLS_CALENDAR.html
tags:
  - oracle
  - 12c
  - reference
---

`NLS_CALENDAR` specifies which calendar system Oracle uses.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_CALENDAR = "` `calendar_system` `"` |
| Default value | None, implies `GREGORIAN` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid calendar format name |
| Basic | No |

`NLS_CALENDAR` can have one of the following values:

- Arabic Hijrah
- English Hijrah
- Gregorian
- Japanese Imperial
- Persian
- ROC Official (Republic of China)
- Thai Buddha

For example, suppose `NLS_CALENDAR` is set to "Japanese Imperial", the date format is "E YY-MM-DD". ("E" is the date format element for the abbreviated era name.) If the date is May 15, 1997, then the `SYSDATE` is displayed as follows:

```
SELECT SYSDATE FROM DUAL;
SYSDATE
--------
H 09-05-15
```

Note:

The value of the initialization parameter `NLS_CALENDER` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. If the initialization parameter is not specified, the initial session value becomes `GREGORIAN`. This initial value is overridden by a client-side value if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NLSPG215) for a listing of available calendar systems
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/NLS_NUMERIC_CHARACTERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.226 NLS\_NUMERIC\_CHARACTERS

`NLS_NUMERIC_CHARACTERS` specifies the characters to use as the group separator and decimal character.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `NLS_NUMERIC_CHARACTERS =`  `   "` `decimal_character` `group_separator` `"` |
| Default value | Derived from `NLS_TERRITORY` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | Yes |
| Basic | No |

`NLS_NUMERIC_CHARACTERS` overrides those characters defined implicitly by `NLS_TERRITORY`. The group separator separates integer groups (that is, thousands, millions, billions, and so on). The decimal separates the integer portion of a number from the decimal portion.

You can specify any character as the decimal or group separator. The two characters specified must be single-byte and must be different from each other. The characters cannot be any numeric character or any of the following characters: plus (+), minus sign (-), less than sign (<), greater than sign (>). Either character can be a space.

For example, if you want to specify a comma as the decimal character and a space as the group separator, you would set this parameter as follows:

```
NLS_NUMERIC_CHARACTERS = ", "
```

Note:

The value of this initialization parameter `NLS_NUMERIC_CHARACTERS` is used to initialize the session value of this parameter, which is the actual value referenced by the SQL query processing. This initial value is overridden by a client-side value if the client uses the Oracle JDBC driver or if the client is OCI-based and the `NLS_LANG` client setting (environment variable) is defined. The initialization parameter value is, therefore, usually ignored.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG218) for more information about this parameter
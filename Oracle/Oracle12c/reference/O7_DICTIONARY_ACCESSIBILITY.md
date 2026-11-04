---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/O7_DICTIONARY_ACCESSIBILITY.html
tags:
  - oracle
  - 12c
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

If the parameter is set to `true`, access to objects in the `SYS` schema is allowed (Oracle7 behavior). The `false` setting ensures that system privileges that allow access to objects in "any schema" do not allow access to objects in the `SYS` schema.

For example, if `O7_DICTIONARY_ACCESSIBILITY` is set to `false`, then the `SELECT ANY TABLE` privilege allows access to views or tables in any schema except the `SYS` schema (data dictionary tables cannot be accessed). If O7\_DICTIONARY\_ACCESSIBILITY is set to `false`, then to access objects in the `SYS` schema, the user should have `SELECT ANY DICTIONARY` system privilege or the user should have been granted `SELECT` object privilege on the specific objects. The system privilege `EXECUTE ANY PROCEDURE` allows access on the procedures in any schema except the `SYS` schema.

If this parameter is set to `false` and you need to access objects in the `SYS` schema, then you must be granted explicit object privileges. The following roles, which can be granted to the database administrator, also allow access to dictionary objects:

- `SELECT_CATALOG_ROLE`
- `EXECUTE_CATALOG_ROLE`

Note:

The `O7_DICTIONARY_ACCESSIBILITY` initialization parameter is deprecated in Oracle Database 12c Release 2 (12.2.0.1), and may be desupported in a future release.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF01603) for information on granting roles
- [Oracle Database 2 Day + Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TDPSG60622) for more information about enabling data dictionary protection using this parameter
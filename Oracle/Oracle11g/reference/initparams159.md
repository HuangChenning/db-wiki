---
title: O7_DICTIONARY_ACCESSIBILITY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams159.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |

`O7_DICTIONARY_ACCESSIBILITY` controls restrictions on `SYSTEM` privileges. If the parameter is set to `true`, access to objects in the `SYS` schema is allowed (Oracle7 behavior). The default setting of `false` ensures that system privileges that allow access to objects in "any schema" do not allow access to objects in the `SYS` schema.

For example, if `O7_DICTIONARY_ACCESSIBILITY` is set to `false`, then the `SELECT ANY TABLE` privilege allows access to views or tables in any schema except the `SYS` schema (data dictionary tables cannot be accessed). If O7\_DICTIONARY\_ACCESSIBILITY is set to `false`, then to access objects in the `SYS` schema, the user should have `SELECT ANY DICTIONARY` system privilege or the user should have been granted `SELECT` object privilege on the specific objects. The system privilege `EXECUTE ANY PROCEDURE` allows access on the procedures in any schema except the `SYS` schema.

If this parameter is set to `false` and you need to access objects in the `SYS` schema, then you must be granted explicit object privileges. The following roles, which can be granted to the database administrator, also allow access to dictionary objects:

- `SELECT_CATALOG_ROLE`
- `EXECUTE_CATALOG_ROLE`
- `DELETE_CATALOG_ROLE`

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for more information on this parameter and the roles mentioned here
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information on granting roles
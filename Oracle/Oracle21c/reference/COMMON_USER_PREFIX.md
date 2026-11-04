---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/COMMON_USER_PREFIX.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.49 COMMON\_USER\_PREFIX

`COMMON_USER_PREFIX` specifies a prefix that the names of common users, roles, and profiles in a multitenant container database (CDB) must start with.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `COMMON_USER_PREFIX = prefix` |
| Default value | In a CDB root, `C##` is the default value. In an application root, the empty string is the default value. |
| Modifiable | No |
| Modifiable in a PDB | No  However, you can modify this parameter in an application root. |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value |

Names of local users, roles, and profiles must not start with the same prefix. A case-insensitive comparison of the prefixes for user, role, and profile names to the value of this parameter is done.

When a value is set for `COMMON_USER_PREFIX`, Oracle will require that the names of common users, roles, and profiles start with the string assigned to this parameter.

The names of users, roles, and profiles created using this prefix must be valid names.

Regardless of the value of the `COMMON_USER_PREFIX` parameter, the names of local users, roles, and profiles cannot start with `C##`. Similarly, the names of application common users and local users in an application PDB cannot start with `C##`.

Caution:

You can change the value of the `COMMON_USER_PREFIX` parameter, but do so only with great care.

If `COMMON_USER_PREFIX` is set to an empty string, Oracle will not enforce any restrictions on the names of common or local users, roles, and profiles.

Setting this parameter to an empty string will result in no restrictions being placed on names of common and local users, roles, and profiles, which could lead to conflicts between the names of local and common users, roles, and profiles when a PDB is plugged into a different CDB, or when opening a PDB that was closed when a common user was created.

Note:

`COMMON_USER_PREFIX` can be set in the context of an application container.

If you set `COMMON_USER_PREFIX` in the application root to a non-null value, then the application common user should start with that prefix, and a local user created in an application PDB cannot start with that prefix.

By default, `COMMON_USER_PREFIX` is the empty string in an application root.

Note:

When you query the `V$PARAMETER` or `V$SYSTEM_PARAMETER` view, a value of `NONE` is returned for the `DEFAULT_VALUE` column for the `COMMON_USER_PREFIX` parameter.

However, the database enforces a default value of `C##` for a CDB root and a default value of the empty string for an application root.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF54735) for information about valid user names
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF54308) for information about valid role names
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF54278) for information about valid profile names
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT89234) for more information about the multitenant architecture
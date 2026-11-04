---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MANDATORY_USER_PROFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.198 MANDATORY\_USER\_PROFILE

`MANDATORY_USER_PROFILE` specifies the mandatory user profile for a CDB or PDB.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MANDATORY_USER_PROFILE = profile_name` |
| Default value | There is no default value |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances must use the same value. |

For `profile_name`, specify the name of a mandatory user profile. Mandatory user profiles are common profiles created in the CDB root with the following SQL statement:

```
CREATE MANDATORY PROFILE ... CONTAINER = ALL;
```

You can set the value of `MANDATORY_USER_PROFILE` in the CDB root or in a PDB.

- When you set this parameter in the CDB root, the specified mandatory user profile applies to the CDB root and all PDBs.
- When you set this parameter in a PDB, the specified mandatory user profile applies only to that PDB and overrides the mandatory user profile for the CDB root, if any.

Only common users with the commonly granted `ALTER` `SYSTEM` privilege or the commonly granted `SYSDBA` privilege can set the value of `MANDATORY_USER_PROFILE` in the CDB root or in a PDB. This prevents local PDB administrators from circumventing any restrictions that are enforced at the CDB root.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-8EF7F4E6-04DD-42B8-A2C9-649923F26587) for more information about mandatory user profiles
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PDB_LOCKDOWN.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.278 PDB\_LOCKDOWN

`PDB_LOCKDOWN` determines the PDB lockdown profile that applies to a PDB.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PDB_LOCKDOWN = pdb-lockdown-profile-name` |
| Default value | `NULL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should have the same value |

A PDB lockdown profile is a mechanism to restrict operations (such as setting values of certain parameters and using certain options) that can be performed by users connected to a given PDB. You can also restrict execution of any packages that allow network access, for example, `UTL_SMTP`.

You create lockdown profiles using the SQL `CREATE LOCKDOWN PROFILE` statement. Then you can set a profile using the SQL `ALTER SESSION` or `ALTER SYSTEM` statement. See the Examples section.

This parameter can be set using the `ALTER SYSTEM` statement with scope set to `MEMORY`, `SPFILE`, or `BOTH`.

The lockdown profile for PDBs can be specified by a common user with common `ALTER SYSTEM` or common `SYSDBA` privilege.

If a PDB lockdown profile is dropped, any PDB to which the dropped profile was assigned (by means of storing the dropped profile name in the `PDB_LOCKDOWN` parameter) will continue to have its `PDB_LOCKDOWN` parameter set to the dropped lockdown profile name. However, the PDB will not have any restrictions imposed by the dropped lockdown profile.

Lockdown profiles can now be created in an application root and are referred to as application lockdown profiles.

A CDB common user with common `SYSDBA` or common `ALTER SYSTEM` privilege can only set `PDB_LOCKDOWN` to a CDB lockdown profile. Similarly, an application common user with application common `SYSDBA` or application common `ALTER SYSTEM` privilege can only set `PDB_LOCKDOWN` to an application lockdown profile.

An application common user cannot overwrite `PDB_LOCKDOWN` if `PDB_LOCKDOWN` is already set to a CDB lockdown profile in an application root or application PDB.

If the `PDB_LOCKDOWN` parameter in a PDB is set to the name of a lockdown profile different from that in its ancestor (for a CDB, the CDB root or, for application PDBs, the application root), the following will govern the interaction between restrictions imposed by these profiles:

- If the `PDB_LOCKDOWN` parameter in a PDB (including an application PDB) is set to a CDB lockdown profile, lockdown profiles specified by the `PDB_LOCKDOWN` parameter in CDB root (and for application PDBs, the application root) are ignored.
- If the `PDB_LOCKDOWN` parameter in an application PDB is set to an application lockdown profile while the `PDB_LOCKDOWN` parameter in the application root or CDB root is set to a CDB lockdown profile, in addition to the rules stipulated in the application lockdown profile, the DISABLE rules from the CDB lockdown profile set in its nearest ancestor (that is, an application root or CDB root) are inherited.
- If there are conflicts between rules comprising the CDB lockdown profile and the application lockdown profile, the rules in the CDB lockdown profile will take precedence (for example, the `OPTION_VALUE` clause of a CDB lockdown profile will take precedence over the `OPTION_VALUE` clause of an application lockdown profile).

Examples

This example shows how the `SYS` user can connect to the database `AS SYSDBA` and use the `CREATE LOCKDOWN PROFILE` statement in the root of a CDB to define a new lockdown profile. After defining the new lockdown profile, the `SYS` user can assign the new lockdown profile to a PDB using the `PDB_LOCKDOWN` parameter:

```
SQL> ALTER SESSION SET CONTAINER=CDB$ROOT;

Session altered.

SQL> CREATE LOCKDOWN PROFILE MYPROFILE;

Lockdown Profile created.

SQL> ALTER SESSION SET CONTAINER=CDB1_PDB1;

Session altered.

SQL> ALTER SYSTEM SET PDB_LOCKDOWN=MYPROFILE;

System altered.

SQL> SHOW PARAMETER PDB_LOCKDOWN

NAME           TYPE        VALUE
-------------- ----------- ---------
pdb_lockdown   string      MYPROFILE
SQL>
```

See Also:

- " [DBA\_LOCKDOWN\_PROFILES](DBA_LOCKDOWN_PROFILES.md) "
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-1F6D3E4F-786A-47A0-A36C-83BAB75FCDAE) for an introduction to PDB lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF-GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about the `CREATE LOCKDOWN PROFILE` statement
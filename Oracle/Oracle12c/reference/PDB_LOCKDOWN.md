---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PDB_LOCKDOWN.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

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
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT-GUID-1F6D3E4F-786A-47A0-A36C-83BAB75FCDAE) for an introduction to PDB lockdown profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF-GUID-1CDEC3A3-F3F1-4279-9370-36AACF416E0A) for more information about the `CREATE LOCKDOWN PROFILE` statement
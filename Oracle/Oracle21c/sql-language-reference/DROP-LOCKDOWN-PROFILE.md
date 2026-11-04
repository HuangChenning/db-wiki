---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-LOCKDOWN-PROFILE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP LOCKDOWN PROFILE

Purpose

Use the `DROP` `LOCKDOWN` `PROFILE` statement to remove a PDB lockdown profile from the database. A PDB that was assigned the dropped profile will continue to be assigned the profile, but will not be subject to the restrictions imposed by the dropped profile.

If the `PDB_LOCKDOWN` initialization parameter for a CDB, an application root, or a PDB has the value of the dropped lockdown profile, then the restrictions imposed by the dropped profile will be disabled when you drop it. However, the value of the `PDB_LOCKDOWN` initialization parameter will remain until you explicitly unset it.

See Also:

- [CREATE LOCKDOWN PROFILE](CREATE-LOCKDOWN-PROFILE.md) and [ALTER LOCKDOWN PROFILE](ALTER-LOCKDOWN-PROFILE.md)
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275) for more information on PDB lockdown profiles

Prerequisites

- You must issue this statement from the CDB Root or the Application Root.
- You must have the `DROP` `LOCKDOWN` `PROFILE` system privilege in the container where you mean to issue the statement.

Syntax

drop\_lockdown\_profile::=

![drop_lockdown_profile](img/drop_lockdown_profile.gif)

> ```
> DROP LOCKDOWN PROFILE profile_name ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

profile\_name

Specify the name of the PDB lockdown profile to be dropped.

You can find the names of existing PDB lockdown profiles by querying the `DBA_LOCKDOWN_PROFILES` data dictionary view.

See Also:

Oracle Database Reference for more information on the [`DBA_LOCKDOWN_PROFILES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=REFRN-GUID-2DEBBEBC-7A6B-4984-A7E7-90314971182E) data dictionary view and the [`PDB_LOCKDOWN`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=REFRN-GUID-27072E94-1E1D-4BB0-AEAE-D7AFDC02E0A1) initialization parameter

Example

The following statement drops PDB lockdown profile `hr_prof`:

```
DROP LOCKDOWN PROFILE hr_prof;
```
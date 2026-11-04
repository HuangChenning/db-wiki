---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-PROFILE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP PROFILE

Purpose

Use the `DROP` `PROFILE` statement to remove a profile from the database. You can drop any profile except the `DEFAULT` profile.

See Also:

[CREATE PROFILE](CREATE-PROFILE.md) and [ALTER PROFILE](ALTER-PROFILE.md) on creating and modifying a profile

Prerequisites

You must have the `DROP` `PROFILE` system privilege.

Syntax

drop\_profile::=

![drop_profile](img/drop_profile.gif)

> ```
> DROP PROFILE profile [ CASCADE ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

profile

Specify the name of the profile to be dropped.

CASCADE

Specify `CASCADE` to deassign the profile from any users to whom it is assigned. Oracle Database automatically assigns the `DEFAULT` profile to such users. You must specify this clause to drop a profile that is currently assigned to users.

Examples

Dropping a Profile: Example

The following statement drops the profile `app_user`, which was created in " [Creating a Profile: Example](CREATE-PROFILE.md) ". Oracle Database drops the profile `app_user` and assigns the `DEFAULT` profile to any users currently assigned the `app_user` profile:

```
DROP PROFILE app_user CASCADE;
```
---
title: DROP PROFILE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8027.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `PROFILE` statement to remove a profile from the database. You can drop any profile except the `DEFAULT` profile.

See Also:

[CREATE PROFILE](statements_6010.md) and [ALTER PROFILE](statements_2008.md) on creating and modifying a profile

Prerequisites

You must have the `DROP` `PROFILE` system privilege.

Syntax

drop\_profile::=

![drop_profile](img/drop_profile.gif)

> ```
> DROP PROFILE profile [ CASCADE ] ;
> ```
  

Semantics

profile

Specify the name of the profile to be dropped.

CASCADE

Specify `CASCADE` to deassign the profile from any users to whom it is assigned. Oracle Database automatically assigns the `DEFAULT` profile to such users. You must specify this clause to drop a profile that is currently assigned to users.

Examples

Dropping a Profile: Example The following statement drops the profile `app_user`, which was created in ["Creating a Profile: Example"](statements_6010.md). Oracle Database drops the profile `app_user` and assigns the `DEFAULT` profile to any users currently assigned the `app_user` profile:

```
DROP PROFILE app_user CASCADE;
```
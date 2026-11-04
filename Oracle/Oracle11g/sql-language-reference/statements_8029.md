---
title: DROP ROLE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8029.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `ROLE` statement to remove a role from the database. When you drop a role, Oracle Database revokes it from all users and roles to whom it has been granted and removes it from the database. User sessions in which the role is already enabled are not affected. However, no new user session can enable the role after it is dropped.

See Also:

- [CREATE ROLE](statements_6012.md) and [ALTER ROLE](statements_2010.md) for information on creating roles and changing the authorization needed to enable a role
- [SET ROLE](statements_10004.md) for information on disabling roles for the current session

Prerequisites

You must have been granted the role with the `ADMIN` `OPTION` or you must have the `DROP` `ANY` `ROLE` system privilege.

Syntax

drop\_role::=

  
[Description of the illustration ''drop\_role.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/drop_role.htm)  

Semantics

role

Specify the name of the role to be dropped.

Examples

Dropping a Role: Example To drop the role `dw_manager`, which was created in ["Creating a Role: Example"](statements_6012.md), issue the following statement:

```
DROP ROLE dw_manager;
```
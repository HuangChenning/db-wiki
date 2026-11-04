---
title: "8.2.5 Specifying Role Names"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/role-names.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 8.2.5 Specifying Role Names

MySQL role names refer to roles, which are named collections of privileges. For role usage examples, see [Section 8.2.10, “Using Roles”](roles.md).

Role names have syntax and semantics similar to account names; see [Section 8.2.4, “Specifying Account Names”](account-names.md). As stored in the grant tables, they have the same properties as account names, which are described in [Grant Table Scope Column Properties](grant-tables.md).

Role names differ from account names in these respects:

- The user part of role names cannot be blank. Thus, there is no “anonymous role” analogous to the concept of “anonymous user.”
- As for an account name, omitting the host part of a role name results in a host part of `'%'`. But unlike `'%'` in an account name, a host part of `'%'` in a role name has no wildcard properties. For example, for a name `'me'@'%'` used as a role name, the host part (`'%'`) is just a literal value; it has no “any host” matching property.
- Netmask notation in the host part of a role name has no significance.
- An account name is permitted to be [`CURRENT_USER()`](information-functions.md) in several contexts. A role name is not.

It is possible for a row in the `mysql.user` system table to serve as both an account and a role. In this case, any special user or host name matching properties do not apply in contexts for which the name is used as a role name. For example, you cannot execute the following statement with the expectation that it sets the current session roles using all roles that have a user part of `myrole` and any host name:

```
SET ROLE 'myrole'@'%';
```

Instead, the statement sets the active role for the session to the role with exactly the name `'myrole'@'%'`.

For this reason, role names are often specified using only the user name part and letting the host name part implicitly be `'%'`. Specifying a role with a non- `'%'` host part can be useful if you intend to create a name that works both as a role an as a user account that is permitted to connect from the given host.
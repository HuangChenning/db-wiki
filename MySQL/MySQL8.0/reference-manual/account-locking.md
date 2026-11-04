---
title: "8.2.20 Account Locking"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/account-locking.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 8.2.20 Account Locking

MySQL supports locking and unlocking user accounts using the `ACCOUNT LOCK` and `ACCOUNT       UNLOCK` clauses for the [`CREATE       USER`](create-user.md) and [`ALTER USER`](alter-user.md) statements:

- When used with [`CREATE USER`](create-user.md), these clauses specify the initial locking state for a new account. In the absence of either clause, the account is created in an unlocked state.
	If the `validate_password` component is enabled, creating an account without a password is not permitted, even if the account is locked. See [Section 8.4.3, “The Password Validation Component”](validate-password.md).
- When used with [`ALTER USER`](alter-user.md), these clauses specify the new locking state for an existing account. In the absence of either clause, the account locking state remains unchanged.
	As of MySQL 8.0.19, [`ALTER USER ...           UNLOCK`](alter-user.md) unlocks any account named by the statement that is temporarily locked due to too many failed logins. See [Section 8.2.15, “Password Management”](password-management.md).

Account locking state is recorded in the `account_locked` column of the `mysql.user` system table. The output from [`SHOW CREATE USER`](show-create-user.md) indicates whether an account is locked or unlocked.

If a client attempts to connect to a locked account, the attempt fails. The server increments the [`Locked_connects`](server-status-variables.md) status variable that indicates the number of attempts to connect to a locked account, returns an [`ER_ACCOUNT_HAS_BEEN_LOCKED`](https://docs.oracle.com/cd/E17952_01/mysql-errors-8.0-en/server-error-reference.html#error_er_account_has_been_locked) error, and writes a message to the error log:

```
Access denied for user 'user_name'@'host_name'.
Account is locked.
```

Locking an account does not affect being able to connect using a proxy user that assumes the identity of the locked account. It also does not affect the ability to execute stored programs or views that have a `DEFINER` attribute naming the locked account. That is, the ability to use a proxied account or stored programs or views is not affected by locking the account.

The account-locking capability depends on the presence of the `account_locked` column in the `mysql.user` system table. For upgrades from MySQL versions older than 5.7.6, perform the MySQL upgrade procedure to ensure that this column exists. See [Chapter 3, *Upgrading MySQL*](upgrading.md). For nonupgraded installations that have no `account_locked` column, the server treats all accounts as unlocked, and using the `ACCOUNT       LOCK` or `ACCOUNT UNLOCK` clauses produces an error.
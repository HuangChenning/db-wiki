---
title: "MySQL :: MySQL 26.10 Reference Manual :: 8.2.3 Grant Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/grant-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 8.2.3 Grant Tables

The `mysql` system database includes several grant tables that contain information about user accounts and the privileges held by them. This section describes those tables. For information about other tables in the system database, see [Section 7.3, “The mysql System Schema”](system-schema.md).

The discussion here describes the underlying structure of the grant tables and how the server uses their contents when interacting with clients. However, normally you do not modify the grant tables directly. Modifications occur indirectly when you use account-management statements such as [`CREATE       USER`](create-user.md), [`GRANT`](grant.md), and [`REVOKE`](revoke.md) to set up accounts and control the privileges available to each one. See [Section 15.7.1, “Account Management Statements”](account-management-statements.md). When you use such statements to perform account manipulations, the server modifies the grant tables on your behalf.

Note

Direct modification of grant tables using statements such as [`INSERT`](insert.md), [`UPDATE`](update.md), or [`DELETE`](delete.md) is discouraged and done at your own risk. The server is free to ignore rows that become malformed as a result of such modifications.

For any operation that modifies a grant table, the server checks whether the table has the expected structure and produces an error if not. To update the tables to the expected structure, perform the MySQL upgrade procedure. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

#### Grant Table Overview

These `mysql` database tables contain grant information:

- `user`: User accounts, static global privileges, and other nonprivilege columns.
- `global_grants`: Dynamic global privileges.
- `db`: Database-level privileges.
- `tables_priv`: Table-level privileges.
- `columns_priv`: Column-level privileges.
- `procs_priv`: Stored procedure and function privileges.
- `proxies_priv`: Proxy-user privileges.
- `default_roles`: Default user roles.
- `role_edges`: Edges for role subgraphs.
- `password_history`: Password change history.

For information about the differences between static and dynamic global privileges, see [Static Versus Dynamic Privileges](privileges-provided.md).)

Grant tables use the `InnoDB` storage engine and are transactional. Each statement either succeeds for all named users or rolls back and has no effect if any error occurs.

Each grant table contains scope columns and privilege columns:

- Scope columns determine the scope of each row in the tables; that is, the context in which the row applies. For example, a `user` table row with `Host` and `User` values of `'h1.example.net'` and `'bob'` applies to authenticating connections made to the server from the host `h1.example.net` by a client that specifies a user name of `bob`. Similarly, a `db` table row with `Host`, `User`, and `Db` column values of `'h1.example.net'`, `'bob'` and `'reports'` applies when `bob` connects from the host `h1.example.net` to access the `reports` database. The `tables_priv` and `columns_priv` tables contain scope columns indicating tables or table/column combinations to which each row applies. The `procs_priv` scope columns indicate the stored routine to which each row applies.
- Privilege columns indicate which privileges a table row grants; that is, which operations it permits to be performed. The server combines the information in the various grant tables to form a complete description of a user's privileges. [Section 8.2.7, “Access Control, Stage 2: Request Verification”](request-access.md), describes the rules for this.

In addition, a grant table may contain columns used for purposes other than scope or privilege assessment.

The server uses the grant tables in the following manner:

- The `user` table scope columns determine whether to reject or permit incoming connections. For permitted connections, any privileges granted in the `user` table indicate the user's static global privileges. Any privileges granted in this table apply to *all* databases on the server.
	Caution
	Because any static global privilege is considered a privilege for all databases, any static global privilege enables a user to see all database names with [`SHOW DATABASES`](show-databases.md) or by examining the [`SCHEMATA`](information-schema-schemata-table.md) table of `INFORMATION_SCHEMA`, except databases that have been restricted at the database level by partial revokes.
- The `global_grants` table lists current assignments of dynamic global privileges to user accounts. For each row, the scope columns determine which user has the privilege named in the privilege column.
- The `db` table scope columns determine which users can access which databases from which hosts. The privilege columns determine the permitted operations. A privilege granted at the database level applies to the database and to all objects in the database, such as tables and stored programs.
- The `tables_priv` and `columns_priv` tables are similar to the `db` table, but are more fine-grained: They apply at the table and column levels rather than at the database level. A privilege granted at the table level applies to the table and to all its columns. A privilege granted at the column level applies only to a specific column.
- The `procs_priv` table applies to stored routines (stored procedures and functions). A privilege granted at the routine level applies only to a single procedure or function.
- The `proxies_priv` table indicates which users can act as proxies for other users and whether a user can grant the [`PROXY`](privileges-provided.md) privilege to other users.
- The `default_roles` and `role_edges` tables contain information about role relationships.
- The `password_history` table retains previously chosen passwords to enable restrictions on password reuse. See [Section 8.2.15, “Password Management”](password-management.md).

The server reads the contents of the grant tables into memory when it starts. You can tell it to reload the tables by issuing a [`FLUSH PRIVILEGES`](flush.md) statement or executing a [**mysqladmin flush-privileges**](mysqladmin.md) or [**mysqladmin reload**](mysqladmin.md) command. Changes to the grant tables take effect as indicated in [Section 8.2.13, “When Privilege Changes Take Effect”](privilege-changes.md).

When you modify an account, it is a good idea to verify that your changes have the intended effect. To check the privileges for a given account, use the [`SHOW         GRANTS`](show-grants.md) statement. For example, to determine the privileges that are granted to an account with user name and host name values of `bob` and `pc84.example.com`, use this statement:

```sql
SHOW GRANTS FOR 'bob'@'pc84.example.com';
```

To display nonprivilege properties of an account, use [`SHOW CREATE USER`](show-create-user.md):

```sql
SHOW CREATE USER 'bob'@'pc84.example.com';
```

#### The user and db Grant Tables

The server uses the `user` and `db` tables in the `mysql` database at both the first and second stages of access control (see [Section 8.2, “Access Control and Account Management”](access-control.md)). The columns in the `user` and `db` tables are shown here.

**Table 8.4 user and db Table Columns**

| Table Name | `user` | `db` |
| --- | --- | --- |
| **Scope columns** | `Host` | `Host` |
|  | `User` | `Db` |
|  |  | `User` |
| **Privilege columns** | `Select_priv` | `Select_priv` |
|  | `Insert_priv` | `Insert_priv` |
|  | `Update_priv` | `Update_priv` |
|  | `Delete_priv` | `Delete_priv` |
|  | `Index_priv` | `Index_priv` |
|  | `Alter_priv` | `Alter_priv` |
|  | `Create_priv` | `Create_priv` |
|  | `Drop_priv` | `Drop_priv` |
|  | `Grant_priv` | `Grant_priv` |
|  | `Create_view_priv` | `Create_view_priv` |
|  | `Show_view_priv` | `Show_view_priv` |
|  | `Create_routine_priv` | `Create_routine_priv` |
|  | `Alter_routine_priv` | `Alter_routine_priv` |
|  | `Execute_priv` | `Execute_priv` |
|  | `Trigger_priv` | `Trigger_priv` |
|  | `Event_priv` | `Event_priv` |
|  | `Create_tmp_table_priv` | `Create_tmp_table_priv` |
|  | `Lock_tables_priv` | `Lock_tables_priv` |
|  | `References_priv` | `References_priv` |
|  | `Reload_priv` |  |
|  | `Shutdown_priv` |  |
|  | `Process_priv` |  |
|  | `File_priv` |  |
|  | `Show_db_priv` |  |
|  | `Super_priv` |  |
|  | `Repl_slave_priv` |  |
|  | `Repl_client_priv` |  |
|  | `Create_user_priv` |  |
|  | `Create_tablespace_priv` |  |
|  | `Create_role_priv` |  |
|  | `Drop_role_priv` |  |
| **Security columns** | `ssl_type` |  |
|  | `ssl_cipher` |  |
|  | `x509_issuer` |  |
|  | `x509_subject` |  |
|  | `plugin` |  |
|  | `authentication_string` |  |
|  | `password_expired` |  |
|  | `password_last_changed` |  |
|  | `password_lifetime` |  |
|  | `account_locked` |  |
|  | `Password_reuse_history` |  |
|  | `Password_reuse_time` |  |
|  | `Password_require_current` |  |
|  | `User_attributes` |  |
| **Resource control columns** | `max_questions` |  |
|  | `max_updates` |  |
|  | `max_connections` |  |
|  | `max_user_connections` |  |

The `user` table `plugin` and `authentication_string` columns store authentication plugin and credential information.

The server uses the plugin named in the `plugin` column of an account row to authenticate connection attempts for the account.

The `plugin` column must be nonempty. At startup, and at runtime when [`FLUSH         PRIVILEGES`](flush.md) is executed, the server checks `user` table rows. For any row with an empty `plugin` column, the server writes a warning to the error log of this form:

```svg
[Warning] User entry 'user_name'@'host_name' has an empty plugin
value. The user will be ignored and no one can login with this user
anymore.
```

To assign a plugin to an account that is missing one, use the [`ALTER USER`](alter-user.md) statement.

The `password_expired` column permits DBAs to expire account passwords and require users to reset their password. The default `password_expired` value is `'N'`, but can be set to `'Y'` with the [`ALTER         USER`](alter-user.md) statement. After an account's password has been expired, all operations performed by the account in subsequent connections to the server result in an error until the user issues an [`ALTER USER`](alter-user.md) statement to establish a new account password.

Note

Although it is possible to “reset” an expired password by setting it to its current value, it is preferable, as a matter of good policy, to choose a different password. DBAs can enforce non-reuse by establishing an appropriate password-reuse policy. See [Password Reuse Policy](password-management.md).

`password_last_changed` is a `TIMESTAMP` column indicating when the password was last changed. The value is non- `NULL` only for accounts that use a MySQL built-in authentication plugin (`sha256_password` or `caching_sha2_password`). The value is `NULL` for other accounts, such as those authenticated using an external authentication system.

`password_last_changed` is updated by the [`CREATE USER`](create-user.md), [`ALTER USER`](alter-user.md), and [`SET PASSWORD`](set-password.md) statements, and by [`GRANT`](grant.md) statements that create an account or change an account password.

`password_lifetime` indicates the account password lifetime, in days. If the password is past its lifetime (assessed using the `password_last_changed` column), the server considers the password expired when clients connect using the account. A value of *`N`* greater than zero means that the password must be changed every *`N`* days. A value of 0 disables automatic password expiration. If the value is `NULL` (the default), the global expiration policy applies, as defined by the [`default_password_lifetime`](server-system-variables.md) system variable.

`account_locked` indicates whether the account is locked (see [Section 8.2.20, “Account Locking”](account-locking.md)).

`Password_reuse_history` is the value of the `PASSWORD HISTORY` option for the account, or `NULL` for the default history.

`Password_reuse_time` is the value of the `PASSWORD REUSE INTERVAL` option for the account, or `NULL` for the default interval.

`Password_require_current` corresponds to the value of the `PASSWORD REQUIRE` option for the account, as shown by the following table.

**Table 8.5 Permitted Password\_require\_current Values**

| Password\_require\_current Value | Corresponding PASSWORD REQUIRE Option |
| --- | --- |
| `'Y'` | `PASSWORD REQUIRE CURRENT` |
| `'N'` | `PASSWORD REQUIRE CURRENT OPTIONAL` |
| `NULL` | `PASSWORD REQUIRE CURRENT DEFAULT` |

`User_attributes` is a JSON-format column that stores account attributes not stored in other columns. The `INFORMATION_SCHEMA` exposes these attributes through the [`USER_ATTRIBUTES`](information-schema-user-attributes-table.md) table.

The `User_attributes` column may contain these attributes:

- `additional_password`: The secondary password, if any. See [Dual Password Support](password-management.md).
- `Restrictions`: Restriction lists, if any. Restrictions are added by partial-revoke operations. The attribute value is an array of elements that each have `Database` and `Restrictions` keys indicating the name of a restricted database and the applicable restrictions on it (see [Section 8.2.12, “Privilege Restriction Using Partial Revokes”](partial-revokes.md)).
- `Password_locking`: The conditions for failed-login tracking and temporary account locking, if any (see [Failed-Login Tracking and Temporary Account Locking](password-management.md)). The `Password_locking` attribute is updated according to the `FAILED_LOGIN_ATTEMPTS` and `PASSWORD_LOCK_TIME` options of the [`CREATE USER`](create-user.md) and [`ALTER USER`](alter-user.md) statements. The attribute value is a hash with `failed_login_attempts` and `password_lock_time_days` keys indicating the value of such options as have been specified for the account. If a key is missing, its value is implicitly 0. If a key value is implicitly or explicitly 0, the corresponding capability is disabled.
- `multi_factor_authentication`: Rows in the `mysql.user` system table have a `plugin` column that indicates an authentication plugin. For single-factor authentication, that plugin is the only authentication factor. For two-factor or three-factor forms of multifactor authentication, that plugin corresponds to the first authentication factor, but additional information must be stored for the second and third factors. The `multi_factor_authentication` attribute holds this information.
	The `multi_factor_authentication` value is an array, where each array element is a hash that describes an authentication factor using these attributes:
	- `plugin`: The name of the authentication plugin.
	- `authentication_string`: The authentication string value.
	- `passwordless`: A flag that denotes whether the user is meant to be used without a password (with a security token as the only authentication method).
	- `requires_registration`: a flag that defines whether the user account has registered a security token.
	The first and second array elements describe multifactor authentication factors 2 and 3.

If no attributes apply, `User_attributes` is `NULL`.

Example: An account that has a secondary password and partially revoked database privileges has `additional_password` and `Restrictions` attributes in the column value:

```sql
mysql> SELECT User_attributes FROM mysql.User WHERE User = 'u'\G
*************************** 1. row ***************************
User_attributes: {"Restrictions":
                   [{"Database": "mysql", "Privileges": ["SELECT"]}],
                  "additional_password": "hashed_credentials"}
```

To determine which attributes are present, use the [`JSON_KEYS()`](json-search-functions.md) function:

```sql
SELECT User, Host, JSON_KEYS(User_attributes)
FROM mysql.user WHERE User_attributes IS NOT NULL;
```

To extract a particular attribute, such as `Restrictions`, do this:

```sql
SELECT User, Host, User_attributes->>'$.Restrictions'
FROM mysql.user WHERE User_attributes->>'$.Restrictions' <> '';
```

Here is an example of the kind of information stored for `multi_factor_authentication`:

```json
{
  "multi_factor_authentication": [
    {
      "plugin": "authentication_ldap_simple",
      "passwordless": 0,
      "authentication_string": "ldap auth string",
      "requires_registration": 0
    },
    {
      "plugin": "authentication_webauthn",
      "passwordless": 0,
      "authentication_string": "",
      "requires_registration": 1
    }
  ]
}
```

#### The tables\_priv and columns\_priv Grant Tables

During the second stage of access control, the server performs request verification to ensure that each client has sufficient privileges for each request that it issues. In addition to the `user` and `db` grant tables, the server may also consult the `tables_priv` and `columns_priv` tables for requests that involve tables. The latter tables provide finer privilege control at the table and column levels. They have the columns shown in the following table.

**Table 8.6 tables\_priv and columns\_priv Table Columns**

| Table Name | `tables_priv` | `columns_priv` |
| --- | --- | --- |
| **Scope columns** | `Host` | `Host` |
|  | `Db` | `Db` |
|  | `User` | `User` |
|  | `Table_name` | `Table_name` |
|  |  | `Column_name` |
| **Privilege columns** | `Table_priv` | `Column_priv` |
|  | `Column_priv` |  |
| **Other columns** | `Timestamp` | `Timestamp` |
|  | `Grantor` |  |

The `Timestamp` and `Grantor` columns are set to the current timestamp and the [`CURRENT_USER`](information-functions.md) value, respectively, but are otherwise unused.

#### The procs\_priv Grant Table

For verification of requests that involve stored routines, the server may consult the `procs_priv` table, which has the columns shown in the following table.

**Table 8.7 procs\_priv Table Columns**

| Table Name | `procs_priv` |
| --- | --- |
| **Scope columns** | `Host` |
|  | `Db` |
|  | `User` |
|  | `Routine_name` |
|  | `Routine_type` |
| **Privilege columns** | `Proc_priv` |
| **Other columns** | `Timestamp` |
|  | `Grantor` |

The `Routine_type` column is an [`ENUM`](enum.md) column with values of `'FUNCTION'` or `'PROCEDURE'` to indicate the type of routine the row refers to. This column enables privileges to be granted separately for a function and a procedure with the same name.

The `Timestamp` and `Grantor` columns are unused.

#### The proxies\_priv Grant Table

The `proxies_priv` table records information about proxy accounts. It has these columns:

- `Host`, `User`: The proxy account; that is, the account that has the [`PROXY`](privileges-provided.md) privilege for the proxied account.
- `Proxied_host`, `Proxied_user`: The proxied account.
- `Grantor`, `Timestamp`: Unused.
- `With_grant`: Whether the proxy account can grant the [`PROXY`](privileges-provided.md) privilege to other accounts.

For an account to be able to grant the [`PROXY`](privileges-provided.md) privilege to other accounts, it must have a row in the `proxies_priv` table with `With_grant` set to 1 and `Proxied_host` and `Proxied_user` set to indicate the account or accounts for which the privilege can be granted. For example, the `'root'@'localhost'` account created during MySQL installation has a row in the `proxies_priv` table that enables granting the [`PROXY`](privileges-provided.md) privilege for `''@''`, that is, for all users and all hosts. This enables `root` to set up proxy users, as well as to delegate to other accounts the authority to set up proxy users. See [Section 8.2.19, “Proxy Users”](proxy-users.md).

#### The global\_grants Grant Table

The `global_grants` table lists current assignments of dynamic global privileges to user accounts. The table has these columns:

- `USER`, `HOST`: The user name and host name of the account to which the privilege is granted.
- `PRIV`: The privilege name.
- `WITH_GRANT_OPTION`: Whether the account can grant the privilege to other accounts.

#### The default\_roles Grant Table

The `default_roles` table lists default user roles. It has these columns:

- `HOST`, `USER`: The account or role to which the default role applies.
- `DEFAULT_ROLE_HOST`, `DEFAULT_ROLE_USER`: The default role.

#### The role\_edges Grant Table

The `role_edges` table lists edges for role subgraphs. It has these columns:

- `FROM_HOST`, `FROM_USER`: The account that is granted a role.
- `TO_HOST`, `TO_USER`: The role that is granted to the account.
- `WITH_ADMIN_OPTION`: Whether the account can grant the role to and revoke it from other accounts by using `WITH ADMIN OPTION`.

#### The password\_history Grant Table

The `password_history` table contains information about password changes. It has these columns:

- `Host`, `User`: The account for which the password change occurred.
- `Password_timestamp`: The time when the password change occurred.
- `Password`: The new password hash value.

The `password_history` table accumulates a sufficient number of nonempty passwords per account to enable MySQL to perform checks against both the account password history length and reuse interval. Automatic pruning of entries that are outside both limits occurs when password-change attempts occur.

Note

The empty password does not count in the password history and is subject to reuse at any time.

If an account is renamed, its entries are renamed to match. If an account is dropped or its authentication plugin is changed, its entries are removed.

#### Grant Table Scope Column Properties

Scope columns in the grant tables contain strings. The default value for each is the empty string. The following table shows the number of characters permitted in each column.

**Table 8.8 Grant Table Scope Column Lengths**

| Column Name | Maximum Permitted Characters |
| --- | --- |
| `Host`, `Proxied_host` | 255 |
| `User`, `Proxied_user` | 32 |
| `Db` | 64 |
| `Table_name` | 64 |
| `Column_name` | 64 |
| `Routine_name` | 64 |

`Host` and `Proxied_host` values are converted to lowercase before being stored in the grant tables.

For access-checking purposes, comparisons of `User`, `Proxied_user`, `authentication_string`, `Db`, and `Table_name` values are case-sensitive. Comparisons of `Host`, `Proxied_host`, `Column_name`, and `Routine_name` values are not case-sensitive.

#### Grant Table Privilege Column Properties

The `user` and `db` tables list each privilege in a separate column that is declared as `ENUM('N','Y') DEFAULT 'N'`. In other words, each privilege can be disabled or enabled, with the default being disabled.

The `tables_priv`, `columns_priv`, and `procs_priv` tables declare the privilege columns as [`SET`](set.md) columns. Values in these columns can contain any combination of the privileges controlled by the table. Only those privileges listed in the column value are enabled.

**Table 8.9 Set-Type Privilege Column Values**

| Table Name | Column Name | Possible Set Elements |
| --- | --- | --- |
| `tables_priv` | `Table_priv` | `'Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop',               'Grant', 'References', 'Index', 'Alter', 'Create View',               'Show view', 'Trigger'` |
| `tables_priv` | `Column_priv` | `'Select', 'Insert', 'Update', 'References'` |
| `columns_priv` | `Column_priv` | `'Select', 'Insert', 'Update', 'References'` |
| `procs_priv` | `Proc_priv` | `'Execute', 'Alter Routine', 'Grant'` |

Only the `user` and `global_grants` tables specify administrative privileges, such as [`RELOAD`](privileges-provided.md), [`SHUTDOWN`](privileges-provided.md), and [`SYSTEM_VARIABLES_ADMIN`](privileges-provided.md). Administrative operations are operations on the server itself and are not database-specific, so there is no reason to list these privileges in the other grant tables. Consequently, the server need consult only the `user` and `global_grants` tables to determine whether a user can perform an administrative operation.

The [`FILE`](privileges-provided.md) privilege also is specified only in the `user` table. It is not an administrative privilege as such, but a user's ability to read or write files on the server host is independent of the database being accessed.

#### Grant Table Concurrency

To permit concurrent DML and DDL operations on MySQL grant tables, read operations that previously acquired row locks on MySQL grant tables are executed as non-locking reads. Operations that are performed as non-locking reads on MySQL grant tables include:

- [`SELECT`](select.md) statements and other read-only statements that read data from grant tables through join lists and subqueries, including [`SELECT             ... FOR SHARE`](innodb-locking-reads.md) statements, using any transaction isolation level.
- DML operations that read data from grant tables (through join lists or subqueries) but do not modify them, using any transaction isolation level.

Statements that no longer acquire row locks when reading data from grant tables report a warning if executed while using statement-based replication.

When using - [`binlog_format=mixed`](replication-options-binary-log.md), DML operations that read data from grant tables are written to the binary log as row events to make the operations safe for mixed-mode replication.

[`SELECT ...         FOR SHARE`](innodb-locking-reads.md) statements that read data from grant tables report a warning. With the `FOR SHARE` clause, read locks are not supported on grant tables.

DML operations that read data from grant tables and are executed using the [`SERIALIZABLE`](innodb-transaction-isolation-levels.md) isolation level report a warning. Read locks that would normally be acquired when using the [`SERIALIZABLE`](innodb-transaction-isolation-levels.md) isolation level are not supported on grant tables.
---
title: "8.2.2 Privileges Provided by MySQL"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/privileges-provided.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 8.2.2 Privileges Provided by MySQL

The privileges granted to a MySQL account determine which operations the account can perform. MySQL privileges differ in the contexts in which they apply and at different levels of operation:

- Administrative privileges enable users to manage operation of the MySQL server. These privileges are global because they are not specific to a particular database.
- Database privileges apply to a database and to all objects within it. These privileges can be granted for specific databases, or globally so that they apply to all databases.
- Privileges for database objects such as tables, indexes, views, and stored routines can be granted for specific objects within a database, for all objects of a given type within a database (for example, all tables in a database), or globally for all objects of a given type in all databases.

Privileges also differ in terms of whether they are static (built in to the server) or dynamic (defined at runtime). Whether a privilege is static or dynamic affects its availability to be granted to user accounts and roles. For information about the differences between static and dynamic privileges, see Static Versus Dynamic Privileges.)

Information about account privileges is stored in the grant tables in the `mysql` system database. For a description of the structure and contents of these tables, see [Section 8.2.3, “Grant Tables”](grant-tables.md). The MySQL server reads the contents of the grant tables into memory when it starts, and reloads them under the circumstances indicated in [Section 8.2.13, “When Privilege Changes Take Effect”](privilege-changes.md). The server bases access-control decisions on the in-memory copies of the grant tables.

Important

Some MySQL releases introduce changes to the grant tables to add new privileges or features. To make sure that you can take advantage of any new capabilities, update your grant tables to the current structure whenever you upgrade MySQL. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

The following sections summarize the available privileges, provide more detailed descriptions of each privilege, and offer usage guidelines.

#### Summary of Available Privileges

The following table shows the static privilege names used in [`GRANT`](grant.md) and [`REVOKE`](revoke.md) statements, along with the column name associated with each privilege in the grant tables and the context in which the privilege applies.

**Table 8.2 Permissible Static Privileges for GRANT and REVOKE**

| Privilege | Grant Table Column | Context |
| --- | --- | --- |
| [`ALL [PRIVILEGES]`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/privileges-provided.html#priv_all) | Synonym for “all privileges” | Server administration |
| `ALTER` | `Alter_priv` | Tables |
| `ALTER ROUTINE` | `Alter_routine_priv` | Stored routines |
| `CREATE` | `Create_priv` | Databases, tables, or indexes |
| `CREATE ROLE` | `Create_role_priv` | Server administration |
| `CREATE ROUTINE` | `Create_routine_priv` | Stored routines |
| `CREATE TABLESPACE` | `Create_tablespace_priv` | Server administration |
| `CREATE TEMPORARY TABLES` | `Create_tmp_table_priv` | Tables |
| `CREATE USER` | `Create_user_priv` | Server administration |
| `CREATE VIEW` | `Create_view_priv` | Views |
| `DELETE` | `Delete_priv` | Tables |
| `DROP` | `Drop_priv` | Databases, tables, or views |
| `DROP ROLE` | `Drop_role_priv` | Server administration |
| `EVENT` | `Event_priv` | Databases |
| `EXECUTE` | `Execute_priv` | Stored routines |
| `FILE` | `File_priv` | File access on server host |
| `GRANT OPTION` | `Grant_priv` | Databases, tables, or stored routines |
| `INDEX` | `Index_priv` | Tables |
| `INSERT` | `Insert_priv` | Tables or columns |
| `LOCK TABLES` | `Lock_tables_priv` | Databases |
| `PROCESS` | `Process_priv` | Server administration |
| `PROXY` | See `proxies_priv` table | Server administration |
| `REFERENCES` | `References_priv` | Databases or tables |
| `RELOAD` | `Reload_priv` | Server administration |
| `REPLICATION CLIENT` | `Repl_client_priv` | Server administration |
| `REPLICATION SLAVE` | `Repl_slave_priv` | Server administration |
| `SELECT` | `Select_priv` | Tables or columns |
| `SHOW DATABASES` | `Show_db_priv` | Server administration |
| `SHOW VIEW` | `Show_view_priv` | Views |
| `SHUTDOWN` | `Shutdown_priv` | Server administration |
| `SUPER` | `Super_priv` | Server administration |
| `TRIGGER` | `Trigger_priv` | Tables |
| `UPDATE` | `Update_priv` | Tables or columns |
| `USAGE` | Synonym for “no privileges” | Server administration |

The following table shows the dynamic privilege names used in [`GRANT`](grant.md) and [`REVOKE`](revoke.md) statements, along with the context in which the privilege applies.

**Table 8.3 Permissible Dynamic Privileges for GRANT and REVOKE**

| Privilege | Context |
| --- | --- |
| `ALLOW_NONEXISTENT_DEFINER` | Orphan object protection |
| `APPLICATION_PASSWORD_ADMIN` | Dual password administration |
| `AUDIT_ABORT_EXEMPT` | Allow queries blocked by audit log filter |
| `AUDIT_ADMIN` | Audit log administration |
| `AUTHENTICATION_POLICY_ADMIN` | Authentication administration |
| `BACKUP_ADMIN` | Backup administration |
| `BINLOG_ADMIN` | Backup and Replication administration |
| `BINLOG_ENCRYPTION_ADMIN` | Backup and Replication administration |
| `CLONE_ADMIN` | Clone administration |
| `CONNECTION_ADMIN` | Server administration |
| `CREATE_SPATIAL_REFERENCE_SYSTEM` | GIS administration |
| `ENCRYPTION_KEY_ADMIN` | Server administration |
| `EXPORT_QUERY_RESULTS` | Allow user to export query results |
| `FIREWALL_ADMIN` | Firewall administration |
| `FIREWALL_EXEMPT` | Firewall administration |
| `FIREWALL_USER` | Firewall administration (deprecated) |
| `FLUSH_OPTIMIZER_COSTS` | Server administration |
| `FLUSH_PRIVILEGES` (Deprecated) | Server administration |
| `FLUSH_STATUS` | Server administration |
| `FLUSH_TABLES` | Server administration |
| `FLUSH_USER_RESOURCES` | Server administration |
| `GROUP_REPLICATION_ADMIN` | Replication administration |
| `GROUP_REPLICATION_STREAM` | Replication administration |
| `INNODB_REDO_LOG_ARCHIVE` | Redo log archiving administration |
| `INNODB_REDO_LOG_ENABLE` | Redo log administration |
| `MASKING_DICTIONARIES_ADMIN` | Server administration |
| `NDB_STORED_USER` | NDB Cluster |
| `OPTIMIZE_LOCAL_TABLE` | [`OPTIMIZE LOCAL               TABLE`](optimize-table.md) statements |
| `OPTION_TRACKER_OBSERVER` | Option Tracker `mysql_option.option_usage` table read access |
| `OPTION_TRACKER_UPDATER` | Option Tracker `mysql_option.option_usage` table write access |
| `PASSWORDLESS_USER_ADMIN` | Authentication administration |
| `PERSIST_RO_VARIABLES_ADMIN` | Server administration |
| `REPLICATION_APPLIER` | `PRIVILEGE_CHECKS_USER` for a replication channel |
| `REPLICATION_SLAVE_ADMIN` | Replication administration |
| `RESOURCE_GROUP_ADMIN` | Resource group administration |
| `RESOURCE_GROUP_USER` | Resource group administration |
| `ROLE_ADMIN` | Server administration |
| `SENSITIVE_VARIABLES_OBSERVER` | Server administration |
| `SESSION_VARIABLES_ADMIN` | Server administration |
| `SET_ANY_DEFINER` | Server administration |
| `SHOW_ROUTINE` | Server administration |
| `SKIP_QUERY_REWRITE` | Server administration |
| `SYSTEM_USER` | Server administration |
| `SYSTEM_VARIABLES_ADMIN` | Server administration |
| `TABLE_ENCRYPTION_ADMIN` | Server administration |
| `TELEMETRY_LOG_ADMIN` | Telemetry log administration for MySQL HeatWave on AWS |
| `TP_CONNECTION_ADMIN` | Thread pool administration |
| `TRANSACTION_GTID_TAG` | Replication administration |
| `VERSION_TOKEN_ADMIN` (Deprecated) | Server administration |
| `XA_RECOVER_ADMIN` | Server administration |

#### Static Privilege Descriptions

Static privileges are built in to the server, in contrast to dynamic privileges, which are defined at runtime. The following list describes each static privilege available in MySQL.

Particular SQL statements might have more specific privilege requirements than indicated here. If so, the description for the statement in question provides the details.

- `ALL`, `ALL             PRIVILEGES`
	These privilege specifiers are shorthand for “all privileges available at a given privilege level” (except `GRANT OPTION`). For example, granting `ALL` at the global or table level grants all global privileges or all table-level privileges, respectively.
- `ALTER`
	Enables use of the [`ALTER             TABLE`](alter-table.md) statement to change the structure of tables. [`ALTER TABLE`](alter-table.md) also requires the `CREATE` and `INSERT` privileges. Renaming a table requires `ALTER` and `DROP` on the old table, `CREATE`, and `INSERT` on the new table.
- `ALTER ROUTINE`
	Enables use of statements that alter or drop stored routines (stored procedures and functions). For routines that fall within the scope at which the privilege is granted and for which the user is not the user named as the routine `DEFINER`, also enables access to routine properties other than the routine definition.
- `CREATE`
	Enables use of statements that create new databases and tables.
- `CREATE ROLE`
	Enables use of the [`CREATE             ROLE`](create-role.md) statement. (The `CREATE             USER` privilege also enables use of the [`CREATE ROLE`](create-role.md) statement.) See [Section 8.2.10, “Using Roles”](roles.md).
	The `CREATE ROLE` and `DROP ROLE` privileges are not as powerful as `CREATE USER` because they can be used only to create and drop accounts. They cannot be used as `CREATE             USER` can be modify account attributes or rename accounts. See [User and Role Interchangeability](roles.md).
- `CREATE ROUTINE`
	Enables use of statements that create stored routines (stored procedures and functions). For routines that fall within the scope at which the privilege is granted and for which the user is not the user named as the routine `DEFINER`, also enables access to routine properties other than the routine definition.
- `CREATE TABLESPACE`
	Enables use of statements that create, alter, or drop tablespaces and log file groups.
- `CREATE TEMPORARY TABLES`
	Enables the creation of temporary tables using the [`CREATE TEMPORARY TABLE`](create-temporary-table.md) statement.
	After a session has created a temporary table, the server performs no further privilege checks on the table. The creating session can perform any operation on the table, such as [`DROP TABLE`](drop-table.md), [`INSERT`](insert.md), [`UPDATE`](update.md), or [`SELECT`](select.md). For more information, see [Section 15.1.24.2, “CREATE TEMPORARY TABLE Statement”](create-temporary-table.md).
- `CREATE USER`
	Enables use of the [`ALTER             USER`](alter-user.md), [`CREATE ROLE`](create-role.md), [`CREATE USER`](create-user.md), [`DROP ROLE`](drop-role.md), [`DROP USER`](drop-user.md), [`RENAME USER`](rename-user.md), and [`REVOKE ALL             PRIVILEGES`](revoke.md) statements.
- `CREATE VIEW`
	Enables use of the [`CREATE             VIEW`](create-view.md) statement.
- `DELETE`
	Enables rows to be deleted from tables in a database.
- `DROP`
	Enables use of statements that drop (remove) existing databases, tables, and views. The `DROP` privilege is required to use the `ALTER TABLE ... DROP PARTITION` statement on a partitioned table. The `DROP` privilege is also required for [`TRUNCATE TABLE`](truncate-table.md).
- `DROP ROLE`
	Enables use of the [`DROP ROLE`](drop-role.md) statement. (The `CREATE USER` privilege also enables use of the [`DROP             ROLE`](drop-role.md) statement.) See [Section 8.2.10, “Using Roles”](roles.md).
	The `CREATE ROLE` and `DROP ROLE` privileges are not as powerful as `CREATE USER` because they can be used only to create and drop accounts. They cannot be used as `CREATE             USER` can be modify account attributes or rename accounts. See [User and Role Interchangeability](roles.md).
- `EVENT`
	Enables use of statements that create, alter, drop, or display events for the Event Scheduler.
- `EXECUTE`
	Enables use of statements that execute stored routines (stored procedures and functions). For routines that fall within the scope at which the privilege is granted and for which the user is not the user named as the routine `DEFINER`, also enables access to routine properties other than the routine definition.
- `FILE`
	Affects the following operations and server behaviors:
	- Enables reading and writing files on the server host using the [`LOAD DATA`](load-data.md) and [`SELECT ...                 INTO OUTFILE`](select-into.md) statements and the [`LOAD_FILE()`](string-functions.md) function. A user who has the `FILE` privilege can read any file on the server host that is either world-readable or readable by the MySQL server. (This implies the user can read any file in any database directory, because the server can access any of those files.)
	- Enables creating new files in any directory where the MySQL server has write access. This includes the server's data directory containing the files that implement the privilege tables.
	- Enables use of the `DATA DIRECTORY` or `INDEX DIRECTORY` table option for the [`CREATE TABLE`](create-table.md) statement.
	As a security measure, the server does not overwrite existing files.
	To limit the location in which files can be read and written, set the [`secure_file_priv`](server-system-variables.md) system variable to a specific directory. See [Section 7.1.8, “Server System Variables”](server-system-variables.md).
- `GRANT OPTION`
	Enables you to grant to or revoke from other users those privileges that you yourself possess.
- `INDEX`
	Enables use of statements that create or drop (remove) indexes. `INDEX` applies to existing tables. If you have the `CREATE` privilege for a table, you can include index definitions in the [`CREATE TABLE`](create-table.md) statement.
- `INSERT`
	Enables rows to be inserted into tables in a database. `INSERT` is also required for the [`ANALYZE TABLE`](analyze-table.md), [`OPTIMIZE TABLE`](optimize-table.md), and [`REPAIR TABLE`](repair-table.md) table-maintenance statements.
- `LOCK TABLES`
	Enables use of explicit [`LOCK             TABLES`](lock-tables.md) statements to lock tables for which you have the `SELECT` privilege. This includes use of write locks, which prevents other sessions from reading the locked table.
- `PROCESS`
	The `PROCESS` privilege controls access to information about threads executing within the server (that is, information about statements being executed by sessions). Thread information available using the [`SHOW PROCESSLIST`](show-processlist.md) statement, the [**mysqladmin processlist**](mysqladmin.md) command, the Information Schema [`PROCESSLIST`](information-schema-processlist-table.md) table, and the Performance Schema [`processlist`](performance-schema-processlist-table.md) table is accessible as follows:
	- With the `PROCESS` privilege, a user has access to information about all threads, even those belonging to other users.
	- Without the `PROCESS` privilege, nonanonymous users have access to information about their own threads but not threads for other users, and anonymous users have no access to thread information.
	Note
	The Performance Schema [`threads`](performance-schema-threads-table.md) table also provides thread information, but table access uses a different privilege model. See [Section 29.12.22.10, “The threads Table”](performance-schema-threads-table.md).
	The `PROCESS` privilege also enables use of the [`SHOW             ENGINE`](show-engine.md) statement, access to the `INFORMATION_SCHEMA` `InnoDB` tables (tables with names that begin with `INNODB_`), and access to the `INFORMATION_SCHEMA` [`FILES`](information-schema-files-table.md) table.
- `PROXY`
	Enables one user to impersonate or become known as another user. See [Section 8.2.19, “Proxy Users”](proxy-users.md).
- `REFERENCES`
	Creation of a foreign key constraint requires the `REFERENCES` privilege for the parent table.
- `RELOAD`
	The `RELOAD` enables the following operations:
	- Use of the [`FLUSH`](flush.md) statement.
	- Use of [**mysqladmin**](mysqladmin.md) commands that are equivalent to [`FLUSH`](flush.md) operations: `flush-hosts`, `flush-logs`, `flush-privileges`, `flush-status`, `flush-tables`, `refresh`, and `reload`.
		The `reload` command tells the server to reload the grant tables into memory. `flush-privileges` is a synonym for `reload`. The `refresh` command closes and reopens the log files and flushes all tables. The other ``flush-*`xxx`*`` commands perform functions similar to `refresh`, but are more specific and may be preferable in some instances. For example, if you want to flush just the log files, `flush-logs` is a better choice than `refresh`.
	- Use of [**mysqldump**](mysqldump.md) options that perform various [`FLUSH`](flush.md) operations: [`--flush-logs`](mysqldump.md) and [`--source-data`](mysqldump.md).
	- Use of the [`RESET BINARY LOGS AND                 GTIDS`](reset-binary-logs-and-gtids.md) and [`RESET                 REPLICA`](reset-replica.md) statements.
- `REPLICATION CLIENT`
	Enables use of the [`SHOW BINARY LOG             STATUS`](show-binary-log-status.md), [`SHOW REPLICA             STATUS`](show-replica-status.md), and [`SHOW BINARY             LOGS`](show-binary-logs.md) statements.
- `REPLICATION SLAVE`
	Enables the account to request updates that have been made to databases on the replication source server, using the [`SHOW             REPLICAS`](show-replicas.md), [`SHOW RELAYLOG             EVENTS`](show-relaylog-events.md), and [`SHOW BINLOG             EVENTS`](show-binlog-events.md) statements. This privilege is also required to use the [**mysqlbinlog**](mysqlbinlog.md) options [`--read-from-remote-server`](mysqlbinlog.md) (`-R`) and [`--read-from-remote-source`](mysqlbinlog.md). Grant this privilege to accounts that are used by replicas to connect to the current server as their replication source server.
- `SELECT`
	Enables rows to be selected from tables in a database. [`SELECT`](select.md) statements require the `SELECT` privilege only if they actually access tables. Some [`SELECT`](select.md) statements do not access tables and can be executed without permission for any database. For example, you can use [`SELECT`](select.md) as a simple calculator to evaluate expressions that make no reference to tables:
	```
	SELECT 1+1;
	SELECT PI()*2;
	```
	The `SELECT` privilege is also needed for other statements that read column values. For example, `SELECT` is needed for columns referenced on the right hand side of *`col_name`* = *`expr`* assignment in [`UPDATE`](update.md) statements or for columns named in the `WHERE` clause of [`DELETE`](delete.md) or [`UPDATE`](update.md) statements.
	The `SELECT` privilege is needed for tables or views used with [`EXPLAIN`](explain.md), including any underlying tables in view definitions.
- `SHOW DATABASES`
	Enables the account to see database names by issuing the `SHOW DATABASE` statement. Accounts that do not have this privilege see only databases for which they have some privileges, and cannot use the statement at all if the server was started with the [`--skip-show-database`](server-options.md) option.
	Caution
	Because any static global privilege is considered a privilege for all databases, any static global privilege enables a user to see all database names with [`SHOW DATABASES`](show-databases.md) or by examining the [`SCHEMATA`](information-schema-schemata-table.md) table of `INFORMATION_SCHEMA`, except databases that have been restricted at the database level by partial revokes.
- `SHOW VIEW`
	Enables use of the [`SHOW CREATE             VIEW`](show-create-view.md) statement. This privilege is also needed for views used with [`EXPLAIN`](explain.md).
- `SHUTDOWN`
	Enables use of the [`SHUTDOWN`](shutdown.md) and [`RESTART`](restart.md) statements, the [**mysqladmin shutdown**](mysqladmin.md) command, and the [`mysql_shutdown()`](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/mysql-shutdown.html) C API function.
- `SUPER`
	`SUPER` is a powerful and far-reaching privilege and should not be granted lightly. If an account needs to perform only a subset of `SUPER` operations, it may be possible to achieve the desired privilege set by instead granting one or more dynamic privileges, each of which confers more limited capabilities. See Dynamic Privilege Descriptions.
	Note
	`SUPER` is deprecated, and you should expect it to be removed in a future version of MySQL. See Migrating Accounts from SUPER to Dynamic Privileges.
	`SUPER` affects the following operations and server behaviors:
	- Enables system variable changes at runtime:
		- Enables server configuration changes to global system variables with [`SET                     GLOBAL`](set-variable.md) and [`SET                     PERSIST`](set-variable.md).
			The corresponding dynamic privilege is `SYSTEM_VARIABLES_ADMIN`.
		- Enables setting restricted session system variables that require a special privilege.
			The corresponding dynamic privilege is `SESSION_VARIABLES_ADMIN`.
		See also [Section 7.1.9.1, “System Variable Privileges”](system-variable-privileges.md).
	- Enables changes to global transaction characteristics (see [Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md)).
		The corresponding dynamic privilege is `SYSTEM_VARIABLES_ADMIN`.
	- Enables the account to start and stop replication, including Group Replication.
		The corresponding dynamic privilege is `REPLICATION_SLAVE_ADMIN` for regular replication, `GROUP_REPLICATION_ADMIN` for Group Replication.
	- Enables use of [`CHANGE REPLICATION                 SOURCE TO`](change-replication-source-to.md) and [`CHANGE                 REPLICATION FILTER`](change-replication-filter.md) statements.
		The corresponding dynamic privilege is `REPLICATION_SLAVE_ADMIN`.
	- Enables binary log control by means of the [`PURGE BINARY LOGS`](purge-binary-logs.md) and [`BINLOG`](binlog.md) statements.
		The corresponding dynamic privilege is `BINLOG_ADMIN`.
	- Enables setting the effective authorization ID when executing a view or stored program. A user with this privilege can specify any account in the `DEFINER` attribute of a view or stored program.
		The corresponding dynamic privileges are `SET_ANY_DEFINER` and `ALLOW_NONEXISTENT_DEFINER`.
	- Enables use of the [`CREATE                 SERVER`](create-server.md), [`ALTER                 SERVER`](alter-server.md), and [`DROP                 SERVER`](drop-server.md) statements.
	- Enables use of the [**mysqladmin debug**](mysqladmin.md) command.
	- Enables `InnoDB` encryption key rotation.
		The corresponding dynamic privilege is `ENCRYPTION_KEY_ADMIN`.
	- Enables execution of deprecated Version Tokens functions.
		The corresponding dynamic privilege is `VERSION_TOKEN_ADMIN`, which is deprecated.
	- Enables granting and revoking roles, use of the `WITH ADMIN OPTION` clause of the [`GRANT`](grant.md) statement, and nonempty `<graphml>` element content in the result from the [`ROLES_GRAPHML()`](information-functions.md) function.
		The corresponding dynamic privilege is `ROLE_ADMIN`.
	- Enables control over client connections not permitted to non- `SUPER` accounts:
		- Enables use of the [`KILL`](kill.md) statement or [**mysqladmin kill**](mysqladmin.md) command to kill threads belonging to other accounts. (An account can always kill its own threads.)
		- The server does not execute [`init_connect`](server-system-variables.md) system variable content when `SUPER` clients connect.
		- The server accepts one connection from a `SUPER` client even if the connection limit configured by the [`max_connections`](server-system-variables.md) system variable is reached.
		- A server in offline mode ([`offline_mode`](server-system-variables.md) enabled) does not terminate `SUPER` client connections at the next client request, and accepts new connections from `SUPER` clients.
		- Updates can be performed even when the [`read_only`](server-system-variables.md) system variable is enabled. This applies to explicit table updates, and to use of account-management statements such as [`GRANT`](grant.md) and [`REVOKE`](revoke.md) that update tables implicitly.
		The corresponding dynamic privilege for the preceding connection control operations is `CONNECTION_ADMIN`.
	You may also need the `SUPER` privilege to create or alter stored functions if binary logging is enabled, as described in [Section 27.9, “Stored Program Binary Logging”](stored-programs-logging.md).
- `TRIGGER`
	Enables trigger operations. You must have this privilege for a table to create, drop, execute, or display triggers for that table.
	When a trigger is activated (by a user who has privileges to execute [`INSERT`](insert.md), [`UPDATE`](update.md), or [`DELETE`](delete.md) statements for the table associated with the trigger), trigger execution requires that the user who defined the trigger still have the `TRIGGER` privilege for the table.
- `UPDATE`
	Enables rows to be updated in tables in a database.
- `USAGE`
	This privilege specifier stands for “no privileges.” It is used at the global level with [`GRANT`](grant.md) to specify clauses such as `WITH GRANT OPTION` without naming specific account privileges in the privilege list. [`SHOW GRANTS`](show-grants.md) displays `USAGE` to indicate that an account has no privileges at a privilege level.

#### Dynamic Privilege Descriptions

Dynamic privileges are defined at runtime, in contrast to static privileges, which are built in to the server. The following list describes each dynamic privilege available in MySQL.

Most dynamic privileges are defined at server startup. Others are defined by a particular component or plugin, as indicated in the privilege descriptions. In such cases, the privilege is unavailable unless the component or plugin that defines it is enabled.

Particular SQL statements might have more specific privilege requirements than indicated here. If so, the description for the statement in question provides the details.

- `ALLOW_NONEXISTENT_DEFINER`
	Enables overriding security checks designed to prevent operations that (perhaps inadvertently) cause stored objects to become orphaned or that cause adoption of stored objects that are currently orphaned. Without this privilege, any attempt to produce an orphaned SQL procedure, function, or view results in an error. An attempt to produce orphaned objects using [`CREATE             PROCEDURE`](create-procedure.md), [`CREATE             FUNCTION`](create-function.md), [`CREATE             TRIGGER`](create-trigger.md), [`CREATE             EVENT`](create-event.md), or [`CREATE             VIEW`](create-view.md) also requires `SET_ANY_DEFINER` in addition to `ALLOW_NONEXISTENT_DEFINER`, so that a definer different from the current user is permissible.
	For details, see [Orphan Stored Objects](stored-objects-security.md).
- `APPLICATION_PASSWORD_ADMIN`
	For dual-password capability, this privilege enables use of the `RETAIN CURRENT PASSWORD` and `DISCARD OLD PASSWORD` clauses for [`ALTER USER`](alter-user.md) and [`SET PASSWORD`](set-password.md) statements that apply to your own account. This privilege is required to manipulate your own secondary password because most users require only one password.
	If an account is to be permitted to manipulate secondary passwords for all accounts, it should be granted the `CREATE USER` privilege rather than `APPLICATION_PASSWORD_ADMIN`.
	For more information about use of dual passwords, see [Section 8.2.15, “Password Management”](password-management.md).
- `AUDIT_ABORT_EXEMPT`
	Allows queries blocked by an “abort” item in the audit log filter. This privilege is defined by the `audit_log` plugin; see [Section 8.4.6, “MySQL Enterprise Audit Plugin (Deprecated)”](audit-log.md).
	Accounts created with the `SYSTEM_USER` privilege have the `AUDIT_ABORT_EXEMPT` privilege assigned automatically when they are created. The `AUDIT_ABORT_EXEMPT` privilege is also assigned to existing accounts with the `SYSTEM_USER` privilege when you carry out an upgrade procedure, if no existing accounts have that privilege assigned. Accounts with the `SYSTEM_USER` privilege can therefore be used to regain access to a system following an audit misconfiguration.
- `AUDIT_ADMIN`
	Enables audit log configuration. This privilege is defined by the `audit_log` plugin; see [Section 8.4.6, “MySQL Enterprise Audit Plugin (Deprecated)”](audit-log.md).
- `BACKUP_ADMIN`
	Enables execution of the [`LOCK INSTANCE             FOR BACKUP`](lock-instance-for-backup.md) statement and access to the Performance Schema [`log_status`](performance-schema-log-status-table.md) table.
	Note
	Besides `BACKUP_ADMIN`, the `SELECT` privilege on the [`log_status`](performance-schema-log-status-table.md) table is also needed for its access.
	The `BACKUP_ADMIN` privilege is automatically granted to users with the `RELOAD` privilege when performing an in-place upgrade to MySQL 9.7 from an earlier version.
- `AUTHENTICATION_POLICY_ADMIN`
	The [`authentication_policy`](server-system-variables.md) system variable places certain constraints on how the authentication-related clauses of [`CREATE USER`](create-user.md) and [`ALTER USER`](alter-user.md) statements may be used. A user who has the `AUTHENTICATION_POLICY_ADMIN` privilege is not subject to these constraints. (A warning does occur for statements that otherwise would not be permitted.)
	For details about the constraints imposed by [`authentication_policy`](server-system-variables.md), see the description of that variable.
- `BINLOG_ADMIN`
	Enables binary log control by means of the [`PURGE BINARY LOGS`](purge-binary-logs.md) and [`BINLOG`](binlog.md) statements.
- `BINLOG_ENCRYPTION_ADMIN`
	Enables setting the system variable [`binlog_encryption`](replication-options-binary-log.md), which activates or deactivates encryption for binary log files and relay log files. This ability is not provided by the `BINLOG_ADMIN`, `SYSTEM_VARIABLES_ADMIN`, or `SESSION_VARIABLES_ADMIN` privileges. The related system variable [`binlog_rotate_encryption_master_key_at_startup`](replication-options-binary-log.md), which rotates the binary log master key automatically when the server is restarted, does not require this privilege.
- `CLONE_ADMIN`
	Enables execution of the `CLONE` statements. Includes `BACKUP_ADMIN` and `SHUTDOWN` privileges.
- `CONNECTION_ADMIN`
	Enables use of the [`KILL`](kill.md) statement or [**mysqladmin kill**](mysqladmin.md) command to kill threads belonging to other accounts. (An account can always kill its own threads.)
	Enables setting system variables related to client connections, or circumventing restrictions related to client connections. `CONNECTION_ADMIN` is required to activate MySQL Server’s offline mode, which is done by changing the value of the [`offline_mode`](server-system-variables.md) system variable to `ON`.
	The `CONNECTION_ADMIN` privilege enables administrators with it to bypass effects of these system variables:
	- [`init_connect`](server-system-variables.md): The server does not execute [`init_connect`](server-system-variables.md) system variable content when `CONNECTION_ADMIN` clients connect.
	- [`max_connections`](server-system-variables.md): The server accepts one connection from a `CONNECTION_ADMIN` client even if the connection limit configured by the [`max_connections`](server-system-variables.md) system variable is reached.
	- [`offline_mode`](server-system-variables.md): A server in offline mode ([`offline_mode`](server-system-variables.md) enabled) does not terminate `CONNECTION_ADMIN` client connections at the next client request, and accepts new connections from `CONNECTION_ADMIN` clients.
	- [`read_only`](server-system-variables.md): Updates from `CONNECTION_ADMIN` clients can be performed even when the [`read_only`](server-system-variables.md) system variable is enabled. This applies to explicit table updates, and to account management statements such as [`GRANT`](grant.md) and [`REVOKE`](revoke.md) that update tables implicitly.
	Group Replication group members need the `CONNECTION_ADMIN` privilege so that Group Replication connections are not terminated if one of the servers involved is placed in offline mode. If the MySQL communication stack is in use ([`group_replication_communication_stack             = MYSQL`](group-replication-system-variables.md)), without this privilege, a member that is placed in offline mode is expelled from the group.
- `CREATE_SPATIAL_REFERENCE_SYSTEM`
	Enables use of the statements [`CREATE             SPATIAL REFERENCE SYSTEM`](create-spatial-reference-system.md), `CREATE OR             REPLACE SPATIAL REFERENCE SYSTEM`, and [`DROP SPATIAL REFERENCE             SYSTEM`](drop-spatial-reference-system.md). Trying to execute any of these statements without having this privilege (or the `SUPER` privilege) now raises the error [`ER_CMD_NEED_SUPER_OR_CREATE_SPATIAL_REFERENCE_SYSTEM`](https://docs.oracle.com/cd/E17952_01/mysql-errors-9.7-en/server-error-reference.html#error_er_cmd_need_super_or_create_spatial_reference_system).
	Use of this privilege is intended to supersede the use of `SUPER` for this purpose, which should be considered deprecated.
- `ENCRYPTION_KEY_ADMIN`
	Enables `InnoDB` encryption key rotation.
- `EXPORT_QUERY_RESULTS`
	Allows the user to export query results to an OCI or AWS object store.
	Applies to MySQL HeatWave only.
- `FIREWALL_ADMIN`
	Enables a user to administer firewall rules for any user. This privilege is defined by the `MYSQL_FIREWALL` plugin; see [Section 8.4.9, “MySQL Enterprise Firewall”](firewall.md).
- `FIREWALL_EXEMPT`
	A user with this privilege is exempt from firewall restrictions. This privilege is defined by the `MYSQL_FIREWALL` plugin; see [Section 8.4.9, “MySQL Enterprise Firewall”](firewall.md).
- `FIREWALL_USER`
	Enables users to update their own firewall rules. This privilege is defined by the MySQL Enterprise Firewall plugin (see [Section 8.4.9.1, “The MySQL Enterprise Firewall Plugin”](firewall-plugin.md)).
	Like the firewall plugin, this privilege is deprecated, and thus subject to removal in a future version of MySQL. `FIREWALL_USER` is not supported by the MySQL Enterprise Firewall component (see [Section 8.4.9.2, “The MySQL Enterprise Firewall Component”](firewall-component.md)), which replaces the plugin.
- `FLUSH_OPTIMIZER_COSTS`
	Enables use of the [`FLUSH             OPTIMIZER_COSTS`](flush.md) statement.
- `FLUSH_PRIVILEGES`
	Enables use of the [`FLUSH             PRIVILEGES`](flush.md) statement.
	Deprecated, along with the [`FLUSH             PRIVILEGES`](flush.md) statement; expect this privilege to be removed in a future version of MySQL. Granting the `FLUSH_PRIVILEGES` privilege triggers a deprecation warning.
- `FLUSH_STATUS`
	Enables use of the [`FLUSH             STATUS`](flush.md) statement.
- `FLUSH_TABLES`
	Enables use of the [`FLUSH             TABLES`](flush.md) statement.
- `FLUSH_USER_RESOURCES`
	Enables use of the [`FLUSH             USER_RESOURCES`](flush.md) statement.
- `GROUP_REPLICATION_ADMIN`
	Enables the account to start and stop Group Replication using the [`START GROUP             REPLICATION`](start-group-replication.md) and [`STOP GROUP             REPLICATION`](stop-group-replication.md) statements, to change the global setting for the [`group_replication_consistency`](group-replication-system-variables.md) system variable, and to use the [`group_replication_set_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) and [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) functions. Grant this privilege to accounts that are used to administer servers that are members of a replication group.
- `GROUP_REPLICATION_STREAM`
	Allows a user account to be used for establishing Group Replication's group communication connections. It must be granted to a recovery user when the MySQL communication stack is used for Group Replication ([`group_replication_communication_stack=MYSQL`](group-replication-system-variables.md)).
- `INNODB_REDO_LOG_ARCHIVE`
	Enables the account to activate and deactivate redo log archiving.
- `INNODB_REDO_LOG_ENABLE`
	Enables use of the [`ALTER             INSTANCE {ENABLE|DISABLE} INNODB REDO_LOG`](alter-instance.md) statement to enable or disable redo logging.
	See [Disabling Redo Logging](innodb-redo-log.md).
- `MASKING_DICTIONARIES_ADMIN`
	Enables the account to add and remove dictionary terms using the [`masking_dictionary_term_add()`](data-masking-component-functions.md) and [`masking_dictionary_term_remove()`](data-masking-component-functions.md) component functions. Accounts also require this dynamic privilege to remove a full dictionary using the [`masking_dictionary_remove()`](data-masking-component-functions.md) function, which removes all of the terms associated with the named dictionary currently in the `mysql.masking_dictionaries` table.
	See [Section 8.5, “MySQL Enterprise Data Masking”](data-masking.md).
- `NDB_STORED_USER`
	Enables the user or role and its privileges to be shared and synchronized between all `NDB` -enabled MySQL servers as soon as they join a given NDB Cluster. This privilege is available only if the [`NDB`](mysql-cluster.md) storage engine is enabled.
	Any changes to or revocations of privileges made for the given user or role are synchronized immediately with all connected MySQL servers (SQL nodes). You should be aware that there is no guarantee that multiple statements affecting privileges originating from different SQL nodes are executed on all SQL nodes in the same order. For this reason, it is highly recommended that all user administration be done from a single designated SQL node.
	`NDB_STORED_USER` is a global privilege and must be granted or revoked using `ON *.*`. Trying to set any other scope for this privilege results in an error. This privilege can be given to most application and administrative users, but it cannot be granted to system reserved accounts such as `mysql.session@localhost` or `mysql.infoschema@localhost`.
	A user that has been granted the `NDB_STORED_USER` privilege is stored in `NDB` (and thus shared by all SQL nodes), as is a role with this privilege. A user that is merely granted a role that has `NDB_STORED_USER` is *not* stored in `NDB`; each `NDB` stored user must be granted the privilege explicitly.
	For more detailed information about how this works in [`NDB`](mysql-cluster.md), see [Section 25.6.13, “Privilege Synchronization and NDB\_STORED\_USER”](mysql-cluster-privilege-synchronization.md).
- `OPTIMIZE_LOCAL_TABLE`
	Enables use of [`OPTIMIZE             LOCAL TABLE`](optimize-table.md) and [`OPTIMIZE             NO_WRITE_TO_BINLOG TABLE`](optimize-table.md) statements.
- `OPTION_TRACKER_OBSERVER`
	This privilege provides write access to the `mysql_option.option_usage` table; both the privilege and the table are supplied by the Option Tracker component. For more information, see [Section 7.5.9, “Option Tracker Component”](option-tracker-component.md).
- `OPTION_TRACKER_UPDATER`
	This privilege is required for write access to the `mysql_option.option_usage` table; both the privilege and the table are supplied by the Option Tracker component. For more information, see [Section 7.5.9, “Option Tracker Component”](option-tracker-component.md).
- `PASSWORDLESS_USER_ADMIN`
	This privilege applies to passwordless user accounts:
	- For account creation, a user who executes [`CREATE USER`](create-user.md) to create a passwordless account must possess the `PASSWORDLESS_USER_ADMIN` privilege.
	- In replication context, the `PASSWORDLESS_USER_ADMIN` privilege applies to replication users and enables replication of [`ALTER USER                 ... MODIFY`](alter-user.md) statements for user accounts that are configured for passwordless authentication.
	For information about passwordless authentication, see [WebAuthn Passwordless Authentication](webauthn-pluggable-authentication.md).
- `PERSIST_RO_VARIABLES_ADMIN`
	For users who also have `SYSTEM_VARIABLES_ADMIN`, `PERSIST_RO_VARIABLES_ADMIN` enables use of [`SET             PERSIST_ONLY`](set-variable.md) to persist global system variables to the `mysqld-auto.cnf` option file in the data directory. This statement is similar to [`SET             PERSIST`](set-variable.md) but does not modify the runtime global system variable value. This makes [`SET             PERSIST_ONLY`](set-variable.md) suitable for configuring read-only system variables that can be set only at server startup.
	See also [Section 7.1.9.1, “System Variable Privileges”](system-variable-privileges.md).
- `REPLICATION_APPLIER`
	Enables the account to act as the `PRIVILEGE_CHECKS_USER` for a replication channel, and to execute `BINLOG` statements in [**mysqlbinlog**](mysqlbinlog.md) output. Grant this privilege to accounts that are assigned using [`CHANGE REPLICATION SOURCE TO`](change-replication-source-to.md) to provide a security context for replication channels, and to handle replication errors on those channels. As well as the `REPLICATION_APPLIER` privilege, you must also give the account the required privileges to execute the transactions received by the replication channel or contained in the [**mysqlbinlog**](mysqlbinlog.md) output, for example to update the affected tables. For more information, see [Section 19.3.3, “Replication Privilege Checks”](replication-privilege-checks.md).
- `REPLICATION_SLAVE_ADMIN`
	Enables the account to connect to the replication source server, start and stop replication using the [`START REPLICA`](start-replica.md) and [`STOP REPLICA`](stop-replica.md) statements, and use the [`CHANGE REPLICATION SOURCE             TO`](change-replication-source-to.md) and [`CHANGE REPLICATION             FILTER`](change-replication-filter.md) statements. Grant this privilege to accounts that are used by replicas to connect to the current server as their replication source server. This privilege does not apply to Group Replication; use `GROUP_REPLICATION_ADMIN` for that.
- `RESOURCE_GROUP_ADMIN`
	Enables resource group management, consisting of creating, altering, and dropping resource groups, and assignment of threads and statements to resource groups. A user with this privilege can perform any operation relating to resource groups.
- `RESOURCE_GROUP_USER`
	Enables assigning threads and statements to resource groups. A user with this privilege can use the [`SET RESOURCE GROUP`](set-resource-group.md) statement and the [`RESOURCE_GROUP`](optimizer-hints.md) optimizer hint.
- `ROLE_ADMIN`
	Enables granting and revoking roles, use of the `WITH ADMIN OPTION` clause of the [`GRANT`](grant.md) statement, and nonempty `<graphml>` element content in the result from the [`ROLES_GRAPHML()`](information-functions.md) function. Required to set the value of the [`mandatory_roles`](server-system-variables.md) system variable.
- `SENSITIVE_VARIABLES_OBSERVER`
	Enables a holder to view the values of sensitive system variables in the Performance Schema tables [`global_variables`](performance-schema-system-variable-tables.md), [`session_variables`](performance-schema-system-variable-tables.md), [`variables_by_thread`](performance-schema-system-variable-tables.md), and [`persisted_variables`](performance-schema-persisted-variables-table.md), to issue `SELECT` statements to return their values, and to track changes to them in session trackers for connections. Users without this privilege cannot view or track those system variable values. See [Persisting Sensitive System Variables](persisted-system-variables.md).
- `SERVICE_CONNECTION_ADMIN`
	Enables connections to the network interface that permits only administrative connections (see [Section 7.1.12.1, “Connection Interfaces”](connection-interfaces.md)).
- `SESSION_VARIABLES_ADMIN`
	For most system variables, setting the session value requires no special privileges and can be done by any user to affect the current session. For some system variables, setting the session value can have effects outside the current session and thus is a restricted operation. For these, the `SESSION_VARIABLES_ADMIN` privilege enables the user to set the session value.
	If a system variable is restricted and requires a special privilege to set the session value, the variable description indicates that restriction. Examples include [`binlog_format`](replication-options-binary-log.md), [`sql_log_bin`](replication-options-binary-log.md), and [`sql_log_off`](server-system-variables.md).
	The `SESSION_VARIABLES_ADMIN` privilege is a subset of the `SYSTEM_VARIABLES_ADMIN` and `SUPER` privileges. A user who has either of those privileges is also permitted to set restricted session variables and effectively has `SESSION_VARIABLES_ADMIN` by implication and need not be granted `SESSION_VARIABLES_ADMIN` explicitly.
	See also [Section 7.1.9.1, “System Variable Privileges”](system-variable-privileges.md).
- `SET_ANY_DEFINER`
	Enables setting the effective authorization ID when executing a view or stored program. A user with this privilege can specify any account as the `DEFINER` attribute for [`CREATE PROCEDURE`](create-procedure.md), [`CREATE FUNCTION`](create-function.md), [`CREATE TRIGGER`](create-trigger.md), [`CREATE EVENT`](create-event.md), [`ALTER EVENT`](alter-event.md), [`CREATE VIEW`](create-view.md), and [`ALTER VIEW`](alter-view.md). Without this privilege, only the effective authentication ID can be specified.
	Stored programs execute with the privileges of the specified account, so ensure that you follow the risk minimization guidelines listed in [Section 27.8, “Stored Object Access Control”](stored-objects-security.md).
- `SHOW_ROUTINE`
	Enables a user to access definitions and properties of all stored routines (stored procedures and functions), even those for which the user is not named as the routine `DEFINER`. This access includes:
	- The contents of the Information Schema [`ROUTINES`](information-schema-routines-table.md) table.
	- The [`SHOW CREATE FUNCTION`](show-create-function.md) and [`SHOW CREATE PROCEDURE`](show-create-procedure.md) statements.
	- The [`SHOW FUNCTION CODE`](show-function-code.md) and [`SHOW PROCEDURE CODE`](show-procedure-code.md) statements.
	- The [`SHOW FUNCTION STATUS`](show-function-status.md) and [`SHOW PROCEDURE STATUS`](show-procedure-status.md) statements.
	`SHOW_ROUTINE` may be granted instead as a privilege with a more restricted scope that permits access to routine definitions. (That is, an administrator can rescind global `SELECT` from users that do not otherwise require it and grant `SHOW_ROUTINE` instead.) This enables an account to back up stored routines without requiring a broad privilege.
- `SKIP_QUERY_REWRITE`
	Queries issued by a user with this privilege are not subject to being rewritten by the `Rewriter` plugin (see [Section 7.6.4, “The Rewriter Query Rewrite Plugin”](rewriter-query-rewrite-plugin.md)).
	This privilege should be granted to users issuing administrative or control statements that should not be rewritten, as well as to `PRIVILEGE_CHECKS_USER` accounts (see [Section 19.3.3, “Replication Privilege Checks”](replication-privilege-checks.md)) used to apply statements from a replication source.
- `SYSTEM_USER`
	The `SYSTEM_USER` privilege distinguishes system users from regular users:
	- A user with the `SYSTEM_USER` privilege is a system user.
	- A user without the `SYSTEM_USER` privilege is a regular user.
	The `SYSTEM_USER` privilege has an effect on the accounts to which a given user can apply its other privileges, as well as whether the user is protected from other accounts:
	- A system user can modify both system and regular accounts. That is, a user who has the appropriate privileges to perform a given operation on regular accounts is enabled by possession of `SYSTEM_USER` to also perform the operation on system accounts. A system account can be modified only by system users with appropriate privileges, not by regular users.
	- A regular user with appropriate privileges can modify regular accounts, but not system accounts. A regular account can be modified by both system and regular users with appropriate privileges.
	This also means that database objects created by users with the `SYSTEM_USER` privilege cannot be modified or dropped by users without the privilege. This also applies to routines for which the definer has this privilege.
	For more information, see [Section 8.2.11, “Account Categories”](account-categories.md).
	The protection against modification by regular accounts that is afforded to system accounts by the `SYSTEM_USER` privilege does not apply to regular accounts that have privileges on the `mysql` system schema and thus can directly modify the grant tables in that schema. For full protection, do not grant `mysql` schema privileges to regular accounts. See [Protecting System Accounts Against Manipulation by Regular Accounts](account-categories.md).
	If the `audit_log` plugin is in use (see [Section 8.4.6, “MySQL Enterprise Audit Plugin (Deprecated)”](audit-log.md)), accounts with the `SYSTEM_USER` privilege are automatically assigned the `AUDIT_ABORT_EXEMPT` privilege, which permits their queries to be executed even if an “abort” item configured in the filter would block them. Accounts with the `SYSTEM_USER` privilege can therefore be used to regain access to a system following an audit misconfiguration.
- `SYSTEM_VARIABLES_ADMIN`
	Affects the following operations and server behaviors:
	- Enables system variable changes at runtime:
		- Enables server configuration changes to global system variables with [`SET                     GLOBAL`](set-variable.md) and [`SET                     PERSIST`](set-variable.md).
		- Enables server configuration changes to global system variables with [`SET                     PERSIST_ONLY`](set-variable.md), if the user also has `PERSIST_RO_VARIABLES_ADMIN`.
		- Enables setting restricted session system variables that require a special privilege. In effect, `SYSTEM_VARIABLES_ADMIN` implies `SESSION_VARIABLES_ADMIN` without explicitly granting `SESSION_VARIABLES_ADMIN`.
		See also [Section 7.1.9.1, “System Variable Privileges”](system-variable-privileges.md).
	- Enables changes to global transaction characteristics (see [Section 15.3.7, “SET TRANSACTION Statement”](set-transaction.md)).
- `TABLE_ENCRYPTION_ADMIN`
	Enables a user to override default encryption settings when [`table_encryption_privilege_check`](server-system-variables.md) is enabled; see [Defining an Encryption Default for Schemas and General Tablespaces](innodb-data-encryption.md).
- `TELEMETRY_LOG_ADMIN`
	Enables telemetry log configuration. This privilege is defined by the `telemetry_log` plugin, which is deployed through MySQL HeatWave on AWS.
- `TP_CONNECTION_ADMIN`
	Enables connecting to the server with a privileged connection. When the limit defined by [`thread_pool_max_transactions_limit`](server-system-variables.md) has been reached, new connections are not permitted, unless overridden by [`thread_pool_longrun_trx_limit`](server-system-variables.md). A privileged connection ignores the transaction limit and permits connecting to the server to increase the transaction limit, remove the limit, or kill running transactions. This privilege is not granted to any user by default. To establish a privileged connection, the user initiating a connection must have the `TP_CONNECTION_ADMIN` privilege.
	A privileged connection can execute statements and start transactions when the limit defined by `thread_pool_max_transactions_limit` has been reached. A privileged connection is placed in the `Admin` thread group. See [Privileged Connections](thread-pool-operation.md).
- `TRANSACTION_GTID_TAG`
	Required for setting the [`gtid_next`](replication-options-gtids.md) system variable to ``AUTOMATIC:*`TAG`*`` or ``UUID:*`TAG`*:NUMBER`` on a replication source server. In addition, at least one of `SYSTEM_VARIABLES_ADMIN`, `SESSION_VARIABLES_ADMIN`, or `REPLICATION_APPLIER` is also required to set `gtid_next` to one of these values on the source.
	The `REPLICATION_CHECKS_APPLIER` must also have this privilege as well as the `REPLICATION_APPLIER` privilege to set `gtid_next` to ``AUTOMATIC:*`TAG`*``. This is checked when starting the replication applier thread.
	This privilege is also required to set the [`gtid_purged`](replication-options-gtids.md) server system variable.
	For more information about using tagged GTIDs, see the description of [`gtid_next`](replication-options-gtids.md), as well as [Section 19.1.4, “Changing GTID Mode on Online Servers”](replication-mode-change-online.md).
- `VERSION_TOKEN_ADMIN`
	Enables execution of Version Tokens functions. This privilege is deprecated. It is defined by the `version_tokens` plugin (also deprecated); see [Version Tokens](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/version-tokens.html).
- `XA_RECOVER_ADMIN`
	Enables execution of the [`XA             RECOVER`](xa-statements.md) statement; see [Section 15.3.8.1, “XA Transaction SQL Statements”](xa-statements.md).
	Prior to MySQL 9.7, any user could execute the [`XA             RECOVER`](xa-statements.md) statement to discover the XID values for outstanding prepared XA transactions, possibly leading to commit or rollback of an XA transaction by a user other than the one who started it. In MySQL 9.7, [`XA             RECOVER`](xa-statements.md) is permitted only to users who have the `XA_RECOVER_ADMIN` privilege, which is expected to be granted only to administrative users who have need for it. This might be the case, for example, for administrators of an XA application if it has crashed and it is necessary to find outstanding transactions started by the application so they can be rolled back. This privilege requirement prevents users from discovering the XID values for outstanding prepared XA transactions other than their own. It does not affect normal commit or rollback of an XA transaction because the user who started it knows its XID.

#### Privilege-Granting Guidelines

It is a good idea to grant to an account only those privileges that it needs. You should exercise particular caution in granting the `FILE` and administrative privileges:

- `FILE` can be abused to read into a database table any files that the MySQL server can read on the server host. This includes all world-readable files and files in the server's data directory. The table can then be accessed using [`SELECT`](select.md) to transfer its contents to the client host.
- `GRANT OPTION` enables users to give their privileges to other users. Two users that have different privileges and with the `GRANT             OPTION` privilege are able to combine privileges.
- `ALTER` may be used to subvert the privilege system by renaming tables.
- `SHUTDOWN` can be abused to deny service to other users entirely by terminating the server.
- `PROCESS` can be used to view the plain text of currently executing statements, including statements that set or change passwords.
- `SUPER` can be used to terminate other sessions or change how the server operates.
- Privileges granted for the `mysql` system database itself can be used to change passwords and other access privilege information:
	- Passwords are stored encrypted, so a malicious user cannot simply read them to know the plain text password. However, a user with write access to the `mysql.user` system table `authentication_string` column can change an account's password, and then connect to the MySQL server using that account.
	- `INSERT` or `UPDATE` granted for the `mysql` system database enable a user to add privileges or modify existing privileges, respectively.
	- `DROP` for the `mysql` system database enables a user to remote privilege tables, or even the database itself.

#### Static Versus Dynamic Privileges

MySQL supports static and dynamic privileges:

- Static privileges are built in to the server. They are always available to be granted to user accounts and cannot be unregistered.
- Dynamic privileges can be registered and unregistered at runtime. This affects their availability: A dynamic privilege that has not been registered cannot be granted.

For example, the `SELECT` and `INSERT` privileges are static and always available, whereas a dynamic privilege becomes available only if the component that implements it has been enabled.

The remainder of this section describes how dynamic privileges work in MySQL. The discussion uses the term “components” but applies equally to plugins.

Note

Server administrators should be aware of which server components define dynamic privileges. For MySQL distributions, documentation of components that define dynamic privileges describes those privileges.

Third-party components may also define dynamic privileges; an administrator should understand those privileges and not install components that might conflict or compromise server operation. For example, one component conflicts with another if both define a privilege with the same name. Component developers can reduce the likelihood of this occurrence by choosing privilege names having a prefix based on the component name.

The server maintains the set of registered dynamic privileges internally in memory. Unregistration occurs at server shutdown.

Normally, a component that defines dynamic privileges registers them when it is installed, during its initialization sequence. When uninstalled, a component does not unregister its registered dynamic privileges. (This is current practice, not a requirement. That is, components could, but do not, unregister at any time privileges they register.)

No warning or error occurs for attempts to register an already registered dynamic privilege. Consider the following sequence of statements:

```
INSTALL COMPONENT 'my_component';
UNINSTALL COMPONENT 'my_component';
INSTALL COMPONENT 'my_component';
```

The first [`INSTALL COMPONENT`](install-component.md) statement registers any privileges defined by component `my_component`, but [`UNINSTALL COMPONENT`](uninstall-component.md) does not unregister them. For the second [`INSTALL         COMPONENT`](install-component.md) statement, the component privileges it registers are found to be already registered, but no warnings or errors occur.

Dynamic privileges apply only at the global level. The server stores information about current assignments of dynamic privileges to user accounts in the `mysql.global_grants` system table:

- The server automatically registers privileges named in `global_grants` during server startup (unless the [`--skip-grant-tables`](server-options.md) option is given).
- The [`GRANT`](grant.md) and [`REVOKE`](revoke.md) statements modify the contents of `global_grants`.
- Dynamic privilege assignments listed in `global_grants` are persistent. They are not removed at server shutdown.

Example: The following statement grants to user `u1` the privileges required to control replication (including Group Replication) on a replica, and to modify system variables:

```
GRANT REPLICATION_SLAVE_ADMIN, GROUP_REPLICATION_ADMIN, BINLOG_ADMIN
ON *.* TO 'u1'@'localhost';
```

Granted dynamic privileges appear in the output from the `SHOW GRANTS` statement and the `INFORMATION_SCHEMA` [`USER_PRIVILEGES`](information-schema-user-privileges-table.md) table.

For [`GRANT`](grant.md) and [`REVOKE`](revoke.md) at the global level, any named privileges not recognized as static are checked against the current set of registered dynamic privileges and granted if found. Otherwise, an error occurs to indicate an unknown privilege identifier.

For [`GRANT`](grant.md) and [`REVOKE`](revoke.md) the meaning of `ALL [PRIVILEGES]` at the global level includes all static global privileges, as well as all currently registered dynamic privileges:

- `GRANT ALL` at the global level grants all static global privileges and all currently registered dynamic privileges. A dynamic privilege registered subsequent to execution of the `GRANT` statement is not granted retroactively to any account.
- `REVOKE ALL` at the global level revokes all granted static global privileges and all granted dynamic privileges.

The [`FLUSH PRIVILEGES`](flush.md) statement reads the `global_grants` table for dynamic privilege assignments and registers any unregistered privileges found there.

For descriptions of the dynamic privileges provided by MySQL Server and components included in MySQL distributions, see Section 8.2.2, “Privileges Provided by MySQL”.

#### Migrating Accounts from SUPER to Dynamic Privileges

In MySQL 9.7, many operations that previously required the `SUPER` privilege are also associated with a dynamic privilege of more limited scope. (For descriptions of these privileges, see Section 8.2.2, “Privileges Provided by MySQL”.) Each such operation can be permitted to an account by granting the associated dynamic privilege rather than `SUPER`. This change improves security by enabling DBAs to avoid granting `SUPER` and tailor user privileges more closely to the operations permitted. `SUPER` is now deprecated; expect it to be removed in a future version of MySQL.

When removal of `SUPER` occurs, operations that formerly required `SUPER` fail unless accounts granted `SUPER` are migrated to the appropriate dynamic privileges. Use the following instructions to accomplish that goal so that accounts are ready prior to `SUPER` removal:

1. Execute this query to identify accounts that are granted `SUPER`:
	```
	SELECT GRANTEE FROM INFORMATION_SCHEMA.USER_PRIVILEGES
	WHERE PRIVILEGE_TYPE = 'SUPER';
	```
2. For each account identified by the preceding query, determine the operations for which it needs `SUPER`. Then grant the dynamic privileges corresponding to those operations, and revoke `SUPER`.
	For example, if `'u1'@'localhost'` requires `SUPER` for binary log purging and system variable modification, these statements make the required changes to the account:
	```
	GRANT BINLOG_ADMIN, SYSTEM_VARIABLES_ADMIN ON *.* TO 'u1'@'localhost';
	REVOKE SUPER ON *.* FROM 'u1'@'localhost';
	```
	After you have modified all applicable accounts, the `INFORMATION_SCHEMA` query in the first step should produce an empty result set.
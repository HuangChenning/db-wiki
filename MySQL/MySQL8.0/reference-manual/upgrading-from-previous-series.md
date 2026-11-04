---
title: "3.5 Changes in MySQL 8.0"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Before upgrading to MySQL 8.0, review the changes described in this section to identify those that apply to your current MySQL installation and applications. Perform any recommended actions.

Changes marked as **Incompatible change** are incompatibilities with earlier versions of MySQL, and may require your attention *before upgrading*. Our aim is to avoid these changes, but occasionally they are necessary to correct problems that would be worse than an incompatibility between releases. If an upgrade issue applicable to your installation involves an incompatibility, follow the instructions given in the description.

### Data Dictionary Changes

MySQL Server 8.0 incorporates a global data dictionary containing information about database objects in transactional tables. In previous MySQL series, dictionary data was stored in metadata files and nontransactional system tables. As a result, the upgrade procedure requires that you verify the upgrade readiness of your installation by checking specific prerequisites. For more information, see [Section 3.6, “Preparing Your Installation for Upgrade”](upgrade-prerequisites.md). A data dictionary-enabled server entails some general operational differences; see [Section 16.7, “Data Dictionary Usage Differences”](data-dictionary-usage-differences.md).

### caching\_sha2\_password as the Preferred Authentication Plugin

The `caching_sha2_password` and `sha256_password` authentication plugins provide more secure password encryption than the `mysql_native_password` plugin, and `caching_sha2_password` provides better performance than `sha256_password`. Due to these superior security and performance characteristics of `caching_sha2_password`, it is as of MySQL 8.0 the preferred authentication plugin, and is also the default authentication plugin rather than `mysql_native_password`. This change affects both the server and the `libmysqlclient` client library:

- For the server, the default value of the [`default_authentication_plugin`](server-system-variables.md) system variable changes from `mysql_native_password` to `caching_sha2_password`.
	This change applies only to new accounts created after installing or upgrading to MySQL 8.0 or higher. For accounts already existing in an upgraded installation, their authentication plugin remains unchanged. Existing users who wish to switch to `caching_sha2_password` can do so using the [`ALTER             USER`](alter-user.md) statement:
	```
	ALTER USER user
	  IDENTIFIED WITH caching_sha2_password
	  BY 'password';
	```
- The `libmysqlclient` library treats `caching_sha2_password` as the default authentication plugin rather than `mysql_native_password`.

The following sections discuss the implications of the more prominent role of `caching_sha2_password`:

#### caching\_sha2\_password Compatibility Issues and Solutions

If your MySQL installation must serve pre-8.0 clients and you encounter compatibility issues after upgrading to MySQL 8.0 or higher, the simplest way to address those issues and restore pre-8.0 compatibility is to reconfigure the server to revert to the previous default authentication plugin (`mysql_native_password`). For example, use these lines in the server option file:

```
[mysqld]
default_authentication_plugin=mysql_native_password
```

That setting enables pre-8.0 clients to connect to 8.0 servers until such time as the clients and connectors in use at your installation are upgraded to know about `caching_sha2_password`. However, the setting should be viewed as temporary, not as a long term or permanent solution, because it causes new accounts created with the setting in effect to forego the improved authentication security provided by `caching_sha2_password`.

The use of `caching_sha2_password` offers more secure password hashing than `mysql_native_password` (and consequent improved client connection authentication). However, it also has compatibility implications that may affect existing MySQL installations:

- Clients and connectors that have not been updated to know about `caching_sha2_password` may have trouble connecting to a MySQL 8.0 server configured with `caching_sha2_password` as the default authentication plugin, even to use accounts that do not authenticate with `caching_sha2_password`. This issue occurs because the server specifies the name of its default authentication plugin to clients. If a client or connector is based on a client/server protocol implementation that does not gracefully handle an unrecognized default authentication plugin, it may fail with an error such as one of these:
	```
	Authentication plugin 'caching_sha2_password' is not supported
	```
	```
	Authentication plugin 'caching_sha2_password' cannot be loaded:
	dlopen(/usr/local/mysql/lib/plugin/caching_sha2_password.so, 2):
	image not found
	```
	```
	Warning: mysqli_connect(): The server requested authentication
	method unknown to the client [caching_sha2_password]
	```
	For information about writing connectors to gracefully handle requests from the server for unknown default authentication plugins, see [Authentication Plugin Connector-Writing Considerations](pluggable-authentication.md).
- Clients that use an account that authenticates with `caching_sha2_password` must use either a secure connection (made using TCP using TLS/SSL credentials, a Unix socket file, or shared memory), or an unencrypted connection that supports password exchange using an RSA key pair. This security requirement does not apply to `mysql_native_passsword`, so the switch to `caching_sha2_password` may require additional configuration (see [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md)). However, client connections in MySQL 8.0 prefer use of TLS/SSL by default, so clients that already conform to that preference may need no additional configuration.
- Clients and connectors that have not been updated to know about `caching_sha2_password` *cannot* connect to accounts that authenticate with `caching_sha2_password` because they do not recognize this plugin as valid. (This is a particular instance of how client/server authentication plugin compatibility requirements apply, as discussed at [Authentication Plugin Client/Server Compatibility](pluggable-authentication.md).) To work around this issue, relink clients against `libmysqlclient` from MySQL 8.0 or higher, or obtain an updated connector that recognizes `caching_sha2_password`.
- Because `caching_sha2_password` is also now the default authentication plugin in the `libmysqlclient` client library, authentication requires an extra round trip in the client/server protocol for connections from MySQL 8.0 clients to accounts that use `mysql_native_password` (the previous default authentication plugin), unless the client program is invoked with a [`--default-auth=mysql_native_password`](connection-options.md) option.

The `libmysqlclient` client library for pre-8.0 MySQL versions is able to connect to MySQL 8.0 servers (except for accounts that authenticate with `caching_sha2_password`). That means pre-8.0 clients based on `libmysqlclient` should also be able to connect. Examples:

- Standard MySQL clients such as [**mysql**](mysql.md) and [**mysqladmin**](mysqladmin.md) are `libmysqlclient` -based.
- The DBD::mysql driver for Perl DBI is `libmysqlclient` -based.
- MySQL Connector/Python has a C Extension module that is `libmysqlclient` -based. To use it, include the `use_pure=False` option at connect time.

When an existing MySQL 8.0 installation is upgraded to MySQL 8.0.4 or higher, some older `libmysqlclient` -based clients may “automatically” upgrade if they are dynamically linked, because they use the new client library installed by the upgrade. For example, if the DBD::mysql driver for Perl DBI uses dynamic linking, it can use the `libmysqlclient` in place after an upgrade to MySQL 8.0.4 or higher, with this result:

- Prior to the upgrade, DBI scripts that use DBD::mysql can connect to a MySQL 8.0 server, except for accounts that authenticate with `caching_sha2_password`.
- After the upgrade, the same scripts become able to use `caching_sha2_password` accounts as well.

However, the preceding results occur because `libmysqlclient` instances from MySQL 8.0 installations prior to 8.0.4 are binary compatible: They both use a shared library major version number of 21. For clients linked to `libmysqlclient` from MySQL 5.7 or older, they link to a shared library with a different version number that is not binary compatible. In this case, the client must be recompiled against `libmysqlclient` from 8.0.4 or higher for full compatibility with MySQL 8.0 servers and `caching_sha2_password` accounts.

MySQL Connector/J 5.1 through 8.0.8 is able to connect to MySQL 8.0 servers, except for accounts that authenticate with `caching_sha2_password`. (Connector/J 8.0.9 or higher is required to connect to `caching_sha2_password` accounts.)

Clients that use an implementation of the client/server protocol other than `libmysqlclient` may need to be upgraded to a newer version that understands the new authentication plugin. For example, in PHP, MySQL connectivity usually is based on `mysqlnd`, which currently does not know about `caching_sha2_password`. Until an updated version of `mysqlnd` is available, the way to enable PHP clients to connect to MySQL 8.0 is to reconfigure the server to revert to `mysql_native_password` as the default authentication plugin, as previously discussed.

If a client or connector supports an option to explicitly specify a default authentication plugin, use it to name a plugin other than `caching_sha2_password`. Examples:

- Some MySQL clients support a [`--default-auth`](connection-options.md) option. (Standard MySQL clients such as [**mysql**](mysql.md) and [**mysqladmin**](mysqladmin.md) support this option but can successfully connect to 8.0 servers without it. However, other clients may support a similar option. If so, it is worth trying it.)
- Programs that use the `libmysqlclient` C API can call the [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/mysql-options.html) function with the `MYSQL_DEFAULT_AUTH` option.
- MySQL Connector/Python scripts that use the native Python implementation of the client/server protocol can specify the `auth_plugin` connection option. (Alternatively, use the Connector/Python C Extension, which is able to connect to MySQL 8.0 servers without the need for `auth_plugin`.)

#### caching\_sha2\_password-Compatible Clients and Connectors

If a client or connector is available that has been updated to know about `caching_sha2_password`, using it is the best way to ensure compatibility when connecting to a MySQL 8.0 server configured with `caching_sha2_password` as the default authentication plugin.

These clients and connectors have been upgraded to support `caching_sha2_password`:

- The `libmysqlclient` client library in MySQL 8.0 (8.0.4 or higher). Standard MySQL clients such as [**mysql**](mysql.md) and [**mysqladmin**](mysqladmin.md) are `libmysqlclient` -based, so they are compatible as well.
- The `libmysqlclient` client library in MySQL 5.7 (5.7.23 or higher). Standard MySQL clients such as [**mysql**](mysql.md) and [**mysqladmin**](mysqladmin.md) are `libmysqlclient` -based, so they are compatible as well.
- MySQL Connector/C++ 1.1.11 or higher or 8.0.7 or higher.
- MySQL Connector/J 8.0.9 or higher.
- MySQL Connector/NET 8.0.10 or higher (through the classic MySQL protocol).
- MySQL Connector/Node.js 8.0.9 or higher.
- PHP: the X DevAPI PHP extension (mysql\_xdevapi) supports `caching_sha2_password`.
	PHP: the PDO\_MySQL and ext/mysqli extensions do not support `caching_sha2_password`. In addition, when used with PHP versions before 7.1.16 and PHP 7.2 before 7.2.4, they fail to connect with `default_authentication_plugin=caching_sha2_password` even if `caching_sha2_password` is not used.

#### caching\_sha2\_password and the root Administrative Account

For upgrades to MySQL 8.0, the authentication plugin existing accounts remains unchanged, including the plugin for the `'root'@'localhost'` administrative account.

For new MySQL 8.0 installations, when you initialize the data directory (using the instructions at [Section 2.9.1, “Initializing the Data Directory”](data-directory-initialization.md)), the `'root'@'localhost'` account is created, and that account uses `caching_sha2_password` by default. To connect to the server following data directory initialization, you must therefore use a client or connector that supports `caching_sha2_password`. If you can do this but prefer that the `root` account use `mysql_native_password` after installation, install MySQL and initialize the data directory as you normally would. Then connect to the server as `root` and use [`ALTER USER`](alter-user.md) as follows to change the account authentication plugin and password:

```
ALTER USER 'root'@'localhost'
  IDENTIFIED WITH mysql_native_password
  BY 'password';
```

If the client or connector that you use does not yet support `caching_sha2_password`, you can use a modified data directory-initialization procedure that associates the `root` account with `mysql_native_password` as soon as the account is created. To do so, use either of these techniques:

- Supply a [`--default-authentication-plugin=mysql_native_password`](server-system-variables.md) option along with [`--initialize`](server-options.md) or [`--initialize-insecure`](server-options.md).
- Set [`default_authentication_plugin`](server-system-variables.md) to `mysql_native_password` in an option file, and name that option file using a [`--defaults-file`](server-options.md) option along with [`--initialize`](server-options.md) or [`--initialize-insecure`](server-options.md). (In this case, if you continue to use that option file for subsequent server startups, new accounts are created with `mysql_native_password` rather than `caching_sha2_password` unless you remove the [`default_authentication_plugin`](server-system-variables.md) setting from the option file.)

#### caching\_sha2\_password and Replication

In replication scenarios for which all servers have been upgraded to MySQL 8.0.4 or higher, replica connections to source servers can use accounts that authenticate with `caching_sha2_password`. For such connections, the same requirement applies as for other clients that use accounts that authenticate with `caching_sha2_password`: Use a secure connection or RSA-based password exchange.

To connect to a `caching_sha2_password` account for source/replica replication:

- Use any of the following [`CHANGE MASTER             TO`](change-master-to.md) options:
	```
	MASTER_SSL = 1
	GET_MASTER_PUBLIC_KEY = 1
	MASTER_PUBLIC_KEY_PATH='path to RSA public key file'
	```
- Alternatively, you can use the RSA public key-related options if the required keys are supplied at server startup.

To connect to a `caching_sha2_password` account for Group Replication:

- For MySQL built using OpenSSL, set any of the following system variables:
	```
	SET GLOBAL group_replication_recovery_use_ssl = ON;
	SET GLOBAL group_replication_recovery_get_public_key = 1;
	SET GLOBAL group_replication_recovery_public_key_path = 'path to RSA public key file';
	```
- Alternatively, you can use the RSA public key-related options if the required keys are supplied at server startup.

### Configuration Changes

- **Incompatible change**: A MySQL storage engine is now responsible for providing its own partitioning handler, and the MySQL server no longer provides generic partitioning support. [`InnoDB`](innodb-storage-engine.md) and `NDB` are the only storage engines that provide a native partitioning handler that is supported in MySQL 8.0. A partitioned table using any other storage engine must be altered—either to convert it to `InnoDB` or `NDB`, or to remove its partitioning— *before* upgrading the server, else it cannot be used afterwards.
	For information about converting `MyISAM` tables to `InnoDB`, see [Section 17.6.1.5, “Converting Tables from MyISAM to InnoDB”](converting-tables-to-innodb.md).
	A table creation statement that would result in a partitioned table using a storage engine without such support fails with an error (ER\_CHECK\_NOT\_IMPLEMENTED) in MySQL 8.0. If you import databases from a dump file created in MySQL 5.7 (or earlier) using [**mysqldump**](mysqldump.md) into a MySQL 8.0 server, you must make sure that any statements creating partitioned tables do not also specify an unsupported storage engine, either by removing any references to partitioning, or by specifying the storage engine as `InnoDB` or allowing it to be set as `InnoDB` by default.
	Note
	The procedure given at [Section 3.6, “Preparing Your Installation for Upgrade”](upgrade-prerequisites.md), describes how to identify partitioned tables that must be altered before upgrading to MySQL 8.0.
	See [Section 26.6.2, “Partitioning Limitations Relating to Storage Engines”](partitioning-limitations-storage-engines.md), for further information.
- **Incompatible change**: Several server error codes are not used and have been removed (for a list, see [Features Removed in MySQL 8.0](mysql-nutshell.md)). Applications that test specifically for any of them should be updated.
- **Important change**: The default character set has changed from `latin1` to `utf8mb4`. These system variables are affected:
	- The default value of the [`character_set_server`](server-system-variables.md) and [`character_set_database`](server-system-variables.md) system variables has changed from `latin1` to `utf8mb4`.
	- The default value of the [`collation_server`](server-system-variables.md) and [`collation_database`](server-system-variables.md) system variables has changed from `latin1_swedish_ci` to `utf8mb4_0900_ai_ci`.
	As a result, the default character set and collation for new objects differ from previously unless an explicit character set and collation are specified. This includes databases and objects within them, such as tables, views, and stored programs. Assuming that the previous defaults were used, one way to preserve them is to start the server with these lines in the `my.cnf` file:
	```
	[mysqld]
	character_set_server=latin1
	collation_server=latin1_swedish_ci
	```
	In a replicated setting, when upgrading from MySQL 5.7 to 8.0, it is advisable to change the default character set back to the character set used in MySQL 5.7 before upgrading. After the upgrade is completed, the default character set can be changed to `utf8mb4`.
	In addition, you should be aware that MySQL 8.0 enforces checks on permitted characters in a given character set which MySQL 5.7 does not; this is a known issue. This means that, prior to attempting to upgrade, you should ensure that no comments contain characters that are not defined for the character set in use. You can fix this in either of two ways:
	- Change the character set to one that includes the character or characters in question.
	- Remove the offending character or characters.
	The preceding applies to table, file, and index comments.
- **Incompatible change**: As of MySQL 8.0.11, it is prohibited to start the server with a [`lower_case_table_names`](server-system-variables.md) setting that is different from the setting used when the server was initialized. The restriction is necessary because collations used by various data dictionary table fields are based on the [`lower_case_table_names`](server-system-variables.md) setting that was defined when the server was initialized, and restarting the server with a different setting would introduce inconsistencies with respect to how identifiers are ordered and compared.

### Server Changes

- In MySQL 8.0.11, several deprecated features related to account management have been removed, such as use of the [`GRANT`](grant.md) statement to modify nonprivilege characteristics of user accounts, the `NO_AUTO_CREATE_USER` SQL mode, the `PASSWORD()` function, and the `old_passwords` system variable.
	Replication from MySQL 5.7 to 8.0 of statements that refer to these removed features can cause replication failure. Applications that use any of the removed features should be revised to avoid them and use alternatives when possible, as described in [Features Removed in MySQL 8.0](mysql-nutshell.md).
	To avoid a startup failure on MySQL 8.0, remove any instance of `NO_AUTO_CREATE_USER` from [`sql_mode`](server-system-variables.md) system variable settings in MySQL option files.
	Loading a dump file that includes the `NO_AUTO_CREATE_USER` SQL mode in stored program definitions into a MySQL 8.0 server causes a failure. As of MySQL 5.7.24 and MySQL 8.0.13, [**mysqldump**](mysqldump.md) removes `NO_AUTO_CREATE_USER` from stored program definitions. Dump files created with an earlier version of `mysqldump` must be modified manually to remove instances of `NO_AUTO_CREATE_USER`.
- In MySQL 8.0.11, these deprecated compatibility SQL modes were removed: `DB2`, `MAXDB`, `MSSQL`, `MYSQL323`, `MYSQL40`, `ORACLE`, `POSTGRESQL`, `NO_FIELD_OPTIONS`, `NO_KEY_OPTIONS`, `NO_TABLE_OPTIONS`. They can no longer be assigned to the `sql_mode` system variable or used as permitted values for the [**mysqldump**](mysqldump.md) [`--compatible`](mysqldump.md) option.
	Removal of `MAXDB` means that the `TIMESTAMP` data type for [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) is no longer treated as [`DATETIME`](datetime.md).
	Replication from MySQL 5.7 to 8.0 of statements that refer to the removed SQL modes can cause replication failure. This includes replication of `CREATE` statements for stored programs (stored procedures and functions, triggers, and events) that are executed while the current [`sql_mode`](server-system-variables.md) value includes any of the removed modes. Applications that use any of the removed modes should be revised to avoid them.
- The text of many MySQL 8.0 error messages has been revised and improved to provide more and better information than in MySQL 5.7. If your application depends on specific content or formatting of error messages, you should test these and be prepared to update the application accordingly prior to performing an upgrade.
- As of MySQL 8.0.3, spatial data types permit an `SRID` attribute, to explicitly indicate the spatial reference system (SRS) for values stored in the column. See [Section 13.4.1, “Spatial Data Types”](spatial-type-overview.md).
	A spatial column with an explicit `SRID` attribute is SRID-restricted: The column takes only values with that ID, and `SPATIAL` indexes on the column become subject to use by the optimizer. The optimizer ignores `SPATIAL` indexes on spatial columns with no `SRID` attribute. See [Section 10.3.3, “SPATIAL Index Optimization”](spatial-index-optimization.md). If you want the optimizer to consider `SPATIAL` indexes on spatial columns that are not SRID-restricted, each such column should be modified:
	- Verify that all values within the column have the same SRID. To determine the SRIDs contained in a geometry column *`col_name`*, use the following query:
		```
		SELECT DISTINCT ST_SRID(col_name) FROM tbl_name;
		```
		If the query returns more than one row, the column contains a mix of SRIDs. In that case, modify its contents so all values have the same SRID.
	- Redefine the column to have an explicit `SRID` attribute.
	- Recreate the `SPATIAL` index.
- Several spatial functions were removed in MySQL 8.0.0 due to a spatial function namespace change that implemented an `ST_` prefix for functions that perform an exact operation, or an `MBR` prefix for functions that perform an operation based on minimum bounding rectangles. The use of removed spatial functions in generated column definitions could cause an upgrade failure. Before upgrading, run [**mysqlcheck --check-upgrade**](mysqlcheck.md) for removed spatial functions and replace any that you find with their `ST_` or `MBR` named replacements. For a list of removed spatial functions, refer to [Features Removed in MySQL 8.0](mysql-nutshell.md).
- The [`BACKUP_ADMIN`](privileges-provided.md) privilege is automatically granted to users with the [`RELOAD`](privileges-provided.md) privilege when performing an in-place upgrade to MySQL 8.0.3 or higher.
- From MySQL 8.0.13, because of differences between row-based or mixed replication mode and statement-based replication mode in the way that temporary tables are handled, there are new restrictions on switching the binary logging format at runtime.
	- `SET @@SESSION.binlog_format` cannot be used if the session has any open temporary tables.
	- `SET @@global.binlog_format` and `SET @@persist.binlog_format` cannot be used if any replication channel has any open temporary tables. `SET                   @@persist_only.binlog_format` is allowed if replication channels have open temporary tables, because unlike `PERSIST`, `PERSIST_ONLY` does not modify the runtime global system variable value.
	- `SET @@global.binlog_format` and `SET @@persist.binlog_format` cannot be used if any replication channel applier is running. This is because the change only takes effect on a replication channel when its applier is restarted, at which time the replication channel might have open temporary tables. This behavior is more restrictive than before. `SET                   @@persist_only.binlog_format` is allowed if any replication channel applier is running.
	- From MySQL 8.0.27, configuring a session setting for [`internal_tmp_mem_storage_engine`](server-system-variables.md) requires the [`SESSION_VARIABLES_ADMIN`](privileges-provided.md) or [`SYSTEM_VARIABLES_ADMIN`](privileges-provided.md) privilege.
	- As of MySQL 8.0.27, the clone plugin permits concurrent DDL operations on the donor MySQL Server instance while a cloning operation is in progress. Previously, a backup lock was held during the cloning operation, preventing concurrent DDL on the donor. To revert to the previous behavior of blocking concurrent DDL on the donor during a clone operation, enable the [`clone_block_ddl`](clone-plugin-options-variables.md) variable. See [Section 7.6.7.4, “Cloning and Concurrent DDL”](clone-plugin-concurrent-ddl.md).
- From MySQL 8.0.30, error log components listed in the [`log_error_services`](server-system-variables.md) value at startup are loaded implicitly early in the MySQL Server startup sequence. If you have previously installed loadable error log components using [`INSTALL             COMPONENT`](install-component.md) and you list those components in a [`log_error_services`](server-system-variables.md) setting that is read at startup (from an option file, for example), your configuration should be updated to avoid startup warnings. For more information, see [Error Log Configuration Methods](error-log-configuration.md).

### InnoDB Changes

- [`INFORMATION_SCHEMA`](information-schema.md) views based on `InnoDB` system tables were replaced by internal system views on data dictionary tables. Affected `InnoDB` [`INFORMATION_SCHEMA`](information-schema.md) views were renamed:
	**Table 3.1 Renamed InnoDB Information Schema Views**
	| Old Name | New Name |
	| --- | --- |
	| `INNODB_SYS_COLUMNS` | `INNODB_COLUMNS` |
	| `INNODB_SYS_DATAFILES` | `INNODB_DATAFILES` |
	| `INNODB_SYS_FIELDS` | `INNODB_FIELDS` |
	| `INNODB_SYS_FOREIGN` | `INNODB_FOREIGN` |
	| `INNODB_SYS_FOREIGN_COLS` | `INNODB_FOREIGN_COLS` |
	| `INNODB_SYS_INDEXES` | `INNODB_INDEXES` |
	| `INNODB_SYS_TABLES` | `INNODB_TABLES` |
	| `INNODB_SYS_TABLESPACES` | `INNODB_TABLESPACES` |
	| `INNODB_SYS_TABLESTATS` | `INNODB_TABLESTATS` |
	| `INNODB_SYS_VIRTUAL` | `INNODB_VIRTUAL` |
	After upgrading to MySQL 8.0.3 or higher, update any scripts that reference previous `InnoDB` [`INFORMATION_SCHEMA`](information-schema.md) view names.
- The [zlib library](http://www.zlib.net/) version bundled with MySQL was raised from version 1.2.3 to version 1.2.11.
	The zlib `compressBound()` function in zlib 1.2.11 returns a slightly higher estimate of the buffer size required to compress a given length of bytes than it did in zlib version 1.2.3. The `compressBound()` function is called by `InnoDB` functions that determine the maximum row size permitted when creating compressed `InnoDB` tables or inserting and updating rows in compressed `InnoDB` tables. As a result, [`CREATE TABLE             ... ROW_FORMAT=COMPRESSED`](create-table.md), [`INSERT`](insert.md), and [`UPDATE`](update.md) operations with row sizes very close to the maximum row size that were successful in earlier releases could now fail. To avoid this issue, test [`CREATE TABLE`](create-table.md) statements for compressed `InnoDB` tables with large rows on a MySQL 8.0 test instance prior to upgrading.
- With the introduction of the [`--innodb-directories`](innodb-parameters.md) feature, the location of file-per-table and general tablespace files created with an absolute path or in a location outside of the data directory should be added to the [`innodb_directories`](innodb-parameters.md) argument value. Otherwise, `InnoDB` is not able to locate these files during recovery. To view tablespace file locations, query the Information Schema [`FILES`](information-schema-files-table.md) table:
	```
	SELECT TABLESPACE_NAME, FILE_NAME FROM INFORMATION_SCHEMA.FILES \G
	```
- Undo logs can no longer reside in the system tablespace. In MySQL 8.0, undo logs reside in two undo tablespaces by default. For more information, see [Section 17.6.3.4, “Undo Tablespaces”](innodb-undo-tablespaces.md).
	When upgrading from MySQL 5.7 to MySQL 8.0, any undo tablespaces that exist in the MySQL 5.7 instance are removed and replaced by two new default undo tablespaces. Default undo tablespaces are created in the location defined by the [`innodb_undo_directory`](innodb-parameters.md) variable. If the [`innodb_undo_directory`](innodb-parameters.md) variable is undefined, undo tablespaces are created in the data directory. Upgrade from MySQL 5.7 to MySQL 8.0 requires a slow shutdown which ensures that undo tablespaces in the MySQL 5.7 instance are empty, permitting them to be removed safely.
	When upgrading to MySQL 8.0.14 or later from an earlier MySQL 8.0 release, undo tablespaces that exist in the pre-upgrade instance as a result of an [`innodb_undo_tablespaces`](innodb-parameters.md) setting greater than 2 are treated as user-defined undo tablespaces, which can be deactivated and dropped using [`ALTER UNDO             TABLESPACE`](alter-tablespace.md) and [`DROP UNDO             TABLESPACE`](drop-tablespace.md) syntax, respectively, after upgrading. Upgrade within the MySQL 8.0 release series may not always require a slow shutdown which means that existing undo tablespaces could contain undo logs. Therefore, existing undo tablespaces are not removed by the upgrade process.
- **Incompatible change**: As of MySQL 8.0.17, the [`CREATE             TABLESPACE ... ADD DATAFILE`](create-tablespace.md) clause does not permit circular directory references. For example, the circular directory reference (`/../`) in the following statement is not permitted:
	```
	CREATE TABLESPACE ts1 ADD DATAFILE ts1.ibd 'any_directory/../ts1.ibd';
	```
	An exception to the restriction exists on Linux, where a circular directory reference is permitted if the preceding directory is a symbolic link. For example, the data file path in the example above is permitted if *`any_directory`* is a symbolic link. (It is still permitted for data file paths to begin with '`../` '.)
	To avoid upgrade issues, remove any circular directory references from tablespace data file paths before upgrading to MySQL 8.0.17 or higher. To inspect tablespace paths, query the Information Schema [`INNODB_DATAFILES`](information-schema-innodb-datafiles-table.md) table.
- Due to a regression introduced in MySQL 8.0.14, in-place upgrade on a case-sensitive file system from MySQL 5.7 or a MySQL 8.0 release prior to MySQL 8.0.14 to MySQL 8.0.16 failed for instances with partitioned tables and [`lower_case_table_names=1`](server-system-variables.md). The failure was caused by a case mismatch issue related to partitioned table file names. The fix that introduced the regression was reverted, which permits upgrades to MySQL 8.0.17 from MySQL 5.7 or MySQL 8.0 releases prior to MySQL 8.0.14 to function as normal. However, the regression is still present in the MySQL 8.0.14, 8.0.15, and 8.0.16 releases.
	In-place upgrade on a case-sensitive file system from MySQL 8.0.14, 8.0.15, or 8.0.16 to MySQL 8.0.17 fails with the following error when starting the server after upgrading binaries or packages to MySQL 8.0.17 if partitioned tables are present and [`lower_case_table_names=1`](server-system-variables.md):
	```
	Upgrading from server version version_number with
	partitioned tables and lower_case_table_names == 1 on a case sensitive file
	system may cause issues, and is therefore prohibited. To upgrade anyway, restart
	the new server version with the command line option 'upgrade=FORCE'. When
	upgrade is completed, please execute 'RENAME TABLE part_table_name
	TO new_table_name; RENAME TABLE new_table_name
	TO part_table_name;' for each of the partitioned tables.
	Please see the documentation for further information.
	```
	If you encounter this error when upgrading to MySQL 8.0.17, perform the following workaround:
	1. Restart the server with [`--upgrade=force`](server-options.md) to force the upgrade operation to proceed.
	2. Identify partitioned table file names with lowercase partition name delimiters `(#p#` or `#sp#`):
		```
		mysql> SELECT FILE_NAME FROM INFORMATION_SCHEMA.FILES WHERE FILE_NAME LIKE '%#p#%' OR FILE_NAME LIKE '%#sp#%';
		```
	3. For each file identified, rename the associated table using a temporary name, then rename the table back to its original name.
		```
		mysql> RENAME TABLE table_name TO temporary_table_name;
		mysql> RENAME TABLE temporary_table_name TO table_name;
		```
	4. Verify that there are no partitioned table file names lowercase partition name delimiters (an empty result set should be returned).
		```
		mysql> SELECT FILE_NAME FROM INFORMATION_SCHEMA.FILES WHERE FILE_NAME LIKE '%#p#%' OR FILE_NAME LIKE '%#sp#%';
		Empty set (0.00 sec)
		```
	5. Run [`ANALYZE TABLE`](analyze-table.md) on each renamed table to update the optimizer statistics in the `mysql.innodb_index_stats` and `mysql.innodb_table_stats` tables.
	Because of the regression still present in the MySQL 8.0.14, 8.0.15, and 8.0.16 releases, importing partitioned tables from MySQL 8.0.14, 8.0.15, or 8.0.16 to MySQL 8.0.17 is not supported on case-sensitive file systems where [`lower_case_table_names=1`](server-system-variables.md). Attempting to do so results in a “Tablespace is missing for table” error.
- MySQL uses delimiter strings when constructing tablespace names and file names for table partitions. A “ `#p#` ” delimiter string precedes partition names, and an “ `#sp#` ” delimiter string precedes subpartition names, as shown:
	```
	schema_name.table_name#p#partition_name#sp#subpartition_name
	table_name#p#partition_name#sp#subpartition_name.ibd
	```
	Historically, delimiter strings have been uppercase (`#P#` and `#SP#`) on case-sensitive file systems such as Linux, and lowercase (`#p#` and `#sp#`) on case-insensitive file systems such as Windows. As of MySQL 8.0.19, delimiter strings are lowercase on all file systems. This change prevents issues when migrating data directories between case-sensitive and case-insensitive file systems. Uppercase delimiter strings are no longer used.
	Additionally, partition tablespace names and file names generated based on user-specified partition or subpartition names, which can be specified in uppercase or lowercase, are now generated (and stored internally) in lowercase regardless of the [`lower_case_table_names`](server-system-variables.md) setting to ensure case-insensitivity. For example, if a table partition is created with the name `PART_1`, the tablespace name and file name are generated in lowercase:
	```
	schema_name.table_name#p#part_1
	table_name#p#part_1.ibd
	```
	During upgrade, MySQL checks and modifies if necessary:
	- Partition file names on disk and in the data dictionary to ensure lowercase delimiters and partition names.
	- Partition metadata in the data dictionary for related issues introduced by previous bug fixes.
	- `InnoDB` statistics data for related issues introduced by previous bug fixes.
	During tablespace import operations, partition tablespace file names on disk are checked and modified if necessary to ensure lowercase delimiters and partition names.
- As of MySQL 8.0.21, a warning is written to the error log at startup or when upgrading from MySQL 5.7 if tablespace data files are found to reside in unknown directories. Known directories are those defined by the [`datadir`](server-system-variables.md), [`innodb_data_home_dir`](innodb-parameters.md), and [`innodb_directories`](innodb-parameters.md) variables. To make a directory known, add it to the [`innodb_directories`](innodb-parameters.md) setting. Making directories known ensures that data files can be found during recovery. For more information, see [Tablespace Discovery During Crash Recovery](innodb-recovery.md).
- **Important change**: From MySQL 8.0.30, the [`innodb_redo_log_capacity`](innodb-parameters.md) variable controls the amount of disk space occupied by redo log files. With this change, the default number of redo log files and their location has also changed. From MySQL 8.0.30, `InnoDB` maintains 32 redo log files in the `#innodb_redo` directory in the data directory. Previously, `InnoDB` created two redo log files in the data directory by default, and the number and size of redo log files were controlled by the [`innodb_log_files_in_group`](innodb-parameters.md) and [`innodb_log_file_size`](innodb-parameters.md) variables. These two variables are now deprecated.
	When the [`innodb_redo_log_capacity`](innodb-parameters.md) setting is defined, [`innodb_log_files_in_group`](innodb-parameters.md) and [`innodb_log_file_size`](innodb-parameters.md) settings are ignored; otherwise, those settings are used to compute the `innodb_redo_log_capacity` setting (`innodb_log_files_in_group` \* `innodb_log_file_size` = `innodb_redo_log_capacity`). If none of those variables are set, redo log capacity is set to the `innodb_redo_log_capacity` default value, which is 104857600 bytes (100MB).
	As is generally required for any upgrade, this change requires a clean shutdown before upgrading.
	For more information about this feature, see [Section 17.6.5, “Redo Log”](innodb-redo-log.md).
- Before MySQL 5.7.35, there was no size limitation for indexes in tables with redundant or compact row format. As of MySQL 5.7.35, the limit is 767 bytes. An upgrade from a MySQL version before 5.7.35 to MySQL 8.0 can produce inaccessible tables. If a table with redundant or compact row format has an index larger than 767 bytes, drop the index and re-create it before an upgrade to MySQL 8.0. The error message is:
	```
	mysql> ERROR 1709 (HY000): Index column size too large. The maximum column size is 767 bytes.
	```

### SQL Changes

- **Incompatible change**: As of MySQL 8.0.13, the deprecated `ASC` or `DESC` qualifiers for `GROUP             BY` clauses have been removed. Queries that previously relied on `GROUP BY` sorting may produce results that differ from previous MySQL versions. To produce a given sort order, provide an `ORDER             BY` clause.
	Queries and stored program definitions from MySQL 8.0.12 or lower that use `ASC` or `DESC` qualifiers for `GROUP             BY` clauses should be amended. Otherwise, upgrading to MySQL 8.0.13 or higher may fail, as may replicating to MySQL 8.0.13 or higher replica servers.
- Some keywords may be reserved in MySQL 8.0 that were not reserved in MySQL 5.7. See [Section 11.3, “Keywords and Reserved Words”](keywords.md). This can cause words previously used as identifiers to become illegal. To fix affected statements, use identifier quoting. See [Section 11.2, “Schema Object Names”](identifiers.md).
- After upgrading, it is recommended that you test optimizer hints specified in application code to ensure that the hints are still required to achieve the desired optimization strategy. Optimizer enhancements can sometimes render certain optimizer hints unnecessary. In some cases, an unnecessary optimizer hint may even be counterproductive.
- **Incompatible change**: In MySQL 5.7, specifying a `FOREIGN KEY` definition for an `InnoDB` table without a ``CONSTRAINT *`symbol`*             `` clause, or specifying the `CONSTRAINT` keyword without a `symbol`, causes `InnoDB` to use a generated constraint name. That behavior changed in MySQL 8.0, with `InnoDB` using the ``FOREIGN KEY *`index_name`*             `` value instead of a generated name. Because constraint names must be unique per schema (database), the change caused errors due to foreign key index names that were not unique per schema. To avoid such errors, the new constraint naming behavior has been reverted in MySQL 8.0.16, and `InnoDB` once again uses a generated constraint name.
	For consistency with `InnoDB`, `NDB` releases based on MySQL 8.0.16 or higher use a generated constraint name if the ``CONSTRAINT *`symbol`*             `` clause is not specified, or the `CONSTRAINT` keyword is specified without a `symbol`. `NDB` releases based on MySQL 5.7 and earlier MySQL 8.0 releases used the ``FOREIGN KEY *`index_name`*             `` value.
	The changes described above may introduce incompatibilities for applications that depend on the previous foreign key constraint naming behavior.
- The handling of system variable values by MySQL flow control functions such as [`IFNULL()`](flow-control-functions.md) and [`CASE()`](flow-control-functions.md) changed in MySQL 8.0.22; system variable values are now handled as column values of the same character and collation, rather than as constants. Some queries using these functions with system variables that were previously successful may subsequently be rejected with Illegal mix of collations. In such cases, cast the system variable to the correct character set and collation.
- **Incompatible change**: MySQL 8.0.28 fixes an issue in previous MySQL 8.0 releases whereby the [`CONVERT()`](cast-functions.md) function sometimes allowed invalid casts of [`BINARY`](binary-varbinary.md) values to nonbinary character sets. Applications which may have relied on this behavior should be checked and if necessary modified prior to upgrade.
	In particular, where `CONVERT()` was used as part of an expression for an indexed generated column, the change in the function's behavior may result in index corruption following an upgrade to MySQL 8.0.28. You can prevent this from happening by following these steps:
	1. Prior to performing the upgrade, correct any invalid input data.
	2. Drop and then re-create the index.
		You can also force a table rebuild using [``ALTER TABLE                 *`table`* FORCE``](alter-table.md), instead.
	3. Upgrade the MySQL software.
	If you cannot validate the input data beforehand, you should not re-create the index or rebuild the table until after you perform the upgrade to MySQL 8.0.28.

### Changed Server Defaults

MySQL 8.0 comes with improved defaults, aiming at the best out of the box experience possible. These changes are driven by the fact that technology is advancing (machines have more CPUS, use SSDs and so on), more data is being stored, MySQL is evolving (InnoDB, Group Replication, AdminAPI), and so on. The following table summarizes the defaults which have been changed to provide the best MySQL experience for the majority of users.

| Option/Parameter | Old Default | New Default |
| --- | --- | --- |
| *Server changes* |  |  |
| [`character_set_server`](server-system-variables.md) | latin1 | utf8mb4 |
| [`collation_server`](server-system-variables.md) | latin1\_swedish\_ci | utf8mb4\_0900\_ai\_ci |
| [`explicit_defaults_for_timestamp`](server-system-variables.md) | OFF | ON |
| [`optimizer_trace_max_mem_size`](server-system-variables.md) | 16KB | 1MB |
| [`validate_password_check_user_name`](validate-password-options-variables.md) | OFF | ON |
| [`back_log`](server-system-variables.md) | \-1 (autosize) changed from: back\_log = 50 + (max\_connections / 5) | \-1 (autosize) changed to: back\_log = max\_connections |
| [`max_allowed_packet`](server-system-variables.md) | 4194304 (4MB) | 67108864 (64MB) |
| [`max_error_count`](server-system-variables.md) | 64 | 1024 |
| [`event_scheduler`](server-system-variables.md) | OFF | ON |
| [`table_open_cache`](server-system-variables.md) | 2000 | 4000 |
| [`log_error_verbosity`](server-system-variables.md) | 3 (Notes) | 2 (Warning) |
| [`local_infile`](server-system-variables.md) | ON (5.7) | OFF |
| *InnoDB changes* |  |  |
| [`innodb_undo_tablespaces`](innodb-parameters.md) | 0 | 2 |
| [`innodb_undo_log_truncate`](innodb-parameters.md) | OFF | ON |
| [`innodb_flush_method`](innodb-parameters.md) | NULL | fsync (Unix), unbuffered (Windows) |
| [`innodb_autoinc_lock_mode`](innodb-parameters.md) | 1 (consecutive) | 2 (interleaved) |
| [`innodb_flush_neighbors`](innodb-parameters.md) | 1 (enable) | 0 (disable) |
| [`innodb_max_dirty_pages_pct_lwm`](innodb-parameters.md) | 0 (%) | 10 (%) |
| [`innodb_max_dirty_pages_pct`](innodb-parameters.md) | 75 (%) | 90 (%) |
| *Performance Schema changes* |  |  |
| `performance-schema-instrument='wait/lock/metadata/sql/%=ON'` | OFF | ON |
| `performance-schema-instrument='memory/%=COUNTED'` | OFF | COUNTED |
| `performance-schema-consumer-events-transactions-current=ON` | OFF | ON |
| `performance-schema-consumer-events-transactions-history=ON` | OFF | ON |
| `performance-schema-instrument='transaction%=ON'` | OFF | ON |
| *Replication changes* |  |  |
| [`log_bin`](replication-options-binary-log.md) | OFF | ON |
| [`server_id`](replication-options.md) | 0 | 1 |
| [`log-slave-updates`](replication-options-binary-log.md) | OFF | ON |
| [`expire_logs_days`](replication-options-binary-log.md) | 0 | 30 |
| [`master-info-repository`](replication-options-replica.md) | FILE | TABLE |
| [`relay-log-info-repository`](replication-options-replica.md) | FILE | TABLE |
| [`transaction-write-set-extraction`](replication-options-binary-log.md) | OFF | XXHASH64 |
| [`slave_rows_search_algorithms`](replication-options-replica.md) | INDEX\_SCAN, TABLE\_SCAN | INDEX\_SCAN, HASH\_SCAN |
| [`slave_pending_jobs_size_max`](replication-options-replica.md) | 16M | 128M |
| [`gtid_executed_compression_period`](replication-options-gtids.md) | 1000 | 0 |
| *Group Replication changes* |  |  |
| [`group_replication_autorejoin_tries`](group-replication-system-variables.md) | 0 | 3 |
| [`group_replication_exit_state_action`](group-replication-system-variables.md) | ABORT\_SERVER | READ\_ONLY |
| [`group_replication_member_expel_timeout`](group-replication-system-variables.md) | 0 | 5 |

For more information about options or variables which have been added, see [Option and Variable Changes for MySQL 8.0](https://dev.mysql.com/doc/mysqld-version-reference/en/optvar-changes-8-0.html), in the *MySQL Server Version Reference*.

The following sections explain the changes to defaults and any impact they might have on your deployment.

**Server Defaults**

- The default value of the [`character_set_server`](server-system-variables.md) system variable and command line option [`--character-set-server`](server-system-variables.md) changed from `latin1` to `utf8mb4`. This is the server’s default character set. At this time, UTF8MB4 is the dominant character encoding for the web, and this change makes life easier for the vast majority of MySQL users. The upgrade from 5.7 to 8.0 does not change the character set for any existing database objects, but, unless you set `character_set_server` explicitly (either back to the previous value, or to a new one), a new schema uses `utf8mb4` by default. We recommend that you move to `utf8mb4` whenever possible.
- The default value of the [`collation_server`](server-system-variables.md) system variable and command line argument [`--collation-server`](server-system-variables.md) changed from `latin1_swedish_ci` to `utf8mb4_0900_ai_ci`. This is the server’s default collation, the ordering of characters in a character set. There is a link between collations and character sets as each character set comes with a list of possible collations. The upgrade from 5.7 to 8.0 does not change any collation for any existing database objects, but takes effect for new objects.
- The default value of the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable changed from `OFF` (MySQL legacy behavior) to `ON` (SQL standard behavior). This option was originally introduced in 5.6 and was `OFF` in 5.6 and 5.7.
- The default value of the [`optimizer_trace_max_mem_size`](server-system-variables.md) system variable changed from `16KB` to `1MB`. The old default caused the optimizer trace to be truncated for any non-trivial query. This change ensures useful optimizer traces for most queries.
- The default value of the [`validate_password_check_user_name`](validate-password-options-variables.md) system variable changed from `OFF` to `ON`. This means that when the `validate_password` plugin is enabled, by default it now rejects passwords that match the current session user name.
- The autosize algorithm for the [`back_log`](server-system-variables.md) system variable has changed. The value for autosize (-1) is now set to the value of [`max_connections`](server-system-variables.md), which is bigger than the calculated by `50 +             (max_connections / 5)`. The `back_log` queues up incoming IP connect requests in situations where the server is not able to keep up with incoming requests. In the worst case, with [`max_connections`](server-system-variables.md) number of clients trying to reconnect at the same time, for example after a network failure, they can all be buffered and reject-retry loops are avoided.
- The default value of the [`max_allowed_packet`](server-system-variables.md) system variable changed from `4194304` (4M) to `67108864` (64M). The main advantage with this larger default is less chance of receiving errors about an insert or query being larger than `max_allowed_packet`. It should be as big as the largest [Section 13.3.4, “The BLOB and TEXT Types”](blob.md) you want to use. To revert to the previous behavior, set `max_allowed_packet=4194304`.
- The default value of the [`max_error_count`](server-system-variables.md) system variable changed from `64` to `1024`. This ensures that MySQL handles a larger number of warnings, such as an UPDATE statement that touches 1000s of rows and many of them give conversion warnings. It is common for many tools to batch updates, to help reduce replication lag. External tools such as pt-online-schema-change defaults to 1000, and gh-ost defaults to 100. MySQL 8.0 covers full error history for these two use cases. There are no static allocations, so this change only affects memory consumption for statements that generate lots of warnings.
- The default value of the [`event_scheduler`](server-system-variables.md) system variable changed from `OFF` to `ON`. In other words, the event scheduler is enabled by default. This is an enabler for new features in SYS, for example “kill idle transactions”.
- The default value of the [`table_open_cache`](server-system-variables.md) system variable changed from `2000` to `4000`. This is a minor change which increases session concurrency on table access.
- The default value of the [`log_error_verbosity`](server-system-variables.md) system variable changed from `3` (Notes) to `2` (Warning). The purpose is to make the MySQL 8.0 error log less verbose by default.

**InnoDB Defaults**

- **Incompatible change** The default value of the [`innodb_undo_tablespaces`](innodb-parameters.md) system variable changed from `0` to `2`. The configures the number of undo tablespaces used by InnoDB. In MySQL 8.0 the minimum value for [`innodb_undo_tablespaces`](innodb-parameters.md) is 2 and rollback segments cannot be created in the system tablespace anymore. Thus, this is a case where you cannot revert back to 5.7 behavior. The purpose of this change is to be able to auto-truncate Undo logs (see next item), reclaiming disk space used by (occasional) long transactions such as a [**mysqldump**](mysqldump.md).
- The default value of the [`innodb_undo_log_truncate`](innodb-parameters.md) system variable changed from `OFF` to `ON`. When enabled, undo tablespaces that exceed the threshold value defined by [`innodb_max_undo_log_size`](innodb-parameters.md) are marked for truncation. Only undo tablespaces can be truncated. Truncating undo logs that reside in the system tablespace is not supported. An upgrade from 5.7 to 8.0 automatically converts your system to use undo tablespaces, using the system tablespace is not an option in 8.0.
- The default value of the [`innodb_flush_method`](innodb-parameters.md) system variable changed from `NULL` to `fsync` on Unix-like systems and from `NULL` to `unbuffered` on Windows systems. This is more of a terminology and option cleanup without any tangible impact. For Unix this is just a documentation change as the default was `fsync` also in 5.7 (the default `NULL` meant `fsync`). Similarly on Windows, [`innodb_flush_method`](innodb-parameters.md) default `NULL` meant `async_unbuffered` in 5.7, and is replaced by default `unbuffered` in 8.0, which in combination with the existing default [`innodb_use_native_aio=ON`](innodb-parameters.md) has the same effect.
- **Incompatible change** The default value of the [`innodb_autoinc_lock_mode`](innodb-parameters.md) system variable changed from `1` (consecutive) to `2` (interleaved). The change to interleaved lock mode as the default setting reflects the change from statement-based to row-based replication as the default replication type, which occurred in MySQL 5.7. *Statement-based replication* requires the consecutive auto-increment lock mode to ensure that auto-increment values are assigned in a predictable and repeatable order for a given sequence of SQL statements, whereas *row-based replication* is not sensitive to the execution order of SQL statements. Thus, this change is known to be incompatible with statement based replication, and may break some applications or user-generated test suites that depend on sequential auto increment. The previous default can be restored by setting `innodb_autoinc_lock_mode=1;`
- The default value of the [`innodb_flush_neighbors`](innodb-parameters.md) system variable changes from `1` (enable) to `0` (disable). This is done because fast IO (SSDs) is now the default for deployment. We expect that for the majority of users, this results in a small performance gain. Users who are using slower hard drives may see a performance loss, and are encouraged to revert to the previous defaults by setting `innodb_flush_neighbors=1`.
- The default value of the [`innodb_max_dirty_pages_pct_lwm`](innodb-parameters.md) system variable changed from `0` (%) to `10` (%). With `innodb_max_dirty_pages_pct_lwm=10`, InnoDB increases its flushing activity when >10% of the buffer pool contains modified (‘dirty’) pages. The purpose of this change is to trade off peak throughput slightly, in exchange for more consistent performance.
- The default value of the [`innodb_max_dirty_pages_pct`](innodb-parameters.md) system variable changed from `75` (%) to `90` (%). This change combines with the change to [`innodb_max_dirty_pages_pct_lwm`](innodb-parameters.md) and together they ensure a smooth InnoDB flushing behavior, avoiding flushing bursts. To revert to the previous behavior, set `innodb_max_dirty_pages_pct=75` and `innodb_max_dirty_pages_pct_lwm=0`.

**Performance Schema Defaults**

- Performance Schema Meta Data Locking (MDL) instrumentation is turned on by default. The compiled default for `performance-schema-instrument='wait/lock/metadata/sql/%=ON'` changed from `OFF` to `ON`. This is an enabler for adding MDL oriented views in SYS.
- Performance Schema Memory instrumentation is turned on by default. The compiled default for `performance-schema-instrument='memory/%=COUNTED'` changed from `OFF` to `COUNTED`. This is important because the accounting is incorrect if instrumentation is enabled after server start, and you could get a negative balance from missing an allocation, but catching a free.
- Performance Schema Transaction instrumentation is turned on by default. The compiled default for `performance-schema-consumer-events-transactions-current=ON`, `performance-schema-consumer-events-transactions-history=ON`, and `performance-schema-instrument='transaction%=ON'` changed from `OFF` to `ON`.

**Replication Defaults**

- The default value of the [`log_bin`](replication-options-binary-log.md) system variable changed from `OFF` to `ON`. In other words, binary logging is enabled by default. Nearly all production installations have the binary log enabled as it is used for replication and point-in-time recovery. Thus, by enabling binary log by default we eliminate one configuration step, enabling it later requires a [**mysqld**](mysqld.md) restart. Enabling it by default also provides better test coverage and it becomes easier to spot performance regressions. Remember to also set [`server_id`](replication-options.md) (see following change). The 8.0 default behavior is as if you issued `./mysqld --log-bin --server-id=1`. If you are on 8.0 and want 5.7 behavior you can issue `./mysqld --skip-log-bin             --server-id=0`.
- The default value of the [`server_id`](replication-options.md) system variable changed from `0` to `1` (combines with the change to [`log_bin=ON`](replication-options-binary-log.md)). The server can be started with this default ID, but in practice you must set the [`server-id`](replication-options.md) according to the replication infrastructure being deployed, to avoid having duplicate server ids.
- The default value of the [`log-slave-updates`](replication-options-binary-log.md) system variable changed from `OFF` to `ON`. This causes a replica to log replicated events into its own binary log. This option is required for Group Replication, and also ensures correct behavior in various replication chain setups, which have become the norm today.
- The default value of the [`expire_logs_days`](replication-options-binary-log.md) system variable changed from `0` to `30`. The new default `30` causes [**mysqld**](mysqld.md) to periodically purge unused binary logs that are older than 30 days. This change helps prevent excessive amounts of disk space being wasted on binary logs that are no longer needed for replication or recovery purposes. The old value of `0` disables any automatic binary log purges.
- The default value of the [`master_info_repository`](replication-options-replica.md) and [`relay_log_info_repository`](replication-options-replica.md) system variables change from `FILE` to `TABLE`. Thus in 8.0, replication metadata is stored in InnoDB by default. This increases reliability to try and achieve crash safe replication by default.
- The default value of the [`transaction-write-set-extraction`](replication-options-binary-log.md) system variable changed from `OFF` to `XXHASH64`. This change enables transaction write sets by default. By using Transaction Write Sets, the source has to do slightly more work to generate the write sets, but the result is helpful in conflict detection. This is a requirement for Group Replication and the new default makes it easy to enable binary log writeset parallelization on the source to speed up replication.
- The default value of the [`slave_rows_search_algorithms`](replication-options-replica.md) system variable changed from `INDEX_SCAN,TABLE_SCAN` to `INDEX_SCAN,HASH_SCAN`. This change speeds up row-based replication by reducing the number of table scans the replica applier has to do to apply the changes to a table without a primary key.
- The default value of the [`slave_pending_jobs_size_max`](replication-options-replica.md) system variable changed from `16M` to `128M`. This change increases the amount of memory available to multithreaded replicas.
- The default value of the [`gtid_executed_compression_period`](replication-options-gtids.md) system variable changed from `1000` to `0`. This change ensures that compression of the `mysql.gtid_executed` table only occurs implicitly as required.

**Group Replication Defaults**

- The default value of [`group_replication_autorejoin_tries`](group-replication-system-variables.md) changed from 0 to 3, which means that automatic rejoin is enabled by default. This system variable specifies the number of tries that a member makes to automatically rejoin the group if it is expelled, or if it is unable to contact a majority of the group before the [`group_replication_unreachable_majority_timeout`](group-replication-system-variables.md) setting is reached.
- The default value of [`group_replication_exit_state_action`](group-replication-system-variables.md) changed from `ABORT_SERVER` to `READ_ONLY`. This means that when a member exits the group, for example after a network failure, the instance becomes read-only, rather than being shut down.
- The default value of [`group_replication_member_expel_timeout`](group-replication-system-variables.md) changed from 0 to 5, meaning that a member suspected of having lost contact with the group is liable for expulsion 5 seconds after the 5-second detection period.

Most of these defaults are reasonably good for both development and production environments. An exception to this is the [`--innodb-dedicated-server`](innodb-parameters.md) option, whose default value remains `OFF`, although we recommend `ON` for production environments. The reason for defaulting to `OFF` is that it causes shared environments such as developer laptops to become unusable, because it takes *all* the memory it can find.

For production environments we recommend using [`--innodb-dedicated-server`](innodb-parameters.md), which determines values for the following InnoDB variables (if not specified explicitly), based on available memory: [`innodb_buffer_pool_size`](innodb-parameters.md), [`innodb_log_file_size`](innodb-parameters.md), and [`innodb_flush_method`](innodb-parameters.md). See [Section 17.8.12, “Enabling Automatic InnoDB Configuration for a Dedicated MySQL Server”](innodb-dedicated-server.md).

Although the new defaults are the best configuration choices for most use cases, there are special cases, as well as legacy reasons for using existing 5.7 configuration choices. For example, some people prefer to upgrade to 8.0 with as few changes to their applications or operational environment as possible. We recommend to evaluate all the new defaults and use as many as you can. Most new defaults can be tested in 5.7, so you can validate the new defaults in 5.7 production before upgrading to 8.0. For the few defaults where you need your old 5.7 value, set the corresponding configuration variable or startup option in your operational environment.

MySQL 8.0 has the Performance Schema [`variables_info`](performance-schema-variables-info-table.md) table, which shows for each system variable the source from which it was most recently set, as well as its range of values. This provides SQL access to all there is to know about a configuration variable and its values.

### Valid Performance Regressions

Performance regressions are expected between MySQL versions 5.7 and 8.0. MySQL 8.0 has more features, changes default values, is more robust, and adds security functionality and additional diagnostic information. Listed here are valid reasons for regressions between these versions which includes potential mediation options. This is not an exhaustive list.

Changes related to default values changing between MySQL versions 5.7 and 8.0:

- [Binary logs](binary-log.md) are disabled by default in 5.7, and enabled by default in 8.0.
	*Mediation*: Disable binary logging by specifying the [`--skip-log-bin`](replication-options-binary-log.md) or [`--disable-log-bin`](replication-options-binary-log.md) option at startup.
- The default character set changed from `latin1` to `utf8mb4` in 8.0. While `utf8mb4` performs significantly better in 8.0 than it did in 5.7, `latin1` is faster than `utf8mb4`.
	*Mediation*: Use `latin1` in 8.0 if `utf8mb4` is not needed.

[Transactional Data Dictionary](data-dictionary.md) (atomic DDL) was introduced in 8.0.

- This increases robustness/reliability at the expense of DDL performance (CREATE / DROP intensive loads), but it should not impact the DML load (SELECT / INSERT / UPDATE / DELETE).
	*Mediation*: None

The more modern [TLS ciphers/algorithms](encrypted-connections.md) used as of 5.7.28 has an effect when TLS (SSL) is enabled (the default):

- Before MySQL 5.7.28, MySQL uses the yaSSL library for the community edition and OpenSSL for the enterprise edition.
	As of MySQL 5.7.28, MySQL only uses OpenSSL with its stronger TLS ciphers, which are more costly in terms of performance.
	Upgrading to MySQL 8.0 from MySQL 5.7.28 or earlier can cause a TLS performance regression.
	*Mediation*: None (if TLS is required for security reasons)

[Performance Schema (PFS)](performance-schema.md) instrumentation is much wider in 8.0 than in 5.7:

- PFS cannot be compiled out in MySQL 8.0 but it can be turned off. Some performance schema instrumentation will still exist even when turned off, but overhead will be smaller.
	*Mediation*: Set performance\_schema = OFF in 8.0, or turn off performance schema instrumentation at finer granularity if some but not all PFS functionality is needed.

Truncating undo tablespaces is enabled by default in 8.0 which can significantly impact performance:

- Historically InnoDB stored undo logs in the system tablespace but there was no way to reclaim space used by undo log. The system tablespace would only grow and not shrink, and this inspired feature requests to remedy this.
	MySQL 8.0 moved the undo log to separate tablespaces which allows both manual and automatic undo log truncation.
	However, auto-truncation has a permanent performance overhead and it can potentially cause stalls.
	*Mediation*: Set innodb\_undo\_log\_truncate = OFF in 8.0, and manually truncate undo logs as needed. For related information, see [Truncating Undo Tablespaces](innodb-undo-tablespaces.md).

The character classes `[[:alpha:]]` or `[[:digit:]]` do not perform as well with regular expression functions such as `REGEXP()` and `RLIKE()` in MySQL 8.0 as they did in MySQL 5.7. This is due to the replacement in MySQL 8.0 of the Spencer regular expression library with the ICU library, which uses UTF-16 internally.

*Mediation*: In place of `[[:alpha:]]`, use `[a-zA-Z]`; in place of `[[:digit:]]`, use `[0-9]`.
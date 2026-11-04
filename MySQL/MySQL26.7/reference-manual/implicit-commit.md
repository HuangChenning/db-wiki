---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.3.3 Statements That Cause an Implicit Commit"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/implicit-commit.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.3.3 Statements That Cause an Implicit Commit

The statements listed in this section (and any synonyms for them) implicitly end any transaction active in the current session, as if you had done a [`COMMIT`](commit.md) before executing the statement.

Most of these statements also cause an implicit commit after executing. The intent is to handle each such statement in its own special transaction. Transaction-control and locking statements are exceptions: If an implicit commit occurs before execution, another does not occur after.

- **Data definition language (DDL) statements that define or modify database objects.** [`ALTER EVENT`](alter-event.md), [`ALTER FUNCTION`](alter-function.md), [`ALTER PROCEDURE`](alter-procedure.md), [`ALTER SERVER`](alter-server.md), [`ALTER TABLE`](alter-table.md), [`ALTER TABLESPACE`](alter-tablespace.md), [`ALTER VIEW`](alter-view.md), [`CREATE DATABASE`](create-database.md), [`CREATE EVENT`](create-event.md), [`CREATE FUNCTION`](create-function.md), [`CREATE INDEX`](create-index.md), [`CREATE PROCEDURE`](create-procedure.md), [`CREATE ROLE`](create-role.md), [`CREATE SERVER`](create-server.md), [`CREATE SPATIAL REFERENCE           SYSTEM`](create-spatial-reference-system.md), [`CREATE TABLE`](create-table.md), [`CREATE TABLESPACE`](create-tablespace.md), [`CREATE TRIGGER`](create-trigger.md), [`CREATE VIEW`](create-view.md), [`DROP DATABASE`](drop-database.md), [`DROP EVENT`](drop-event.md), [`DROP FUNCTION`](drop-function.md), [`DROP INDEX`](drop-index.md), [`DROP PROCEDURE`](drop-procedure.md), [`DROP ROLE`](drop-role.md), [`DROP SERVER`](drop-server.md), [`DROP SPATIAL REFERENCE SYSTEM`](drop-spatial-reference-system.md), [`DROP TABLE`](drop-table.md), [`DROP TABLESPACE`](drop-tablespace.md), [`DROP TRIGGER`](drop-trigger.md), [`DROP VIEW`](drop-view.md), [`INSTALL PLUGIN`](install-plugin.md), [`RENAME TABLE`](rename-table.md), [`TRUNCATE TABLE`](truncate-table.md), [`UNINSTALL PLUGIN`](uninstall-plugin.md).
	[`CREATE TABLE`](create-table.md) and [`DROP TABLE`](drop-table.md) statements do not commit a transaction if the `TEMPORARY` keyword is used. (This does not apply to other operations on temporary tables such as [`ALTER           TABLE`](alter-table.md) and [`CREATE           INDEX`](create-index.md), which do cause a commit.) However, although no implicit commit occurs, neither can the statement be rolled back, which means that the use of such statements causes transactional atomicity to be violated. For example, if you use [`CREATE           TEMPORARY TABLE`](create-table.md) and then roll back the transaction, the table remains in existence.
	The [`CREATE TABLE`](create-table.md) statement in `InnoDB` is processed as a single transaction. This means that a [`ROLLBACK`](commit.md) from the user does not undo [`CREATE           TABLE`](create-table.md) statements the user made during that transaction.
	[`CREATE TABLE ...           SELECT`](create-table.md) causes an implicit commit before and after the statement is executed when you are creating nontemporary tables. (No commit occurs for `CREATE TEMPORARY TABLE           ... SELECT`.)
- **Statements that implicitly use or modify tables in the `mysql` database.** [`ALTER USER`](alter-user.md), [`CREATE USER`](create-user.md), [`DROP USER`](drop-user.md), [`GRANT`](grant.md), [`RENAME USER`](rename-user.md), [`REVOKE`](revoke.md), [`SET PASSWORD`](set-password.md).
- **Transaction-control and locking statements.** [`BEGIN`](commit.md), [`LOCK TABLES`](lock-tables.md), `SET           autocommit = 1` (if the value is not already 1), [`START           TRANSACTION`](commit.md), [`UNLOCK           TABLES`](lock-tables.md).
	[`UNLOCK           TABLES`](lock-tables.md) commits a transaction only if any tables currently have been locked with [`LOCK           TABLES`](lock-tables.md) to acquire nontransactional table locks. A commit does not occur for [`UNLOCK           TABLES`](lock-tables.md) following [`FLUSH TABLES           WITH READ LOCK`](flush.md) because the latter statement does not acquire table-level locks.
	Transactions cannot be nested. This is a consequence of the implicit commit performed for any current transaction when you issue a [`START           TRANSACTION`](commit.md) statement or one of its synonyms.
	Statements that cause an implicit commit cannot be used in an XA transaction while the transaction is in an `ACTIVE` state.
	The [`BEGIN`](commit.md) statement differs from the use of the `BEGIN` keyword that starts a [`BEGIN ...           END`](begin-end.md) compound statement. The latter does not cause an implicit commit. See [Section 15.6.1, “BEGIN... END Compound Statement”](begin-end.md).
- **Data loading statements.** [`LOAD DATA`](load-data.md). [`LOAD DATA`](load-data.md) causes an implicit commit only for tables using the [`NDB`](mysql-cluster.md) storage engine.
- **Administrative statements.** [`ANALYZE TABLE`](analyze-table.md), [`CACHE INDEX`](cache-index.md), [`CHECK TABLE`](check-table.md), [`FLUSH`](flush.md), [`LOAD INDEX INTO           CACHE`](load-index.md), [`OPTIMIZE           TABLE`](optimize-table.md), [`REPAIR TABLE`](repair-table.md), [`RESET`](reset.md) (but not [`RESET PERSIST`](reset-persist.md)).
- **Replication control statements**. [`START           REPLICA`](start-replica.md), [`STOP           REPLICA`](stop-replica.md), [`RESET           REPLICA`](reset-replica.md), [`CHANGE REPLICATION           SOURCE TO`](change-replication-source-to.md).
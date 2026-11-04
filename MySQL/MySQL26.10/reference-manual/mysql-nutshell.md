---
title: "MySQL :: MySQL 26.10 Reference Manual :: 1.4 What Is New in MySQL 26.10"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-nutshell.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 1.4 What Is New in MySQL 26.10

This section summarizes what has been added to, deprecated in, changed, and removed from MySQL 26.10 since MySQL 9.7. A companion section lists MySQL server options and variables that have been added, deprecated, or removed in MySQL 26.10; see [Section 1.5, “Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 26.10”](added-deprecated-removed.md).

### Features Added or Changed in MySQL 26.10

The following features have been added to MySQL 26.10:

- **Four-part exact release identity.** MySQL Server now exposes an exact release identity in `MAJOR.MINOR.PATCH.UPDATE` form so that separately delivered updates on the same patch line can be distinguished. The update component is always present on update-aware interfaces, including when its value is 0. Use [`VERSION_WITH_UPDATE()`](information-functions.md), the [`version_with_update`](server-system-variables.md) system variable, or `mysqld --version-with-update` to obtain the full value. Existing interfaces such as `VERSION()`, `version`, and `mysqld --version` continue to return the three-part compatibility version. The `mysql_upgrade_history` audit file records exact-release transitions in a nested `update_history` array without changing compatibility checks.
	See [mysql\_upgrade\_history File](data-directory.md) for more information.
- **Granular concurrency and update control for JSON duality views.** `JSON_DUALITY_OBJECT() ` now supports the CHECK and NO CHECK annotations at table and column level, and the `UPDATE` and `NO               UPDATE` annotations at column level. These annotations determine which projected columns participate in `ETAG` calculation and which fields can be modified through the view. Column settings inherit from their table unless explicitly overridden. The [`JSON_DUALITY_VIEW_COLUMNS`](information-schema-json-duality-view-columns-table.md) Information Schema table exposes the effective settings using `ALLOW_CHECK` and `ALLOW_UPDATE`.

### Features Deprecated in MySQL 26.10

The following features are deprecated in MySQL 26.10 and may be removed in a future series. Where alternatives are shown, applications should be updated to use them.

For applications that use features deprecated in MySQL 26.10 that have been removed in a later MySQL version, statements may fail when replicated from a MySQL 26.10 source to a replica running a later version, or may have different effects on source and replica. To avoid such problems, applications that use features deprecated in 26.10 should be revised to avoid them and use alternatives when possible.

- **SCRAM-SHA-1 authentication.** The `SCRAM-SHA-1` authentication method for SASL LDAP authentication is deprecated as of MySQL 9.5.0. Use `SCRAM-SHA-256` instead; this is also now the default value for [`authentication_ldap_sasl_auth_method_name`](pluggable-authentication-system-variables.md).
	See [Section 8.4.1.6, “LDAP Pluggable Authentication”](ldap-pluggable-authentication.md), for more information.

### Features Removed in MySQL 26.10

The following items are obsolete and have been removed in MySQL 26.10. Where alternatives are shown, applications should be updated to use them.

For MySQL 9.7 applications that use features removed in MySQL 26.10, statements may fail when replicated from a MySQL 9.7 source to a MySQL 26.10 replica, or may have different effects on source and replica. To avoid such problems, applications that use features removed in MySQL 26.10 should be revised to avoid them and use alternatives when possible.

- **Server system and status variables removed.** Server system and status variables removed in MySQL 26.10 are shown in the following list:
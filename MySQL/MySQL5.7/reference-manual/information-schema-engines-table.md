---
title: "24.3.7 The INFORMATION_SCHEMA ENGINES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-engines-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.7 The INFORMATION\_SCHEMA ENGINES Table

The `ENGINES` table provides information about storage engines. This is particularly useful for checking whether a storage engine is supported, or to see what the default engine is.

The `ENGINES` table has these columns:

- `ENGINE`
	The name of the storage engine.
- `SUPPORT`
	The server's level of support for the storage engine, as shown in the following table.
	| Value | Meaning |
	| --- | --- |
	| `YES` | The engine is supported and is active |
	| `DEFAULT` | Like `YES`, plus this is the default engine |
	| `NO` | The engine is not supported |
	| `DISABLED` | The engine is supported but has been disabled |
	A value of `NO` means that the server was compiled without support for the engine, so it cannot be enabled at runtime.
	A value of `DISABLED` occurs either because the server was started with an option that disables the engine, or because not all options required to enable it were given. In the latter case, the error log should contain a reason indicating why the option is disabled. See [Section 5.4.2, “The Error Log”](error-log.md).
	You might also see `DISABLED` for a storage engine if the server was compiled to support it, but was started with a ``--skip-*`engine_name`*`` option. For the [`NDB`](mysql-cluster.md) storage engine, `DISABLED` means the server was compiled with support for NDB Cluster, but was not started with the [`--ndbcluster`](mysql-cluster-options-variables.md) option.
	All MySQL servers support `MyISAM` tables. It is not possible to disable `MyISAM`.
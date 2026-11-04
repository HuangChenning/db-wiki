---
title: "5.6.1 Installing and Uninstalling Loadable Functions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/function-loading.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.6.1 Installing and Uninstalling Loadable Functions

Loadable functions, as the name implies, must be loaded into the server before they can be used. MySQL supports automatic function loading during server startup and manual loading thereafter.

While a loadable function is loaded, information about it is available as described in [Section 5.6.2, “Obtaining Information About Loadable Functions”](obtaining-loadable-function-information.md).

#### Installing Loadable Functions

To load a loadable function manually, use the [`CREATE         FUNCTION`](create-function-loadable.md) statement. For example:

```
CREATE FUNCTION metaphon
  RETURNS STRING
  SONAME 'udf_example.so';
```

The file base name depends on your platform. Common suffixes are `.so` for Unix and Unix-like systems, `.dll` for Windows.

[`CREATE         FUNCTION`](create-function-loadable.md) has these effects:

- It loads the function into the server to make it available immediately.
- It registers the function in the `mysql.func` system table to make it persistent across server restarts. For this reason, [`CREATE             FUNCTION`](create-function-loadable.md) requires the [`INSERT`](privileges-provided.md) privilege for the `mysql` system database.

Automatic loading of loadable functions occurs during the normal server startup sequence. The server loads functions registered in the `mysql.func` table. If the server is started with the [`--skip-grant-tables`](server-options.md) option, functions registered in the table are not loaded and are unavailable.

#### Uninstalling Loadable Functions

To remove a loadable function, use the [`DROP         FUNCTION`](drop-function-loadable.md) statement. For example:

```
DROP FUNCTION metaphon;
```

[`DROP         FUNCTION`](drop-function-loadable.md) has these effects:

- It unloads the function to make it unavailable.
- It removes the function from the `mysql.func` system table. For this reason, [`DROP             FUNCTION`](drop-function-loadable.md) requires the [`DELETE`](privileges-provided.md) privilege for the `mysql` system database. With the function no longer registered in the `mysql.func` table, the server does not load the function during subsequent restarts.

While a loadable function is loaded, information about it is available from the `mysql.func` system table. See [Section 5.6.2, “Obtaining Information About Loadable Functions”](obtaining-loadable-function-information.md). [`CREATE         FUNCTION`](create-function-loadable.md) adds the function to the table and [`DROP         FUNCTION`](drop-function-loadable.md) removes it.

#### Reinstalling or Upgrading Loadable Functions

To reinstall or upgrade the shared library associated with a loadable function, issue a [`DROP         FUNCTION`](drop-function-loadable.md) statement, upgrade the shared library, and then issue a [`CREATE         FUNCTION`](create-function-loadable.md) statement. If you upgrade the shared library first and then use [`DROP         FUNCTION`](drop-function-loadable.md), the server may unexpectedly shut down.
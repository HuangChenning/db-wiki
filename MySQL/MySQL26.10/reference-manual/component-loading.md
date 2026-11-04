---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.5.1 Installing and Uninstalling Components"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/component-loading.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.5.1 Installing and Uninstalling Components

Components must be loaded into the server before they can be used. MySQL supports manual component loading at runtime and automatic loading during server startup.

While a component is loaded, information about it is available as described in [Section 7.5.2, “Obtaining Component Information”](obtaining-component-information.md).

The [`INSTALL COMPONENT`](install-component.md) and [`UNINSTALL COMPONENT`](uninstall-component.md) SQL statements enable component loading and unloading. For example:

```sql
INSTALL COMPONENT 'file://component_validate_password';
UNINSTALL COMPONENT 'file://component_validate_password';
```

A loader service handles component loading and unloading, and also registers loaded components in the `mysql.component` system table.

Components are loaded in the server locally (not replicated).

The SQL statements for component manipulation affect server operation and the `mysql.component` system table as follows:

- [`INSTALL COMPONENT`](install-component.md) loads components into the server. The components become active immediately. The loader service also registers loaded components in the `mysql.component` system table. For subsequent server restarts, the loader service loads any components listed in `mysql.component` during the startup sequence. This occurs even if the server is started with the [`--skip-grant-tables`](server-options.md) option. The optional `SET` clause permits setting component system-variable values when you install components.
- [`UNINSTALL COMPONENT`](uninstall-component.md) deactivates components and unloads them from the server. The loader service also unregisters the components from the `mysql.component` system table so that the server no longer loads them during its startup sequence for subsequent restarts.

Compared to the corresponding [`INSTALL       PLUGIN`](install-plugin.md) statement for server plugins, the [`INSTALL COMPONENT`](install-component.md) statement for components offers the significant advantage that it is not necessary to know any platform-specific file name suffix for naming the component. This means that a given [`INSTALL COMPONENT`](install-component.md) statement can be executed uniformly across platforms.

A component when installed may also automatically install related loadable functions. If so, the component when uninstalled also automatically uninstalls those functions.
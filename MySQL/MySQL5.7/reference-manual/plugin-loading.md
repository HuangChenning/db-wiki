---
title: "5.5.1 Installing and Uninstalling Plugins"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/plugin-loading.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.5.1 Installing and Uninstalling Plugins

Server plugins must be loaded into the server before they can be used. MySQL supports plugin loading at server startup and runtime. It is also possible to control the activation state of loaded plugins at startup, and to unload them at runtime.

While a plugin is loaded, information about it is available as described in [Section 5.5.2, “Obtaining Server Plugin Information”](obtaining-plugin-information.md).

#### Installing Plugins

Before a server plugin can be used, it must be installed using one of the following methods. In the descriptions, *`plugin_name`* stands for a plugin name such as `innodb`, `csv`, or `validate_password`.

##### Built-in Plugins

A built-in plugin is known by the server automatically. By default, the server enables the plugin at startup. Some built-in plugins permit this to be changed with the ``--*`plugin_name`*[=*`activation_state`*]`` option.

##### Plugins Registered in the mysql.plugin System Table

The `mysql.plugin` system table serves as a registry of plugins (other than built-in plugins, which need not be registered). During the normal startup sequence, the server loads plugins registered in the table. By default, for a plugin loaded from the `mysql.plugin` table, the server also enables the plugin. This can be changed with the ``--*`plugin_name`*[=*`activation_state`*]`` option.

If the server is started with the [`--skip-grant-tables`](server-options.md) option, plugins registered in the `mysql.plugin` table are not loaded and are unavailable.

##### Plugins Named with Command-Line Options

A plugin located in a plugin library file can be loaded at server startup with the [`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), or [`--early-plugin-load`](server-options.md) option. Normally, for a plugin loaded at startup, the server also enables the plugin. This can be changed with the ``--*`plugin_name`*[=*`activation_state`*]`` option.

The [`--plugin-load`](server-options.md) and [`--plugin-load-add`](server-options.md) options load plugins after built-in plugins and storage engines have initialized during the server startup sequence. The [`--early-plugin-load`](server-options.md) option is used to load plugins that must be available prior to initialization of built-in plugins and storage engines.

The value of each plugin-loading option is a semicolon-separated list of *`plugin_library`* and *`name`* `=` *`plugin_library`* values. Each *`plugin_library`* is the name of a library file that contains plugin code, and each *`name`* is the name of a plugin to load. If a plugin library is named without any preceding plugin name, the server loads all plugins in the library. With a preceding plugin name, the server loads only the named plugin from the libary. The server looks for plugin library files in the directory named by the [`plugin_dir`](server-system-variables.md) system variable.

Plugin-loading options do not register any plugin in the `mysql.plugin` table. For subsequent restarts, the server loads the plugin again only if [`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), or [`--early-plugin-load`](server-options.md) is given again. That is, the option produces a one-time plugin-installation operation that persists for a single server invocation.

[`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), and [`--early-plugin-load`](server-options.md) enable plugins to be loaded even when [`--skip-grant-tables`](server-options.md) is given (which causes the server to ignore the `mysql.plugin` table). [`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), and [`--early-plugin-load`](server-options.md) also enable plugins to be loaded at startup that cannot be loaded at runtime.

The [`--plugin-load-add`](server-options.md) option complements the [`--plugin-load`](server-options.md) option:

- Each instance of [`--plugin-load`](server-options.md) resets the set of plugins to load at startup, whereas [`--plugin-load-add`](server-options.md) adds a plugin or plugins to the set of plugins to be loaded without resetting the current set. Consequently, if multiple instances of [`--plugin-load`](server-options.md) are specified, only the last one applies. With multiple instances of [`--plugin-load-add`](server-options.md), all of them apply.
- The argument format is the same as for [`--plugin-load`](server-options.md), but multiple instances of [`--plugin-load-add`](server-options.md) can be used to avoid specifying a large set of plugins as a single long unwieldy [`--plugin-load`](server-options.md) argument.
- [`--plugin-load-add`](server-options.md) can be given in the absence of [`--plugin-load`](server-options.md), but any instance of [`--plugin-load-add`](server-options.md) that appears before [`--plugin-load`](server-options.md) has no effect because [`--plugin-load`](server-options.md) resets the set of plugins to load.

For example, these options:

```
--plugin-load=x --plugin-load-add=y
```

are equivalent to these options:

```
--plugin-load-add=x --plugin-load-add=y
```

and are also equivalent to this option:

```
--plugin-load="x;y"
```

But these options:

```
--plugin-load-add=y --plugin-load=x
```

are equivalent to this option:

```
--plugin-load=x
```

##### Plugins Installed with the INSTALL PLUGIN Statement

A plugin located in a plugin library file can be loaded at runtime with the [`INSTALL PLUGIN`](install-plugin.md) statement. The statement also registers the plugin in the `mysql.plugin` table to cause the server to load it on subsequent restarts. For this reason, [`INSTALL PLUGIN`](install-plugin.md) requires the [`INSERT`](privileges-provided.md) privilege for the `mysql.plugin` table.

The plugin library file base name depends on your platform. Common suffixes are `.so` for Unix and Unix-like systems, `.dll` for Windows.

Example: The [`--plugin-load-add`](server-options.md) option installs a plugin at server startup. To install a plugin named `myplugin` from a plugin library file named `somepluglib.so`, use these lines in a `my.cnf` file:

```
[mysqld]
plugin-load-add=myplugin=somepluglib.so
```

In this case, the plugin is not registered in `mysql.plugin`. Restarting the server without the [`--plugin-load-add`](server-options.md) option causes the plugin not to be loaded at startup.

Alternatively, the [`INSTALL PLUGIN`](install-plugin.md) statement causes the server to load the plugin code from the library file at runtime:

```
INSTALL PLUGIN myplugin SONAME 'somepluglib.so';
```

[`INSTALL PLUGIN`](install-plugin.md) also causes “permanent” plugin registration: The plugin is listed in the `mysql.plugin` table to ensure that the server loads it on subsequent restarts.

Many plugins can be loaded either at server startup or at runtime. However, if a plugin is designed such that it must be loaded and initialized during server startup, attempts to load it at runtime using [`INSTALL         PLUGIN`](install-plugin.md) produce an error:

```
mysql> INSTALL PLUGIN myplugin SONAME 'somepluglib.so';
ERROR 1721 (HY000): Plugin 'myplugin' is marked as not dynamically
installable. You have to stop the server to install it.
```

In this case, you must use [`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), or [`--early-plugin-load`](server-options.md).

If a plugin is named both using a [`--plugin-load`](server-options.md), [`--plugin-load-add`](server-options.md), or [`--early-plugin-load`](server-options.md) option and (as a result of an earlier [`INSTALL         PLUGIN`](install-plugin.md) statement) in the `mysql.plugin` table, the server starts but writes these messages to the error log:

```
[ERROR] Function 'plugin_name' already exists
[Warning] Couldn't load plugin named 'plugin_name'
with soname 'plugin_object_file'.
```

#### Controlling Plugin Activation State

If the server knows about a plugin when it starts (for example, because the plugin is named using a [`--plugin-load-add`](server-options.md) option or is registered in the `mysql.plugin` table), the server loads and enables the plugin by default. It is possible to control activation state for such a plugin using a ``--*`plugin_name`*[=*`activation_state`*]`` startup option, where *`plugin_name`* is the name of the plugin to affect, such as `innodb`, `csv`, or `validate_password`. As with other options, dashes and underscores are interchangeable in option names. Also, activation state values are not case-sensitive. For example, `--my_plugin=ON` and `--my-plugin=on` are equivalent.

- ``--*`plugin_name`*=OFF``
	Tells the server to disable the plugin. This may not be possible for certain built-in plugins, such as `mysql_native_password`.
- ``--*`plugin_name`*[=ON]``
	Tells the server to enable the plugin. (Specifying the option as ``--*`plugin_name`*`` without a value has the same effect.) If the plugin fails to initialize, the server runs with the plugin disabled.
- ``--*`plugin_name`*=FORCE``
	Tells the server to enable the plugin, but if plugin initialization fails, the server does not start. In other words, this option forces the server to run with the plugin enabled or not at all.
- ``--*`plugin_name`*=FORCE_PLUS_PERMANENT``
	Like `FORCE`, but in addition prevents the plugin from being unloaded at runtime. If a user attempts to do so with [`UNINSTALL PLUGIN`](uninstall-plugin.md), an error occurs.

Plugin activation states are visible in the `LOAD_OPTION` column of the Information Schema [`PLUGINS`](information-schema-plugins-table.md) table.

Suppose that `CSV`, `BLACKHOLE`, and `ARCHIVE` are built-in pluggable storage engines and that you want the server to load them at startup, subject to these conditions: The server is permitted to run if `CSV` initialization fails, must require that `BLACKHOLE` initialization succeeds, and should disable `ARCHIVE`. To accomplish that, use these lines in an option file:

```
[mysqld]
csv=ON
blackhole=FORCE
archive=OFF
```

The ``--enable-*`plugin_name`*`` option format is a synonym for ``--*`plugin_name`*=ON``. The ``--disable-*`plugin_name`*`` and ``--skip-*`plugin_name`*`` option formats are synonyms for ``--*`plugin_name`*=OFF``.

If a plugin is disabled, either explicitly with `OFF` or implicitly because it was enabled with `ON` but fails to initialize, aspects of server operation that require the plugin change. For example, if the plugin implements a storage engine, existing tables for the storage engine become inaccessible, and attempts to create new tables for the storage engine result in tables that use the default storage engine unless the [`NO_ENGINE_SUBSTITUTION`](sql-mode.md) SQL mode is enabled to cause an error to occur instead.

Disabling a plugin may require adjustment to other options. For example, if you start the server using [`--skip-innodb`](innodb-parameters.md) to disable [`InnoDB`](innodb-storage-engine.md), other ``innodb_*`xxx`*`` options likely need to be omitted at startup. In addition, because [`InnoDB`](innodb-storage-engine.md) is the default storage engine, it cannot start unless you specify another available storage engine with [`--default_storage_engine`](server-system-variables.md). You must also set [`--default_tmp_storage_engine`](server-system-variables.md).

#### Uninstalling Plugins

At runtime, the [`UNINSTALL PLUGIN`](uninstall-plugin.md) statement disables and uninstalls a plugin known to the server. The statement unloads the plugin and removes it from the `mysql.plugin` system table, if it is registered there. For this reason, [`UNINSTALL PLUGIN`](uninstall-plugin.md) statement requires the [`DELETE`](privileges-provided.md) privilege for the `mysql.plugin` table. With the plugin no longer registered in the table, the server does not load the plugin during subsequent restarts.

[`UNINSTALL PLUGIN`](uninstall-plugin.md) can unload a plugin regardless of whether it was loaded at runtime with [`INSTALL PLUGIN`](install-plugin.md) or at startup with a plugin-loading option, subject to these conditions:

- It cannot unload plugins that are built in to the server. These can be identified as those that have a library name of `NULL` in the output from [`INFORMATION_SCHEMA.PLUGINS`](information-schema-plugins-table.md) or [`SHOW PLUGINS`](show-plugins.md).
- It cannot unload plugins for which the server was started with ``--*`plugin_name`*=FORCE_PLUS_PERMANENT``, which prevents plugin unloading at runtime. These can be identified from the `LOAD_OPTION` column of the Information Schema [`PLUGINS`](information-schema-plugins-table.md) table.

To uninstall a plugin that currently is loaded at server startup with a plugin-loading option, use this procedure.

1. Remove from the `my.cnf` file any options related to the plugin.
2. Restart the server.
3. Plugins normally are installed using either a plugin-loading option at startup or with [`INSTALL             PLUGIN`](install-plugin.md) at runtime, but not both. However, removing options for a plugin from the `my.cnf` file may not be sufficient to uninstall it if at some point [`INSTALL PLUGIN`](install-plugin.md) has also been used. If the plugin still appears in the output from [`INFORMATION_SCHEMA.PLUGINS`](information-schema-plugins-table.md) or [`SHOW PLUGINS`](show-plugins.md), use [`UNINSTALL PLUGIN`](uninstall-plugin.md) to remove it from the `mysql.plugin` table. Then restart the server again.
---
title: "7.9.3 The LOCK_ORDER Tool"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/lock-order-tool.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.9.3 The LOCK\_ORDER Tool

The MySQL server is a multithreaded application that uses numerous internal locking and lock-related primitives, such as mutexes, rwlocks (including prlocks and sxlocks), conditions, and files. Within the server, the set of lock-related objects changes with implementation of new features and code refactoring for performance improvements. As with any multithreaded application that uses locking primitives, there is always a risk of encountering a deadlock during execution when multiple locks are held at once. For MySQL, the effect of a deadlock is catastrophic, causing a complete loss of service.

To enable detection of lock-acquisition deadlocks and enforcement that runtime execution is free of them, MySQL supports `LOCK_ORDER` tooling. This enables a lock-order dependency graph to be defined as part of server design, and server runtime checking to ensure that lock acquisition is acyclic and that execution paths comply with the graph.

This section provides information about using the `LOCK_ORDER` tool, but only at a basic level. For complete details, see the Lock Order section of the MySQL Server Doxygen documentation, available at [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html).

The `LOCK_ORDER` tool is intended for debugging the server, not for production use.

To use the `LOCK_ORDER` tool, follow this procedure:

1. Build MySQL from source, configuring it with the [`-DWITH_LOCK_ORDER=ON`](source-configuration-options.md) **CMake** option so that the build includes `LOCK_ORDER` tooling.
	Note
	With the [`WITH_LOCK_ORDER`](source-configuration-options.md) option enabled, MySQL builds require the **flex** program.
2. To run the server with the `LOCK_ORDER` tool enabled, enable the `lock_order` system variable at server startup. Several other system variables for `LOCK_ORDER` configuration are available as well.
3. For MySQL test suite operation, **mysql-test-run.pl** has a `--lock-order` option that controls whether to enable the `LOCK_ORDER` tool during test case execution.

The system variables described following configure operation of the `LOCK_ORDER` tool, assuming that MySQL has been built to include `LOCK_ORDER` tooling. The primary variable is `lock_order`, which indicates whether to enable the `LOCK_ORDER` tool at runtime:

- If `lock_order` is disabled (the default), no other `LOCK_ORDER` system variables have any effect.
- If `lock_order` is enabled, the other system variables configure which `LOCK_ORDER` features to enable.

Note

In general, it is intended that the `LOCK_ORDER` tool be configured by executing **mysql-test-run.pl** with the `--lock-order` option, and for **mysql-test-run.pl** to set `LOCK_ORDER` system variables to appropriate values.

All `LOCK_ORDER` system variables must be set at server startup. At runtime, their values are visible but cannot be changed.

Some system variables exist in pairs, such as `lock_order_debug_loop` and `lock_order_trace_loop`. For such pairs, the variables are distinguished as follows when the condition occurs with which they are associated:

- If the `_debug_` variable is enabled, a debug assertion is raised.
- If the `_trace_` variable is enabled, an error is printed to the logs.

**Table 7.8 LOCK\_ORDER System Variable Summary**

| Variable Name | Variable Type | Variable Scope |
| --- | --- | --- |
| lock\_order | Boolean | Global |
| lock\_order\_debug\_loop | Boolean | Global |
| lock\_order\_debug\_missing\_arc | Boolean | Global |
| lock\_order\_debug\_missing\_key | Boolean | Global |
| lock\_order\_debug\_missing\_unlock | Boolean | Global |
| lock\_order\_dependencies | File name | Global |
| lock\_order\_extra\_dependencies | File name | Global |
| lock\_order\_output\_directory | Directory name | Global |
| lock\_order\_print\_txt | Boolean | Global |
| lock\_order\_trace\_loop | Boolean | Global |
| lock\_order\_trace\_missing\_arc | Boolean | Global |
| lock\_order\_trace\_missing\_key | Boolean | Global |
| lock\_order\_trace\_missing\_unlock | Boolean | Global |

- `lock_order`
	| Command-Line Format | `--lock-order[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether to enable the `LOCK_ORDER` tool at runtime. If `lock_order` is disabled (the default), no other `LOCK_ORDER` system variables have any effect. If `lock_order` is enabled, the other system variables configure which `LOCK_ORDER` features to enable.
	If `lock_order` is enabled, an error is raised if the server encounters a lock-acquisition sequence that is not declared in the lock-order graph.
- `lock_order_debug_loop`
	| Command-Line Format | `--lock-order-debug-loop[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_debug_loop` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool causes a debug assertion failure when it encounters a dependency that is flagged as a loop in the lock-order graph.
- `lock_order_debug_missing_arc`
	| Command-Line Format | `--lock-order-debug-missing-arc[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_debug_missing_arc` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the LOCK\_ORDER tool causes a debug assertion failure when it encounters a dependency that is not declared in the lock-order graph.
- `lock_order_debug_missing_key`
	| Command-Line Format | `--lock-order-debug-missing-key[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_debug_missing_key` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool causes a debug assertion failure when it encounters an object that is not properly instrumented with the Performance Schema.
- `lock_order_debug_missing_unlock`
	| Command-Line Format | `--lock-order-debug-missing-unlock[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_debug_missing_unlock` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool causes a debug assertion failure when it encounters a lock that is destroyed while still held.
- `lock_order_dependencies`
	| Command-Line Format | `--lock-order-dependencies=file_name` |
	| --- | --- |
	| System Variable | `lock_order_dependencies` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | File name |
	| Default Value | `empty string` |
	The path to the `lock_order_dependencies.txt` file that defines the server lock-order dependency graph.
	It is permitted to specify no dependencies. An empty dependency graph is used in this case.
- `lock_order_extra_dependencies`
	| Command-Line Format | `--lock-order-extra-dependencies=file_name` |
	| --- | --- |
	| System Variable | `lock_order_extra_dependencies` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | File name |
	| Default Value | `empty string` |
	The path to a file containing additional dependencies for the lock-order dependency graph. This is useful to amend the primary server dependency graph, defined in the `lock_order_dependencies.txt` file, with additional dependencies describing the behavior of third party code. (The alternative is to modify `lock_order_dependencies.txt` itself, which is not encouraged.)
	If this variable is not set, no secondary file is used.
- `lock_order_output_directory`
	| Command-Line Format | `--lock-order-output-directory=dir_name` |
	| --- | --- |
	| System Variable | `lock_order_output_directory` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Directory name |
	| Default Value | `empty string` |
	The directory where the `LOCK_ORDER` tool writes its logs. If this variable is not set, the default is the current directory.
- `lock_order_print_txt`
	| Command-Line Format | `--lock-order-print-txt[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_print_txt` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool performs a lock-order graph analysis and prints a textual report. The report includes any lock-acquisition cycles detected.
- `lock_order_trace_loop`
	| Command-Line Format | `--lock-order-trace-loop[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_trace_loop` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool prints a trace in the log file when it encounters a dependency that is flagged as a loop in the lock-order graph.
- `lock_order_trace_missing_arc`
	| Command-Line Format | `--lock-order-trace-missing-arc[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_trace_missing_arc` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `ON` |
	Whether the `LOCK_ORDER` tool prints a trace in the log file when it encounters a dependency that is not declared in the lock-order graph.
- `lock_order_trace_missing_key`
	| Command-Line Format | `--lock-order-trace-missing-key[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_trace_missing_key` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Whether the `LOCK_ORDER` tool prints a trace in the log file when it encounters an object that is not properly instrumented with the Performance Schema.
- `lock_order_trace_missing_unlock`
	| Command-Line Format | `--lock-order-trace-missing-unlock[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `lock_order_trace_missing_unlock` |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `ON` |
	Whether the `LOCK_ORDER` tool prints a trace in the log file when it encounters a lock that is destroyed while still held.
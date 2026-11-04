---
title: "MySQL :: MySQL 26.10 Reference Manual :: 17.8.13 Enabling Automatic InnoDB Configuration for a Dedicated MySQL Server"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/innodb-dedicated-server.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 17.8.13 Enabling Automatic InnoDB Configuration for a Dedicated MySQL Server

When the server is started with [`--innodb-dedicated-server`](innodb-parameters.md), `InnoDB` automatically calculates values for and sets the following system variables:

You should consider using `--innodb-dedicated-server` only if the MySQL instance resides on a dedicated server where it can use all available system resources—for example, if you run MySQL Server in a Docker container or dedicated VM that runs MySQL only. Using `--innodb-dedicated-server` is not recommended if the MySQL instance shares system resources with other applications.

The value for each affected variable is determined and applied by `--innodb-dedicated-server` as described in the following list:

- [`innodb_buffer_pool_size`](innodb-parameters.md)
	Buffer pool size is calculated according to the amount of memory detected on the server, as shown in the following table:
	**Table 17.8 Automatically Configured Buffer Pool Size**
	| Detected Server Memory | Buffer Pool Size |
	| --- | --- |
	| Less than 1GB | 128MB (the default value) |
	| 1GB to 4GB | *`detected server memory`* \* 0.5 |
	| Greater than 4GB | *`detected server memory`* \* 0.75 |
- [`innodb_redo_log_capacity`](innodb-parameters.md)
	Redo log capacity is calculated according to the number of logical processors available on the server. The formula is (number of available logical processors / 2) GB, with a maximum dynamic default value of 16 GB.

If one of the variables listed previously is set explicitly in an option file or elsewhere, this explicit value is used, and a startup warning similar to this one is printed to `stderr`:

\[Warning\] \[000000\] InnoDB: Option innodb\_dedicated\_server is ignored for innodb\_buffer\_pool\_size because innodb\_buffer\_pool\_size=134217728 is specified explicitly.

Setting one variable explicitly does not prevent the automatic configuration of other options.

If the server is started with [`--innodb-dedicated-server`](innodb-parameters.md) and [`innodb_buffer_pool_size`](innodb-parameters.md) is set explicitly, variable settings based on buffer pool size use the buffer pool size value calculated according to the amount of memory detected on the server rather than the explicitly defined buffer pool size value.

Note

Automatic configuration settings are applied by `--innodb-dedicated-server` *only* when the MySQL server is started. If you later set any of the affected variables explicitly, this overrides its predetermined value, and the value that was explicitly set is applied. Setting one of these variables to `DEFAULT` causes it to be set to the actual default value as shown in the variable's description in the Manual, and does *not* cause it to revert to the value set by [`--innodb-dedicated-server`](innodb-parameters.md). The corresponding system variable `innodb_dedicated_server` is changed only by starting the server with [`--innodb-dedicated-server`](innodb-parameters.md) (or with `--innodb-dedicated-server=ON` or `--innodb-dedicated-server=OFF`); it is otherwise read-only.
---
title: "MySQL :: MySQL 26.10 Reference Manual :: 12.3.2 Server Character Set and Collation"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/charset-server.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 12.3.2 Server Character Set and Collation

MySQL Server has a server character set and a server collation. By default, these are `utf8mb4` and `utf8mb4_0900_ai_ci`, but they can be set explicitly at server startup on the command line or in an option file and changed at runtime.

Initially, the server character set and collation depend on the options that you use when you start [**mysqld**](mysqld.md). You can use [`--character-set-server`](server-system-variables.md) for the character set. Along with it, you can add [`--collation-server`](server-system-variables.md) for the collation. If you don't specify a character set, that is the same as saying [`--character-set-server=utf8mb4`](server-system-variables.md). If you specify only a character set (for example, `utf8mb4`) but not a collation, that is the same as saying [`--character-set-server=utf8mb4`](server-system-variables.md) [`--collation-server=utf8mb4_0900_ai_ci`](server-system-variables.md) because `utf8mb4_0900_ai_ci` is the default collation for `utf8mb4`. Therefore, the following three commands all have the same effect:

```svg
mysqld
mysqld --character-set-server=utf8mb4
mysqld --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_0900_ai_ci
```

Character set and collation startup options require explicit names. [`--character-set-server`](server-system-variables.md) accepts exactly one value; multiple values are rejected. The value `utf8` is rejected for this option, and `utf8_*` collation names are rejected for [`--collation-server`](server-system-variables.md). Use explicit `utf8mb3`, `utf8mb4`, `utf8mb3_*`, or `utf8mb4_*` names. These restrictions also apply to settings read from option files.

One way to change the settings is by recompiling. To change the default server character set and collation when building from sources, use the [`DEFAULT_CHARSET`](source-configuration-options.md) and [`DEFAULT_COLLATION`](source-configuration-options.md) options for **CMake**. For example:

```svg
cmake . -DDEFAULT_CHARSET=latin1
```

Or:

```svg
cmake . -DDEFAULT_CHARSET=latin1 \
  -DDEFAULT_COLLATION=latin1_german1_ci
```

Both [**mysqld**](mysqld.md) and **CMake** verify that the character set/collation combination is valid. If not, each program displays an error message and terminates.

The server character set and collation are used as default values if the database character set and collation are not specified in [`CREATE DATABASE`](create-database.md) statements. They have no other purpose.

The current server character set and collation can be determined from the values of the [`character_set_server`](server-system-variables.md) and [`collation_server`](server-system-variables.md) system variables. These variables can be changed at runtime.
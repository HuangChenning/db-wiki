---
title: "MySQL :: MySQL 26.7 Reference Manual :: A.3 MySQL 26.7 FAQ: Server SQL Mode"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/faqs-sql-modes.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## A.3 MySQL 26.7 FAQ: Server SQL Mode

A.3.1. What are server SQL modes?

A.3.2. How many server SQL modes are there?

A.3.3. How do you determine the server SQL mode?

A.3.4. Is the mode dependent on the database or connection?

A.3.5. Can the rules for strict mode be extended?

A.3.6. Does strict mode impact performance?

A.3.7. What is the default server SQL mode when MySQL 26.7 is installed?

| **A.3.1.** | What are server SQL modes? |
| --- | --- |
|  | Server SQL modes define what SQL syntax MySQL should support and what kind of data validation checks it should perform. This makes it easier to use MySQL in different environments and to use MySQL together with other database servers. The MySQL Server apply these modes individually to different clients. For more information, see [Section 7.1.11, “Server SQL Modes”](sql-mode.md). |
| **A.3.2.** | How many server SQL modes are there? |
|  | Each mode can be independently switched on and off. See [Section 7.1.11, “Server SQL Modes”](sql-mode.md), for a complete list of available modes. |
| **A.3.3.** | How do you determine the server SQL mode? |
|  | You can set the default SQL mode (for [**mysqld**](mysqld.md) startup) with the [`--sql-mode`](server-options.md) option. Using the statement [``SET         [GLOBAL\|SESSION]         sql_mode='*`modes`*'``](https://dev.mysql.com/doc/refman/26.7/en/set-variable.html "15.7.6.1 SET Syntax for Variable Assignment"), you can change the settings from within a connection, either locally to the connection, or to take effect globally. You can retrieve the current mode by issuing a `SELECT @@sql_mode` statement. |
| **A.3.4.** | Is the mode dependent on the database or connection? |
|  | A mode is not linked to a particular database. Modes can be set locally to the session (connection), or globally for the server. you can change these settings using [``SET         [GLOBAL\|SESSION]         sql_mode='*`modes`*'``](https://dev.mysql.com/doc/refman/26.7/en/set-variable.html "15.7.6.1 SET Syntax for Variable Assignment"). |
| **A.3.5.** | Can the rules for strict mode be extended? |
|  | When we refer to *strict mode*, we mean a mode where at least one of the modes [`TRADITIONAL`](sql-mode.md), [`STRICT_TRANS_TABLES`](sql-mode.md), or [`STRICT_ALL_TABLES`](sql-mode.md) is enabled. Options can be combined, so you can add restrictions to a mode. See [Section 7.1.11, “Server SQL Modes”](sql-mode.md), for more information. |
| **A.3.6.** | Does strict mode impact performance? |
|  | The intensive validation of input data that some settings requires more time than if the validation is not done. While the performance impact is not that great, if you do not require such validation (perhaps your application already handles all of this), then MySQL gives you the option of leaving strict mode disabled. However, if you do require it, strict mode can provide such validation. |
| **A.3.7.** | What is the default server SQL mode when MySQL 26.7 is installed? |
|  | The default SQL mode in MySQL 8.0 includes these modes: [`ONLY_FULL_GROUP_BY`](sql-mode.md), [`STRICT_TRANS_TABLES`](sql-mode.md), [`NO_ZERO_IN_DATE`](sql-mode.md), [`NO_ZERO_DATE`](sql-mode.md), [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md), and [`NO_ENGINE_SUBSTITUTION`](sql-mode.md).  For information about all available modes and default MySQL behavior, see [Section 7.1.11, “Server SQL Modes”](sql-mode.md). |
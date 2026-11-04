---
title: "8.1.4 Security-Related mysqld Options and Variables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/security-options.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

The following table shows [**mysqld**](mysqld.md) options and system variables that affect security. For descriptions of each of these, see [Section 7.1.7, “Server Command Options”](server-options.md), and [Section 7.1.8, “Server System Variables”](server-system-variables.md).

**Table 8.1 Security Option and Variable Summary**

| Name | Cmd-Line | Option File | System Var | Status Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- | --- |
| [allow-suspicious-udfs](server-options.md) | Yes | Yes |  |  |  |  |
| [automatic\_sp\_privileges](server-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [chroot](server-options.md) | Yes | Yes |  |  |  |  |
| [local\_infile](server-system-variables.md) | Yes | Yes | Yes |  | Global | Yes |
| [safe-user-create](server-options.md) | Yes | Yes |  |  |  |  |
| [secure\_file\_priv](server-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [skip-grant-tables](server-options.md) | Yes | Yes |  |  |  |  |
| [skip\_name\_resolve](server-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [skip\_networking](server-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [skip\_show\_database](server-options.md) | Yes | Yes | Yes |  | Global | No |
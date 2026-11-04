---
title: "29.13 Performance Schema Option and Variable Reference"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/performance-schema-option-variable-reference.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

**Table 29.16 Performance Schema Variable Reference**

| Name | Cmd-Line | Option File | System Var | Status Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- | --- |
| [performance\_schema](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [Performance\_schema\_accounts\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance\_schema\_accounts\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [Performance\_schema\_cond\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_cond\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance-schema-consumer-events-stages-current](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-stages-history](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-stages-history-long](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-statements-cpu](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-statements-current](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-statements-history](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-statements-history-long](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-transactions-current](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-transactions-history](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-transactions-history-long](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-waits-current](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-waits-history](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-events-waits-history-long](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-global-instrumentation](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-statements-digest](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance-schema-consumer-thread-instrumentation](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [Performance\_schema\_digest\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance\_schema\_digests\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_stages\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_stages\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_statements\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_statements\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_transactions\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_transactions\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_waits\_history\_long\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_events\_waits\_history\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [Performance\_schema\_file\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_file\_handles\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_file\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_hosts\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance\_schema\_hosts\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance-schema-instrument](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [Performance\_schema\_locker\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance-schema-logger](performance-schema-options.md) | Yes | Yes |  |  |  |  |
| [performance\_schema\_max\_cond\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_cond\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_digest\_length](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_file\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_file\_handles](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_file\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_logger\_classes](performance-schema-system-variables.md) | Yes |  | Yes |  | Global | No |
| [performance\_schema\_max\_memory\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_metadata\_locks](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_meter\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_metric\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_mutex\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_mutex\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_prepared\_statements\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_program\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_rwlock\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_rwlock\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_socket\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_socket\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_stage\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_statement\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_statement\_stack](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_table\_handles](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_table\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_thread\_classes](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_max\_thread\_instances](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [Performance\_schema\_memory\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_metadata\_lock\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_meter\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_metric\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_mutex\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_mutex\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_nested\_statement\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_prepared\_statements\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_program\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_rwlock\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_rwlock\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_session\_connect\_attrs\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance\_schema\_session\_connect\_attrs\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_setup\_actors\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [performance\_schema\_setup\_objects\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
| [Performance\_schema\_socket\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_socket\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_stage\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_statement\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_table\_handles\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_table\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_thread\_classes\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_thread\_instances\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Performance\_schema\_users\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [performance\_schema\_users\_size](performance-schema-system-variables.md) | Yes | Yes | Yes |  | Global | No |
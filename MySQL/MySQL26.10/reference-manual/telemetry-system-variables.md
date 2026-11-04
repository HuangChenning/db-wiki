---
title: "MySQL :: MySQL 26.10 Reference Manual :: 35.2 Telemetry Variables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/telemetry-system-variables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 35.2 Telemetry Variables

The following table lists the Telemetry variables.

**Table 35.1 Telemetry Variable Summary**

| Name | Cmd-Line | Option File | System Var | Status Var | Var Scope | Dynamic |
| --- | --- | --- | --- | --- | --- | --- |
| [Performance\_schema\_logger\_lost](performance-schema-status-variables.md) |  |  |  | Yes | Global | No |
| [Telemetry\_logs\_supported](server-status-variables.md) |  |  |  | Yes | Global | No |
| [Telemetry\_metrics\_supported](server-status-variables.md) |  |  |  | Yes | Global | No |
| [Telemetry\_traces\_supported](server-status-variables.md) |  |  |  | Yes | Global | No |
| [telemetry.live\_sessions](server-status-variables.md) |  |  |  | Yes | Global | No |
| [telemetry.log\_enabled](telemetry-logs-configuration.md) |  |  | Yes |  | Global | Yes |
| [telemetry.metrics\_enabled](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.metrics\_reader\_frequency\_1](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.metrics\_reader\_frequency\_2](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.metrics\_reader\_frequency\_3](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_blrp\_max\_export\_batch\_size](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_blrp\_max\_queue\_size](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_blrp\_schedule\_delay](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_bsp\_max\_export\_batch\_size](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_bsp\_max\_queue\_size](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_bsp\_schedule\_delay](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_certificates](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_cipher](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_cipher\_suite](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_client\_certificates](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_client\_key](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_compression](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_endpoint](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_headers](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_max\_tls](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_min\_tls](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_network\_namespace](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_protocol](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_secret\_headers](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_logs\_timeout](telemetry-logs-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_certificates](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_cipher](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_cipher\_suite](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_client\_certificates](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_client\_key](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_compression](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_endpoint](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_headers](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_max\_tls](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_min\_tls](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_network\_namespace](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_protocol](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_secret\_headers](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_metrics\_timeout](telemetry-metrics-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_certificates](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_cipher](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_cipher\_suite](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_client\_certificates](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_client\_key](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_compression](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_endpoint](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_headers](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_max\_tls](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_min\_tls](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_network\_namespace](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_protocol](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_secret\_headers](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_exporter\_otlp\_traces\_timeout](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.otel\_log\_level](telemetry-trace-configuration.md) |  |  | Yes |  | Global | Yes |
| [telemetry.otel\_resource\_attributes](telemetry-trace-configuration.md) |  |  | Yes |  | Global | No |
| [telemetry.query\_text\_enabled](telemetry-trace-configuration.md) |  |  | Yes |  | Global | Yes |
| [telemetry.resource\_provider](server-system-variables.md) |  |  | Yes |  | Global | No |
| [telemetry.run\_level](server-status-variables.md) |  |  |  | Yes | Global | No |
| [telemetry.secret\_provider](server-system-variables.md) |  |  | Yes |  | Global | No |
| [telemetry.trace\_enabled](telemetry-trace-configuration.md) |  |  | Yes |  | Global | Yes |
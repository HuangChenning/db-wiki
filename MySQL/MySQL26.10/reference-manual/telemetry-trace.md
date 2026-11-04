---
title: "MySQL :: MySQL 26.10 Reference Manual :: 35.3 OpenTelemetry Trace"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/telemetry-trace.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 35.3 OpenTelemetry Trace

Tracing telemetry enables you to visualize the flow of any processing action as it is processed through your server. The data for each action, a span, includes possible error information and timing data. Traces are generated for `COM_QUERY` commands executed, including non-query commands such as `COM_PING`, or `COM_STMT_CLOSE`. Query statement traces also have an associated SQL text attribute.

Telemetry tracing is implemented in:
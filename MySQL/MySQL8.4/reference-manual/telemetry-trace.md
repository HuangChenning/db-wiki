---
title: "35.3 OpenTelemetry Trace"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/telemetry-trace.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

Tracing telemetry enables you to visualize the flow of any processing action as it is processed through your server. The data for each action, a span, includes possible error information and timing data. Traces are generated for `COM_QUERY` commands executed, including non-query commands such as `COM_PING`, or `COM_STMT_CLOSE`. Query statement traces also have an associated SQL text attribute.

Telemetry tracing is implemented in:
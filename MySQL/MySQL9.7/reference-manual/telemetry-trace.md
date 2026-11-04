---
title: "35.3 OpenTelemetry Trace"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/telemetry-trace.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

Tracing telemetry enables you to visualize the flow of any processing action as it is processed through your server. The data for each action, a span, includes possible error information and timing data. Traces are generated for `COM_QUERY` commands executed, including non-query commands such as `COM_PING`, or `COM_STMT_CLOSE`. Query statement traces also have an associated SQL text attribute.

Telemetry tracing is implemented in:
---
title: "MySQL :: MySQL 26.7 Reference Manual :: 35.5 OpenTelemetry Logging"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/telemetry-logging.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 35.5 OpenTelemetry Logging

MySQL's OpenTelemetry Logging enables you to export telemetry logs from your MySQL Server to OpenTelemetry backends for analysis. This feature is implemented in the following ways:

- Telemetry Logging Component: collects instrumented log events from the server, formats it in OpenTelemetry's OTLP format, and exports the logs to the defined endpoint using the OpenTelemetry OTLP network protocol. The process listening at the endpoint can be an OpenTelemetry collector or any other OpenTelemtry-compatible backend. If you want to export to multiple backends, you must use an OpenTelemetry collector.
	See [Section 35.1, “Installing OpenTelemetry Support”](telemetry-trace-install.md).
- Telemetry Logging Interface: API which enables you to define and integrate your own OpenTelemetry Logging components. This interface makes it possible to discover the available logging instrumentation, enable loggers, generate records, and extract the associated trace contexts.
	The interface does not provide logging. You must use MySQL Enterprise Edition, MySQL HeatWave, or develop your own component to provide logging.
	For information on the interface and sample component code, see the *Server telemetry logs service* sections of the [MySQL Server Doxygen Documentation](https://dev.mysql.com/doc/dev/mysql-server/latest/).
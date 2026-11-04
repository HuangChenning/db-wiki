---
title: "MySQL :: MySQL 26.7 Reference Manual :: 35.5.1 Configuring Log Telemetry"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/telemetry-logs-configuration.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 35.5.1 Configuring Log Telemetry

This section describes the configuration for server.

For information on the configured loggers, see [Section 29.12.21.1, “The setup\_loggers Table”](performance-schema-setup-loggers-table.md).

#### Server Configuration System Variables

The following are the server telemetry logging system variables:

- `telemetry.log_enabled`
	| System Variable | `telemetry.log_enabled` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | Yes |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	Controls whether telemetry logs are exported or not.
- `telemetry.otel_exporter_otlp_logs_protocol`
	| System Variable | `telemetry.otel_exporter_otlp_logs_protocol` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `http/protobuf` |
	| Valid Values | `http/protobuf`  `http/json` |
	OTLP transport protocol
- `telemetry.otel_exporter_otlp_logs_endpoint`
	| System Variable | `telemetry.otel_exporter_otlp_logs_endpoint` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `empty` |
	Target URL to which the exporter sends logs.
- `telemetry.otel_exporter_otlp_logs_network_namespace`
	| System Variable | `telemetry.otel_exporter_otlp_logs_network_namespace` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	(Linux only) Network namespace to use when sending data to the logs endpoint.
- `telemetry.otel_exporter_otlp_logs_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_logs_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	The trusted certificate to use when verifying a server's TLS credentials.
- `telemetry.otel_exporter_otlp_logs_client_key`
	| System Variable | `telemetry.otel_exporter_otlp_logs_client_key` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	Client's private key in PEM format.
- `telemetry.otel_exporter_otlp_logs_client_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_logs_client_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	Client certificate/chain trust for client's private key in PEM format.
- `telemetry.otel_exporter_otlp_logs_headers`
	| System Variable | `telemetry.otel_exporter_otlp_logs_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	A list of headers to apply to all outgoing logs
- `telemetry.otel_exporter_otlp_logs_secret_headers`
	| System Variable | `telemetry.otel_exporter_otlp_logs_secret_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Name of a secret, that contains the sensitive data for logs headers. The data content and format depends on the secret provider implementation provided with system variable [`telemetry.secret_provider`](server-system-variables.md).
- `telemetry.otel_exporter_otlp_logs_compression`
	| System Variable | `telemetry.otel_exporter_otlp_logs_compression` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `none (no compression)` |
	| Valid Values | `none (no compression)`  `gzip` |
	Compression used by log exporter.
- `telemetry.otel_exporter_otlp_logs_timeout`
	| System Variable | `telemetry.otel_exporter_otlp_logs_timeout` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10000` |
	| Unit | milliseconds |
	Time in milliseconds the OTLP exporter waits for each batch export.
- `telemetry.otel_blrp_schedule_delay`
	| System Variable | `telemetry.otel_blrp_schedule_delay` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `5000` |
	| Unit | milliseconds |
	Delay interval between two consecutive exports in milliseconds.
- `telemetry.otel_blrp_max_queue_size`
	| System Variable | `telemetry.otel_blrp_max_queue_size` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `2048` |
	Maximum queue size.
- `telemetry.otel_blrp_max_export_batch_size`
	| System Variable | `telemetry.otel_blrp_max_export_batch_size` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `512` |
	Maximum batch size.
- `telemetry.otel_exporter_otlp_logs_min_tls`
	| System Variable | `telemetry.otel_exporter_otlp_logs_min_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
	The minimum accepted TLS version. If left empty, TLS 1.2 is used.
- `telemetry.otel_exporter_otlp_logs_max_tls`
	| System Variable | `telemetry.otel_exporter_otlp_logs_max_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
	The maximum accepted TLS version. If left empty, there is no maximum TLS version.
- `telemetry.otel_exporter_otlp_logs_cipher`
	| System Variable | `telemetry.otel_exporter_otlp_logs_cipher` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[list of ciphers]` |
	Current list of TLS 1.2 ciphers to use for logs. The current default is:
	```svg
	ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:
	ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:
	ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-AES128-CCM:
	DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-CCM:
	DHE-RSA-AES128-CCM:DHE-RSA-CHACHA20-POLY1305
	```
- `telemetry.otel_exporter_otlp_logs_cipher_suite`
	| System Variable | `telemetry.otel_exporter_otlp_logs_cipher_suite` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Current list of TLS 1.3 ciphers to use for logs. The current default is:
	```svg
	TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_CCM_SHA256
	```

#### Server Configuration Status Variables

This section describes the logger-related status variables.

- [`Telemetry_logs_supported`](server-status-variables.md): displays whether the server was compiled with Telemetry logging support.
- [`Performance_schema_logger_lost`](performance-schema-status-variables.md): Displays the number of logger instruments which failed to be created.

#### Server Configuration Command Line

This section describes the logger-related command line configuration options.

- [`performance-schema-logger`](performance-schema-options.md): defines the default values for loggers. This can be defined multiple times, similarly to [`--performance-schema-instrument`](performance-schema-options.md).
	In the following example, all loggers are configured with the error level `ERROR`, except `foo` and `bar` which are configured to error level `INFO` and `WARNING`, respectively:
	```svg
	--performance-schema-logger = 'logger/% = Level:ERROR' --performance-schema-logger = 'logger/foo/% = Level:INFO' 
	--performance-schema-logger = 'logger/bar/% = Level:WARNING'
	```
	To see the configured loggers, run the following:
	```sql
	select * from performance_schema.setup_loggers;
	+------------------------+-------+-------------------------+
	| NAME                   | LEVEL | DESCRIPTION             |
	+------------------------+-------+-------------------------+
	| logger/sql/error_log   | info  | MySQL error logger      |
	| logger/sql/slow_log    | info  | MySQL slow query logger |
	| logger/sql/general_log | info  | MySQL general logger    |
	+------------------------+-------+-------------------------+
	```
	This example shows the default MySQL error logger. This can be set to one of the following values:
	- `none`
	- `error`
	- `warn`
	- `info`
	- `debug`
	The following example changes the error logging level to WARNING:
	```sql
	mysql> UPDATE performance_schema.setup_loggers
	       SET LEVEL='WARN'
	```
- [`performance_schema_max_logger_classes`](performance-schema-system-variables.md): this system variable can also be set from the command line. For example:
	```svg
	--performance_schema_max_logger_classes=100
	```
	Editing this value requires a server restart.
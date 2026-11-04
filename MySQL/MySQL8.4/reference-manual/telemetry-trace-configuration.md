---
title: "35.3.1 Configuring Trace Telemetry"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/telemetry-trace-configuration.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 35.3.1 Configuring Trace Telemetry

This section describes the configuration for server and client.

#### Server Configuration

The following are the server trace telemetry configuration variables:

- `telemetry.trace_enabled`
	| System Variable | `telemetry.trace_enabled` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | Yes |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `ON` |
	Controls whether telemetry traces are collected or not.
- `telemetry.query_text_enabled`
	| System Variable | `telemetry.query_text_enabled` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | Yes |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `ON` |
	Controls whether the SQL query text is included in the trace
- `telemetry.otel_log_level`
	| System Variable | `telemetry.otel_log_level` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | Yes |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `ERROR` |
	| Valid Values | `SILENT`  `INFO`  `ERROR`  `WARNING`  `DEBUG` |
	Controls which OpenTelemetry logs are printed in the server logs
- `telemetry.otel_resource_attributes`
	| System Variable | `telemetry.otel_resource_attributes` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `empty` |
	See corresponding OpenTelemetry variable OTEL\_RESOURCE\_ATTRIBUTES.
- `telemetry.otel_exporter_otlp_traces_protocol`
	| System Variable | `telemetry.otel_exporter_otlp_traces_protocol` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `http/protobuf` |
	| Valid Values | `http/protobuf`  `http/json` |
	OTLP transport protocol
- `telemetry.otel_exporter_otlp_traces_endpoint`
	| System Variable | `telemetry.otel_exporter_otlp_traces_endpoint` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `http://localhost:4318/v1/traces` |
	Target URL to which the exporter sends traces
- `telemetry.otel_exporter_otlp_traces_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_traces_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	The trusted certificate to use when verifying a server's TLS credentials.
- `telemetry.otel_exporter_otlp_traces_client_key`
	| System Variable | `telemetry.otel_exporter_otlp_traces_client_key` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	Client's private key in PEM format.
- `telemetry.otel_exporter_otlp_traces_client_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_traces_client_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value |  |
	Client certificate/chain trust for clients private key in PEM format.
- `telemetry.otel_exporter_otlp_traces_headers`
	| System Variable | `telemetry.otel_exporter_otlp_traces_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `empty` |
	See corresponding OpenTelemetry variable OTEL\_EXPORTER\_TRACES\_HEADERS.
- `telemetry.otel_exporter_otlp_traces_compression`
	| System Variable | `telemetry.otel_exporter_otlp_traces_compression` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `none (no compression)` |
	| Valid Values | `none (no compression)`  `gzip` |
	Compression used by exporter
- `telemetry.otel_exporter_otlp_traces_timeout`
	| System Variable | `telemetry.otel_exporter_otlp_traces_timeout` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10000` |
	| Unit | milliseconds |
	Time in milliseconds the OLTP exporter waits for each batch export.
- `telemetry.otel_bsp_schedule_delay`
	| System Variable | `telemetry.otel_bsp_schedule_delay` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `5000` |
	| Unit | milliseconds |
	Delay interval between two consecutive exports in milliseconds
- `telemetry.otel_bsp_max_queue_size`
	| System Variable | `telemetry.otel_bsp_max_queue_size` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `2048` |
	Maximum queue size
- `telemetry.otel_bsp_max_export_batch_size`
	| System Variable | `telemetry.otel_bsp_max_export_batch_size` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `512` |
	Maximum batch size
- `telemetry.otel_exporter_otlp_traces_min_tls`
	| System Variable | `telemetry.otel_exporter_otlp_traces_min_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
- `telemetry.otel_exporter_otlp_traces_max_tls`
	| System Variable | `telemetry.otel_exporter_otlp_traces_max_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
- `telemetry.otel_exporter_otlp_traces_cipher`
	| System Variable | `telemetry.otel_exporter_otlp_traces_cipher` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
- `telemetry.otel_exporter_otlp_traces_cipher_suite`
	| System Variable | `telemetry.otel_exporter_otlp_traces_cipher_suite` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |

#### Client Configuration

The MySQL client reads telemetry configuration from the `[telemetry_client]` section of the configuration file. See [Installing Client Plugin](telemetry-trace-install.md) for information on the `telemetry_client` option. The following configuration options are available:

**Table 35.2 mysql client Telemetry Option Summary**

| Option Name | Description |
| --- | --- |
| [\--telemetry\_client](mysql-command-options.md) | Enables the telemetry client. |
| \--otel\_bsp\_max\_export\_batch\_size | See variable OTEL\_BSP\_MAX\_EXPORT\_BATCH\_SIZE. |
| \--otel\_bsp\_max\_queue\_size | See variable OTEL\_BSP\_MAX\_QUEUE\_SIZE. |
| \--otel\_bsp\_schedule\_delay | See variable OTEL\_BSP\_SCHEDULE\_DELAY. |
| \--otel\_exporter\_otlp\_traces\_certificates | Not in use at this time. Reserved for future development. |
| \--otel\_exporter\_otlp\_traces\_client\_certificates | Not in use at this time. Reserved for future development. |
| \--otel\_exporter\_otlp\_traces\_client\_key | Not in use at this time. Reserved for future development. |
| \--otel\_exporter\_otlp\_traces\_compression | Compression type |
| \--otel\_exporter\_otlp\_traces\_endpoint | The trace export endpoint |
| \--otel\_exporter\_otlp\_traces\_headers | Key-value pairs to be used as headers associated with HTTP requests |
| \--otel\_exporter\_otlp\_traces\_protocol | The OTLP transport protocol |
| \--otel\_exporter\_otlp\_traces\_timeout | Time OLTP exporter waits for each batch export |
| \--otel-help | When enabled, prints help about telemetry\_client options. |
| \--otel\_log\_level | Controls which opentelemetry logs are printed in the server logs |
| \--otel\_resource\_attributes | See corresponding OpenTelemetry variable OTEL\_RESOURCE\_ATTRIBUTES. |
| \--otel-trace | This system variable controls whether telemetry traces are collected or not. |

- `trace`
	| Command-Line Format | `--otel-trace` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `ON` |
	Controls whether telemetry traces are collected or not.
- `help`
	| Command-Line Format | `--otel-help` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	When enabled, prints help about telemetry\_client options.
- `otel_log_level`
	| Command-Line Format | `--otel_log_level` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `ERROR` |
	| Valid Values | `ERROR`  `SILENT`  `WARNING`  `INFO`  `DEBUG` |
	Controls which OpenTelemetry logs are printed in the server logs
- `otel_resource_attributes`
	| Command-Line Format | `--otel_resource_attributes` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	See corresponding OpenTelemetry variable OTEL\_RESOURCE\_ATTRIBUTES.
- `otel_exporter_otlp_traces_protocol`
	| Command-Line Format | `--otel_exporter_otlp_traces_protocol` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `http/protobuf` |
	| Valid Values | `http/protobuf`  `http/json` |
	OTLP transport protocol
- `otel_exporter_otlp_traces_endpoint`
	| Command-Line Format | `--otel_exporter_otlp_traces_endpoint` |
	| --- | --- |
	| Type | String |
	| Default Value | `http://localhost:4318/v1/traces` |
	Target URL to which the exporter sends traces
- `otel_exporter_otlp_traces_certificates`
	| Command-Line Format | `--otel_exporter_otlp_traces_certificates` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	The trusted certificate to use when verifying a server's TLS credentials.
- `otel_exporter_otlp_traces_client_key`
	| Command-Line Format | `--otel_exporter_otlp_traces_client_key` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Client's private key in PEM format.
- `otel_exporter_otlp_traces_client_certificates`
	| Command-Line Format | `--otel_exporter_otlp_traces_client_certificates` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Client certificate/chain trust for clients private key in PEM format.
- `otel_exporter_otlp_traces_headers`
	| Command-Line Format | `--otel_exporter_otlp_traces_headers` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	See corresponding OpenTelemetry variable OTEL\_EXPORTER\_TRACES\_HEADERS.
- `otel_exporter_otlp_traces_compression`
	| Command-Line Format | `--otel_exporter_otlp_traces_compression` |
	| --- | --- |
	| Type | String |
	| Default Value | `none` |
	| Valid Values | `none`  `gzip` |
	Compression used by exporter
- `otel_exporter_otlp_traces_timeout`
	| Command-Line Format | `--otel_exporter_otlp_traces_timeout` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `10000` |
	Time OLTP exporter waits for each batch export
- `otel_bsp_schedule_delay`
	| Command-Line Format | `--otel_bsp_schedule_delay` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `5000` |
	Delay interval between two consecutive exports in milliseconds
- `otel_bsp_max_queue_size`
	| Command-Line Format | `--otel_bsp_max_queue_size` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `2048` |
	Maximum queue size
- `otel_bsp_max_export_batch_size`
	| Command-Line Format | `--otel_bsp_max_export_batch_size` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `512` |
	Maximum batch size

#### Client Configuration Example

The following is an example of a `my.cnf` configuration file containing the Client Telemetry plugin configuration:

```
[mysql]

telemetry-client = ON

[telemetry_client]
help = ON
trace = OFF
otel-resource-attributes = "RK1=RV1, RK2=RV2, RK3=RV3"
otel-log-level = "error"
otel-exporter-otlp-traces-headers = "K1=V1, K2=V2"
otel-exporter-otlp-traces-protocol = "http/json"
```

If `telemetry-client = ON` is set in the configuration file, you do not need to specify `--telemetry-client` when starting the client.
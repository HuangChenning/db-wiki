---
title: "35.4.1 Configuring Metrics Telemetry"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/telemetry-metrics-configuration.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 35.4.1 Configuring Metrics Telemetry

#### Server Configuration

- `telemetry.metrics_enabled`
	| System Variable | `telemetry.metrics_enabled` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `ON` |
	Controls whether telemetry metrics are collected or not.
- `telemetry.otel_exporter_otlp_metrics_protocol`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_protocol` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `http/protobuf` |
	| Valid Values | `http/protobuf`  `http/json` |
	The OLTP transport protocol.
	Note
	MySQL does not support the `gprc` protocol.
- `telemetry.otel_exporter_otlp_metrics_endpoint`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_endpoint` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `http://localhost:4318/v1/metrics` |
	Endpoint metric signals are sent to.
- `telemetry.otel_exporter_otlp_metrics_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	The trusted certificate to use when verifying a server's TLS credentials.
- `telemetry.otel_exporter_otlp_metrics_client_key`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_client_key` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Client's private key in PEM format.
- `telemetry.otel_exporter_otlp_metrics_client_certificates`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_client_certificates` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Client certificate/chain trust for clients private key in PEM format.
- `telemetry.otel_exporter_otlp_metrics_min_tls`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_min_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
	Minimum TLS version to use for metrics.
- `telemetry.otel_exporter_otlp_metrics_max_tls`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_max_tls` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `[none]`  `1.2`  `1.3` |
	Maximum TLS version to use for metrics.
- `telemetry.otel_exporter_otlp_metrics_cipher`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_cipher` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	TLS cipher to use for metrics (TLS 1.2).
- `telemetry.otel_exporter_otlp_metrics_cipher_suite`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_cipher_suite` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	TLS cipher to use for metrics (TLS 1.3).
- `telemetry.otel_exporter_otlp_metrics_headers`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Key-value pairs to be used as headers associated with HTTP requests.
- `telemetry.otel_exporter_otlp_metrics_compression`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_compression` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `none (no compression)` |
	| Valid Values | `none (no compression)`  `gzip` |
	Compression used by exporter
- `telemetry.otel_exporter_otlp_metrics_timeout`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_timeout` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10000` |
	| Unit | milliseconds |
	Time in milliseconds the OLTP exporter waits for each batch export.
- `telemetry.metrics_reader_frequency_1`
	| System Variable | `telemetry.metrics_reader_frequency_1` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10` |
	| Unit | seconds |
	Mandatory. Defines the interval in seconds (f1) between meter evaluations for meters with a frequency less than or equal to the interval, f1. For example:
	```
	SELECT * from performance_schema.setup_meters WHERE FREQUENCY <= telemetry.metrics_reader_frequency_1
	```
- `telemetry.metrics_reader_frequency_2`
	| System Variable | `telemetry.metrics_reader_frequency_2` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10` |
	| Unit | seconds |
	Optional. Defines the interval in seconds (f2) between meter evaluations for meters with a frequency greater than the interval, f1. For example, if f1 and f2 are defined:
	```
	SELECT * from performance_schema.setup_meters WHERE FREQUENCY <= telemetry.metrics_reader_frequency_1
	```
	and, every f2 seconds:
	```
	SELECT * from performance_schema.setup_meters 
	      WHERE FREQUENCY > telemetry.metrics_reader_frequency_1 
	      AND FREQUENCY <= metrics_reader_frequency_2;
	```
- `telemetry.metrics_reader_frequency_3`
	| System Variable | `telemetry.metrics_reader_frequency_3` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Integer |
	| Default Value | `10` |
	| Unit | seconds |
	Optional. Defines the interval in seconds (f3) between meter evaluations for meters with a frequency greater than the interval, f2. For example, if f1, f2, and f3 are defined:
	```
	SELECT * from performance_schema.setup_meters WHERE FREQUENCY <= telemetry.metrics_reader_frequency_1
	```
	and, every f2 seconds:
	```
	SELECT * from performance_schema.setup_meters 
	      WHERE FREQUENCY > telemetry.metrics_reader_frequency_1 
	      AND FREQUENCY <= metrics_reader_frequency_2;
	```
	and, every f3 seconds:
	```
	SELECT * from performance_schema.setup_meters WHERE FREQUENCY > telemetry.metrics_reader_frequency_2;
	```
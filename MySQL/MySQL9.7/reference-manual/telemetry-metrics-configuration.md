---
title: "35.4.1 Configuring Metrics Telemetry"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/telemetry-metrics-configuration.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 35.4.1 Configuring Metrics Telemetry

This section lists the system variables used to configure Metric telemetry.

#### Server Configuration

- `telemetry.metrics_enabled`
	| System Variable | `telemetry.metrics_enabled` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | Boolean |
	| Default Value | `OFF` |
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
	| Default Value | `empty` |
	Endpoint metric signals are sent to.
- `telemetry.otel_exporter_otlp_metrics_network_namespace`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_network_namespace` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	(Linux only) Network namespace to use when sending data to the metrics endpoint.
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
	Current list of TLS 1.2 ciphers to use for metrics. The current default is:
	```
	ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:
	ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:
	ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-AES128-CCM:
	DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-CCM:
	DHE-RSA-AES128-CCM:DHE-RSA-CHACHA20-POLY1305
	```
- `telemetry.otel_exporter_otlp_metrics_cipher_suite`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_cipher_suite` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Current list of TLS 1.3 ciphers to use for metrics. The current default is:
	```
	TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_CCM_SHA256
	```
- `telemetry.otel_exporter_otlp_metrics_headers`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Key-value pairs to be used as headers associated with HTTP requests.
- `telemetry.otel_exporter_otlp_metrics_secret_headers`
	| System Variable | `telemetry.otel_exporter_otlp_metrics_secret_headers` |
	| --- | --- |
	| Scope | Global |
	| Dynamic | No |
	| [`SET_VAR`](optimizer-hints.md) Hint Applies | No |
	| Type | String |
	| Default Value | `[none]` |
	Name of a secret, that contains the sensitive data for metrics headers. The data content and format depends on the secret provider implementation provided with system variable [`telemetry.secret_provider`](server-system-variables.md).
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
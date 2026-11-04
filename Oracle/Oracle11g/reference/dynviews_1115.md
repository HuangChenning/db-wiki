---
title: "V$DISPATCHER_CONFIG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1115.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DISPATCHER_CONFIG` displays information about the dispatcher configurations and their attributes.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONF_INDX` | `NUMBER` | Zero-based index of the `DISPATCHERS` configuration |
| `NETWORK` | `VARCHAR2(1024)` | Network protocol or listening address of dispatchers (may be truncated) |
| `DISPATCHERS` | `NUMBER` | Number of dispatchers to maintain for the configuration |
| `CONNECTIONS` | `NUMBER` | Maximum number of concurrent connections per dispatcher |
| `SESSIONS` | `NUMBER` | Maximum number of concurrent sessions per dispatcher |
| `POOL` | `VARCHAR2(4)` | Indicates whether Connection Pooling is on: |
| `TICKS` | `NUMBER` | Tick size (in seconds) for Connection Pooling timeout |
| `INBD_TIMOUT` | `NUMBER` | Timeout duration (in ticks) for pooled inbound connections |
| `OUTBD_TIMOUT` | `NUMBER` | Timeout duration (in ticks) for pooled outbound connections |
| `MULTIPLEX` | `VARCHAR2(4)` | Indicates whether Session Multiplexing is on: |
| `LISTENER` | `VARCHAR2(1200)` | Listeners to register dispatchers with (may be truncated) |
| `SERVICE` | `VARCHAR2(128)` | Service names supported (may be truncated) |
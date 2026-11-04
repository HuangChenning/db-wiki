---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DISPATCHER_RATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.187 V$DISPATCHER\_RATE

`V$DISPATCHER_RATE` displays rate statistics for a number of activities performed by the dispatcher processes.

Collected samples have an activity-specific "time-to-live" (`TTL_*` columns). Statistics are reported over the following two types of time intervals:

- Current statistics (`CUR_` columns)
	Current statistics use samples collected over the most recent time-to-live interval.
- Historical statistics (`AVG_` and most of the `MAX_` columns)
	Historical statistics make use of all samples that are no longer current.

At the time of collection, a sample is current. After the time-to-live has elapsed, the sample becomes historical. Each type of activity has a specific scale (represented by the `SCALE_*` columns) at which the statistics are reported.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(4)` | Name of the dispatcher process |
| `PADDR` | `RAW(4 \| 8)` | Address of the dispatcher process |
| `CUR_LOOP_RATE` | `NUMBER` | Rate at which the dispatcher has been iterating through its dispatching loop, reported over the past `TTL_LOOPS`, in iterations/ `SCALE_LOOPS` |
| `CUR_EVENT_RATE` | `NUMBER` | Rate at which the dispatcher has been processing dispatcher events, reported over the past `TTL_LOOPS`, in events/ `SCALE_LOOPS`. Such dispatcher events include network events and shared server requests. |
| `CUR_EVENTS_PER_LOOP` | `NUMBER` | Average number of events the dispatcher has been processing in each iteration through its dispatching loop, reported over the past `TTL_LOOPS`, in events/iteration |
| `CUR_MSG_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying messages between clients and shared servers, reported over the past `TTL_MSG`, in messages/ `SCALE_MSG` |
| `CUR_SVR_BUF_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying buffers to shared servers, reported over the past `TTL_SVR_BUF`, in messages/ `SCALE_SVR_BUF` |
| `CUR_SVR_BYTE_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying data to shared servers, reported over the past `TTL_SVR_BUF`, in bytes/ `SCALE_SVR_BUF` |
| `CUR_SVR_BYTE_PER_BUF` | `NUMBER` | Average number of data types in each buffer relayed to shared servers, reported over the past `TTL_SVR_BUF`, in bytes/buffer |
| `CUR_CLT_BUF_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying buffers to clients, reported over the past `TTL_CLT_BUF`, in buffers/ `SCALE_CLT_BUF` |
| `CUR_CLT_BYTE_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying data to clients, reported over the past `TTL_CLT_BUF`, in bytes/ `SCALE_CLT_BUF` |
| `CUR_CLT_BYTE_PER_BUF` | `NUMBER` | Average number of data bytes in each buffer relayed to clients, reported over the past `TTL_CLT_BUF`, in bytes/buffer |
| `CUR_BUF_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying buffers to either clients or shared servers, reported over the past `TTL_BUF`, in bytes/ `SCALE_BUF` |
| `CUR_BYTE_RATE` | `NUMBER` | Rate at which the dispatcher has been relaying data to either clients or shared servers, reported over the past `TTL_BUF`, in bytes/ `SCALE_BUF` |
| `CUR_BYTE_PER_BUF` | `NUMBER` | Average number of data bytes in each buffer relayed to either clients or shared servers, reported over the past `TTL_BUF`, in bytes/buffer |
| `CUR_IN_CONNECT_RATE` | `NUMBER` | Rate at which the dispatcher has been accepting incoming client connections, reported over the past `TTL_IN_CONNECT`, in connections/ `SCALE_IN_CONNECT` |
| `CUR_OUT_CONNECT_RATE` | `NUMBER` | Rate at which the dispatcher has been establishing outbound connections, reported over the past `TTL_OUT_CONNECT`, in connections/ `SCALE_OUT_CONNECT` |
| `CUR_RECONNECT_RATE` | `NUMBER` | In a connection pooling setup, the rate at which clients have been reconnecting to the dispatcher, reported over the past `TTL_RECONNECT`, in reconnections/ `SCALE_RECONNECT` |
| `MAX_LOOP_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever iterated through its dispatching loop, reported in iterations/ `SCALE_LOOPS`, over the dispatcher's lifetime excluding the past `TTL_LOOPS` |
| `MAX_EVENT_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever processed dispatcher events, reported in events/ `SCALE_LOOPS`, over the dispatcher's lifetime excluding the past `TTL_LOOPS` |
| `MAX_EVENTS_PER_LOOP` | `NUMBER` | Maximum number of events the dispatcher has ever processed in one iteration through its dispatching loop, reported in events/iteration, over the dispatcher's lifetime |
| `MAX_MSG_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed messages between clients and shared servers, reported in messages/ `SCALE_MSG`, over the dispatcher's lifetime excluding the past `TTL_MSG` |
| `MAX_SVR_BUF_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed buffers to shared servers, reported in buffers/ `SCALE_SVR_BUF`, over the dispatcher's lifetime excluding the past `TTL_SVR_BUF` |
| `MAX_SVR_BYTE_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed data to shared servers, reported in bytes/ `SCALE_SVR_BUF`, over the dispatcher's lifetime excluding the past `TTL_SVR_BUF` |
| `MAX_SVR_BYTE_PER_BUF` | `NUMBER` | Maximum number of data bytes the dispatcher has ever relayed in one buffer to a client, reported in bytes/buffer, over the dispatcher's lifetime |
| `MAX_CLT_BUF_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed buffers to either clients or shared servers, reported in buffers/ `SCALE_CLT_BUF`, over the dispatcher's life time excluding the past `TTL_CLT_BUF` |
| `MAX_CLT_BYTE_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed buffers to clients, reported in bytes/ `SCALE_CLT_BUF`, over the dispatcher's lifetime excluding the last `TTL_CLT_BUF` |
| `MAX_CLT_BYTE_PER_BUF` | `NUMBER` | Maximum number of data bytes the dispatcher has ever relayed in one buffer to a client, reported in bytes/buffer, over the dispatcher's lifetime |
| `MAX_BUF_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed buffers to either clients or shared servers, reported in buffers/ `SCALE_BUF`, over the dispatcher's lifetime, excluding the past `TTL_BUF` |
| `MAX_BYTE_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever relayed data to either clients or shared servers, reported in bytes/ `SCALE_BUF`, over the dispatcher's lifetime excluding the past `TTL_BUF` |
| `MAX_BYTE_PER_BUF` | `NUMBER` | Maximum number of data bytes the dispatcher has ever relayed in one buffer to either a client or a shared server, reported in bytes/buffer, over the dispatcher's lifetime |
| `MAX_IN_CONNECT_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever accepted incoming client connections, reported in connections/ `SCALE_IN_CONNECT`, over the dispatcher's lifetime excluding the past `TTL_IN_CONNECT` |
| `MAX_OUT_CONNECT_RATE` | `NUMBER` | Maximum rate at which the dispatcher has ever established outbound connections, reported in connections/ `SCALE_OUT_CONNECT`, over the dispatcher's lifetime excluding the past `TTL_OUT_CONNECT` |
| `MAX_RECONNECT_RATE` | `NUMBER` | In a connection pooling setup, the maximum rate at which clients have ever reconnected to this dispatcher, reported in reconnections/ `SCALE_RECONNECT`, over the dispatcher's lifetime excluding the past `TTL_RECONNECT` |
| `AVG_LOOP_RATE` | `NUMBER` | Historical average rate at which the dispatcher has iterated through its dispatching loop, reported in iterations/ `SCALE_LOOPS`, over the dispatcher's lifetime excluding the past `TTL_LOOPS` |
| `AVG_EVENT_RATE` | `NUMBER` | Historical average rate at which the dispatcher has processed dispatcher events, reported in events/ `SCALE_LOOPS`, over the dispatcher's lifetime excluding the past `TTL_LOOPS` |
| `AVG_EVENTS_PER_LOOP` | `NUMBER` | Historical average number of events the dispatcher has processed in one iteration through its dispatching loop, reported in events/iteration, over the dispatcher's lifetime excluding the past `TTL_LOOPS` |
| `AVG_MSG_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed messages between clients and shared servers, reported in messages/ `SCALE_MSG`, over the dispatcher's lifetime excluding the past `TTL_MSG` |
| `AVG_SVR_BUF_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed buffers to shared servers, reported in buffers/ `SCALE_SVR_BUF`, over the dispatcher's lifetime excluding the past `TTL_SVR_BUF` |
| `AVG_SVR_BYTE_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed data to shared servers, reported in bytes/ `SCALE_SVR_BUF`, over the dispatcher's lifetime excluding the past `TTL_SVR_BUF` |
| `AVG_SVR_BYTE_PER_BUF` | `NUMBER` | Historical average number of data bytes per buffer the dispatcher has relayed to shared servers, reported in bytes/buffer, over the dispatcher's lifetime excluding the past `TTL_SVR_BUF` |
| `AVG_CLT_BUF_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed buffers to clients, reported in buffers/ `SCALE_CLT_BUF`, over the dispatcher's lifetime excluding the past `TTL_CLT_BUF` |
| `AVG_CLT_BYTE_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed data to clients, reported in bytes/ `SCALE_CLT_BUF`, over the dispatcher's lifetime excluding the past `TTL_CLT_BUF` |
| `AVG_CLT_BYTE_PER_BUF` | `NUMBER` | Historical average number of data bytes per buffer the dispatcher has relayed to clients, reported in bytes/buffer, over the dispatcher's lifetime excluding the past `TTL_CLT_BUF` |
| `AVG_BUF_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed buffers to either clients or shared servers, reported in buffers/ `SCALE_BUF`, over the dispatcher's lifetime excluding the past `TTL_BUF` |
| `AVG_BYTE_RATE` | `NUMBER` | Historical average rate at which the dispatcher has relayed data to either clients or shared servers, reported in bytes/ `SCALE_BUF`, over the dispatcher's lifetime excluding the past `TTL_BUF` |
| `AVG_BYTE_PER_BUF` | `NUMBER` | Historical average number of data bytes per buffer the dispatcher has relayed to either clients or shared servers, reported in bytes/buffer, over the dispatcher's lifetime excluding the past `TTL_BUF` |
| `AVG_IN_CONNECT_RATE` | `NUMBER` | Historical average rate at which the dispatcher has accepted incoming client connections, reported in connections/ `SCALE_IN_CONNECT`, over the dispatcher's lifetime excluding the past `TTL_IN_CONNECT` |
| `AVG_OUT_CONNECT_RATE` | `NUMBER` | Historical average rate at which the dispatcher has established outbound connections, reported in connections/ `SCALE_OUT_CONNECT`, over the dispatcher's lifetime excluding the past `TTL_OUT_CONNECT` |
| `AVG_RECONNECT_RATE` | `NUMBER` | In a connection pooling setup, the historical average rate at which clients have reconnected to this dispatcher, reported in reconnections/ `SCALE_RECONNECT`, over the dispatcher's lifetime excluding the past `TTL_RECONNECT` |
| `TTL_LOOPS` | `NUMBER` | Time-to-live for "loops" samples, reported in hundredths of a second. Default is `10` minutes. |
| `TTL_MSG` | `NUMBER` | Time-to-live for "messages" samples, reported in hundredths of a second. Default is `10` seconds. |
| `TTL_SVR_BUF` | `NUMBER` | Time-to-live for "buffers to servers" samples, reported in hundredths of a second. Default is `1` second. |
| `TTL_CLT_BUF` | `NUMBER` | Time-to-live for "buffers to clients" samples, reported in hundredths of a second. Default is `1` second. |
| `TTL_BUF` | `NUMBER` | Time-to-live for "buffers to clients/servers" samples, reported in hundredths of a second. Default is `1` second. |
| `TTL_IN_CONNECT` | `NUMBER` | Time-to-live for "inbound connections" samples, reported in hundredths of a second. Default is `10` minutes. |
| `TTL_OUT_CONNECT` | `NUMBER` | Time-to-live for "outbound connections" samples, reported in hundredths of a second. Default is `10` minutes. |
| `TTL_RECONNECT` | `NUMBER` | Time-to-live for "reconnections" samples, reported in hundredths of a second. Default is `10` minutes. |
| `SCALE_LOOPS` | `NUMBER` | Scale for "loops" statistics, reported in hundredths of a second. Default is `1` minute. |
| `SCALE_MSG` | `NUMBER` | Scale for "messages" statistics, reported in hundredths of a second. Default is `1` second. |
| `SCALE_SVR_BUF` | `NUMBER` | Scale for "buffers to servers" statistics, reported in hundredths of a second. Default is `1/10` second. |
| `SCALE_CLT_BUF` | `NUMBER` | Scale for "buffers to clients" statistics, reported in hundredths of a second. Default is `1/10 ` second. |
| `SCALE_BUF` | `NUMBER` | Scale for "buffers to clients/servers" statistics, reported in hundredths of a second. Default is `1/10` second. |
| `SCALE_IN_CONNECT` | `NUMBER` | Scale for "inbound connections" statistics, reported in hundredths of a second. Default is `1` minute. |
| `SCALE_OUT_CONNECT` | `NUMBER` | Scale for "outbound connections" statistics, reported in hundredths of a second. Default is `1` minute. |
| `SCALE_RECONNECT` | `NUMBER` | Scale for "reconnections" statistics, reported in hundredths of a second. Default is `1` minute. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
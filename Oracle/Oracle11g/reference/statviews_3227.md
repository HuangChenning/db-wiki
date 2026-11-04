---
title: DBA_HIST_IC_DEVICE_STATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3227.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IC_DEVICE_STATS` displays operating system information about the usage of interconnect devices by the machine. This usage contains Oracle usage but is not limited to it. The quality of the information depends on the operating system.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `IF_NAME` | `VARCHAR2(256)` | `NOT NULL` | Name of the device (same as `NAME` in `DBA_HIST_CLUSTER_INTERCON`) |
| `IP_ADDR` | `VARCHAR2(64)` | `NOT NULL` | IP address of the device (same as `IP_ADDRESS` in `DBA_HIST_CLUSTER_INTERCON`) |
| `NET_MASK` | `VARCHAR2(16)` |  | Network mask |
| `FLAGS` | `VARCHAR2(32)` |  | Flags |
| `MTU` | `NUMBER` |  | Maximum transmission unit |
| `BYTES_RECEIVED` | `NUMBER` |  | Number of bytes received since OS start time |
| `PACKETS_RECEIVED` | `NUMBER` |  | Number of packets received since OS start time |
| `RECEIVE_ERRORS` | `NUMBER` |  | Number of receive errors since OS start time |
| `RECEIVE_DROPPED` | `NUMBER` |  | Number of receive messages that were dropped |
| `RECEIVE_BUF_OR` | `NUMBER` |  | Number of receive buffer overruns experienced |
| `RECEIVE_FRAME_ERR` | `NUMBER` |  | Number of receive errors due to frame error |
| `BYTES_SENT` | `NUMBER` |  | Number of bytes sent since OS start time |
| `PACKETS_SENT` | `NUMBER` |  | Number of packets sent since OS start time |
| `SEND_ERRORS` | `NUMBER` |  | Number of send errors since OS start time |
| `SENDS_DROPPED` | `NUMBER` |  | Number of send messages that were dropped |
| `SEND_BUF_OR` | `NUMBER` |  | Number of send buffer overruns experienced |
| `SEND_CARRIER_LOST` | `NUMBER` |  | Number of send errors due to carrier lost |
---
title: "V$SECUREFILE_TIMER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3002.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SECUREFILE_TIMER` displays information about time taken (in microseconds) by functions of SecureFiles. These timer values are collected per session.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(50)` | Name of the function |
| `LAYER_ID` | `NUMBER` | ID of the layer that the function belongs to: - `0` - Entire Subtree - `1` - Delta Updates - `2` - Write gather cache - `3` - Deduplication - `4` - Compression & Encryption - `5` - Inode - `6` - Space - `7` - Utilities - `8` - Row-Column Intersection |
| `OWNTIME` | `NUMBER` | Total time taken by the function |
| `MAXTIME` | `NUMBER` | Maximum time taken by a single call |
| `MINTIME` | `NUMBER` | Minimum time taken by a single call |
| `INVOCATIONS` | `NUMBER` | Number of times the function was invoked |
| `LAYER_NAME` | `VARCHAR2(50)` | Name of the layer to which the function belongs |
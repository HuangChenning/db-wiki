---
title: DBA_LOGSTDBY_SKIP_TRANSACTION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4127.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGSTDBY_SKIP_TRANSACTION` displays the skip settings chosen. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `XIDUSN` | `NUMBER` |  | Transaction ID undo segment number |
| `XIDSLT` | `NUMBER` |  | Transaction ID slot number |
| `XIDSQN` | `NUMBER` |  | Transaction ID sequence number |
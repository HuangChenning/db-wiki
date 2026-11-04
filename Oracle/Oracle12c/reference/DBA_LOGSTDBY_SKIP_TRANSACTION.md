---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_SKIP_TRANSACTION.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGSTDBY_SKIP_TRANSACTION` displays the skip settings chosen. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `XIDUSN` | `NUMBER` |  | Transaction ID undo segment number |
| `XIDSLT` | `NUMBER` |  | Transaction ID slot number |
| `XIDSQN` | `NUMBER` |  | Transaction ID sequence number |
| `CON_NAME` | `VARCHAR2(384)` |  | Container name |
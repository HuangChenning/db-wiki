---
title: DBA_LOGSTDBY_UNSUPPORTED_TABLE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4129.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGSTDBY_UNSUPPORTED_TABLE` displays the data tables that are not supported by Logical Standby. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the unsupported table |
---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_LOGSTDBY_UNSUPPORTED_TABLE.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.172 DBA\_LOGSTDBY\_UNSUPPORTED\_TABLE

`DBA_LOGSTDBY_UNSUPPORTED_TABLE` displays the data tables that are not supported by Logical Standby.

The data displayed pertains to the container in which the view is queried. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the unsupported table |
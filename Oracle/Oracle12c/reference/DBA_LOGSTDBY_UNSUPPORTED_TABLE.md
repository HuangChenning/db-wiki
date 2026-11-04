---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_LOGSTDBY_UNSUPPORTED_TABLE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_LOGSTDBY_UNSUPPORTED_TABLE` displays the data tables that are not supported by Logical Standby.

The data displayed pertains to the container in which the view is queried. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the unsupported table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the unsupported table |
---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RSRC_GROUP_MAPPINGS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RSRC_GROUP_MAPPINGS` displays the mapping between session attributes and consumer groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Session attribute to match |
| `VALUE` | `VARCHAR2(128)` |  | Attribute value |
| `CONSUMER_GROUP` | `VARCHAR2(128)` |  | Target consumer group name |
| `STATUS` | `VARCHAR2(128)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |
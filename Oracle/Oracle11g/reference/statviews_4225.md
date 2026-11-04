---
title: DBA_RSRC_GROUP_MAPPINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4225.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_GROUP_MAPPINGS` displays the mapping between session attributes and consumer groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(30)` |  | Session attribute to match |
| `VALUE` | `VARCHAR2(128)` |  | Attribute value |
| `CONSUMER_GROUP` | `VARCHAR2(30)` |  | Target consumer group name |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |
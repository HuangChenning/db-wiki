---
title: DBA_RSRC_CONSUMER_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4224.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_CONSUMER_GROUPS` displays information about all resource consumer groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONSUMER_GROUP_ID` | `NUMBER` | `NOT NULL` | ID of the consumer group |
| `CONSUMER_GROUP` | `VARCHAR2(30)` |  | Name of the consumer group |
| `CPU_METHOD` | `VARCHAR2(30)` |  | CPU resource allocation method for the consumer group |
| `MGMT_METHOD` | `VARCHAR2(30)` |  | Resource allocation method for the consumer group |
| `INTERNAL_USE` | `VARCHAR2(3)` |  | Indicates whether the consumer group is for internal use only (`YES`) or not (`NO`) |
| `COMMENTS` | `VARCHAR2(2000)` |  | Text comment on the consumer group |
| `CATEGORY` | `VARCHAR2(30)` |  | Category of the consumer group |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |
| `MANDATORY` | `VARCHAR2(3)` |  | Indicates whether the consumer group is mandatory (`YES`) or not (`NO`) |
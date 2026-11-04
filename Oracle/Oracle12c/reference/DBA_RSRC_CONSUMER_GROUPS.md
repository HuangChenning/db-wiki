---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RSRC_CONSUMER_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RSRC_CONSUMER_GROUPS` displays information about all resource consumer groups in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CONSUMER_GROUP_ID` | `NUMBER` | `NOT NULL` | ID of the consumer group |
| `CONSUMER_GROUP` | `VARCHAR2(128)` |  | Name of the consumer group |
| `CPU_METHOD` | `VARCHAR2(128)` |  | CPU resource allocation method for the consumer group |
| `MGMT_METHOD` | `VARCHAR2(128)` |  | Resource allocation method for the consumer group |
| `INTERNAL_USE` | `VARCHAR2(3)` |  | Indicates whether the consumer group is for internal use only (`YES`) or not (`NO`) |
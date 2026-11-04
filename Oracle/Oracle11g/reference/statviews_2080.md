---
title: ALL_STREAMS_MESSAGE_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2080.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_MESSAGE_RULES` displays information about the Streams messaging rules accessible to the current user.

Related View

`DBA_STREAMS_MESSAGE_RULES` displays information about all Streams messaging rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(30)` |  | Name of the Streams client |
| `STREAMS_TYPE` | `VARCHAR2(11)` |  | Type of the Streams client: |
| `MESSAGE_TYPE_NAME` | `VARCHAR2(30)` |  | Name of the message type |
| `MESSAGE_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the message type |
| `MESSAGE_RULE_VARIABLE` | `VARCHAR2(30)` |  | Name of the variable in the message rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_CONDITION` | `VARCHAR2(4000)` |  | Rule condition |

See Also:

["DBA\_STREAMS\_MESSAGE\_RULES"](statviews_5008.md)
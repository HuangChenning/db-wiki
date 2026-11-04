---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_STREAMS_MESSAGE_RULES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_STREAMS_MESSAGE_RULES` displays information about the Streams messaging rules accessible to the current user.

Related View

`DBA_STREAMS_MESSAGE_RULES` displays information about all Streams messaging rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAMS_NAME` | `VARCHAR2(128)` |  | Name of the Streams client |
| `STREAMS_TYPE` | `VARCHAR2(11)` |  | Type of the Streams client:  - `PROPAGATION` - Streams propagation - `APPLY` - Streams apply process - `DEQUEUE` - Streams messaging client |
| `MESSAGE_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the message type |
| `MESSAGE_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the message type |
| `MESSAGE_RULE_VARIABLE` | `VARCHAR2(128)` |  | Name of the variable in the message rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_CONDITION` | `VARCHAR2(4000)` |  | Rule condition |

See Also:

- " [DBA\_STREAMS\_MESSAGE\_RULES](DBA_STREAMS_MESSAGE_RULES.md) "
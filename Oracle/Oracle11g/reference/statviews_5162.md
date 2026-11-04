---
title: REDACTION_POLICIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5162.htm
tags:
  - oracle
  - 11g
  - reference
---

`REDACTION_POLICIES` displays all redaction policies in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object with the policy |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object with the policy |
| `POLICY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the policy |
| `EXPRESSION` | `VARCHAR2(4000)` | `NOT NULL` | Expression for this policy |
| `ENABLE` | `VARCHAR2(7)` |  | Indicates whether the policy is enabled (`YES`) or not (`NO`) |
| `POLICY_DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the policy |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asopart1b.htm#ASOAG10135) for more information about Oracle Data Redaction
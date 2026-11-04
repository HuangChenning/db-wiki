---
title: "V$VPD_POLICY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3121.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$VPD_POLICY` displays all the fine-grained security policies and predicates associated with the cursors currently in the library cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Cursor address |
| `PARADDR` | `RAW(4 \| 8)` | Parent cursor address |
| `SQL_HASH` | `NUMBER` | SQL hash number |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier |
| `CHILD_NUMBER` | `NUMBER` | Cursor's child number under the parent |
| `OBJECT_OWNER` | `VARCHAR2(30)` | Owner of the object with the policy |
| `OBJECT_NAME` | `VARCHAR2(30)` | Name of the object with the policy |
| `POLICY_GROUP` | `VARCHAR2(30)` | Name of the policy group |
| `POLICY` | `VARCHAR2(30)` | Name of the policy |
| `POLICY_FUNCTION_OWNER` | `VARCHAR2(30)` | Owner of the policy function |
| `PREDICATE` | `VARCHAR2(4000)` | Predicate for the policy (truncated to `4000` bytes in length) |
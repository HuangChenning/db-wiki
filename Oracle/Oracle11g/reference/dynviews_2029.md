---
title: "V$LOCK_TYPE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2029.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOCK_TYPE` describes the type of locks available.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(64)` | A two-letter internal resource identifier |
| `NAME` | `VARCHAR2(64)` | Resource type name. This is a short (less than 32 characters) enqueue type name. |
| `ID1_TAG` | `VARCHAR2(64)` | Description of the enqueue type. |
| `ID2_TAG` | `VARCHAR2(64)` | Further description of the enqueue type. |
| `IS_USER` | `VARCHAR2(3)` | User enqueue. These are enqueues that are acquired as a direct result of a SQL statement. Applications may get deadlocks on these enqueues. Such deadlocks are considered application errors. |
| `DESCRIPTION` | `VARCHAR2(4000)` | Explanation of how or for what purpose the enqueue is used. |
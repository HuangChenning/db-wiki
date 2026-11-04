---
title: "V$CONTEXT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1086.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CONTEXT` displays set attributes in the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(31)` | Namespace that the attribute is in |
| `ATTRIBUTE` | `VARCHAR2(31)` | Name of the attribute |
| `VALUE` | `VARCHAR2(4000)` | Value of the attribute |
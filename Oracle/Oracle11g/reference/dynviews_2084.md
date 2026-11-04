---
title: "V$OPTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2084.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OPTION` displays Oracle Database options and features. Typically, although not always, options must be separately licensed, whereas features come with the product and are enabled based on the product that is running (Standard Edition, Enterprise Edition, and so on).

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Name of the option (or feature) |
| `VALUE` | `VARCHAR2(64)` | Indicates whether the option (or feature) is installed (`TRUE`) or not (`FALSE`) |

See Also:

[Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/toc.htm)
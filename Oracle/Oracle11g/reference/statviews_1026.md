---
title: ALL_CAPTURE_EXTRA_ATTRIBUTES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1026.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CAPTURE_EXTRA_ATTRIBUTES` displays information about the extra attributes for the capture processes accessible to the current user.

Related View

`DBA_CAPTURE_EXTRA_ATTRIBUTES` displays information about the extra attributes for all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the capture process |
| `ATTRIBUTE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the extra attribute |
| `INCLUDE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is included (`YES`) or not (`NO`) |
| `ROW_ATTRIBUTE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is a row LCR attribute (`YES`) or not (`NO`) |
| `DDL_ATTRIBUTE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is a DDL LCR attribute (`YES`) or not (`NO`) |

See Also:

["DBA\_CAPTURE\_EXTRA\_ATTRIBUTES"](statviews_3098.md)
---
title: ALL_ERRORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1086.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ERRORS` describes the current errors on the stored objects accessible to the current user.

Related Views

- `DBA_ERRORS` describes the current errors on all stored objects in the database.
- `USER_ERRORS` describes the current errors on the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object: - `VIEW` - `PROCEDURE` - `FUNCTION` - `PACKAGE` - `PACKAGE BODY` - `TRIGGER` - `TYPE` - `TYPE BODY` - `LIBRARY` - `JAVA SOURCE` - `JAVA CLASS` - `DIMENSION` |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | Sequence number (for ordering purposes) |
| `LINE` | `NUMBER` | `NOT NULL` | Line number at which the error occurred |
| `POSITION` | `NUMBER` | `NOT NULL` | Position in the line at which the error occurred |
| `TEXT` | `VARCHAR2(4000)` | `NOT NULL` | Text of the error |
| `ATTRIBUTE` | `VARCHAR2(9)` |  | Indicates whether the error is an error (`ERROR`) or a warning (`WARNING`) |
| `MESSAGE_NUMBER` | `NUMBER` |  | Numeric error number (without any prefix) |

See Also:

- ["DBA\_ERRORS"](statviews_3170.md)
- ["USER\_ERRORS"](statviews_5296.md)
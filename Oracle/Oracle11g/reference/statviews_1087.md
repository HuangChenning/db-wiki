---
title: ALL_ERRORS_AE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1087.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ERRORS_AE` describes the current errors on the stored objects (across all editions) accessible to the current user.

Related Views

- `DBA_ERRORS_AE` describes the current errors on all stored objects (across all editions) in the database.
- `USER_ERRORS_AE` describes the current errors on the stored objects (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object: - `TYPE` - `TYPE BODY` - `VIEW` - `PROCEDURE` - `FUNCTION` - `PACKAGE` - `PACKAGE BODY` - `TRIGGER` - `JAVA SOURCE` - `JAVA CLASS` |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | Sequence number (for ordering purposes) |
| `LINE` | `NUMBER` | `NOT NULL` | Line number at which this error occurred |
| `POSITION` | `NUMBER` | `NOT NULL` | Position in the line at which this error occurred |
| `TEXT` | `VARCHAR2(4000)` | `NOT NULL` | Text of the error |
| `ATTRIBUTE` | `VARCHAR2(9)` |  | Indicates whether the error is an error (`ERROR`) or a warning (`WARNING`) |
| `MESSAGE_NUMBER` | `NUMBER` |  | Numeric error number (without any prefix) |
| `EDITION_NAME` | `VARCHAR2(30)` |  | Name of the edition in which the object is actual |

See Also:

- ["DBA\_ERRORS\_AE"](statviews_3171.md)
- ["USER\_ERRORS\_AE"](statviews_5297.md)
---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ERRORS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.183 ALL\_ERRORS

`ALL_ERRORS` describes the current errors on the stored objects accessible to the current user.

Related Views

- `DBA_ERRORS` describes the current errors on all stored objects in the database.
- `USER_ERRORS` describes the current errors on the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object:  - `ANALYTIC` `VIEW` - `ASSEMBLY` - `ATTRIBUTE` `DIMENSION` - `DIMENSION` - `FUNCTION` - `HIERARCHY` - `JAVA` `CLASS` - `JAVA` `SOURCE` - `LIBRARY` - `PACKAGE` - `PACKAGE` `BODY` - `PROCEDURE` - `QUEUE` - `TRIGGER` - `TYPE` - `TYPE BODY` - `VIEW` |
| `SEQUENCE` | `NUMBER` | `NOT NULL` | Sequence number (for ordering purposes) |
| `LINE` | `NUMBER` | `NOT NULL` | Line number at which the error occurred |
| `POSITION` | `NUMBER` | `NOT NULL` | Position in the line at which the error occurred |
| `TEXT` | `VARCHAR2(4000)` | `NOT NULL` | Text of the error |
| `ATTRIBUTE` | `VARCHAR2(9)` |  | Indicates whether the error is an error (`ERROR`) or a warning (`WARNING`) |
| `MESSAGE_NUMBER` | `NUMBER` |  | Numeric error number (without any prefix) |

See Also:

- " [DBA\_ERRORS](DBA_ERRORS.md) "
	" [USER\_ERRORS](USER_ERRORS.md) "
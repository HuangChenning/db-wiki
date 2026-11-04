---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_ADMINISTRATOR.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_ADMINISTRATOR` displays information about the users who have been granted privileges to be a Streams administrator by procedures in the `DBMS_STREAMS_AUTH` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user who has been granted privileges to be a Streams administrator |
| `LOCAL_PRIVILEGES` | `VARCHAR2(3)` |  | Indicates whether the user has been granted local Streams administrator privileges (`YES`) or not (`NO`) |
| `ACCESS_FROM_REMOTE` | `VARCHAR2(3)` |  | Indicates whether the user can be used for remote Streams administration through a database link (`YES`) or not (`NO`) |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS514) for more information about the `DBMS_STREAMS_AUTH` package
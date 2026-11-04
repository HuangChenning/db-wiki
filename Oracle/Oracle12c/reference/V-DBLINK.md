---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-DBLINK.html
tags:
  - oracle
  - 12c
  - reference
---

`V$DBLINK` describes all database links (links with `IN_TRANSACTION = YES`) opened by the session issuing the query on `V$DBLINK`. These database links must be committed or rolled back before being closed.

| Column | Datatype | Description |
| --- | --- | --- |
| `DB_LINK` | `VARCHAR2(128)` | Name of the database link |
| `OWNER_ID` | `NUMBER` | Owner of the database link UID |
| `LOGGED_ON` | `VARCHAR2(3)` | Whether the database link is currently logged on |
| `HETEROGENEOUS` | `VARCHAR2(3)` | Whether the database link is heterogeneous |
| `PROTOCOL` | `VARCHAR2(6)` | Communication protocol for the database link |
| `OPEN_CURSORS` | `NUMBER` | Whether there are open cursors for the database link |
| `IN_TRANSACTION` | `VARCHAR2(3)` | Whether the database link is currently in a transaction |
| `UPDATE_SENT` | `VARCHAR2(3)` | Whether there has been an update on the database link |
| `COMMIT_POINT_STRENGTH` | `NUMBER` | Commit point strength of the transactions on the database link |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
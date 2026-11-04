---
title: "V$DBLINK"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1111.htm
tags:
  - oracle
  - 11g
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
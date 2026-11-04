---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OBJECT_DEPENDENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.95 V$OBJECT\_DEPENDENCY

`V$OBJECT_DEPENDENCY` displays the objects depended on by a package, procedure, or cursor that is currently loaded in the shared pool. For example, together with `V$SESSION` and `V$SQL`, this view can be used to determine which tables are used in the SQL statement that a user is currently executing.

See Also:

" [V$SESSION](V-SESSION.md) " and " [V$SQL](V-SQL.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `FROM_ADDRESS` | `RAW(4 \| 8)` | Address of a procedure, package, or cursor that is currently loaded in the shared pool |
| `FROM_HASH` | `NUMBER` | Hash value of a procedure, package, or cursor that is currently loaded in the shared pool |
| `TO_OWNER` | `VARCHAR2(64)` | Owner of the object that is depended on |
| `TO_NAME` | `VARCHAR2(1000)` | Name of the object that is depended on |
| `TO_ADDRESS` | `RAW(4 \| 8)` | Address of the object that is depended on. These can be used to look up more information on the object in `V$DB_OBJECT_CACHE`. |
| `TO_HASH` | `NUMBER` | Hash value of the object that is depended on. These can be used to look up more information on the object in `V$DB_OBJECT_CACHE`. |
| `TO_TYPE` | `NUMBER` | Type of the object that is depended on |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
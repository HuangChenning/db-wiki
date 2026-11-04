---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_OBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.34 DBA\_ADVISOR\_OBJECTS

`DBA_ADVISOR_OBJECTS` displays information about the objects currently referenced by all advisors in the database.

Each row in the view pertains to an object instantiation.

Related View

`USER_ADVISOR_OBJECTS` displays information about the objects currently referenced by the advisors owned by the current user. This view does not display the `OWNER` `ATTR21`, and `ATTR22` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Identifier of the object |
| `TYPE` | `VARCHAR2(64)` |  | Name of the type |
| `TYPE_ID` | `NUMBER` | `NOT NULL` | Type identifier number |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Task referencing the object |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` |  | The name of the task execution with which this entry (row) is associated |
| `ATTR1` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR2` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR3` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR4` | `CLOB` |  | Attributes and identifiers that cannot be expressed in the `ATTR1`, `ATTR2`, and `ATTR3` columns |
| `ATTR5` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR6` | `RAW(2000)` |  | Attributes and identifier of the object |
| `ATTR7` | `NUMBER` |  | Attributes and identifier of the object |
| `ATTR8` | `NUMBER` |  | Attributes and identifier of the object |
| `ATTR9` | `NUMBER` |  | Attributes and identifier of the object |
| `ATTR10` | `NUMBER` |  | Attributes and identifier of the object |
| `ATTR11` | `NUMBER` |  | Attributes and identifier of the object |
| `ATTR16` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR17` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR18` | `VARCHAR2(4000)` |  | Attributes and identifier of the object |
| `ATTR21` | `DATE` |  | Attributes and identifier of the object |
| `ATTR22` | `DATE` |  | Attributes and identifier of the object |
| `OTHER` | `CLOB` |  | Other attributes and identifiers of the object |
| `ADV_SQL_ID` | `VARCHAR2(13)` |  | If the object type is `SQL`, then this column contains the SQL identifier of the SQL statement. Otherwise, the value of this column is null. |

Note:

The definition of the `ATTRn` columns depends on the advisors that are using the object. For example, the `SQL` object type defines the attribute columns as follows:

- `ATTR1` contains the SQL ID
- `ATTR2` contains the SQL address (in the cursor cache)
- `ATTR4` contains the SQL text

See Also:

" [USER\_ADVISOR\_OBJECTS](USER_ADVISOR_OBJECTS.md) "
---
title: DBA_ADVISOR_RATIONALE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3027.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_RATIONALE` displays information about the rationales for all recommendations in the database.

Related View

`USER_ADVISOR_RATIONALE` displays information about the rationales for the recommendations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(30)` |  | The name of the task execution with which this entry (row) is associated |
| `REC_ID` | `NUMBER` |  | Recommendation associated with the rationale |
| `RATIONALE_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the rationale |
| `IMPACT_TYPE` | `VARCHAR2(4000)` |  | Impact on the system due to the problem described in the rationale. The impact can be described in terms of time, cost, or % degradation. |
| `IMPACT` | `NUMBER` |  | Calculated impact value |
| `MESSAGE` | `VARCHAR2(4000)` |  | Message containing an overview of the rationale |
| `OBJECT_ID` | `NUMBER` |  | Identifier of an object specified in the `DBA_ADVISOR_OBJECTS` view |
| `TYPE` | `VARCHAR2(30)` |  | Type of the rationale; defines what data exists in the attribute columns and how to interpret it: - `TEXT` - Text sentence for descriptive messages. The `ATTR1` column contains the text. - `CHART` - Chart containing data to be displayed. The `ATTR1` column contains the data. |
| `ATTR1` | `VARCHAR2(4000)` |  | Parameters defining the rationale |
| `ATTR2` | `VARCHAR2(4000)` |  | Parameters defining the rationale |
| `ATTR3` | `VARCHAR2(4000)` |  | Parameters defining the rationale |
| `ATTR4` | `VARCHAR2(4000)` |  | Parameters defining the rationale |
| `ATTR5` | `CLOB` |  | Parameters defining the rationale |

See Also:

["USER\_ADVISOR\_RATIONALE"](statviews_5209.md)
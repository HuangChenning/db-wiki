---
title: "V$AW_OLAP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1042.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$AW_OLAP` provides a record of active sessions and their use with analytic workspaces. A row is generated whenever an analytic workspace is created or attached. The first row for a session is created when the first command is issued. It identifies the `SYS.EXPRESS` workspace, which is attached automatically to each session. Rows related to a particular analytic workspace are deleted when the workspace is detached from the session or the session ends.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | A unique numeric identifier for a session |
| `AW_NUMBER` | `NUMBER` | A unique numeric identifier for an analytic workspace. To get the name of the analytic workspace, join this column to the `AW_NUMBER` column of the `USER_AWS` view or to the `AWSEQ#` column of the `AW$` table. |
| `ATTACH_MODE` | `VARCHAR2(10)` | `READ ONLY` or `READ WRITE` |
| `GENERATION` | `NUMBER` | The generation of an analytic workspace. Each UPDATE creates a new generation. Sessions attaching the same workspace between UPDATE commands share the same generation. |
| `TEMP_SPACE_PAGES` | `NUMBER` | The number of pages stored in temporary segments for the analytic workspace. |
| `TEMP_SPACE_READS` | `NUMBER` | The number of times data has been read from a temporary segment and not from the page pool. |
| `LOB_READS` | `NUMBER` | The number of times data has been read from the table where the analytic workspace is stored (the permanent LOB). |
| `POOL_CHANGED_PAGES` | `NUMBER` | The number of pages in the page pool that have been modified in this analytic workspace. |
| `POOL_UNCHANGED_PAGES` | `NUMBER` | The number of pages in the page pool that have not been modified in this analytic workspace. |
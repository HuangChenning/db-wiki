---
title: "V$MEMORY_DYNAMIC_COMPONENTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2060.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MEMORY_DYNAMIC_COMPONENTS` displays information about the dynamic SGA components. This view summarizes information based on all completed SGA resize operations since instance startup. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `CURRENT_SIZE` | `NUMBER` | Current size of the component |
| `MIN_SIZE` | `NUMBER` | Minimum size of the component since instance startup |
| `MAX_SIZE` | `NUMBER` | Maximum size of the component since instance startup |
| `USER_SPECIFIED_SIZE` | `NUMBER` | Value of the user parameter for the component |
| `OPER_COUNT` | `NUMBER` | Number of operations since instance startup |
| `LAST_OPER_TYPE` | `VARCHAR2(13)` | Last completed operation for the component: |
| `LAST_OPER_MODE` | `VARCHAR2(9)` | Mode of the last completed operation: |
| `LAST_OPER_TIME` | `DATE` | Start time of the last completed operation |
| `GRANULE_SIZE` | `NUMBER` | Granularity of the `GROW` or `SHRINK` operation |
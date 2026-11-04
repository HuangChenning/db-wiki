---
title: USER_ADDM_TASKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5198.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_ADDM_TASKS` displays information about the ADDM tasks owned by the current user. The view contains one row for each row in the related `USER_ADVISOR_TASKS` view that has `ADVISOR_NAME=ADDM` and `STATUS=COMPLETED`. Its columns (except for `OWNER`) are the same as those in ["DBA\_ADVISOR\_TASKS"](statviews_3041.md).
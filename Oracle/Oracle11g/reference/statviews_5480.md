---
title: USER_TAB_MODIFICATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5480.htm
tags:
  - oracle
  - 11g
  - reference
---

`USER_TAB_MODIFICATIONS` describes modifications to all tables owned by the current user that have been modified since the last time statistics were gathered on the tables. Its columns are the same as those in ["ALL\_TAB\_MODIFICATIONS"](statviews_2107.md).

Note:

This view is populated only for tables with the `MONITORING` attribute. It is intended for statistics collection over a long period of time. For performance reasons, the Oracle Database does not populate this view immediately when the actual modifications occur. Run the `FLUSH_DATABASE_MONITORING_INFO` procedure in the `DBMS_STATS` PL/SQL package to populate this view with the latest information. The `ANALYZE_ANY` system privilege is required to run this procedure.
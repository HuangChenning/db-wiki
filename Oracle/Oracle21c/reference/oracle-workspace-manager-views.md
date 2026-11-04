---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/oracle-workspace-manager-views.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.9 Oracle Workspace Manager Views

A number of data dictionary views are relevant only if you are using Oracle Workspace Manager:

- [`ALL_MP_GRAPH_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03004) and [`USER_MP_GRAPH_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03121)
- [`ALL_MP_PARENT_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03006) and [`USER_MP_PARENT_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03123)
- [`ALL_REMOVED_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03007) and [`USER_REMOVED_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM99101)
- [`ALL_VERSION_HVIEW`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03010)
- [`ALL_WM_CONS_COLUMNS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03012) and [`USER_WM_CONS_COLUMNS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03122)
- [`ALL_WM_CONSTRAINTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03014) and [`USER_WM_CONSTRAINTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03124)
- [`ALL_WM_IND_COLUMNS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03016) and [`USER_WM_IND_COLUMNS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03126)
- [`ALL_WM_IND_EXPRESSIONS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03018) and [`USER_WM_IND_EXPRESSIONS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03128)
- [`ALL_WM_LOCKED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03020) and [`USER_WM_LOCKED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03130)
- [`ALL_WM_MODIFIED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03030) and [`USER_WM_MODIFIED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03140)
- [`ALL_WM_RIC_INFO`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03040) and [`USER_WM_RIC_INFO`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03160)
- [`ALL_WM_TAB_TRIGGERS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03050) and [`USER_WM_TAB_TRIGGERS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03170)
- [`ALL_WM_VERSIONED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03060) and [`USER_WM_VERSIONED_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03180)
- [`ALL_WM_VT_ERRORS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03070), [`DBA_WM_VT_ERRORS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03107), and [`USER_WM_VT_ERRORS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03190)
- [`ALL_WORKSPACE_PRIVS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03080) and [`USER_WORKSPACE_PRIVS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03200)
- [`ALL_WORKSPACE_SAVEPOINTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03090) and [`USER_WORKSPACE_SAVEPOINTS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03210)
- [`ALL_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03100), [`DBA_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03115), and [`USER_WORKSPACES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03220)
- [`DBA_WM_SYS_PRIVS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03105)
- [`DBA_WORKSPACE_SESSIONS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03110)
- [`ROLE_WM_PRIVS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03120)
- [`USER_WM_PRIVS`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03150)
- [`WM_COMPRESS_BATCH_SIZES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03233)
- [`WM_COMPRESSIBLE_TABLES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03234)
- [`WM_EVENTS_INFO`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03235)
- [`WM_INSTALLATION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADWSM03230)
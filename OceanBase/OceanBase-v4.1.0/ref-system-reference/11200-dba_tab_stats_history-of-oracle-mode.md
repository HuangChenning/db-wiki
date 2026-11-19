---
title: DBA_TAB_STATS_HISTORY
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699111.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# DBA_TAB_STATS_HISTORY

DBA_TAB_STATS_HISTORY 
==========================================

功能 
-------------------

展示数据库中所有表的表统计修改历史记录。

相关视图 
---------------------

* ALL_TAB_STATS_HISTORY

  

* USER_TAB_STATS_HISTORY

  




字段说明 
---------------------



|     **字段名称**      |           **类型**            | **是否可以为 NULL** |  **描述**   |
|-------------------|-----------------------------|----------------|-----------|
| OWNER             | VARCHAR2(128)               | NO             | 表的所有者     |
| TABLE_NAME        | VARCHAR2(128)               | NO             | 表名        |
| PARTITION_NAME    | VARCHAR2(128)               | YES            | 分区名称      |
| SUBPARTITION_NAME | VARCHAR2(128)               | YES            | 子分区名称     |
| STATS_UPDATE_TIME | TIMESTAMP(6) WITH TIME ZONE | YES            | 更新统计信息的时间 |

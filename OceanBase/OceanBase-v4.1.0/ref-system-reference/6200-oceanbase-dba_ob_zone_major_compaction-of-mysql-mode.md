---
title: oceanbase.DBA_OB_ZONE_MAJOR_COMPACTION
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699274.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_ZONE_MAJOR_COMPACTION

oceanbase.DBA_OB_ZONE_MAJOR_COMPACTION
===========================================================


功能
-------------------

展示本租户各个 Zone 的合并信息。

字段说明
----------------------

|       字段名称        |      类型      | 是否可以为 NULL |                                                                                            描述                                                                                            |
|-------------------|--------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ZONE              | varchar(128) | NO         | Zone 名称                                                                                                                                                                                  |
| BROADCAST_SCN | bigint(20) unsigned   | NO         | 广播的合并版本号                                                                                                                                                                                 |
| LAST_SCN      | bigint(20) unsigned   | NO         | 上一次合并的版本号                                                                                                                                                                                |
| LAST_FINISH_TIME  | timestamp(6)   | NO         | 上一次合并结束时间                                                                                                                                                                                |
| START_TIME        | timestamp(6)   | NO         | 合并开始时间                                                                                                                                                                                   |
| STATUS            | varchar(10)  | NO         | <li> `IDLE`：没有在合并中   <li> `COMPACTION`：正在合并中   <li> `CHECKSUM`：校验 checksum    |

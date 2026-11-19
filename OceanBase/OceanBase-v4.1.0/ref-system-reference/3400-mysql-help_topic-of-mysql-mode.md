---
title: mysql.help_topic
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702026.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# mysql.help_topic

mysql.help_topic 
=====================================

**功能** 
---------------------------

与其他三个表 mysql.help_category、mysql.help_relation、mysql.help_keyword 合作生成 help 命令。

**相关表/视图** 
-------------------------------

* mysql.help_category

  

* mysql.help_relation

  

* mysql.help_keyword

  




字段说明 
-------------------------



|     **字段名称**     |     **类型**     | **是否可以为 NULL** | **描述** |
|------------------|----------------|----------------|--------|
| help_topic_id    | bigint(20)     | NO             | 主题 ID  |
| name             | varchar(64)    | NO             | 主题名    |
| help_category_id | bigint(20)     | NO             | 类目 ID  |
| description      | varchar(65535) | NO             | 描述     |
| example          | varchar(65535) | NO             | 示例     |
| url              | varchar(65535) | NO             | url 地址 |

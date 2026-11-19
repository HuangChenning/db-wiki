---
title: config_additional_dir
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702088.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# config_additional_dir

config_additional_dir 用于设置本地存储配置文件的多个目录，为了冗余存储多份配置文件。


|      **属性**      |                                                **描述**                                                 |
|------------------|-------------------------------------------------------------------------------------------------------|
| 参数类型             | 字符串列表              |
| 默认值              | <li> etc2   <li> etc3    |
| 取值范围             | NULL               |
| 是否重启 OBServer 节点生效 | 否                  |

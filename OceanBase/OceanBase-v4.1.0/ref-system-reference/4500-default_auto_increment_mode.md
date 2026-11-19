---
title: default_auto_increment_mode
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700987.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# default_auto_increment_mode

`default_auto_increment_mode` 用于设置默认的自增列自增模式。

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 字符串  |
| 默认值 | order |
| 取值范围 | <li>order：自增列数据保持递增<li>noorder：自增列只保证自增值唯一 |
| 是否重启 OBServer 节点生效 | 否 |

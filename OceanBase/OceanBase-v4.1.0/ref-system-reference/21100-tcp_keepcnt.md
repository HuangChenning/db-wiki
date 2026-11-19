---
title: tcp_keepcnt
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702108.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tcp_keepcnt

tcp_keepcnt 
================================

`tcp_keepcnt` 用于设置关闭一个非活跃连接之前的最大重试次数。


|        属性        |   描述    |
|------------------|---------|
| 参数类型             | 整数类型    |
| 默认值              | 10      |
| 取值范围             | \[1,+∞) |
| 是否重启 OBServer 节点生效 | 否       |

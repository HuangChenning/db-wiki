---
title: tcp_keepidle
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702109.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tcp_keepidle

tcp_keepidle 
=================================

`tcp_keepidle` 用于设置客户端连接上服务器后，如果没有数据发送，多久后会发送 Keepalive 探测分组，单位为秒。


|        属性        |    描述    |
|------------------|----------|
| 参数类型             | 时间类型     |
| 默认值              | 7200s    |
| 取值范围             | \[1s,+∞) |
| 是否重启 OBServer 节点生效 | 否        |

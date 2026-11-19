---
title: query_response_time_stats
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699373.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# query_response_time_stats

`query_response_time_stats` 用于设置是否启用 `information_schema.QUERY_RESPONSE_TIME` 视图的统计信息收集。

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 布尔类型 |
| 默认值 | False |
| 取值范围 | <li>True：启用<li>False：禁用 |
| 是否重启 OBServer 节点生效 | 否 |

---
title: open_cursors
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700971.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# open_cursors

open_cursors 
=================================

open_cursors 用于限制单个 Session 可以同时打开的游标数量。


|        属性        |     描述      |
|------------------|-------------|
| 参数类型             | 整型          |
| 默认值              | 50          |
| 取值范围             | \[0,65535\] |
| 是否重启 OBServer 节点生效 | 否           |

设置单个 Session 可以同时打开的游标数量为 `20`。示例如下：
```sql
obclient> ALTER SYSTEM SET open_cursors = 20;
```

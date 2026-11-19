---
title: plsql_optimize_level
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700974.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# plsql_optimize_level

plsql_optimize_level 
=========================================

plsql_optimize_level 用于指定编译优化级别。


|        属性        |                 描述                 |
|------------------|------------------------------------|
| 参数类型             | 整数类型                               |
| 默认值              | 1                                  |
| 取值范围             | 0：表示不开启优化 1：表示开启优化 |
| 是否重启 OBServer 节点生效 | 否                                  |



使用示例如下：

```sql
obclient> ALTER SYSDATE SET plsql_optimize_level=1;
```

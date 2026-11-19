---
title: plsql_debug
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700973.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# plsql_debug

plsql_debug 
================================

plsql_debug 用于指定是否编译成 debug 版本。


|        属性        |                                                     描述                                                     |
|------------------|------------------------------------------------------------------------------------------------------------|
| 参数类型             | 布尔类型                    |
| 默认值              | False                   |
| 取值范围             | <li> True：是   <li> False：否    |
| 是否重启 OBServer 节点生效 | 否                       |



使用示例如下：

```sql
obclient> ALTER SYSDATE SET plsql_debug=false;
```

---
title: "SQL 查询导致的异常"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702038.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SQL 查询导致的异常

#### 说明

- 其中 tenant_list 和 global 为可选字段，如果 tenant_list 没有指定，则清空所有租户的执行计划缓存，否则只清空指定租户的；如果 global 没有指定，则清空本机的执行计划缓存，否则清空该租户所在的所有 server 上的计划缓存，默认是最小范围。
- tenant_list 示例如下：tenant = 'tenant1, tenant2, tenant3....'

#### 注意

- 索引创建尽量包含全部所查询的列：包含的列越全越好，这样可以尽可能的减少回表的行数。

- 等值条件永远放在复合索引包含列的最前面。

- 过滤与排序数据量大的字段放在复合索引包含列的前面。

#### 说明

- 其中 EXECUTE_TIME 值，如果值过大，考虑存在等待事件或逻辑读次数异常多。

- RETRY_CNT 字段即 retry 次数，如果次数很多，则可能有锁冲突或切主等情况。

- QUEUE_TIME 过大，则表明 CPU 资源不够用。

- GET_PLAN_TIME 为获取执行计划的时间，如果如果时间很长，一般会伴随 IS_HIT_PLAN＝0，表示没有命中 plan。

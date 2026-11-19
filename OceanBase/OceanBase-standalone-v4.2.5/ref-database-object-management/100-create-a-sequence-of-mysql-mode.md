---
title: "创建序列"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150321.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建序列

#### 注意

- 如果同时指定 `MINVALUE` 和 `MAXVALUE`，则 `MINVALUE` 必须小于 `MAXVALUE`。
- `MAXVALUE` 和 `MINVALUE` 之差必须大于等于 `INCREMENT BY int_value`。
- `CACHE` 的值必须大于 `1`，如果 `CACHE INT_VALUE` 的值为 `1`，则等价于 `NOCACHE`。
- 指定了 `CYCLE`，且 `INCREMENT BY` 的值小于 `0` 时，必须指定 `MINVALUE`。
- 指定了 `CYCLE` 时，`CACHE` 的数量必须不能超过一个 `CYCLE`。

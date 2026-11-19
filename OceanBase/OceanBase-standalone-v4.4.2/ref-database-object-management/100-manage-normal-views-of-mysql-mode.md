---
title: "管理普通视图"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077681.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 管理普通视图

#### 注意

当过滤条件中使用 `WITH CHECK OPTION` 子句时：

- MySQL 模式应确保创建语句不能是 “不可更新视图”。
- 视图定义中暂不支持使用 `JOIN` 操作。

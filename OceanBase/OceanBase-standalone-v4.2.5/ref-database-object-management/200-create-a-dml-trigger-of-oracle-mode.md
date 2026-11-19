---
title: "创建 DML 触发器"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150383.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建 DML 触发器

#### 注意

当一个基表被修改（`INSERT`、`UPDATE` 或 DELETE）时要执行存储过程，执行触发器时根据其所依附的基表改动而自动触发，因此与应用程序无关，使用触发器可以保证数据的一致性和完整性。

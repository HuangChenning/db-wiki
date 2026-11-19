---
title: "创建索引"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077673.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建索引

#### 注意

多值索引可以定义为唯一索引。如果将其定义为唯一索引，尝试插入已存在于多值索引中的值会返回重复键错误。如果已经存在重复值，尝试添加唯一的多值索引会失败。

#### 注意

当前版本只支持创建局部全文索引。

---
title: "更改表"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577959.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 更改表

#### 注意

修改表的 Collation 和字符集设置仅影响后续添加的字符类型的列的数据保存方式，已有字符类型的列的数据保存方式不会被修改。

#### 注意

- 当前仅支持将行存表修改为列存表（`each column`）和将行存表修改为行存列存冗余格式的表（`all columns, each column`）时指定 `DELAYED`。
- 在执行 `DELAYED` 延迟操作行存表转列存表命令后，在基线数据实际完成合并前，由于数据存储格式没有真正的转换，查询性能可能不符合预期。

#### 说明

将通过设置 `WITH COLUMN GROUP(all columns)` 选项创建的行存表转换为列存表时，再设置 `ADD COLUMN GROUP(each column)` 后，还要执行 `DROP COLUMN GROUP(all columns)` 命令来删除这个列组。

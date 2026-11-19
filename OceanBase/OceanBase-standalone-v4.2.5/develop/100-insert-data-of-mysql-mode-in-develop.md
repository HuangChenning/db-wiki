---
title: "插入数据"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701992.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 插入数据

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 说明

- 指定 `ON DUPLICATE KEY UPDATE column_name = expr `：当要插入的主键或唯一键有重复时，可以使用 `column_name = expr ` 赋值语句来更新表中冲突行的数据。 `column_name = expr ` 赋值语句可以为冲突行赋某一列或几列的值。赋多列值时，列与列之间用逗号分隔。
- 不指定 `ON DUPLICATE KEY UPDATE column_name = expr `：当要插入的主键或唯一键有重复时，插入数据时，系统会报错。

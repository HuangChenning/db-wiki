---
title: "插入数据时提示重复的输入，错误代码 ERROR 1062"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702158.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 插入数据时提示重复的输入，错误代码 ERROR 1062

#### 说明

- 指定 `ON DUPLICATE KEY UPDATE column_name = expr`：当要插入的主键或唯一键有重复值时，可以使用 `column_name = expr` 赋值语句来更新表中冲突行的数据。`column_name = expr` 赋值语句可以为冲突行赋某一列或几列的值。赋多列值时，列与列之间用逗号分隔。
- 不指定 `ON DUPLICATE KEY UPDATE column_name = expr`：当要插入的主键或唯一键有重复值时，系统会报错。

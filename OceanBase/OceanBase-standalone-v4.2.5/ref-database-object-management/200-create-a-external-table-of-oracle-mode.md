---
title: "创建外表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150337.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建外表

#### 注意

如果需要手动定义列映射，则自动列映射功能将会失效，所有列都需要手动定义映射。

#### 注意

`local_file_path`必须是一个目录，而不是一个文件。如果需要制定单独的一个文件，需要在 `LOCATION` 中指定该文件的上层目录，并通过设置 `PATTERN` 属性来指定该文件。

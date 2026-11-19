---
title: "锁定查询结果 LOCK IN SHARE MODE"
book: "应用开发"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578093.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 锁定查询结果 LOCK IN SHARE MODE

#### 注意

OceanBase 数据库模拟了 `LOCK IN SHARE MODE` 共享锁语法的功能，使用写锁来实现，这样可以满足一些软件的兼容性需求，同时保证语法的正确性。由于使用写锁会使添加了 `LOCK IN SHARE MODE` 命令的读操作之间相互阻塞，因此一般不建议使用该语法，特别是在性能敏感的场景中更应该避免使用。

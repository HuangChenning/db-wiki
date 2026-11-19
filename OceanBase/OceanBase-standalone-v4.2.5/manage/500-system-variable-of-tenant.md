---
title: "租户系统变量"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701785.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 租户系统变量

OceanBase 数据库的租户系统变量分为全局变量和 Session 变量。通过系统变量的设置可以使 OceanBase 数据库的行为符合业务的要求。

- 全局变量：表示 Global 级别的修改，数据库同一租户内的不同用户共享全局变量。全局变量的修改不会随会话的退出而失效。此外，全局变量修改后，对当前已打开的 Session 不生效，需要重新建立 Session 才能生效。
- 会话变量：表示 Session 级别的修改。当客户端连接到数据库后，数据库会复制全局变量来自动生成 Session 变量。Session 变量的修改仅对当前 Session 生效。

系统变量与系统配置项的对比：

[TABLE]

## 相关文档

- [配置项和系统变量概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001499714)
- [查看系统变量](600-view-system-variables-of-tenant.md)
- [修改系统变量](700-modify-system-variables-of-tenant.md)

---
title: "概况"
book: "触发器"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_two_text1.html"
tags:
  - highgo
  - highgo-v9
  - guide-triggers
---

## 触发器

触发器是数据库的回调函数，可创建到表（分区或非分区均可）、视图及外表上，可以在指定的数据库事件发生时自动执行/调用。

触发器可分为行级触发器和语句级触发器：行级触发器，对于每个影响的行触发一次；语句级触发器，不管语句影响多少行，只针对语句触发一次。

触发器还可根据触发时间进行分类：BEFORE、AFTER、INSTEAD OF，分别称为 BEFORE 触发器、AFTER 触发器和 INSTEAD OF 触发器。BEFORE 触发器在事件开始前触发，可以用于跳过当前行的修改、修改要更新或插入的数据；AFTER 在事件结束时触发，可以用于返回结果。以上两种的语句触发器可定义在表、视图或外表上，而以上两种的行触发器仅可定义在表和外表上，不可以定义在视图上。INSTEAD OF 触发器仅可定义为行级触发器，在视图上定义。

下面的表格总结了哪些触发器类型可以被用在表、视图和外部表上：

| 何时 | 事件 | 行级 | 语句级 |
| --- | --- | --- | --- |
| BEFORE | INSERT/UPDATE/DELETE | 表和外部表 | 表、视图和外部表 |
| TRUNCATE | – | 表 |  |
| AFTER | INSERT/UPDATE/DELETE | 表和外部表 | 表、视图和外部表 |
| TRUNCATE | – | 表 |  |
| INSTEAD OF | INSERT/UPDATE/DELETE | 视图 | – |
| TRUNCATE | – | – |  |
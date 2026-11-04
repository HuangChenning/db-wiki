---
title: "INFORMATION_SCHEMA表"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql4.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## INFORMATION\_SCHEMA表

从V9.0.5开始支持以下information\_schema通用表:

| 表名 | 描述 |
| --- | --- |
| information\_schema.tables | 提供数据库中各个表的信息 |
| information\_schema.table\_privileges | 提供关于表级权限的信息 |
| information\_schema.partitions | 提供关于表分区的信息。该表中的每一行对应于一个被分区表的单个分区或子分区 |
| information\_schema.columns | 提供关于表中各列的信息 |
| information\_schema.column\_privileges | 提供关于列级权限的信息 |
| information\_schema.key\_column\_usage | 描述哪些关键列具有约束 |
| information\_schema.views | 提供数据库中视图的信息 |
| information\_schema.routines | 提供了关于存储过程（stored procedures）和存储函数（stored functions）的信息。该表不包括内建（native）函数或可加载的函数（loadable functions） |
| information\_schema.triggers | 提供关于触发器（Triggers）的信息 |
| information\_schema.table\_constraints | 用于描述哪些表具有约束（constraints） |
| information\_schema.schemata | 提供关于数据库的信息 |
| information\_schema.schema\_privileges | 提供关于模式（数据库）级权限的信息 |
| information\_schema.statistics | 提供有关表索引的信息 |
| information\_schema.collations | 提供每种字符集对应的排序规则（collation）信息 |
| information\_schema.character\_sets | 提供可用字符集的信息 |
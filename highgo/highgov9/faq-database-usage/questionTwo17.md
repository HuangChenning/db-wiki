---
title: "pg_dump 备份用户视图报错"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo17.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

## pg\_dump 备份报错

## 环境

- CPU：Hygon C86 7380 32-core Processor
- 操作系统：BigCloud Enterprise Linux For Euler 22.10 LTS
- 数据库版本：9.0.3.2
- 兼容模式：Oracle

## 问题描述及解决方法

**问题描述** ：

在使用 `pg_dump` 备份数据库时出现：

```sql
[highgo@zhzyglxtDB-1 ~]$ pg_dump -d hljzydb -U highgo -p 1521 -M oracle -s -Fp -f 20260302hljzydb_ddl.sql
for
pg_dump: 错误: 查询是: SELECT pg_catalog.pg_get_viewdef('7772761'::pg_catalog.oid) AS viewdef
```

**解决方法** ：

```
解决视图定义中的错误，并重建视图。
```
---
title: "瀚高数据库 V4.5 文档目录"
version: "V4.5"
tags:
  - highgo
  - highgo-v45
  - catalog
---

# 瀚高数据库 V4.5 文档目录

路径都相对于本文件所在的 `highgov45` 目录。检索时先选定一栏，再打开对应的 `contents.md`。

## 最佳实践

- `way-installation-deployment/contents.md`：安装实施类。介绍安全版、企业版单机与集群部署，以及流复制搭建。
- `way-configuration/contents.md`：配置类。介绍主机、密码算法、驱动连接、SSL、口令策略和扩展插件配置。
- `way-daily-use/contents.md`：日常使用类。汇集数据导入导出、对象管理、用户权限、表空间、复制和 SQL 使用实践。
- `way-operations-guide/contents.md`：运维指导类。汇集主备判断、性能优化、服务检查、日志、备份恢复和 HAC 集群运维实践。

## SQL开发指南

- `sql-separation-of-duties/contents.md`：三权分立。介绍系统管理员、安全保密管理员和安全审计员的权限分立机制。
- `sql-data-preparation/contents.md`：数据准备。介绍登录、用户切换和 psql 等 SQL 开发准备工作。
- `sql-data-definition/contents.md`：数据定义。介绍 CREATE、DROP、ALTER 和约束等数据定义操作。
- `sql-data-manipulation/contents.md`：数据操纵。介绍 INSERT、UPDATE 和 DELETE 数据操纵语句。
- `sql-data-query/contents.md`：数据查询。介绍表达式、连接、分组、排序、组合查询和子查询。
- `sql-data-control/contents.md`：数据控制。概述 SQL 数据控制相关能力。
- `sql-data-types/contents.md`：数据类型。介绍数字、货币、字符、二进制、日期时间、布尔、枚举和数组等类型。
- `sql-built-in-functions/contents.md`：常用内置函数。介绍数学、三角、字符串、格式化和聚集函数。
- `sql-triggers/contents.md`：触发器。介绍触发器的创建、管理、删除和事件触发器。
- `sql-stored-procedures-functions/contents.md`：存储过程&函数。介绍函数定义、条件控制、循环遍历和打印输出。

## 开发手册

- `develop-installation-manual/contents.md`：HGDB-SEE V4.5.8 安装手册。介绍 HGDB-SEE V4.5.8 的安装环境、准备和实施过程。
- `develop-sql-command-quick-reference/contents.md`：HGDB SQL命令速查手册。提供 HGDB SQL 命令速查资料。
- `develop-security-management/contents.md`：HGDB 安全管理手册。介绍身份认证、访问控制、安全审计、数据安全和资源限制。
- `develop-sql-language-basics/contents.md`：HGDB-SEE V4.5 SQL语言基础。系统介绍 SQL 语法、数据定义与操作、查询、类型、函数、索引和并发控制。

## 常见问题

- `faq-application-development/contents.md`：开发应用类。汇集关键字处理和序列权限等应用开发问题。
- `faq-connections/contents.md`：连接使用类。汇集管理工具、ODBC、psql、JDK 和客户端连接问题。
- `faq-migration-compatibility/contents.md`：迁移兼容类。汇集 Oracle 等迁移兼容问题。
- `faq-database-usage/contents.md`：数据库使用类。汇集复制、备份、存储、安装、维护和资源故障问题。

## 产品插件

- `extensions-list/contents.md`：插件列表。列出瀚高数据库 V4.5 和 V9.0 的产品插件支持情况。

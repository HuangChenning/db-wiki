---
title: 达梦数据库 DM8 文档目录
version: "DM8"
tags:
  - dameng
  - dm8
  - catalog
---

# 达梦数据库 DM8 文档目录

路径都相对于本文件所在的 `html-to-md` 目录。检索时先选定一栏，再打开对应的 `contents.md`。

## 产品手册 / 安装与初始化

- `installation/contents.md`：DM8 安装手册。安装、卸载、许可证和配置工具。
- `dminit/contents.md`：DM8 dminit 使用手册。用 dminit 初始化数据库。
- `fast-loader/contents.md`：DM8 快速装载工具使用手册。用快速装载工具批量导入数据。
- `linux-scripts/contents.md`：DM8 Linux 脚本使用手册。Linux 上的安装和运维脚本。
- `dmdbchk/contents.md`：DM8 dmdbchk 使用手册。用 dmdbchk 检查数据库。

## 产品手册 / 管理

- `administrator/contents.md`：DM8 系统管理员手册。实例结构、对象管理、调优、备份恢复和升级。
- `security/contents.md`：DM8 安全管理。用户、权限、审计和加密等安全配置。
- `job-system/contents.md`：DM8 作业系统使用手册。作业的创建、调度和监控。
- `system-packages/contents.md`：DM8 系统包使用手册。内置系统包的用法。
- `backup-restore/contents.md`：DM8 备份与还原。数据库备份和还原。

## 产品手册 / SQL 与开发

- `sql-language/contents.md`：DM8 SQL 语言使用手册。SQL 语句、函数和数据类型。
- `sql-programming/contents.md`：DM8 SQL 程序设计。存储过程、函数和程序块。
- `disql/contents.md`：DM8 DIsql 使用手册。DIsql 命令行工具。
- `programmer/contents.md`：DM8 程序员手册。DPI、ODBC、JDBC 和 .NET 编程接口。
- `proc/contents.md`：DM8 PROC 使用手册。嵌入式 SQL 预编译器 PROC。
- `dmpython/contents.md`：DM8 dmPython 使用手册。用 Python 连接达梦并执行 SQL。

## 产品手册 / 高可用与集群

- `data-watch/contents.md`：DM8 数据守护与读写分离集群。数据守护和读写分离的配置与切换。
- `dsc/contents.md`：DM8 数据共享集群。DSC 共享存储集群。
- `mpp/contents.md`：DM8 大规模并行处理MPP。MPP 并行处理集群。
- `dpc/contents.md`：DM8 分布计算集群。分布式计算集群的部署和使用。

## 产品手册 / 工具与迁移

- `dexp-dimp/contents.md`：DM8 dexp 和 dimp 手册。逻辑导出 dexp 和导入 dimp。
- `dts/contents.md`：DM8 数据迁移工具 DTS。用 DTS 迁移、对比和转换数据。
- `dmdem/contents.md`：DMDEM 达梦企业管理系统。企业管理系统的使用说明和版本说明。

## 快速上手

- `start-versions/contents.md`：DM 数据库版本介绍。版本区别和安装包获取。
- `start-install/contents.md`：DM 数据库安装。Windows 和 Linux 上的安装、实例和启停。
- `start-tools/contents.md`：DM 数据库工具介绍。管理工具、迁移工具、DIsql、监视器和 SQLark。
- `start-basics/contents.md`：DM 数据库基本操作。表空间、用户、权限和对象的基本操作。
- `start-migration/contents.md`：DM 数据移植。从 Oracle、MySQL、PostgreSQL、SQL Server、DB2 迁到达梦。
- `start-dev/contents.md`：DM 应用程序开发。各语言连接达梦的入门示例。
- `start-clusters/contents.md`：DM 数据库集群介绍。数据守护、共享存储和分布式集群简介。
- `start-dmdrs/contents.md`：达梦数据复制软件DMDRS。DMDRS 的介绍、安装和功能。

## 运维指南

- `ops-deploy/contents.md`：数据库规范化部署。单机和各类集群的安装部署。
- `ops-monitor/contents.md`：数据库运维监控。系统资源、实例状态和监控工具。
- `ops-health/contents.md`：数据库健康检查。系统、实例和集群的健康检查。
- `ops-backup/contents.md`：数据库备份还原。物理备份、逻辑备份和实战案例。
- `ops-performance/contents.md`：性能诊断与优化。性能诊断和优化步骤。
- `ops-troubleshoot/contents.md`：故障诊断与排除。SQL、实例和人为操作故障。

## 应用开发指南

- `app-java/contents.md`：JAVA 语言。JDBC 以及 Hibernate、MyBatis、Spring 等框架。
- `app-c/contents.md`：C/C++ 语言。ODBC、DPI、Pro*C 和 QODBC。
- `app-dotnet/contents.md`：.NET 语言。.NET Data Provider 和 Dapper。
- `app-php/contents.md`：PHP 语言。PHP 连接达梦。
- `app-python/contents.md`：Python 语言。dmPython、Django、SQLAlchemy 和 Flask。
- `app-go/contents.md`：GO 语言。Go 的 ODBC、GORM 和 DM 接口。
- `app-javascript/contents.md`：JavaScript 语言。Node.js 连接达梦。

## SQL 开发指南

- `sql-practice/contents.md`：SQL 基础实践。查询、DML、函数、触发器、过程和视图。
- `sql-advanced/contents.md`：SQL 进阶技巧。分区表和层次查询。
- `sql-dmpl/contents.md`：DM_SQL。DMSQL 数据类型、异常、集合和包。
- `sql-best-practice/contents.md`：开发最佳实践。读写分离集群的开发原则。

## 常见问题

- `faq-product/contents.md`：产品常见问题。达梦产品相关问答。
- `faq-install/contents.md`：安装部署常见问题。单机安装、集群部署、实例启动和访问。
- `faq-ops/contents.md`：运维常见问题。检查、变更、备份、故障和配置。
- `faq-sql/contents.md`：SQL 常见问题。语法、函数、查询和错误码。
- `faq-migrate/contents.md`：迁移常见问题。从 Oracle、MySQL、SQL Server 和其他库迁移。
- `faq-ha/contents.md`：高可靠常见问题。Data Watch、DSC 和 DMDPC。
- `faq-dev/contents.md`：应用开发常见问题。各语言和第三方工具适配。
- `faq-ecosystem/contents.md`：生态工具与套件问题。DMHS、DMETL、DMDRS 和 DMDEM。

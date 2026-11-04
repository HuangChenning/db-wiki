---
title: Oracle Database 11g Release 2 文档目录
version: "11.2"
tags:
  - oracle
  - 11g
  - catalog
---

# Oracle Database 11g Release 2 文档目录

路径都相对于本文件所在的 `html-to-md` 目录。检索时先选定一本书，再打开该书的 `contents.md`。
各书目录里的 `index.md` 是 Oracle 原书字母索引，不是本文件。

## 概念与升级

- `concepts/contents.md`：Concepts（E40540-04）。数据库体系结构、事务、存储、进程和数据字典。
- `new-features-guide/contents.md`：New Features Guide（E41360-06）。11.2 各补丁版本的新特性。
- `readme/contents.md`：Readme（E41331-17）。本版本的安装与已知问题说明。
- `upgrade-guide/contents.md`：Upgrade Guide（E23633-11）。从旧版本升级到 11.2 的步骤和兼容性。

## 管理、参数与排错

- `administrators-guide/contents.md`：Administrator's Guide（E25494-07）。建库、启动关闭、表空间、用户、调度和诊断。
- `administrators-reference-for-linux-and-unix-based-operating-systems/contents.md`：Administrator's Reference for Linux and UNIX-Based Operating Systems（E10839-25）。Linux 和 UNIX 上的 Oracle 管理命令与操作系统集成。
- `performance-tuning-guide/contents.md`：Performance Tuning Guide（E41573-04）。实例调优、SQL 调优、等待事件和统计信息。
- `utilities/contents.md`：Utilities（E22490-08）。Data Pump、SQL*Loader、外部表和 DBVERIFY 等工具。
- `reference/contents.md`：Reference（E40402-18）。初始化参数、静态数据字典视图和动态性能视图。
- `error-messages/contents.md`：Error Messages（E17766-03）。ORA-、PLS-、TNS- 等错误号的原因和处理。

## 高可用、集群与存储

- `high-availability-overview/contents.md`：High Availability Overview（E17157-09）。高可用架构和 MAA 方案概览。
- `high-availability-best-practices/contents.md`：High Availability Best Practices（E10803-06）。最大可用架构的配置和运维实践。
- `data-guard-concepts-and-administration/contents.md`：Data Guard Concepts and Administration（E41134-03）。Data Guard 物理/逻辑备库的概念和管理。
- `data-guard-broker/contents.md`：Data Guard Broker（E40771-07）。用 Broker 配置和切换 Data Guard。
- `real-application-clusters-administration-and-deployment-guide/contents.md`：Real Application Clusters Administration and Deployment Guide（E41960-04）。RAC 集群的管理和部署。
- `real-application-clusters-installation-guide-for-linux-and-unix/contents.md`：Real Application Clusters Installation Guide for Linux and UNIX（E41962-05）。在 Linux 和 UNIX 上安装 RAC。
- `real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit/contents.md`：Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)（E48195-02）。在 Windows x64 上安装 RAC。
- `database-clusterware-administration-and-deployment-guide/contents.md`：Database Clusterware Administration and Deployment Guide（E41959-04）。Clusterware 的管理和部署。
- `grid-infrastructure-installation-guide-for-linux/contents.md`：Grid Infrastructure Installation Guide for Linux（E41961-10）。在 Linux 上安装 Grid Infrastructure。
- `automatic-storage-management-administrators-guide/contents.md`：Automatic Storage Management Administrator's Guide（E18951-03）。ASM 磁盘组和文件系统管理。
- `real-application-testing-users-guide/contents.md`：Real Application Testing User's Guide（E41481-03）。Database Replay 和 SQL Performance Analyzer。

## 备份与恢复

- `backup-and-recovery-users-guide/contents.md`：Backup and Recovery User's Guide（E10642-08）。RMAN 备份、恢复和闪回的用法。
- `backup-and-recovery-reference/contents.md`：Backup and Recovery Reference（E10643-09）。RMAN 命令和恢复目录视图。

## 安全与网络

- `advanced-security-administrators-guide/contents.md`：Advanced Security Administrator's Guide（E40393-10）。网络加密、认证和数据安全选件。
- `database-vault-administrators-guide/contents.md`：Database Vault Administrator's Guide（E23090-13）。Database Vault 领域、规则和职责分离。
- `enterprise-user-security-administrators-guide/contents.md`：Enterprise User Security Administrator's Guide（E10744-04）。企业用户、目录服务和共享 schema。
- `net-services-administrators-guide/contents.md`：Net Services Administrator's Guide（E41945-03）。监听器、命名方法、连接和网络配置。
- `net-services-reference/contents.md`：Net Services Reference（E10835-13）。listener.ora、tnsnames.ora 和网络参数。

## SQL 与开发

- `sql-language-reference/contents.md`：SQL Language Reference（E41084-04）。SQL 语句、函数、数据类型和语法图。
- `sql-language-quick-reference/contents.md`：SQL Language Quick Reference（E41085-04）。SQL 语法的简表。
- `pl-sql-language-reference/contents.md`：PL/SQL Language Reference（E25519-13）。PL/SQL 语言、游标、包和触发器语法。
- `pl-sql-packages-and-types-reference/contents.md`：PL/SQL Packages and Types Reference（E40758-03）。DBMS_、UTL_ 等内置包和类型。
- `jdbc-developers-guide/contents.md`：JDBC Developer's Guide（E16548-03）。用 JDBC 连接 Oracle 并执行 SQL。
- `sql-developer-users-guide/contents.md`：SQL Developer User's Guide（E12152-08）。SQL Developer 图形工具的用法。
- `sqlplus-users-guide-and-reference/contents.md`：SQL*Plus User's Guide and Reference（E16604-03）。SQL*Plus 命令、脚本和报表。
- `sqlplus-quick-reference/contents.md`：SQL*Plus Quick Reference（E16605-02）。SQL*Plus 命令语法简表。
- `sqlplus-release-notes/contents.md`：SQL*Plus Release Notes（E16608-03）。SQL*Plus 11.2 的版本说明。
- `data-cartridge-developers-guide/contents.md`：Data Cartridge Developer's Guide（E10765-02）。数据卡匣和可扩展索引的开发接口。

## 数据仓库

- `data-warehousing-guide/contents.md`：Data Warehousing Guide（E25554-02）。分区、物化视图、ETL 和查询重写。
- `olap-customizing-analytic-workspace-manager/contents.md`：OLAP Customizing Analytic Workspace Manager（E17237-01）。定制 Analytic Workspace Manager。

## 安装与网关

- `database-client-installation-guide-for-linux/contents.md`：Database Client Installation Guide for Linux（E24322-14）。在 Linux 上安装 Oracle 客户端。
- `database-examples-installation-guide/contents.md`：Database Examples Installation Guide（E24501-04）。安装示例 schema 和示例程序。
- `database-quick-installation-guide-for-linux-x86/contents.md`：Database Quick Installation Guide for Linux x86（E24324-06）。Linux x86 上的数据库快速安装。
- `database-quick-installation-guide-for-linux-x86-64/contents.md`：Database Quick Installation Guide for Linux x86-64（E24326-09）。Linux x86-64 上的数据库快速安装。
- `database-gateway-for-adabas-users-guide/contents.md`：Database Gateway for Adabas User's Guide（E12074-01）。通过网关访问 Adabas 数据。


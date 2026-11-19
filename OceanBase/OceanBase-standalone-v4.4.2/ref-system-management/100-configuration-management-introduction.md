---
title: "配置管理介绍"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077400.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 配置管理介绍

OceanBase 数据库通过设置配置项和系统变量来完成配置管理。

## 配置项

配置项主要用于运维，常用于控制机器及其以上级别的系统行为。可以作为节点启动参数和租户创建参数，也可以在节点运行时进行修改以调整系统行为。 有关配置项的详细介绍请参见 [设置参数](200-set-parameters.md)。

## 系统变量

系统变量通常和用户 Session 绑定，用于控制 Session 级别的 SQL 行为。

支持设置 Global 和 Session 级别的变量。设置 Global 级别的系统变量后，当前 Session 上不会生效，新建的任何 Session 都能读到新的变量值。设置 Session 级别的系统变量后，仅对当前 Session 生效。

有关系统变量的详细介绍请参见 [设置变量](300-set-variables.md)。

## 系统配置项和系统变量对比

[TABLE]

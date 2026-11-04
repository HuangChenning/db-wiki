---
title: FORCEVIEW
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle21.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## FORCEVIEW

## 说明

在创建视图时，指定FORCE选项后，当出现视图的基表不存在、引用了不存在的对象类型或者当前模式的拥有者不具有创建视图的权限这几种情况下，可以创建视图成功不会报错，但会出现警告提示信息。

语法支持CREATE和ALTER，其中ALTER语法仅支持COMPLIE。

语法如下：

## 示例

\--不存在table1时告警提示

highgo=# create or replace force view myforceview as select \* from table1;

WARNING: View created with compilation errors

CREATE VIEW

highgo=# alter view myforceview compile;

WARNING: View altered with compilation errors

ALTER VIEW

\--当创建对应table1后

highgo=# create table table1(id int);

CREATE TABLE

highgo=# alter view myForceview compile;

ALTER VIEW
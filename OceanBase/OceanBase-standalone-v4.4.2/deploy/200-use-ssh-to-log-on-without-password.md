---
title: "（可选）设置无密码 SSH 登录"
book: "部署集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076969.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# （可选）设置无密码 SSH 登录

#### 说明

此处需要为所用用户配置免密登录。若计划使用 admin 用户部署 OceanBase 集中式数据库，则需要为目标机器的 admin 用户配置免密。建议使用 admin 用户部署 OceanBase 集中式数据库。

#### 注意

您必须将脚本前两行的 **SERVERS** 列表和 **PASSWORD** 替换成您自己的实际机器列表和密码。

---
title: "发起恢复"
book: "常用工具"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004255601.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 发起恢复

#### 说明

入口一是从 **租户管理** 全局页面发起恢复，发起恢复时需填写或修改存储配置。入口二是从租户列表中选择的对应租户中发起恢复，发起恢复时可复用该租户的备份存储配置，无需填写或修改存储配置。

#### 说明

单击 **测试** 后，obshell 会测试待恢复的已备份文件的存储配置，测试成功后，**恢复源信息栏** 会显示对应的待恢复源租户名，若测试失败会报错，请填写正确的存储配置。

#### 说明

OceanBase 集中式数据库中 Unit 数量为 1。

#### 说明

在 OceanBase 集中式数据库中，副本个数只有一个且只能是全能型副本。

#### 说明

Unit 数量与 **各 Zone 的 Unit 数量** 配置一致，且不支持修改。

#### 说明

OceanBase 集中式数据库中仅存在一个 Zone。

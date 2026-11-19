---
title: "凭据管理"
book: "常用工具"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077112.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 凭据管理

#### 说明

obshell 自 V4.4.0 起支持凭据管理功能，您可访问 [阿里云镜像站](https://mirrors.aliyun.com/oceanbase/community/stable/el/?spm=a2c6h.25603864.0.0.1f4328b3mIcuek) 获取相应安装包，使用 obshell 直接进行升级，升级操作详参：[集群管理](100-ob-dashboard-cluster-management.md)。

#### 说明

目前凭据对象的授权类型仅支持密码验证，需确保使用该用户名和用户密码可以成功连接该凭据的应用主机的 IP 地址。

#### 说明

配置的 IP 地址不能存在已有凭据。

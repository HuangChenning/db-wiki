---
title: "轻量运维部署方案"
book: "部署集中式版"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701718.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 轻量运维部署方案

#### 注意

两种部署方案下虽然使用的安装包不同，但是其中 OceanBase 集中式数据库的能力是一致的。

#### 注意

轻量运维部署方案和平台运维部署方案使用的安装包不同，在获取安装包的时候，务必确保获取到相应的安装包。

#### 说明

可以通过 [OceanBase 官网软件下载中心](https://www.oceanbase.com/softwarecenter-standalone)获取集中式数据库安装包。该安装包配置有试用版许可证（非生产用途），有效期为 180 天，仅供您进行学习、测试或适配使用，不提供技术支持及 SLA 保障，不得用于营利性、商业性或生产目的。试用许可证过期后，您将无法继续使用数据库功能。如果您需要将软件用于生产环境，或营利性、商业性目的，并需要专业的技术支持保障，请联系 OceanBase 获取商业版许可。

#### 说明

部署 OceanBase 集中式数据库推荐使用 admin 用户，也可以使用其他用户(不推荐 root 用户)。但是要求用户具备 sudo 权限和作为数据库相关目录的所有者。

#### 注意

执行 `install_obd.sh` 不需要加 sudo 。

#### 说明

脚本会根据机器的资源情况自动获取集群资源配置的取值范围和默认值，机器资源情况不同时，输出的取值范围和默认值也不相同。

#### 注意

以下内容以 x86 架构的 CentOS Linux 7.9 镜像作为环境，其他环境可能略有不同。

#### 说明

您需根据您环境的真实情况修改下述参数。

#### 注意

在配置秘钥路径后，如果您的秘钥不需要口令，请注释或者删除 `password`，以免 `password` 被视为秘钥口令用于登录，导致校验失败。

#### 说明

若 OceanBase 集群中无需部署监控，您可略去本节配置。

#### 说明

`obagent` 组件下的 `servers` 配置需和 `oceanbase` 组件下保持一致。

#### 说明

本节中所使用命令的详细使用方法可参见官网《OceanBase 安装部署工具》文档中 [obd 常用命令](../common-tools/100-obd-commands.md) 中集群部署下的配置文件部署。

#### 说明

Hint 是特殊的注释，不受 `-c` 影响。

#### 注意

执行 `install_obd.sh` 命令不需要加 sudo 。

#### 说明

- 图形化界面默认使用 8680 端口，您可使用 `obd web -p <PORT>` 命令指定端口。
- 在阿里云或其他云环境下，可能出现程序无法获取公网 IP，从而输出内网地址的情况，此 IP 非公网地址，您需要使用正确的地址访问图形化界面。
- `obd web` 命令绑定在 0.0.0.0 上，在多网卡部署的情况下，您可通过任意一个可访问的 IP 访问图形化界面。
- 执行 `obd web` 命令不需要加 sudo 。

#### 说明

Grafana 组件的部署依赖 OBAgent 和 Prometheus 组件，Prometheus 组件的部署依赖 OBAgent 组件。具体体现如下：

- 勾选 Grafana 组件时会自动勾选 OBAgent 和 Prometheus 组件。
- 勾选 Prometheus 组件时会自动勾选 OBAgent 组件。
- 取消勾选 OBAgent 组件时会自动取消勾选 Grafana 和 Prometheus 组件。

#### 注意

配置与 OBServer 节点不同的节点，需要以下要求：

- obd 能访问到各个节点。
- 部署 Prometheus 的机器能够访问 OBServer 所在节点。

#### 注意

配置与 OBServer 节点不同的节点，需要以下要求：

- obd 能访问到各个节点。
- 部署 Grafana 的机器能够访问 OBServer 所在节点和 Prometheus 所在的节点。

#### 说明

在阿里云或其他云环境下，可能出现程序无法获取公网 IP，从而输出内网地址的情况，此 IP 非公网地址，您需要使用正确的地址访问图形化界面。

#### 说明

在创建 Oracle 模式时，白屏页面不支持设置密码，需用户在 Oracle 租户创建后，登录数据库手动设置密码。

#### 说明

自定义时，设置为 `%` 表示所有客户端都可以连接，存在访问安全风险，请谨慎操作。

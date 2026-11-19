---
title: "obd 常用命令"
book: "常用工具"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005105564.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# obd 常用命令

#### 说明

本文仅介绍部分常用命令，obd 命令的详细介绍可参见官网[《OceanBase 安装部署工具》](https://www.oceanbase.com/docs/obd-cn)文档 **obd 命令** 章节。

#### 说明

配置 sudo 免密是为了方便操作，您可在部署集群完成后手动去除 sudo 免密。

#### 说明

- `-p` 和 `--ssh-key-file` 二者仅需配置其一。

- `-u` 和 `--ssh-key-file` 选项自 obd V3.5.0 支持。

#### 说明

obd 自 V3.2.0 起新增 `obd host precheck` 命令，支持查看部署 OceanBase 数据库时建议修改的主机内核参数。并于 V3.5.0 增强命令功能，支持登录设置检查、系统权限检查等多种检查项。

#### 说明

- `-p` 和 `--ssh-key-file` 二者仅需配置其一。

- `-u` 和 `--ssh-key-file` 选项自 obd V3.5.0 支持。

#### 说明

在阿里云或其他云环境下，可能出现程序无法获取公网 IP，从而输出内网地址的情况，此 IP 非公网地址，您需要使用正确的地址访问图形化界面。

#### 说明

若仅停止指定组件，集群下的组件没有全部停止，集群不会进入到 `stopped` 状态。

#### 说明

若仅启动指定组件，集群下的组件没有全部启动，集群不会进入到 `running` 状态。

#### 说明

重启整个集群时，如果集群下的组件没有全部启动，集群不会进入到 `running` 状态。

#### 注意

部分配置项修改后需要执行 `obd cluster redeploy` 命令才会生效（如 `home_path`、`cluster_id`、`data_dir`、`redo_dir`、`obshell_port`、`zone`、`appname` 等），该命令会销毁集群并重新部署，您集群中的数据会丢失，请谨慎操作。

#### 注意

`obd cluster destroy` 命令不可逆，会在停止 observer 进程的同时清除数据库文件。因此执行以下命令前，请先确认集群已经不再使用，并且需要备份的数据已经完成备份。

#### 说明

如需删除租户，可执行 `obd cluster tenant drop` 命令删除，该命令会自动删除对应的资源单元和资源池。

#### 注意

在一主多备场景中，将一个备租户切换为主租户后，其他的备租户无法切换到新主租户下，您需自行选择解耦或对其他备租户执行 Failover 操作生成新的主租户。

#### 说明

不支持使用备份命令备份系统租户（sys 租户）。

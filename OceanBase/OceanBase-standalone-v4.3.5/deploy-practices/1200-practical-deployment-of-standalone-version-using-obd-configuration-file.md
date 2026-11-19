---
title: "使用 obd 配置文件部署集中式版实践"
book: "集中式版部署实践"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003582818.html"
tags:
  - oceanbase
  - standalone
  - deploy-practices
---

# 使用 obd 配置文件部署集中式版实践

#### 注意

OceanBase 数据库在 V4.2.5 BP3、V4.2.5 BP4、V4.2.5 BP5、V4.3.5 BP1、V4.3.5 BP2、V4.3.5 BP3 版本增加了对 X86 架构环境运行的指令集要求。OBServer 进程会在启动前检查当前环境是否支持 AVX 指令集，如果缺少该指令集会禁止启动。\
OceanBase 数据库自以下版本开始对 AVX 指令集的强制依赖策略已调整：

- 对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始不再强制要求 AVX 指令集支持。
- 对于 V4.2.5 版本，从 V4.2.5 BP6 版本开始不再强制要求 AVX 指令集支持。

#### 注意

如果一个挂载点的目录文件容量大于 16T，仅支持 XFS 类型。

#### 说明

- 此处因安装目录、日志保存目录及数据保存目录分别在不同的磁盘，所以需要在对应的目录下都查询 IOPS 情况。如果安装目录、日志保存目录及数据保存目录为同一磁盘，只需切换到该磁盘的挂载目录下，查询 IOPS 情况。

- 若服务器中无 fio 工具，可执行 `yum install -y fio` 命令安装。

#### 说明

`obd host user init`命令为 obd V3.5.0 新增命令，具体介绍可参见 [obd 常用命令](../common-tools/100-obd-commands.md) 中用户初始化内容。

#### 说明

`obd host init`命令为 obd V3.3.0 新增命令，具体介绍可参见 [obd 常用命令](../common-tools/100-obd-commands.md) 中主机初始化内容。

#### 注意

- 若 [参数配置](#参数配置) 小节采用 **使用 obd 命令配置** 且已经安装了 obd，此处可以跳过安装 obd 的步骤。
- 若 [参数配置](#参数配置) 小节采用 **手动配置** 方式并未安装 obd，此处需参照本步骤先安装 obd。

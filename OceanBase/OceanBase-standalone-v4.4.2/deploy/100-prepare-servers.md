---
title: "准备服务器"
book: "部署集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076963.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 准备服务器

#### 说明

- 磁盘中日志盘需要内存的 3 倍以上，数据盘要满足目标数据量的存储。
- OBServer 服务器内存设置建议不超过 1T。
- 这里列的资源需求指的是为 OceanBase 所预留的资源，而不是服务器本身的全部资源。

#### 说明

- 磁盘中日志盘需要内存的 3 倍以上，数据盘要满足目标数据量的存储。
- OBServer 服务器内存设置建议不超过 1T。
- 这里列的资源需求指的是为 OceanBase 所预留的资源，而不是服务器本身的全部资源。

#### 注意

OceanBase 集中式数据库在 V4.2.5 BP3、V4.2.5 BP4、V4.2.5 BP5、V4.3.5 BP1、V4.3.5 BP2、V4.3.5 BP3 版本增加了对 X86 架构环境运行的指令集要求。OBServer 进程会在启动前检查当前环境是否支持 AVX 指令集，如果缺少该指令集会禁止启动。\
OceanBase 集中式数据库自以下版本开始对 AVX 指令集的强制依赖策略已调整：

- 对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始不再强制要求 AVX 指令集支持。
- 对于 V4.2.5 版本，从 V4.2.5 BP6 版本开始不再强制要求 AVX 指令集支持。

#### 说明

操作系统需要配置网络和软件管理器（yum 或 zypper 源）。

#### 说明

不同的服务器修改 BIOS 的方式不同，具体操作请参见服务器操作手册。

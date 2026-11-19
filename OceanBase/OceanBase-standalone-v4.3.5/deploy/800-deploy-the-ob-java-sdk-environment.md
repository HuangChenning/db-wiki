---
title: "部署 OceanBase 集中式数据库 JAVA SDK 环境"
book: "部署集中式版"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577272.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 部署 OceanBase 集中式数据库 JAVA SDK 环境

#### 注意

如果需要使用 HDFS/ODPS 外表功能，并且 OceanBase 数据库是分布式部署，那么对应机器节点都需要进行如下的部署配置 JAVA 环境和安装依赖，不可仅设置某一节点。

#### 注意

所有环境配置和依赖安装操作均需以 admin 用户身份 执行。请通过以下方式切换用户。

#### 注意

请使用 OpenJDK 8 最新版本。

#### 注意

该路径用于配置当前 OBServer 运行节点上的 java home 目录，即对应配置项 [ob_java_home](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002525417) 的取值。

#### 注意

请下载 1.0.1 版本 devdeps-java-extensions RPM 安装包。

#### 注意

该路径用于配置 OBServer 启动的 jvm 可加载的可执行依赖 jar 包路径，即对应配置项 [ob_java_connector_path](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002525418) 的取值。

#### 说明

- 如果是初次使用 JAVA SDK 环境，不需要重启 observer 进程。
- 由于当前的 OBServer 支持的 JNI 相关配置项无法做到灵活的及时设置及时生效，所以如果需要尝试变更相关 java 环境变量的配置项，需要重启 observer 进程才可生效。

#### 注意

以下所有配置项均为集群配置，一次设置即可，不用所有节点单独设置。

#### 注意

以下设置均在 sys 租户中操作。

#### 说明

该路径来自于 OpenJDK JAVA 安装路径。

#### 说明

该路径来自于 jar 包 RPM 安装路径。

#### 注意

- 该配置项变更需要重启 observer 进程，由于当前的 HDFS 对接使用的内存拷贝为 HDFS 数据流直接拷贝到 cpp 内存堆上，可以适当减少 `-Xmx2048m -Xms2048m` 的设置。
- gc 日志文件仅在配置文件夹路径存在时生成；若路径不存在，则不会生成。

#### 注意

HDFS JAVA SDK 不需要设置该配置项，其他配置项完全一样。

#### 说明

如果集群是通过 obd 部署，则可以使用 obd 命令重启；如果是通过 OCP 部署，则使用 OCP 进行重启。

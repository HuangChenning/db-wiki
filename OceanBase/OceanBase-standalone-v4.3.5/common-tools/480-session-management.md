---
title: "会话管理"
book: "常用工具"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005258215.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 会话管理

#### 说明

obshell 自 V4.4.0 起支持会话管理功能，您可访问 [阿里云镜像站](https://mirrors.aliyun.com/oceanbase/community/stable/el/?spm=a2c6h.25603864.0.0.1f4328b3mIcuek) 获取相应安装包，使用 obshell 直接进行升级，升级操作详参：[集群管理](100-ob-dashboard-cluster-management.md)。

#### 说明

您也直接可以在 **会话管理** 页面右上角输入会话 ID 检索对应会话详情。

#### 说明

关闭会话指终止给定的会话 ID（Client Session ID），关闭当前会话查询可终止连接当前正在执行的语句，但是会保持会话连接的原状，详细介绍参见 [KILL](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479616)。

#### 说明

会话统计中的来源指节点的 IP，由于集中式版只有一个节点，因此只有一个来源。

#### 说明

死锁自动检测是集群级别行为，默认是开启状态，若需关闭死锁自动检测，您可单击 **集群管理** 页面右上角 **···**，在下拉列表中单击 **关闭死锁自动检测** 按钮，在弹出的二次确认框中单击 **确定** 即可成功关闭。关闭后，可在 **集群管理** 页面开启死锁自动检测，步骤同关闭一致。

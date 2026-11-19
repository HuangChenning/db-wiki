---
title: "巡检服务管理"
book: "常用工具"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005258216.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 巡检服务管理

#### 说明

obshell Dashboard 自 V4.4.0 起支持巡检服务功能，您可访问 [阿里云镜像站](https://mirrors.aliyun.com/oceanbase/community/stable/el/?spm=a2c6h.25603864.0.0.1f4328b3mIcuek) 获取相应安装包，使用 obshell Dashboard 直接进行升级，升级操作详参：[集群管理](100-ob-dashboard-cluster-management.md)。

#### 说明

- 在发起巡检服务前，需确保已在 OBServer 节点安装 obdiag V3.7.2 或以上版本，或已在 **软件包管理** 上传 obdiag V3.7.2 或以上版本的安装包，否则无法成功发起巡检并提示“工作目录或系统路径下不存在可用的 obdiag(\>=3.7.2)，请上传或安装（升级）oceanbase-diagnostic-tool 包，前往 **软件包管理**”。obdiag 安装方法详见文档 [obdiag 安装](https://www.oceanbase.com/docs/common-obdiag-cn-1000000004494302)。
- 如果集群中存在多个节点，发起巡检前需要存在各节点间的凭据，用于 obdiag 所在节点通过凭据中记录的 SSH 凭据连接集群中其它节点，否则可能发起失败，新建凭据详见文档 [凭据管理](650-credential-management.md)。
- 由于集中式版仅有一个节点，因此在发起巡检前不需要新建凭据。

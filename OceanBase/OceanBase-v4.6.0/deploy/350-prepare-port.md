---
title: "环境检查清单"
book: "OceanBase 部署"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007052293.html"
tags:
  - oceanbase
  - distributed
  - deploy
---

# 环境检查清单

#### 注意

如果安装包下载目录空间不足，OAT 在拉取镜像或安装过程中会直接报错失败。请在部署前确认目录空间充足，必要时扩容或更换目录。

#### 说明

此问题在自动化部署中较为常见，许多部署脚本在后台非交互式环境中运行，而 \`.bashrc\` 中的某些命令只适合交互式 shell。建议在所有待部署服务器上部署前统一完成此项检查。

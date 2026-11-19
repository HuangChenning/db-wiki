---
title: "组件用户准备说明"
book: "OceanBase 部署"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007052294.html"
tags:
  - oceanbase
  - distributed
  - deploy
---

# 组件用户准备说明

#### 注意

OceanBase \`observer\` 进程通常以 \`admin\` 用户运行，切换运行用户可能导致目录权限问题。请确保运行用户对数据目录有适当权限。

#### 注意

OAT 会自动创建 \`admin\` 用户且无法更改，这与需要手动创建 \`admin\` 系统用户的 OBServer 逻辑不同，部署时注意区分。

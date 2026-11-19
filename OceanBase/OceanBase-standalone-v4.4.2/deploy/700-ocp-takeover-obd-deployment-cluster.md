---
title: "使用 OCP 接管 obd 部署的集中式数据库"
book: "部署集中式版"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006076873.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 使用 OCP 接管 obd 部署的集中式数据库

#### 说明

- 本文以待接管集中式数据库的部署名为 myoceanbase 为例，您需根据实际部署名进行修改。部署名可执行 `obd cluster list` 命令查看，输出中的 `Name` 字段即为部署名。

- 本文所用 obd 命令的详细介绍可参见 [集群命令组](https://www.oceanbase.com/docs/common-obd-cn-1000000003892230)。

#### 说明

proxyro 账号的密码用于 OBProxy 访问 OceanBase 集群，集中式数据库不存在 OBProxy，因此此处可以选择不开启 `录入 proxyro 账号的密码`。

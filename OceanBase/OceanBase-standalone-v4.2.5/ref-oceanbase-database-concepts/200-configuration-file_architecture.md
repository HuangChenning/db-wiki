---
title: "配置文件"
book: "系统原理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150074.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 配置文件

#### 说明

集群级配置项仅支持在系统租户下配置。

#### 说明

执行成功以后，所有被指定的租户的配置项均会被修改。

#### 说明

- `all`：从 V4.2.1 版本开始，`tenant = all` 和 `tenant = all_user` 具有相同的语义，都表示对所有用户租户生效。`all` 语法即将被废除，不再推荐使用。
- `all_user`：对所有用户租户生效。
- `all_meta`：对所有 META 租户生效。

#### 说明

`PARAM_OPTS` 表示设置配置项所使用的其它限定条件，比如：指定 Zone、指定 OBServer 节点等。

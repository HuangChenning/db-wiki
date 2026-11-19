---
title: "RPC 连接认证"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577537.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# RPC 连接认证

#### 说明

`_enable_pkt_nio` 用于控制 RPC 网络框架 pkt-nio 的启用和关闭，默认值为 True。

#### 说明

- 默认安装目录路径：/home/admin/oceanbase。
- wallet 文件夹及文件夹下的文件名不能更改。
- 请确保所需的证书文件就绪后再开启认证，否则，会导致认证失败，进而服务不可用。

#### 注意

虽然将服务端认证方式设置为 `ALL`（即 `ALTER SYSTEM SET rpc_server_authentication_method = 'ALL';` ）也可以开启认证，但这也意味着服务端允许客户端不进行认证直接连接，存在较大的安全风险。因此，在生产环境下不建议采用这种方式。

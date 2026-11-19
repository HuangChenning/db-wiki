---
title: "附：安装配置 OCI"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577891.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 附：安装配置 OCI

#### 注意

将 OCI 安装目录中的 10 个 so 文件拷贝到 OceanBase 数据库节点的安装目录下后，再在安装目录下将 `libclntsh.so.12.1` 文件拷贝一份并重命名为 `libclntsh.so`（或者也可以在安装目录下建立一个指向安装目录中 `libclntsh.so.12.1` 库文件的软链接，并将软连接命名为 `libclntsh.so`）。

#### 注意

配置环境变量时，`/home/admin/oceanbase/lib`后面的冒号（:）必须加上。

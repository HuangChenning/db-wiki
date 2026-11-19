---
title: "通过 ODC 连接 OceanBase 数据库"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077438.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 通过 ODC 连接 OceanBase 数据库

#### 说明

ODC 第一次运行时，加载时间会比较长，请耐心等待。

#### 说明

主机名和端口号可从连接的数据库所在租户信息页面获取，如在公有云或 OCP 上创建的租户。

#### 说明

- 如配置信息有误，会出现异常提示，例如用户或密码不对、网络异常等。
- 用户只可连接本租户下的数据库，否则会报出测试失败的错误。
- ODC V4.0.0 及之后版本支持不填账号密码即可保存连接。

#### 说明

MySQL 模式下，如不指定默认库，则默认连接 information_schema 库。 如 information_schema 库连接失败，请将默认数据库设置为该用户有权限的库。

#### 说明

- 自 ODC V2.3.0 之后版本，导入导出功能需在创建连接的高级配置中设置 root@sys 用户。
- 自 ODC V2.4.1 之后版本，导入导出功能查询视图信息时取消 root@sys 账号强依赖（如未配置 root@sys 账号，ODC 部分对象如存储过程和函数等不支持导出功能；如配置 root@sys 账号，通过访问 `sys` 租户下的视图信息得到最优的数据路由策略，可提升导出速度）。
- **sys 租户账号和密码** 为集群租户下用户的账号和密码 (账号请勿填入“@sys#集群”)。例如：账号为 root。

#### 说明

保存前，可以单击**测试连接**进行数据库连接测试，如果数据库用户名和密码正确，则会提示**连接成功**。

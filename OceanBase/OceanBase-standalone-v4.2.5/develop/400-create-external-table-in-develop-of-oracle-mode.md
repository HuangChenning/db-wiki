---
title: "创建外表"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701950.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建外表

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 说明

默认情况下，外部文件中的数据列与外表定义的列是自动按顺序对应的，即外表的第一列对应外部文件中第一列的数据。当外部文件中的列顺序与外表中定义的列顺序不一致时，可以通过形如 \`metadata\$filecol{N}\` 的伪列来指定外表的列对应外部文件中的第 N 列。其中，文件中的列从 1 开始编号。

#### 注意

因为外表的其他属性未添加，所以上面的 SQL 语句不能运行。

#### 注意

对于使用本地 Location 格式的场景，需设置系统变量 `secure_file_priv` 配置可以访问的路径。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。

#### 注意

示例中涉及 IP 的命令做了脱敏处理，在验证时应根据自己机器真实 IP 填写。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。

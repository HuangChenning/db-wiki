---
title: "创建外表"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701982.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建外表

#### 注意

因为外表的其他属性未添加，所以上面的 SQL 语句不能运行。

#### 注意

对于使用本地 Location 格式的场景，需设置系统变量 `secure_file_priv` 配置可以访问的路径。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。

#### 注意

示例中涉及 IP 的命令做了脱敏处理，在验证时应根据自己机器真实 IP 填写。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502601)。

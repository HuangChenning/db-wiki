---
title: information_schema.CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699253.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# information_schema.CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS

information_schema.CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS
================================================================================

描述
--------------------

`information_schema.CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS` 用来展示不同用户登录失败的尝试次数。

字段说明
----------------------

|    **字段名称**     |    **类型**    | **是否可以为 NULL** |                             **描述**                             |
|-----------------|--------------|----------------|----------------------------------------------------------------|
| USERHOST        | varchar(261) | NO             | 表示登录失败的用户名和主机信息的组合，其格式为 `<user_name>@<hostname or ip address>` |
| FAILED_ATTEMPTS | bigint(20)   | NO             | 登录失败的尝试次数                                                      |

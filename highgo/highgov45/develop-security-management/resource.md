---
title: "6.资源限制"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/resource.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 6\. 资源限制

| 限制项 | 使用方式 | 取值 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| 用户的并发会话数量 | CREATE USER时指定CONNECTION LIMIT选项 | \-1-2147483647 | \-1（无限制） | 该限制仅针对于普通连接。预备事务和后台工作者连接都不受这一限制。 |
| 服务器的并发会话数量 | 修改参数max\_connections | 1-262143 | 100 | 该限制针对所有服务器连接。 |
| 会话最大空闲时间 | 设置安全参数hg\_clientnoinput | 0-1440（单位分钟） | 30（单位分钟） | 设置为0不限制。 |
| 导致用户被锁的密码输入次数 | 设置安全参数hg\_idcheck. pwdlock | 0-10 | 5 | 设置为0表示不限制密码错误次数。 |
| 密码错误导致的用户锁定的时长 | 设置安全参数hg\_idcheck.pwdlocktime | 0-240（单位小时） | 24（单位小时） | 设置为0表示一直被锁定。 |
| 用户密码有效期 | 设置安全参数hg\_idcheck.pwdvaliduntil | 0-365（单位天） | 7（单位天） | 设置为0表示不限制天数。 |
| 能够访问数据库的IP地址 | 设置pg\_hba.conf中的 *address* 项 | 无 | 无 |  |
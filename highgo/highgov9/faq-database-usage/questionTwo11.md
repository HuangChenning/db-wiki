---
title: "MySQL模式连接问题"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo11.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

## 问题1：

使用mysql兼容用户，工具连接报错。

![questionTwo11-1](img/questionTwo11-1.png)

pg\_hba文件内容如下。

![questionTwo11-2](img/questionTwo11-2.png)

解决方案：

pg\_hba.conf文件先走了md5的密码方式，调整文件内容，设置highgo用户走md5密码方式，mysql用户走mysql\_native\_password的方式解决。

![questionTwo11-3](img/questionTwo11-3.png)

## 问题2：

工具连接报错。

> Communications link failure
> 
> The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
> 
> Connection refused: no further information

![questionTwo11-4](img/questionTwo11-4.png)

解决方案：

MySQL模式监听地址没开放。

开放监听地址。

`alter system set mysql.listen_addresses = '*';`

重启数据库生效参数。

`pg_ctl  restart`

![questionTwo11-5](img/questionTwo11-5.png)
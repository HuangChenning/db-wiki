---
title: "4、使用安全版数据库开启ssl加密后jdbc写法"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/ssl_jdbc.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## 使用安全版数据库开启ssl加密后jdbc写法

**文档用途**

本文用于指导使用安全版数据库开启ssl加密后jdbc连接串写法。

默认写法会提示拒绝ssl连接，虽然可以通过关闭ssl等方法解决，但是在等保测评和数据库安全上会有隐患。

**详细信息**

jdbc写法如下：

```
jdbc.url=jdbc:highgo://数据库ip地址:5866/highgo?ssl=true&&sslfactory=com.highgo.jdbc.ssl.NonValidatingFactory
```
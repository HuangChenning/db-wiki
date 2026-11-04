---
title: "22、密码文件的格式和使用"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/password_use.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 密码文件的格式和使用

## 1、密码文件命名：

Windows上该文件被命名为%APPDATA%\\postgresql\\pgpass.conf，不清楚%APPDATA%路径，可以直接将其复制到windows资源管理器地址栏回车。

Unix上该文件被命名为$HOME.pgpass，$HOME为操作系统用户的家目录。

## 2、密码文件格式：

主机名或IP:端口号:数据库名:用户名:密码

1.冒号必须为英文半角冒号。

2.前四项可以使用\*以通配所有情况，但我们不建议这样设置。

3.在Unix系统中，权限请设置为600。

4.我们建议不要把superuser加入密码文件。

## 3、举例

```
192.168.100.103:5866:*:highgo:123456

192.168.100.103:5866:highgo:highgo:123456

192.168.9.156:*:*:highgo:123456

*:*:*:postgres:123456

*:*:*:*:123456
```
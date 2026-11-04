---
title: "3、瀚高数据库常用驱动连接字符串"
book: "配置类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/connect_string.html"
tags:
  - highgo
  - highgo-v45
  - way-configuration
---

## 瀚高数据库常用驱动连接字符串

## 1、常见驱动字符串示例

```
驱动：com.highgo.jdbc.Driver
 URL: jdbc:highgo://ip:端口号/数据库名
    jdbc:highgo://localhost:5866/highgo"（示例）
 用户名：highgo（示例）
 密码：highgo1（示例）
```

如果有类型选择建议添加如下选项

```
jdbc.type=postgre
```

## 2、测试工具连接字符串示例

以BenchmarkSQL为例（关于BenchmarkSQL工具使用请参考support文章：013750804）

① 使用HGDB驱动：

```
BenchmarkSQL:
db=highgo
driver=com.highgo.jdbc.Drive
conn=jdbc:highgo://localhost:5866/
```

② 使用工具自身驱动

```
BenchmarkSQL:postgresql
db=postgresql
driver=org.postgresql.com
conn=jdbc:postgresql://localhost:5866/
```
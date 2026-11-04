---
title: "2、数据库对象查询常用原命令"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/object_find.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 数据库常用原命令

## 1、查看当前实例中包含哪些用户

```
highgo=# \du
```

## 2、查看当前实例中包含哪些库，且各库大小

```
highgo=# \l+
```

## 3、查看当前实例中包含哪些表空间，且各表空间大小

```
highgo=# \db+
```

## 4、查看当前连接库中包含哪些表，且各表大小

```
highgo=# \dt+
```

注意\\dt+看到的表为当前库search\_path参数配置的模式下的各表，如需查看其他模式下的表大小，需执行\\d+ 模式.表名。

## 5、查看当前连接库中自定义函数

```
highgo=# \df
```

## 6、查看当前连接库中自定义序列

```
highgo=# \ds
```

## 7、查看当前连接信息

```
highgo=# \conninfo
```
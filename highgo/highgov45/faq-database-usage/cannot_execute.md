---
title: "12、cannot execute INSERT in a read-only transaction"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/cannot_execute.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## cannot execute INSERT in a read-only transaction

## 1、文档用途

解决cannot execute INSERT in a read-only transaction的问题

## 2、详细信息

在使用瀚高数据库遇到以上问题时，一般有两种情况：

第一种：当前数据库是个集群，应用系统或工具连接到了一个备节点上；此时更换连接到主节点就可以解决。

第二种：应用系统里代码加上了@Transactional注解 比如代码中有两个方法，A方法调用B方法，B方法执行数据库操作，加上了@Transactional注解，但是A没有加，就会导致cannot execute INSERT in a read-only transaction错误；此时将@Transactional补全或全都去掉都可以解决
---
title: "15、hgproxy配置黑名单，解决主备读取不一致的问题"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/hgproxy_black.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## hgproxy配置黑名单，解决主备读取不一致的问题

## 1、问题描述

高并发情况下，数据读取不一致。

## 2、问题原因

集群中使用了异步流复制，数据同步延迟造成。

## 3、解决方案

设置黑名单，将特定sql全部发往主节点查询。下为参考步骤。

### (1)配置参数

配置文件/opt/hgproxy/etc/proxy1.conf中，如下参数设置黑白名单

```
[BlackList]
black_regex_token_list          ='table1;Table2;TABLE3'    # 匹配到了发往主节点
white_regex_token_list          =                                # 匹配成功发往备节点
object_relationship_list        = /opt/hgproxy/etc/object_relationship_list.json
```

black\_regex\_token\_list

> 当希望特定的 SQL 发往主节点时，可以使用黑名单正则匹配。正则黑名单匹配成功发往主节点。配置时以分号分隔。配置时和下面white\_regex\_token\_list 冲突时，以黑名单为准。默认值为空

white\_regex\_token\_list

> 当希望特定的 SQL 发往备节点时，可以使用白名单正则匹配。正则白名单匹配成功发往备节点。配置时，以分号分隔。默认值为空

object\_relationship\_list

> 该参数配置文件绝对路径。该文件的功能是配置函数与表关系，表与表关系的文件路径。默认为“/opt/HighGo/tools/hgproxy/etc/object\_relationship\_list.json”

### (2) 重启服务生效

```
systemctl restart hgproxy
```
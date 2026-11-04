---
title: "20、HGDB 创建用户报错"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/user_error.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## HGDB 创建用户报错

## 1、问题描述

## 2、问题原因

bug：数据库开启 mysql 兼容后，存在日期格式问题。

触发条件：数据库版本 458 以下，开启mysql 兼容，用户有限期不为 0。

## 3、解决方案

1）更改数据库兼容模式或将用户有效期设置为 0。

```
alter system set compatible_db = oracle;
select pg_reload_conf();

psql -U syssso
select set_secure_param('hg_idcheck.pwdvaliduntil','0');
```

2）升级数据库版本至 458 以上。
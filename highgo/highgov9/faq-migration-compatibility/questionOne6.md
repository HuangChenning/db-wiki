---
title: "HGMIGV4.4.1工具迁移报错：Packet for query is too large"
book: "迁移兼容类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionOne6.html"
tags:
  - highgo
  - highgo-v9
  - faq-migration-compatibility
---

问题：

HGMIGV4.4.1 工具，迁移mysql到V9.0.5 MySQL模式报错。

> Packet for query is too large (4,462,199 > 4,194,304). You can change this value on the server by setting the ‘max\_allowed\_packet’ variable. 执行Insert写入行数据异常-1

解决：

V9.0.5数据库，登录5866端口修改数据库参数解决。

```
alter system set max_allowed_packet TO 1073741824  ; 
select pg_reload_conf(); 
show max_allowed_packet ;
```
---
title: "replace函数问题"
book: "迁移兼容类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/index.html"
tags:
  - highgo
  - highgo-v9
  - faq-migration-compatibility
---

##### 问题现象

在使用replace函数，将字符串中某个值替换成空时，整个字符串被替换成空

```bash
SELECT replace('Hello Word','Hello','');
```

![1_1](img/1_1.webp)

##### 解决方案

创建replace函数

```bash
create or replace function sys.replace(text, text, text default null::text) 
returns text language c immutable parallel safe 
as '$libdir/ivorysql_ora', $$ora_replace$$;
/
```

![1_2](img/1_2.webp)

![1_3](img/1_3.webp)
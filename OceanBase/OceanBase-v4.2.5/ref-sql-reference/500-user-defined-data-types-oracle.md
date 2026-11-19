---
title: "用户自定义子类型"
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503110.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# 用户自定义子类型

PL 允许用户基于基础数据类型创建自定义子类型 `SUBTYPE`，也可以基于自定义类型再次定义。 


  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

自定义子类型 `SUBTYPE` 的语法如下：

```javascript
SUBTYPE subtype_name IS base_type
{ precision [, scale ]  [ NOT NULL ]
```



对于自定义类型，可以重新定义精度，或者做非空约束。示例如下：

```javascript
obclient> DECLARE
  SUBTYPE score IS NUMBER;
  amount score(6,2); 

  SUBTYPE item IS score NOT NULL;
  item1 item := 1; 

BEGIN 
  amount := item1;
END;
/
```

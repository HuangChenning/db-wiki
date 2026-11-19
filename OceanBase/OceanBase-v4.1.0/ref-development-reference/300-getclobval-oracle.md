---
title: GETCLOBVAL
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702531.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# GETCLOBVAL

GETCLOBVAL 
===============================

`GETCLOBVAL` 成员函数返回一个包含序列化 XML 表示的 `CLOB`。如果返回的 `CLOB` 是临时的，则必须在使用后将其释放。


  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

语法 
-----------------------

```sql
MEMBER FUNCTION getClobVal()
RETURN clob;
```

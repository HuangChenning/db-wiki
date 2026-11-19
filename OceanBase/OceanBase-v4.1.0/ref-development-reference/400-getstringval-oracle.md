---
title: GETSTRINGVAL
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702532.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# GETSTRINGVAL

GETSTRINGVAL 
=================================

`GETSTRINGVAL` 成员函数以字符串形式返回文档。它返回一个包含序列化 XML 表示的字符串，或者如果是文本节点时返回文本本身。如果 XML 文档超过 `VARCHAR2` 最大大小 (4000)，则在运行时会引发错误。


  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

语法 
-----------------------

```sql
MEMBER FUNCTION getStringVal()
RETURN VARCHAR2；
```

---
title: OLD_CURRENT_USER
book: "PL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016569.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# OLD_CURRENT_USER

`OLD_CURRENT_USER` 此函数用于从 `sys_context` 返回会话值（'`userenv`', '`current_user`'）。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法 

```sql
DBMS_UTILITY.OLD_CURRENT_USER 
RETURN VARCHAR2;
```

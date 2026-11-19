---
title: ALTER SERVER
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503335.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ALTER SERVER

## 描述

该语句用于更改服务器信息。

## 语法

```sql
ALTER SERVER  server_name
    OPTIONS (option [, option] ...)

option: {
    HOST character-literal
  | DATABASE character-literal
  | USER character-literal
  | PASSWORD character-literal
  | SOCKET character-literal
  | OWNER character-literal
  | PORT numeric-literal
}
```

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>仅支持该关键字语法，功能暂不生效。</p>
</main>

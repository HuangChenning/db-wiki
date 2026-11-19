---
title: REPAIR TABLE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503351.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# REPAIR TABLE

该语句用于修复可能损坏的表。

## 语法

```sql
REPAIR [NO_WRITE_TO_BINLOG | LOCAL]
    TABLE tbl_name [, tbl_name] ...
    [QUICK] [EXTENDED] [USE_FRM]
```

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>当前版本仅支持该关键字语法，功能暂不生效。</p>
</main>

---
title: ALTER LOGFILE GROUP
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503294.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ALTER LOGFILE GROUP

## 描述

该语句用来修改日志文件组。

## 语法

```sql
ALTER LOGFILE GROUP logfile_group
    ADD UNDOFILE 'file_name'
    [INITIAL_SIZE [=] size]
    [WAIT]
    ENGINE [=] engine_name
```

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>仅支持该关键字语法，功能不生效。</p>
</main>

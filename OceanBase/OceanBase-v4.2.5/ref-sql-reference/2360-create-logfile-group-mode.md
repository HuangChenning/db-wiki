---
title: CREATE LOGFILE GROUP
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503284.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CREATE LOGFILE GROUP

## 描述

该语句用来创建日志文件组。

## 语法

```sql
CREATE LOGFILE GROUP logfile_group
    ADD UNDOFILE 'undo_file'
    [INITIAL_SIZE [=] initial_size]
    [UNDO_BUFFER_SIZE [=] undo_buffer_size]
    [REDO_BUFFER_SIZE [=] redo_buffer_size]
    [NODEGROUP [=] nodegroup_id]
    [WAIT]
    [COMMENT [=] 'string']
    ENGINE [=] engine_name
```

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>仅支持该关键字语法，功能不生效。</p>
</main>

---
title: DROPPYTHON
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479912.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DROPPYTHON

`DBMS_PYTHON.DROPPYTHON` 用于删除 Python 外部资源。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 OceanBase 数据库 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
DBMS_PYTHON.DROPPYTHON(IN py_name VARCHAR(65535));
```

`py_name` 是上传时 `loadpython` 的 `python_name`。

## 示例

执行如下命令删除上传的 Python 外部资源：

```shell
obclient> CALL DBMS_PYTHON.DROPPYTHON('my_add_python');
```

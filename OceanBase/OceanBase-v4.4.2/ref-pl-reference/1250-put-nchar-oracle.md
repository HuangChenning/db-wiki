---
title: PUT_NCHAR
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005719939.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# PUT_NCHAR

`PUT_NCHAR` 存储过程用于以 `NCHAR` 方式追加到当前行缓冲。

<main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版暂不支持。</p>
  </main>

## 语法

```sql
UTL_FILE.PUT_NCHAR(
    file    IN FILE_TYPE,
    buffer  IN VARCHAR2
);
```

## 参数解释

|    参数     |           解释            |
|-----------|-------------------------|
| file      | 由调用 `FOPEN` 返回的活动文件句柄。  |
| buffer    | 文本缓冲区，包含要写入文件的行。        |

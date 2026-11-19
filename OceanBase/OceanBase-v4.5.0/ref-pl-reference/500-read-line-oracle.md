---
title: READ_LINE
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480116.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# READ_LINE

`READ_LINE` 读取 HTTP 响应体的一行文本格式数据，遇到换行符时结束。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

# 语法

```sql
UTL_HTTP.READ_LINE(
   r            IN OUT NOCOPY resp,
   data         OUT NOCOPY  VARCHAR2 CHARACTER SET ANY_CS,
   remove_crlf  IN  BOOLEAN DEFAULT FALSE);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
|data|文本形式的 HTTP 响应主体|
|remove_crlf|是否除去 newline characters，默认为 `False`|

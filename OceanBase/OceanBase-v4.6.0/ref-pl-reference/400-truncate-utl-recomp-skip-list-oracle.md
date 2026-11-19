---
title: TRUNCATE_UTL_RECOMP_SKIP_LIST
book: "PL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005686588.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# TRUNCATE_UTL_RECOMP_SKIP_LIST

`TRUNCATE_UTL_RECOMP_SKIP_LIST` 用于清空 `UTL_RECOMP_SKIP_LIST` 表。

 <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版暂不支持。</p>
  </main>

## 语法

```sql
UTL_RECOMP.TRUNCATE_UTL_RECOMP_SKIP_LIST();
```

## 示例

```shell
EXECUTE UTL_RECOMP.TRUNCATE_UTL_RECOMP_SKIP_LIST();
Query OK, 1 row affected (23.463 sec)
```

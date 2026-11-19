---
title: GET_PREFS
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480205.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# GET_PREFS

`GET_PREFS` 函数用于获取指定首选项的默认值。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版暂不支持。</p>
  </main>

## 语法

```sql
DBMS_STATS.GET_PREFS (
   pname     IN   VARCHAR2,
   ownname   IN   VARCHAR2 DEFAULT NULL,
   tabname   IN   VARCHAR2 DEFAULT NULL)
 RETURN VARCHAR2;
```

## 参数说明

|   参数    |                说明              |
|---------|-----------------------------------|
| pname   | Prefs 的名字。                      |
| ownname | 用户名。如果用户名设置为 `NULL`，会默认使用当前登录用户名。 |
| tabname | 表名。                              |

## 异常情况

|    错误码    |          描述          |
|-----------|----------------------|
| OBE-20000 | 资源管理器未启用，无法同时收集统计信息。 |
| OBE-20001 | 无效的输入值。              |

## 示例

获取用户 `testUser01` 的 `tbl1` 表中 `GRANULARITY` 参数的默认值。

```sql
obclient> SELECT DBMS_STATS.GET_PREFS ('GRANULARITY','testUser01','tbl1') FROM DUAL;
+----------------------------------------------------------+
| DBMS_STATS.GET_PREFS ('GRANULARITY','testUser01','tbl1') |
+----------------------------------------------------------+
| AUTO                                                     |
+----------------------------------------------------------+
1 row in set
```

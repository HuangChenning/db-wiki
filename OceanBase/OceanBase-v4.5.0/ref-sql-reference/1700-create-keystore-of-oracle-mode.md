---
title: CREATE KEYSTORE
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480921.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CREATE KEYSTORE

## 描述

该语句用来创建 Keystore 对象，此对象用于存储密钥。在透明加密场景中，需要创建 Keystore 对象，每个租户最多只能创建一个 Keystore 对象。

## 语法

```sql
ADMINISTER KEY MANAGEMENT CREATE KEYSTORE [keystore_name] IDENTIFIED BY [password] ;
```

## 参数解释

|      参数       |          描述          |
|---------------|----------------------|
| keystore_name | 指定 Keystore 名称。      |
| password      | 指定访问控制 Keystore 的密码。 |

## 示例

创建一个 Keystore 对象 `keystore1`。

```sql
obclient> ADMINISTER KEY MANAGEMENT CREATE KEYSTORE keystore1 IDENTIFIED BY **1***;
```

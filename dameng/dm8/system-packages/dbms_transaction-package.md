---
title: "DBMS_TRANSACTION 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_transaction-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_TRANSACTION 包提供获得当前活动事务号的功能。

## 18.1 相关方法

返回当前活动事务号。

**语法如下：**

```
FUNCTION LOCAL_TRANSACTION_ID (
    CREATE_TRANSACTION BOOLEAN := FALSE
) RETURN VARCHAR2;
```

**参数详解**

- create\_transaction
	表示如果当前没有活动事务，是否创建一个新的事务。TRUE：创建；FALSE：不创建，返回空。缺省为 FALSE。

## 18.2 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_TRANSACTION');
```

例 查询当前活动事务号。

```
SELECT DBMS_TRANSACTION.LOCAL_TRANSACTION_ID(FALSE);
```

结果如下：

```
6755
```

需要注意的是，该查询语句本身也是活动事务，因此该语句必然返回一个活动事务号。
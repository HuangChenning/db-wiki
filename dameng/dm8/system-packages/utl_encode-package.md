---
title: "UTL_ENCODE 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/utl_encode-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

UTL\_ENCODE 包提供了对 varbinary 和 blob 类型数据进行编码和解码的功能。

## 23.1 相关方法

1. BASE64\_ENCODE

将 varbinary 或 blob 格式的数据 R 编码成 base64 字符集格式，再以 varbinary 类型返回。

**语法如下：**

```
FUNCTION UTL_ENCODE.BASE64_ENCODE (
    R     IN     VARBINARY
)RETURN VARBINARY;
或
FUNCTION UTL_ENCODE.BASE64_ENCODE (
    R     IN     BLOB
)RETURN VARBINARY;
```
2. BASE64\_DECODE

将 base64 字符集的编码 R，解码成原始的 varbinary 类型数据。

在遇到输入值中存在非 base64 编码的内容时，报错。

**语法如下：**

```
FUNCTION UTL_ENCODE.BASE64_DECODE (
    R     IN     VARBINARY
)RETURN VARBINARY;
```
3. BASE64\_DECODE2

将 base64 字符集的编码 R，解码成原始的 varbinary 类型数据。

在遇到输入值中存在非 base64 编码的内容时，返回 NULL，不报错。

**语法如下：**

```
FUNCTION UTL_ENCODE.BASE64_DECODE2 (
    R     IN     VARBINARY
)RETURN VARBINARY;
```

## 23.2 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'UTL_ENCODE');
```

例使用 BASE64\_ENCODE 和 BASE64\_deCODE 对数据进行编码和解码。

```
//数据准备：
drop TABLE T;
create table T (i VARBINARY (10));
insert into t VALUES ('420921197908051523');
//使用BASE64_ENCODE和BASE64_deCODE：
select utl_encode.base64_ENCODE (i) from t;
查询结果为：0x51676B6847586B494252556A
select utl_encode.base64_DECODE (utl_encode.base64_ENCODE (i)) FROM t;
查询结果为：0x420921197908051523
```
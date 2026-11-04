---
title: "DBMS_LDAP 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_ldap-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

LDAP 是一种轻量级的目录访问协议，DBMS\_LDAP 是 DM 数据库提供的一个 PL/SQL 系统包，用于在数据库内部与 LDAP 服务器之间交互，实现目录服务的查询、认证、修改和管理。

## 54.1 数据类型

DBMS\_LDAP 包中支持的数据类型语法如下：

```
SUBTYPE SESSION IS BINARY(32);
SUBTYPE MESSAGE IS BINARY(32); 
SUBTYPE MOD_ARRAY IS BINARY(32); 
SUBTYPE BERVAL IS BINARY(32000); 
TYPE STRING_COLLECTION IS TABLE OF VARCHAR2(32767) INDEX BY BINARY_INTEGER; 
TYPE BERVAL_COLLECTION IS TABLE OF VARBINARY(32767) INDEX BY BINARY_INTEGER;
TYPE BLOB_COLLECTION IS TABLE OF BLOB INDEX BY BINARY_INTEGER;
```

## 54.2 相关方法

1. INIT

建立与 LDAP 服务器的连接，并返回通信会话句柄。

**语法如下：**

```
FUNCTION INIT(
    HOSTNAME        IN  VARCHAR2,
    PORTNUM         IN  PLS_INTEGER
)RETURN SESSION;
```

**参数详解**

- HOSTNAME
	LDAP 服务器主机名。
- PORTNUM
	LDAP 服务器端口。

**返回值**

通信会话句柄。

2. CREATE\_MOD\_ARRAY

创建用于存放条目信息的数组。

**语法如下：**

```
FUNCTION CREATE_MOD_ARRAY(
    NUM             IN  PLS_INTEGER
) RETURN MOD_ARRAY;
```

**参数详解**

- NUM
	数组大小，不超过 8192。

**返回值**

存放条目信息的数组。

3. POPULATE\_MOD\_ARRAY

填充条目信息。

**语法如下：**

```
PROCEDURE POPULATE_MOD_ARRAY(
    MODPTR          IN  MOD_ARRAY,
    MOD_OP          IN  PLS_INTEGER,
    MOD_TYPE        IN  VARCHAR2,
    MODVAL          IN  STRING_COLLECTION
);

PROCEDURE POPULATE_MOD_ARRAY(
    MODPTR          IN  MOD_ARRAY,
    MOD_OP          IN  PLS_INTEGER,
    MOD_TYPE        IN  VARCHAR2,
    MODBVAL         IN  BERVAL_COLLECTION
);
  
PROCEDURE POPULATE_MOD_ARRAY(
    MODPTR          IN  MOD_ARRAY,
    MOD_OP          IN  PLS_INTEGER,
    MOD_TYPE        IN  VARCHAR2,
    MODBVAL         IN  BLOB_COLLECTION
);
```

**参数详解**

- MODPTR
	条目数组。
- MOD\_OP
	条目操作，可指定为 MOD\_ADD、MOD\_DELETE、MOD\_REPLACE。
- MOD\_TYPE
	条目类型
- MODBVAL
	条目数据。
4. ADD\_S

向服务器添加条目。

**语法如下：**

```
FUNCTION ADD_S(
    LD              IN  SESSION,
    ENTRYDN         IN  VARCHAR2,
    MODPTR          IN  MOD_ARRAY
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- ENTRYDN
	条目路径
- MODPTR
	条目数组。
5. FREE\_MOD\_ARRAY

释放条目数组。

**语法如下：**

```
PROCEDURE FREE_MOD_ARRAY(
    MODPTR          IN  MOD_ARRAY
);
```

**参数详解**

- MODPTR
	条目数组。
6. MODIFY\_S

修改条目信息。

**语法如下：**

```
FUNCTION MODIFY_S(
    LD              IN  SESSION,
    ENTRYDN         IN  VARCHAR2,
    MODPTR          IN  MOD_ARRAY
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- ENTRYDN
	条目路径。
- MODPTR
	条目数组
7. SIMPLE\_BIND\_S

登录 LDAP 服务器。

**语法如下：**

```
FUNCTION SIMPLE_BIND_S(
    LD              IN  SESSION,
    DN              IN  VARCHAR2,
    PASSWD          IN  VARCHAR2
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- DN
	条目路径。
- PASSWD
	登录密码。
8. UNBIND\_S

断开与 LDAP 服务器的连接。

**语法如下：**

```
FUNCTION UNBIND_S(
    LD              IN OUT  SESSION 
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
9. SEARCH\_S

查找条目。

**语法如下：**

```
FUNCTION SEARCH_S(
    LD              IN  SESSION,
    BASE            IN  VARCHAR2,
    SCOPE           IN  PLS_INTEGER,
    FILTER          IN  VARCHAR2,
    ATTRS           IN  STRING_COLLECTION,
    ATTRONLY        IN  PLS_INTEGER,
    RES             OUT MESSAGE
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- BASE
	基准路径。
- SCOPE
	搜索范围。
- FILTER
	过滤条件。
- ATTRS
	需要返回的属性数组。
- ATTRSONLY
	属性返回模式。
- RES
	输出的结果集。
10. COUNT\_ENTRIES

计算条目数量。

**语法如下：**

```
FUNCTION COUNT_ENTRIES (
    LD              IN  SESSION,
    MSG             IN  MESSAGE 
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- MSG
	结果集句柄。
11. FIRST\_ENTRY

获取第一个条目。

**语法如下：**

```
FUNCTION FIRST_ENTRY(
    LD              IN  SESSION,
    MSG             IN  MESSAGE 
) RETURN MESSAGE;
```

**参数详解**

- LD
	SESSION 类型句柄。
- MSG
	结果集句柄。

**返回值**

返回第一个条目。

12. NEXT\_ENTRY

获取下一条条目。

**语法如下：**

```
FUNCTION NEXT_ENTRY (
    LD              IN  SESSION,
    MSG             IN  MESSAGE 
) RETURN MESSAGE;
```

**参数详解**

- LD
	SESSION 类型句柄。
- MSG
	结果集句柄。

**返回值**

返回下一个条目。

13. GET\_DN

获取条目路径。

**语法如下：**

```
FUNCTION GET_DN(
    LD              IN  SESSION,
    LDAPENTRY       IN  MESSAGE
) RETURN VARCHAR2;
```

**参数详解**

- LD
	SESSION 类型句柄。
- LDAPENTRY
	条目句柄。

**返回值**

返回条目对应的路径。

14. GET\_VALUES

从 LDAP 条目中获取指定属性的字符串类型值。

**语法如下：**

```
FUNCTION GET_VALUES(
    LD              IN  SESSION,
    LDAPENTRY       IN  MESSAGE,
    ATTR            IN  VARCHAR2
) RETURN STRING_COLLECTION;
```

**参数详解**

- LD
	SESSION 类型句柄。
- LDAPENTRY
	条目句柄。
- ATTR
	属性名。

**返回值**

获取的指定属性的字符串类型值。

15. RENAME\_S

重命名条目。

**语法如下：**

```
FUNCTION RENAME_S(
    LD              IN  SESSION,
    DN              IN  VARCHAR2,
    NEWRDN          IN  VARCHAR2,
    NEWPARENT       IN  VARCHAR2,
    DELETEOLDRDN    IN  PLS_INTEGER,
    SERVERCTRLS     IN  LDAPCONTROL DEFAULT NULL,
    CLIENTCTRLS     IN  LDAPCONTROL DEFAULT NULL
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- DN
	条目路径。
- NEWRDN
	新的条目相对路径。
- NEWPARENT
	父路径。
- DELETEOLDRDN
	是否删除原先的条目相对路径。
- SERVERCTRLS
	仅兼容支持，无实际意义。
- CLIENTCTRLS
	仅兼容支持，无实际意义。
16. DELETE\_S

同步方式删除条目。

**语法如下：**

```
FUNCTION DELETE_S(
    LD              IN  SESSION,
    ENTRYDN         IN  VARCHAR2
) RETURN PLS_INTEGER;
```

**参数详解**

- LD
	SESSION 类型句柄。
- ENTRYDN
	条目路径。
17. MSGFREE

释放结果集。

**语法如下：**

```
FUNCTION MSGFREE(
    LM              IN  MESSAGE
) RETURN PLS_INTEGER;
```

**参数详解**

- LM
	结果集句柄。
18. ERR2STRING

根据返回的 LDAP 错误码获取错误描述。

**语法如下：**

```
FUNCTION ERR2STRING(
    LDAP_ERR        IN  PLS_INTEGER
) RETURN VARCHAR2;
```

**参数详解**

- LDAP\_ERR
	错误码。

**返回值**

错误码对应的错误描述。

## 54.3 举例说明

使用包内的过程和函数之前，如果还未创建过系统包。请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_LDAP');
```

向 LDAP 添加条目：

```
declare
  l_retval   PLS_INTEGER;
  l_add_vals   DBMS_LDAP.STRING_COLLECTION;
  l_array    DBMS_LDAP.MOD_ARRAY;
  l_session     DBMS_LDAP.SESSION;
begin
    l_session := dbms_ldap.init('192.168.0.1', 389);
    l_retval := dbms_ldap.simple_bind_s(l_session, 'cn=admin,dc=dm_ldap,dc=com','mypwd');
    --增加数据
    l_array := dbms_ldap.create_mod_array(10);
    l_add_vals(1) := 'test_user1';
    dbms_ldap.populate_mod_array(l_array,
                               dbms_ldap.MOD_ADD,
                               'cn',
                               l_add_vals);
   l_add_vals(1) := 'Doe1';
  dbms_ldap.populate_mod_array(l_array,
                               dbms_ldap.MOD_ADD,
                               'sn',
                               l_add_vals);
  l_add_vals(1) := 'top';
  l_add_vals(2) := 'person';
  dbms_ldap.populate_mod_array(l_array,
                               dbms_ldap.MOD_ADD,
                               'objectClass',
                               l_add_vals);
l_retval := dbms_ldap.add_s(l_session, 'cn=test_user1, dc=dm_ldap, dc=com', l_array);
    dbms_ldap.free_mod_array(l_array);
    l_retval := dbms_ldap.unbind_s(l_session);
end;
/
```
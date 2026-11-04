---
title: "DBMS_METADATA 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_metadata-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_METADATA 包提供一种方法，可以将元数据以 XML 格式或 creation DDL 语句格式进行检索，也可以提交 XML 以重新创建对象。通过此方法，用户可以更方便地管理和查询数据库中的元数据。

需要注意的是，DBMS\_METADATA 包中的方法获取系统内建聚集索引时，当 INI 参数 INNER\_INDEX\_DDL\_SHOW=1，结果显示为“INNER CLUSTER INDEX”，当 INI 参数 INNER\_INDEX\_DDL\_SHOW=0，则报错。

## 9.1 数据类型

DBMS\_METADATA 包中涉及到类型。如下统一说明。

1. KU$\_PARSED\_ITEM 记录类型
```
TYPE KU$_PARSED_ITEM IS RECORD (
    ITEM            VARCHAR(30),
    VALUE            VARCHAR(4000),
    OBJECT_ROW        SMALLINT
);
```

**参数详解**

- ITEM
	被解析对象属性的名称。
- VALUE
	对象属性值，如果没有就是 NULL。
- OBJECT\_ROW
	对象所在的行数。

KU$\_PARSED\_ITEMS 为 KU$\_PARSED\_ITEM 类型的索引表：

```
TYPE KU$_PARSED_ITEMS IS TABLE OF KU$_PARSED_ITEM INDEX BY INT;
```
2. KU$\_DDL 记录类型
```
TYPE KU$_DDL IS RECORD(
    DDLTEXT            CLOB,
    PARSEDITEM        KU$_PARSED_ITEMS 
);
```

**参数详解**

- DDLTEXT
	DDL 语句。
- PARSEDITEM
	对象属性。

KU$\_DDLS 为 KU$\_DDL 类型的索引表：

```
TYPE KU$_DDLS IS TABLE OF KU$_DDL INDEX BY INT;
```
3. KU$\_MULTI\_DDL 记录类型
```
TYPE KU$_MULTI_DDL IS RECORD(
    OBJECT_ROW        NUMBER,
    DDLS            KU$_DDLS
);
```

**参数详解**

- OBJECT\_ROW
	对象所在的行数。
- DDLS
	KU$\_DDLS 类型。

KU$\_MULTI\_DDLS 为 KU$\_MULTI\_DDL 类型的索引表：

```
TYPE KU$_MULTI_DDLS IS TABLE OF KU$_MULTI_DDL INDEX BY INT;
```

## 9.2 相关方法

1. GET\_DDL

获取指定对象元数据中的 DDL 语句。

权限使用说明：

用户只能看到自己被授权的对象定义。拥有 DBA/DB\_OBJECT\_ADMIN 权限可看到其他用户的对象定义。

用户可查询自己模式下的对象定义。拥有 DBA/DB\_OBJECT\_ADMIN 权限才能查看 sys 模式下的对象定义。

三权分立下，拥有 DBA 权限的用户可以查询其他用户的对象定义，但 SYSDBA 和普通用户无权限查询 SYSSSO、SYSAUDITOR 的对象定义。

四权分立下，拥有 DB\_OBJECT\_ADMIN 权限的用户可以查询其他用户的对象定义。但 SYSDBA 和普通用户无权限查询 SYSSSO、SYSAUDITOR 的对象定义，SYSDBO 可以查询 SYSDBA 的对象定义。

拥有 dba/DB\_OBJECT\_ADMIN 权限可查看表空间、USER、ROLE、PROFILE、DIR 定义。

**语法如下：**

```
FUNCTION GET_DDL(
    OBJECT_TYPE        IN        VARCHAR(30),
    NAME            IN        VARCHAR(128), 
    SCHNAME            IN        VARCHAR(128)    DEFAULT NULL
) RETURN CLOB
```

**参数详解**

- object\_type
	对象类型。包括表、视图、物化视图、索引、全文索引、存储过程、函数、包、目录等，详情请见 open 参数详解。其中，object\_type 只能为大写。
- name
	对象名称，区分大小写。
- schname
	模式，默认是当前用户模式。

**返回值**

以 ddl 返回对象元数据中的 DDL 语句。

**错误处理**

INVALID\_ARGVAL：如果输入参数中存在空值或非法值。

OBJ\_NOT\_FOUND：如果指定的对象在数据库中不存在。

2. OPEN

打开对象类型的句柄

**语法如下：**

```
FUNCTION OPEN (
    OBJECT_TYPE        IN        VARCHAR
) RETURN INT;
```

**参数详解**

- object\_type

可返回的对象类型名称，合法的类型名称见下表 9.1。

表9.1 OPEN函数可返回的对象类型名称

| **类型名称** | **含义** | **属性** | **说明** |
| --- | --- | --- | --- |
| CLASS | 类类型 | SN | 默认返回类头类体 |
| JCLASS | java class 类型 | SN | 无 |
| CLASS\_HEAD | 类型名 | SN | 无 |
| CLASS\_BODY | 类型体 | SN | 无 |
| COL\_STATISTICS | 列统计 | D | 无 |
| COMMENT | 注释 | D | 无 |
| CONSTRAINT | 约束 | SND | 不包括聚集主键和非空约束 |
| CONTEXT | 上下文 | N | 无 |
| CONTEXT\_INDEX | 全文索引 | N | 无 |
| DATABASE\_EXPORT | 数据库下的所有对象 | H | 库级导出 |
| DB\_LINK | 数据库链接 | SN | 因此类对象具有所有者,因此将其视为模式级对象。   对于公有连接，它们的所有者是 PUBLIC；对于私有链接，它们的创建者就是它们的所有者 |
| DIRECTORY | 目录 | N | 无 |
| DOMAIN | 域 | N | 无 |
| FUNCTION | 存储函数 | SN | 无 |
| INDEX | 索引 | SND | 不包括系统内部定义的索引 |
| INDEX\_STATISTICS | 索引统计 | D | 无 |
| JOB | 任务 | N | 无 |
| OBJECT\_GRANT | 对象权限 | DG | 无 |
| PACKAGE | 包 | SN | 默认返回包头包体 |
| PKG\_SPEC | 包头 | SN | 无 |
| PKG\_BODY | 包体 | SN | 无 |
| POLICY | 策略 | D | 无 |
| PROCEDURE | 存储过程 | SN | 无 |
| ROLE | 角色 | N | 无 |
| ROLE\_GRANT | 角色权限 | G | 无 |
| SCHEMA\_EXPORT | 模式下的所有对象 | H | 模式级导出 |
| SEQUENCE | 序列 | SN | 无 |
| SYNONYM | 同义词 | 见说明 | 私有同义词为模式对象，公有同义词为命名对象 |
| SYSTEM\_GRANT | 系统权限 | G | 无 |
| TABLE | 表 | SN | 无 |
| TABLE\_STATISTICS | 表统计信息 | D | 无 |
| TABLE\_EXPORT | 表及与其相关的元数据 | H | 表级导出 |
| TABLESPACE | 表空间 | N | 无 |
| TRIGGER | 触发器 | SND | 无 |
| USER | 用户 | N | 无 |
| VIEW | 视图 | SN | 无 |
| TYPE | 用户自定义类型 | SN | 无 |
| MATERIALIZED\_VIEW | 物化视图 | SN | 无 |
| MATERIALIZED\_VIEW\_LOG | 物化视图日志 | SN | 无 |
| PROFILE | PROFILE 对象 | N | 无 |

> **注意**
> 
> 属性列中，S表示模式对象，N表示命名的对象，D表示依赖对象，G表示被授权的对象，H表示包含不同类型的对象。

**返回值**

不透明的句柄。该句柄将用于 SET\_FILTER, SET\_PARSE\_ITEM, FETCH\_XXX, CLOSE。

**错误处理**

INVALID\_ARGVAL：如果输入参数中存在空值或非法值。

3. FETCH\_DDL

该函数返回符合 OPEN，SET\_FILTER，SET\_PARSE\_ITEM 设定条件的对象元数据。

**语法如下：**

```
FUNCTION FETCH_DDL (
    HANDLE        IN        INT
)RETURN KU$_DDLS;
```

**参数详解**

- handle
	OPEN 函数返回的句柄。

**返回值**

对象的元数据或者当所有对象都已返回后返回 NULL。

**使用说明：**

从表 ku$\_ddls 中返回 ddl 语句，表 ku$\_ddls 的每一行在 ddlText 列包含一条 ddl 语句；如果使用解析的话，解析出的对象属性将从 parsedItem 列返回。

**错误处理**

INVALID\_ARGVAL：参数为 NULL，或者参数值非法。

4. FETCH\_CLOB

该函数返回符合 OPEN，SET\_FILTER 设定条件的对象元数据。

**语法如下：**

```
FUNCTION  FETCH_CLOB(
    HANDLE        IN        INT
)RETURN CLOB;
```

**参数详解**

- handle
	OPEN 函数返回的句柄。

**返回值**

对象的元数据或者当所有对象都已返回后返回 NULL。

**使用说明：**

将对象以 clob 返回。

**异常：**

INVALID\_ARGVAL：参数为 NULL，或者参数值非法。

5. GET\_GRANTED\_DDL

该函数用于返回对象的授权语句。权限使用说明和 GET\_DDL 一样，请参考 GET\_DDL。

**语法如下：**

```
FUNCTION GET_GRANTED_DDL (
    OBJECT_TYPE        IN        VARCHAR(30),
    GRANTEE            IN        VARCHAR(128) DEFAULT NULL,
    OBJECT_COUNT    IN        INT    DEFAULT  10000
)RETURN CLOB;
```

**参数详解**

- object\_type
	对象类型。参数要与 OPEN 的对象类型参数相同, 不能为 heterogeneous 对象类型。
- grantee
	被赋予权限的对象。
- object\_count
	返回对象个数的最大值。

**返回值**

以 ddl 返回对象的元数据

**异常:**

INVALID\_ARGVAL：参数值为 null，或者参数值非法。

OBJ\_NOT\_FOUND：指定的对象数据库中不存在。

6. GET\_DEPENDENT\_DDL

该函数用于返回依赖对象的 DDL 语句。权限使用说明和 GET\_DDL 一样，请参考 GET\_DDL。

**语法如下：**

```
FUNCTION GET_DEPENDENT_DDL (
    OBJECT_TYPE                IN        VARCHAR(30),
    BASE_OBJECT_NAME        IN        VARCHAR(128),
    BASE_OBJECT_SCHEMA        IN        VARCHAR(128)    DEFAULT NULL,
    OBJECT_COUNT            IN        INT        DEFAULT 10000
)RETURN CLOB;
```

**参数详解**

- object\_type
	对象类型。参数要与 OPEN 的对象类型参数相同, 不能为 heterogeneous 对象类型。
- base\_object\_name
	基对象名称。内部使用 BASE\_OBJECT\_NAME 过滤器过滤。
- base\_object\_schema
	基对象模式。内部使用 BASE\_OBJECT\_SCHEMA 过滤器过滤。
- object\_count
	返回对象个数的最大值。

**返回值**

以 ddl 返回对象的元数据。

**异常:**

INVALID\_ARGVAL：参数值为 null，或者参数值非法。

OBJ\_NOT\_FOUND：指定的对象数据库中不存在。

7. ADD\_TRANSFORM

该过程用在 fetch\_clob 前，表示 feTCH\_CLOB 的内容以 DDL 形式展示，即返回对象的 ddl 格式的语句。不调用则默认情况下返回 XML 格式化定义（当 XML 脚本元数据中包含非格式化拼入的特殊字符时，会进行相应的实体引用转换，如表“T<>”转义为“t<>”。会转换的特殊字符有五种：大于号“>”转换为“>”；小于号“<”转换为“<”；“&”转换为“&”；双引号转换为“"”；单引号转换为“'”）。

因为要支持这个函数，metadata 包中元数据改造成了 xml 格式。ku$\_ddl.DDLTEXT 为元数据。

**语法如下：**

```
FUNCTION ADD_TRANSFORM (
                HANDLE          IN NUMBER,
                NAME            IN VARCHAR2,
                ENCODING        IN VARCHAR2 DEFAULT NULL,
                OBJECT_TYPE     IN VARCHAR2 DEFAULT NULL)
RETURN NUMBER;
```

**参数详解**

- handle
	OPEN 函数返回的句柄。
- NAME
	参数值有 DDL 和 MODIFY。表示转换类型，目前只支持 DDL，其他字符则不起作用。
- ENCODING
	编码。忽略，暂不支持设置。
- OBJECT\_TYPE
	应用本格式化定义的对象类型。由于 transform\_handle 只支持会话级，因此该参数暂无实际作用。

**返回值**

TRANSFORM\_HANDLE 的会话句柄，表示定义的格式化应用于当前会话。目前暂定从 10000 开始计数，无实际作用。因为此函数可直接设置全局的转换类型。但该句柄可传递给 SET\_TRANSFORM\_PARAM。当 NAME 为 MODIFY 时，句柄返回值可以用于函数 SET\_REMAP\_PARAM，但暂不支持。

**错误处理**

无

8. GET\_QUERY

该函数用于获取查询文本。

**语法如下：**

```
FUNCTION GET_QUERY (
    HANDLE        IN        INT
)RETURN VARCHAR;
```

**参数详解**

- handle
	OPEN 函数返回的句柄。

**返回值**

将被用于 FETCH\_XXX 函数的查询文本。

**错误处理**

INVALID\_ARGVAL：参数值为 null，或非法。

9. CHECK\_HANDLE

打印句柄使用情况。打印结果中 USE 为 1 的句柄表示当前该句柄正在使用。

**语法如下：**

```
PROCEDURE CHECK_HANDLE ();
```

**参数详解**

无。

10. CLOSE

关闭 OPEN 打开的句柄，并清理相关环境。

**语法如下：**

```
PROCEDURE CLOSE (
    HANDLE        IN        INT
);
```

**参数详解**

- handle
	OPEN 函数返回的句柄。

**错误处理**

INVALID\_ARGVAL：参数为 NULL，或者参数值非法。

11. CLOSE\_ALL

关闭全部句柄。

**语法如下：**

```
PROCEDURE CLOSE_ALL ();
```

**参数详解**

无。

12. SET\_FILTER

该过程用于过滤待返回的对象。

**语法如下：**

```
PROCEDURE SET_FILTER (
    HANDLE        IN        INT,
    NAME        IN        VARCHAR,
    VAL            IN        VARCHAR,
    OBJECT_TYPE_PATH    IN     VARCHAR DEFAULT NULL
);
```

**参数详解**

- handle
	句柄，由 DBMS\_METADATA.OPEN 输出。
- name
	过滤器的名称，详见下表。
- value
	过滤器的值，与 name 相对应，详见下表 9.2。
- OBJECT\_TYPE\_PATH
	忽略，暂不支持设置。

表9.2 SET\_FILTER过程中的过滤器名称

| **对象类型** | **名称** | **数据类型** | **含义** |
| --- | --- | --- | --- |
| 可命名对象 | NAME | 文本 | 通过对象名过滤 |
| 可命名对象 | NAME\_EXPR | 文本表达式 | 通过对象名的 where 表达式过滤，满足条件的返回 |
| 可命名对象 | EXCLUDE\_NAME\_EXPR | 文本表达式 | 通过对象名的 where 表达式过滤，不满足条件的返回 |
| 模式对象 | SCHEMA | 文本 | 通过模式名过滤，如果是公有同义词则指定其模式为 PUBLIC |
| 模式对象 | SCHEMA\_EXPR | 文本表达式 | 通过对象名的 where 表达式过滤，默认为当前模式 |
| 表、索引、表级导出 | TS | 文本 | 通过表空间名过滤 |
| 表、索引、表级导出 | TS\_EXPR | 文本表达式 | 通过表空间名的 where 表达式过滤 |
| 依赖对象 | BASE\_OBJECT\_NAME | 文本 | 通过基对象名过滤。 |
| 依赖对象 | BASE\_OBJECT\_SCHEMA | 文本 | 通过基对象模式过滤。如果使用 BASE\_OBJECT\_NAME 过滤，默认是当前模式。 |
| 依赖对象 | BASE\_OBJECT\_NAME\_EXPR | 文本表达式 | 通过基对象名的 where 表达式过滤，满足条件的返回。不适用于模式和库级触发器。 |
| 依赖对象 | EXCLUDE\_BASE\_OBJECT\_NAME\_EXPR | 文本表达式 | 通过基对象名的 where 表达式过滤，不满足条件的返回。不适用于模式和库级触发器。 |
| 依赖对象 | BASE\_OBJECT\_SCHEMA\_EXPR | 文本表达式 | 通过基对象模式的 where 表达式过滤。 |
| 依赖对象 | BASE\_OBJECT\_TYPE | 文本 | 通过基对象的对象类型过滤。 |
| 依赖对象 | BASE\_OBJECT\_TYPE\_EXPR | 文本表达式 | 通过基对象的对象类型表达式过滤。 |
| 依赖对象 | BASE\_OBJECT\_TS | 文本 | 通过基对象的表空间过滤。 |
| 依赖对象 | BASE\_OBJECT\_TS\_EXPR | 文本表达式 | 通过基对象的表空间 where 表达式过滤。 |
| 被授权对象 | GRANTEE | 文本 | 被授权的用户或角色。 AUDIT\_obj 只能过滤跟 grantee 有关的其他 grant 过滤器不适用。 |
| 被授权对象 | ROLE\_NAME | 文本 | 通过权限或角色的名称过滤 |
| 被授权对象 | ROLE\_NAME\_EXPR | 文本表达式 | 通过权限或角色的 where 表达式名称过滤 |
| 被授权对象 | GRANTEE\_EXPR | 文本表达式 | 通过被授权者名称的 where 表达式过滤，符合条件的返回 |
| 被授权对象 | EXCLUDE\_GRANTEE\_EXPR | 文本表达式 | 通过被授权者名称的 where 表达式过滤，不符合条件的返回 |
| 对象权限(OBJECT\_GRANT ) | GRANTOR | 文本 | 通过授权者过滤，对于系统用户（sysdba sysauditor syssso）赋予的权限在权限表里面 ID 记录的都是-1，所以设定了一个 grantor 叫"$SUPER",当 filter 中设定 grantor 为$SUPER 时，系统用户赋予的权限将全部返回而不区分具体是哪个系统用户 |
| 所有对象 | CUSTOM\_FILTER | 文本 | 用户自定义过滤，要求填写完整的 where 子句，如“NAME = ‘T1’” |
| 模式级导出 | SCHEMA | 文本 | 通过模式名过滤 |
| 模式级导出 | SCHEMA\_EXPR | 文本表达式 | 通过模式名 where 表达式过滤，有以下两种情况：1.获取模式对象； 2.获取依赖于此模式的对象。默认情况下，将选中当前用户的对象。 |
| 表级导出 | SCHEMA | 文本 | 通过模式名过滤 |
| 表级导出 | SCHEMA\_EXPR | 文本表达式 | 通过模式名 where 表达式过滤，有以下两种情况：1.获取模式下的表；2.获取依赖于表的对象。默认情况下，将选中当前用户的对象。 |
| 表级导出 | NAME | 文本 | 通过表名过滤出表及依赖表的对象 |
| 表级导出 | NAME\_EXPR | 文本表达式 | 通过表名的 where 表达式过滤出表及依赖表的对象 |

> **注意**
> 
> 约束的BASE\_OBJECT\_TYPE 是UTAB，注释的BASE\_OBJECT\_TYPE为TABLE或者VIEW。索引、OBJECT\_GRANT的BASE\_OBJECT\_TYPE为UTAB，TABLE\_STATISTICS，INDEX\_STATISTICS，COL\_STATISTICS的BASE\_OBJECT\_TYPE分别对应为T、I、C。

**错误处理**

INVALID\_ARGVAL：参数为 NULL，或者参数值非法。

INVALID\_CALL\_ORDER：无效的过程/函数调用顺序。在调用 FETCH\_xxx 之后，不允许再调用 SET\_FILTER 。

OBJ\_N\_FLT\_NOT\_MATCH：参数不一致，包括如下状况：

- 过滤器名字与 DBMS\_METADATA.OPEN 中指定的类型不匹配。
- 输入的过滤器的 value 与期待的数据类型不匹配。
13. SET\_PARSE\_ITEM

该过程用于解析对象的属性。

**语法如下：**

```
PROCEDURE SET_PARSE_ITEM (
    HANDLE            IN        INT,
    NAME            IN        VARCHAR,
    OBJECT_TYPE        IN        VARCHAR        DEFAULT NULL
);
```

**参数详解**

- handle
	OPEN 函数返回的句柄。
- name
	被解析对象属性的名称，具体的可被解析的对象属性名称见下表 9.3。
- object\_type
	应用于不同对象的集合，不设置时解析所有的对象。

表9.3 SET\_PARSE\_ITEM可解析的对象属性

| **对象类型** | **属性名称** | **含义** |
| --- | --- | --- |
| 所有对象 | VERB | 如果调用 FETCH\_DDL，表 ku$\_ddls 每一行 ddltext 列中的动词将被返回. 如果 ddlText 是 SQL DDL 语句, SQL 中的动词 (如 CREATE, GRANT, AUDIT) 被返回。如果 ddlText 是过程(如 DBMS\_METADATA.FETCH\_DDL()) 那么 package.procedure-name 被返回 |
| 所有对象 | OBJECT\_TYPE | 如果调用 FETCH\_DDL， ddlText 是 SQL DDL 语句且包含动词 CREATE 或者 ALTER，DDL 语句中的对象类型将被返回 (如 TABLE，PKG\_BODY 等等)。否则“表 OPEN 函数可返回的对象类型名称”中的对象类型被返回 |
| 模式对象 | SCHEMA | 返回对象的模式，如果不是模式对象则没有返回值 |
| 命名的对象 | NAME | 返回对象的名称，如果不是命名的对象则没有返回值 |
| 表、表数据、索引 | TABLESPACE | 返回对象表空间名称，如果是分区表则返回默认的表空间。对于 TABLE\_DATA 对象, 总是返回行所在的表空间 |
| 触发器 | ENABLE | 返回触发器是禁用还是启用状态 |
| 依赖对象 | BASE\_OBJECT\_NAME | 返回基对象名称，如果不是依赖对象则没有返回值 |
| 依赖对象 | BASE\_OBJECT\_SCHEMA | 返回基对象所属的模式，如果不是依赖对象则没有返回值 |
| 依赖对象 | BASE\_OBJECT\_TYPE | 返回基对象所属类型，如果不是依赖对象则没有返回值 |

> **注意**
> 
> 对象类型是可解析的对象属性所适用的范围；BASE\_OBJECT\_NAME，BASE\_OBJECT\_SCHEMA，BASE\_OBJECT\_TYPE这三个属性只解析约束、索引、全文索引、表级/视图级触发器。

**使用说明：**

FETCH\_XXX 函数可以返回对象的 ddl 语句，使用 SET\_PARSE\_ITEM 则可以返回对象的各个属性，可以多次调用 SET\_PARSE\_ITEM 来解析和返回多个解析项，返回的解析项存于表 ku$\_parsed\_items 中。

**错误处理**

INVALID\_ARGVAL：参数为 NULL,或者参数值非法。

INVALID\_CALL\_ORDER：无效的过程/函数调用顺序。SET\_PARSE\_ITEM 只能用于 FETCH\_xxx 函数之前。第一次调用 FETCH\_xxx 后，不允许再调用 SET\_PARSE\_ITEM。

14. SET\_COUNT

该过程用于指定一次 fetch\_xxx 函数调用所返回对象个数的最大值。

**语法如下：**

```
PROCEDURE SET_COUNT (
    HANDLE        IN        INT,
    VALUE        IN        INT
);
```

**参数详解**

- handle
	OPEN 函数返回的句柄。
- value
	设定的最大值。

**错误处理**

INVALID\_ARGVAL：参数值为 null 或非法；

INVALID\_CALL\_ORDER：无效的过程/函数调用顺序。SET\_COUNT 只能用于第一次调用 FETCH\_xxx 函数之前，第一次调用 FETCH\_xxx 后，不允许再调用 SET\_COUNT。

15. SET\_TRANSFORM\_PARAM

该过程用于格式化过滤会话级约束或存储选项的定义。

**语法如下：**

```
PROCEDURE SET_TRANSFORM_PARAM (
    TRANSFORM_HANDLE    IN        INT,
    NAME                IN        VARCHAR,
    VALUE                IN        BOOLEAN        DEFAULT TRUE,
    OBJECT_TYPE            IN        VARCHAR        DEFAULT NULL
);
```

**参数详解**

- transform\_handle
	会话句柄，目前仅支持 DBMS\_METADATA.SESSION\_TRANSFORM，表示定义的格式化应用于当前会话。
- name
	表示待过滤的约束或存储选项的名称，可取值 CONSTRAINTS 或 STORAGE：CONSTRAINTS 表示约束；STORAGE 表示存储选项。与参数 VALUE 配合使用。
- value
	表示是否过滤约束或存储选项的定义，可取值 TRUE 或 FALSE：TRUE 表示过滤；FALSE 表示不过滤。缺省为 TRUE。
- object\_type
	应用本格式化定义的对象类型，由于 transform\_handle 只支持会话级，因此该参数暂无实际作用。

**错误处理**

INVALID\_ARGVAL：参数值为 null 或非法。

## 9.3 错误处理

错误、异常情况释义：

ER\_EXCEED\_OPEN\_NUM：同时 OPEN 失败数目超过限制 10 次。  
INVALID\_OBJ\_TYPE：无效的对象类型。  
INVALID\_FLT\_TYPE：无效的过滤器名称。  
OBJ\_N\_FLT\_NOT\_MATCH：对象类型与过滤器不匹配。  
INVALID\_EXPR\_VAL：无效的表达式值。  
INVALID\_ATTRI\_NAME：不可解析的对象属性。  
INVALID\_ARGVAL：非法的参数数据。  
INVALID\_CALL\_ORDER：无效的过程/函数调用顺序。  
OBJ\_NOT\_FOUND：未找到对象或不允许查询系统定义的内部索引。

## 9.4 举例说明

使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_METADATA');
```

例 1 获取表和存储过程的 DDL 语句。

```
//建表
CREATE TABLE "SYSDBA"."T1"
(
"C1" CHAR(10) NOT NULL,
"C2" CHAR(10),
CONSTRAINT "PK" PRIMARY KEY("C1")) STORAGE(ON "MAIN", CLUSTERBTR);
//获取对象的ddl语句
SELECT DBMS_METADATA.GET_DDL('TABLE','T1','SYSDBA');
```

执行结果如下：

```
CREATE TABLE "SYSDBA"."T1"
(
"C1" CHAR(10) NOT NULL,
"C2" CHAR(10),
CONSTRAINT "PK" NOT CLUSTER PRIMARY KEY("C1")) STORAGE(ON "MAIN", CLUSTERBTR) ;
```

例 2 使用 DBMS\_METADATA 程序化接口获取元数据。

```
//建表
CREATE TABLE "RESOURCES"."TIMECARDS"
(  "EMPLOYEE_ID" INT,
   "WEEK" NUMBER(2,0),
   "JOB_ID" VARCHAR2(10),
   "HOURS_WORKED" NUMBER(4,2),  
   FOREIGN KEY ("EMPLOYEE_ID")
   REFERENCES "RESOURCES"."EMPLOYEE" ("EMPLOYEEID")
) STORAGE(ON "MAIN", CLUSTERBTR) ;
//建函数
CREATE OR REPLACE FUNCTION get_table_md RETURN CLOB IS
//定义局部变量
h NUMBER; //handle returned by OPEN
th NUMBER; //handle returned by ADD_TRANSFORM
doc CLOB;
BEGIN
//指定对象类型
h := DBMS_METADATA."OPEN" ('TABLE');

//使用过滤器返回特定的对象
DBMS_METADATA.SET_FILTER(h,'SCHEMA','RESOURCES');
DBMS_METADATA.SET_FILTER(h,'NAME','TIMECARDS');

//获取DDL格式的语句
DBMS_METADATA.ADD_TRANSFORM(H,'DDL');

//获取对象
doc := DBMS_METADATA.FETCH_CLOB(h);

//释放资源
DBMS_METADATA."CLOSE" (h);
RETURN doc;
END;
/

SELECT get_table_md;
```

查询结果如下：

```
CREATE TABLE "RESOURCES"."TIMECARDS"
(
"EMPLOYEE_ID" INT,
"WEEK" NUMBER(2,0),
"JOB_ID" VARCHAR2(10),
"HOURS_WORKED" NUMBER(4,2),
FOREIGN KEY("EMPLOYEE_ID") REFERENCES "RESOURCES"."EMPLOYEE"("EMPLOYEEID")
) STORAGE(ON "MAIN", CLUSTERBTR) ;
```

例 3 使用 DBMS\_METADATA 浏览接口获取元数据。

```
SELECT DBMS_METADATA.GET_DDL('TABLE','TIMECARDS','RESOURCES');
```

查询结果同例 2。

例 4 获取多个对象。

```
DROP TABLE my_metadata;
CREATE TABLE my_metadata (md clob);
CREATE OR REPLACE PROCEDURE get_tables_md IS
//定义局部变量
h NUMBER;  //handle returned by 'OPEN'
th NUMBER; //handle returned by 'ADD_TRANSFORM'
doc CLOB;  //metadata is returned in a CLOB
BEGIN
//指定对象类型
h := DBMS_METADATA."OPEN" ('TABLE');

// 使用过滤器指定模式
DBMS_METADATA.SET_FILTER(h,'SCHEMA','sysdba') ;

//获取DDL格式的语句
DBMS_METADATA.ADD_TRANSFORM(H,'DDL');

//获取对象
LOOP
    doc := DBMS_METADATA.FETCH_CLOB(h);
   //当没有对象可获取时, FETCH_CLOB 返回 NULL
    EXIT WHEN doc IS NULL;
   //将元数据存入表中
    INSERT INTO my_metadata(md) VALUES (doc);
    COMMIT;
END LOOP;
//释放资源
DBMS_METADATA."CLOSE" (h);
END;
/

CALL get_tables_md;
SELECT * FROM my_metadata;
```

例 5 使用 parse items 解析特定的元数据属性。

```
DROP TABLE my_metadata;
CREATE TABLE my_metadata (
   object_type VARCHAR2(30),
   name VARCHAR2(30),
   md CLOB);
CREATE OR REPLACE PROCEDURE get_tables_and_indexes IS
//定义局部变量
h1 NUMBER; // 打开表返回的句柄
doc DBMS_METADATA.ku$_ddls;  //ku$_ddls，返回的元数据
ddl CLOB;  //对象的ddl语句
pi DBMS_METADATA.ku$_parsed_items;  //包含在ku$_ddL中的对象返回的解析项
objname VARCHAR2(30);   //解析对象的名称
BEGIN
//指定对象类型: TABLE.
h1 := DBMS_METADATA."OPEN" ('TABLE');

//获取DDL格式语句
DBMS_METADATA.ADD_TRANSFORM(H1,'DDL');

//将表名作为解析项返回
DBMS_METADATA.SET_PARSE_ITEM(h1,'NAME');

//设置循环: 获取 TABLE 对象
LOOP
    doc := dbms_metadata.fetch_ddl(h1);

//当没有对象可获取时，FETCH_CLOB 返回 NULL
    EXIT WHEN doc IS NULL;

//循环ku$_ddls表中的行
    FOR i IN doc.FIRST..doc.LAST LOOP
          ddl := doc(i).ddlText;
        pi := doc(i).parsedItem;
        //循环返回的解析项
        IF pi IS NOT NULL AND pi.COUNT > 0 THEN
            FOR j IN pi.FIRST..pi.LAST LOOP
                IF pi(j).item='NAME' THEN
                    objname := pi(j).value;
                END IF;
            END LOOP;
         END IF;
        //将该对象的信息插入表 my_metadata中
         INSERT INTO my_metadata(object_type, name, md)
             VALUES ('TABLE',objname,ddl);
            COMMIT;
         END LOOP;
    END LOOP;
    DBMS_METADATA."CLOSE" (h1);
END;
/
CALL get_tables_and_indexes;
SELECT * FROM my_metadata;
```

例 6 使用 SET\_TRANSFORM\_PARAM 格式化过滤约束。

```
//建表
DROP TABLE "SYSDBA"."T1";
CREATE TABLE "SYSDBA"."T1"
(
"C1" CHAR(10) NOT NULL,
"C2" CHAR(10),
CONSTRAINT "PK" PRIMARY KEY("C1")) STORAGE(ON "MAIN", CLUSTERBTR);
//格式化过滤约束
DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM, 'CONSTRAINTS', FALSE, '');
//查看表定义
SELECT DBMS_METADATA.GET_DDL('TABLE','T1','SYSDBA');
```

执行结果如下：

```
CREATE TABLE "SYSDBA"."T1"
(
"C1" CHAR(10),
"C2" CHAR(10)) STORAGE(ON "MAIN", CLUSTERBTR);
```

例 7 使用 ADD\_TRANSFORM 返回对象的 ddl 格式的语句。

```
CREATE TABLE TRANS1(C1 INT);
CREATE OR REPLACE FUNCTION get_table_md RETURN CLOB IS
h NUMBER; //handle returned by OPEN
th NUMBER; //handle returned by ADD_TRANSFORM
doc CLOB;
BEGIN
h := DBMS_METADATA."OPEN" ('TABLE');
PRINT 'set_filter|'||h;
//使用过滤器返回特定的对象
DBMS_METADATA.SET_FILTER(h,'SCHEMA','SYSDBA');
DBMS_METADATA.SET_FILTER(h,'NAME','TRANS1');
//获取对象
th:=DBMS_METADATA.ADD_TRANSFORM(h,'DDL1');
DBMS_METADATA.SET_TRANSFORM_PARAM(th,'STORAGE',FALSE);
doc := DBMS_METADATA.FETCH_CLOB(h);
DBMS_METADATA."CLOSE" (h);
RETURN doc;
END;
/
select get_table_md;
```

执行结果：

```
//无STORAGE标签
<?XML VERSION="1.0"?><ROWSET><ROW><TABLE_T><SCHEMANAME>SYSDBA</SCHEMANAME><NAME>TRANS1</NAME><COL_LIST><COL_LIST_ITEM><COL_NAME>C1</COL_NAME><COLTYPE>INT</COLTYPE></COL_LIST_ITEM></COL_LIST></TABLE_T></ROW></ROWSET>
```

例 8 使用 check\_handle 打印句柄使用情况。

```
DECLARE
    H NUMBER; 
    H1 NUMBER;
BEGIN
  H := DBMS_METADATA."OPEN" ('CONSTRAINT');
  H1 := DBMS_METADATA."OPEN" ('CONSTRAINT');
  DBMS_METADATA.CHECK_HANDLE();
  DBMS_METADATA."CLOSE_ALL";
  DBMS_METADATA.CHECK_HANDLE();
END;
/
```

打印结果如下：

```
HANDLE   USE
1  
2  
3  
4  
5  
6  
7  
8  
9  1
10  1
HANDLE   USE
1  
2  
3  
4  
5  
6  
7  
8  
9  0
10  0
```
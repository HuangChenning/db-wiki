---
title: "DPI 编程指南"
book: "DM8 程序员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dpi-rogramming-guide.html
tags:
  - dameng
  - dm8
  - programmer
---

## 2.1 DPI 简介

本章主要介绍 DPI 的基本概念以及使用方法，以便于用户更好地使用 DPI 编写应用程序。DPI 提供了访问 DM 数据库的最直接的途径。

DPI 的实现参考了 Microsoft ODBC 3.0 标准，函数功能以及调用过程与 ODBC 3.0 十分类似，命名统一采用 dpi 开头的小写英文字母方式，各个单词之间以下划线分割(例：ODBC 函数 SQLAllocStmt 对应的 DPI 函数就是 dpi\_alloc\_stmt)，用户可以参考《Microsoft ODBC 3.0 程序员参考手册（第二卷）》之 API 参考部分的函数说明及调用方法。

**句柄**

句柄是用于 DPI 函数申请和使用资源的变量。达梦 DPI 包含以下句柄：

| **句柄** | **说明** | **宏定义** |
| --- | --- | --- |
| dhenv | 环境句柄 | DSQL\_HANDLE\_ENV |
| dhcon | 连接句柄 | DSQL\_HANDLE\_DBC |
| dhstmt | 语句句柄 | DSQL\_HANDLE\_STMT |
| dhdesc | 描述符句柄 | DSQL\_HANDLE\_DESC |
| dhloblctr | Lob 句柄 | DSQL\_HANDLE\_LOB\_LOCATOR |
| dhobj | 复合类型句柄 | DSQL\_HANDLE\_OBJECT |
| dhobjdesc | 复合类型描述符句柄 | DSQL\_HANDLE\_OBJDESC |
| dhbfile | BFILE 文件句柄 | DSQL\_HANDLE\_BFILE |

**返回值**

DPI 的函数执行结果通过返回值来反馈给用户，DPI 包含以下返回值：

| **宏定义** | **值** | **说明** |
| --- | --- | --- |
| DSQL\_SUCCESS | 0 | 执行成功 |
| DSQL\_SUCCESS\_WITH\_INFO | 1 | 执行成功，有警告信息 |
| DSQL\_NO\_DATA | 100 | 未取得数据 |
| DSQL\_ERROR | \-1 | 执行失败 |
| DSQL\_INVALID\_HANDLE | \-2 | 非法的句柄 |
| DSQL\_NEED\_DATA | 99 | 需要数据 |
| DSQL\_STILL\_EXECUTING | 2 | 语句正在执行 |
| DSQL\_PARAM\_DATA\_AVAILABLE | 101 | 有参数值可以获取 |

**数据类型**

数据类型为数据库中字段类型和 C 语言的数据类型。

DPI 中包括以下 DSQL 类型，对应对象创建时指定的类型：

| **宏定义** | **定义类型** | **说明** |
| --- | --- | --- |
| DSQL\_CHAR | char\[(n)\] | 定长字符类型 |
| DSQL\_VARCHAR | varchar(n) | 变长字符类型 |
| DSQL\_BIT | bit | 位类型 |
| DSQL\_TINYINT | tinyint | 有符号小整型（1 字节） |
| DSQL\_SMALLINT | smallint | 有符号短整型（2 字节） |
| DSQL\_INT | int | 有符号整型（4 字节） |
| DSQL\_BIGINT | bigint | 有符号长整型（8 字节） |
| DSQL\_DEC | dec\[(p,s)\] numeric\[(p,s)\] number\[(p,s)\] | 精确数字类型 |
| DSQL\_FLOAT | real | 单精度浮点型 |
| DSQL\_DOUBLE | float double | 双精度浮点型 |
| DSQL\_BLOB | blob image longvarbinary | 二进制大字段 |
| DSQL\_DATE | date | 日期 |
| DSQL\_TIME | time\[(n)\] | 时间 |
| DSQL\_TIMESTAMP | timestamp\[(n)\] | 时间戳 |
| DSQL\_BINARY | binary\[(n)\] | 二进制类型 |
| DSQL\_VARBINARY | varbinary\[(n)\] | 变长二进制类型 |
| DSQL\_CLOB | clob text longvarchar | 字符大字段 |
| DSQL\_TIME\_TZ | time with time zone | 带时区的时间类型 |
| DSQL\_TIMESTAMP\_TZ | timestamp with time zone | 带时区的时间戳类型 |
| DSQL\_RSET | cursor | 结果集类型 |
| DSQL\_CLASS | class | class 复合类型 |
| DSQL\_RECORD | record | record 复合类型 |
| DSQL\_ARRAY | array | 动态 array |
| DSQL\_SARRAY | array | 静态 array |
| DSQL\_INTERVAL\_YEAR | interval year | 年时间间隔类型 |
| DSQL\_INTERVAL\_MONTH | interval month | 月时间间隔类型 |
| DSQL\_INTERVAL\_DAY | interval day | 日时间间隔类型 |
| DSQL\_INTERVAL\_HOUR | interval hour | 时时间间隔类型 |
| DSQL\_INTERVAL\_MINUTE | interval minute | 分时间间隔类型 |
| DSQL\_INTERVAL\_SECOND | interval second | 秒时间间隔类型 |
| DSQL\_INTERVAL\_YEAR\_TO\_MONTH | interval year to month | 年转月 时间间隔类型 |
| DSQL\_INTERVAL\_DAY\_TO\_HOUR | interval day to hour | 日转时 时间间隔类型 |
| DSQL\_INTERVAL\_DAY\_TO\_MINUTE | interval day to minute | 日转分 时间间隔类型 |
| DSQL\_INTERVAL\_DAY\_TO\_SECOND | interval day to second | 日转秒 时间间隔类型 |
| DSQL\_INTERVAL\_HOUR\_TO\_MINUTE | interval hour to minute | 时转分 时间间隔类型 |
| DSQL\_INTERVAL\_HOUR\_TO\_SECOND | interval hour to second | 时转秒 时间间隔类型 |
| DSQL\_INTERVAL\_MINUTE\_TO\_SECOND | interval minute to second | 分转秒 时间间隔类型 |
| DSQL\_BOOLEAN | boolean | bool 类型 |

DPI 中包括以下 C 类型，对应绑定时使用的数据类型：

| **宏定义** | **类型** | **说明** |
| --- | --- | --- |
| DSQL\_C\_NCHAR | char | 字符类型 |
| DSQL\_C\_SSHORT | signed short | 有符号短整型 |
| DSQL\_C\_USHORT | unsigned short | 无符号短整型 |
| DSQL\_C\_SLONG | signed int | 有符号整型 |
| DSQL\_C\_ULONG | unsigned int | 无符号整型 |
| DSQL\_C\_FLOAT | float | 单精度浮点型 |
| DSQL\_C\_DOUBLE | double | 双精度浮点型 |
| DSQL\_C\_BIT | char | 位类型 |
| DSQL\_C\_STINYINT | char | 有符号小整型 |
| DSQL\_C\_UTINYINT | unsigned char | 无符号小整型 |
| DSQL\_C\_SBIGINT | \_\_int64 | 有符号长整型，注 1：在 Windows 操作系统下，C 中的定义为\_\_int64，在其他操作系统下会有其他的表示方式 |
| DSQL\_C\_UBIGINT | unsigned\_\_int64 | 无符号长整型 |
| DSQL\_C\_BINARY | unsigned char | 二进制类型 |
| DSQL\_C\_DATE | dpi\_date\_t   其结构体类型如下：   struct dpi\_date\_struct{ sdint2 year;   udint2 month;   udint2 day;   }; | 日期类型 |
| DSQL\_C\_TIME | dpi\_time\_t   结构体类型如下：   struct dpi\_time\_struct   {   udint2 hour;   udint2 minute;   udint2 second;   }; | 时间类型 |
| DSQL\_C\_TIMESTAMP | dpi\_timestamp\_t   结构体类型如下   struct dpi\_timestamp\_struct   {   sdint2 year;   udint2 month;   udint2 day;   udint2 hour;   udint2 minute;   udint2 second;   udint4 fraction;   }; | 日期时间类型   fraction 的单位是纳秒，取值范围是 0~999,999,999 |
| DSQL\_C\_NUMERIC | dpi\_numeric\_t   结构体类型如下   struct dpi\_numeric\_struct   {   udbyte precision;   sdbyte scale;   udbyte sign;   Udbyte val\[DPI\_MAX\_NUMERIC\_LEN\];   }; | 数字类型   sign 值为 1 表示正数，0 表示负数 |
| DSQL\_C\_INTERVAL\_YEAR | dpi\_interval\_t   结构体类型如下：   struct dpi\_interval\_struct   {   DPIINTERVAL interval\_type;   sdint2 interval\_sign;   union {   dpi\_year\_month\_t year\_month;   dpi\_day\_second\_t day\_second;   } intval;   };      struct dpi\_year\_month\_struct   {   udint4 year;   udint4 month;   };   struct dpi\_day\_second\_struct   {   udint4 day;   udint4 hour;   udint4 minute;   udint4 second;   udint4 fraction;   }; | 年时间间隔类型   fraction 的单位是纳秒，取值范围是 0~999,999,999 |
| DSQL\_C\_INTERVAL\_MONTH | dpi\_interval\_t | 月时间间隔类型 |
| DSQL\_C\_INTERVAL\_DAY | dpi\_interval\_t | 日时间间隔类型 |
| DSQL\_C\_INTERVAL\_HOUR | dpi\_interval\_t | 时时间间隔类型 |
| DSQL\_C\_INTERVAL\_MINUTE | dpi\_interval\_t | 分时间间隔类型 |
| DSQL\_C\_INTERVAL\_SECOND | dpi\_interval\_t | 秒时间间隔类型 |
| DSQL\_C\_INTERVAL\_YEAR\_TO\_MONTH | dpi\_interval\_t | 年转月 时间间隔类型 |
| DSQL\_C\_INTERVAL\_DAY\_TO\_HOUR | dpi\_interval\_t | 日转时 时间间隔类型 |
| DSQL\_C\_INTERVAL\_DAY\_TO\_MINUTE | dpi\_interval\_t | 日转分 时间间隔类型 |
| DSQL\_C\_INTERVAL\_DAY\_TO\_SECOND | dpi\_interval\_t | 日转秒 时间间隔类型 |
| DSQL\_C\_INTERVAL\_HOUR\_TO\_MINUTE | dpi\_interval\_t | 时转分 时间间隔类型 |
| DSQL\_C\_INTERVAL\_HOUR\_TO\_SECOND | dpi\_interval\_t | 时转秒 时间间隔类型 |
| DSQL\_C\_INTERVAL\_MINUTE\_TO\_SECOND | dpi\_interval\_t | 分转秒 时间间隔类型 |
| DSQL\_C\_DEFAULT | \- | 自动映射类型 |
| DSQL\_C\_LOB\_HANDLE | dhloblctr | 大字段句柄 |
| DSQL\_C\_RSET | dhstmt | 结果集类型 |
| DSQL\_C\_CLASS | dhobj | 复合对象类型 |
| DSQL\_C\_RECORD | dhobj | 复合对象类型 |
| DSQL\_C\_ARRAY | dhobj | 复合对象类型 |
| DSQL\_C\_SARRAY | dhobj | 复合对象类型 |
| DSQL\_C\_WCHAR | wchar\_t | 宽字节类型 |
| DSQL\_C\_BOOLEAN | dboolean | 有符号整形。有效值 0/1 |

**诊断**

函数调用的返回信息放在诊断区域中。每一个环境、连接、及描述符句柄都有一个诊断区域。在诊断区域的头字段返回一般的函数执行信息，它的记录字段记录函数调用的错误信息和警告。用户可以指定获取某一个记录的信息从而更准确地判断函数执行的情况。

## 2.2 DPI 句柄

### 2.2.1 环境句柄

客户端程序要和数据库服务器进行通信，必须首先进行环境的设置，需要使用到环境句柄。一个环境句柄可以包含多个连接句柄。客户端程序可以通过函数 dpi\_alloc\_env 来申请一个环境句柄。环境句柄申请成功后就可以通过函数 dpi\_alloc\_con 来申请连接句柄了。环境句柄包含属性如下表所示：

| **属性** | **说明** | **字段类型** | **取值** |
| --- | --- | --- | --- |
| DSQL\_ATTR\_LOCAL\_CODE | 本地编码 | sdint4 | PG\_GBK 等 |
| DSQL\_ATTR\_LANG\_ID | 错误消息的语言 | sdint4 | LANGUAGE\_CN（表示简体中文）、LANGUAGE\_EN（表示英文）、LANGUAGE\_CNT\_HK（表示香港繁体中文） |

### 2.2.2 连接句柄

客户端程序要和数据库服务器进行通信，必须和数据库服务器建立连接。所以需要先连接数据库服务器，再使用数据库函数 dpi\_alloc\_con 申请连接句柄。要申请连接句柄必须先成功申请环境句柄。一个连接只能属于一个环境句柄。申请连接句柄成功后可以通过函数 dpi\_login 来进行数据的连接登录。

连接句柄包含属性如下表所示：

| **属性** | **说明** | **字段类型** | **取值** |
| --- | --- | --- | --- |
| DSQL\_ATTR\_ACCESS\_MODE | 连接的访问模式（可读写） | udint4 | DSQL\_MODE\_READ\_ONLY 或者 DSQL\_MODE\_READ\_WRITE。 缺省为 DSQL\_MODE\_READ\_WRITE |
| DSQL\_ATTR\_ASYNC\_ENABLE | 允许异步执行，暂未支持相应功能 | udint4 | 未支持 |
| DSQL\_ATTR\_AUTO\_IPD | 自动分配参数描述符（只读） | udint4 |  |
| DSQL\_ATTR\_AUTOCOMMIT | 自动提交（可读写） | udint4 | DSQL\_AUTOCOMMIT\_ON 或者 DSQL\_AUTOCOMMIT\_OFF。 缺省为 DSQL\_AUTOCOMMIT\_ON |
| DSQL\_ATTR\_CLIENT\_VERSION | DPI 接口版本（只读） | sdbyte\* |  |
| DSQL\_ATTR\_CONNECTION\_DEAD | 检测连接是否存活（只读） | udint4 | DSQL\_CD\_TRUE 或 DSQL\_CD\_FALSE |
| DSQL\_ATTR\_CONNECTION\_TIMEOUT | 执行超时时间（可读写） | udint4 | udint4 数值 |
| DSQL\_ATTR\_LOGIN\_TIMEOUT | 登录超时时间 | udint4 | udint4 数值 |
| DSQL\_ATTR\_PACKET\_SIZE | 网络包大小，暂未支持相应功能 | udint4 |  |
| DSQL\_ATTR\_TXN\_ISOLATION | 事务隔离级（可读写） | udint4 | ISO\_LEVEL\_READ\_UNCOMMITTED，ISO\_LEVEL\_READ\_COMMITTED，ISO\_LEVEL\_SERIALIZABLE |
| DSQL\_ATTR\_LOGIN\_PORT | 登录端口号（可读写） | Udint2 | sdint2 数值，缺省为 5236 |
| DSQL\_ATTR\_STR\_CASE\_SENSITIVE | 大小写是否敏感（只读） | udint4 |  |
| DSQL\_ATTR\_MAX\_ROW\_SIZE | 行最大字节数（只读） | udint4 |  |
| DSQL\_ATTR\_LOGIN\_USER | 登录用户（只读） | sdbyte\* |  |
| DSQL\_ATTR\_LOGIN\_SERVER | 登录服务器 IP 或 unixsocket 文件路径名。如果 DSQL\_ATTR\_INET\_TYPE 是 Unix SOCKET，那么 DSQL\_ATTR\_LOGIN\_SERVER 必须填写 unixsocket 文件路径名。两者需配套使用。只有 Linux 环境才支持 UNIXSOCKET，Windows 不支持（设置了也会被忽略） | sdbyte\* |  |
| DSQL\_ATTR\_INSTANCE\_NAME | 实例名称（只读） | sdbyte\* |  |
| DSQL\_ATTR\_CURRENT\_SCHEMA | 当前模式（可读写）。若在用户登录之前设置模式，则会将用户会话模式设置成指定的模式，指定为不存在的模式将报错；若在用户登录以后再设置模式会报错 | sdbyte\* |  |
| DSQL\_ATTR\_SERVER\_CODE | 服务器的编码（只读） | sdint4 |  |
| DSQL\_ATTR\_LOCAL\_CODE | 本地编码（可读写） | sdint4 | PG\_SQL\_ASCII，PG\_UTF8，PG\_GBK，PG\_BIG5，PG\_ISO\_8859\_9，PG\_EUC\_JP，PG\_EUC\_KR，PG\_KOI8R，PG\_ISO\_8859\_1，PG\_GB18030，PG\_ISO\_8859\_11，PG\_UTF16 |
| DSQL\_ATTR\_LANG\_ID | 错误消息的语言（可读写） | sdint4 | LANGUAGE\_CN（表示简体中文）、LANGUAGE\_EN（表示英文）、LANGUAGE\_CNT\_HK（表示香港繁体中文） |
| DSQL\_ATTR\_APP\_NAME | 应用名称（可读写） | sdbyte\* |  |
| DSQL\_ATTR\_COMPRESS\_MSG | 消息压缩（可读写） | sdint4 | DSQL\_TRUE 压缩，DSQL\_FALSE 不压缩 |
| DSQL\_ATTR\_CURRENT\_CATALOG | （只读） | sdbyte\* |  |
| DSQL\_ATTR\_RWSEPARATE | 读写分离（可读写） | udint4 | DSQL\_RWSEPARATE\_OFF 关闭；DSQL\_RWSEPARATE\_ON 开启；DSQL\_RWSEPARATE\_ON2 开启，只连接事务一致性备库 |
| DSQL\_ATTR\_RWSEPARATE\_PERCENT | 读写分离比例（可读写） | udint4 | 取值范围 0~100，缺省为 25 |
| DSQL\_ATTR\_TRX\_STATE | 事务状态（只读） | sdint4 | DSQL\_TRX\_ACTIVE 和 DSQL\_TRX\_COMPLETE |
| DSQL\_ATTR\_USE\_STMT\_POOL | 语句句柄缓存池（可读写） | dint4 | DSQL\_TRUE 开启，DSQL\_FALSE 关闭 |
| DSQL\_ATTR\_SSL\_PATH | SSL 证书所在的路径（可读写） | sdbyte\* | 字符串（最长 256） |
| DSQL\_ATTR\_SSL\_PWD | SSL 加密密码（可读写） | sdbyte\* | 字符串（最长 512） |
| DSQL\_ATTR\_MPP\_LOGIN | mpp 登录方式（可读写） | sdint4 | DSQL\_MPP\_LOGIN\_GLOBAL 全局登录   DSQL\_MPP\_LOGIN\_LOCAL 本地登录 |
| DSQL\_ATTR\_UKEY\_NAME | UKEY 登录验证的 UKEY 名 | sdbyte\* |  |
| DSQL\_ATTR\_UKEY\_PIN | UKEY 登录验证时的 UKEY 密钥 | sdbyte\* | 最长 256 |
| DSQL\_ATTR\_UDP\_FLAG | UDP 通讯的收发模式 | sdint4 | 1 表示单发单收，2 表示多发多收，缺省为 2 |
| DSQL\_ATTR\_INET\_TYPE | 指定网络连接类型 | sdbyte\* | 取值为：   DSQL\_INET\_TCP：对应 TCP 协议；   DSQL\_INET\_UDP：对应 UDP 协议；   DSQL\_INET\_IPC：对应 IPC 协议；   DSQL\_INET\_UNIXSOCKET：对应 UNIXSOCKET 协议；   DSQL\_INET\_RDMA：对应 RDMA 协议；   缺省为 DSQL\_INET\_TCP |
| DSQL\_ATTR\_LOGIN\_CERTIFICATE | 指定登录加密用户名密码公钥所在的路径。该属性和 dm\_svc.conf 中配置项 LOGIN\_CERTIFICATE 功能一样。两者不一致时，DSQL\_ATTR\_LOGIN\_CERTIFICATE 设置优先 | udbyte\* | 字符串（最长 256） |
| DSQL\_ATTR\_TCNAME\_LOWER | 是否将通过描述获取的表名和列名转换为小写 | udint4 | DSQL\_TRUE 或者 DSQL\_FALSE。 缺省为 DSQL\_FALSE |
| DSQL\_ATTR\_QUOTE\_REPLACE | 指定连接上所创建的语句句柄在执行语句时是否替换语句中的双引号为单引号 | udint4 | DSQL\_TRUE 是；DSQL\_FALSE 否。缺省为 DSQL\_FALSE |
| DSQL\_ATTR\_COMPATIBLE\_MODE | 运行兼容模式。在连接之前可设置 | udint4 | DSQL\_COMPATIBLE\_MODE\_DM0UL 或者 DSQL\_COMPATIBLE\_MODE\_ORA1UL。缺省为 0 |
| DSQL\_ATTR\_DM\_SVC\_PATH | 连接使用的 dm\_svc.conf 所在目录。配置后只读取连接所用的服务配置信息，其他不影响全局设置。设置后优先使用，在该路径下找不到 dm\_svc.conf 或者该文件中没有指定的服务配置项,则转向全局配置文件查找 | sdbyte\* |  |
| DSQL\_ASYNC\_MODE | 连接的异步模式（只读） | udint4 | DSQL\_AM\_NONE（不支持）   DSQL\_AM\_CONNECTION（连接级异步）   DSQL\_AM\_STATEMENT（语句级异步） |

### 2.2.3 语句句柄

DPI 用语句句柄来存取名称、参数、错误以及其他关于语句处理流程的信息。在一个连接句柄下可以有多个语句句柄，一个特定的 SQL 语句总是和一个连接句柄相联系的。在 DPI 中，通过语句句柄可以了解到语句的状态、当前语句的诊断信息、语句的参数以及结果集绑定的应用程序变量等信息、每一个语句的当前属性值。客户程序调用 dpi\_alloc\_stmt 函数申请一个语句句柄，用 dpi\_free\_stmt 函数释放一个语句句柄。

语句句柄包含属性如下表所示：

| **属性** | **说明** | **字段类型** | **取值** |
| --- | --- | --- | --- |
| DSQL\_ATTR\_ROW\_BIND\_TYPE | 行绑定类型（可读写） | ulength |  |
| DSQL\_ATTR\_ROW\_BIND\_OFFSET\_PTR | 行绑定偏移（可读写） | ulength\* |  |
| DSQL\_ATTR\_ROW\_OPERATION\_PTR | 绑定行数据处理指示（可读写） | udint2\* |  |
| DSQL\_ATTR\_ROW\_STATUS\_PTR | 获取行数据状态指示（可读写） | udint2\* |  |
| DSQL\_ATTR\_ROWS\_FETCHED\_PTR | 已获取行数指示（可读写） | ulength\* |  |
| DSQL\_ATTR\_ROW\_ARRAY\_SIZE | 行集大小（可读写） | ulength |  |
| DSQL\_ATTR\_ROWSET\_SIZE | 行集大小（可读写） | ulength |  |
| DSQL\_ATTR\_USE\_BOOKMARKS | 是否使用书签（可读写） | ulength |  |
| DSQL\_ATTR\_FETCH\_BOOKMARK\_PTR | 书签值（可读写） | ulength\* |  |
| DSQL\_ATTR\_PARAM\_BIND\_OFFSET\_PTR | 参数绑定值的偏移位置（可读写） | ulength\* |  |
| DSQL\_ATTR\_PARAM\_BIND\_TYPE | 参数绑定类型（可读写） | ulength |  |
| DSQL\_ATTR\_PARAM\_OPERATION\_PTR | 参数数据处理指示（可读写） | udint2\* |  |
| DSQL\_ATTR\_PARAM\_STATUS\_PTR | 参数使用状态（可读写） | udint2\* |  |
| DSQL\_ATTR\_PARAMS\_PROCESSED\_PTR | 参数集中参数处理的个数（可读写） | ulength\* |  |
| DSQL\_ATTR\_PARAMSET\_SIZE | 参数集大小（可读写） | ulength |  |
| DSQL\_ATTR\_ROW\_NUMBER | 当前行位置（只读） | ulength |  |
| DSQL\_ATTR\_IMP\_ROW\_DESC | 服务器端的行描述（只读） | void\* |  |
| DSQL\_ATTR\_IMP\_PARAM\_DESC | 服务器端参数描述（只读） | void\* |  |
| DSQL\_ATTR\_APP\_PARAM\_DESC | 应用程序参数描述（可读写） | void\* |  |
| DSQL\_ATTR\_APP\_ROW\_DESC | 应用程序行描述（可读写） | void\* |  |
| DSQL\_ATTR\_CURSOR\_TYPE | 游标类型（可读写） | ulength | DSQL\_CURSOR\_FORWARD\_ONLY DSQL\_CURSOR\_STATIC DSQL\_CURSOR\_KEYSET\_DRIVEN DSQL\_CURSOR\_DYNAMIC |
| DSQL\_ATTR\_CONCURRENCY | 游标的并发方式（可读写） | ulength | DSQL\_CONCUR\_READ\_ONLY DSQL\_CONCUR\_LOCK DSQL\_CONCUR\_ROWVER DSQL\_CONCUR\_VALUES |
| DSQL\_ATTR\_CURSOR\_SCROLLABLE | 游标是否可滚动（可读写） | ulength | DSQL\_NONSCROLLABLE DSQL\_SCROLLABLE |
| DSQL\_ATTR\_CURSOR\_SENSITIVITY | 结果集修改对其他游标是否可见（可读写） | ulength | DSQL\_UNSPECIFIED DSQL\_INSENSITIVE DSQL\_SENSITIVE |
| DSQL\_ATTR\_MAX\_LENGTH | 字符类型或者二进制类型列的最大返回长度（可读写） | ulength |  |
| DSQL\_ATTR\_MAX\_ROWS | 结果集返回的最大行数（可读写） | ulength |  |
| DSQL\_ATTR\_NOSCAN | 是否检查语句中的转义符（可读写），暂未支持相应功能 | ulength |  |
| DSQL\_ATTR\_QUERY\_TIMEOUT | 语句执行超时时间（可读写） | ulength |  |
| DSQL\_ATTR\_RETRIEVE\_DATA | 游标滚动后是否检索数据（可读写），暂未支持相应功能 | ulength |  |
| DSQL\_ATTR\_ENABLE\_AUTO\_IPD | 自动分配参数描述符（可读写） | ulength | DSQL\_TRUE 或者 DSQL\_FALSE |
| DSQL\_ATTR\_ASYNC\_ENABLE | 异步执行（可读写），支持语句级异步 | ulength | DSQL\_ASYNC\_ENABLE\_OFF 0 DSQL\_ASYNC\_ENABLE\_ON 1 |
| DSQL\_ATTR\_KEYSET\_SIZE | 键集驱动游标结果集中行的大小（可读写），暂未支持相应功能 | ulength |  |
| DSQL\_ATTR\_SIMULATE\_CURSOR | 指定游标更新和删除是否只影响单行（可读写），暂未支持相应功能 |  |  |
| DSQL\_ATTR\_METADATA\_ID | 是否允许模糊查询（可读写） | ulength | DSQL\_TRUE DSQL\_FALSE |
| DSQL\_ATTR\_SQL\_CHARSET | 字符集编码（可读写） | sdint4 | PG\_SQL\_ASCII，PG\_UTF8， PG\_GBK，PG\_BIG5， PG\_ISO\_8859\_9，PG\_EUC\_JP， PG\_EUC\_KR，PG\_KOI8R， PG\_ISO\_8859\_1，PG\_GB18030， PG\_ISO\_8859\_11，PG\_UTF16 |
| DSQL\_ATTR\_IGN\_BP\_ERR | 批量参数错误数据处理策略（可读写） | sdint4 | DSQL\_TRUE DSQL\_FALSE |
| DSQL\_ATTR\_BP\_MAX\_ERRS | 开启容错的情况允许的最大容错行数（可读写） | ulength |  |
| DSQL\_ATTR\_QUOTE\_REPLACE | 指定连接上所创建的语句句柄在执行语句时是否替换语句中的双引号为单引号（可读写） | udint4 | DSQL\_TRUE 是；DSQL\_FALSE 否。缺省为继承自句柄所在连接句柄的属性 |

### 2.2.4 描述符句柄

一个描述符句柄是指包含列或者动态参数信息的一个数据结构。对于许多应用程序，直接访问与操作描述符会使得操作更加简单。在 DPI 中描述符分为以下几种类型：

1. 应用程序参数描述符（APD）：包含被应用程序设置的输入动态参数信息或者随执行 SQL 语句中的 CALL 产生的输出动态参数信息。例如：地址、长度、C 类型等。
2. 驱动执行参数描述符（IPD）：对于输入参数，在完成应用程序指定的数据转换之后，它包含了与 APD 相同参数的信息。对于输出参数，在进行了一些应用程序指定的数据转换之前，它包含了返回参数的信息。例如：SQL 数据类型、长度等。
3. 驱动执行行描述符（IRD）：包含结果集中列绑定的信息。例如：SQL 数据类型、长度等。
4. 应用程序行描述符（ARD）：包含应用程序绑定列结果集的信息。例如：地址、长度、C 类型等。

描述符字段包括头字段与记录域字段，它们全面地描述列与参数。

一个描述符包括了以下的头字段：

| **属性** | **说明** | **字段类型** |
| --- | --- | --- |
| DSQL\_DESC\_ALLOC\_TYPE | 描述符的分配类型（只读） | sdint2 |
| DSQL\_DESC\_ARRAY\_SIZE | 描述符的记录数组大小（APD，ARD 可读写） | ulength |
| DSQL\_DESC\_ARRAY\_STATUS\_PTR | 数据状态指示（可读写） | udint2\* |
| DSQL\_DESC\_BIND\_OFFSET\_PTR | 绑定数据偏移（APD，ARD 可读写） | slength\* |
| DSQL\_DESC\_BIND\_TYPE | 绑定类型（APD，ARD 可读写） | ulength |
| DSQL\_DESC\_COUNT | 描述符包含记录个数（APD，ARD，IPD 可读写，IRD 只读） | udint2 |
| DSQL\_DESC\_ROWS\_PROCESSED\_PTR | 处理数据的个数（IRD，IPD 可读写） | ulength\* |

一个描述符包括了以下的记录域字段：

| **属性** | **说明** | **字段类型** |
| --- | --- | --- |
| DSQL\_DESC\_AUTO\_UNIQUE\_VALUE | 结果集列是否是自动增长的（IRD 只读） | sdint4 |
| DSQL\_DESC\_BASE\_COLUMN\_NAME | 结果集列的基列列名（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_BASE\_TABLE\_NAME | 结果集列的基表名（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_CASE\_SENSITIVE | 对象是否大小写敏感（IRD，IPD 只读） | sdint4 |
| DSQL\_DESC\_CATALOG\_NAME | 列对应的库名（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_CONCISE\_TYPE | 对象对应的精简类型（APD，ARD，IPD 可读写，IRD 只读） | sdint2 |
| DSQL\_DESC\_DATA\_PTR | 绑定数据的地址（APD，ARD 可读写） | void\* |
| DSQL\_DESC\_DATETIME\_INTERVAL\_CODE | 时间日期类型，时间日期间隔类型的子类型（APD，ARD，IPD 可读写，IRD 只读） | sdint2 |
| DSQL\_DESC\_DATETIME\_INTERVAL\_PRECISION | 时间间隔类型的引导精度（APD，ARD，IPD 可读写，IRD 只读） | sdint4 |
| DSQL\_DESC\_DISPLAY\_SIZE | 列的显示长度（IRD 只读） | slength |
| DSQL\_DESC\_FIXED\_PREC\_SCALE | 指示是否是固定精度刻度的数字类型（IPD，IRD 只读） | sdint2 |
| DSQL\_DESC\_INDICATOR\_PTR | 指示符地址（APD，ARD 可读写） | slength\* |
| DSQL\_DESC\_LABEL | 列的标签（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_LENGTH | 字符类型的最大或实际字符长度或者二进制类型的最大或实际字节长度（APD，ARD，IPD 可读写，IRD 只读） | ulength |
| DSQL\_DESC\_LITERAL\_PREFIX | 列的前缀字符（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_LITERAL\_SUFFIX | 列的后缀字符（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_LOCAL\_TYPE\_NAME | 本地的类型名（IPD，IRD 只读） | sdbyte\* |
| DSQL\_DESC\_NAME | 列的别名（IPD 可读写，IRD 只读） | sdbyte\* |
| DSQL\_DESC\_NULLABLE | 记录域是否可以为空（IPD，IRD 只读） | sdint2 |
| DSQL\_DESC\_NUM\_PREC\_RADIX | 记录域数字类型精度的表示基数（APD，ARD，IPD 可读写，IRD 只读） | sdint4 |
| DSQL\_DESC\_OCTET\_LENGTH | 记录域的最大字节长度（APD，ARD，IPD 可读写，IRD 只读） | slength |
| DSQL\_DESC\_OCTET\_LENGTH\_PTR | 指示绑定字符类型或二进制类型的实际字节长度（APD，ARD 可读写） | slength\* |
| DSQL\_DESC\_PARAMETER\_TYPE | 参数类型（IPD 可读写） | sdint2 |
| DSQL\_DESC\_PRECISION | 精确数字类型的位数或者近似数字类型的尾数位数，或者时间类型，时间戳类型，秒间隔类型秒精度（APD，ARD，IPD 可读写，IRD 只读） | sdint2 |
| DSQL\_DESC\_ROWVER | 指示列是否记录行的版本信息（IPD，IRD 只读） | sdint2 |
| DSQL\_DESC\_SCALE | DEC 或者 NUMERIC 类型的刻度 | sdint2 |
| DSQL\_DESC\_SCHEMA\_NAME | 列所属基表所在的模式名（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_SEARCHABLE | 列的条件查询方式（IRD 只读） | sdint2 |
| DSQL\_DESC\_TABLE\_NAME | 列所在的基表表名（IRD 只读） | sdbyte\* |
| DSQL\_DESC\_TYPE | C 类型或者 DSQL 类型，时间或者间隔类型则表示的为详细的类型 DSQL\_DT 或 DSQL\_INTERVAL（APD，ARD，IPD 可读写，IRD 只读） | sdint2 |
| DSQL\_DESC\_TYPE\_NAME | 数据源的数据类型（IPD，IRD 只读） | sdbyte\* |
| DSQL\_DESC\_UNNAMED | 记录域是否是命名的（IPD 可读写，IRD 只读） | sdint2 |
| DSQL\_DESC\_UNSIGNED | 指示记录域是否为无符号数字类型（IPD，IRD 只读） | sdint2 |
| DSQL\_DESC\_UPDATABLE | 列是否为可更新（IRD 只读） | sdint2 |
| DSQL\_DESC\_BIND\_PARAMETER\_TYPE | 参数类型（IPD 可读写），暂未支持相应功能 | sdint2 |
| DSQL\_DESC\_DATETIME\_FORMAT | 时间类型格式（APD，ARD 可读写），暂未支持相应功能 | sdbyte\* |
| DSQL\_DESC\_DATETIME\_TZ\_FORMAT | 时间类型格式（APD，ARD 可读写），用于设置默认的 timestamp\_tz 的解析格式串 | sdbyte\* |
| DSQL\_DESC\_CHARSET | 字符集编码（APD，ARD 可读写），暂未支持相应功能 | sdint4 |

### 2.2.5 LOB 句柄

LOB 句柄为大字段操纵句柄，可以对大字段进行更新和读取处理。通过 lob 句柄可以获取大字段对象的长度、读取大字段实际数据、更新大字段数据、截取大字段数据。LOB 句柄从属于某一个语句句柄，可以通过 dpi\_alloc\_handle 或者 dpi\_alloc\_lob\_locator 函数进行分配，再通过绑定到某个大字段对象进行操作。在释放语句句柄时必须先释放语句句柄上所有的 LOB 句柄，否则函数会返回执行失败的错误。

## 2.3 函数原型

DPI 函数可分为常规编码下支持的函数和 UTF-16 编码下支持的函数，常规编码指的是 DPI 连接句柄 DSQL\_ATTR\_LOCAL\_CODE 属性取值中支持的编码，具体可参考 2.2.2 连接句柄 。

### 2.3.1 常规编码

**1\. dpi\_alloc\_handle**

**函数**

```
DPIRETURN
dpi_alloc_handle(
        sdint2         hndl_type,
        dhandle     hndl_in,
        dhandle     *hndl_out
);
```

**功能**

用于分配环境、连接、语句、描述符、lob、复合类型对象句柄。

**参数**

1） hndl\_type

输入参数，需要分配句柄的类型，必须为下列值之一：

- DSQL\_HANDLE\_ENV
- DSQL\_HANDLE\_DBC
- DSQL\_HANDLE\_STMT
- DSQL\_HANDLE\_DESC
- DSQL\_HANDLE\_LOB\_LOCATOR
- DSQL\_HANDLE\_OBJECT

2） hndl\_in

输入参数，通过此句柄分配新的句柄，新句柄运行环境从属此句柄。

如果 hndl\_type 为 DSQL\_HANDLE\_ENV，则这个值为 NULL；

如果 hndl\_type 为 DSQL\_HANDLE\_DBC，则这个值必须是一个环境句柄；

如果 hndl\_type 为 DSQL\_HANDLE\_STMT、DSQL\_HANDLE\_DESC 或者 DSQL\_HANDLE\_OBJECT，则这个值必须是一个连接句柄；

如果 hndl\_type 为 DSQL\_HANDLE\_LOB\_LOCATOR，则这个值必须是一个语句句柄。

3） hndl\_out

输出参数，一个存放新分配句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

如果函数执行失败，则 hndl\_out 返回 NULL。

**2\. dpi\_free\_handle**

**函数**

```
DPIRETURN
dpi_free_handle(
        sdint2         hndl_type,
        dhandle     hndl
);
```

**功能**

释放资源，用于释放句柄资源。

**参数**

1）hndl\_type

输入参数，需要被释放句柄的类型。必须为下列值之一：

- DSQL\_HANDLE\_ENV
- DSQL\_HANDLE\_DBC
- DSQL\_HANDLE\_STMT
- DSQL\_HANDLE\_DESC
- DSQL\_HANDLE\_LOB\_LOCATOR
- DSQL\_HANDLE\_OBJECT

2）hndl

输入参数，需要被释放的句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

若函数执行失败，则需要被释放的句柄依然有效。

**3\. dpi\_alloc\_env**

**函数**

```
DPIRETURN
dpi_alloc_env(
        dhenv  *dpi_henv
);
```

**功能**

分配环境句柄。

**参数**

dpi\_henv

输出参数，一个存放新分配环境句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

**说明**

该函数作用与 dpi\_alloc\_handle 指定分配 DSQL\_HANDLE\_ENV 一致。

**4\. dpi\_alloc\_con**

**函数**

```
DPIRETURN
dpi_alloc_con(
        dhenv     dpi_henv,
        dhcon      *dpi_hcon
);
```

**功能**

分配连接句柄。

**参数**

1. dpi\_henv

输入参数，通过此环境句柄分配新的连接句柄，新句柄运行环境从属此句柄。

2. dpi\_hcon

输出参数，一个存放新分配连接句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_alloc\_handle 指定分配 DSQL\_HANDLE\_DBC 一致。

**5\. dpi\_alloc\_stmt**

**函数**

```
DPIRETURN
dpi_alloc_stmt(
        dhcon         dpi_hcon,
        dhstmt         *dpi_hstm
);
```

**功能**

分配语句句柄。

**参数**

1. dpi\_hcon

输入参数，通过此连接句柄分配新的语句句柄，新句柄运行环境从属此句柄。

2. dpi\_hstmt

输出参数，一个存放新分配语句句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_alloc\_handle 指定分配 DSQL\_HANDLE\_STMT 一致。

**6\. dpi\_alloc\_desc**

**函数**

```
DPIRETURN
dpi_alloc_desc(
        dhcon     dpi_hcon,
        dhdesc     *dpi_hdesc
);
```

**功能**

分配描述符句柄。

**参数**

1. dpi\_hcon

输入参数，通过此连接句柄分配新的描述符句柄，新句柄运行环境从属此句柄。

2. dpi\_hdesc

输出参数，一个存放新分配描述符句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_alloc\_handle 指定分配 DSQL\_HANDLE\_DESC 一致。

**7\. dpi\_alloc\_lob\_locator**

**函数**

```
DPIRETURN
dpi_alloc_lob_locator(
        dhstmt         dpi_hstmt,
        dhloblctr     *dpi_loblctr
);
```

**功能**

分配 lob 句柄。

**参数**

1. dpi\_hstmt

输入参数，通过此语句句柄分配新的 lob 句柄，新句柄运行环境从属此句柄。

2. dpi\_loblctr

输出参数，一个存放新分配 lob 句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_alloc\_handle 指定分配 DSQL\_HANDLE\_LOB\_LOCATOR 一致。

**8\. dpi\_free\_env**

**函数**

```
DPIRETURN
dpi_free_env(
        dhenv         dpi_henv
);
```

**功能**

释放环境句柄。

**参数**

dpi\_henv

输入参数，需要被释放的环境句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_free\_handle 指定 DSQL\_HANDLE\_ENV 一致。

**9\. dpi\_free\_con**

**函数：**

```
DPIRETURN
dpi_free_con(
        dhcon     dpi_hcon
);
```

**功能**

释放连接句柄。

**参数**

dpi\_hcon

输入参数，需要被释放的连接句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_free\_handle 指定 DSQL\_HANDLE\_DBC 一致。在释放连接时必须保证连接已经与服务器断开，否则函数失败。

**10\. dpi\_free\_stmt**

**函数**

```
DPIRETURN
dpi_free_stmt(
        dhstmt         dpi_hstmt
);
```

**功能**

释放语句句柄。

**参数**

dpi\_hstmt

输入参数，需要被释放的语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_free\_handle 指定 DSQL\_HANDLE\_STMT 一致。在释放语句句柄时必须保证句柄上分配的 lob 句柄都已经释放，否则函数执行失败。

**11\. dpi\_free\_desc**

**函数**

```
DPIRETURN
dpi_free_desc(
        dhdesc         dpi_hdesc
);
```

**功能**

释放描述符句柄。

**参数**

dpi\_hdesc

输入参数，需要被释放的描述符句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_free\_handle 指定 DSQL\_HANDLE\_DESC 一致。所要释放的描述符句柄必须为手动分配的，否则函数执行失败。

**12\. dpi\_free\_lob\_locator**

**函数**

```
DPIRETURN
dpi_free_lob_locator(
        dhloblctr     dpi_loblctr
);
```

**功能**

释放 lob 句柄。

**参数**

dpi\_loblctr

输入参数，需要被释放的 lob 句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

该函数作用与 dpi\_free\_handle 指定 DSQL\_HANDLE\_LOB\_LOCATOR 一致。

**13\. dpi\_set\_env\_attr**

**函数**

```
DPIRETURN
dpi_set_env_attr(
        dhenv         dpi_henv,
        sdint4         attr_id,
        dpointer     val,
        sdint4         val_len
);
```

**功能**

设置环境句柄的属性。

**参数**

1） dpi\_henv

输入参数，需要被设置属性的环境句柄。

2） attr\_id

输入参数，设置的属性，参见 2.2.1 环境句柄 。

3） val

输入参数，所需设置属性的值。根据属性的不同，值可能为 32 位的整型数据或者以 0 结尾的字符串。

4） val\_len

输入参数，如果设置的 val 指向字符串或者二进制缓冲区，此参数表示 val 的字节长度。如果 val 为整型数据，则此参数忽略。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**14\. dpi\_set\_con\_attr**

**函数**

```
DPIRETURN
dpi_set_con_attr(
        dhcon         dpi_hcon,
        sdint4         attr_id,
        dpointer     val,
        sdint4         val_len
);
```

**功能**

设置连接句柄属性。

**参数**

1） dpi\_hcon

输入参数，需要被设置属性的连接句柄。

2） attr\_id

输入参数，设置的属性，参见 2.2.2 连接句柄 。

3） val

输入参数，所需设置属性的值。根据属性的不同，值可能为 32 位的整型数据或者以 0 结尾的字符串。

4） val\_len

输入参数，如果设置的 val 指向字符串或者二进制缓冲区，此参数表示 val 的字节长度。如果 val 为整型数据，则此参数忽略。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**15\. dpi\_set\_stmt\_attr**

**函数**

```
DPIRETURN
dpi_set_stmt_attr(
        dhstmt             dpi_hstmt,
        sdint4             attr_id,
        dpointer         val,
        sdint4             val_len
);
```

**功能**

设置语句句柄属性。

**参数**

1） dpi\_hstmt

输入参数，需要被设置属性的语句句柄。

2. attr\_id

输入参数，设置的属性，参见 2.2.3 语句句柄 。

3. val

输入参数，所需设置属性的值。根据属性的不同，值可能为下列之一：

- 一个描述符句柄
- 一个 udint4 类型的值
- 一个 ulength 类型的值
- 一个下列情况之一的指针：
	- 一个以 0 结尾的字符串
		- 一个二进制缓冲区
		- 一个 slength、ulength 或者 udint2 类型的值或者数组
		- 一个驱动定义的值
4. val\_len

输入参数，如果设置的 val 指向字符串或者二进制缓冲区，此参数表示 val 的字节长度。如果 val 为整型数据，则此参数忽略。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**16\. dpi\_get\_env\_attr**

**函数**

```
DPIRETURN
dpi_get_env_attr(
        dhenv         dpi_henv,
        sdint4         attr_id,
        dpointer     val,
        sdint4         buf_len,
        sdint4         *val_len
);
```

**功能**

获取环境句柄属性。

**参数**

1. dpi\_henv

输入参数，获取属性的环境句柄。

2. attr\_id

输入参数，需要获取的属性。

3. val

输出参数，指向返回指定属性当前值的缓冲区的指针。

4. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回的不是字符串，则此参数忽略。

5. val\_len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

属性值参见函数 dpi\_set\_env\_attr。

**17\. dpi\_get\_con\_attr**

**函数**

```
DPIRETURN
dpi_get_con_attr(
        dhcon         dpi_hcon,
        sdint4         attr_id,
        dpointer     val,
        sdint4         buf_len,
        sdint4         *val_len
);
```

**功能**

获取连接句柄属性。

**参数**

1)dpi\_hcon

输入参数，获取属性的连接句柄。

2. attr\_id

输入参数，需要获取的属性。

3)val

输出参数，指向返回指定属性当前值的缓冲区的指针。

4. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回的不是字符串，则此参数忽略。

5. val\_len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

属性值参见函数 dpi\_set\_con\_attr。

**18\. dpi\_get\_stmt\_attr**

**函数**

```
DPIRETURN
dpi_get_stmt_attr(
        dhstmt         dpi_hstmt,
        sdint4         attr_id,
        dpointer     val,
        sdint4         buf_len,
        sdint4         *val_len
);
```

**功能**

获取语句句柄属性。

**参数**

1. dpi\_hstmt

输入参数，获取属性的语句句柄。

2. attr\_id

输入参数，需要获取的属性。

3. val

输出参数，指向返回指定属性当前值的缓冲区的指针。

4. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回的不是字符串，则此参数忽略。

5. val\_len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

属性值参见函数 dpi\_set\_stmt\_attr

**19\. dpi\_get\_diag\_rec**

**函数**

```
DPIRETURN
dpi_get_diag_rec(
        sdint2         hndl_type,
        dhandle         hndl,
        sdint2         rec_num,
        sdint4         *err_code,
        sdbyte         *err_msg,
        sdint2         buf_sz,
        sdint2         *msg_len
);
```

**功能**

获取复合字段的诊断信息。

**参数**

1. hndl\_type 输入参数，需要获取诊断信息的句柄类型。必须为下列值之一：
- DSQL\_HANDLE\_ENV
- DSQL\_HANDLE\_DBC
- DSQL\_HANDLE\_STMT
- DSQL\_HANDLE\_DESC
- DSQL\_HANDLE\_LOB\_LOCATOR
- DSQL\_HANDLE\_OBJECT
- DSQL\_HANDLE\_OBJECTDESC
2. hndl

输入参数，需要取得诊断信息且类型为 hndl\_type 的句柄。

3. rec\_num

输入参数，诊断信息的索引号。索引起始为 1。

4. err\_code

输出参数，指向用于记录错误码的缓冲区的指针。此信息包含在 DSQL\_DIAG\_ERROR\_CODE 诊断域中。

5. err\_msg

输出参数，指向用于记录诊断消息缓冲区的指针。此信息包含在 DSQL\_DIAG\_MESSAGE\_TEXT 诊断域中。

6. buf\_sz

输入参数，err\_msg 缓冲区的长度。

7. msg\_len

输出参数，指向用于返回诊断消息总长度的缓冲区的指针。如果诊断消息长度大于等于 buf\_sz，则诊断消息被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA\_FOUND

**说明**

函数返回值含义：

- DSQL\_SUCCESS：函数成功返回诊断信息。
- DSQL\_SUCCESS\_WITH\_INFO：err\_msg 缓冲区长度不足，诊断信息被截断。
- DSQL\_ERROR：发生了下列情况之一：
	- rec\_num 小于等于 0。
		- buf\_sz 小于 0。
- DSQL\_INVALID\_HANDLE：hndl\_type 类型的 hndl 为一个无效的句柄。
- DSQL\_NO\_DATA：rec\_num 大于句柄所含有的诊断信息总数。

诊断信息用于定位错误原因，分为诊断头信息以及诊断域信息。

诊断头信息包含以下属性：

- DSQL\_DIAG\_NUMBER：诊断信息个数。
- DSQL\_DIAG\_DYNAMIC\_FUNCTION\_CODE：语句类型。
- DSQL\_DIAG\_ROW\_COUNT：语句执行影响的行数。
- DSQL\_DIAG\_PRINT\_INFO：存储过程或语句块的打印信息。
- DSQL\_DIAG\_EXPLAIN：explain 语句的结果。

诊断域信息包含以下属性：

- DSQL\_DIAG\_COLUMN\_NUMBER：出错的列号。
- DSQL\_DIAG\_ROW\_NUMBER：出错的行号。
- DSQL\_DIAG\_MESSAGE\_TEXT：错误信息。
- DSQL\_DIAG\_ERROR\_CODE：错误码。

**20\. dpi\_get\_diag\_field**

**函数**

```
DPIRETURN
dpi_get_diag_field(
        sdint2         hndl_type,
        dhandle      hndl,
        sdint2         rec_num,
        sdint2         diag_id,
        dpointer     diag_info,
        slength         buf_len,
        slength     *info_len
);
```

**功能**

获取诊断信息的某个指定诊断头或诊断域的值。

**参数**

1. hndl\_type

输入参数，需要获取诊断信息的句柄类型。必须为下列值之一：

- DSQL\_HANDLE\_ENV
- DSQL\_HANDLE\_DBC
- DSQL\_HANDLE\_STMT
- DSQL\_HANDLE\_DESC
- DSQL\_HANDLE\_LOB\_LOCATOR
- DSQL\_HANDLE\_OBJECT
- DSQL\_HANDLE\_OBJECTDESC
2. hndl

输入参数，需要取得诊断信息且类型为 hndl\_type 的句柄。

3. rec\_num

输入参数，诊断信息的索引号。索引起始为 1。如果 diag\_id 为诊断头信息，则此参数被忽略。

4. diag\_id

输入参数，指定需要获取值的诊断头或诊断域。更多信息可参考本章节 dpi\_get\_diag\_rec 函数介绍中关于诊断信息的说明。

5. diag\_info

输出参数，指向返回诊断头或诊断域信息的缓冲区的指针。数据类型依赖于 diag\_id。

6. buf\_len

输入参数，如果 diag\_info 返回的是字符串，则此参数为 diag\_info 缓冲区的长度。如果 diag\_info 返回的不是字符串，则此参数忽略。

7. info\_len

输出参数，指向返回 diag\_info 中可提供字符串的总长度的缓冲区的指针。如果 diag\_info 为 NULL，则不返回长度，如果 diag\_info 值为字符串，总长度大于等于 buf\_len，则 diag\_info 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

函数返回值含义：

- DSQL\_SUCCESS：函数成功返回诊断信息。
- DSQL\_SUCCESS\_WITH\_INFO：diag\_info 缓冲区长度不足，诊断信息被截断。
- DSQL\_ERROR：发生了下列情况之一：
	- rec\_num 小于等于 0。对于诊断头，忽略 rec\_num。
		- 所要求的诊断头或诊断域的值为字符串，而 buf\_len 小于 0。
		- diag\_id 不是一个有效的诊断头或诊断域。
		- diag\_id 为 DSQL\_DIAG\_ROW\_COUNT，DSQL\_DIAG\_DYNAMIC\_FUNCTION\_CODE，DSQL\_DIAG\_PRINT\_INFO 或者 DSQL\_DIAG\_EXPLAIN，但 hndl 不是一个语句句柄。
- DSQL\_INVALID\_HANDLE：hndl\_type 类型的 hndl 为一个无效的句柄。
- DSQL\_NO\_DATA：rec\_num 大于句柄所含有的诊断信息总数。

**21\. dpi\_login**

**函数**

```
DPIRETURN
dpi_login(
        dhcon         dpi_hcon,
        sdbyte        * svr,
        sdbyte        * user,
        sdbyte        * pwd
);
```

**功能**

与指定的数据库服务器建立连接。

**参数**

1. dpi\_hcon

输入参数，连接句柄。

2. svr

输入参数，数据库服务器所对应的地址。

3. user

输入参数，登录数据库服务器的登录名。

4. pwd

输入参数，登录数据库服务器的口令。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

若需要登录的服务器的端口不是默认端口，则需要在调用之前设置连接属性 DSQL\_ATTR\_LOGIN\_PORT，或者 svr 设置为 ip:port 形式，例如：192.168.0.143:5289。登录函数支持以服务名登录，需要配置 dm\_svc.conf 文件。

**22\. dpi\_logout**

**函数**

```
DPIRETURN
dpi_logout(
        dhcon     dpi_hcon
);
```

**功能**

断开与数据库服务器的连接。

**参数**

dpi\_hcon

输入参数，连接句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**23\. dpi\_commit**

**函数**

```
DPIRETURN
dpi_commit(
    dhcon         dpi_hcon
);
```

**功能**

提交连接上的所有活动事务。

**参数**

dpi\_hcon

输入参数，连接句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

手动提交事务，必须将连接的自动提交属性设置为非自动提交，否则无效果。默认为自动提交。

**24\. dpi\_rollback**

**函数**

```
DPIRETURN
dpi_rollback(
        dhcon         dpi_hcon
);
```

**功能**

回滚连接上的所有活动事务。

**参数**

dpi\_hcon

输入参数，连接句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

手动回滚事务，必须将连接的自动提交属性设置为非自动提交，否则无效果。默认为自动提交。

**25\. dpi\_copy\_desc**

**函数**

```
DPIRETURN
dpi_copy_desc(
        dhdesc         src_desc,
        dhdesc         target_desc
);
```

**功能**

复制一个描述符句柄的信息到另外一个描述符句柄上。

**参数说明：**

1）src\_desc

输入参数，源描述符句柄。

2）target\_desc

输入参数，目的描述符句柄。目的描述符句柄可以为 APD、ARD 或者 IPD，但不能为 IRD。

**返回值：**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

描述符句柄拷贝。只能拷贝到 APD、ARD 或者 IPD，不能拷贝到 IRD。

**26\. dpi\_set\_desc\_rec**

**函数**

```
DPIRETURN
dpi_set_desc_rec(
    dhdesc          dpi_desc,
    udint2          rec_num,
    sdint2          type,
    sdint2          sub_type,
    slength         length,
    sdint2          prec,
    sdint2          scale,
    dpointer        data_ptr,
    slength*        str_len,
    slength*        ind_ptr
);
```

**功能**

设置复合的描述符域的信息。这些信息可以影响所绑定列或者参数的数据类型和绑定的缓冲区信息。

**参数**

1）dpi\_desc

输入参数，描述符句柄。不能为 IRD 句柄。

2）rec\_num

输入参数，包含所设置域的描述符记录的索引号。此参数从 0 起始。当为 0 时，表示所设置的为书签列。此参数值必须大于等于 0。如果此参数的值大于 DSQL\_DESC\_COUNT 的值，则 DSQL\_DESC\_COUNT 的值改变为 rec\_num。

3）type

输入参数，设置描述符记录 DSQL\_DESC\_TYPE 域的值。

4）sub\_type

输入参数，对于类型为 DSQL\_DT 或者 DSQL\_INTERVAL 的记录，此参数值设置 DSQL\_DESC\_DATETIME\_INTERVAL\_CODE 域的值。

5）length

输入参数，此参数值设置描述符记录的 DSQL\_DESC\_OCTET\_LENGTH 域的值。

6）prec

输入参数，此参数值设置描述符记录的 DSQL\_DESC\_PRECISION 域的值。

7） scale

输入参数，此参数值设置描述符记录的 DSQL\_DESC\_SCALE 域的值。

8） data\_ptr

输入或输出参数，此参数值设置描述符记录的 DSQL\_DESC\_DATA\_PTR 域的值。data\_ptr 可以设置为 NULL。如果 data\_ptr 设置为 NULL，dpi\_desc 又与 ARD 关联，则这意味着清空了绑定信息。

9） str\_len

输入或输出参数，此参数值设置描述符记录的 DSQL\_DESC\_OCTET\_LENGTH\_PTR 域的值。str\_len 可以设置为 NULL。

10）ind\_ptr

输入或输出参数，此参数值设置描述符记录的 DSQL\_DESC\_INDICATOR\_PTR 域的值。ind\_ptr 可以设置为 NULL。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

具体参见 dpi\_set\_desc\_field 函数说明。

**27\. dpi\_set\_desc\_field**

**函数**

```
DPIRETURN
dpi_set_desc_field(
    dhdesc     dpi_desc,
    udint2      rec_num,
    sdint2      field,
    dpointer    val,
    sdint4      val_len
);
```

**功能**

设置描述符记录单个域的值。

**参数**

1. dpi\_desc

输入参数，描述符句柄。

2. rec\_num

输入参数，包含所设置域的描述符记录的索引号。此参数从 0 起始。当为 0 时，表示所设置的为书签列。此参数值必须大于等于 0。如果此参数的值大于 DSQL\_DESC\_COUNT 的值，则 DSQL\_DESC\_COUNT 的值改变为 rec\_num。

3. field

输入参数，所要设置的域。描述符句柄请参考 2.2.4 描述符句柄 。

4. val

输入参数，指向包含描述符信息的缓冲区，或者一个 4 字节的值。数据类型依赖于 field 的值。如果 val 为一个 4 字节的值，则是 4 字节还是 2 字节的值依赖于 field 参数。

5. val\_len

输入参数，如果 val 指向一个字符串或者二进制缓冲区，则此参数为 val 的长度。如果 val 是一个整型数据，则此参数被忽略。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

| **属性** | 字段类型 | 属性 | 字段类型 |  |  |
| --- | --- | --- | --- | --- | --- |
| DSQL\_DESC\_ALLOC\_TYPE | sdint2 | DSQL\_DESC\_LITERAL\_PREFIX | sdbyte\* |  |  |
| DSQL\_DESC\_ARRAY\_SIZE | ulength | DSQL\_DESC\_LITERAL\_SUFFIX | sdbyte\* |  |  |
| DSQL\_DESC\_ARRAY\_STATUS\_PTR | udint2\* | DSQL\_DESC\_LOCAL\_TYPE\_NAME | sdbyte\* |  |  |
| DSQL\_DESC\_BIND\_OFFSET\_PTR | slength\* | DSQL\_DESC\_NAME | sdbyte\* |  |  |
| DSQL\_DESC\_BIND\_TYPE | ulength | DSQL\_DESC\_NULLABLE | sdint2 |  |  |
| DSQL\_DESC\_COUNT | sdint2 | DSQL\_DESC\_NUM\_PREC\_RADIX | sdint4 |  |  |
| DSQL\_DESC\_ROWS\_PROCESSED\_PTR | ulength\* | DSQL\_DESC\_OCTET\_LENGTH | slength |  |  |
| DSQL\_DESC\_AUTO\_UNIQUE\_VALUE | sdint4 | DSQL\_DESC\_OCTET\_LENGTH\_PTR | slength\* |  |  |
| DSQL\_DESC\_BASE\_COLUMN\_NAME | sdbyte\* | DSQL\_DESC\_PARAMETER\_TYPE | sdint2 |  |  |
| DSQL\_DESC\_BASE\_TABLE\_NAME | sdbyte\* | DSQL\_DESC\_PRECISION | sdint2 |  |  |
| DSQL\_DESC\_CASE\_SENSITIVE | sdint4 | DSQL\_DESC\_ROWVER | sdint2 |  |  |
| DSQL\_DESC\_CATALOG\_NAME | sdbyte\* | DSQL\_DESC\_SCALE | sdint2 |  |  |
| DSQL\_DESC\_CONCISE\_TYPE | sdint2 | DSQL\_DESC\_SCHEMA\_NAME | sdbyte\* |  |  |
| DSQL\_DESC\_DATA\_PTR | void\* | DSQL\_DESC\_SEARCHABLE | sdint2 |  |  |
| DSQL\_DESC\_DATETIME\_INTERVAL\_CODE | sdint2 | DSQL\_DESC\_TABLE\_NAME | sdbyte\* |  |  |
| DSQL\_DESC\_DATETIME\_INTERVAL\_PRECISION | sdint4 | DSQL\_DESC\_TYPE | sdint2 |  |  |
| DSQL\_DESC\_DISPLAY\_SIZE | slength | DSQL\_DESC\_TYPE\_NAME | sdbyte\* |  |  |
| DSQL\_DESC\_FIXED\_PREC\_SCALE | sdint2 | DSQL\_DESC\_UNNAMED | sdint2 |  |  |
| DSQL\_DESC\_INDICATOR\_PTR | slength\* | DSQL\_DESC\_UNSIGNED | sdint2 |  |  |
| DSQL\_DESC\_LABEL | sdbyte\* | DSQL\_DESC\_UPDATABLE | sdint2 |  |  |
| DSQL\_DESC\_LENGTH | ulength |  |  |  |  |

**28\. dpi\_get\_desc\_rec**

**函数**

```
DPIRETURN
dpi_get_desc_rec(
    dhdesc      dpi_desc,
    udint2       rec_num,
    sdbyte      *name_buf,
    sdint2       name_buf_len,
    sdint2       *name_len,
    sdint2       *type,
    sdint2       *sub_type,
    slength      *length,
    sdint2       *prec,
    sdint2       *scale,
    sdint2       *nullable
);
```

**功能**

获取复合的描述符记录的域的当前设置或值。

**参数**

1. dpi\_desc

输入参数，描述符句柄。

2. rec\_num

输入参数，包含所要获取域的描述符记录的索引号。此参数从 0 起始。当为 0 时，表示所设置的为书签列。此参数值必须大于等于 0 且小于等于 DSQL\_DESC\_COUNT 的值。

3)name\_buf

输出参数，指向返回 DSQL\_DESC\_NAME 域值的缓冲区的指针。

4. name\_buf\_len

输入参数，name\_buf 缓冲区的字节长度。

5)name\_len

输出参数，指向返回可填充 name\_buf 的数据的总长度的缓冲区的指针。如果总长度大于或等于 name\_buf\_len，则 name\_buf 中的数据被截断，并以 0 结尾。

6. type

输出参数，指向返回 DSQL\_DESC\_TYPE 域值的缓冲区的指针。

7. sub\_type

输入参数，对于类型为 DSQL\_DT 或者 DSQL\_INTERVAL 的记录，此参数值设置 DSQL\_DESC\_DATETIME\_INTERVAL\_CODE 域的值。

8. length

输出参数，指向返回 DSQL\_DESC\_OCTET\_LENGTH 域值的缓冲区指针。

9. prec

输出参数，指向返回 DSQL\_DESC\_PRECISION 域值的缓冲区指针。

10. scale

输出参数，指向返回 DSQL\_DESC\_SCALE 域值的缓冲区指针。

11. nullable

输出参数，指向返回 DSQL\_DESC\_NULLABLE 域值的缓冲区指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

具体参见 dpi\_set\_desc\_field 说明。

**29\. dpi\_get\_desc\_field**

**函数**

```
DPIRETURN
dpi_get_desc_field(
    dhdesc      dpi_desc,
    udint2       rec_num,
    sdint2       field,
    dpointer     val,
    sdint4       val_len,
    sdint4       *str_len
);
```

**功能**

获取单个描述符记录的域的当前值或设置。

**参数**

1） dpi\_desc

输入参数，描述符句柄。

2） rec\_num

输入参数，包含所要获取域的描述符记录的索引号。此参数从 0 起始。当为 0 时，表示所设置的为书签列。此参数值必须大于等于 0 且小于等于 DSQL\_DESC\_COUNT 的值。

3. field

输入参数，需要获取值的描述符域。详见函数 dpi\_set\_desc\_field。

4. val

输出参数，指向返回描述信息的缓冲区的指针。数据类型依赖于 field。

5. val\_len

输入参数，如果 val 返回的是字符串类型的值，则此参数表示 val 缓冲区的字节长度。如果 val 返回的整型数据，则此参数被忽略。

6. str\_len

输出参数，指向返回 val 中可填充的最大字符串的字节长度的缓冲区指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

具体参见 dpi\_set\_desc\_field 说明。

**30\. dpi\_bind\_param**

**函数**

```
DPIRETURN
dpi_bind_param(
    dhstmt          dpi_hstmt,
    udint2           iparam,
    sdint2           param_type,
    sdint2           ctype,
    sdint2           dtype,
    ulength          precision,
    sdint2           scale,
    dpointer         buf,
    slength          buf_len,
    slength          *ind_ptr
);
```

**功能**

绑定缓冲区到 SQL 语句中的参数标记。

**参数**

1. dpi\*\*\_\*\*hstmt

输入参数，语句句柄。

2. iparam

输入参数，参数索引号。起始为 1。

3. param\_type

输入参数，参数的类型。必须是下列值之一：

● DSQL\_PARAM\_INPUT 用于绑定非调用存储过程的 SQL 语句的输入参数

● DSQL\_PARAM\_OUTPUT 用于绑定过程、函数、语句的输出参数

● DSQL\_PARAM\_INPUT\_OUTPUT 用于绑定调用存储过程的输入和输出参数

● DSQL\_PARAM\_INPUT\_OUTPUT\_STREAM 用于绑定输入输出流

● DSQL\_PARAM\_OUTPUT\_STREAM 用于绑定输出流

4. ctype

输入参数，参数的 C 数据类型。

5. dtype

输入参数，参数所对应的数据库的 D 数据类型

6. precision

输入参数，列的宽度或者参数相应域的值。

7. scale

输入参数，列的小数位数或者参数相应域的值。

8. buf

输入参数，指向存放参数数据的缓冲区的指针。

9. buf\_len

输入参数，buf 缓冲的字节长度。

10. ind\_ptr

输入参数，指向存储参数长度的缓冲区的指针。

DSQL\_NULL\_DATA：表示参数值为 NULL；

DSQL\_DATA\_AT\_EXEC，表示延迟补充数据；

如果是输出参数返回 indp 是-1，表示输出参数返回空。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

绑定信息将持续作用直到再次调用 dpi\_bind\_param 或者 dpi\_unbind\_params。

**31\. dpi\_desc\_param**

**函数**

```
DPIRETURN
dpi_desc_param(
    dhstmt           dpi_hstmt,
    udint2           iparam,
    sdint2           *sql_type,
    ulength          *prec,
    sdint2           *scale,
    sdint2           *nullable
);
```

**功能**

获取准备语句中参数的相关描述信息。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. iparam

输入参数，参数的索引号。起始为 1。

3. sql\_type

输出参数，指向返回参数数据库 D 类型的缓冲区的指针。

4. prec

输出参数，指向返回参数相应域的值的缓冲区的指针。返回数据源定义的相应参数的标记列或表达式的大小。（此外，对于绑定参数以后再执行该接口，varchar 类型的 prec 会放大至默认最大值）。

5. scale

输出参数，指向返回参数相应域的值的缓冲区的指针。返回数据源定义的相应参数的标记列或表达式的小数位数。

6. nullable

输出参数，指向返回参数是否允许为空的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

在绑定信息作用期间返回绑定参数描述信息；无绑定信息时返回服务器描述信息。

**32\. dpi\_exec**

**函数**

```
DPIRETURN
dpi_exec(
        dhstmt         dpi_hstmt
);
```

**功能**

执行一个已经准备好的语句。如果参数中包含参数，则使用参数的当前设置或值。

**参数**

dpi\_hstmt

输入参数，语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NEED\_DATA

**说明**

执行一个已准备好的语句，可以多次执行。如果多次执行一个查询语句，需要先调用 dpi\_close\_cursor 关闭当前游标，否则会报错。

**33\. dpi\_exec\_direct**

**函数**

```
DPIRETURN
dpi_exec_direct(
    dhstmt          dpi_hstmt,
    sdbyte          *sql_txt
);
```

**功能**

直接执行一条语句。如果语句中包含参数，则使用参数的当前设置或值。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. sql\_txt

输入参数，要执行的 sql 语句，以结束符结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NEED\_DATA

**说明**

单次执行某条语句。

**34\. dpi\_unbind\_params**

**函数**

```
DPIRETURN
dpi_unbind_params(
    dhstmt          dpi_hstmt
);
```

**功能**

清空语句句柄上绑定的参数信息。

**参数**

dpi\_hstmt

输入参数，语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**35\. dpi\_unbind\_columns**

**函数**

```
DPIRETURN
dpi_unbind_columns(
    dhstmt          dpi_hstmt
);
```

**功能**

清空语句句柄上绑定的列信息。

**参数**

dpi\_hstmt

输入参数，语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**36\. dpi\_param\_data**

**函数**

```
DPIRETURN
dpi_param_data(
    dhstmt          dpi_hstmt,
    dpointer         *val_ptr
);
```

**功能**

与 dpi\_put\_data 一起使用，用于协助在语句执行时提供参数的数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. val\_ptr

输出参数，指向用于返回 dpi\_bind\_param 绑定的参数地址的缓冲区指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NEED\_DATA

**说明**

当调用 dpi\_exec 或者 dpi\_exec\_direct 时，如果返回 DSQL\_NEED\_DATA，则说明需要提供某个参数的数据，此时调用 dpi\_param\_data 获取具体参数的信息，并调用 dpi\_put\_data 发送相应参数的数据。再次循环上述步骤直至 dpi\_param\_data 返回 DSQL\_SUCCESS 或 DSQL\_SUCCESS\_WITH\_INFO。

**37\. dpi\_prepare**

**函数**

```
DPIRETURN
dpi_prepare(
    dhstmt          dpi_hstmt,
    sdbyte          *sql_txt
);
```

**功能**

准备一条用于执行的 sql 语句。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. sql\_txt

输入参数，需要准备的 sql 语句，以结束符结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**38\. dpi\_put\_data**

**函数**

```
DPIRETURN
dpi_put_data(
    dhstmt          dpi_hstmt,
    dpointer         val,
    slength          val_len
);
```

**功能**

在语句执行时发送参数数据到驱动。与 dpi\_param\_data 配合使用。

**参数：**

1. dpi\_hstmt

输入参数，语句句柄。

2. val

输入参数，指向包含实际数据缓冲区的指针。缓冲区数据类型必须与 dpi\_bind\_param 时绑定的 C 类型一致。

3. val\_len

输入参数，val 中数据的实际字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

参见 dpi\_param\_data 说明。

**39\. dpi\_number\_params**

**函数**

```
DPIRETURN
dpi_number_params(
    dhstmt          dpi_hstmt,
    udint2*          param_cnt
);
```

**功能**

获取 sql 语句中包含参数的个数。

**参数：**

1. dpi\_hstmt

输入参数，语句句柄。

2. param\_cnt

输出参数，指向用于存放参数个数的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**40\. dpi\_set\_cursor\_name**

**函数**

```
DPIRETURN
dpi_set_cursor_name(
    dhstmt          dpi_hstmt,
    sdbyte          *name,
    sdint2           name_len
);
```

**功能**

设置游标的游标名。如果不设置游标名，驱动将创建默认的游标名。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. name

输入参数，指向包含游标名的缓冲区的指针。

3. name\_len

输入参数，name 的实际长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

游标名用于定位更新/删除操作。

**41\. dpi\_get\_cursor\_name**

**函数**

```
DPIRETURN
dpi_get_cursor_name(
    dhstmt          dpi_hstmt,
    sdbyte          *name,
    sdint2           buf_len,
    sdint2           *name_len
);
```

**功能**

获取指定语句句柄上的游标名。

**参数：**

1. dpi\_hstmt

输入参数，语句句柄。

2. name

输出参数，指向返回游标名的缓冲区的指针。

3. buf\_len

输入参数，name 缓冲区的字节长度。

4. name\_len

输出参数，执行存放游标名总长度的缓冲区指针。如果游标名长度大于或者等于 buf\_len，则 name 中的数据被截断并以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**42\. dpi\_close\_cursor**

**函数**

```
DPIRETURN
dpi_close_cursor(
    dhstmt          dpi_hstmt
);
```

**功能**

关闭语句句柄上已经打开的游标，并丢弃所关联的结果集。

**参数**

dpi\_hstmt

输入参数，语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**43\. dpi\_bind\_col**

**函数**

```
DPIRETURN
dpi_bind_col(
    dhstmt          dpi_hstmt,
    udint2           icol,
    sdint2           ctype,
    dpointer         val,
    slength          buf_len,
    slength          *ind
);
```

**功能**

绑定数据缓冲区到结果集中的列。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. icol

输入参数，结果集列的索引号。起始为 0。如果 icol 为 0，则绑定的为书签列。

3. ctype

输入参数，数据转换指定的 C 类型。

4. val

输出参数，指向存放实际值的缓冲区。

5. buf\_len

输入参数，存放数据缓冲区的长度。

6. ind

输出参数，指向返回实际数据长度的缓冲区。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

绑定列到输出缓冲区用于在调用 dpi\_fetch 或者 dpi\_fetch\_scroll 时检索数据。

**44\. dpi\_number\_columns**

**函数**

```
DPIRETURN
dpi_number_columns(
    dhstmt          dpi_hstmt,
    sdint2           *col_cnt
);
```

**功能**

获取结果集中列的个数。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. col\_cnt

输出参数，指向返回结果集列个数的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**45\. dpi\_desc\_column**

**函数**

```
DPIRETURN
dpi_desc_column(
    dhstmt          dpi_hstmt,
    sdint2           icol,
    sdbyte          *name,
    sdint2           buf_len,
    sdint2           *name_len,
    sdint2           *sqltype,
    ulength          *col_sz,
    sdint2           *dec_digits,
    sdint2           *nullable
);
```

**功能**

获取结果集列的描述信息。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. icol

输入参数，结果集列的索引号。起始为 0。如果为 0，则描述的是书签列信息。

3. name

输出参数，指向返回列名的缓冲区的指针。

4. buf\_len

输入参数，name 缓冲区的字节长度。

5. name\_len

输出参数，指向返回列名总长度的缓冲区的指针。如果列名长度大于或者等于 buf\_len，则 name 中数据被截断并以结束符结尾。

6. sqltype

输出参数，指向返回列的数据库 DSQL 类型的缓冲区的指针。

7. col\_sz

输出参数，指向返回列的宽度的缓冲区的指针。

8. dec\_digits

输出参数，指向返回列的小数位数的缓冲区的指针。

9. nullable

输出参数，指向返回列是否允许为空的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**46\. dpi\_col\_attr**

**函数**

```
DPIRETURN
dpi_col_attr(
    dhstmt          dpi_hstmt,
    udint2           icol,
    udint2           fld_id,
    dpointer         chr_attr,
    sdint2           buf_len,
    sdint2           *chr_attr_len,
    slength          *num_attr
);
```

**功能**

获取结果集中列的描述信息。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. icol

输入参数，结果集列的索引号。起始索引为 0。当参数被指定为 0 时，除了 DSQL\_DESC\_TYPE 和 DSQL\_DESC\_OCTET\_LENGTH 外，其他域的值为无效值。

3. fld\_id

输入参数，需要获取值的描述域。

4. chr\_attr

输出参数，指向返回 fld\_id 域的值，此参数仅返回字符串，如果 fld\_id 对应的值不是字符串，则此参数不会被使用。

5. buf\_len

输入参数，chr\_attr 缓冲区的字节长度。

6. chr\_attr\_len

输出参数，指向返回 fld\_id 域可返回字符串的最大长度的缓冲区的指针。如果返回值长度大于或者等于 buf\_len，则 chr\_attr 中数据被截断并以 0 结尾。

7. num\_attr

输出参数，指向返回整型数据的缓冲区的指针。如果 fld\_id 所返回的值为整型数据，则此参数有意义，否则此参数不会被使用。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

详细参数含义参见 2.2.4 描述符句柄 。

**47\. dpi\_bulk\_operation**

**函数**

```
DPIRETURN
dpi_bulk_operation(
    dhstmt          dpi_hstmt,
    udint2           op
);
```

**功能**

执行批量插入和批量的书签操作。包括通过书签更新、删除、获取数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. op

输入参数，操作方式。必须是下列之一：

- DSQL\_ADD
- DSQL\_UPDATE\_BY\_BOOKMARK
- DSQL\_DELETE\_BY\_BOOKMARK
- DSQL\_FETCH\_BY\_BOOKMARK

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NEED\_DATA

**说明**

函数执行后游标位置未知，必须调用 dpi\_fetch\_scroll 重新定位游标。

**48\. dpi\_fetch**

**函数**

```
DPIRETURN
dpi_fetch(
    dhstmt          dpi_hstmt,
    ulength         *row_num
);
```

**功能**

获取下一个行集数据和返回所有绑定列的数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. row\_num

输出参数，指向返回取得行数的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

无。

**49\. dpi\_fetch\_scroll**

**函数**

```
DPIRETURN
dpi_fetch_scroll(
    dhstmt          dpi_hstmt,
    sdint2           orient,
    slength          offset,
    ulength         *row_num
);
```

**功能**

获取指定行集数据和返回所有绑定列的数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. orient

输入参数，获取方式。必须是下列之一：

- DSQL\_FETCH\_NEXT
- DSQL\_FETCH\_PRIOR
- DSQL\_FETCH\_FIRST
- DSQL\_FETCH\_LAST
- DSQL\_FETCH\_ABSOLUTE
- DSQL\_FETCH\_RELATIVE
- DSQL\_FETCH\_BOOKMARK
3. offset

输入参数，获取行的偏移。此参数的意义依赖于 orient，对于 orient 为 DSQL\_FETCH\_RELATIVE 时有效，意义为相对于当前游标位置的偏移量。

4. row\_num

输出参数，指向返回取得行数的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

无。

**50\. dpi\_get\_data**

**函数**

```
DPIRETURN
dpi_get_data(
    dhstmt          dpi_hstmt,
    udint2           icol,
    sdint2           ctype,
    dpointer         val,
    slength          buf_len,
    slength          *val_len
);
```

**功能**

获取结果集中单个列的数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. icol

输入参数，结果集中列的索引号。结果集索引起始为 1。如果 icol 被设置为 0，则获取的是书签列的值，且只有当书签选项启用时才有效。

3. ctype

输入参数，所要获取数据的目标 C 类型。

4. val

输出参数，指向存放数据的缓冲区的指针。

5. buf\_len

输入参数，val 缓冲区的字节长度。

6. val\_len

输出参数，指向存放数据长度的缓冲区的指针。如果此参数为 NULL，则不返回长度，如果数据长度为 NULL，则返回错误。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明** ：

dpi\_get\_data 可以分批获取字符类型或者二进制类型数据。

**51\. dpi\_more\_results**

**函数**

```
DPIRETURN
dpi_more_results(
    dhstmt          dpi_hstmt
);
```

**功能**

确定句柄上是否包含有多个结果集。如果有，则处理这些结果集。

**参数**

dpi\_hstmt

输入参数，语句句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NO\_DATA

**说明**

无。

**52\. dpi\_set\_pos**

**函数**

```
DPIRETURN
dpi_set_pos(
    dhstmt         dpi_hstmt,
    ulength         row_num,
    udint2          op,
    udint2          lock_type
);
```

**功能**

定位，更新结果集的数据。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. row\_num

输入参数，行集中行的位置。如果 row\_num 为 0，则操作作用于行集中的每一行。

3. op

输入参数，操作方式。必须是下列之一：

- DSQL\_POSITION
- DSQL\_REFRESH
- DSQL\_UPDATE
- DSQL\_DELETE
- DSQL\_ADD
4. lock\_type

输入参数，指定在 op 操作之后行的封锁方式。必须是下列之一：

- DSQL\_LOCK\_NO\_CHANGE
- DSQL\_LOCK\_EXCLUSIVE
- DSQL\_LOCK\_UNLOCK

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

DSQL\_NEED\_DATA

**说明**

无。

**53\. dpi\_row\_count**

**函数**

```
DPIRETURN
dpi_row_count(
    dhstmt          dpi_hstmt,
    sdint8           *row_num
);
```

**功能**

返回 sql 语句所影响行的总数。

**参数**

1. dpi\_hstmt

输入参数，语句句柄。

2. row\_num

输出参数，指向返回影响行数的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**54\. dpi\_lob\_get\_length**

**函数**

```
DPIRETURN
dpi_lob_get_length(
    dhloblctr        dpi_loblctr,
    slength         *len
);
```

**功能**

获取 lob 句柄对应大对象的实际长度。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. len

输出参数，指向返回大字段长度的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

CLOB 为字符长度，BLOB 为字节长度。

**55\. dpi\_lob\_read**

**函数**

```
DPIRETURN
dpi_lob_read(
    dhloblctr       dpi_loblctr,
    ulength         start_pos,
    sdint2          ctype,
    slength        data_to_read,
    dpointer        val_buf,
    slength         buf_len,
    slength         *data_get
);
```

**功能**

读取 lob 句柄所对应大字段的实际数据。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. start\_pos

输入参数，起始的偏移。起始为 1。CLOB 类型此参数表示字符偏移，BLOB 类型此参数表示字节偏移。

3. ctype

输入参数，所获取数据的目标 C 类型。

4. data\_to\_read

输入参数，CLOB 类型表示要读取的字符数，BLOB 类型表示要读取的字节数，缺省值为 0。

5. val\_buf

输出参数，指向存放获取数据的缓冲区的指针。

6. buf\_len

输入参数，val\_buf 缓冲区的字节长度。

7. data\_get

输出参数，指向返回已获取数据的实际长度。CLOB 类型表示字符长度，BLOB 类型表示字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**56\. dpi\_lob\_read2**

**函数**

```
DPIRETURN
dpi_lob_read2(
    dhloblctr       dpi_loblctr,
    Udint8         start_pos,
    sdint2          ctype,
    slength           data_to_read,
    dpointer        val_buf,
    slength         buf_len,
    slength         *data_get
);
```

**功能**

读取 lob 句柄所对应大字段的实际数据。与 dpi\_lob\_read 函数的区别在于 start\_pos 参数的数据类型不同。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. start\_pos

输入参数，起始的偏移。起始为 1。CLOB 类型此参数表示字符偏移，BLOB 类型此参数表示字节偏移。

3. ctype

输入参数，所获取数据的目标 C 类型。

4. data\_to\_read

输入参数，CLOB 类型表示要读取的字符数，BLOB 类型表示要读取的字节数，缺省值为 0。

5. val\_buf

输出参数，指向存放获取数据的缓冲区的指针。

6. buf\_len

输入参数，val\_buf 缓冲区的字节长度。

7. data\_get

输出参数，指向返回已获取数据的实际长度。CLOB 类型表示字符长度，BLOB 类型表示字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**57\. dpi\_lob\_read3**

**函数**

```
DPIRETURN
dpi_lob_read3(
    dhloblctr    dpi_loblctr,
    udint8        start_pos,
    sdint2        ctype,
    slength        data_to_read,
    dpointer    val_buf,
    slength        buf_len,
    slength        *data_get,
    slength        *data_get_bytes
);
```

**功能**

读取 lob 句柄所对应大字段的实际数据，带有数据的字节输出。

**参数**

1. dpi\_loblctr

输入参数，大字段操作符。

2. start\_pos

输入参数，起始的偏移。起始为 1。CLOB 类型此参数表示字符偏移，BLOB 类型此参数表示字节偏移。

3. ctype

输入参数，缓冲区的 C 类型。

4. data\_to\_read

输入参数，读取的数据总数，CLOB 类型表示要读取的字符数，BLOB 类型表示要读取的字节数，缺省值为 0，0 表示填满缓冲区。

5. val\_buf

输出参数，指向存放获取数据的缓冲区的指针。

6. buf\_len

输入参数，val\_buf 缓冲区的字节长度。

7. data\_get

输出参数，指向返回已获取数据的实际长度。CLOB 类型表示字符长度，BLOB 类型表示字节长度。

8. data\_get\_bytes

输出参数，指向缓冲区中的数据字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**58\. dpi\_lob\_write**

**函数**

```
DPIRETURN
dpi_lob_write(
    dhloblctr             dpi_loblctr,
    ulength              start_pos,
    sdint2               ctype,
    dpointer             val,
    ulength              bytes_to_write,
    ulength              *data_writed
);
```

**功能**

更新 lob 句柄所对应的大字段的数据。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. start\_pos

输入参数，起始的偏移。起始为 1。CLOB 类型此参数表示字符偏移，BLOB 类型此参数表示字节偏移。

3. ctype

输入参数，更新数据的 C 数据类型。

4. val

输入参数，指向存放更新数据缓冲区的指针。

5. bytes\_to\_write

输入参数，需要更新数据的字节长度。

6. data\_writed

输出参数，指向返回已更新数据的长度。对于 CLOB 类型此参数表示字符长度，BLOB 类型则此参数表示字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**59\. dpi\_lob\_write2**

**函数**

```
DPIRETURN
dpi_lob_write2(
    dhloblctr             dpi_loblctr,
    Udint8              start_pos,
    sdint2               ctype,
    dpointer             val,
    ulength              bytes_to_write,
    ulength              *data_writed
);
```

**功能**

更新 lob 句柄所对应的大字段的数据。与 dpi\_lob\_write 函数的区别在于 start\_pos 参数的数据类型不同。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. start\_pos

输入参数，起始的偏移。起始为 1。CLOB 类型此参数表示字符偏移，BLOB 类型此参数表示字节偏移。

3. ctype

输入参数，更新数据的 C 数据类型。

4. val

输入参数，指向存放更新数据缓冲区的指针。

5. bytes\_to\_write

输入参数，需要更新数据的字节长度。

6. data\_writed

输出参数，指向返回已更新数据的长度。对于 CLOB 类型此参数表示字符长度，BLOB 类型则此参数表示字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**60\. dpi\_lob\_truncate**

**函数**

```
DPIRETURN
dpi_lob_truncate(
    dhloblctr            dpi_loblctr,
    ulength             len,
    ulength             *data_len
);
```

**功能**

截断 lob 句柄所对应的大字段到指定的长度。

**参数**

1. dpi\_loblctr

输入参数，lob 句柄。

2. len

输入参数，大字段被截断后的长度。对于 CLOB 类型此参数表示字符长度，BLOB 类型则此参数表示字节长度。

3. data\_len

输出参数，大字段被截断后的实际长度。对于 CLOB 类型此参数表示字符长度，BLOB 类型则此参数表示字节长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**61\. dpi\_alloc\_obj**

**函数**

```
DPIRETURN
dpi_alloc_obj(
    dhcon            dpi_con,
    dhobj*            object
);
```

**功能**

分配复合类型句柄。

**参数**

1. dpi\_con

输入参数，通过此连接句柄分配新的语句句柄，新句柄运行环境从属此句柄。

2. object

输出参数， 一个存放新分配复合对象句柄数据结构的缓冲区地址。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**62\. dpi\_free\_obj**

**函数**

```
DPIRETURN
dpi_free_obj(
        dhobj     object
);
```

**功能**

释放复合对象句柄。

**参数**

1. object

输入参数，复合对象句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**63\. dpi\_desc\_obj**

**函数**

```
DPIRETURN
dpi_desc_obj(  
dhcon           dpi_con,
sdbyte*         schema,
sdbyte*         compobj_name,
dhobjdesc*      obj_desc
);
```

**功能**

获取复合对象的描述信息。

**参数**

1. dpi\_con

输入参数，连接句柄。

2. schema

输入参数，复合对象所属模式名。

3. compobj\_name

输入参数，复合对象名。

4. obj\_desc

输出参数，复合对象描述符句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**64\. dpi\_desc\_obj2**

**函数**

```
DPIRETURN
dpi_desc_obj(  
dhcon           dpi_con,
sdbyte*         schema,
sdbyte*         pkg_name,
sdbyte*         compobj_name,
dhobjdesc*      obj_desc
);
```

**功能**

获取复合对象的描述信息。该函数功能覆盖了 dpi\_desc\_obj()的功能，描述的复合对象包括包内的复合对象和不属于包内的复合对象，若对象不属于包内，则 pkg\_name 参数置为 NULL 即可。

**参数**

1. dpi\_con

输入参数，连接句柄。

2. schema

输入参数，复合对象所属模式名。

3. pkg\_name

输入参数，复合对象所在的包名，可以为 NULL。

4. compobj\_name

输入参数，复合对象名。

5. obj\_desc

输出参数，复合对象描述符句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**65\. dpi\_free\_obj\_desc**

**函数**

```
DPIRETURN
dpi_free_obj_desc(  
dhobjdesc       obj_desc
);
```

**功能**

释放复合对象描述符句柄。

**参数**

obj\_desc

输入参数，复合对象描述符句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**66\. dpi\_get\_obj\_attr**

**函数**

```
DPIRETURN
dpi_get_obj_attr(  
    dhobj           object, 
    udint4          nth,
    udint2          attr_id,
    dpointer        buf,
    udint4          buf_len,
    slength*        len
);
```

**功能**

获取复合对象的属性值。

**参数**

1. object

输入参数，获取属性的复合对象句柄。

2. nth

保留输入参数，暂不起作用。

3. attr\_id

输入参数，需要获取的属性。

4. buf

输出参数，指向返回指定属性当前值的缓冲区的指针。

5. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回的不是字符串，则此参数忽略。

6. len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

| **属性** | **字段类型** |
| --- | --- |
| DSQL\_ATTR\_OBJ\_VAL\_COUNT | udint4 |

**67\. dpi\_get\_obj\_desc\_attr**

**函数**

```
DPIRETURN
dpi_get_obj_desc_attr(
    dhobjdesc       obj_desc,
    udint4          nth,
    udint2          attr_id,
    dpointer        buf,
    udint4          buf_len,
    slength*        len
);
```

**功能**

获取复合对象描述符上的属性值。

**参数**

1. obj\_desc

输入参数，复合对象描述符句柄。

2. nth

复合对象要获取域下标

3. attr\_id

输入参数，需要获取的属性。

4. buf

输出参数，指向返回指定属性当前值的缓冲区的指针。

5. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回  
的不是字符串，则此参数忽略。

6. len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

| **属性** | **字段类型** |
| --- | --- |
| DSQL\_ATTR\_OBJ\_TYPE | sdint2 |
| DSQL\_ATTR\_OBJ\_PREC | sdint2 |
| DSQL\_ATTR\_OBJ\_SCALE | sdint2 |
| DSQL\_ATTR\_OBJ\_NAME | sdbyte\* |
| DSQL\_ATTR\_OBJ\_DESC | dhobjdesc |
| DSQL\_ATTR\_OBJ\_FIELD\_COUNT | udint4 |
| DSQL\_ATTR\_OBJ\_SCHAME | sdbyte\* |

**68\. dpi\_bind\_obj\_desc**

**函数**

```
DPIRETURN
dpi_bind_obj_desc(
    dhobj object,
    dhobjdesc desc
);
```

**功能**

绑定复合对象描述符句柄。

**参数**

1. object

输入参数，复合对象句柄。

2. desc

输入参数，复合对象描述符句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**69.dpi\_unbind\_obj\_desc**

**函数**

```
DPIRETURN
dpi_unbind_obj_desc(
    dhobj           object
);
```

**功能**

解除复合对象描述符句柄绑定。

**参数**

object

输入参数，复合对象句柄。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**70\. dpi\_set\_obj\_val**

**函数**

```
DPIRETURN
dpi_set_obj_val(
    dhobj           object,
    udint4          nth,
    udint2          ctype,
    dpointer        val,
    slength         val_len
);
```

**功能**

复合对象绑定值。

**参数**

1. object

输入参数，复合对象句柄。

2. nth

输入参数，绑定域下标。

3. ctype

输入参数，绑定的 c 数据类型。

4. val

输入参数，指向存放参数数据的缓冲区的指针。

5. val\_len

输入参数，指向存储参数长度的缓冲区的指针。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**71\. dpi\_get\_obj\_val**

**函数**

```
DPIRETURN
dpi_get_obj_val(
    dhobj           object,
    udint4          nth,
    udint2          ctype,
    dpointer        val,
    udint4          buf_len,
    slength*        val_len
);
```

**功能**

获取复合对象各个域的值。

**参数**

1. object

输入参数，复合对象句柄。

2. nth

复合对象域下标。

3. cytpe

输入参数，数据转换指定的 C 类型。

4. val

输出参数，指向存放实际值的缓冲区。

5. buf\_len

输入参数，如果 val 返回的是字符串，则此参数为 val 缓冲区的长度。如果 val 返回的不是字符串，则此参数忽略。

6. val\_len

输出参数，指向返回 val 中可提供字符串的总长度的缓冲区的指针。如果 val 为 NULL，则不返回长度，如果属性值为字符串，总长度大于等于 buf\_len，则 val 值被截断且以 0 结尾。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**72\. dpi\_build\_rowid**

**函数**

```
DPIRETURN   
dpi_build_rowid(
  dhcon      dpi_con,  
  sdint4     epno,  
  sdint8     partno,  
  udint8     real_rowid,  
  sdbyte*     rowid_buf,   
  udint4     rowid_buf_len,   
  udint4*     rowid_len   
);
```

**功能**

生成一个流式的 ROWID 数据。

**参数**

1. dpi\_con

输入参数，连接句柄。

2. epno

输入参数，站点号。

3. partno

输入参数，分区号。

4. real\_rowid

输入参数，实际的行号。

5. rowid\_buf

输出参数，输出缓冲区。

6. rowid\_buf\_len

输入参数，缓冲区大小。

7. rowid\_len

输出参数，实际数据长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**73\. dpi\_rowid\_to\_char**

**函数**

```
DPIRETURN  
dpi_rowid_to_char(
  dhcon      dpi_con,  
  sdbyte*     rowid,   
  udint4     rowid_len,   
  sdbyte*     dest_buf,  
  udint4     dest_buf_len,  
  udint4*     dest_len   
);
```

**功能**

将一个流式的 ROWID 转换为 base64 格式的字符串 ROWID。

**参数**

1. dpi\_con

输入参数，连接句柄。

2. rowid

输入参数，rowid 数据。

3. rowid\_len

输入参数，rowid 数据长度。

4. dest\_buf

输出参数，输出缓冲区。

5. dest\_buf\_len

输入参数，缓冲区大小。

6. dest\_len

输出参数，实际数据长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**74\. dpi\_char\_to\_rowid**

**函数**

```
DPIRETURN   
dpi_char_to_rowid (
  dhcon      dpi_con,  
  sdbyte*     rowid_str,  
  udint4     rowid_len,   
  sdbyte*     dest_buf,   
  udint4     dest_buf_len,   
  udint4*     dest_len  
);
```

**功能**

将一个 base64 格式字符串的 ROWID 转换为流式的 ROWID。

**参数**

1. dpi\_con

输入参数，连接句柄。

2. rowid\_str

输入参数，rowid 数据。

3. rowid\_len

输入参数，rowid 数据长度。

4. dest\_buf

输出参数，输出缓冲区。

5. dest\_buf\_len

输入参数，缓冲区大小。

6. dest\_len

输出参数，实际数据长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**75\. dpi\_bfile\_construct**

**函数**

```
DPIRETURN
dpi_bfile_construct(
    dhbfile             bfile_lctr,
    udbyte*             dir_name,
    udint4              dir_name_len,
    udbyte*             file_name,
    udint4              file_name_len
);
```

**功能**

构造 bfile。

**参数**

1. bfile\_lctr

输入参数，bfile 文件句柄。

2. dir\_name

输入参数，路径名

3. dir\_name\_len

输入参数，路径名长度。

4. file\_name

输入参数，文件名。

5. file\_name\_len

输入参数，文件名长度。

**返回值**

DSQL\_SUCCESS

DSQL\_SUCCESS\_WITH\_INFO

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

**76\. dpi\_bfile\_get\_name**

**函数**

```
DPIRETURN
dpi_bfile_get_name(
    dhbfile             bfile_lctr,
    udbyte*             dir_buf,
    udint4              dir_buf_len,
    udint4*             dir_len,
    udbyte*             file_buf,
    udint4              file_buf_len,
    udint4*             file_len
);
```

**功能**

获取 bfile 的名字。

**参数**

1. bfile\_lctr

输入参数，bfile 文件句柄。

2. dir\_buf

输出参数，路径名缓存区

3. dir\_buf\_len

输入参数，路径名缓存区长度。

4. dir\_len

输出参数，路径名长度

5. file\_buf

输出参数，文件名缓存区

6. file\_buf\_len

输入参数，文件名缓存区长度。

7. file\_len

输出参数，文件名长度。

**返回值**

DSQL\_SUCCESS

```
DSQL_SUCCESS_WITH_INFO
```

DSQL\_ERROR

DSQL\_INVALID\_HANDLE

**说明**

无。

### 2.3.2 UTF-16 编码

使用 UTF-16 编码下的 DPI 函数编程时需要用到 DM 的头文件 DPIucode.h。

UTF-16 编码支持以下 DPI 函数：

- dpi\_set\_con\_attrW：UTF-16 编码下设置连接句柄属性，用法同常规编码下的 dpi\_set\_con\_attr 函数。
- dpi\_get\_con\_attrW：UTF-16 编码下获取连接句柄属性，用法同常规编码下的 dpi\_get\_con\_attr 函数。
- dpi\_get\_diag\_recW：UTF-16 编码下获取复合字段的诊断信息，用法同常规编码下的 dpi\_get\_diag\_rec 函数。
- dpi\_get\_diag\_fieldW：UTF-16 编码下获取诊断信息的某个指定诊断头或诊断域的值，用法同常规编码下的 dpi\_get\_diag\_field 函数。
- dpi\_set\_desc\_fieldW：UTF-16 编码下设置描述符记录单个域的值，用法同常规编码下的 dpi\_set\_desc\_field 函数。
- dpi\_get\_desc\_fieldW：UTF-16 编码下获取单个描述符记录的域的当前值或设置，用法同常规编码下的 dpi\_get\_desc\_field 函数。
- dpi\_get\_desc\_recW：UTF-16 编码下获取复合的描述符记录的域的当前设置或值，用法同常规编码下的 dpi\_get\_desc\_rec 函数。
- dpi\_loginW：UTF-16 编码下与指定的数据库服务器建立连接，用法同常规编码下的 dpi\_login 函数。
- dpi\_exec\_directW：UTF-16 编码下直接执行一条语句。如果语句中包含参数，则使用参数的当前设置或值。用法同常规编码下的 dpi\_exec\_direct 函数。
- dpi\_prepareW：UTF-16 编码下准备一条用于执行的 sql 语句，用法同常规编码下的 dpi\_prepare 函数。
- dpi\_get\_dataW：UTF-16 编码下获取结果集中单个列的数据，用法同常规编码下的 dpi\_get\_data 函数。
- dpi\_set\_cursor\_nameW：UTF-16 编码下设置游标的游标名。如果不设置游标名，驱动将创建默认的游标名。用法同常规编码下的 dpi\_set\_cursor\_name 函数。
- dpi\_get\_cursor\_nameW：UTF-16 编码下获取指定语句句柄上的游标名，用法同常规编码下的 dpi\_get\_cursor\_name 函数。
- dpi\_desc\_columnW：UTF-16 编码下获取结果集列的描述信息，用法同常规编码下的 dpi\_desc\_column 函数。
- dpi\_col\_attrW：UTF-16 编码下获取结果集中列的描述信息，用法同常规编码下的 dpi\_col\_attr 函数。
- dpi\_lob\_readW：UTF-16 编码下读取 lob 句柄所对应大字段的实际数据，用法同常规编码下的 dpi\_lob\_read 函数。
- dpi\_lob\_readW2：UTF-16 编码下读取 lob 句柄所对应大字段的实际数据，用法同常规编码下的 dpi\_lob\_read2 函数。
- dpi\_lob\_readW3：UTF-16 编码下读取 lob 句柄所对应大字段的实际数据，用法同常规编码下的 dpi\_lob\_read3 函数。
- dpi\_lob\_writeW：UTF-16 编码下更新 lob 句柄所对应的大字段的数据，用法同常规编码下的 dpi\_lob\_write 函数。
- dpi\_lob\_writeW2：UTF-16 编码下更新 lob 句柄所对应的大字段的数据，用法同常规编码下的 dpi\_lob\_write2 函数。
- dpi\_get\_obj\_desc\_attrW：UTF-16 编码下获取复合对象描述符上的属性值，用法同常规编码下的 dpi\_get\_obj\_desc\_attr 函数。
- dpi\_bfile\_constructW：UTF-16 编码下构造 bfile，用法同常规编码下的 dpi\_bfile\_construct 函数。
- dpi\_bfile\_get\_nameW：UTF-16 编码下获取 bfile 的名字，用法同常规编码下的 dpi\_bfile\_get\_name 函数。

## 2.4 编程参考

### 2.4.1 编程步骤

应用程序使用 DPI 访问数据库，可以按照以下几个基本步骤进行：

1. 调用函数 dpi\_alloc\_env 申请环境句柄。（通过 dpi\_set\_env\_attr 和 dpi\_get\_env\_attr 可以设置和获取环境句柄属性）。
2. 调用函数 dpi\_alloc\_con 申请连接句柄（通过 dpi\_set\_con\_attr 和 dpi\_get\_con\_attr 可以设置和获取连接句柄属性）。
3. 调用函数 dpi\_login 连接数据库服务器。
4. 调用函数 dpi\_alloc\_stmt 申请语句句柄（通过 dpi\_set\_stmt\_attr 和 dpi\_get\_stmt\_attr 可以设置和获取语句句柄属性）。
5. 调用函数 dpi\_exec\_direct 直接执行 SQL 语句（也可以通过 dpi\_prepare 准备语句，然后通过 dpi\_bind\_param 绑定参数，再通过 dpi\_exec 来执行带参数的 sql 语句；还可以通过 dpi\_fetch 或 dpi\_fetch\_scroll 来获取查询的结果集数据）。
6. 调用函数 dpi\_free\_stmt 释放申请的语句句柄。
7. 调用函数 dpi\_logout 断开应用程序与数据源之间的连接。
8. 调用函数 dpi\_free\_con 释放申请的连接句柄。
9. 调用函数 dpi\_free\_env 释放申请的环境句柄。

程序在编译的过程中需要用到 DM 的头文件 DPI.h、DPIext.h、DPItypes.h，在链接阶段需要用到 dmdpi.lib 这个库文件，在执行阶段需要用到动态库 dmdpi.dll 以及 dmcalc.dll、dmcomm.dll、dmcyt.dll、dmclientlex.dll、dmcvt.dll、dmelog.dll、dmmem.dll、dmmsg.dll、dmos.dll、dmutl.dll。这几个动态库在安装 DM 时，已经被放到安装目录下。

如果是在 UTF-16 编码环境下编程，则还需要用到 DM 的头文件 DPIucode.h。本章节示例均为常规编码环境下的编程示例。

另外，当使用 64 位的 DPI 接口时，需要添加 DM64 的宏，即 Linux 平台下编译程序时添加“-DDM64”编译参数，Windows 平台下则在相应工程的预处理器定义中添加“DM64”。

### 2.4.2 普通数据插入与查询方式的操作

下面通过一个简单的 Windows 环境下的示例来说明 DPI 普通数据插入与查询。

创建一个表，通过参数绑定以及数组绑定的方式插入数据，通过 fetch 和 fetch scroll 获取结果集并显示，以及通过将结果集输出到数组中。

```
#include "DPI.h"
#include "DPIext.h"
#include "DPItypes.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
/******************************************************
Notes:
定义相应常量
*******************************************************/
#define ROWS    10                //数组绑定一次插入和读取的行数
#define CHARS    80*1024            //一次读取和写入的字节数800K
#define FLEN    500                //文件名长度(带地址路径)
#define DM_SVR  "127.0.0.1:8000"
#define DM_USER "SYSDBA"
#define DM_PWD  "Hust4400_DBA"
//函数检查及错误信息显示
#define DPIRETURN_CHECK(rt, hndl_type, hndl) if(!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA){dpi_err_msg_print(hndl_type, hndl);return rt;}
#define FUN_CHECK(rt) if(!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA){goto END;}
/******************************************************
Notes:
定义常用句柄和变量
*******************************************************/
dhenv        henv;        /* 环境句柄 */
dhcon        hcon;        /* 连接句柄 */
dhstmt        hstmt;        /* 语句句柄 */
dhdesc      hdesc;      /* 描述符句柄 */
dhloblctr    hloblctr;    /* lob类型控制句柄 */
DPIRETURN   rt;         /* 函数返回值 */
/******************************************************
Notes:
    错误信息获取打印
Param:
    hndl_type:    句柄类型
    hndl:        句柄
Return:
    无
*******************************************************/
void
dpi_err_msg_print(sdint2 hndl_type, dhandle hndl)
{
    sdint4 err_code;
    sdint2 msg_len;
    sdbyte err_msg[SDBYTE_MAX];
    //获取错误信息字段
/*    dpi_get_diag_field(hndl_type, hndl, 1, DSQL_DIAG_MESSAGE_TEXT, err_msg, sizeof(err_msg), NULL);
    printf("err_msg = %s\n", err_msg);*/
    //获取错误信息集合
    dpi_get_diag_rec(hndl_type, hndl, 1, &err_code, err_msg, sizeof(err_msg), &msg_len);
    printf("err_msg = %s, err_code = %d\n", err_msg, err_code);
}
/******************************************************
Notes:
    连接数据库
Param:
    server: 服务器IP
    uid:    数据库登录账号
    pwd:    数据库登录密码
Return:
    DSQL_SUCCESS 执行成功
    DSQL_ERROR   执行失败
*******************************************************/
DPIRETURN 
dm_dpi_connect(sdbyte* server,  sdbyte* uid, sdbyte* pwd)
{
    //申请环境句柄 
    rt = dpi_alloc_env(&henv);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_ENV, henv);  
    //申请连接句柄
    rt = dpi_alloc_con(henv, &hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);  
    //连接数据库服务器
    rt = dpi_login(hcon, server, uid, pwd);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);  
    return DSQL_SUCCESS;
}
/************************************************
    断开数据库连接
************************************************/
DPIRETURN
dm_dpi_disconnect()
{
    //断开连接
    rt = dpi_logout(hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);  
    //释放连接句柄和环境句柄
    rt = dpi_free_con(hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    rt = dpi_free_env(henv);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_ENV, henv);  
    return DSQL_SUCCESS;
}
/************************************************
    初始化表
************************************************/
DPIRETURN 
dm_init_table()
{
    //申请语句句柄
    rt = dpi_alloc_stmt(hcon, &hstmt);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    //执行sql
    dpi_exec_direct(hstmt, "drop table dpi_demo");
    rt = dpi_exec_direct(hstmt, "create table dpi_demo(c1 int, c2 char(20), c3 varchar(50), c4 numeric(7,3), c5 timestamp(5), c6 clob, c7 blob)");
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
    //释放语句句柄
    rt = dpi_free_stmt(hstmt);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
  
    printf("dm init table success\n");
    return DSQL_SUCCESS;
}
/************************************************
    通过参数绑定的方式执行sql语句
************************************************/
DPIRETURN
dm_insert_with_bind_param()
{
     sdint4          c1 = 0;         // 与字段匹配的变量  
     sdbyte           c2[10]; 
     sdbyte           c3[10]; 
     ddouble           c4; 
     dpi_timestamp_t     c5; 
     sdbyte           c6[18]; 
     sdbyte           c7[18];
     slength      c1_ind_ptr;
     slength      c2_ind_ptr;       //缓冲区长度  
     slength      c3_ind_ptr; 
    slength      c4_ind_ptr=0;
    slength      c5_ind_ptr=0;
     slength      c6_ind_ptr; 
     slength      c7_ind_ptr;  
     //分配语句句柄 
     rt = dpi_alloc_stmt(hcon, &hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
     //准备sql 
  rt = dpi_prepare(hstmt, "insert into dpi_demo(c1,c2,c3,c4,c5,c6,c7) values(?,?,?,?,?,?,?)"); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     //字段变量赋值  
    c1 = 201410;
     memcpy(c2, "abcde", 5); 
     memcpy(c3, "abcdefghi", 9); 
     c4      = 0.009; 
     c5.year    = 2011; 
     c5.month  = 3; 
     c5.day    = 1; 
     c5.hour    = 11; 
     c5.minute  = 45; 
     c5.second  = 50; 
     c5.fraction  = 900000000; 
     memcpy(c6, "adfadsfetre2345ert", 18); 
     memcpy(c7, "1234567890abcdef12", 18);  
     c1_ind_ptr =sizeof(c1);
     c2_ind_ptr = 5;       //获取缓冲区长度  
     c3_ind_ptr = 9; 
     c4_ind_ptr =sizeof(c4);
     c5_ind_ptr =sizeof(c5);
     c6_ind_ptr = 18; 
     c7_ind_ptr = 18;  
      //绑定参数  
     rt = dpi_bind_param(hstmt, 1, DSQL_PARAM_INPUT, DSQL_C_SLONG, DSQL_INT, sizeof(c1), 0, &c1, sizeof(c1), &c1_ind_ptr);
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 2, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CHAR, sizeof(c2), 0, c2, sizeof(c2), &c2_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 3, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_VARCHAR, sizeof(c3), 0, c3, sizeof(c3), &c3_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 4, DSQL_PARAM_INPUT, DSQL_C_DOUBLE, DSQL_DOUBLE, sizeof(c4), 0, &c4, sizeof(c4), &c4_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 5, DSQL_PARAM_INPUT, DSQL_C_TIMESTAMP, DSQL_TIMESTAMP, sizeof(c5), 0, &c5, sizeof(c5), &c5_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 6, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CLOB, sizeof(c6), 0, c6, sizeof(c6), &c6_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 7, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_BLOB, sizeof(c7), 0, c7, sizeof(c7), &c7_ind_ptr); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     // 执行Dsql
     rt = dpi_exec(hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     // 释放语句句柄 
     rt = dpi_free_stmt(hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     printf("dm insert with bind param success\n"); 
     return DSQL_SUCCESS; 
}
/************************************************
    通过参数绑定数组的方式执行sql语句
************************************************/
DPIRETURN
dm_insert_with_bind_array()
{
     sdint4          c1[ROWS];           // 定义字段相应的变量  
     sdbyte           c2[ROWS][10];   
     sdbyte           c3[ROWS][10];   
     ddouble           c4[ROWS]; 
     dpi_timestamp_t     c5[ROWS]; 
     sdbyte           c6[ROWS][18]; 
     sdbyte           c7[ROWS][18]; 
    slength      c1_ind_ptr[ROWS];       // 缓冲区长度  
     slength      c2_ind_ptr[ROWS];       // 缓冲区长度  
    slength      c3_ind_ptr[ROWS];       // 缓冲区长度  
    slength      c4_ind_ptr[ROWS];       // 缓冲区长度  
    slength      c5_ind_ptr[ROWS];       // 缓冲区长度  
     slength      c6_ind_ptr[ROWS]; 
     slength      c7_ind_ptr[ROWS];  
     int        i; 
     ulength        i_array_rows = ROWS;  
     //分配语句句柄   
     rt = dpi_alloc_stmt(hcon, &hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
     //设置语句句柄属性  
     rt = dpi_set_stmt_attr(hstmt, DSQL_ATTR_PARAMSET_SIZE, (dpointer)i_array_rows, sizeof(i_array_rows)); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     //准备sql 
     rt = dpi_prepare(hstmt, "insert into dpi_demo(c1,c2,c3,c4,c5,c6,c7) values(?,?,?,?,?,?,?)"); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     //赋值  
     for (i=0; i<i_array_rows; i++)  
     { 
         c1[i]      = i+10; 
         memcpy(c2[i], "abcde", 5); 
         memcpy(c3[i], "abcdefghi", 9); 
         c4[i]      = 0.00901; 
        c5[i].year    = 2011; 
         c5[i].month  = 3; 
         c5[i].day    = 1; 
         c5[i].hour    = 11; 
         c5[i].minute  = 45; 
         c5[i].second  = 50; 
         c5[i].fraction  = 900; 
         memcpy(c6[i], "adfadsfetre2345ert", 18); 
         memcpy(c7[i], "1234567890abcdef12", 18);
        c1_ind_ptr[i] = sizeof(c1[i]);
         c2_ind_ptr[i] = 5;  //获取缓冲区长度 
         c3_ind_ptr[i] = 9; 
        c4_ind_ptr[i] = sizeof(c4[i]);
        c5_ind_ptr[i] = sizeof(c5[i]);
         c6_ind_ptr[i] = 18; 
         c7_ind_ptr[i] = 18; 
     }  
     // 绑定参数  
     rt = dpi_bind_param(hstmt, 1, DSQL_PARAM_INPUT, DSQL_C_SLONG, DSQL_INT, sizeof(c1[0]), 0, &c1[0], sizeof(c1[0]), &c1_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 2, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CHAR, 
sizeof(c2[0]), 0, c2[0], sizeof(c2[0]), &c2_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 3, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_VARCHAR, 
     sizeof(c3[0]), 0, c3[0], sizeof(c3[0]), &c3_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 4, DSQL_PARAM_INPUT, DSQL_C_DOUBLE, DSQL_DOUBLE, 
sizeof(c4[0]), 0, &c4[0], sizeof(c4[0]), (slength*)&c4_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 5, DSQL_PARAM_INPUT, DSQL_C_TIMESTAMP, 
DSQL_TIMESTAMP, sizeof(c5[0]), 0, &c5[0], sizeof(c5[0]), (slength*)&c5_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 6, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CLOB, 
sizeof(c6[0]), 0, c6[0], sizeof(c6[0]), &c6_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     rt = dpi_bind_param(hstmt, 7, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_BLOB, 
sizeof(c7[0]), 0, c7[0], sizeof(c7[0]), &c7_ind_ptr[0]); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt); 
     // 执行Dsql  
     rt = dpi_exec(hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     //释放语句句柄  
     rt = dpi_free_stmt(hstmt); 
     DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);  
     printf("dm insert with bind array success\n"); 
     return DSQL_SUCCESS; 
}
/************************************************
    fetch获取结果集
************************************************/
DPIRETURN
dm_select_with_fetch()
{
    sdint4                c1 = 0;             //与字段匹配的变量，用于获取字段值
    sdbyte                c2[20];
    sdbyte                c3[50];
    ddouble           c4;
    dpi_timestamp_t        c5;
    sdbyte                c6[50];
    sdbyte                c7[FLEN];  
    slength                c1_ind = 0;     //缓冲区 
    slength                c2_ind = 0;
    slength                c3_ind = 0;
    slength                c4_ind = 0;
    slength                c5_ind = 0;
    slength                c6_ind = 0;
    slength                c7_ind = 0;  
    ulength                row_num;        //行数 
    sdint4                 dataflag = 0;  
    //分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);  
    //执行sql语句
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);  
    // 绑定输出列 
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1, sizeof(c1), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2, sizeof(c2), &c2_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3, sizeof(c3), &c3_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4, sizeof(c4), &c4_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5, sizeof(c5), &c5_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6, sizeof(c6), &c6_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_NCHAR, &c7, sizeof(c7), &c7_ind), DSQL_HANDLE_STMT, hstmt);  
    printf("dm_select_with_fetch......\n");
    printf("----------------------------------------------------------------------\n");
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
        printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
        printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
        printf("c6 = %s, c7 = %s\n",c6, c7);
        dataflag = 1;
}
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
{
    //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_fetch failed\n");
        return DSQL_ERROR;
}
    printf("----------------------------------------------------------------------\n");
    if (!dataflag)
    {
        printf("dm no data\n");
    }  
    // 释放语句句柄 
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
/************************************************
    使用参数绑定后再fetch获取结果集
************************************************/
DPIRETURN
dm_select_with_fetch_with_param()
{
    sdint4                c1 = 0;             //与字段匹配的变量，用于获取字段值
    slength             c1_param_ind = 0;
    sdbyte                c2[20];
    sdbyte                c3[50];
    ddouble                c4;
    dpi_timestamp_t        c5;
    sdbyte                c6[50];
    sdbyte                c7[FLEN];  
    slength                c1_ind = 0;     //缓冲区
    slength                c2_ind = 0;
    slength                c3_ind = 0;
    slength                c4_ind = 0;
    slength                c5_ind = 0;
    slength                c6_ind = 0;
    slength                c7_ind = 0;  
    ulength                row_num;        // 行数 
    sdint4              dataflag = 0;  
    c1 = 10;    //读取c1=10的数据  
    //分配语句句柄
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    // 准备sql
    DPIRETURN_CHECK(dpi_prepare(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo where c1 = ?"), DSQL_HANDLE_STMT, hstmt);
    //绑定参数 
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 1, DSQL_PARAM_INPUT, DSQL_C_STINYINT, DSQL_INT, sizeof(c1), 0, &c1, sizeof(c1), &c1_param_ind), DSQL_HANDLE_STMT, hstmt);
    // 执行sql 
    DPIRETURN_CHECK(dpi_exec(hstmt), DSQL_HANDLE_STMT, hstmt);  
    // 绑定输出列
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1, sizeof(c1), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2, sizeof(c2), &c2_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3, sizeof(c3), &c3_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4, sizeof(c4), &c4_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5, sizeof(c5), &c5_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6, sizeof(c6), &c6_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_NCHAR, &c7, sizeof(c7), &c7_ind), DSQL_HANDLE_STMT, hstmt);  
    // 打印输出信息 
    printf("dm_select_with_fetch_with_param......\n");
    printf("----------------------------------------------------------------------\n");
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
        printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
        printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
        printf("c6 = %s, c7 = %s\n",c6, c7);
        dataflag = 1;
}
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
{
    //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_fetch_with_param failed\n");
        return DSQL_ERROR;
}
    printf("----------------------------------------------------------------------\n");
    if (!dataflag)
    {
        printf("dm no data\n");
    }  
    //释放语句句柄 
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
/************************************************
fetch获取结果集,scroll结果集
************************************************/
DPIRETURN
dm_select_with_fetch_scroll()
{
    sdint4                c1 = 0;             //与字段匹配的变量，用于获取字段值 
    sdbyte                c2[20];
    sdbyte                c3[50];
    ddouble                c4;
    dpi_timestamp_t        c5;
    sdbyte                c6[50];
    sdbyte                c7[FLEN];
    slength                c1_ind = 0;     //缓冲区 
    slength                c2_ind = 0;
    slength                c3_ind = 0;
    slength                c4_ind = 0;
    slength                c5_ind = 0;
    slength                c6_ind = 0;
    slength                c7_ind = 0;
    ulength                row_num;        // 行数 
    ulength                val = DSQL_CURSOR_DYNAMIC;
    sdint4              dataflag = 0;
    // 分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    //设置语句句柄属性
    DPIRETURN_CHECK(dpi_set_stmt_attr(hstmt, DSQL_ATTR_CURSOR_TYPE, (dpointer)val, 0), DSQL_HANDLE_STMT, hstmt);
    //执行sql 
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    // 绑定输出列
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1, sizeof(c1), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2, sizeof(c2), &c2_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3, sizeof(c3), &c3_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4, sizeof(c4), &c4_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5, sizeof(c5), &c5_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6, sizeof(c6), &c6_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_NCHAR, &c7, sizeof(c7), &c7_ind), DSQL_HANDLE_STMT, hstmt);
    // 显示输出信息
    printf("dm_select_with_fetch_scroll......\n");
    printf("----------------------------------------------------------------------\n");
    for(rt=dpi_fetch_scroll(hstmt, DSQL_FETCH_NEXT, 0, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch_scroll(hstmt, DSQL_FETCH_NEXT, 0, &row_num))
    {
        printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
        printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
        printf("c6 = %s, c7 = %s\n",c6, c7);
        dataflag = 1;
}
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
{
    //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_fetch_scroll failed\n");
        return DSQL_ERROR;
}
    if (!dataflag)
    {
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm no data\n");
        return DSQL_SUCCESS;
}

    DPIRETURN_CHECK(dpi_fetch_scroll(hstmt, DSQL_FETCH_FIRST, 0, &row_num), DSQL_HANDLE_STMT, hstmt);
    printf("move first : 1\n");
    printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
    printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
    printf("c6 = %s, c7 = %s\n",c6, c7);
    DPIRETURN_CHECK(dpi_fetch_scroll(hstmt, DSQL_FETCH_LAST, 0, &row_num), DSQL_HANDLE_STMT, hstmt);
    printf("move last : 19\n");
    printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
    printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
    printf("c6 = %s, c7 = %s\n",c6, c7);
    DPIRETURN_CHECK(dpi_fetch_scroll(hstmt, DSQL_FETCH_ABSOLUTE, 6, &row_num), DSQL_HANDLE_STMT, hstmt);
    printf("move absolute 6: 14\n");
    printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
    printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
    printf("c6 = %s, c7 = %s\n",c6, c7);
    DPIRETURN_CHECK(dpi_fetch_scroll(hstmt, DSQL_FETCH_PRIOR, 0, &row_num), DSQL_HANDLE_STMT, hstmt);
    printf("move prior : 13\n");
    printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
    printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
    printf("c6 = %s, c7 = %s\n",c6, c7);
    DPIRETURN_CHECK(dpi_fetch_scroll(hstmt, DSQL_FETCH_RELATIVE, 3, &row_num), DSQL_HANDLE_STMT, hstmt);
    printf("move relative 3: 16\n");
    printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
    printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
    printf("c6 = %s, c7 = %s\n",c6, c7);
    printf("----------------------------------------------------------------------\n");
    //释放语句句柄 
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
/************************************************
fetch获取结果集输出到数组
使用dpi_set_pos更新结果集，分别查询更新前和更新后的结果集
************************************************/
DPIRETURN
dm_select_with_fetch_array()
{
    sdint4                c1[ROWS];             //与字段匹配的变量，用于获取字段值
    sdbyte                c2[ROWS][20];
    sdbyte                c3[ROWS][50];
    ddouble                c4[ROWS];
    dpi_timestamp_t        c5[ROWS];
    sdbyte                c6[ROWS][50];
    sdbyte                c7[ROWS][FLEN];
    slength                c1_ind[ROWS];     //缓冲区 
    slength                c2_ind[ROWS];
    slength                c3_ind[ROWS];
    slength                c4_ind[ROWS];
    slength                c5_ind[ROWS];
    slength                c6_ind[ROWS];
    slength                c7_ind[ROWS];
    ulength                row_num;        //行数 
    ulength                i;
    ulength                i_array_rows = ROWS;
    //分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    //设置语句句柄属性
    DPIRETURN_CHECK(dpi_set_stmt_attr(hstmt, DSQL_ATTR_ROWSET_SIZE, (dpointer)i_array_rows, sizeof(i_array_rows)), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_set_stmt_attr(hstmt, DSQL_ATTR_CURSOR_TYPE, (dpointer)DSQL_CURSOR_KEYSET_DRIVEN, 0), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_set_stmt_attr(hstmt, DSQL_ATTR_CONCURRENCY, (dpointer)DSQL_CONCUR_VALUES, 0), DSQL_HANDLE_STMT, hstmt);
    //执行sql
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    //绑定输出列
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1[0], sizeof(c1[0]), &c1_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2[0], sizeof(c2[0]), &c2_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3[0], sizeof(c3[0]), &c3_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4[0], sizeof(c4[0]), &c4_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5[0], sizeof(c5[0]), &c5_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6[0], sizeof(c6[0]), &c6_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_NCHAR, &c7[0], sizeof(c7[0]), &c7_ind[0]), DSQL_HANDLE_STMT, hstmt);
    /* 打印输出信息 */
    printf("dm_select_with_fetch_array......\n");
    printf("----------------------------------------------------------------------\n");
    printf("更新前结果集如下：\n");
    rt=dpi_fetch(hstmt, &row_num);
    // rt=dpi_fetch_scroll(hstmt, DSQL_FETCH_NEXT, 0, &row_num);
    // DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
  
    if (DSQL_SUCCEEDED(rt) && rt!=DSQL_NO_DATA)
    {
        row_num = row_num > ROWS ? ROWS : row_num;
        for (i=0; i<row_num; i++)
        {
            printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1[i], c2[i], c3[i], c4[i]);
            printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5[i].year,c5[i].month,c5[i].day,c5[i].hour,c5[i].minute,c5[i].second,c5[i].fraction);
            printf("c6 = %s, c7 = %s\n",c6[i], c7[i]);
        }
}
    else if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
{
    //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_fetch_array failed\n");
        return DSQL_ERROR;
}
    else
    {
        printf("dm no data\n");
    }
    //使用dpi_set_pos更新结果集，更新第1行的数据
    c1[0] = 202508;
    memcpy(c2[0], "fglmn", 5); 
    memcpy(c3[0], "fglmnyhtd", 9); 
    c4[0]      = 0.04081; 
    c5[0].year    = 2025; 
    c5[0].month  = 8; 
    c5[0].day    = 29; 
    c5[0].hour    = 15; 
    c5[0].minute  = 43; 
    c5[0].second  = 45; 
    c5[0].fraction  = 700; 
    memcpy(c6[0], "jhfrts345hnmd6dgfn", 18); 
    memcpy(c7[0], "9876543210abcdef12", 18);
    row_num = 1;
    DPIRETURN_CHECK(dpi_set_pos(hstmt, row_num, DSQL_UPDATE, DSQL_LOCK_NO_CHANGE), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_close_cursor(hstmt), DSQL_HANDLE_STMT, hstmt);

    //再次执行sql，查询更新后的结果集
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    //绑定输出列
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1[0], sizeof(c1[0]), &c1_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2[0], sizeof(c2[0]), &c2_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3[0], sizeof(c3[0]), &c3_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4[0], sizeof(c4[0]), &c4_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5[0], sizeof(c5[0]), &c5_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6[0], sizeof(c6[0]), &c6_ind[0]), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_NCHAR, &c7[0], sizeof(c7[0]), &c7_ind[0]), DSQL_HANDLE_STMT, hstmt);
    printf("更新后结果集如下：\n");
    rt=dpi_fetch(hstmt, &row_num);
    if (DSQL_SUCCEEDED(rt) && rt!=DSQL_NO_DATA)
    {
        row_num = row_num > ROWS ? ROWS : row_num;
        for (i=0; i<row_num; i++)
        {
            printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1[i], c2[i], c3[i], c4[i]);
            printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5[i].year,c5[i].month,c5[i].day,c5[i].hour,c5[i].minute,c5[i].second,c5[i].fraction);
            printf("c6 = %s, c7 = %s\n",c6[i], c7[i]);
        }
}
    else if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
{
    //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_fetch_array failed\n");
        return DSQL_ERROR;
}
    else
    {
        printf("dm no data\n");
    }
    printf("----------------------------------------------------------------------\n");
    //释放语句句柄 
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}

DPIRETURN
    dm_insert_select_complex_type_value()
    {
        dhobj           obj;          //复合对象句柄
        dhobjdesc       obj_desc;     //复合对象描述句柄
        udint4          cnt, cnt1;
        slength         len;
        sdint2          type, type1, type2;
        sdint2          prec, prec1, prec2;
        sdint2          scale, scale1, scale2;
        int             c1_data,c1_val;
        char            c2_data[21],c2_val[21];
        slength         val_len[2],data_len[2];
        //分配语句句柄 
        DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
        dpi_exec_direct(hstmt, "drop table t");
        dpi_exec_direct(hstmt, "drop class cls1");
        DPIRETURN_CHECK(dpi_exec_direct(hstmt, "create class cls1 as c1 int; c2 varchar(20); end;"),DSQL_HANDLE_STMT, hstmt);
        DPIRETURN_CHECK(dpi_exec_direct(hstmt, "create table t(c1 cls1)"),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_desc_obj(hcon, "SYSDBA", "CLS1", &obj_desc),DSQL_HANDLE_DBC,hcon);
        DPIRETURN_CHECK(dpi_alloc_obj(hcon, &obj),DSQL_HANDLE_DBC,hcon);
        DPIRETURN_CHECK(dpi_bind_obj_desc(obj,obj_desc),DSQL_HANDLE_OBJECT,obj);
        //复合类型获取描述信息
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 0, DSQL_ATTR_OBJ_FIELD_COUNT, &cnt1, sizeof(cnt1), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("cnt is : %d\n",cnt1);
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 1, DSQL_ATTR_OBJ_TYPE, &type1, sizeof(type1), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("type1 is : %d\n",type1);
        if (type1!=DSQL_INT)
        {
            printf("type error");
        }
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 2, DSQL_ATTR_OBJ_TYPE, &type2, sizeof(type2), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("type2 is : %d\n",type2);
        if (type1!=DSQL_VARCHAR)
        {
            printf("type error");
        }
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 1, DSQL_ATTR_OBJ_PREC, &prec1, sizeof(prec1), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("prec1 is : %d\n",prec1);
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 2, DSQL_ATTR_OBJ_PREC, &prec2, sizeof(prec2), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("prec1 is : %d\n",prec2);
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 1, DSQL_ATTR_OBJ_SCALE, &scale1, sizeof(scale1), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("scale1 is : %d\n",scale1);
        DPIRETURN_CHECK(dpi_get_obj_desc_attr(obj_desc, 2, DSQL_ATTR_OBJ_SCALE, &scale2, sizeof(scale2), NULL),DSQL_HANDLE_OBJDESC,obj_desc);
        printf("scale2 is : %d\n",scale2);

        //复合类型插入
        c1_data=1;
        strcpy(c2_data,"aaa");
        data_len[0]=sizeof(c1_data);
        data_len[1]=strlen(c2_data);
        DPIRETURN_CHECK(dpi_set_obj_val(obj, 1, DSQL_C_SLONG, &c1_data, data_len[0]),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_set_obj_val(obj, 2, DSQL_C_NCHAR, &c2_data, data_len[1]),DSQL_HANDLE_STMT,hstmt);
        // 执行sql 
        DPIRETURN_CHECK(dpi_prepare(hstmt,"insert into t(c1) values(?)"), DSQL_HANDLE_STMT, hstmt);
        //绑定输出列 
        len = sizeof(obj);
        DPIRETURN_CHECK(dpi_bind_param(hstmt, 1, DSQL_PARAM_INPUT, DSQL_C_CLASS, DSQL_CLASS, 0, 0, &obj, sizeof(obj), &len), DSQL_HANDLE_STMT, hstmt);
        DPIRETURN_CHECK(dpi_exec(hstmt),DSQL_HANDLE_STMT, hstmt);
        DPIRETURN_CHECK(dpi_commit(hcon),DSQL_HANDLE_DBC,hcon);
        //复合类型查询
        DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1 from t"),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_CLASS, &obj, sizeof(obj), &len),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_fetch(hstmt, NULL),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_get_obj_val(obj, 1, DSQL_C_SLONG, &c1_val, sizeof(c1_val), &val_len[0]),DSQL_HANDLE_STMT,hstmt);
        DPIRETURN_CHECK(dpi_get_obj_val(obj, 2, DSQL_C_NCHAR, c2_val, sizeof(c2_val), &val_len[1]),DSQL_HANDLE_STMT,hstmt);
        printf("c1_val=%d,c2_val=%s\n",c1_val,c2_val);
        if (c1_val!=c1_data||strcmp(c2_val,c2_data)!=0)
        {
            printf("dpi_get_obj_val获取结果 error");
        }
        printf("----------------------------------------------------------------------\n");
        //释放语句句柄 
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        return DSQL_SUCCESS;
    }

//入口函数
DPIRETURN
main()
{
    //连接数据库
    rt = dm_dpi_connect(DM_SVR, DM_USER, DM_PWD);
    FUN_CHECK(rt);
    //初始化表
    rt = dm_init_table();
    FUN_CHECK(rt);
    //通过参数绑定的方式插入数据
    rt = dm_insert_with_bind_param();
    FUN_CHECK(rt);
    //通过数组绑定的方式插入数据
    rt = dm_insert_with_bind_array();
    FUN_CHECK(rt);
    //通过fetch查询得到结果集
    rt = dm_select_with_fetch();
    FUN_CHECK(rt);
    //通过参数绑定查询得到结果集
    rt = dm_select_with_fetch_with_param();
    FUN_CHECK(rt);
    //通过fetch scroll获取结果集
    rt = dm_select_with_fetch_scroll();
    FUN_CHECK(rt);
    //查询列绑定数组输出
    rt = dm_select_with_fetch_array();
    FUN_CHECK(rt);
   //复合类型插入查询描述信息获取示例
    rt = dm_insert_select_complex_type_value();
    FUN_CHECK(rt);
 //断开连接
    rt = dm_dpi_disconnect();
    FUN_CHECK(rt);
END:
    return DSQL_SUCCESS;
}
```

编译后运行，结果如下：

```
dm init table success
dm insert with bind param success
dm insert with bind array success
dm_select_with_fetch......
----------------------------------------------------------------------
c1 = 201410, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:51.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 10, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 11, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 12, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 13, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 14, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 15, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 16, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 17, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 18, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 19, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
----------------------------------------------------------------------
dm_select_with_fetch_with_param......
----------------------------------------------------------------------
c1 = 10, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
----------------------------------------------------------------------
dm_select_with_fetch_scroll......
----------------------------------------------------------------------
c1 = 201410, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:51.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 10, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 11, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 12, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 13, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 14, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 15, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 16, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 17, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 18, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 19, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
move first : 1
c1 = 201410, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:51.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
move last : 19
c1 = 19, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
move absolute 6: 14
c1 = 14, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
move prior : 13
c1 = 13, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
move relative 3: 16
c1 = 16, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
----------------------------------------------------------------------
dm_select_with_fetch_array......
----------------------------------------------------------------------
更新前结果集如下：
c1 = 201410, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:51.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 10, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 11, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 12, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 13, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 14, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 15, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 16, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 17, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 18, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
更新后结果集如下：
c1 = 202508, c2 = fglmn              , c3 = fglmnyhtd, c4 = 0.041000, c5 = 2025-8-29 15:43:45.0
c6 = jhfrts345hnmd6dgfn, c7 = 9876543210abcdef12
c1 = 10, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 11, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 12, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 13, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 14, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 15, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 16, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 17, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
c1 = 18, c2 = abcde              , c3 = abcdefghi, c4 = 0.009000, c5 = 2011-3-1 11:45:50.0
c6 = adfadsfetre2345ert, c7 = 1234567890abcdef12
----------------------------------------------------------------------
cnt is : 2
type1 is : 7
type2 is : 2
type errorprec1 is : 4
prec1 is : 20
scale1 is : 0
scale2 is : 0
c1_val=1,c2_val=aaa
----------------------------------------------------------------------
```

### 2.4.3 大字段操作

下面通过一个简单的 Windows 环境下的示例来说明 DPI 大字段操作。

创建一个表，读取文件插入到 lob 字段，从 lob 字段读取数据写入到文件，更新 lob 字段值，通过专用函数 dpi\_lob\_read 读取大字段数据，通过 dpi\_lob\_truncate 截取大字段。

```
#include "DPI.h"
#include "DPIext.h"
#include "DPItypes.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
/******************************************************
Notes:
定义相应常量
*******************************************************/
#define ROWS    10                //数组绑定一次插入和读取的行数
#define CHARS    80*1024            //一次读取和写入的字节数800K
#define FLEN    500                //文件名长度(带地址路径)
#define DM_SVR  "192.168.0.120:5336"
#define DM_USER "SYSDBA"
#define DM_PWD  "sysDBA*00"
#define IN_FILE     "d:\\drivers_win64+win32.zip"
#define UP_FILE     "d:\\drivers_rh6_64+rh6_32.zip"
//函数检查及错误信息显示
#define DPIRETURN_CHECK(rt, hndl_type, hndl) if(!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA){dpi_err_msg_print(hndl_type, hndl);return rt;}
#define FUN_CHECK(rt) if(!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA){goto END;}
/******************************************************
Notes:
定义常用句柄和变量
*******************************************************/
dhenv        henv;        /* 环境句柄 */
dhcon        hcon;        /* 连接句柄 */
dhstmt        hstmt;        /* 语句句柄 */
dhdesc      hdesc;      /* 描述符句柄 */
dhloblctr    hloblctr;    /* lob类型控制句柄 */
DPIRETURN   rt;         /* 函数返回值 */
/******************************************************
Notes:
    错误信息获取打印
Param:
    hndl_type:    句柄类型
    hndl:        句柄
Return:
    无
*******************************************************/
void
dpi_err_msg_print(sdint2 hndl_type, dhandle hndl)
{
    sdint4 err_code;
    sdint2 msg_len;
    sdbyte err_msg[SDBYTE_MAX];
    //获取错误信息字段
/*    dpi_get_diag_field(hndl_type, hndl, 1, DSQL_DIAG_MESSAGE_TEXT, err_msg, sizeof(err_msg), NULL);
    printf("err_msg = %s\n", err_msg);*/
    //获取错误信息集合
    dpi_get_diag_rec(hndl_type, hndl, 1, &err_code, err_msg, sizeof(err_msg), &msg_len);
    printf("err_msg = %s, err_code = %d\n", err_msg, err_code);
}
/******************************************************
Notes:
    连接数据库
Param:
    server:    服务器IP
    uid:    数据库登录账号
    pwd:    数据库登录密码
Return:
    DSQL_SUCCESS 执行成功
    DSQL_ERROR   执行失败
*******************************************************/
DPIRETURN 
dm_dpi_connect(sdbyte* server,  sdbyte* uid, sdbyte* pwd)
{
    //申请环境句柄
    rt = dpi_alloc_env(&henv);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_ENV, henv);
    //申请连接句柄 
    rt = dpi_alloc_con(henv, &hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    //连接数据库服务器
    rt = dpi_login(hcon, server, uid, pwd);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    return DSQL_SUCCESS;
}
/************************************************
    断开数据库连接
************************************************/
DPIRETURN
dm_dpi_disconnect()
{
    //断开连接
    rt = dpi_logout(hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    //释放连接句柄和环境句柄
    rt = dpi_free_con(hcon);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    rt = dpi_free_env(henv);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_ENV, henv);
  
    return DSQL_SUCCESS;
}
/************************************************
    初始化表
************************************************/
DPIRETURN 
dm_init_table()
{
    //申请语句句柄
    rt = dpi_alloc_stmt(hcon, &hstmt);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    //执行sql 
    dpi_exec_direct(hstmt, "drop table dpi_demo");
    rt = dpi_exec_direct(hstmt, "create table dpi_demo(c1 int, c2 char(20), c3 varchar(50), c4 numeric(7,3), c5 timestamp(5), c6 clob, c7 blob)");
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
    //释放语句句柄 
    rt = dpi_free_stmt(hstmt);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
    printf("dm init table success\n");
    return DSQL_SUCCESS;
}
/************************************************
    从带地址路径的文件名中获取不带路径的文件名
************************************************/
sdbyte*
dm_get_file_name(char* fdirname)
{
    char* fname;
    fname = (char*)malloc(FLEN);
    while(1)
    {
        fdirname = strchr(fdirname+1,'\\');
        if (fdirname == NULL)
        {
            break;
        }
        memcpy(fname, fdirname + 1, FLEN);
    }
    return fname;
}
/************************************************
    读取文件数据写入到lob字段
************************************************/
DPIRETURN
dm_read_file_to_put_data(char* fname)
{
    FILE*        pfile = NULL;
    sdbyte        tmpbuf[CHARS];
    slength        rlen = 0;
    slength        len     = 0;
    //打开文件
    pfile = fopen(fname, "rb");
    if (pfile == NULL)
    {
        printf("open %s fail\n", fname);
        return DSQL_ERROR;
    }
    //读取文件数据写入到缓冲区
    printf("==========Begin write==========\n");
    while (!feof(pfile))
    {
        len = fread(tmpbuf, sizeof(char), CHARS, pfile);
        if (len <= 0)
        {
            return DSQL_ERROR;
        }
        DPIRETURN_CHECK(dpi_put_data(hstmt, tmpbuf, len), DSQL_HANDLE_STMT, hstmt);
        rlen += len;
        printf("write %u bytes\n", rlen);
    }
    printf("==========End   write==========\n");
    fclose(pfile);
    return DSQL_SUCCESS;
}
/************************************************
    读取数据写入到文件
************************************************/
DPIRETURN
dm_write_file_from_get_data(char* fname)
{
    FILE*        pfile = NULL;
    sdbyte        tmpbuf[CHARS];
    slength        val_len;
    slength        wlen = 0;
    slength        len     = 0;
    //打开文件
    pfile = fopen(fname, "wb");
    if (pfile == NULL)
    {
        printf("open %s fail\n", fname);
        return DSQL_ERROR;
    }
    //读取数据写入到文件
    printf("==========Begin read==========\n");
    while(DSQL_SUCCEEDED(dpi_get_data(hstmt, 7, DSQL_C_BINARY, tmpbuf, CHARS, &val_len)))
    {
        len = val_len > CHARS ? CHARS : val_len;
        fwrite(tmpbuf, sizeof(char), len, pfile);
        wlen += len;
        printf("read %u bytes\n", wlen);
    }
    printf("==========End   read==========\n");
    fclose(pfile);
    return DSQL_SUCCESS;
}
/************************************************
    读取文件插入到blob字段
************************************************/
DPIRETURN
dm_insert_with_file()
{
    sdint4            c1;             //定义字段相应的变量 
    sdbyte            c2[10];
    sdbyte            c3[10];
    ddouble            c4;
    dpi_timestamp_t c5;
    sdbyte            c6[FLEN];
    sdint4            c7;
    slength            c2_ind_ptr;        //缓冲区长度
    slength            c3_ind_ptr;
    slength            c6_ind_ptr;
    slength            c7_ind_ptr = DSQL_DATA_AT_EXEC;
    dpointer        c7_val_ptr;

    //分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    //准备sql
    DPIRETURN_CHECK(dpi_prepare(hstmt, "insert into dpi_demo(c1,c2,c3,c4,c5,c6,c7) values(?,?,?,?,?,?,?)"), DSQL_HANDLE_STMT, hstmt);
    //赋值 
    c1            = 1;
    memcpy(c2, "abcde", 10);
    memcpy(c3, "abcdefghi", 10);
    c4            = 1000.001;
    c5.year        = 2011;
    c5.month    = 3;
    c5.day        = 1;
    c5.hour        = 11;
    c5.minute    = 45;
    c5.second    = 50;
    c5.fraction    = 900000000;
    memcpy(c6, dm_get_file_name(IN_FILE), FLEN);
    c7            = DSQL_DATA_AT_EXEC;
    c2_ind_ptr = sizeof(c2);    //获取缓冲区长度 
    c3_ind_ptr = sizeof(c3);
    c6_ind_ptr = sizeof(c6);
    //绑定参数 
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 1, DSQL_PARAM_INPUT, DSQL_C_SLONG, DSQL_INT, sizeof(c1), 0, &c1, sizeof(c1), NULL), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 2, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CHAR, sizeof(c2), 0, &c2, sizeof(c2), &c2_ind_ptr), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 3, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_VARCHAR, sizeof(c3), 0, &c3, sizeof(c3), &c3_ind_ptr), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 4, DSQL_PARAM_INPUT, DSQL_C_DOUBLE, DSQL_DOUBLE, sizeof(c4), 0, &c4, sizeof(c4), NULL), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 5, DSQL_PARAM_INPUT, DSQL_C_TIMESTAMP, DSQL_TIMESTAMP, sizeof(c5), 0, &c5, sizeof(c5), NULL), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 6, DSQL_PARAM_INPUT, DSQL_C_NCHAR, DSQL_CLOB, sizeof(c6), 0, &c6, sizeof(c6), &c6_ind_ptr), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_param(hstmt, 7, DSQL_PARAM_INPUT, DSQL_C_BINARY, DSQL_BLOB, sizeof(c7), 0, &c7, sizeof(c7), &c7_ind_ptr), DSQL_HANDLE_STMT, hstmt);
    //执行sql 
    if (dpi_exec(hstmt) == DSQL_NEED_DATA)
    {
        if (dpi_param_data(hstmt, &c7_val_ptr) == DSQL_NEED_DATA)   //绑定数据
        {
            if (!DSQL_SUCCEEDED(dm_read_file_to_put_data(IN_FILE))) return DSQL_ERROR;  //读取文件数据存入到字段
        }
        DPIRETURN_CHECK(dpi_param_data(hstmt, &c7_val_ptr), DSQL_HANDLE_STMT, hstmt); //绑定数据
    }
    //释放语句句柄
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    printf("dm insert with file success\n");
    return DSQL_SUCCESS;
}
/************************************************
    查询，并将blob字段中插入的文件写入到新的文件中
************************************************/
DPIRETURN
dm_select_with_file()
{
    sdint4                c1 = 0;             //与字段匹配的变量，用于获取字段值
    sdbyte                c2[20];
    sdbyte                c3[50];
    ddouble                c4;
    dpi_timestamp_t        c5;
    sdbyte                c6[50];
    sdbyte                c7[FLEN];
    slength                c1_ind = 0;     //缓冲区
    slength                c2_ind = 0;
    slength                c3_ind = 0;
    slength                c4_ind = 0;
    slength                c5_ind = 0;
    slength                c6_ind = 0;
    slength                c7_ind = 0;
    ulength                row_num;        //行数
    ulength                rows = 1;
    sdint4              dataflag = 0;
    //分配语句句柄
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1, sizeof(c1), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2, sizeof(c2), &c2_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3, sizeof(c3), &c3_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4, sizeof(c4), &c4_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5, sizeof(c5), &c5_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6, sizeof(c6), &c6_ind), DSQL_HANDLE_STMT, hstmt);
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
        printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
        printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
        printf("c6 = %s\n",c6);
        sprintf(c7, "F:\\%d_%s", rows, c6);
        printf("c7 write to %s\n",c7);
        if (!DSQL_SUCCEEDED(dm_write_file_from_get_data(c7))) return DSQL_ERROR;    //获取数据写入到文件
        rows++;
        dataflag = 1;
    }
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
    {
        //释放语句句柄
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_select_with_file failed\n");
        return DSQL_ERROR;
    }
    if (!dataflag)
    {
        printf("dm no data\n");
    }
    //释放语句句柄
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
/************************************************
    截断lob句柄所对应的大字段到指定的长度
************************************************/
DPIRETURN
dm_blob_truncate_data(
                   )
{
    slength            c1_ind = 0;
    slength         trun_len;
    ulength         row_num;        //行数 
    rt = dpi_alloc_stmt(hcon, &hstmt);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_DBC, hcon);
    rt = dpi_alloc_lob_locator(hstmt, &hloblctr);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    rt = dpi_exec_direct(hstmt, "select c7 from dpi_demo");
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
    rt = dpi_bind_col(hstmt, 1, DSQL_C_LOB_HANDLE, &hloblctr, sizeof(hloblctr), &c1_ind);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_STMT, hstmt);
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
        printf("%d\n", CHARS);
        rt = dpi_lob_truncate(hloblctr, CHARS, &trun_len);
        printf("%d\n", trun_len);
        FUN_CHECK(rt);
    }
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
    {
        DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_blob_truncate_data failed\n");
        return DSQL_ERROR;
    }

END:  
    DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    printf("dm_blob_truncate_data success\n");
    return DSQL_SUCCESS;
}
/************************************************
    lob_read
************************************************/
DPIRETURN
dm_lob_read(char* fname)
{
    FILE*        pfile = NULL;
    sdbyte        tmpbuf[CHARS];
    slength        val_len;
    slength        wlen = 0;
    slength     len, rlen;
    ulength     pos;
    //打开文件 
    pfile = fopen(fname, "wb");
    if (pfile == NULL)
    {
        printf("open %s fail\n", fname);
        return DSQL_ERROR;
    }
    //获取大字段长度
    rt = dpi_lob_get_length(hloblctr, &len);
    DPIRETURN_CHECK(rt, DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    //读取数据写入到文件 
    printf("==========Begin read==========\n");
    while(len > 0)
    {
        pos = wlen+1;
        rlen = (len > CHARS) ? CHARS : len;
        rt = dpi_lob_read(hloblctr, pos, DSQL_C_BINARY, rlen, tmpbuf, sizeof(tmpbuf), &val_len);
        fwrite(tmpbuf, sizeof(char), val_len, pfile);
        wlen += val_len;
        printf("read %u bytes\n", wlen);
        len = len - CHARS;
    }
    printf("==========End   read==========\n");
    fclose(pfile);
    return DSQL_SUCCESS;
}
/************************************************
    读取lob句柄所对应大字段的实际数据
************************************************/
DPIRETURN
dm_lob_read_to_file()
{
    sdint4                c1 = 0;             //与字段匹配的变量，用于获取字段值
    sdbyte                c2[20];
    sdbyte                c3[50];
    ddouble                c4;
    dpi_timestamp_t        c5;
    sdbyte                c6[50];
    sdbyte                c7[FLEN];
    slength                c1_ind = 0;     //缓冲区 
    slength                c2_ind = 0;
    slength                c3_ind = 0;
    slength                c4_ind = 0;
    slength                c5_ind = 0;
    slength                c6_ind = 0;
    slength                c7_ind = 0;
    ulength                row_num;        //行数
    ulength                rows = 1;
    sdint4              dataflag = 0;
    //分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_alloc_lob_locator(hstmt, &hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c1,c2,c3,c4,c5,c6,c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_SLONG, &c1, sizeof(c1), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 2, DSQL_C_NCHAR, &c2, sizeof(c2), &c2_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 3, DSQL_C_NCHAR, &c3, sizeof(c3), &c3_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 4, DSQL_C_DOUBLE, &c4, sizeof(c4), &c4_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 5, DSQL_C_TIMESTAMP, &c5, sizeof(c5), &c5_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 6, DSQL_C_NCHAR, &c6, sizeof(c6), &c6_ind), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 7, DSQL_C_LOB_HANDLE, &hloblctr, sizeof(hloblctr), &c7_ind), DSQL_HANDLE_STMT, hstmt);
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
        printf("c1 = %d, c2 = %s, c3 = %s, c4 = %f, ", c1, c2, c3, c4);
        printf("c5 = %d-%d-%d %d:%d:%d.%d\n",c5.year,c5.month,c5.day,c5.hour,c5.minute,c5.second,c5.fraction);
        printf("c6 = %s\n",c6);
        sprintf(c7, "F:\\%d_%s", rows, c6);
        printf("c7 write to %s\n",c7);
        if (!DSQL_SUCCEEDED(dm_lob_read(c7))) return DSQL_ERROR;    //获取数据写入到文件
        rows++;
        dataflag = 1;
    }
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
    {
        DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_lob_read_to_file failed\n");
        return DSQL_ERROR;
    }
    if (!dataflag)
    {
        printf("dm no data\n");
    }
    DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
/************************************************
    lob_write
************************************************/
DPIRETURN
dm_lob_write(char* fname)
{
    FILE*        pfile = NULL;
    sdbyte        tmpbuf[CHARS];
    slength        rlen = 0;
    slength        len     = 0;
    slength        wlen;
    ulength     pos;
    //打开文件 
    pfile = fopen(fname, "rb");
    if (pfile == NULL)
    {
        printf("open %s fail\n", fname);
        return DSQL_ERROR;
    }
    //读取文件数据写入到缓冲区
    printf("==========Begin write==========\n");
    while (!feof(pfile))
    {
        len = fread(tmpbuf, sizeof(char), CHARS, pfile);
        if (len <= 0)
        {
            return DSQL_ERROR;
        }
        pos = rlen+1;
        //DPIRETURN_CHECK(dpi_lob_write(hloblctr, pos, DSQL_C_BINARY, tmpbuf, len, &wlen), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
        rt = dpi_lob_write(hloblctr, pos, DSQL_C_BINARY, tmpbuf, len, &wlen);
        if(!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
        {
            dpi_err_msg_print(DSQL_HANDLE_LOB_LOCATOR, hloblctr);
            return rt;
        }

        rlen += len;
        printf("write %u bytes\n", rlen);
    }
    printf("==========End   write==========\n");
    fclose(pfile);
    return DSQL_SUCCESS;
}
/************************************************
    读取文件更新到lob字段
************************************************/
DPIRETURN
dm_lob_write_to_update()
{  
    slength                c1_ind = 0;     //缓冲区
    ulength                row_num;        //行数 
    ulength                rows = 1;
    sdint4              dataflag = 0;
    //分配语句句柄 
    DPIRETURN_CHECK(dpi_alloc_stmt(hcon, &hstmt), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_alloc_lob_locator(hstmt, &hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    DPIRETURN_CHECK(dpi_exec_direct(hstmt, "select c7 from dpi_demo"), DSQL_HANDLE_STMT, hstmt);
    DPIRETURN_CHECK(dpi_bind_col(hstmt, 1, DSQL_C_LOB_HANDLE, &hloblctr, sizeof(hloblctr), &c1_ind), DSQL_HANDLE_STMT, hstmt);
    for(rt=dpi_fetch(hstmt, &row_num); DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA; rt=dpi_fetch(hstmt, &row_num))
    {
     printf("%s update to c7\n",UP_FILE);
     if (!DSQL_SUCCEEDED(dm_lob_write(UP_FILE))) return DSQL_ERROR;    // 获取数据写入到文件 
     rows++;
     dataflag = 1;
    }
    if (!DSQL_SUCCEEDED(rt)&&rt!=DSQL_NO_DATA)
    {
        DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
        DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
        printf("dm_lob_write_to_update failed\n");
        return DSQL_ERROR;
    }
    if (!dataflag)
    {
        printf("dm no data\n");
    }
    DPIRETURN_CHECK(dpi_free_lob_locator(hloblctr), DSQL_HANDLE_LOB_LOCATOR, hloblctr);
    DPIRETURN_CHECK(dpi_free_stmt(hstmt), DSQL_HANDLE_STMT, hstmt);
    return DSQL_SUCCESS;
}
//入口函数
DPIRETURN
main()
{
    //连接数据
    rt = dm_dpi_connect(DM_SVR, DM_USER, DM_PWD);
    FUN_CHECK(rt);
    //初始化表
    rt = dm_init_table();
    FUN_CHECK(rt);
    //读取文件插入到lob字段（通过dpi_put_data函数写数据）
    rt = dm_insert_with_file();
    FUN_CHECK(rt);
    //从lob字段读取数据写入文件（通过dpi_get_data获取数据）
    rt = dm_select_with_file();
    FUN_CHECK(rt);

    //更新大字段（通过dpi_lob_write更新大字段数据）
    rt = dm_lob_write_to_update();
    FUN_CHECK(rt);
    //获取大字段值（通过dpi_lob_read读取大字段数据）
    rt = dm_lob_read_to_file();
    FUN_CHECK(rt);
    //截取大字段数据
    rt = dm_blob_truncate_data();
    FUN_CHECK(rt);
    //断开连接
    rt = dm_dpi_disconnect();
    FUN_CHECK(rt);
END:
    return  rt;
}
```

编译后运行，结果如下。由于大字段内容过多，这里省略部分输出：

```
dm init table success
==========Begin write==========
write 81920 bytes
write 163840 bytes
write 245760 bytes
...
write 49889280 bytes
write 49956327 bytes
==========End   write==========
dm insert with file success
c1 = 1, c2 = abcde, c3 = abcdefghi, c4 = 1000.001000, c5 = 2011-3-1 11:45:50.900000000
c6 =drivers_win64+win32.zip
c7 write to F:\1_drivers_win64+win32.zip
==========Begin read==========
read 81920 bytes
read 163840 bytes
...
read 49889280 bytes
read 49956327 bytes
==========End   read==========
d:\\drivers_rh6_64+rh6_32.zip update to c7
==========Begin write==========
write 81920 bytes
write 163840 bytes
write 245760 bytes
write 327680 bytes
...
write 49807360 bytes
write 49889280 bytes
write 49956327 bytes
==========End   write==========
c1 = 1, c2 = abcde, c3 = abcdefghi, c4 = 1000.001000, c5 = 2011-3-1 11:45:50.900000000
c6 = drivers_win64+win32.zip
c7 write to F:\1_drivers_win64+win32.zip
==========Begin read==========
read 81920 bytes
read 163840 bytes
read 245760 bytes
...
read 49889280 bytes
read 49956327 bytes
==========End   read==========
81920
81920
dm_blob_truncate_data success
```

## 2.5 数据捕获

数据捕获，用于捕获数据库中的表和视图的数据变化。用户根据应用的要求可以定制，用户可以监控表或视图的全部列，也可以监控表或视图的部分列，亦可以监控符合特定条件的列。另外，增强其可读性，在存储捕获的列的信息的时候，可以对这些列执行表达式操作，如把 binary 存储成字符串。

主要功能介绍如下：

1. 支持对表的数据捕获
- 支持对 DM 所有数据类型的捕获；
- 能够捕获指定的表的数据变化；
- 能够指定只捕获表中某些字段的数据变化；
- 能够捕获符合一定 WHERE 条件的数据变化（包括原来不符合条件，经修改后变成符合条件的记录；原来符合条件，经修改后变成不符合条件的记录）；
- 能够对捕获的字段进行计算或者函数转换，最终提供的是计算或转换后的值（视图不支持）；
- 能够给出变化数据记录的主键值（有主键时）或 ROWID 值；
2. 支持对视图的数据捕获
- 能够捕获指定的视图的数据变化；
- 视图的来源能够支持同一用户下多表联合，不同用户下多表联合；
- 支持除了大字段以外的，所有 DM 数据类型的捕获；

### 2.5.1 数据类型

1. **cpt\_col\_def\_struct**

**定义：**

```
STRUCT cpt_col_def_struct
{
SDBYTE name[129];
SDBYTE col_define[129];
SDBYTE expr[1024];
};
typedef struct cpt_col_def_struct cpt_col_def_t;
```

**功能说明：**

指定捕获的字段转成其他的类型进行存储，计算 expr 的值，并存储成 col\_define 的类型。

**参数说明：**

name：字段名称，必须与捕获对象字段一致。

col\_define：字段类型，该类型只有在表达式不为空时指定才有效，在指定 col\_define 时，要指定完整的定义，如 int，varchar(200)，numeric(10,2)。视图指定计算表达式时，该参数无效。

expr：字段表达式，如果为空串，则不做计算。视图指定表达时，允许用户指定各种表达式，如 C1+1，或者 cast 计算函数等。

2. **cpt\_error\_info\_struct**

**定义：**

```
struct cpt_error_info_struct

{

sdint4 error_no;

sdbyte error_info[DM_MAX_CPT_ERROR_INFO_LEN];

};

typedef struct cpt_error_info_struct cpt_error_info_t;
```

**功能说明：**

指定错误码。

**参数说明：**

error\_no：发生错误返回的 code 码。

error\_info：发生错误返回的信息。

### 2.5.2 相关方法

1. **dm\_create\_change\_data\_capture**

**定义：**

```
DMBOOL  DM_CREATE_CHANGE_DATA_CAPTURE(
##IF CPT_WITH_API
DHCON        CON_HDBC,
##ELSE
VOID *PIDAO_CONNECTION,   
##ENDIF   
SDBYTE*        SCHNAME,
SDBYTE*        TVNAME,
SDBYTE*        WHERES,
CPT_COL_DEF_T*    COL_DEFS,       
UDINT2        N_COLS,
SDBYTE*        CDC_ID,
UDINT4        CDC_ID_LEN,
SDBYTE*        CDC_BLOB_ID,
UDINT4        CDC_BLOB_ID_LEN,
CPT_ERROR_INFO_T* ERROR_INFO
);
```

**功能说明：**

打开数据捕获的 DPI 接口。

**参数说明：**

con\_hdbc：输入参数，数据库连接句柄。

pidao\_connection：输入参数，IDAO\_Connection 接口指针。

schname：输入参数，捕获对象所属模式，不允许使用带有下划线的模式名，否则会出现错误。

tvname：输入参数，捕获表/视图名。

wheres：输入参数，捕获条件，条件中需明确指定新值或旧值作为条件，若没有条件，则设为空串” ”。如何使用 where 条件？视图捕获，允许指定 where 条件，但是不允许指定新值旧值的指定，视图中没有没有这些概念。举例如下：

```
例1：监控C1列中，为20的数据变化（新值或者旧值为20）；
where 为：'C1 = 20'；
例2：监控C2列中，大于20同时小于60的值（新值旧值在区间(20,60)）；
where 为：'C2 > 20 and C2 < 60'；
例3：监控C1列中，旧值\>100的数据变化并且C2 为零的数据变化；
where 为：'OLD.C1 > 100 and C2 = 0'；
```

col\_defs：输入参数，字段描述。

n\_cols：输入参数，捕获字段数。n\_cols 和 col\_defs 必须一致，否则可能发生不可预知的错误

cdc\_id：输出参数，捕获请求标识，对应变化表名。

cdc\_id\_len：输入参数，标识缓冲区长度，建议需大于等于 129。

cdc\_blob\_id：输出参数，捕获请求标识，对应变化大字段表表名。

cdc\_blob\_id\_len：输入参数，大字段标识缓冲区长度，建议需大于等于 129。

error\_info：输出参数，操作产生错误的原因。

2. **dm\_drop\_change\_data\_capture**

**定义：**

```
DMBOOL  DM_DROP_CHANGE_DATA_CAPTURE(
##IF CPT_WITH_API
DHCON        CON_HDBC,
##ELSE
VOID *  PIDAO_CONNECTION,
##ENDIF
SDBYTE*        CDC_ID,
CPT_ERROR_INFO_T*  ERROR_INFO
);
```

**功能说明：**

关闭数据捕获的 DPI 接口。

**参数说明：**

con\_hdbc：输入参数，数据库连接句柄；

pidao\_connection：输入参数，IDAO\_Connection 接口指针；

cdc\_id： 输入参数，捕获表的名字，该表用于记录捕获的数据；

error\_info：输出参数，发生错误返回的错误信息。

3. **DM\_CPT\_SET\_LOCAL\_CODE**

**定义：**

```
VOID DM_CPT_SET_LOCAL_CODE(
        sdint4         code_id,
        sdint4          lang_id
);
```

**功能说明：**

修改数据捕获的语言信息。

**参数说明：**

CODE\_ID：输入参数，编码类型，暂时无效；

LANG\_ID：输入参数，语言类型，0 表示中文，1 表示英文。

### 2.5.3 数据信息搜集表

针对每个请求对象 T（表或者视图），创建一个对应的数据捕获表 CDC\_T\_ID，如果 T 的捕获字段包含大字段，还需要建立捕获从表 CDC\_BLOB\_T\_ID。

**(1) CDC\_T\_ID**

**定义：**

```
CREATE TABLE CDC_T_ID (
    OP_SEQ             BIGINT,
    OP_ROWID         ROWID,
    OPTYPE             CHAR(1),
    HAS_BLOB         CHAR(1),
    OP_time             TIMESTAMP,
    T表的主键值或ROW_ID BINARY(8),
    …
    OP_ERROR         VARchar(250)
);
```

**参数说明：**

OP\_SEQ：操作顺序；

OP\_ROWID：不管有没有主键值，都把 rowid 添加上；

OP\_TYPE：操作类型：'I'/'D'/'U'/'T'/'F'/'D'/'A'，分别表示：

- I: 插入一条符合条件的记录；
- U: 更新一条符合条件的记录为符合条件的记录；
- T: 更新一条不符合条件的记录为符合条件的记录；
- F: 更新一条符合条件的记录为不符合条件的记录；
- D: 删除一条符合条件的记录；
- A: 数据采集表被修改

HAS\_BLOB：是否有大字段：'Y'/'N'。

OP\_TIME：修改的时间；

T 表的主键值或 ROW\_ID：显示表的主键值，如果没有主键则显示 ROW\_ID。

OP\_ERROR：错误码

…：表示监控的字段；比如监控 C1，C2。则为 C1，C2 的定义，如：

```
C1 INT,
C2 VARCHAR(20);
```

**(2) CDC\_ BLOB\_T\_ID**

**定义：**

```
CREATE TABLE CDC_T_BLOB_ID(
    OP_SEQ             BIGINT,
    OP_ROWID        ROWID,
    COL_NAME        VARCHAR(128),
    OP_TIME            TIMESTAMP,
    T表的主键值或ROWID$        BIGINT
);
```

**参数说明：**

OP\_SEQ ：操作顺序；

OP\_ROWID：不管有没有主键值，都把 rowid 添加上；

COL\_NAME：大字段名；

OP\_TIME：修改的时间；

T 表的主键值或 ROWID$：显示表的主键值，如果没有主键则显示 rowid。

### 2.5.4 举例说明

第一步，初始化数据捕获环境。

```
SP_INIT_CPT_SYS(1) ;
```

第二步，创建要监控的表对象 T1。

```
create table t1(c1 int,c2 blob, c3 CHAR(10),c4 SMALLINT,primary key(c1));
insert into t1 values(1, 'a' , 'aB', 11);
commit;
```

第三步，在具体代码中调用 DPI 接口。通过调用数据捕获 DPI 接口，指定对具体对象、具体列的监控。

下面编写一段代码，通过调用数据捕获 DPI 接口，来实现对表 T1 中，所有列的监控。

```
#include "DPIext.h"
#include "DPI.h"
#include "DPItypes.h"
#include "dmcpt_dll.h"

dhenv    henv;        //环境句柄
dhcon    hdbc;        //连接句柄

dhcon get_hdbc(dhcon hdbc,dhenv    henv)
{
    //创建DPI运行环境
    //dpi_init();
    //申请一个环境句柄
    dpi_alloc_env(&henv);
    //申请一个连接句柄
    dpi_alloc_con(henv,&hdbc);
    //设置连接端口
    dpi_set_con_attr(hdbc, DSQL_ATTR_LOGIN_PORT, 5236, 0);
    //连接到本地服务器
    if (!DSQL_SUCCEEDED(dpi_login(hdbc,"192.168.0.38","SYSDBA","sysDBA*00")))
    {
        printf("connect failed!\n");
        //释放连接句柄
        dpi_free_con(hdbc);
        //释放环境句柄
        dpi_free_env(henv);
        exit(-1);
    }
    return hdbc;
}
void free_hdbc(dhcon hdbc,dhenv    henv)
{
    //断开与数据源之间的连接
    dpi_logout(hdbc);
    //释放连接句柄
    dpi_free_con(hdbc);
    //释放环境句柄
    dpi_free_env(henv);
    }

void test_cptview_case1()
{
    cpt_col_def_t* col_def;
    cpt_col_def_t* temp;
    char cdc_id[130] = "NULL";
    char cdc_blob_id[130]="NULL";
    cpt_error_info_t    ei;
    col_def=(cpt_col_def_t*)malloc(sizeof(cpt_col_def_t)*4);
    strcpy(col_def->name,"c1");
    strcpy(col_def->col_define,"");
    strcpy(col_def->expr,"");

    temp = col_def + 1;
    strcpy(temp->name,"c2");
    strcpy(temp->col_define,"");
    strcpy(temp->expr,"");

    temp = temp + 1;
    strcpy(temp->name,"c3");
    strcpy(temp->col_define,"");
    strcpy(temp->expr,"");

    temp =  temp + 1;
    strcpy(temp->name,"c4");
    strcpy(temp->col_define,"");
    strcpy(temp->expr,"");

    hdbc=get_hdbc(hdbc, henv);  
    dm_create_change_data_capture(hdbc,"SYSDBA","T1","",col_def,4,cdc_id,130,cdc_blob_id,130, &ei);
    printf("cdc_id:%s\n",cdc_id);
    printf("cdc_blob_id:%s\n",cdc_blob_id);
    printf("%s\n",ei.error_info);
    //可以在此改变表中的数据，
    //手动在客户端查询打印出的cdc_id和cdc_blob_id表名，监控开启捕获后，T1表中数据的变化。
    //dm_drop_change_data_capture(hdbc,cdc_id, &ei);可以在此处关闭DPI接口。因为本例需要后面查看查看捕获表，所以不关闭。
    free_hdbc(hdbc, henv);
}
void main()
{
    test_cptview_case1();
    system("pause");
}
```

第四步，在数据捕获的窗口中，查看打印出的 cdc\_id 和 cdc\_blob\_id。

```
cdc_id:CPT_SYSDBA_T1_82118833738749
cdc_blob_id:CPT_SYSDBA_T1_82118833738749_BLOB
```

第五步，对具体对象进行操作。通过 disql 等客户端来改变表中的数据。

```
insert into t1 values(2, 'B', 'BC', 22);
insert into t1 values(3, 'C', 'CD', 33);
insert into t1 values(4, 'D', 'DE', 44);
```

第六步，查看数据捕获表。通过 disql 等客户端来查看 cdc\_id 和 cdc\_blob\_id 表中的数据。

cdc\_id 表：

```
select * from CPT_SYSDBA_T1_82118833738749;
```

查询结果如下：

```
行号       OP_SEQ               OP_ROWID           OPTYPE HAS_BLOB OP_TIME                    C1          C3         C4          OP_ERROR
---------- -------------------- ------------------ ------ -------- -------------------------- ----------- ---------- ----------- --------
1          1                    AAAAAAAAAA//////// I      Y        2023-04-06 16:45:10.000000 2           BC         22          NULL
2          2                    AAAAAAAAAA//////// I      Y        2023-04-06 16:45:10.000000 3           CD         33          NULL
3          3                    AAAAAAAAAA//////// I      Y        2023-04-06 16:45:10.000000 4           DE         44          NULL
```

cdc\_blob\_id 表：

```
select * from CPT_SYSDBA_T1_82118833738749_BLOB;
```

查询结果如下：

```
行号       OP_SEQ               OP_ROWID           COL_NAME OP_TIME                    C1
---------- -------------------- ------------------ -------- -------------------------- -----------
1          1                    AAAAAAAAAAAAAAAAAC C2       2023-04-06 16:45:10.000000 2
2          2                    AAAAAAAAAAAAAAAAAD C2       2023-04-06 16:45:10.000000 3
3          3                    AAAAAAAAAAAAAAAAAE C2       2023-04-06 16:45:10.000000 4
```

第七步，结束的时候，关闭数据捕获的环境。

```
SP_INIT_CPT_SYS(0);
```
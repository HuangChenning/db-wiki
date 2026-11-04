---
title: "DM FLDR 编程指南"
book: "DM8 程序员手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/fldr-rogramming-guide.html
tags:
  - dameng
  - dm8
  - programmer
---

## 7.1 C 编程指南

### 7.1.1 接口介绍

快速装载接口 FLDR 是达梦数据库提供的能够快速将文本数据载入 DM 数据库的一种数据载入方式。用户通过使用 FLDR 接口能够把按照一定格式排序的文本数据以简单、快速、高效的方式载入到达梦数据库中。

本节介绍的为 FLDR 的 C 接口。

### 7.1.2 接口说明

#### 7.1.2.1 返回值说明

DM FLDR 接口有以下五种返回值：

FLDR\_SUCCESS：接口成功执行；

FLDR\_ERROR：接口执行出错；

FLDR\_INVALID\_HANDLE：用户使用错误的句柄；

FLDR\_SUCCESS\_WITH\_INFO：接口执行成功但有警告信息；

FLDR\_NO\_DATA：数据未找到。

#### 7.1.2.2 接口说明

1. **fldr\_alloc**

**描述**

用于分配快速装载对象实例，所有快速装载都将通过该句柄进行操作。

**格式**

```
FLDR_RETURN 
fldr_alloc(
    fhinstance         *instance
);
```

**参数**

instance（输出）：快速装载实例的句柄

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR。

**说明**

该函数分配出用于快速装载实例句柄，用户必须首先调用该函数获得快速装载的实例句柄，只有通过该句柄才能进行后续的快速装载操作。

2. **fldr\_free**

**描述**

释放快速装载实例句柄。

**格式**

```
FLDR_RETURN 
fldr_free(
    fhinstance         instance
);
```

**参数**

instance（输入）：快速装载实例的句柄。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

释放快速装载实例句柄，将该实例句柄上所有快速装载所占用的资源释放。

如果用户调用 fldr\_initialize 进行初始化，而没有调用 fldr\_uninitialize 通知装载结束，调用此函数将会自动结束该此装载，未使用 fldr\_batch 或者 fldr\_finish 进行提交的行将会被抛弃。

3. **fldr\_set\_attr**

**描述**

设置快速装载实例的属性。

**格式**

```
FLDR_RETURN 
fldr_set_attr(
    fhinstance         instance, 
    fsint4           attrid, 
    fpointer         value, 
    fsint4           length
);
```

**参数**

instance（输入）：快速装载实例的句柄。

attrid（输入）：属性。关于属性详细内容请参考表 7.1 属性介绍。

value（输入）：属性值。

length（输入）：属性值占用的空间大小，value 类型为字符串时使用。value 类型为整数时，该参数无意义。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

该函数可在调用 fldr\_initialize 之前调用，用户可根据本地及服务器的环境特征设置本次快速装载的属性，从而获得较高的效率。

在 fldr\_initialize 之后对该函数进行调用将返回执行不成功的错误。

表7.1 属性介绍

| **属性（attrid）** | **属性说明（value）** | **value 类型** |
| --- | --- | --- |
| FLDR\_ATTR\_SERVER | 服务器 IP 地址。缺省情况下为本地服务器 LOCALHOST | 字符串 |
| FLDR\_ATTR\_UID | 用户名。不能缺省 | 字符串 |
| FLDR\_ATTR\_PWD | 密码。不能缺省 | 字符串 |
| FLDR\_ATTR\_PORT | 服务器端口。缺省情况下端口号为 5236 | 整数 |
| FLDR\_ATTR\_TABLE | 目标表 | 字符串 |
| FLDR\_ATTR\_SET\_INDENTITY | 是否插入自增列。1 是，服务器将使用指定的数据作为自增列的数据进行插入；0 否，对于自增列服务器将自动生成数据插入，忽略指定的数据。缺省为 0 | 整数 |
| FLDR\_ATTR\_DATA\_SORTED | 数据是否已按照聚集索引排序。缺省为 0。 1 表示用户必须保证数据已按照聚集索引排序完成，并且如果表中存在数据，需要插入的数据索引值要比表中数据的索引值大，服务器在做插入操作时顺序进行插入。0 表示服务器对于每条记录进行定位插入 | 整数 |
| FLDR\_ATTR\_INDEX\_OPTION | 索引的设置选项，缺省为 1。 1：不刷新二级索引，数据按照索引先排序，装载完后再将排序的数据插入索引； 2：不刷新二级索引，数据装载完成后重建所有二级索引； 3：刷新二级索引，数据装载的同时将数据插入二级索引 | 整数 |
| FLDR\_ATTR\_INSERT\_ROWS | 只读属性。当前发送到服务器的行数 | 整数 |
| FLDR\_ATTR\_COMMIT\_ROWS | 只读属性。当前提交到数据库的行数 | 整数 |
| FLDR\_ATTR\_PROCESS\_ROWS | 只读属性。用户绑定的数据行数 | 整数 |
| FLDR\_ATTR\_SEND\_NODE\_NUM | 指定数据载入时发送节点的个数，默认由系统计算一个初始值。取值范围为 16~65535。若在数据载入时发现发送节点不够用，系统会动态增加分配。在系统内存足够的情况下，可以适当设大 SEND\_NODE\_NUMBER 值，提升 dmfldr 载入性能 | 整数 |
| FLDR\_ATTR\_TASK\_THREAD\_NUM | 指定数据载入时处理用户数据的线程数目。默认情况下，dmfldr 将该参数值设为系统 CPU 的个数。在 dmfldr 客户端所在机器 CPU 大于 8 环境中，提高 TASK\_THREAD\_NUMBER 值可以提升 dmfldr 装载性能。取值范围为 1~128 | 整数 |
| FLDR\_ATTR\_BAD\_FILE | 记录错误数据的文件绝对路径。缺省为 dmfldr.exe 所在目录。缺省的错误文件名为 fldr.bad。文件记录的信息为数据文件中存在格式错误的行数据以及转换出错的行数据 | 字符串 |
| FLDR\_ATTR\_DATA\_CHAR\_SET | 数据文件中数据的编码格式。默认与当前机器编码格式一致。参数取值为 1 表示国际编码 UTF-8，为 2 表示中文编码 GBK，为 6 表示韩文字符集 EUC-KR，为 9 表示单字节字符编码 SINGLE\_BYTE，为 10 表示中文编码 GB18030 | 整数 |
| FLDR\_ATTR\_LOG\_FILE | 指定日志文件绝对路径，缺省为 dmfldr.exe 所在目录。缺省日志文件名为 fldr.log。日志文件记录了 dmfldr 运行过程中的工作信息、错误信息以及统计信息 | 字符串 |
| FLDR\_ATTR\_ERRORS\_PERMIT | 允许出现错误数据的行数，超过该值装载将报错。取值范围为 0~4294967295，缺省为 100 | 整数 |
| FLDR\_ATTR\_SSL\_PATH | 通信加密的 SSL 数字证书路径，缺省为不使用加密。数字证书路径由用户自己创建，将相应的证书需放入该文件夹中。其中服务器证书必须与 dmserver 目录同级，客户端目录可以任意设置 | 字符串 |
| FLDR\_ATTR\_SSL\_PWD | 通信加密的 SSL 数字证书密码。和 ssl\_path 一起使用 | 字符串 |
| FLDR\_ATTR\_LOCAL\_CODE | 指定本地字符集。取值为 1 表示 UTF-8，2 表示 GBK，3 表示 BIG5，4 表示 ISO 8859 9，5 表示 EUC JP，6 表示 EUC KR，7 表示 KOI8R，8 表示 ISO 8859 1，9 表示 ASCII，10 表示 GB18030，11 表示 ISO 8859 11。缺省值是本地编码 | 整数 |
| FLDR\_ATTR\_NULL\_MODE | 指定载入数据时对 NULL 字符串和空值的处理方式。取值 1 和 0，缺省为 0。 1 表示数据载入时将 NULL 字符串处理为空值，数据导出时则空值处理为 NULL 字符串；0 表示数据载入时将 NULL 字符串处理为字符串 | 整数 |
| FLDR\_ATTR\_SERVER\_BLDR\_NUM | 水平分区表装载时，指定服务器 BLDR 的最大个数，整数类型，取值范围为 1～1024，缺省为 64。 服务器的 BLDR 保存水平分区子表相关信息，BLDR\_NUM 的设置也就指定了服务器能同时载入的水平分区子表的个数 | 整数 |
| FLDR\_ATTR\_BDTA\_SIZE | BDTA（Batch DaTA）的大小，整数类型，取值范围为 100~10000，缺省为 5000。 BDTA 代表 DM 数据库批量数据处理机制中一个批量，在内存、CPU 允许的条件下，增大 BDTA\_SIZE 能加快装载速度；在网络是装载性能瓶颈时，增大 BDTA\_SIZE 影响不大 | 整数 |
| FLDR\_ATTR\_COMPRESS\_FLAG | 指定是否压缩 BDTA。1 是；0 否。缺省为 0。 压缩 BDTA 能节省网络带宽，但同时也会加重 CPU 的负担，用户应根据具体应用情况考虑是否制定压缩 | 整数 |
| FLDR\_ATTR\_FLUSH\_FLAG | 指定提交数据时服务器的处理方式。若设置为 1 则服务器将数据写入磁盘后才返回响应消息；若设置为 0 则服务器确认数据正确即返回响应消息，之后才将数据写入磁盘。缺省为 0 | 整数 |
| FLDR\_ATTR\_MPP\_CLIENT | 当服务器环境为 MPP 环境时，若此参数值为 1，为客户端分发模式，数据在 FLDR 客户端分发好后直接往指定站点发送数据；若此参数值为 0，为本地分发模式，FLDR 客户端将数据全部发往连接的 MPP EP 站点。缺省值为 1 | 整数 |
| FLDR\_ATTR\_DATA\_PATH | 指定数据文件路径 | 字符串 |
| FLDR\_ATTR\_BUFFER\_SIZE | 指定读取文件缓冲区的页大小。取值范围为 1~2048，缺省为 10。单位为 MB | 整数 |
| FLDR\_ATTR\_LOB\_DIRECTORY | 指定 dmfldr 使用的大字段数据存放的目录 | 字符串 |
| FLDR\_ATTR\_LOB\_FIL\_NAME | 指定 dmfldr 导出大字段数据的文件名。缺省为 dmfldr.lob | 字符串 |
| FLDR\_ATTR\_BLOB\_TYPE | 指定 BLOB 数据值的实际类型。取值：1 表示值为十六进制；0 表示值为十六进制字符。缺省为 0 | 整数 |
| FLDR\_ATTR\_ENABLE\_CLASS\_TYPE | 指定是否以 BLOB 方式导入导出 CLASS 类型列数据。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_CONFLICT\_FLAG | 指定是否忽略唯一性冲突。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_RECONN | 指定自动重连次数。取值范围为 0~4294967295，缺省为 0，表示不进行自动重连 | 整数 |
| FLDR\_ATTR\_RECONN\_TIME | 指定自动重连等待时间。取值范围为 1~10000，缺省为 5。单位为秒 | 整数 |
| FLDR\_ATTR\_ERROR\_ROWS | 只读属性。装载错误行数 | 整数 |
| FLDR\_ATTR\_SKIP\_ROWS | 初始忽略逻辑行数，缺省为 0 | 整数 |
| FLDR\_ATTR\_LOAD\_ROWS | 需要装载的行数，默认装载全部行数 | 整数 |
| FLDR\_ATTR\_READ\_ROWS | 工作线程一次最大处理的行数，缺省为 100000，最大支持 2^26-10000 | 整数 |
| FLDR\_ATTR\_DIRECT\_MODE | 是否使用快速方式装载。0 否；1 是。缺省值为 1 | 整数 |
| FLDR\_ATTR\_ROWS\_COMMIT | 提交频次。取值范围 1~2147483647，缺省值为 50000。当 FLDR\_ATTR\_DIRECT\_MODE 为 0 时有效 | 整数 |
| FLDR\_ATTR\_LOAD\_MODE | 装载方式。1：表示载入；2：表示载出；3：表示载出 ORACLE。缺省值为 1 | 整数 |
| FLDR\_ATTR\_SILENT | 是否以静默方式装载数据。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_OCI\_DIRECTORY | OCI 动态库所在的目录 | 字符串 |
| FLDR\_ATTR\_CLIENT\_LOB | 大字段目录是否在本地。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_IGNORE\_BATCH\_ERRORS | 是否忽略错误数据继续导入。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_NULL\_STR | 载入时视为 NULL 值处理的字符串 | 字符串 |
| FLDR\_ATTR\_SINGLE\_HLDR\_HP | 是否使用单个 HLDR 装载 HUGE 水平分区表。0 否；1 是。缺省值为 1 | 整数 |
| FLDR\_ATTR\_EP | 指定需要发送数据的站点序号列表，仅向 MPP/DPC 环境导入数据时有效 | 字符串 |
| FLDR\_ATTR\_SINGLE\_FILE | MPP/DPC 环境下，是否只生成单个数据文件。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_LAN\_MODE | MPP/DPC 环境下，是否以内网模式装载数据。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_CNVT\_MODE | 非法字符处理选项，为 0 时表示跳过该数据行，为 1 时表示使用(\*)替换错误字节；缺省为 0 | 整数 |
| FLDR\_ATTR\_PARALLEL | 是否开启并行装载。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_SQL | 使用自定义查询语句，仅导出模式有效 | 字符串 |
| FLDR\_ATTR\_LOG\_SIZE | 日志信息缓冲区的大小，单位 MB，有效值范围 1~100；缺省为 1 | 整数 |
| FLDR\_ATTR\_COMMIT\_OPTION | 提交选项，0：每发送一批数据后提交，1：发送完所有数据后提交；缺省为 0 | 整数 |
| FLDR\_ATTR\_APPEND\_OPTION | 追加选项，0：追加方式，1：替代方式，2：插入方式；缺省为 0 | 整数 |
| FLDR\_ATTR\_COLNAME\_HEADING | 是否在导出文件头中打印列名。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_IGNORE\_AIMLESS\_DATA | 是否忽略无目标数据。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_LOB\_AS\_VARCHAR | 是否将 CLOB 作为 VARCHAR 进行导入导出。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_LOB\_AS\_VARCHAR\_SIZE | 将 CLOB 作为 VARCHAR 进行导入导出时，lob 数据最大大小，缺省为 10MB | 整数 |
| FLDR\_ATTR\_LOG\_LEVEL | 记录错误数据信息级别，0：不记录，1：只记录到 log 文件；2：只记录到 bad 文件；3：记录到 log 和 bad 文件；4：错误仅输出到屏幕；缺省为 3 | 整数 |
| FLDR\_ATTR\_WIDTH | 设置列数据宽度 | 整数 |
| FLDR\_ATTR\_SQLFILE | 自定义查询语句所在文件，仅导出模式有效 | 字符串 |
| FLDR\_ATTR\_PRIORITY\_ENCLOSE | DB2 模式下，是否 enclose 优先级最高。0 否；1 是。缺省值为 0 | 整数 |
| FLDR\_ATTR\_EXPORT\_MODE | MPP/DPC 环境，使用 SQL 语句时的导出模式，0：普通模式；1：快速模式，LOCAL 方式连接；2：缓存模式，即 FLDR\_EXPORT\_MODE\_BUFFER 模式，仅在调用 fldr 接口时可设置。缺省为 0 | 整数 |
| FLDR\_ATTR\_BAD\_FILE\_MODE | 错误数据文件模式，0：普通模式；1：纯数据模式；缺省为 0 | 整数 |
| FLDR\_ATTR\_PLOG\_FILE | ldrp 日志文件，缺省为 ldrp.log | 字符串 |
| FLDR\_ATTR\_COMPATIBLE\_MODE | 兼容模式，0：不做兼容；1：兼容 DB2；2：兼容 MYSQL；缺省为 0 | 整数 |
| FLDR\_ATTR\_OUT\_FILE\_ROWS | 导出模式下，每个导出文件中数据的最大行数，取值范围 0~999999999，缺省为 0 | 整数 |
| FLDR\_ATTR\_OUT\_FILE\_SIZE | 导出模式下，每个导出文件的最大大小，单位 KB，取值范围 0~4194303，缺省为 0 | 整数 |

4. **fldr\_get\_attr**

**描述**

获取快速装载实例的属性。

**格式**

```
FLDR_RETURN 
fldr_get_attr(
    fhinstance           instance, 
    fsint4            attrid, 
    fpointer        buffer, 
    fsint4            buf_sz,
    fsint4*            length
);
```

**参数**

instance（输入）：快速装载实例的句柄。

attrid（输入）：属性标识，指出将要获取的属性，关于属性详细内容参见 fldr\_set\_attr()的说明部分。

buffer（输出）：将属性值填入 buffer 所指向的内存中。

buf\_sz（输入）：属性缓冲区的长度。

length（输出）：向 buffer 指向的缓冲区填写的数据的长度。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

参见 fldr\_set\_attr()函数说明中各属性说明。

5. **fldr\_initialize**

**描述**

初始化当前快速装载实例。

**格式**

```
FLDR_RETURN 
fldr_initialize(
    fhinstance           instance, 
    fsint4              type,
    fpointer           conn,
    fchar*            server, 
    fchar *            uid, 
    fchar*            pwd,
    fchar*            table
);
```

**参数**

instance（输入）：快速装载实例的句柄。

type（输入）：数据装载类型，可取的值如下：

- FLDR\_TYPE\_BIND 用户使用绑定方式进行装载。一般用于接口，如 dci、odbc 等；
- FLDR\_TYPE\_TEXT\_STREAM 已经废弃；
- FLDR\_TYPE\_CTRL 已经废弃；
- FLDR\_TYPE\_JNI 通过调用 fldr 接口进行装载，会设置 silent=true，主要用于 jni、dts；
- FLDR\_TYPE\_JNI\_FILE 通过调用 fldr 的 fldr\_exec\_ctl\_low 接口进行装载使用, 因为 fldr\_initialize 作为 fldr 接口会对表对象上锁，而 fldr\_exec\_ctl\_low 作为 fldr 命令行工具的入口，也会对表进行锁操作；因此只有通过设置为该类型后，才可以使用 fldr\_exec\_ctl\_low 接口；
- FLDR\_TYPE\_FODBC 供 odbc 使用；
- FLDR\_TYPE\_DIMP 供逻辑导入工具使用；
- FLDR\_TYPE\_DEFAULT 用于非使用接口的场景，直接使用命令行工具的场景。

conn（输入）：通过 dpi 分配的连接对象，如果该参数不为 NULL 值，则使用用户指定的连接作为导入的连接，忽略 server、uid、pwd 这三个参数。

server（输入）：链接的服务器。将被记录到实例的 FLDR\_ATTR\_SERVER 属性中。

uid（输出）：登录用户。将被记录到实例的 FLDR\_ATTR\_UID 属性中。

pwd（输入）：用户密码。将被记录到实例的 FLDR\_ATTR\_PWD 属性中。

table（输入）：进行快速装载的表。将被记录到实例的 FLDR\_ATTR\_TABLE 属性中。

**返回值**

FLDR\_SUCCESS、FLDR\_SUCCESS\_WITH\_INFO、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

根据用户通过 fldr\_set\_attr 设置的属性初始化快速装载环境，如果用户未指定连接则根据用户提供的服务器、用户和密码建立到服务器的连接。

6. **fldr\_uninitialize**

**描述**

释放快速装载实例所占用的资源。

**格式**

```
FLDR_RETURN 
fldr_uninitialize(
    fhinstance         instance,
    fsint4            flag
);
```

**参数**

instance（输入）：快速装载实例的句柄。

flag（输入）：指出是否对已插入的数据进行事务提交，以永久保存到数据库。取值：FLDR\_UNINITILIAZE\_COMMIT 为是，FLDR\_UNINITILIAZE\_ROLLBACK 为否。如果用户调用了 fldr\_finish 结束导入则该参数将不会起任何作用。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

仅在调用过 fldr\_initialize 后使用，未初始化调用或重复调用将会报错。用户在调用该函数后可重新初始化快速装载句柄，进行新的数据装载。

7. **fldr\_bind**

**描述**

绑定输入列。

**格式**

```
FLDR_RETURN 
fldr_bind(
    fhinstance           instance,
    fsint2            col_idx,
    fsint2            type,
    fchar*            date_fmt,
    fpointer        data,
    fsint4            col_len,
    fsint4*           ind_len
);
```

**参数**

instance（输入）：快速装载实例的句柄。

col\_idx（输入）：绑定列的编号。从 1 开始计数，对应快速装载的表的相应列。

type（输入）：用户绑定数据的 C 类型。

date\_fmt（输入）：当绑定列对应的表的列为时间日期类型，且绑定的 c 数据为 FLDR\_C\_CHAR 类型，该参数为字符串到日期类型的格式串。其他情况，忽略该绑定输入。

data（输入）：指向用于存放数据内存的地址指针，可在 fldr\_sendrows 之前对其进行填充，快速装载接口在用户调用 fldr\_sendrows 时读取数据内容。

col\_len（输入）：列定义长度。

ind\_len（输入）：用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向 fsint4 类型的数组。如果地址中保存的值为 FLDR\_DATA\_NULL，绑定列的该行数据被视为空值。对于 FLDR\_C\_BINARY 和 FLDR\_C\_CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

支持绑定的 C 类型见下表：

| 类型 | 宏定义 | 说明 |
| --- | --- | --- |
| 二进制数据 | FLDR\_C\_BINARY | 变长 |
| 字符数据 | FLDR\_C\_CHAR | 变长 |
| 1 字节整型数据 | FLDR\_C\_BYTE | 定长 |
| 2 字节整型数据 | FLDR\_C\_SHORT | 定长 |
| 4 字节整型数据 | FLDR\_C\_INT | 定长 |
| 8 字节整型数据 | FLDR\_C\_BIGINT | 定长 |
| 单精度浮点数 | FLDR\_C\_FLOAT | 定长 |
| 双精度浮点数 | FLDR\_C\_DOUBLE | 定长 |

8. **fldr\_bind\_nth**

**描述**

绑定输入列，fldr\_bind 的多线程版本。

**格式**

```
FLDR_RETURN 
fldr_bind_nth(
    fhinstance        instance,
    fsint2          col_idx,
    fsint2            type,
    fchar*          date_fmt,
    fpointer        str_binds,
    fpointer        data,
    fsint4          col_len,
    fsint4          data_len,
    fsint4*         ind_len,
    fsint4          nth
);
```

**参数**

instance（输入）：快速装载实例的句柄。

col\_idx（输入）：绑定列的编号。从 1 开始计数，对应快速装载的表的相应列。

type（输入）：用户绑定数据的 C 类型。

date\_fmt（输入）：当绑定列对应的表的列为时间日期类型，且绑定的 c 数据为 FLDR\_C\_CHAR 类型，该参数为字符串到日期类型的格式串。其他情况，忽略该绑定输入。

str\_binds（输入）：字符串绑定内存。

data（输入）：指向用于存放数据内存的地址指针，可在 fldr\_sendrows 之前对其进行填充，快速装载接口在用户调用 fldr\_sendrows 时读取数据内容。

col\_len（输入）：列定义长度。

data\_len（输入）：用于记录单行数据最大的长度。当进行多行绑定的时候，对于变长的 C 类型，根据该参数内容进行便宜的计算。对于固定长度的 C 数据类型，该参数内容被忽略。

ind\_len（输入）：用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向 fsint4 类型的数组。如果地址中保存的值为 FLDR\_DATA\_NULL，绑定列的该行数据被视为空值。对于 FLDR\_C\_BINARY 和 FLDR\_C\_CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

nth（输入）：多线程绑定，第几个线程，从 0 开始。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

支持绑定的 C 类型见下表：

| 类型 | 宏定义 | 说明 |
| --- | --- | --- |
| 二进制数据 | FLDR\_C\_BINARY | 变长 |
| 字符数据 | FLDR\_C\_CHAR | 变长 |
| 1 字节整型数据 | FLDR\_C\_BYTE | 定长 |
| 2 字节整型数据 | FLDR\_C\_SHORT | 定长 |
| 4 字节整型数据 | FLDR\_C\_INT | 定长 |
| 8 字节整型数据 | FLDR\_C\_BIGINT | 定长 |
| 单精度浮点数 | FLDR\_C\_FLOAT | 定长 |
| 双精度浮点数 | FLDR\_C\_DOUBLE | 定长 |

9. **fldr\_sendrows**

**描述**

发送行数。

**格式**

```
FLDR_RETURN 
fldr_sendrows(
    fhinstance         instance,
    fsint4            rows
);
```

**参数**

instance（输入）：快速装载实例的句柄。

rows（输入）：在多行绑定的情况，指明绑定的行数。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

10. **fldr\_sendrows\_nth**

**描述**

发送行数，fldr\_sendrows 的多线程版本。

**格式**

```
FLDR_RETURN 
fldr_sendrows_nth(
    fhinstance        instance,
    fsint4          rows,
    fsint4          nth,
    fsint4          seq_no
);
```

**参数**

instance（输入）：快速装载实例的句柄。

rows（输入）：在多行绑定的情况，指明绑定的行数。

nth（输入）：多线程版本，第几个线程。

seq\_no（输入）：数据批次的序号。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

11. **fldr\_batch**

**描述**

批量提交行数据，永久保存到服务器。

**格式**

```
FLDR_RETURN 
fldr_batch(
    fhinstance         instance,
    fsint8           *rows
);
```

**参数**

instance（输入）：快速装载实例的句柄。

rows（输出）：批量提交的行数。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

**说明**

将上一次调用 fldr\_batch 之后所有 fldr\_sendrows 装载的行进行提交，永久保存到数据库中。

12. **fldr\_finish**

**描述**

结束一次批量操作。仅在调用过 fldr\_initialize 后使用，未初始化调用将会报错。

**格式**

```
FLDR_RETURN 
fldr_finish(
    fhinstance         instance
);
```

**参数**

instance（输入）：快速装载实例的句柄。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE。

13. **fldr\_get\_diag**

**描述**

获取出错时的诊断信息。

**格式：**

```
FLDR_RETURN 
fldr_get_diag(
    fhinstance           instance,
    fsint4            rec_num,
    fsint4*         err_code,
    fchar*             err_msg,
    fsint4          buf_sz,
    fsint4*         msg_len
);
```

**参数**

instance（输入）：快速装载实例的句柄。

rec\_num（输入）：诊断信息索引号。

err\_code（输出）：发生错误的错误码。

err\_msg（输出）：错误消息缓冲区。

buf\_sz（输入）：缓冲区大小。

msg\_len（输出）：错误信息在缓冲区中占用的大小。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR、FLDR\_INVALID\_HANDLE、FLDR\_NO\_DATA。

**说明**

当用户调用快速装载接口返回 FLDR\_ERROR 时，可通过该函数获取出错的错误信息，进行当前状况的判断。该函数出现错误将不会生成任何诊断信息。

14. **fldr\_exec\_ctl\_low**

**描述**

类似命令行工具，通过控制文件，执行数据装载。

该接口与接口 fldr\_initialize 的操作（包括连接服务器、为装载表上锁等）存在一定冲突。在调用 fldr\_initialize 后调用 fldr\_exec\_ctl\_low 时，需指定 fldr\_type 为 FLDR\_TYPE\_JNI\_FILE。由于 fldr\_initialize 并非为必要使用的，当未调用 fldr\_initialize 时，可以通过 fldr\_set\_attr 来设置 server、user、password、table 等信息，而后使用 fldr\_exec\_ctl\_low 来进行装载，这种情况下，fldr\_type 需指定为 FLDR\_TYPE\_DEFAULT。另外，若使用 fldr\_exec\_ctl\_low 进行数据导出时，如果调用 fldr\_initialize，则必须在调用 fldr\_initialize 前，通过 fldr\_set\_attr 来设置 load\_mode 为导出模式，否则 fldr\_initialize 将认为是默认导入模式，并依照导入模式规范进行部分初始化操作，此时可能引发与导出预期不符的情况。

**格式**

```
FLDR_RETURN
fldr_exec_ctl_low(
    fhinstance      instance,
    fchar*          ctl_buffer,
    fsint4          fldr_type,
    fsint8*         row_count   
);
```

**参数**

instance（输入）：快速装载实例的句柄。

ctl\_buffer（输入）：控制文件 buffer。

fldr\_type（输入）：数据装载类型。具体取值与对应说明请参考接口 5.fldr\_initialize 参数 type 的说明。

row\_count（输出）：返回成功装载的行数。仅支持载入行数，不支持载出行数。

**返回值**

FLDR\_SUCCESS、FLDR\_ERROR。

**说明**

此接口让用户可以通过自定义程序实现数据快速装载。

15． **fldr\_get\_statistic**

**描述**

获取当前完成的装载的统计结果。

**格式**

```
FLDR_RETURN 
fldr_get_statistic(
    fhinstance      instance,
    fsint8*         suc_num,
    fsint8*         dis_num,
    fsint8*         err_num
);
```

**参数**

instance（输入）：快速装载实例的句柄。

suc\_num（输出）：快速装载成功数据的行数（载出时为载出成功的行数）。

dis\_num（输出）：快速装载丢弃数据的行数（载出时为载出丢弃的行数）。

err\_num（输出）：快速装载失败数据的行数（载出时为 0）。

**返回值**  
FLDR\_SUCCESS、FLDR\_INVALID\_HANDLE。

**说明**

用户可以通过本接口获取当前装载的统计结果。

16. **fldr\_fetch\_data**

**描述**

在 FLDR\_EXPORT\_MODE\_BUFFER 导出模式下, 取数据使用。

**格式**

```
FLDR_RETURN
fldr_fetch_data(
    fhinstance          instance,  
    void*               node_handle,  
    fchar*              data,   
    fsint4              data_len   
);
```

**参数**

instance（输入）：快速装载实例的句柄。

node\_handle（输入）：导出节点句柄。

data（输入）：导出数据空间地址。

data\_len（输入）：导出数据空间大小。

**返回值**

FLDR\_SUCCESS、 FLDR\_INVALID\_HANDLE、FLDR\_ERR\_OUT\_OF\_MEM、 FLDR\_ERROR。

17.**fldr\_export**

**描述**

在 FLDR\_EXPORT\_MODE\_BUFFER 导出模式下, 导出数据接口。

**格式**

```
FLDR_RETURN
fldr_export(
    fhinstance          instance,  
    fchar*              ctl_buf  
)
```

**参数**

instance（输入）：快速装载实例的句柄。

ctl\_buf（输入）：控制文件内容。

**返回值**

FLDR\_SUCCESS、 FLDR\_INVALID\_HANDLE、FLDR\_ERR\_OUT\_OF\_MEM、 FLDR\_ERR\_NOT\_SUPPORTED、FLDR\_ERROR。

18.**fldr\_fetch\_data\_len**

**描述**

在 FLDR\_EXPORT\_MODE\_BUFFER 导出模式下, 取数据前获取数据长度。

**格式**

```
FLDR_RETURN
fldr_fetch_data_len(
    fhinstance          instance,   
    void**              node_handle,  
    fsint4*             data_len  
);
```

**参数**

instance（输入）：快速装载实例的句柄。

node\_handle（输出）：导出节点句柄。

data\_len（输出）：导出数据大小。

**返回值**

FLDR\_SUCCESS、 FLDR\_INVALID\_HANDLE、 FLDR\_ERROR。

### 7.1.3 基本示例

程序在编译的过程中需要用到 DM 的头文件 fldr.h，在连接阶段需要用到 dmfldr\_dll.lib 这个库文件，在执行阶段需要用到动态库 dmfldr\_dll.dll、dmbcast.dll、dmcalc.dll、dmelog.dll、dmmem.dll、dmos.dll、dmutl.dll、dmdta.dll、dmcfg.dll、dmstrt.dll、dmcpr.dll、dmcyt.dll、dmcvt.dll、dmmout.dll、dmcomm.dll、dmdpi.dll、dmclientlex.dll、dmfldr\_comm.dll。这几个动态库在安装 DM 时，已经被放到安装目录下。

例 1 一个基本的示例。

```
#include "fldr.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main()
{
    fhinstance      instance;
    FLDR_RETURN     ret;
    char            server[20] = "192.168.0.35";
    char            user[20] = "SYSDBA";
    char            pwd[20] = "sysDBA*00";
    char            table[20] = "TEST";   
// 提前建好表CREATE TABLE TEST(C1 INT, C2 VARCHAR2(100));
    int             c1[100];
    int             c1_len[100];
    char            c2[100][100];
    int             c2_len[100];
    int             i;

    for (i = 0; i < 100; i++)
    {
        c1[i]   = i;
        sprintf(c2[i], "i = %d", i);
        c2_len[i] = strlen(c2[i]);
    }

    ret = fldr_alloc(&instance);  
    fldr_set_attr(instance, FLDR_ATTR_PORT, (fpointer)5236, 0);
    fldr_initialize(instance, FLDR_TYPE_BIND, NULL, (fchar*)server, (fchar*)user, (fchar*)pwd, (fchar*)table);
    fldr_bind_nth(instance, 1, FLDR_C_INT, NULL, NULL, c1, 4, 0, c1_len, 0);
    fldr_bind_nth(instance, 2, FLDR_C_CHAR, NULL, NULL, c2, 100, 100*100, c2_len, 0);
    fldr_sendrows_nth(instance, 100, 0, 1);  
    fldr_uninitialize(instance, FLDR_UNINITILIAZE_COMMIT);
    fldr_free(instance);
    return 0;
}
```

例 2 缓存模式下的数据导出。

```
#include "fldr.h"
#include <iostream>

int main()
{
    fhinstance  instance = NULL;
    FLDR_RETURN    rt = FLDR_SUCCESS;
    char    server[20] = "localhost", 
            uid[20] = "SYSDBA",
            pwd[20] = "SYSDBA";
    fchar                    ctl_buf[1024];
    fsint8                    row_count;
    
    rt = fldr_alloc(&instance);
    rt = fldr_set_attr(instance, FLDR_ATTR_SERVER, server, strlen(server));
    rt = fldr_set_attr(instance, FLDR_ATTR_PORT, (fpointer)10111, 0);
    rt = fldr_set_attr(instance, FLDR_ATTR_UID, uid, strlen(uid));
    rt = fldr_set_attr(instance, FLDR_ATTR_PWD, pwd, strlen(pwd));

    rt = fldr_set_attr(instance, FLDR_ATTR_LOAD_MODE, (fpointer)2, 0);
    rt = fldr_set_attr(instance, FLDR_ATTR_EXPORT_MODE, (fpointer)2, 0);
    rt = fldr_set_attr(instance, FLDR_ATTR_TASK_THREAD_NUM, (fpointer)1, 0);

    sprintf_s((char*)ctl_buf, 1024, "load\n infile 't1.txt' STR '  A  '\n into table t1\nfields ','");
    rt = fldr_export(instance, ctl_buf);

    void* handle;
    fchar* data;
    fsint4 len;
    while (1)
    {
        rt = fldr_fetch_data_len(instance, &handle, &len);
        if (len == 0)
            break;

        data = (fchar*)malloc(len);

        rt = fldr_fetch_data(instance, handle, data, len);

        for (int i = 0; i < len; ++i)
        {
            std::cout << data[i];
        }
        std::cout << std::endl;

        free(data);
    }

    rt = fldr_free(instance);

    return rt;
}
```

## 7.2 JNI 编程指南

### 7.2.1 接口介绍

java 调用 dm 快速装载接口导数据是通过 jni 接口来完成的。所引用的对象在 com.dameng.floader.jar 中的 com.dameng.floader.Instance，com.dameng.floader.Properties。主要类是 com.dameng.floader.Instance。

### 7.2.2 接口说明

1. **allocInstance**

**描述**

用于分配快速装载对象实例，所有快速装载都将通过该句柄进行操作。

**格式**

```
boolean
allocInstance();
```

**参数**

无。

**返回值**

true 或 false

**说明**

该函数分配出用于快速装载实例句柄，用户必须首先调用该函数获得快速装载的实例句柄，只有通过该句柄才能进行后续的快速装载操作。

2. **free**

**描述**

释放快速装载实例句柄。

**格式**

```
void
free();
```

**参数**

无。

**返回值**

无。

**说明**

释放快速装载实例句柄，将该实例句柄上所有快速装载所占用的资源释放。

3. **setAttribute**

**描述**

设置快速装载实例的属性。

**格式**

```
boolean
setAttribute(
    int         attr_id,
    String         value
);
```

**参数**

attr\_id（输入）：属性标识，指出将要设置的属性，关于属性详细内容请参考表 7.1 属性介绍。

value（输入）：属性值，根据 attrid 不同该参数的意义不同。

**返回值**

true，false

4. **getAttribute**

**描述**

获取快速装载实例的属性。

**格式**

```
String
getAttribute(
    int     attr_id
);
```

**参数**

attrid（输入）：属性标识，指出将要获取的属性，关于属性详细内容参见 setAttribute 的说明部分。

**返回值**

属性值。

**说明**

参见 setAttribute 函数说明中各属性说明。

5. **initializeInstance**

**描述**

初始化当前快速装载实例。

**格式**

```
boolean
initializeInstance(
    String         server,
    String         user,
    String         pwd,
    String         table
);
```

**参数**

server（输入）：链接的服务器。将被记录到实例的 FLDR\_ATTR\_SERVER 属性中。

user（输入）：登录用户。将被记录到实例的 FLDR\_ATTR\_UID 属性中。

pwd（输入）：用户密码。将被记录到实例的 FLDR\_ATTR\_PWD 属性中。

table（输入）：进行快速装载的表。将被记录到实例的 FLDR\_ATTR\_TABLE 属性中。

**返回值**

true，false

**说明**

根据用户通过 setAttribute 设置的属性初始化快速装载环境，如果用户未指定连接则根据用户提供的服务器、用户和密码建立到服务器的连接。

6. **uninitialize**

**描述**

释放快速装载实例所占用的资源。

**格式**

```
boolean
uninitialize();
```

**参数**

无。

**返回值**

true，false

**说明**

用于释放所占用快速装载实例所占用的资源。用户在调用该函数后可重新初始化快速装载句柄，进行新的数据装载。

7.**fldr\_Bind\_Columns\_ex**

**描述**

绑定输入列。

**格式**

```
boolean
fldr_Bind_Columns_ex(
    int         colNumber, 
    int         type, 
    String         datefmt, 
    Object         data, 
    int         maxcollen,
    int[]         ind_len, 
    int         threadNum
);
```

**参数**

colNumber（输入）：绑定列的编号。从 1 开始计数，对应快速装载的表的相应列。

type（输入）：用户绑定数据的 JAVA 类型。此处 FLDR JNI 调用的 JAVA 数据类型是从 com.dameng.floader.DataTypes 里进行调用。 [第 4 章 DM JDBC 编程指南](jdbc-rogramming-guide.md) 中 JDBC 接口调用 JAVA 数据类型是从 java.sql.Types 里进行调用。com.dameng.floader.DataTypes 的数据类型与 java.sql.Types 的数据类型并不相同，两者的差异见下表：

<table><tbody><tr><td><b>com.dameng.floader.DataTypes（FLDR JNI）</b></td><td><b>java.sql.Types（JDBC接口）</b></td></tr><tr><td rowspan="3">DataTypes.FLDR_C_TINYINT</td><td>Types.BIT</td></tr><tr><td>Types.BOOLEAN</td></tr><tr><td>Types.TINYINT</td></tr><tr><td>DataTypes.FLDR_C_SHORT</td><td>Types.SMALLINT</td></tr><tr><td>DataTypes.FLDR_C_INT</td><td>Types.INTEGER</td></tr><tr><td>DataTypes.FLDR_C_BIGINT</td><td>Types.BIGINT</td></tr><tr><td rowspan="5">DataTypes.FLDR_C_BINARY</td><td>Types.STRUCT</td></tr><tr><td>Types.BINARY</td></tr><tr><td>Types.VARBINARY</td></tr><tr><td>Types.LONGVARBINARY</td></tr><tr><td>Types.BLOB</td></tr><tr><td>DataTypes.FLDR_C_CHAR</td><td>其他</td></tr></tbody></table>

datefmt（输入）：当绑定列对应的表的列为时间日期类型，且绑定的 JAVA 数据为 String 类型，该参数为字符串到日期类型的格式串，默认为“yyyy-mm-dd hh-mm-ss”。其他情况，忽略该绑定输入。

data（输入）：指向用于存放数据内存的地址指针。

maxcollen（输入）：用于记录绑定数据最大的长度，不允许为负值。当进行多行绑定的时候，对于变长的 C 类型，应该至少为该列数据所有行数据的总长。对于固定长度的 JAVA 数据类型，该参数内容被忽略。

ind\_len（输入）：用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向 INT 类型的数组。如果地址中保存的值为-1，绑定列的该行数据被视为空值。对于 BINARY 和 CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

threadNum（输入）：多线程调用，线程序号，单线程传 0 或 1。

**返回值**

true，false

8. **fldr\_Bind\_Columns\_Direct\_ex**

**描述**

绑定输入列。功能与 fldr\_Bind\_Columns\_ex 函数相同，fldr\_Bind\_Columns\_Direct\_ex 仅支持绑定字符串类型数据，且通常结合 JAVA 的直接内存使用，可以减少 JNI 内存拷贝。

**格式**

```
boolean

fldr_Bind_Columns_Direct_ex(

    int            colNumber, 

    int         type, 

    String         datefmt, 

    Object        data, 

    int         maxcollen,

    int[]         ind_len, 

    int         threadNum

);
```

**参数**

type（输入）：用户绑定数据的 JAVA 类型。此处仅支持 DataTypes.FLDR\_C\_CHAR。

data（输入）：指向用于存放数据内存的地址指针。通常使用 JAVA 的直接内存地址指针。

其余参数请参考 fldr\_Bind\_Columns\_ex 函数的参数说明。

**返回值**

true，false

9. **fldr\_Send\_Rows\_ex**

**描述**

发送行数。

**格式**

```
boolean
fldr_Send_Rows_ex(
long rows, 
int threadNum, 
int seqNo
);
```

**参数**

rows（输入）：在多行绑定的情况，指明绑定的行数。

threadNum（输入）：多线程调用，线程序号，单线程传 0 或 1。

seqNo（输入）：数据批次，从 1 开始自增，保证数据有序。

**返回值**

true，false

10. **setControl**

**描述**

利用控制文件执行数据装载。与 fldr\_exec\_ctl\_low 类似，也存在与 initializeInstance 类似的关系，因此也需要保证若使用 fldr\_exec\_ctl\_low 进行数据导出时，如果调用 fldr\_initialize，则必须在调用 fldr\_initialize 前，通过 fldr\_set\_attr 来设置 load\_mode 为导出模式，否则 fldr\_initialize 将认为是默认导入模式，并依照导入模式规范进行部分初始化操作，此时可能引发与导出预期不符的情况。

**格式**

```
long

setControl(

  String   ctrl

);
```

**参数**

ctrl（输入）：控制文件的内容。

**返回值**

成功装载的行数。

11. **batch**

**描述**

批量提交行数据，永久保存到服务器。

**格式**

```
long

batch();
```

**参数**

无。

**返回值**

批量提交的行数。

**说明**

将上一次调用 batch 之后所有 fldr\_Send\_Rows\_ex 装载的行进行提交，永久保存到数据库中。

12. **finish**

**描述**

结束一次批量操作。

**格式**

```
boolean

finish();
```

**参数**

无。

**返回值：**

true，false

**13\. getStatistic**

**描述**

获取当前完成的装载的统计结果, 不适用于多表装载。

**格式**

```
long[]
getStatistic();
```

**参数**

无。

**返回值**

long 数组。其中：

- 数组第 0 个值为快速装载成功数据的行数(载出时为载出成功的行数)；
- 数组第 1 个值为快速装载丢弃数据的行数(载出时为载出丢弃的行数)；
- 数组第 2 个值为快速装载失败数据的行数(载出时为 0)。

**说明**

若对多表装载使用，将只会返回最后一次装载的统计结果。

14. **getErrorMsg**

**描述**

出错时，获取错误的描述信息。

**格式**

```
string
getErrorMsg();
```

**参数**

无。

**返回值**

错误的描述信息。

**说明**

用户可以在调用接口出错时，通过本接口获取错误的描述信息。

### 7.2.3 基本示例

例 1 直接指定待载入的数据，并将其载入至数据库。

第一步，数据准备，创建数据库表 test1。

```
create table sysdba.test1(c1 int ,c2 varchar(50));
commit;
```

第二步，将数据载入至数据库

```
package com.dameng;
import java.io.File;
import com.dameng.floader.DataTypes;
import com.dameng.floader.Instance;
import com.dameng.floader.Properties;

public class TestFloder {
    public static void main(String[] args)
    {
        Instance instance = new Instance();
        int threadNum = 1;
        TestFloder floder = new TestFloder();
        String tableName = "SYSDBA.TEST1";
  
        //使用当前类中自定义的init函数，设置属性信息，并初始化当前快速装载实例
        boolean success = floder.init(instance, threadNum, tableName);
  
        //若快速装载实例初始化成功，则直接指定待装载数据，并按行进行数据装载
        if(success){
            try{
              int        c1[] = {1,2,3,4,5,6,7,8,9};        //数值类型数据
                int        c1_ind[] = {4,4,4,4,4,4,4,4,4};    //长度指示符  -1表示空
                byte[]     byteArray = new byte[9];
                for(int i = 0; i < 9; i++){
                    byteArray[i] = ((Integer)c1[i]).byteValue();
                }
                String    c2[] = {"a1","a12","a123","a1234","a12345","a123456","a1234567","a12345678","a123456789"};    //字符串类型数据
                int        c2_ind[] = {2,3,4,5,6,7,8,9,10}; 
                byte[][]     byteArray2 = new byte[9][];
                for(int i = 0; i < 9; i++){
                    byteArray2[i] = c2[i].getBytes();
                }   
                //按行装载数据
                for(int i = 1; i < 10; i++){
                    //绑定数值类型数据，data参数传入int数组c1
                    instance.fldr_Bind_Columns_ex(1, DataTypes.FLDR_C_INT, null, c1, 4, c1_ind, 1);
                    //绑定字符串类型数据，data参数传入byte数组byteArray2
                  instance.fldr_Bind_Columns_ex(2, DataTypes.FLDR_C_CHAR, null, byteArray2, 54, c2_ind, 1);
                    instance.fldr_Send_Rows_ex(9, 1, i);
                }
            }catch(Exception e){
                   e.printStackTrace();
            }
        }
  
        //若快速装载实例初始化失败，则打印错误信息，并释放快速装载实例
        if(!success){
            String message = instance.getErrorMsg();
            System.out.println("出错信息:" + message);
            instance.free();
        }

        //快速装载完成，打印实际插入的行数，并释放快速装载实例
        else{
            instance.finish();
            // 返回实际插入的行数
            long rowHaveCopied = Long.parseLong(instance.getAttribute(Properties.FLDR_ATTR_COMMIT_ROWS));
            System.out.println("已复制行数:" + rowHaveCopied);
            instance.uninitialize();
            instance.free();
        }
    }

    /**********自定义init函数，设置属性信息，并初始化当前快速装载实例**********/
    public boolean init(Instance instance, int threadNum, String tableName)
    {
        // 分配句柄
        instance.allocInstance();
        // 设置必要的属性信息
        String host = "localhost";
        String port = "5236";
        String userName = "SYSDBA";
        String password = "sysDBA*00";
        instance.setAttribute(Properties.FLDR_ATTR_SERVER, host);
        instance.setAttribute(Properties.FLDR_ATTR_PORT, port);
        instance.setAttribute(Properties.FLDR_ATTR_UID, userName);
        instance.setAttribute(Properties.FLDR_ATTR_PWD, password);
  
        // 其余属性用户均可根据实际情况选择性设置
        // 设置编码
        //instance.setAttribute(Properties.FLDR_ATTR_DATA_CHAR_SET, System.getProperty("file.encoding"));
        // 设置是否插入自增列
        //instance.setAttribute(Properties.FLDR_ATTR_SET_INDENTITY, "0");
        // fldr task线程默认为cpu个数，如果客户端线程数大于cpu个数，则必须设置该参数
        //instance.setAttribute(Properties.FLDR_ATTR_TASK_THREAD_NUM, String.valueOf(threadNum));

        // 记录出错的信息
        String dmHome = System.getProperty("DM_HOME");
        if(dmHome != null && !dmHome.equals("")){
            if(dmHome.endsWith("/") || dmHome.endsWith("\\")){
                instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + "BADFILE_1.TXT");
            }else{
                instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + File.separator + "BADFILE_1.TXT");
            }
        }

        // 装载日志
        if (dmHome != null && !dmHome.equals("")){
            if (dmHome.endsWith("/") || dmHome.endsWith("\\")){
                instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + "FLDRLOG_1.TXT");
            }else{
                instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + File.separator + "FLDRLOG_1.TXT");
            }
        }

        //初始化当前快速装载实例
        boolean success = instance.initializeInstance(null, null, null, tableName);
        return success;
}
}
```

例 2 将数据文件中的数据载入至数据库

第一步，数据准备，创建数据库表 test2。

```
create table sysdba.test2(c1 int ,c2 varchar(50));
commit;
```

第二步，准备数据文件 e:\\fldr\_insert.txt，文件内容如下：

```
1|a
2|b
```

第三步，将数据文件内容载入至数据库中。

```
package com.dameng;
import java.io.File;
import com.dameng.floader.Instance;
import com.dameng.floader.Properties;

public class TestFloder {
    public static void main(String[] args)
    {
        Instance instance = new Instance();
        int threadNum = 1;
        TestFloder floder = new TestFloder();
        String tableName = "SYSDBA.TEST2";
  
        //使用当前类中自定义的init函数，设置属性信息，并初始化当前快速装载实例
        boolean success = floder.init(instance, threadNum, tableName);
  
        //若快速装载实例初始化成功，则将数据文件内容载入至数据库中
        if(success){
            String ctl = "LOAD DATA\r\n" +
                "INFILE 'e:\\fldr_insert.txt'\r\n" +
                "INTO TABLE SYSDBA.TEST2\r\n" +
                "FIELDS '|'\r\n" +
                "(\r\n" +
                "C1 ,\r\n" +
                "C2 \r\n" +
                ")";
            //根据ctrl内容进行数据载入
            instance.setControl(ctl);
        }
  
        //若快速装载实例初始化失败，则打印错误信息，并释放快速装载实例
        if(!success){
            String message = instance.getErrorMsg();
            System.out.println("出错信息:" + message);
            instance.free();
        }

        //快速装载完成，打印实际插入的行数，并释放快速装载实例
        else{
            instance.finish();
            // 返回实际插入的行数
            long rowHaveCopied = Long.parseLong(instance.getAttribute(Properties.FLDR_ATTR_COMMIT_ROWS));
            System.out.println("已复制行数:" + rowHaveCopied);
            instance.uninitialize();
            instance.free();
        }
    }

    /**********自定义init函数，设置属性信息，并初始化当前快速装载实例**********/
    public boolean init(Instance instance, int threadNum, String tableName)
    {
        // 分配句柄
        instance.allocInstance();
        // 设置必要的属性信息
        String host = "localhost";
        String port = "5236";
        String userName = "SYSDBA";
        String password = "sysDBA*00";
        instance.setAttribute(Properties.FLDR_ATTR_SERVER, host);
        instance.setAttribute(Properties.FLDR_ATTR_PORT, port);
        instance.setAttribute(Properties.FLDR_ATTR_UID, userName);
        instance.setAttribute(Properties.FLDR_ATTR_PWD, password);
  
        // 其余属性用户均可根据实际情况选择性设置
        // 设置编码
        //instance.setAttribute(Properties.FLDR_ATTR_DATA_CHAR_SET, System.getProperty("file.encoding"));
        // 设置是否插入自增列
        //instance.setAttribute(Properties.FLDR_ATTR_SET_INDENTITY, "0");
        // fldr task线程默认为cpu个数，如果客户端线程数大于cpu个数，则必须设置该参数
        //instance.setAttribute(Properties.FLDR_ATTR_TASK_THREAD_NUM, String.valueOf(threadNum));

        // 记录出错的信息
        String dmHome = System.getProperty("DM_HOME");
        if(dmHome != null && !dmHome.equals("")){
            if(dmHome.endsWith("/") || dmHome.endsWith("\\")){
                instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + "BADFILE_2.TXT");
            }else{
                instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + File.separator + "BADFILE_2.TXT");
            }
        }

        // 装载日志
        if (dmHome != null && !dmHome.equals("")){
            if (dmHome.endsWith("/") || dmHome.endsWith("\\")){
                instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + "FLDRLOG_2.TXT");
            }else{
                instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + File.separator + "FLDRLOG_2.TXT");
            }
        }

        //初始化当前快速装载实例
        boolean success = instance.initializeInstance(null, null, null, tableName);
        return success;
}
}
```

例 3 将数据库表中的数据载出到文件中

第一步，数据准备，创建数据库表 test3。

```
create table sysdba.test3(c1 int);
insert into sysdba.test3 values(1),(2),(3);
commit;
```

第二步，将表 test3 中的数据载出到文件 e:\\fldr\_out.txt 中。

```
package com.dameng;
import com.dameng.floader.Instance;
import com.dameng.floader.Properties;

public class TestFloder {
    public static void main(String[] args)
    {
        Instance instance = new Instance();
        try{
            if(instance.allocInstance()){
                instance.setAttribute(Properties.FLDR_ATTR_SERVER, "192.168.1.55");
                instance.setAttribute(Properties.FLDR_ATTR_PORT, "5236");
                instance.setAttribute(Properties.FLDR_ATTR_UID, "SYSDBA");
                instance.setAttribute(Properties.FLDR_ATTR_PWD, "sysDBA*00");
                instance.setAttribute(Properties.FLDR_ATTR_DATA_CHAR_SET, "GBK");
                instance.setAttribute(Properties.FLDR_ATTR_LOAD_MODE, "2");
                //初始化当前快速装载实例
                instance.initializeInstance(null, null, null, "SYSDBA.TEST3");
                String ctl = "OPTIONS\r\n" + 
                        "(\r\n" + 
                        "mode='out'\r\n" + 
                        ")\r\n" + 
                        "Load\r\n" + 
                        "infile 'e:\\fldr_out.txt'\r\n" + 
                        "Append\r\n" + 
                        "into table SYSDBA.TEST3\r\n" + 
                        "FIELDS '|'";
                //根据ctrl内容进行数据载出
                instance.setControl(ctl);
            }else{
                System.out.println(instance.getErrorMsg());
            }
        }finally{
            //释放
            instance.uninitialize();
            instance.free();
        }
    }
}
```

第三步，查看文件 e:\\fldr\_out.txt。

```
1
2
3
```
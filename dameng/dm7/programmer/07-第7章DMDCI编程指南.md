---
title: "第7章 DM DCI编程指南"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=199"
tags:
  - dameng
  - dm7
  - programmer
---

## 第7 章 DM DCI 编程指南

## 7.1 DM DCI 介绍

本章将较全面而系统地介绍DM DCI（DM Call Interface）的基本概念以及DM DCI 的使用方法，以便用户更好地使用DM DCI 编写应用程序。

OCI（Oracle Call Interface）是ORACLE 公司开发的一个应用程序开发工具，是一个通过访问Oracle 数据库的服务器，控制各类SQL 语句的执行，进而创建应用程序的的应用程序接口（API）。它支持SQL 所有的数据定义、数据操作、查询、事务管理等操作，支持C和C++的数据类型、调用、语法和语义。它提供了一组可对Oracle 数据库进行存取的接口子例程(函数)。

DM DCI 是参照OCI 的接口标准，结合自身的特点，为开发人员提供向oracle 兼容功能的一款接口产品。以下部分将介绍dci 的实现内容，以及针对oralce 兼容的实现和限制。

## 7.2 数据类型

DCI 支持的数据类型表7.1 所示：

表7.1 DCI 支持的数据类型

数据类型类型说明SQLT_CHR 变长字符串类型整数类型，当指定长度为1 时，对应C的BYTE 类型；长度为2 时，对应C的SQLT_INT short 类型；长度为4 时，对应C的int 类型；长度为8 时，对应C的int64 类型。

浮点数据类型，当指定的长度为4 时，对应C数据类型float，当指定长度为8 时，SQLT_FLT对应C数据类型double SQLT_STR 以空结尾的变长字符串类型SQLT_LNG 长数据类型SQLT_VCS 变长字符类型7 字节存贮的时间格式，SQLT_DAT取值范围是公元前4712 年1 月1 日至公元9999 年12 月31 日SQLT_ODT 标准的时间数据类型，可以使用OCIDate 结构体来格式化获取的日期SQLT_VBI 变长二进制数据类型SQLT_BIN 二进制数据类型SQLT_LBI 长二进制数据类型SQLT_UIN 无符号整数类型SQLT_LVC 长变长字符类型SQLT_LVB 长变长二进制数据类型SQLT_AFC 固定长度的字符串类型SQLT_AVC 变长字符类型结果集游标类型，该参数用在存贮过程的游标参数，SQLT_RSET可以返回结果集中产生的结果集。

## 第7 章 DM DCI 编程指南

SQLT_TIME OCITime 结构体可以用此类型绑定。

SQLT_TIMESTAMP OCIDateTime 结构体可以用此类型绑定。

SQLT_CLOB CLOB 类型SQLT_BLOB BLOB 类型

## 7.3 参考函数

### 7.3.1 关系型接口函数

#### 7.3.3.1 Connect、 Authorize 和 Initialize 方法

1. OCIEnvCreate

描述创建并初始化环境句柄格式sword OCIEnvCreate ( OCIEnv **envhpp,

ub4 mode,CONST dvoid *ctxp,CONST dvoid *(*malocfp)(dvoid *ctxp,size_t size),CONST dvoid *(*ralocfp)(dvoid *ctxp,dvoid *memptr,size_t newsize),CONST void (*mfreefp)(dvoid *ctxp,dvoid *memptr))size_t xtramemsz,

dvoid **usrmempp );

参数

参数描述envhpp（OUT）用于输出环境句柄mode（IN） 初始化的模式，目前只支持OCI_DEFAULT – 默认模式ctxp(IN) 保留兼容，忽略该参数malocfp(IN) 保留兼容，忽略该参数ralocfp(IN) 保留兼容，忽略该参数mfreefp(IN) 保留兼容，忽略该参数xtramemsz(IN) 额外附加分配的内存空间usrmempp(OUT) 返回额外分配的附加内存空间的地址

## 第7 章 DM DCI 编程指南

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR，使用无效句柄时返回OCI_INVALID_HANDLE

2. OCIEnvInit

描述分配并初始化环境句柄。

格式sword OCIEnvInit ( OCIEnv **envhpp,

ub4 mode,size_t xtramemsz,

dvoid **usrmempp );

参数

参数描述envp(OUT) 环境句柄mode(IN) 初始化的模式，目前只支持OCI_DEFAULT – 默认模式xtramem_sz(IN) 额外附加分配的内存空间usrmempp(IN) 返回额外分配的附加内存空间的地址

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

3. OCIInitialize

描述初始化OCI 应用环境，OCI 会在这个函数中初始化内部的全局变量和加载一些配置信息。

格式sword OCIInitialize ( ub4 mode,

CONST dvoid *ctxp,CONST dvoid *(*malocfp)(/* dvoid *ctxp,size_t size _*/),CONST dvoid *(*ralocfp)(/*_ dvoid *ctxp,dvoid *memptr,size_t newsize _*/),CONST void (*mfreefp)(/*_ dvoid *ctxp,dvoid *memptr _*/));

参数

参数描述mode(IN) 初始化的模式，目前只支持OCI_DEFAULT – 默认模式

## 第7 章 DM DCI 编程指南

ctxp(IN) 保留兼容，忽略该参数malocfp(IN) 保留兼容，忽略该参数ralocfp(IN) 保留兼容，忽略该参数mfreefp(IN) 保留兼容，忽略该参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCILogoff

描述断开通过OCILogon 与服务器建立的连接。

格式sword OCILogoff ( OCISvcCtx *svchp OCIError *errhp );

参数

参数描述svchp(IN) 要断开连接的上下文句柄errhp(INOUT) 错误信息句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCILogon

描述根据用户名和密码，登录到一个指定的数据库服务上，并初始化相关的上下文句柄。

格式sword OCILogon ( OCIEnv *envhp,

OCIError *errhp,OCISvcCtx **svchp,CONST OraText *username,ub4 uname_len,CONST OraText *password,ub4 passwd_len,CONST OraText *dbname,

ub4 dbname_len );

参数

参数描述envhp(IN) 环境句柄errhp(INOUT) 错误信息句柄svchp(INOUT) 上下文句柄username(IN) 登录的用户名uname_len(IN) 登录的用户名长度password(IN) 登录的口令

## 第7 章 DM DCI 编程指南

passwd_len(IN) 登录的口令长度dbname(IN) 数据库服务名dbname_len(IN) 数据库服务名长

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCIServerAttach

描述附加一个数据库服务到指定的连接句柄上。

格式sword OCIServerAttach ( OCIServer *srvhp,

OCIError *errhp,CONST text *dblink,sb4 dblink_len,

ub4 mode );

参数

参数描述srvhp(IN) 连接句柄errhp(INOUT) 错误信息句柄dblink(IN) 要关联的数据库服务名dblink_len(IN) 数据库服务名的长度mode(IN) 附加模式，目前只支持OCI_DEFAULT

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

7. OCIServerDetach

描述解除连接句柄和数据库服务名之间的关联。

格式sword OCIServerDetach ( OCIServer *srvhp,

OCIError *errhp,

ub4 mode );

参数

参数描述srvhp(IN) 连接句柄errhp(INOUT) 错误信息句柄mode(IN) 附加模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

8. OCISessionBegin

## 第7 章 DM DCI 编程指南

描述使用登录信息在指定的上下文句柄上打开与数据库服务的连接。

格式sword OCISessionBegin ( OCISvcCtx *svchp,

OCIError *errhp,OCISession *usrhp,ub4 credt,ub4 mode );

参数

参数描述svchp(IN) 指定打开连接的上下文errhp(INOUT) 错误信息句柄usrhp(IN) 登录信息句柄登录的方式, 目前只支持OCI_CRED_RDBMS – 通过用户名credt(IN)和口令与数据库服务建立起连接mode(IN) 连接模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

9. OCISessionEnd

描述结束OCISessionBegin 函数中上下文句柄与数据库服务之间的连接。

格式sword OCISessionEnd ( OCISvcCtx *svchp,

OCIError *errhp,OCISession *usrhp,

ub4 mode );

参数

参数描述svchp(IN) 指定断开连接的上下文errhp(INOUT) 错误信息句柄usrhp(IN) 登录信息句柄mode(IN) 连接模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.2 Handle 和 Descriptor 方法

1. OCIAttrGet

## 第7 章 DM DCI 编程指南

描述获取句柄上的属性值。

格式sword OCIAttrGet ( CONST dvoid *trgthndlp,

ub4 trghndltyp,dvoid *attributep,ub4 *sizep,ub4 attrtype,OCIError *errhp );

参数

参数描述trgthndlp(IN) 要获取属性的句柄trghndltyp(IN) trgthndlp 参数句柄的类型attributep(OUT) 存放输出属性的缓冲区size(OUT) 存放输出属性大小的缓冲区attrtype(IN) 要获取的属性errhp(IN) 错误信息句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明DCI 支持如下句柄的属性获取：

句柄描述OCI_HTYPE_ENV 环境句柄OCI_HTYPE_ERROR 错误句柄OCI_HTYPE_SVCCTX 上下文句柄OCI_HTYPE_STMT 语句句柄OCI_HTYPE_SERVER 服务器句柄OCI_HTYPE_SESSION 会话句柄OCI_HTYPE_TRANS 事务句柄OCI_HTYPE_BIND 参数绑定句柄OCI_HTYPE_DEFINE 列绑定句柄OCI_HTYPE_DIRPATH_STREAM dp 流句柄OCI_HTYPE_DIRPATH_COLUMN_ARRAY dp 列数据数组OCI_HTYPE_DIRPATH_CTX dp 运行环境句柄OCI_DTYPE_PARAM 描述信息参数句柄OCI_HTYPE_DESCRIBE 描述句柄

2. OCIAttrSet

描述设置句柄的属性。

格式

## 第7 章 DM DCI 编程指南

sword OCIAttrSet ( dvoid *trgthndlp,

ub4 trghndltyp,dvoid *attributep,ub4 size,ub4 attrtype,OCIError *errhp );

参数

参数描述trgthndlp(IN) 需要设置属性的句柄trghndltyp(IN) trgthndlp 参数句柄的类型attributep(IN) 要设置属性值的指针size(IN) attributep 参数的大小attrtype(IN) 要设置的句柄属性errhp(IN) 错误信息句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明参考OCIAttrSet 函数获取支持的句柄。

3. OCIDescriptorAlloc

描述分配一个存贮大字段描述符句柄。

格式sword OCIDescriptorAlloc ( CONST dvoid *parenth,

dvoid **descpp,ub4 type,size_t xtramem_sz,dvoid **usrmempp);

参数

参数描述parenth(IN) 环境句柄descpp(OUT) 存贮大字段描述符指针描述符类型，目前只支持OCI_DTYPE_LOB 大字段描述、OCI_DTYPE_TIME –时间类型type(IN)OCI_DTYPE_TIMESTAMP-日期时间类型xtramem_sz(IN) 额外附加分配的内存空间usrmempp(IN) 返回额外分配的附加内存空间的地址

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明支持的描述句柄

句柄描述

## 第7 章 DM DCI 编程指南

OCI_DTYPE_LOB 大字段句柄OCI_DTYPE_TIME 时间类型句柄OCI_DTYPE_TIMESTAMP 日期时间类型句柄

4. OCIDescriptorFree

描述释放OCIDescriptorAlloc 生成的描述符。

格式sword OCIDescriptorFree ( dvoid *descp,

ub4 type );

参数

参数描述descp(IN) 描述符指针type(IN) 描述符类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明参见OCIDescriptorAlloc 说明中可分配的句柄。

5. OCIHandleAlloc

描述分配和初始化各种句柄。

格式sword OCIHandleAlloc ( CONST dvoid *parenth,

dvoid **hndlpp,ub4 type,size_t xtramem_sz,

dvoid **usrmempp );

参数

参数描述parentth(IN) 环境句柄hndlpp(OUT) 句柄指针type(IN) 句柄类型xtramem_sz(IN) 额外附加分配的内存空间usrmempp(IN) 返回额外分配的附加内存空间的地址

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明DCI 支持如下句柄的分配：

句柄描述

## 第7 章 DM DCI 编程指南

OCI_HTYPE_ENV 环境句柄OCI_HTYPE_ERROR 错误句柄OCI_HTYPE_SVCCTX 上下文句柄OCI_HTYPE_STMT 语句句柄OCI_HTYPE_SERVER 服务器句柄OCI_HTYPE_SESSION 会话句柄OCI_HTYPE_TRANS 事务句柄OCI_HTYPE_BIND 参数绑定句柄OCI_HTYPE_DEFINE 列绑定句柄OCI_HTYPE_DIRPATH_STREAM dp 流句柄OCI_HTYPE_DIRPATH_COLUMN_ARRAY dp 列数据数组OCI_HTYPE_DIRPATH_CTX dp 运行环境句柄OCI_HTYPE_DESCRIBE 描述句柄

6. OCIHandleFree

描述释放由OCIHandleAlloc 所分配的句柄。

格式sword OCIHandleFree ( dvoid *hndlp,ub4 type );

参数

参数描述

hndlp(IN) 句柄指针type(IN) 句柄类型返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明参考OCIHandleAlloc 获得句柄分配相关信息。

7. OCIParamGet

描述获取描述符句柄上指定位置的描述符句柄。

格式sword OCIParamGet ( CONST dvoid *hndlp,

ub4 htype,OCIError *errhp,dvoid **parmdpp,ub4 pos );

参数

参数描述hndlp(IN) 一个存在描述信息的句柄

## 第7 章 DM DCI 编程指南

htype(IN) hndlp 参数句柄的类型errhp(IN) 错误信息句柄parmdpp(OUT) 输出的描述符句柄pos(IN) 要获取描述符上指定位置的描述信息

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明dci 支持如下句柄的param 句柄获取

句柄描述

OCI_HTYPE_STMT 语句句柄OCI_DTYPE_PARAM 参数句柄

#### 7.3.3.3 Bind、Define 和 Describe 方法

1. OCIBindArrayOfStruct

描述以数组方式进行参数绑定。

格式sword OCIBindArrayOfStruct ( OCIDefine * bindp,

OCIError *errhp,ub4 pvskip,ub4 indskip,ub4 alskip,ub4 rcskip );

参数

参数描述

bindp (IN) 绑定结构指针

errhp(INOUT) 错误信息句柄每个值间隔的大小，在一次性返回多行时，pvskip(IN)OCI 会跟据这个大小来回填每一行的值indskip(IN) 空值指示符的间隔大小

alskip (IN) 返回值长度指示符的间隔大小

rcskip(IN) 指示多行绑定跳过的字节数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

2. OCIBindByName

描述按参数名称绑定SQL 语句中的参数。

## 第7 章 DM DCI 编程指南

格式sword OCIBindByName ( OCIStmt *stmtp,

OCIBind **bindpp,OCIError *errhp,CONST text *placeholder,sb4 placeh_len,dvoid *valuep,sb4 value_sz,ub2 dty,dvoid *indp,ub2 *alenp,ub2 *rcodep,ub4 maxarr_len,ub4 *curelep,ub4 mode );

参数

参数描述stmtp(IN) 语句句柄bindp(OUT) 绑定信息句柄errhp(INOUT) 错误信息句柄placeholder(IN) 绑定的参数名称placeh_len(IN) 参数名称的长度valuep(IN) 参数值缓冲区指针value_sz(IN) 参数类型单个值的大小dty(IN) 参数的数据类型indp(IN) 保留参数，请置NULL alenp(IN) 保留参数，请置NULL rcodep(IN) 保留参数，请置NULL maxarr_len(IN) 保留参数curelep(IN) 保留参数，请置NULL mode(IN) 绑定的模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

3. OCIBindByPos

描述按参数在SQL 语句中出现的位置进行绑定。

格式sword OCIBindByPos ( OCIStmt *stmtp,

OCIBind **bindp,OCIError *errhp,ub4 position,

## 第7 章 DM DCI 编程指南

dvoid *valuep,sb4 value_sz,ub2 dty,dvoid *indp,ub2 *alenp,ub2 *rcodep,ub4 maxarr_len,ub4 *curelep,ub4 mode );

参数

参数描述stmtp(IN) 语句句柄bindp(OUT) 绑定信息句柄errhp(INOUT) 错误信息句柄position(IN) 参数在SQL 中出现的位置，从1 开始记数valuep(IN) 参数值缓冲区指针value_sz(IN) 参数类型单个值的大小参数的数据类型，不支持SQLT_RDD、SQLT_NTY、SQLT_REF、SQLT_FILE dty(IN)SQLT_VST 类型indp(IN) 保留参数，请置NULL alenp(IN) 保留参数，请置NULL rcodep(IN) 保留参数，请置NULL maxarr_len(IN) 保留参数curelep(IN) 保留参数，请置NULL mode(IN) 绑定的模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCIBindDynamic

描述动态绑定参数。

格式sword OCIBindDynamic ( OCIBind *bindp,

OCIError *errhp,dvoid *ictxp,OCICallbackInBind (icbfp)(/*_dvoid *ictxp,OCIBind *bindp,ub4 iter,ub4 index,dvoid **bufpp,ub4 *alenp,

## 第7 章 DM DCI 编程指南

ub1 *piecep,dvoid **indpp */),dvoid *octxp,OCICallbackOutBind (ocbfp)(/*_dvoid *octxp,OCIBind *bindp,ub4 iter,ub4 index,dvoid **bufpp,ub4 **alenpp,ub1 *piecep,dvoid **indpp,

ub2 **rcodepp _*/) );

参数

参数描述bindp (INOUT) 绑定参数句柄errhp (INOUT) 错误句柄ictxp(IN) 输入参数环境icbfp(IN) 输入回调函数octxp(IN) 输出参数环境ocbfp(IN) 输出回调函数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCIDefineArrayOfStruct

描述以数组方式进行列绑定。

格式sword OCIDefineArrayOfStruct ( OCIDefine *defnp,

OCIError *errhp,ub4 pvskip,ub4 indskip,ub4 rlskip,ub4 rcskip );

参数

参数描述

defnp (IN) 绑定结构指针

errhp(INOUT) 错误信息句柄每个值间隔的大小，在一次性返回多行时，pvskip(IN)OCI 会跟据这个大小来回填每一行的值indskip(IN) 空值指示符的间隔大小

## 第7 章 DM DCI 编程指南

rlskip (IN) 返回值长度指示符的间隔大小

rcskip(IN) 指示多行绑定跳过的字节数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCIDefineByPos

描述按位置来绑定查询返回结果集中每一列的取值空间。

格式sword OCIDefineByPos ( OCIStmt *stmtp,

OCIDefine **defnpp,OCIError *errhp,ub4 position,dvoid *valuep,sb4 value_sz,ub2 dty,dvoid *indp,ub2 *rlenp,ub2 *rcodep,ub4 mode );

参数

参数描述stmtp(IN) 语句句柄绑定结构输出指针，可以通过使用该参数调用OCIDefineArrayOfStruct 来指定该列每个值defnp(OUT)之间的间隔大小。

errhp(INOUT) 错误信息句柄position(IN) 参数在SQL 中出现的位置，从1 开始记数valuep(IN) 参数值缓冲区指针value_sz(IN) 参数类型单个值的大小dty(IN) 参数的数据类型指示符缓冲区，如果结果集中存在NULL值，那么OCI会回填该缓冲区，把对应的位置置为indp(IN) -1，其它情况下置0；如果在绑定的时候，未设置该指示符缓冲区，但是获取的结果中存又存在NULL值，该函数会返回OCI_ERROR的错误。

返回值长度指示缓冲区，如果返回值未发生截断，那么该缓冲区中的值就是实际的返回值rlenp(IN) 长度；如果返回值在获取的时候发生了截断，那么该缓冲区的值就是未截断以前的长度；

如果返回值是空值，该缓冲区的值将被置为0。

rcodep(IN) 保留参数mode(IN) 绑定模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

## 第7 章 DM DCI 编程指南

7. OCIDescribeAny

描述连续写入内容到一个大字段存贮描述符中。

格式sword OCIDescribeAny ( OCISvcCtx *svchp,

OCIError *errhp,dvoid *objptr,ub4 objptr_len,ub1 objptr_typ,ub1 info_level,ub1 objtyp,OCIDescribe *dschp );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄objptr(IN) 要被描述的对像指针，目前只支持字符串类型指针objnm_len(IN) objptr 参数中字符串的长度objptr_typ(IN) objptr 指针类型，目前只支持OCI_OTYPE_NAME – 对像名称类型指针info_level(IN) 存放读到数据的缓冲区指针objtyp(IN) objptr 参数所指的对像类型一个描述符句柄，该句柄可以通过使用OCI_HTYPE_DESCRIBE dschp(IN)作为参数调用OCIHandleAlloc 分配得到

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明DCI 支持如下对象的描述：

句柄描述OCI_PTYPE_DATABASE 数据库，达梦不支持数据库概念，进行描述将会返回错误OCI_PTYPE_SCHEMA 模式OCI_PTYPE_TABLE 表OCI_PTYPE_VIEW 视图OCI_PTYPE_PROC 存储过程OCI_PTYPE_FUNC 函数OCI_PTYPE_PKG 包

#### 7.3.3.4 Statement 方法

1. OCIStmtExecute

描述

## 第7 章 DM DCI 编程指南

执行准备好的语句。

格式sword OCIStmtExecute ( OCISvcCtx *svchp,

OCIStmt *stmtp,OCIError *errhp,ub4 iters,ub4 rowoff,CONST OCISnapshot *snap_in,OCISnapshot *snap_out,ub4 mode );

参数

参数描述svchp(IN) 环境句柄stmtp(IN) 语句句柄errhp(INOUT) 错误句柄对查询语句且进行了列绑定，则该值需置为1；

iters(IN) 对查询语句且没有进行列绑定，则该值置为0；

对非查询语句与rowoff 配合，指示执行次数rowoff(IN) 对非查询语句与iters 配合，指示执行次数snap_in(IN) 不支持snap_out(OUT) 不支持mode(IN) 执行模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

说明支持mode 的模式：

模式描述OCI_COMMIT_ON_SUCCESS 成功后提交事务OCI_DEFAULT 默认OCI_DESCRIBE_ONLY 描述信息OCI_EXACT_FETCH 获取行数据OCI_PARSE_ONLY 语法分析

2. OCIStmtFetch

描述提取SQL 生成的结果集中的行集。当执行一条查询以后，可以多次调用该函数来返回结果集中的所有行，直到该函数返回OCI_NO_DATA。

格式sword OCIStmtFetch (OCIStmt *stmtp, OCIError *errhp, ub4 nrows, ub2 orientation, ub4 mode)参数

参数描述

## 第7 章 DM DCI 编程指南

stmtp(IN) 语句句柄errhp(INOUT) 错误信息句柄nrows(IN) 需要获取的行数orientation (IN) 行集提取的方式mode(IN) 提取模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回 OCI_SUCCESS，失败返回 OCI_ERROR，出现警告信息返回OCI_SUCCESS_WITH_INFO，超过行集末尾而无法获取数据OCI_NO_DATA。

说明支持的行集提取的方式

方式描述OCI_FETCH_NEXT 从当前游标位置向下进行提取操作OCI_FETCH_FIRST 从结果集的第一行开始向下进行提取操作OCI_FETCH_LAST 从结果集的最后一行开始向下提取操作OCI_FETCH_PRIOR 从结果集的当前游标位置向上进行提取操作

3. OCIStmtFetch2

描述可滚动获取行集。

格式sword OCIStmtFetch2 ( OCIStmt *stmthp,

OCIError *errhp,ub4 nrows,ub2 orientation,sb4 fetchOffset,

ub4 mode );

参数

参数描述

stmthp (INOUT) 语句句柄errhp (INOUT) 错误句柄nrows(IN) 获取行数orientation(IN) 游标方向fetchOffset(IN) 偏移mode(IN) 获取模式，不支持该参数，忽略其输入返回值成功返回 OCI_SUCCESS，失败返回 OCI_ERROR，出现警告信息返回OCI_SUCCESS_WITH_INFO，超过行集末尾而无法获取数据返回OCI_NO_DATA。

说明支持如下游标方向

方向描述OCI_FETCH_NEXT/OCI_DEFAULT 向后获取

## 第7 章 DM DCI 编程指南

OCI_FETCH_CURRENT 获取当前行OCI_FETCH_FIRST 从行集头部获取OCI_FETCH_LAST 从行集尾部获取OCI_FETCH_PRIOR 向前获取OCI_FETCH_ABSOLUTE 以绝对位置定位获取OCI_FETCH_RELATIVE 以相对位置定位获取

4. OCIStmtGetPieceInfo

描述获取获取运行时参数信息。

格式sword OCIStmtGetPieceInfo( CONST OCIStmt *stmtp,

OCIError *errhp,dvoid **hndlpp,ub4 *typep,ub1 *in_outp,ub4 *iterp,ub4 *idxp,ub1 *piecep );

参数

参数描述stmtp(IN) 语句句柄errhp (INOUT) 错误句柄hndlpp(OUT) 绑定句柄typep (OUT) 绑定类型in_outp (OUT) 输入输出类型iterp (OUT) 获取循环计数信息idxp (OUT) 不支持该参数，忽略piecep (OUT) 分片信息

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCIStmtPrepare

描述准备一条SQL 语句，以便随后调用OCIStmtExecute 来执行。

格式sword OCIStmtPrepare ( OCIStmt *stmtp,

OCIError *errhp,CONST text *stmt,ub4 stmt_len,ub4 language,ub4 mode );

## 第7 章 DM DCI 编程指南

参数

参数描述stmtp(IN) 语句句柄errhp(INOUT) 错误信息句柄stmt(IN) 准备执行的SQL 语句stmt_len(IN) stmt 参数中SQL 语句的长度language(IN) 保留参数mode(IN) 准备模式，目前只支持OCI_DEFAULT – 默认模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCIStmtSetPieceInfo

描述设置运行时分批提供数据的信息。

格式sword OCIStmtSetPieceInfo ( dvoid *hndlp,

ub4 type,OCIError *errhp,CONST dvoid *bufp,ub4 *alenp,ub1 piece,CONST dvoid *indp,ub2 *rcodep );

参数

参数描述

hndlp (IN/OUT) 句柄，dci 仅支持绑定参数的句柄

type(IN) 忽略errhp(IN OUT) 错误句柄

bufp (IN/OUT) 缓冲区指针alenp (IN/OUT) 长度指针piece (IN) 当前piece indp (IN/OUT) 指示符指针rcodep (IN/OUT) 返回值指针返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.5 LOB 方法

1. OCILobGetLength

描述

## 第7 章 DM DCI 编程指南

返回大字段的长度，按字节计算。

格式sword OCILobGetLength ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *locp,ub4 *lenp );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(IN) 存贮大字段描述符指针lenp(OUT) 返回的大字段长度，按字节计算

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

2. OCILobRead

描述读取某个大字段中指定长度的内容。

格式sword OCILobRead ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *locp,ub4 *amtp,ub4 offset,dvoid *bufp,ub4 bufl,dvoid *ctxp,OCICallbackLobRead (cbfp)( dvoid *ctxp,CONST dvoid *bufp,ub4 len,ub1 piece)ub2 csid,ub1 csfrm );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(IN) 存贮大字段描述符指针Amtp(IN/OUT) 该参数为输入输出参数，当调用函数时，该参数表明想读取的字节数，

## 第7 章 DM DCI 编程指南

当函数执行完以后，OCI 会回填实际读到的字节数offset 保留参数bufp(IN) 存放读到数据的缓冲区指针bufl(IN) 存放读到数据的缓冲区长度ctxp 保留参数cbfp 保留参数csid 保留参数csfrm 保留参数

返回值如果执行成功，在还有数据未读取完的情况下，返回OCI_NEED_DATA；如果数据都已经读完则返回OCI_SUCCESS；执行失败则返回OCI_ERROR。

3. OCILobWrite

描述连续写入内容到一个大字段存贮描述符中。

格式sword OCILobWrite ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *locp,ub4 *amtp,ub4 offset,dvoid *bufp,ub4 buflen,ub1 piece,dvoid *ctxp,OCICallbackLobWrite (cbfp)(dvoid *ctxp,dvoid *bufp,ub4 *lenp,ub1 *piecep)ub2 csid,ub1 csfrm );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(IN) 存贮大字段描述符指针该参数为输入输出参数，当调用函数时，该参数表明想读取的字节数，amtp(IN/OUT）当函数执行完以后，OCI 会回填实际读到的字节数offset 保留参数

## 第7 章 DM DCI 编程指南

bufp(IN) 存放读到数据的缓冲区指针buflen(IN) 存放读到数据的缓冲区长度piece 保留参数ctxp 保留参数cbfp 保留参数csid 保留参数csfrm 保留参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCILobCreateTemporary

描述创建一个临时大字段。

格式sword OCILobCreateTemporary(OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *locp,ub2 csid,ub1 csfrm,ub1 lobtype,boolean cache,

OCIDuration duration);

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(IN) 存贮大字段描述符指针csid 保留参数csfrm 保留参数Lobtype(IN) 大字段类型 OCI_TEMP_BLOB OCI_TEMP_CLOB Cache 保留参数duration 保留参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCILobFreeTemporary

描述释放临时大字段。

格式sword OCILobFreeTemporary( OCISvcCtx *svchp,

OCIError *errhp,

## 第7 章 DM DCI 编程指南

OCILobLocator *locp);

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(IN) 存贮大字段描述符指针

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCILobFileClose

描述关闭一个已经打开的BFILE格式sword OCILobFileClose ( OCISvcCtx *svchp,

OCIError *errhp,

OCILobLocator *filep );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄filep(INOUT) BFILE 句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

7. OCILobFileCLoseAll

描述关闭所有在服务句柄上打开的BFILE格式sword OCILobFileCLoseAll ( OCISvcCtx *svchp,OCIError *errhp );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

8. OCILobFileExists

描述判断是否存在指定的BFILE

## 第7 章 DM DCI 编程指南

格式sword OCILobFileExists ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *filep,

boolean *flag );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄filep(IN) BFILE 句柄flag(OUT) TRUE 表示文件存在，FALSE 表示文件不存在

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

9. OCILobFileGetName

描述获取BFILE 所对应的目录对象及文件名格式sword OCILobFileGetName ( OCIEnv *envhp,

OCIError *errhp,const OCILobLocator *filep,OraText *dir_alias,ub2 *d_length,OraText *filename,

ub2 *f_length );

参数

参数描述svchp(INOUT) 上下文句柄指针errhp(INOUT) 错误信息句柄filep(IN) BFILE 句柄dir_alias(OUT) 目录对象缓冲区d_length(INOUT) 输入时为dir_alias 缓冲区长度,输出时为实际的目录对象的长度filename(OUT) 文件名缓冲区f_length(INOUT) 输入时为filename 缓冲区长度,输出时为实际文件名的长度

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

10. OCILobFileIsOpen

描述判断BFILE 是否已经打开格式

## 第7 章 DM DCI 编程指南

sword OCILobFileIsOpen ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *filep,

boolean *flag );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄filep(IN) BFILE 句柄flag(OUT) TRUE 表示文件已打开，FALSE 表示文件未打开

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

11. OCILobFileOpen

描述以只读方式打开一个BFILE格式sword OCILobFileOpen ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *filep,

ub1 mode );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄filep(INOUT) BFILE 句柄mode(IN) 文件打开方式,合法值为OCI_FILE_READONLY

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

12. OCILobFileSetName

描述设置BFILE 对象的目录及文件名格式sword OCILobFileSetName ( OCIEnv *envhp,

OCIError *errhp,OCILobLocator **filepp,const OraText *dir_alias,ub2 d_length,const OraText *filename,

ub2 f_length );

## 第7 章 DM DCI 编程指南

参数

参数描述svchp(INOUT) 上下文句柄指针errhp(INOUT) 错误信息句柄filepp(INOUT) BFILE 句柄dir_alias(IN) 设置的目录对象缓冲区d_length(IN) 目录对象的长度filename(IN) 设置的文件名对象缓冲区f_length(IN) 文件名对象的长度

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

13. OCILobLoadFromFile

描述加载BFILE 文件的数据到LOB 对象中格式sword OCILobLoadFromFile ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *dst_locp,OCILobLocator *src_locp,ub4 amount,ub4 dst_offset,

ub4 src_offset );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄dst_locp(INOUT) LOB 句柄src_locp(INOUT) BFILE 句柄amount(IN) 加载的数据总数dst_offset(IN) 加载到目标lob 对象的偏移,字符类型lob 为字符偏移,字节类型lob 为字节偏移,起始为1 src_offset(IN) BFILE 对象的起始偏移,起始为1

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

14. OCILobLocatorAssign

描述赋值一个LOB 对象到另外一个格式sword OCILobLocatorAssign ( OCISvcCtx *svchp,

OCIError *errhp,

## 第7 章 DM DCI 编程指南

const OCILobLocator *src_locp,

OCILobLocator **dst_locpp );

参数

参数描述svchp(INOUT) 上下文句柄指针errhp(INOUT) 错误信息句柄src_locp(IN) 被复制的LOB/BFILE 句柄dst_locp(INOUT) 需要设置的LOB/BFILE 句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

15. OCILobAssign

描述赋值一个LOB 对象到另外一个格式sword OCILobAssign ( OCISvcCtx *svchp,

OCIError *errhp,const OCILobLocator *src_locp,

OCILobLocator **dst_locpp );

参数

参数描述svchp(INOUT) 上下文句柄指针errhp(INOUT) 错误信息句柄src_locp(IN) 被复制的LOB/BFILE 句柄dst_locp(INOUT) 需要设置的LOB/BFILE 句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

16. OCILobLocatorIsInit

描述判断给定的LOB/BFILE 句柄是否已经初始化格式sword OCILobLocatorIsInit ( OCIEnv *envhp,

OCIError *errhp,const OCILobLocator *locp,

boolean *is_initialized );

参数

参数描述svchp(INOUT) 上下文句柄指针errhp(INOUT) 错误信息句柄

## 第7 章 DM DCI 编程指南

locp(IN) LOB/BFILE 句柄is_initialized (OUT) TRUE 表示已初始化,FALSE 表示未初始化

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

17. OCILobOpen

描述打开一个LOB/BFILE 对象格式sword OCILobOpen ( OCISvcCtx *svchp,

OCIError *errhp,OCILobLocator *locp,

ub1 mode );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(INOUT) LOB/BFILE 句柄mode (IN) 打开模式

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

18. OCILobClose

描述关闭一个LOB/BFILE 对象格式sword OCILobClose ( OCISvcCtx *svchp,

OCIError *errhp,

OCILobLocator *locp );

参数

参数描述svchp(IN) 上下文句柄指针errhp(INOUT) 错误信息句柄locp(INOUT) LOB/BFILE 句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

19. OCILobIsEqual

描述判断给定的LOB/BFILE 句柄是否相等

## 第7 章 DM DCI 编程指南

格式sword OCILobIsEqual ( OCIEnv *envhp,

const OCILobLocator *x,const OCILobLocator *y,

boolean *is_equal );

参数

参数描述svchp(IN) 上下文句柄指针x(IN) LOB/BFILE 句柄y(IN) LOB/BFILE 句柄is_equal(OUT) TRUE 表示相等,FALSE 表示不等

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.6 Direct Path Loading 方法

1. OCIDirPathAbort

描述取消当前装载的数据格式sword OCIDirPathAbort ( OCIDirPathCtx *dpctx,OCIError *errhp );

参数

参数描述dpctx(IN) dp 环境句柄errhp (INOUT) 错误句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

2. OCIDirPathColArrayEntryGet

描述获取direct path 列绑定的信息。

格式sword OCIDirPathColArrayEntryGet ( OCIDirPathColArray *dpca,

OCIError *errhp,ub4 rownum,ub2 colIdx,ub1 **cvalpp,ub4 *clenp,

## 第7 章 DM DCI 编程指南

ub1 *cflgp );

参数

参数描述dpca (IN/OUT) direct pathcolumn array 句柄errhp (INOUT) 错误句柄rownum (IN) 行偏移colIdx (IN) 列号cvalpp (IN/OUT) 绑定地址缓冲区clenp (IN/OUT) 长度缓冲区cflgp (IN/OUT) 标志缓冲区

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

3. OCIDirPathColArrayEntrySet

描述绑定direct path 行数据。

格式sword OCIDirPathColArrayEntrySet ( OCIDirPathColArray *dpca,

OCIError *errhp,ub4 rownum,ub2 colIdx,ub1 *cvalp,ub4 clen,

ub1 cflg );

参数

参数描述dpca(IN/OUT) direct pathcolumn array 句柄errhp(INOUT) 错误句柄rownum(IN) 行偏移colIdx(IN) 行号cvalp(IN) 数据地址clen(IN) 长度cflg(IN) 数据标志

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCIDirPathColArrayReset

描述清除direct path 列绑定的信息。

格式sword OCIDirPathColArrayReset ( OCIDirPathColArray *dpca,

## 第7 章 DM DCI 编程指南

OCIError *errhp );

参数

参数描述

dpca(IN) direct pathcolumn array 句柄errhp(INOUT) 错误句柄返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCIDirPathColArrayToStream

描述将绑定的行数据转换为发送到服务的流数据。

格式sword OCIDirPathColArrayToStream ( OCIDirPathColArray *dpca,

OCIDirPathCtx const *dpctx,OCIDirPathStream *dpstr,OCIError *errhp,ub4 rowcnt,

ub4 rowoff );

参数

参数描述dpca (IN) direct pathcolumn array 句柄dpctx (IN) direct path 环境句柄dpstr (IN /OUT) direct path 流句柄errhp (INOUT) 错误句柄rowcnt (IN) 转换行数rowoff (IN) 转换行偏移

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCIDirPathDataSave

描述将数据永久性保存至服务器。

格式sword OCIDirPathDataSave ( OCIDirPathCtx *dpctx,

OCIError *errhp,

ub4 action );

参数

参数描述dpctx(IN) direct path 环境句柄errhp(INOUT) 错误句柄

## 第7 章 DM DCI 编程指南

指示进行数据保存后的行为。

action(IN)仅支持OCI_DIRPATH_DATASAVE_SAVEONLY 选项，忽略其他选项

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

7. OCIDirPathFinish

描述完成数据装载。

格式sword OCIDirPathFinish ( OCIDirPathCtx *dpctx,OCIError *errhp );

参数

参数描述dpctx(IN) direct path 环境句柄errhp(INOUT) 错误句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

8. OCIDirPathLoadStream

描述将流数据发送到服务器。

格式sword OCIDirPathLoadStream ( OCIDirPathCtx *dpctx,

OCIDirPathStream *dpstr,

OCIError *errhp );

参数

参数描述dpctx(IN) direct path 环境句柄dpstr(IN) direct path 流句柄errhp(INOUT) 错误句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

9. OCIDirPathPrepare

描述准备装载数据。

格式sword OCIDirPathPrepare ( OCIDirPathCtx *dpctx,

OCISvcCtx *svchp,

OCIError *errhp );

## 第7 章 DM DCI 编程指南

参数

参数描述dpctx(IN) direct path 环境句柄svchp(IN) 上下文句柄errhp(INOUT) 错误句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

10. OCIDirPathStreamReset

描述清除流句柄中的数据，为下一次装载做准备。

格式sword OCIDirPathStreamReset ( OCIDirPathStream *dpstr,OCIError *errhp );

参数

参数描述dpstr(IN) direct path 流句柄errhp(INOUT) 错误句柄

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.7 Transaction 方法

1. OCITransCommit

描述提交SQL 的执行动作。

格式sword OCITransCommit ( OCISvcCtx *svchp,

OCIError *errhp,

ub4 flags );

参数

参数描述svchp(IN) 上下文句柄errhp(INOUT) 错误信息句柄flags(IN) 保留参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

2. OCITransDetach

## 第7 章 DM DCI 编程指南

描述将事务从会话剥离。

格式sword OCITransDetach ( OCISvcCtx *svchp,

OCIError *errhp,

ub4 flags );

参数

参数描述svchp(IN) 上下文句柄errhp(INOUT) 错误信息句柄flags(IN) 保留参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

3. OCITransRollback

描述回滚SQL 的执行动作。

格式sword OCITransRollback ( dvoid *svchp,

OCIError *errhp,

ub4 flags );

参数

参数描述svchp(IN) 上下文句柄errhp(INOUT) 错误信息句柄flags(IN) 保留参数

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCITransStart

描述启动事务。

格式word OCITransStart ( OCISvcCtx *svchp,

OCIError *errhp,uword timeout,

ub4 flags );

参数

参数描述

## 第7 章 DM DCI 编程指南

svchp (INOUT) 上下文句柄errhp (INOUT) 错误句柄timeout(IN) 事务超时，不支持该设置，忽略输入flags(IN) 事务属性标识

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.8 Miscellaneous 方法

1. OCIErrorGet

描述获取OCI 操作失败产生的错误信息。

格式sword OCIErrorGet ( dvoid *hndlp,

ub4 recordno,text *sqlstate,sb4 *errcodep,text *bu fp,ub4 bufsiz,ub4 type );

参数

参数描述hndlp(IN) 错误信息句柄或环境信息句柄错误信息位置，目前只支持一条错误信息，recordno(IN)所以请把该参数置为1 sqlstate(OUT) 错误的状态码errcodep(OUT) 错误码bufp(OUT) 错误的描述信息bufsiz(IN) bufp 所指的缓冲区大小type(IN) 句柄类型（错误句柄或环境句柄）

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

#### 7.3.3.9 date_datetime_inteval_fun 方法

1. OCIDateTimeFromText

描述从字符串转化成OCIDateTime*类型。

格式

## 第7 章 DM DCI 编程指南

sword OCIDateTimeFromText ( dvoid *hndl,

OCIError *err,const OraText *date_str,size_t dstr_length,const OraText *fmt,ub1 fmt_length,const OraText *lang_name,size_t lang_length,

OCIDateTime *datetime );

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄date_str(IN) 时间字符串dstr_length(IN) 时间字符串长度fmt(IN) 时间转换格式fmt_length(IN) 时间转换格式长度lang_name(IN) 语言串lang_length(IN) 语言串长度datetime(IN/OUT) OCIDateTime*类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

2. OCIDateTimeToText

描述从OCIDateTime*类型转换成字符串。

格式sword OCIDateTimeToText ( dvoid *hndl,

OCIError *err,OCIDateTime *datetime const OraText *fmt,ub1 fmt_length,ub1 fsprec,const OraText *lang_name,size_t lang_length,size_t *buf_size,const OraText *buf);

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄

## 第7 章 DM DCI 编程指南

datetime(IN/OUT) OCIDateTime*类型fmt(IN) 时间转换格式fmt_length(IN) 时间转换格式长度fsprec(IN) 保留毫秒位数lang_name(IN) 语言串lang_length(IN) 语言串长度date_str(IN) 时间字符串缓冲区dstr_length(IN) 时间字符串缓冲区长度

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

3. OCIDateTimeGetDate

描述从OCIDateTime*类型获取日期。

格式

```
OCIDateTimeGetDate(         dvoid       *hndl,
OCIError    *err,
CONST  OCIDateTime *datetime,
sb2         *yr,
ub1         *mnth,
ub1         *dy);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄datetime(IN) OCIDateTime*类型yr（OUT） 年mnth（OUT）月dy（OUT） 日

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

4. OCIDateTimeGetTime

描述从OCIDateTime*类型获取时间。

格式

```
OCIDateTimeGetTime(     dvoid       *hndl,
OCIError    *err,
CONST  OCIDateTime *datetime,
ub1         *hr,
ub1         *mm,
```

## 第7 章 DM DCI 编程指南

```
ub1         *ss,
ub4         *fsec);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄datetime(IN) OCIDateTime*类型hr（OUT） 时mm（OUT）分ss（OUT） 秒fsec 毫秒

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

5. OCIIntervalSetYearMonth

描述设置OCIinterval 间隔年月类型的年和月。

格式

```
OCIIntervalSetYearMonth(       dvoid       *hndl,
OCIError    *err,
sb4         yr,
sb4         mnth,
OCIInterval  *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄yr（IN） 年mnth（IN） 月result（OUT）间隔年月类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

6. OCIIntervalGetYearMonth

描述获取OCIinterval 间隔年月类型的年和月。

格式

```
OCIIntervalGetYearMonth(dvoid  *hndl,
OCIError  *err,
sb4  *yr,
sb4  *mnth,
```

## 第7 章 DM DCI 编程指南

```
CONST OCIInterval *interval);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄yr（OUT） 年mnth（OUT）月result（IN） 间隔年月类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

7. OCIIntervalSetDaySecond

描述设置OCIinterval 间隔日时类型的日、时、分和秒。

格式

```
OCIIntervalSetDaySecond(        dvoid       *hndl,
OCIError    *err,
sb4         dy,
sb4         hr,
sb4         mm,
sb4         ss,
sb4         fsec,
OCIInterval *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄dy（IN） 日Hr (IN) 时Mm(IN) 分ss（IN） 秒Fsec(IN) 毫秒result（OUT）间隔日时类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

8. OCIIntervalGetDaySecond

描述获取OCIinterval 间隔日时类型的日、时、分和秒。

格式

```
OCIIntervalGetDaySecond(       dvoid       *hndl,
```

## 第7 章 DM DCI 编程指南

```
OCIError    *err,
sb4         dy,
sb4         hr,
sb4         mm,
sb4         ss,
sb4         fsec,
OCIInterval *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄dy（OUT）日hr (OUT) 时mm(OUT) 分ss（OUT）秒fsec(OUT) 毫秒result(IN） 间隔日时类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

9. OCIIntervalCompare

描述比较两个OCIinterval 类型的值是否相等。

格式

```
OCIIntervalCompare(        dvoid        *hndl,
OCIError     *err,
OCIInterval   *inter1,
OCIInterval   *inter2,
sword        *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄inter1 (IN）间隔类型inter12(IN）间隔类型result(OUT) 结果

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

10. OCIIntervalAdd

描述返回两个interval 类型的和。

格式

## 第7 章 DM DCI 编程指南

OCIIntervalAd`d( dvoid *hndl,`

```
OCIError    *err,
OCIInterval  *addend1,
OCIInterval  *addend2,
OCIInterval  *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄inter1 (IN）间隔类型inter12(IN）间隔类型result(OUT) 结果

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

11. OCIIntervalAssign

描述OCIinterval 类型的赋值。

格式OCIInterval`Assign( dvoid` `*hndl,`

```
OCIError  *err,
CONST OCIInterval *ininter,
OCIInterval  *outinter);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄ininter (IN） 间隔类型outinter(OUT）间隔类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

12. OCIIntervalFromText

描述OCIinterval 类型的值的从文本构造。

格式

```
OCIIntervalFromText(         dvoid            *hndl,
OCIError         *err,
CONST OraText   *inpstr,
size_t            str_len,
```

## 第7 章 DM DCI 编程指南

```
OCIInterval       *result);
```

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄inpstr (IN） Interval 字符串str_len(IN）串长度result(OUT) 返回的OCIinterval*类型

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

13. OCIIntervalCheck

描述OCIinterval 类型的值的检查。

格式

```
OCIIntervalCheck(           dvoid  *hndl,
OCIError  *err,
CONST OCIInterval *interval,
```

`ub4` *valid);

参数

参数描述hndl(IN) 会话信息句柄err(INOUT) 错误信息句柄interval (IN）间隔类型valid(OUT）是否合法

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

14. OCINumberToInt

描述OCINumber 类型转化成Int。

格式

```
OCINumberToInt( OCIError        *err,
CONST OCINumber *number,
uword           rsl_length,
uword           rsl_flag,
dvoid           *rsl);
```

参数

参数描述

## 第7 章 DM DCI 编程指南

err(INOUT) 错误信息句柄number(IN) 要转化的OCINumber rsl_length(IN) Int 缓冲区的大小rsl_flag(IN) 输出的标识：OCI_NUMBER_UNSIGNED 或OCI_NUMBER_SIGNED rsl(IN) int 指针

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

15. OCINumberFromInt

描述从Int 转化成OCINumber 类型。

格式

```
OCINumberFromInt(          OCIError    *err,
CONST dvoid *inum,
uword       inum_length,
uword       inum_s_flag,
OCINumber   *number);
```

参数

参数描述err(INOUT) 错误信息句柄inum (IN) int 指针inum_length (IN) Int 缓冲区的大小inum_s_flag (IN) 标识：OCI_NUMBER_UNSIGNED 或OCI_NUMBER_SIGNED number(OUT) 转化后的OCINumber

返回值成功返回OCI_SUCCESS，失败返回OCI_ERROR。

## 7.4 使用DM DCI 编程基本步骤

一个应用程序中，我们是通过调用DCI 提供的库函数来实现对达梦数据库的操纵的。

为了与oracle 兼容，DCI 提供的函数都是以OCI 开头的与OCI 同名的函数，比如创建OCI环境的OCI 函数：OCIEnvCreate()。OCI 函数的一个特点或者说是难点就是它的参数特别多，函数往往都有十几个参数。一个DCI 应用程序的基本结构包括：

1. 初始化OCI 环境和线程；
2. 分配必要的句柄与数据结构；
3. 建立与数据库的连接以及创建用户会话；
4. 通过SQL 与DM 服务器交换数据，而后再做数据处理；
5. 结束用户会话与断开与数据库的连接；
6. 释放在程序中所分配的句柄。

如图7.1 所示：

## 第7 章 DM DCI 编程指南

创建OCI环境（第一步）分配句柄和数据结构（第二步）连接数据库，开始会话（第三步）执行SQL，处理语句（第四步）结束会话，断开连接（第五步）释放句柄（第六步）图7.1 DCI 程序步骤

一个SQL 语句在OCI 应用程序中的执行步骤一般如下：

1. 准备SQL 语句。调用函数OCIStmtPrepare( )；
2. 在SQL 语句中绑定需要输入到SQL 语句中的变量。对于DML 语句来说，由于它

带有输入变量，我们可以通过调用一个或者多个函数OCIBindByPos()、OCIBindByName()等把输入变量的地址绑定在DML 语句中的占位符中；

3. 执行SQL 语句。调用OCIStmrExecute()函数。对于DDL 语句到这一步就完成了一

个语句的执行；

4. 描述SQL 中输出的数据。如果有必要的话，我们可以调用函数OCIParamGet()与

OCIAttGet( )来获取我们所读取的记录的字段个数、字段的数据类型以及字段数据定义的最大长度。

过程以及过程中调用到的函数如图7.2 所示：

准备SQL OCIStmtPrepare()OCIStmtPrepare()OCIBindByPos()绑定 OCIBindObject()OCIBindDynamic()OCIBindArrayByStruct()执行 OCIStmtExecute()OCIParamGet()描述OCIAttrGet()OCIDefineByPos()OCIDefineObject()定义变量 OCIDefineDynamic()OCIBindDynamic()OCIDefineArrayByStruct()获取数据 OCIStmtFetch()

图7.2 过程以及过程中调用到的函数

图7.2 是一个一般SQL 执行的流程图，对于不同的SQL 语句，所需要的步骤也有所不

## 第7 章 DM DCI 编程指南

同。对于DDL 语句，由于没有数据的输入与输出，仅仅涉及到一些权限与定义或者删除数据库中的对象的问题，因此只需要上图的第一步与第三步便可以了。而对于DML 语句，由于有数据的输入与输出，因此需要的步骤就多一些。

下面通过一个简单的Windows 环境下的示例来说明DM DCI 的调用方式。实现了对bookshop 示例库中的person 模式下的person 表进行的增、删、改、查的基本操作。在编译的过程中需要用到DM 的头文件dci.h，在连接阶段需要用到dmoci.lib 这个库文件，在执行阶段需要用到动态库dmoci.dll、dmcalc.dll、dmelog.dll、dmmen.dll、dmos.dll、dmutl.dll、dmclientlex.dll、dmfldr_dll.dll、dmbcast.dll、dmdta.dll、dmcfg.dll、dmstrt.dll、dmcpr.dll、dmcyt.dll、dmcvt.dll、dmmout.dll、dmdpi.dll、dmcomm.dll。

/************************************************************************//* DCI编程实例 *//************************************************************************/#include <stdio.h>#include <string.h>#include <stdlib.h>#include <malloc.h>#include "DCI.h"/* 声明句柄 */OCIEnv *envhp; /* 环境句柄 */OCISvcCtx *svchp; /* 服务环境句柄 */OCIServer *srvhp; /* 服务器句柄 */OCISession *authp; /* 会话句柄 */OCIStmt *stmthp; /* 语句句柄 */OCIDescribe *dschp; /* 描述句柄 */OCIError *errhp; /* 错误句柄 */OCIDefine *defhp[3]; /* 定义句柄 */OCIBind *bidhp [4]; /* 绑定句柄 */sb2 ind[3]; /* 指示符变量 *//* 绑定select结果集的参数 */text szpersonid[11]; /* 存储personid列 */text szsex[2]; /* 存储sex列 */text szname[51]; /* 存储name列 */text szemail[51]; /* 存储mail列 */text szphone[26]; /* 存储phone列 */char sql[256]; /* 存储执行的sql语句*/int main(int argc, char *argv[]){char strServerName[50];

char strUserName[50];

char strPassword[50];

int ret;

text errbuf[100];

/* 设置服务器，用户名和密码 */

## 第7 章 DM DCI 编程指南

strcpy(strServerName,"localhost");

strcpy(strUserName,"SYSDBA");

strcpy(strPassword,"SYSDBA");

/* 初始化OCI应用环境*/OCIInitialize(OCI_DEFAULT, NULL, NULL, NULL, NULL);

/* 初始化环境句柄 */OCIEnvInit(&envhp, OCI_DEFAULT,0, 0);

/* 分配句柄 */OCIHandleAlloc(envhp, (dvoid**)&svchp, OCI_HTYPE_SVCCTX, 0, 0); /*服务器环境句柄*/OCIHandleAlloc(envhp, (dvoid**)&srvhp, OCI_HTYPE_SERVER, 0, 0); /* 服务器句柄*/OCIHandleAlloc(envhp, (dvoid**)&authp, OCI_HTYPE_SESSION, 0, 0); /* 会话句柄 */OCIHandleAlloc(envhp, (dvoid**)&errhp, OCI_HTYPE_ERROR, 0, 0); /* 错误句柄 */OCIHandleAlloc(envhp, (dvoid**)&dschp, OCI_HTYPE_DESCRIBE,0,0); /*描述符句柄*//* 连接服务器 */OCIServerAttach(srvhp, errhp,(text *)strServerName,(sb4)strlen(strServerName),OCI_DEFAULT);

/* 设置用户名和密码 */OCIAttrSet(authp,OCI_HTYPE_SESSION,(text *)strUserName,(ub4)strlen(strUserName),OCI_ATTR_USERNAME,errhp);

OCIAttrSet(authp,OCI_HTYPE_SESSION,(text *)strPassword,(ub4)strlen(strPassword), OCI_ATTR_PASSWORD,errhp);

/* 设置服务器环境句柄属性 */OCIAttrSet ((dvoid*)svchp, (ub4) OCI_HTYPE_SVCCTX,(dvoid*)srvhp, (ub4) 0, OCI_ATTR_SERVER, errhp);

OCIAttrSet(svchp, OCI_HTYPE_SVCCTX,(dvoid*)authp,0, OCI_ATTR_SESSION, errhp);

/* 创建并开始一个用户会话 */OCISessionBegin (svchp, errhp, authp,OCI_CRED_RDBMS,OCI_DEFAULT);

OCIHandleAlloc(envhp, (dvoid**)&stmthp,OCI_HTYPE_STMT, 0, 0); /* 语句句柄 *//************************************************************************//* 查询person表 *//************************************************************************/strcpy(sql, "select personid, name, phone from person.person");

/* 准备SQL语句 */OCIStmtPrepare(stmthp, errhp,(text *)sql, strlen(sql),OCI_NTV_SYNTAX, OCI_DEFAULT);

/* 绑定输出列 */OCIDefineByPos (stmthp,&defhp[0],errhp, 1,(ub1*)szpersonid,sizeof(szpersonid),SQLT_STR,&ind[0], 0, 0, OCI_DEFAULT);

OCIDefineByPos (stmthp,&defhp[1],errhp, 2,(ub1*)szname,sizeof(szname),SQLT_STR,&ind[1], 0, 0, OCI_DEFAULT);

OCIDefineByPos (stmthp,&defhp[2],errhp, 3,(ub1*)szphone,sizeof(szphone),SQLT_STR,&ind[2], 0, 0, OCI_DEFAULT);

/* 执行SQL语句 */ret=OCIStmtExecute(svchp, stmthp,errhp, (ub4)0, 0, NULL, NULL, OCI_DEFAULT);

## 第7 章 DM DCI 编程指南

if (ret != 0){OCIErrorGet(errhp, 1, NULL, &ret, (OraText *)errbuf, sizeof(errbuf), OCI_HTYPE_ERROR);

printf("%s\n",errbuf);

}printf("%-10s%-10s%-10s\n", "PERSONID", "NAME", "PHONE");

while((OCIStmtFetch(stmthp, errhp,1,OCI_FETCH_NEXT,OCI_DEFAULT))!=OCI_NO_DATA){printf("%-10s", szpersonid);

printf("%-10s", szname);

printf("%-10s\n", szphone);

}/************************************************************************//* 向person表插入一条数据 *//************************************************************************/memset(sql, 0, sizeof(sql));

strcpy(sql, "insert into person.person(sex, name, email, phone) values(:sex,:name,:email,:phone)");

/* 准备SQL语句 */OCIStmtPrepare(stmthp, errhp,(text *)sql, strlen(sql),OCI_NTV_SYNTAX, OCI_DEFAULT);

/* 设置输入参数 */memset(szsex, 0, sizeof(szsex));

strcpy(szsex, "M");

memset(szname, 0, sizeof(szname));

strcpy(szname, "张三");

memset(szemail, 0, sizeof(szemail));

strcpy(szemail, "zhangsan@dameng.com");

memset(szphone, 0, sizeof(szphone));

strcpy(szphone, "027-87588000");

/* 绑定输入列 */OCIBindByName (stmthp, &bidhp[0], errhp, ":sex", 4, szsex, strlen((char*)szsex),SQLT_AFC, NULL, NULL, NULL, 0, NULL, 0);

OCIBindByName (stmthp, &bidhp[1], errhp, ":name", 5, szname, strlen((char*)szname),SQLT_AFC, NULL, NULL, NULL, 0, NULL, 0);

OCIBindByName (stmthp, &bidhp[2], errhp, ":email", 6, szemail, strlen((char*)szemail),SQLT_AFC, NULL, NULL, NULL, 0, NULL, 0);

OCIBindByName (stmthp, &bidhp[3], errhp, ":phone", 6, szphone, strlen((char*)szphone),SQLT_AFC, NULL, NULL, NULL, 0, NULL, 0);

/* 执行SQL语句 */ret=OCIStmtExecute(svchp, stmthp, errhp, (ub4)1, (ub4) 0, (CONST OCISnapshot*) 0, (OCISnapshot*) 0,(ub4) OCI_DEFAULT);

if (ret != 0){

## 第7 章 DM DCI 编程指南

OCIErrorGet(errhp, 1, NULL, &ret, (OraText *)errbuf, sizeof(errbuf), OCI_HTYPE_ERROR);

printf("%s\n",errbuf);

}/* 提交到数据库 */OCITransCommit(svchp, errhp, OCI_DEFAULT);

/************************************************************************//* 更新person表 *//************************************************************************/memset(sql, 0, sizeof(sql));

strcpy(sql, "update person.person set sex='M',name='Liuhuan',email='liujian@mail',phone='13636396811'WHERE personid='1'");

/* 准备SQL语句 */OCIStmtPrepare(stmthp, errhp,(text *)sql, strlen(sql),OCI_NTV_SYNTAX, OCI_DEFAULT);

/* 执行SQL语句 */ret=OCIStmtExecute(svchp, stmthp, errhp, (ub4)1, (ub4) 0, (CONST OCISnapshot*) 0, (OCISnapshot*) 0,(ub4) OCI_DEFAULT);

if (ret != 0){OCIErrorGet(errhp, 1, NULL, &ret, (OraText *)errbuf, sizeof(errbuf), OCI_HTYPE_ERROR);

printf("%s\n",errbuf);

}/* 提交到数据库 */OCITransCommit(svchp, errhp, OCI_DEFAULT);

/************************************************************************//* 删除person表的ID为的数据,首先要在数据库中存在这条记录 *//************************************************************************/memset(sql, 0, sizeof(sql));

strcpy(sql, "delete from person.person WHERE personid=:1");

/* 准备SQL语句 */OCIStmtPrepare(stmthp, errhp,(text *)sql, strlen(sql),OCI_NTV_SYNTAX, OCI_DEFAULT);

/* 绑定输入参数 */memset(szpersonid, 0, sizeof(szpersonid));

strcpy(szpersonid, "20");

OCIBindByPos(stmthp, &bidhp[0], errhp, 1, szpersonid, strlen((char*)szpersonid),SQLT_AFC, NULL, NULL, NULL, 0, NULL, 0);

/* 执行SQL语句 */ret=OCIStmtExecute(svchp, stmthp, errhp, (ub4)1, (ub4) 0, (CONST OCISnapshot*) 0, (OCISnapshot*) 0,(ub4) OCI_DEFAULT);

if (ret != 0){OCIErrorGet(errhp, 1, NULL, &ret, (OraText *)errbuf, sizeof(errbuf), OCI_HTYPE_ERROR);

printf("%s\n",errbuf);

}/* 提交到数据库 */

## 第7 章 DM DCI 编程指南

OCITransCommit(svchp, errhp, OCI_DEFAULT);

//结束会话OCISessionEnd(svchp, errhp, authp, (ub4) 0);

//断开与数据库的连接OCIServerDetach(srvhp, errhp, OCI_DEFAULT);

//释放OCI句柄OCIHandleFree((dvoid*)dschp, OCI_HTYPE_DESCRIBE);

OCIHandleFree((dvoid*)stmthp, OCI_HTYPE_STMT );

OCIHandleFree((dvoid*)errhp, OCI_HTYPE_ERROR);

OCIHandleFree((dvoid*)authp, OCI_HTYPE_SESSION );

OCIHandleFree((dvoid*)svchp, OCI_HTYPE_SVCCTX);

OCIHandleFree((dvoid*)srvhp, OCI_HTYPE_SERVER);

return 0;

}

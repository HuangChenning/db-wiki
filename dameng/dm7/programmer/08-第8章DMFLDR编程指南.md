---
title: "第8章 DM FLDR编程指南"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=249"
tags:
  - dameng
  - dm7
  - programmer
---

## 第8 章 DM FLDR 编程指南

## 8.1 DM FLDR 接口介绍

快速装载接口FLDR 是达梦数据库提供的能够快速将文本数据载入DM 数据库的一种数据载入方式。用户通过使用FLDR 接口能够把按照一定格式排序的文本数据以简单、快速、高效的方式载入到达梦数据库中。

## 8.2 DM FLDR 接口说明

### 8.2.1 返回值说明

DM FLDR 接口有以下五种返回值：

FLDR_SUCCESS：接口成功执行FLDR_ERROR：接口执行出错FLDR_INVALID_HANDLE：用户使用错误的句柄FLDR_SUCCESS_WITH_INFO：接口执行成功但有警告信息FLDR_NO_DATA：数据未找到

### 8.2.2 接口说明

1． fldr_alloc描述：

用于分配快速装载对象实例，所有快速装载都将通过该句柄进行操作。

格式：

FLDR_RETURN fldr_alloc(fhinstance *instance);

参数：

instance（输出） 快速装载实例的句柄返回值：

FLDR_SUCCESS、FLDR_ERROR注释：

该函数分配出用于快速装载实例句柄，用户必须首先调用该函数获得快速装载的实例句柄，只有通过该句柄才能进行后续的快速装载操作2． fldr_free

## 第8 章 DM FLDR 编程指南

描述：

释放快速装载实例句柄。

格式：

FLDR_RETURN fldr_free(fhinstance instance);

参数：

instance（输入） 快速装载实例的句柄返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

释放快速装载实例句柄，将该实例句柄上所有快速装载所占用的资源释放。

如果用户调用fldr_initialize 进行初始化，而没有调用fldr_uninitialize 通知装载结束，调用此函数将会自动结束该此装载，未使用fldr_batch 或者fldr_finish 进行提交的行将会被抛弃。

3． fldr_set_attr描述：

设置快速装载实例的属性。

格式：

FLDR_RETURN

fldr_set_attr(fhinstance instance,fsint4 attrid,fpointer value,fsint4 length);

参数：

instance（输入） 快速装载实例的句柄attrid(输入) 属性标识，指出将要设置的属性，关于属性详细内容参见注释部分value (输入) 属性值，根据attrid 不同该参数的意义不同，其可能是32 位的整数或者指向一片内存的指针length（输入） 属性值长度。value 参数为指向一片内存数据的指针时，该参数用来指出该内存数据的长度，如果value 做为整数传入时，该参数忽略其意义。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

该函数可在调用fldr_initialize 之前调用，用户可根据本地及服务器的环境特征设置本次快速装载的属性，从而获得较高的效率。

在fldr_initialize 之后对该函数进行调用将返回执行不成功的错误。

可设置的属性见下表：

属性（attrid） 属性说明（value） value类型

## 第8 章 DM FLDR 编程指南

FLDR_ATTR_SERVER 服务器地址。 指针FLDR_ATTR_UID 用户名。 指针FLDR_ATTR_PWD 密码。 指针FLDR_ATTR_PORT 服务器端口整数FLDR_ATTR_TABLE 目标表指针FLDR_ATTR_SET_INDENTITY 是否插入自增列（默认FALSE），如果设置为TRUE 整数则服务器将使用指定的数据作为自增列的数据进行插入，如果为FALSE则对于自增列服务器将自动生成数据插入，忽略指定的数据FLDR_ATTR_DATA_SORTED 数据是否已按照聚集索引排序。默认为FALSE 整数FLDR_ATTR_INDEX_OPTION 1不刷新二级索引，数据按照索引先排序，装载完整数后再将排序的数据插入索引2不刷新二级索引，数据装载完成后重建所有二级索引(默认为1)FLDR_ATTR_DATA_SIZE 指出本地缓冲数据的最大行数。默认为1000，最大整数为10000，最小为100。

FLDR_ATTR_INERT_ROWS 8字节整数。只读属性。当前发送到服务器的行数。整数FLDR_ATTR_COMMIT_ROWS 8字节整数。只读属性。当前提交到数据库的行数整数FLDR_ATTR_PROCESS_ROWS 8字节整数。只读属性。用户绑定的数据行数整数FLDR_ATTR_SEND_NODE_NU 发送链表节点个数，默认128，最大为20480，最小整数M为16。多线程处理中每个线程所支配的向服务器发送数据节点的个数。

FLDR_ATTR_TASK_THREAD_ 任务线程数整数NUM FLDR_ATTR_BAD_FILE 记录出错数据的文件，出错数据将全部使用字符串指针表示FLDR_ATTR_DATA_CHAR_SE 设置输入数据字符类型的字符集整数T FLDR_ATTR_LOG_FILE 指定日志记录文件指针FLDR_ATTR_SSL_PATH 在加密通讯模式下加密证书的路径指针FLDR_ATTR_SSL_PWD 加密证书的密钥指针FLDR_ATTR_LOCAL_CODE 指定本地字符集整数FLDR_ATTR_MPP_LOCAL_FL 指明是否是mpp模式下的单节点数据。默认值为整数AG FALSE

4． fldr_get_attr描述：

获取快速装载实例的属性。

格式：

FLDR_RETURN fldr_get_attr(fhinstance instance,fsint4 attrid,

## 第8 章 DM FLDR 编程指南

fpointer buffer,fsint4 buf_sz,fsint4* length);

参数：

instance（输入） 快速装载实例的句柄attrid(输入) 属性标识，指出将要获取的属性，关于属性详细内容参见fldr_set_attr()的注释部分buffer (输出) 将属性值填入buffer 所指向的内存中buf_sz（输入）属性缓冲区的长度length（输出） 向buffer 指向的缓冲区填写的数据的长度。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

参见fldr_set_attr()函数说明中各属性说明。

5． fldr_initialize描述：

初始化当前快速装载实例。

格式：

FLDR_RETURN fldr_initialize(fhinstance instance,fint4 type,fpointer conn,fchar* server,fchar * uid,fchar* pwd,fchar* table);

参数：

instance（输入） 快速装载实例的句柄type (输入) 可用值为FLDR_TYPE_BIND：用户使用绑定方式进行装载conn (输入) 通过dpi 分配的连接对象，如果该参数不为NULL 值，则使用用户指定的连接作为导入的连接，忽略server,uid,pwd 这三个参数server (输入) 链接的服务器。将被记录到实例的FLDR_ATTR_SERVER 属性中uid (输出) 登录用户。将被记录到实例的FLDR_ATTR_UID 属性中pwd（输入） 用户密码。将被记录到实例的FLDR_ATTR_PWD 属性中table（输入） 进行快速装载的表。将被记录到实例的FLDR_ATTR_TABLE 属性中返回值：

FLDR_SUCCESS、 FLDR_SUCCESS_WITH_INFO、 FLDR_ERROR、FLDR_INVALID_HANDLE

## 第8 章 DM FLDR 编程指南

注释：

根据用户通过fldr_set_attr 设置的属性初始化快速装载环境，如果用户未指定连接则根据用户提供的服务器、用户和密码建立到服务器的连接。

6． fldr_uninitialize描述：

释放快速装载实例所占用的资源。

格式：

FLDR_RETURN fldr_uninitialize(fhinstance instance,fint4 flag);

参数：

instance（输入） 快速装载实例的句柄flag (输入) 指出是否对已插入的数据进行事务提交，以永久保存到数据库。

取值：FLDR_UNINITILIAZE_COMMIT为是，FLDR_UNINITILIAZE_ROLLBACK为否。如果用户调用了fldr_finish结束导入则该参数将不会起任何作用。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

用于释放所占用快速装载实例所占用的资源。用户在调用该函数后可重新初始化快速装载句柄，进行新的数据装载。

7． fldr_bind描述：

绑定输入列。

格式：

FLDR_RETURN fldr_bind(fhinstance instance,fsint2 col_idx,fsint2 type,fchar* date_fmt,fpointer data,fsint4 data_len,fsint4* ind_len);

参数：

instance（输入） 快速装载实例的句柄col_idx (输入) 绑定列的编号。从1 开始计数，对应快速装载的表的相应列。

type (输入) 用户绑定数据的C类型date_fmt（输入） 当绑定列对应的表的列为时间日期类型，且绑定的c数据为

## 第8 章 DM FLDR 编程指南

FLDR_C_CHAR 类型，该参数为字符串到日期类型的格式串。其他情况，忽略该绑定输入data（输入） 指向用于存放数据内存的地址指针， 可在fldr_sendrows 之前对其进行填充，快速装载接口在用户调用fldr_sendrows 时读取数据内容data_len（输入） 用于记录单行数据最大的长度。当进行多行绑定的时候，对于变长的C类型，根据该参数内容进行便宜的计算。对于固定长度的C数据类型，该参数内容被忽略ind_len（输入） 用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向fsint4 类型的数组。如果地址中保存的值为FLDR_DATA_NULL，绑定列的该行数据被视为空值。对于FLDR_C_BINARY 和FLDR_C_CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

支持绑定的C类型见下表：

类型宏定义说明二进制数据 FLDR_C_BINARY 变长字符数据 FLDR_C_CHAR 变长1 字节整型数据 FLDR_C_BYTE 定长2 字节整型数据 FLDR_C_SHORT 定长4 字节整型数据 FLDR_C_INT 定长8 字节整型数据 FLDR_C_BIGINT 定长单精度浮点数 FLDR_C_FLOAT 定长双精度浮点数 FLDR_C_DOUBLE 定长

8． fldr_bind_nth描述：

绑定输入列，fldr_bind 的多线程版本。

格式：

FLDR_RETURN fldr_bind_nth(fhinstance instance,fsint2 col_idx,fsint2 type,fchar* date_fmt,fpointer str_binds,fpointer data,fsint4 col_len,fsint4 data_len,fsint4* ind_len,fsint4 nth);

参数：

## 第8 章 DM FLDR 编程指南

instance（输入） 快速装载实例的句柄col_idx (输入) 绑定列的编号。从1 开始计数，对应快速装载的表的相应列。

type (输入) 用户绑定数据的C类型date_fmt（输入） 当绑定列对应的表的列为时间日期类型，且绑定的c数据为FLDR_C_CHAR 类型，该参数为字符串到日期类型的格式串。其他情况，忽略该绑定输入str_binds(输入） 字符串绑定内存data（输入） 指向用于存放数据内存的地址指针， 可在fldr_sendrows 之前对其进行填充，快速装载接口在用户调用fldr_sendrows 时读取数据内容col_len（输入） 列定义长度data_len（输入） 用于记录单行数据最大的长度。当进行多行绑定的时候，对于变长的C类型，根据该参数内容进行便宜的计算。对于固定长度的C数据类型，该参数内容被忽略ind_len（输入） 用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向fsint4 类型的数组。如果地址中保存的值为FLDR_DATA_NULL，绑定列的该行数据被视为空值。对于FLDR_C_BINARY 和FLDR_C_CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

nth（输入） 多线程绑定，第几个线程，从0 开始。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

支持绑定的C类型见下表：

类型宏定义说明二进制数据 FLDR_C_BINARY 变长字符数据 FLDR_C_CHAR 变长1 字节整型数据 FLDR_C_BYTE 定长2 字节整型数据 FLDR_C_SHORT 定长4 字节整型数据 FLDR_C_INT 定长8 字节整型数据 FLDR_C_BIGINT 定长单精度浮点数 FLDR_C_FLOAT 定长双精度浮点数 FLDR_C_DOUBLE 定长

9． fldr_sendrows描述：

发送行数。

格式：

FLDR_RETURN fldr_sendrows(fhinstance instance,fint4 rows);

参数：

instance（输入） 快速装载实例的句柄

## 第8 章 DM FLDR 编程指南

rows (输入) 在多行绑定的情况，指明绑定的行数。

返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE 10． fldr_sendrows_nth描述：

发送行数，fldr_sendrows 的多线程版本。

格式：

FLDR_RETURN fldr_sendrows_nth(fhinstance instance,fsint4 rows,fsint4 nth,fsint4 seq_no);

参数：

instance（输入） 快速装载实例的句柄rows (输入) 在多行绑定的情况，指明绑定的行数。

nth(输入） 多线程版本，第几个线程seq_no(输入） 数据批次的序号返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE 11． fldr_batch描述：

批量提交行数据，永久保存到服务器。

格式：

FLDR_RETURN fldr_batch(fhinstance instance,fsint8 *rows);

参数：

instance（输入） 快速装载实例的句柄rows (输出) 批量提交的行数返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE注释：

将上一次调用fldr_batch 之后所有fldr_sendrows 装载的行进行提交，永久保存到数据库中。

12． fldr_finish描述：

## 第8 章 DM FLDR 编程指南

结束一次批量操作。

格式：

FLDR_RETURN

fldr_finish(fhinstance instance);

参数：

instance（输入） 快速装载实例的句柄返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE 13． fldr_get_diag描述：

获取出错时的诊断信息。

格式：

FLDR_RETURN fldr_get_diag(

fhinstance instance,fsint4 rec_num,fint4 err_code,fchar* err_msg,fint4 buf_sz,fint4 *msg_len);

参数：

instance（输入） 快速装载实例的句柄rec_num（输入） 诊断信息索引号err_code（输出） 发生错误的错误码err_msg（输出） 错误消息缓冲区buf_sz（输入）缓冲区大小msg_len（输出） 错误信息在缓冲区中占用的大小返回值：

FLDR_SUCCESS、FLDR_ERROR、FLDR_INVALID_HANDLE、FLDR_NO_DATA注释：

当用户调用快速装载接口返回FLDR_ERROR 时，可通过该函数获取出错的错误信息，进行当前状况的判断。该函数出现错误将不会生成任何诊断信息。

14． fldr_exec_ctl_low描述：

类似命令行工具，通过控制文件，执行数据装载。

格式：

FLDR_RETURN

fldr_exec_ctl_low(fhinstance instance,

## 第8 章 DM FLDR 编程指南

fchar* ctl_buffer,fsint4 fldr_type,fsint8* row_count);

参数：

instance（输入） 快速装载实例的句柄ctl_buffer（输入） 控制文件buffer fldr_type（输入） 数据装载类型row_count（输出）返回成功装载的行数返回值：

FLDR_SUCCESS、FLDR_ERROR注释：

此接口让用户可以通过自定义程序实现数据快速装载。

## 8.3 编程实例

程序在编译的过程中需要用到DM 的头文件fldr.h，在连接阶段需要用到dmfldr_dll2.lib这个库文件，在执行阶段需要用到动态库dmfldr_dll.dll、dmbcast.dll、dmcalc.dll、dmelog.dll、dmmem.dll、dmos.dll、dmutl.dll、dmdta.dll、dmcfg.dll、dmstrt.dll、dmcpr.dll、dmcyt.dll、dmcvt.dll、dmmout.dll、dmcomm.dll、dmdpi.dll、dmclientlex.dll。这几个动态库在安装DM 时，已经被放到安装目录下。

#include "fldr.h"#include <stdio.h>#include <stdlib.h>#include <string.h>int main(){fhinstance instance;

FLDR_RETURN ret;

char server[20] = "192.168.0.35";

char user[20] = "SYSDBA";

char pwd[20] = "SYSDBA";

char table[20] = "TEST";

// 提前建好表CREATE TABLE TEST(C1 INT, C2 VARCHAR2(100));

int c1[100];

int c1_len[100];

char c2[100][100];

int c2_len[100];

int i;

for (i = 0; i < 100; i++){

## 第8 章 DM FLDR 编程指南

c1[i] = i;

sprintf(c2[i], "i = %d", i);

c2_len[i] = strlen(c2[i]);

}ret = fldr_alloc(&instance);

fldr_initialize(instance, FLDR_TYPE_BIND, NULL, server, user, pwd, table);

fldr_bind_nth(instance, 1, FLDR_C_INT, NULL, NULL, c1, 4, 0, c1_len, 0);

fldr_bind_nth(instance, 2, FLDR_C_CHAR, NULL, NULL, c2, 100, 100*100, c2_len, 0);

fldr_sendrows_nth(instance, 100, 0, 1);

fldr_uninitialize(instance, FLDR_UNINITILIAZE_COMMIT);

fldr_free(instance);

return 0;

}

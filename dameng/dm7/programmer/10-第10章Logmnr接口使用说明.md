---
title: "第10章 Logmnr接口使用说明"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=269"
tags:
  - dameng
  - dm7
  - programmer
---

## 第10 章 Logmnr 接口使用说明

Logmnr 包是达梦数据库的日志分析工具，达梦提供了JNI 接口和C接口，供应用程序直接调用。

## 10.1 JNI 接口

logmnr.jar 包是达梦数据库的日志分析工具的JNI 接口，供应用程序直接调用。

一般调用过程如下：

1. 初始化LOGMNR 环境；
2. 创建一个分析日志的连接；
3. 添加需要分析的日志文件；
4. 启动日志文件分析；
5. 获取完成分析的日志数据；
6. 终止日志文件分析；
7. 关闭当前连接；
8. 销毁LOGMNR 环境。

### 10.1.1 接口说明

logmnr.jar 包括两个类：LogmnrDll 和LogmnrRecord。logmnr.jar 位于DM 安装目录的jar文件夹下，例如：D:\dmdbms\jar\logmnr.jar。LogmnrDll 中包含了所有功能接口；LogmnrRecord是日志分析结果数据的返回值对应的对象类型。

#### 10.1.1.1 初始化环境

函数原型int LogmnrDll.initLogmnr();

功能说明初始化LOGMNR 环境。

参数说明无。

返回值0：初始化成功；

< 0 的值和异常：初始化失败。

## 第10 章 Logmnr 接口使用说明

#### 10.1.1.2 创建连接

函数原型long LogmnrDll.createConnect(String hostName, int port, String userName, String password);

功能说明创建一个分析日志的连接。

参数说明hostName：ip 或主库名。

port：端口号。

userName：用户名。

password：密码。

返回值创建的数据库连接标识ID。

#### 10.1.1.3 添加日志文件

函数原型int LogmnrDll.addLogFile(long connId, String logFileName, int option);

功能说明添加需要分析的归档日志文件。

参数说明connId：数据库连接标识ID。

logFileName：需要分析的归档日志文件名（绝对路径）。

option：可选配置参数。包括以下值：

1：结束当前日志挖掘（隐式调用endLogmnr，以前添加的归档日志文件将被清除），并增加新的归档日志文件。

2：删除日志文件。

3：增加的归档日志文件名。

返回值0：添加成功；

< 0 的值和异常：添加失败。

如果当前已经startLogmnr，则addLogFile 将报错，如果需要添加新的日志文件，需要先调用endLogmnr 结束当前日志分析后再添加文件。

## 第10 章 Logmnr 接口使用说明

#### 10.1.1.4 移除日志文件

函数原型int LogmnrDll.removeLogFile(long connId, String logFileName);

功能说明移除指定的归档日志文件。

参数说明connId：数据库连接标识ID。

logFileName：需要移除档日志文件名（绝对路径）。

返回值0：移除成功；

< 0 的值和异常：移除失败。

同addLogFile 一样，如果当前已经startLogmnr，则removeLogFile 将报错，如果需要移除日志文件，需要先调用endLogmnr 结束当前日志分析后再移除文件。

#### 10.1.1.5 启动日志分析

函数原型int LogmnrDll.startLogmnr(long connId, long trxid, String startTime, String endTime);

功能说明启动当前会话的归档日志文件分析，对添加的归档日志文件进行日志分析。

参数说明connId：数据库连接标识ID。

trxid：分析归档日志的事务id 号，默认为-1，表示不区分事务号。

startTime：分析归档日志的起始时间，默认1988/1/1。

endTime：分析归档日志的结束时间，默认2110/12/31。

返回值0：启动成功；

< 0 的值和异常：启动失败。

#### 10.1.1.6 获取数据

函数原型LogmnrRecord[]LogmnrDll.getData(long connId, int rownum);

## 第10 章 Logmnr 接口使用说明

功能说明获取日志文件分析结果数据。

参数说明connId：数据库连接标识ID。

rownum：获取行数。

返回值获取的logmnr 记录，为LogmnrRecord 对象数组，详见10.1.1.6.1 LogmnrRecord 对象说明。

##### 10.1.1.6.1 LogmnrRecord 对象说明

LogmnrRecord 对象支持的成员变量入下表所示。获取和设置这些变量可以使用相应的“get+成员变量”和“set+成员变量”方法。

成员变量类型说明scn long 当前记录的LSN startScn long 当前事务的起始LSN commitScn long 当前事务的截止LSN timestamp String 当前记录的创建时间startTimestamp String 当前事务的起始时间commitTimestamp String 当前事务的截止时间xid String 当前记录的事务ID 号操作类型包括start、insert、update、delete、commit、rollback operation String等语句操作类型。插入操作值为1，更新操作值为3，删除操作operationCode String 值为2，事务起始语句值为6，提交操作值为7，回滚操作值为36 rollBack int 当前记录是否被回滚（1 是0 否）segOwner String 执行这条语句的用户名tableName String 操作的表名rowId String 对应记录的行号rbasqn int 对应的归档日志文件号rbablk int RBASQN 所指日志文件的块号从0 开始rbabyte int RBABLK 所指块号的块内偏移dataObj int 对象ID 号dataObjv int 对象版本号sqlRedo String 当前记录对应的sql 语句rsId Stirng 记录集ID

## 第10 章 Logmnr 接口使用说明

连续sql 标志。如果sql 长度超过单个sql_redo 字段能存储ssn int 的长度，则sql 会被截断成多个sql 片段在结果集中“连续”返回与SSN 配合。最后一个片段的csf 值为0，其余片段的值csf int均为1。没因超长发生截断的sql 该字段值均为0 status int 日志状态。默认为0

#### 10.1.1.7 终止日志分析

函数原型int LogmnrDll.endLogmnr(long connId, int option);

功能说明终止当前会话的归档日志文件分析。

参数说明connId：数据库连接标识ID。

options：可选模式如下：

0：清除当前会话的归档日志文件分析环境，再次分析时需要重新add_logfile。

1：保留当前会话的归档日志文件分析环境，不需要重新add_logfile。

返回值0：终止成功；

< 0 的值和异常：终止失败。

#### 10.1.1.8 关闭连接

函数原型int LogmnrDll.closeConnect(long connId);

功能说明关闭当前连接，清理字典缓存等。

参数说明connId：数据库连接标识ID。

返回值0：关闭成功；

< 0 的值和异常：关闭失败。

#### 10.1.1.9 销毁环境

函数原型boolean LogmnrDll.deinitLogmnr();

## 第10 章 Logmnr 接口使用说明

功能说明销毁LOGMNR 环境。

参数说明无。

返回值0：添加销毁；

< 0 的值和异常：销毁失败。

#### 10.1.1.10 设置属性

函数原型int LogmnrDll.setAttr(long connId, int attr, int attr_value)功能说明设置属性。

有如下三个属性可以配置：

LogmnrDll.LOGMNR_ATTR_PARALLEL_NUM 并行线程数有效值(2, 16)；

LogmnrDll.LOGMNR_ATTR_BUFFER_NUM 任务缓存节点数有效值(8, 1024)；

LogmnrDll.LOGMNR_ATTR_CONTENT_NUM 结果缓存节点数有效值(256,2048)。

参数说明connId：数据库连接标识ID。

attr：属性名。

attr_value：属性值。

返回值0：添加成功；

< 0 的值和异常：添加失败。

### 10.1.3 编程实例

下面用一个例子来说明dmlogmnr 接口的使用方法。

数据库安装在本机上，端口号为5236，用户名和密码均为SYSDBA。要分析的日志为D:\dm7data\arch\ARCHIVE_LOCAL1_20160704082303068.log。分析的结果放在D:\dm7data\result.txt 中。其中logmnr.jar 包放在DM 数据库安装目录的jar 文件夹下。

在项目中创建类名为dbmslob，代码实现如下：

import java.io.PrintStream;

import com.dameng.logmnr.LogmnrDll;

import com.dameng.logmnr.LogmnrRecord;

public class dbmslob {public static void main(String[] args) {try

## 第10 章 Logmnr 接口使用说明

{LogmnrDll.initLogmnr();

long connid = LogmnrDll.createConnect("localhost", 5236, "SYSDBA", "SYSDBA");

LogmnrDll.addLogFile(connid,"D:\\dm7data\\arch\\ARCHIVE_LOCAL1_20160704082303068.log",3);

LogmnrDll.startLogmnr(connid, -1, null, null);

LogmnrRecord[] arr = LogmnrDll.getData(connid, 100);

PrintStream ps = new PrintStream("D:\\dm7data\\result.txt");

System.setOut(ps);

System.out.println("日志分析结果打印：");

for (int i = 0; i < arr.length; i++) {System.out.println("-----------------------------" + i + "-----------------------------" + "\n");

System.out.println("xid:" + arr[i].getXid() + "\n");

System.out.println("operation:" + arr[i].getOperation() + "\n");

System.out.println("sqlRedo:" + arr[i].getSqlRedo() + "\n");

System.out.println("#############################" + i +"#############################" + "\n");

System.out.println("scn:" + arr[i].getScn() + "\n");

System.out.println("startScn:" + arr[i].getStartScn() + "\n");

System.out.println("commitScn:" + arr[i].getCommitScn() + "\n");

System.out.println("timestamp:" + arr[i].getTimestamp() + "\n");

System.out.println("startTimestamp:" + arr[i].getStartTimestamp() + "\n");

System.out.println("commitTimestamp:" + arr[i].getCommitTimestamp() + "\n");

System.out.println("operationCode:" + arr[i].getOperationCode() + "\n");

System.out.println("rollBack:" + arr[i].getRollBack() + "\n");

System.out.println("segOwner:" + arr[i].getSegOwner() + "\n");

System.out.println("tableName:" + arr[i].getTableName() + "\n");

System.out.println("rowId:" + arr[i].getRowId() + "\n");

System.out.println("rbasqn:" + arr[i].getRbasqn() + "\n");

System.out.println("rbablk:" + arr[i].getRbablk() + "\n");

System.out.println("rbabyte:" + arr[i].getRbabyte() + "\n");

System.out.println("dataObj:" + arr[i].getDataObj() + "\n");

System.out.println("dataObjv:" + arr[i].getDataObjv() + "\n");

System.out.println("//dataObjd:" + arr[i].getDataObjd() + "\n");

System.out.println("rsId:" + arr[i].getRsId() + "\n");

System.out.println("ssn:" + arr[i].getSsn() + "\n");

System.out.println("csf:" + arr[i].getCsf() + "\n");

System.out.println("status:" + arr[i].getStatus() + "\n");

System.out.println("#############################" + i +"#############################" + "\n");

}System.out.println("结果打印完毕");

ps.flush();

ps.close();

LogmnrDll.endLogmnr(connid, 1);

## 第10 章 Logmnr 接口使用说明

LogmnrDll.deinitLogmnr();

}catch (Exception e) {e.printStackTrace();

}}}

分析的结果在D:\dm7data\result.txt 中查看。

## 10.2 C 接口

dmlogmnr.dll 是达梦数据库的日志分析工具的C接口，供应用程序直接调用。

### 10.2.1 接口说明

#### 10.2.1.1 初始化环境

函数原型dmcode_t logmnr_client_init();

参数说明无。

功能说明初始化LOGMNR 环境。说明：初始化互斥量等。

返回值0：成功；

<0：错误。

#### 10.2.1.2 创建连接

函数原型

dmcode_t logmnr_client_create_connect(schar* ip,usint port,schar* uname,schar* pwd,void** conn);

功能说明

## 第10 章 Logmnr 接口使用说明

创建一个分析日志的连接。

参数说明ip：输入参数，服务器IP；

port：输入参数，端口号；

uname：输入参数，用户名；

pwd：输入参数，登录密码；

conn：输出参数，连接句柄。

返回值0：成功；

<0：错误。

#### 10.2.1.3 增加日志文件

函数原型

dmcode_t logmnr_client_add_logfile(void* conn,schar* logfilename,ulint options);

功能说明增加需要分析的归档日志文件。

参数说明conn：连接句柄；

logfilename：需要分析的归档日志文件名（绝对路径）；

options：

可选配置参数包括：

1：结束当前日志挖掘 （隐式调用endLogmnr，以前添加的归档日志文件将被清除），并增加新的归档日志文件。

2：删除日志文件。

3：增加的归档日志文件名。

说明：一旦startLogmnr，addLogFile 可以继续添加文件，那么新添加的文件必须比之前添加的所有文件的创建时间都要晚。

返回值0：成功；

<0：错误。

#### 10.2.1.4 删除日志文件

函数原型

## 第10 章 Logmnr 接口使用说明

dmcode_t logmnr_client_remove_logfile(void* conn,schar* logfilename);

功能说明移除某个需要分析的归档日志文件。

参数说明conn：连接句柄；

logfilename：待移除的归档日志文件名（绝对路径）。

说明：只有startLogmnr 之前才能进行remove 操作，否则会报错返回。

返回值0：成功<0：错误

#### 10.2.1.5 启动日志分析

函数原型

dmcode_t logmnr_client_start(void* conn,lint64 trxid,schar* starttime,schar* endtime);

功能说明启动当前会话的归档日志文件分析，对ADD_LOGFILE 添加的归档日志文件进行日志分析。

参数说明conn：连接句柄。

trxid：分析归档日志的事务id 号，默认为-1,表示不区分事务号。

starttime：分析归档日志的起始时间，默认1988/1/1。

endtime：分析归档日志的结束时间，默认2110/12/31。

返回值0：成功；

<0：错误。

## 第10 章 Logmnr 接口使用说明

#### 10.2.1.6 获取信息

函数原型dmcode_t

logmnr_client_get_data(void* conn,lint row_num,logmnr_content_t*** data,lint* real_num);

功能说明获取数据参数说明conn：输入参数，连接句柄；

rownum：输入参数，获取行数；

data：输出参数，返回数据；

real_num：输出参数，实际获取行数。

返回值获取的logmnr 记录。

#### 10.2.1.7 终止日志分析

函数原型

dmcode_t logmnr_client_end(void* conn,ulint options);

功能说明终止当前会话的归档日志文件分析。

参数说明conn：连接句柄；

options：

可选模式如下：

0：清除当前会话的归档日志文件分析环境，再次分析时需要重新add_logfile。

1：保留当前会话的归档日志文件分析环境，不需要重新add_logfile返回值0：成功；

<0：错误。

## 第10 章 Logmnr 接口使用说明

#### 10.2.1.8 结束连接

函数原型

dmcode_t logmnr_client_close_connect(void* conn);

参数说明conn：连接句柄。

功能说明关闭当前连接。说明：会清理字典缓存等。

返回值0：成功；

<0：错误。

#### 10.2.1.9 销毁环境

函数原型dmcode_t logmnr_client_deinit();

功能说明销毁LOGMNR 环境。

参数说明无。

返回值0：成功；

<0：错误。

#### 10.2.1.10 设置日志分析属性

函数原型dmcode_t

logmnr_client_set_attr(void* conn,ulint attr,void* val,ulint val_len);

## 第10 章 Logmnr 接口使用说明

参数说明conn：输入参数，连接句柄；

attr：输入参数，属性名称；

val：输入参数，属性attr 的值；

val_len：输入参数，属性值val 的长度。

功能说明设置日志分析属性。

有如下三个属性可以设置：

LOGMNR_ATTR_PARALLEL_NUM 并行线程数有效值(2, 16)；

LOGMNR_ATTR_BUFFER_NUM 任务缓存节点数有效值(8, 1024)；

LOGMNR_ATTR_CONTENT_NUM 结果缓存节点数有效值(256, 2048)。

返回值0：成功；

<0：错误。

#### 10.2.1.11 获取日志分析属性

函数原型

dmcode_t logmnr_client_get_attr(void* conn,ulint attr,void* buf,ulint buf_len,ulint* val_len);

参数说明conn：输入参数，连接句柄；

attr：输入参数，属性名称；

buf：输出参数，属性attr 的值；

buf_len：输入参数，属性值缓存buf 的长度；

val_len：输出参数，属性值的实际长度(<=buf_len)。

功能说明获取日志分析属性。

有如下四个属性可以获取：

LOGMNR_ATTR_PARALLEL_NUM 并行线程数有效值(2, 16)；

LOGMNR_ATTR_BUFFER_NUM 任务缓存节点数有效值(8, 1024)；

LOGMNR_ATTR_CONTENT_NUM 结果缓存节点数有效值(256, 2048)；

LOGMNR_ATTR_CHAR_CODE 本地编码（只读）。

返回值

## 第10 章 Logmnr 接口使用说明

0：成功；

<0：错误。

#### 10.2.2 编程实例

#include "logmnr_client.h"#include "logmnr_pub.h"#include "utl.h"void main(int argc, schar* argv[]){lint rt;

void* conn;

logmnr_content_t** logmnr_contents;

lint real_num;

lint64 b_t, time_used;

ulint char_code;

rt = logmnr_client_init();

if (rt < 0){fprintf(stderr, "logmnr_client_init error");

exit(-1);

}rt = logmnr_client_create_connect("LOCALHOST", 5236, "SYSDBA", "SYSDBA", &conn);

if (rt < 0){fprintf(stderr, "logmnr_client_create_connect error");

exit(-1);

}//需要添加的文件名rt = logmnr_client_add_logfile(conn, "d:\\dm7data\\arch\\ARCHIVE_LOCAL1_20140725091059625.log",LOGMNR_ADDFILE);

if (rt < 0){fprintf(stderr, "logmnr_client_add_logfile error");

exit(-1);

}rt = logmnr_client_set_attr(conn, LOGMNR_ATTR_PARALLEL_NUM, (void*)2, 0);

if (rt < 0){fprintf(stderr, "logmnr_client_set_attr error");

exit(-1);

}b_t = dm_get_usec_tick_count();

rt = logmnr_client_start(conn, -1, NULL, NULL);

if (rt < 0){fprintf(stderr, "logmnr_client_start error");

exit(-1);

}rt = logmnr_client_get_attr(conn, LOGMNR_ATTR_CHAR_CODE, &char_code, 4, 0);

if (rt < 0){fprintf(stderr, "logmnr_client_set_attr error");

exit(-1);

## 第10 章 Logmnr 接口使用说明

}while(TRUE){rt = logmnr_client_get_data(conn, 6, &logmnr_contents, &real_num);

if (rt < 0){fprintf(stderr, "logmnr_client_get_data error");

exit(-1);

}if (real_num == 0)break;

}time_used = dm_get_usec_tick_count() - b_t;

fprintf(stderr, "已用时间：%ld秒", time_used / 1000/ 1000);

rt = logmnr_client_end(conn, 0);

if (rt < 0){fprintf(stderr, "logmnr_client_end error");

exit(-1);

}rt = logmnr_client_close_connect(conn);

if (rt < 0){fprintf(stderr, "logmnr_client_close_connect error");

exit(-1);

}rt = logmnr_client_deinit();

if (rt < 0){fprintf(stderr, "logmnr_client_deinit error");

exit(-1);

}}

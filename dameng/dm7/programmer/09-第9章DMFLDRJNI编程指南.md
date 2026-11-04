---
title: "第9章 DM FLDR JNI编程指南"
book: "DM7程序员手册"
version: "DM7"
source: "temp/doc/DM7³ÌÐòÔ±ÊÖ²á.pdf#page=260"
tags:
  - dameng
  - dm7
  - programmer
---

## 第9 章 DM FLDR JNI 编程指南

## 9.1 DM FLDR JNI 接口介绍

java 调用dm 快速装载接口导数据是通过jni 接口来完成的。所引用的对象在com.dameng.jni_7.0.0.jar com.dameng.floader.Instance，com.dameng.floader.Properties。主要类是com.dameng.floader.Instance。

## 9.2 接口说明

1． allocInstance描述：

用于分配快速装载对象实例，所有快速装载都将通过该句柄进行操作。

格式：

boolean allocInstance();

参数：无返回值：

true, false注释：

该函数分配出用于快速装载实例句柄，用户必须首先调用该函数获得快速装载的实例句柄，只有通过该句柄才能进行后续的快速装载操作。

2． free描述：

释放快速装载实例句柄。

格式：

void free();

参数：无返回值：无注释：

释放快速装载实例句柄，将该实例句柄上所有快速装载所占用的资源释放。

3． setAttribute描述：

设置快速装载实例的属性。

格式：

bollean setAttribute(int attr_id,

## 第9 章 DM FLDR JNI 编程指南

String value);

参数：

attr_id(输入) 属性标识，指出将要设置的属性，关于属性详细内容参见注释部分。

value (输入) 属性值，根据attrid 不同该参数的意义不同。

返回值：

true, false注释：

可设置的属性见下表：

属性（attrid） 属性说明（value）FLDR_ATTR_SERVER 服务器地址FLDR_ATTR_UID 用户名FLDR_ATTR_PWD 密码FLDR_ATTR_PORT 服务器端口FLDR_ATTR_TABLE 目标表FLDR_ATTR_SET_INDENTITY 是否插入自增列（默认FALSE），如果设置为TRUE则服务器将使用指定的数据作为自增列的数据进行插入，如果设置为FALSE则对于自增列服务器将自动生成数据插入，忽略指定的数据FLDR_ATTR_DATA_SORTED 数据是否已按照聚集索引排序。默认为FALSE FLDR_ATTR_INDEX_OPTION 1不刷新二级索引，数据按照索引先排序，装载完后再将排序的数据插入索引2不刷新二级索引，数据装载完成后重建所有二级索引（默认为1）FLDR_ATTR_DATA_SIZE 指出本地缓冲数据的最大行数。默认为1000，最大为10000，最小为100 FLDR_ATTR_INERT_ROWS 8字节整数。只读属性。当前发送到服务器的行数FLDR_ATTR_COMMIT_ROWS 8字节整数。只读属性。当前提交到数据库的行数FLDR_ATTR_PROCESS_ROWS 8字节整数。只读属性。用户绑定的数据行数FLDR_ATTR_SEND_NODE_NUM 发送链表节点个数，默认128，最大为20480，最小为16。多线程处理中每个线程所支配的向服务器发送数据节点的个数FLDR_ATTR_TASK_THREAD_NUM 任务线程数FLDR_ATTR_BAD_FILE 记录出错数据的文件，出错数据将全部使用字符串表示FLDR_ATTR_DATA_CHAR_SET 设置输入数据字符类型的字符集FLDR_ATTR_LOG_FILE 指定日志记录文件FLDR_ATTR_SSL_PATH 在加密通讯模式下加密证书的路径FLDR_ATTR_SSL_PWD 加密证书的密钥FLDR_ATTR_LOCAL_CODE 指定本地字符集FLDR_ATTR_SERVER_BLDR_SIZE 水平分区表装载时，指定服务器bldr的最大个数，范围为1～65535，默认为100 FLDR_ATTR_MPP_LOCAL_FLAG 指明是否是mpp模式下的单节点数据。默认值为FALSE

> 4． getAttribute

## 第9 章 DM FLDR JNI 编程指南

描述：

获取快速装载实例的属性。

格式：

String getAttribute(int attr_id);

参数：

attrid(输入) 属性标识，指出将要获取的属性，关于属性详细内容参见setAttribute 的注释部分。

返回值：

属性值。

注释：

参见setAttribute 函数说明中各属性说明。

5． initializeInstance描述：

初始化当前快速装载实例。

格式：

boolean initializeInstance(String server,String user,String pwd,String table);

参数：

server (输入) 链接的服务器。将被记录到实例的FLDR_ATTR_SERVER 属性中。

user (输入) 登录用户。将被记录到实例的FLDR_ATTR_UID 属性中。

pwd（输入） 用户密码。将被记录到实例的FLDR_ATTR_PWD 属性中。

table（输出） 进行快速装载的表。将被记录到实例的FLDR_ATTR_TABLE 属性中。

返回值：

true, false注释：

根据用户通过setAttribute 设置的属性初始化快速装载环境，如果用户未指定连接则根据用户提供的服务器、用户和密码建立到服务器的连接。

6． unitialize描述：

释放快速装载实例所占用的资源。

格式：

boolean uninitialize();

## 第9 章 DM FLDR JNI 编程指南

参数：无返回值：

true, false注释：

用于释放所占用快速装载实例所占用的资源。用户在调用该函数后可重新初始化快速装载句柄，进行新的数据装载。

7． fldr_Bind_Columns_ex描述：

绑定输入列。

格式：

boolean fldr_Bind_Columns_ex(int colNumber,int type,String datefmt,Object data,int maxcollen,int[] ind_len,int threadNum);

参数：

colNumber(输入) 绑定列的编号。从1 开始计数，对应快速装载的表的相应列。

type (输入) 用户绑定数据的JAVA 类型。

datefmt（输入） 当绑定列对应的表的列为时间日期类型，且绑定的JAVA 数据为String 类型，该参数为字符串到日期类型的格式串。其他情况，忽略该绑定输入。

data（输入） 指向用于存放数据内存的地址指针。

maxcollen（输入） 用于记录单行数据最大的长度。当进行多行绑定的时候，对于变长的C类型，根据该参数内容进行便宜的计算。对于固定长度的JAVA 数据类型，该参数内容被忽略。

ind_len（输入） 用户绑定的数据长度指示符。当为批量绑定时，传入的地址为指向INT 类型的数组。如果地址中保存的值为-1，绑定列的该行数据被视为空值。对于BINARY 和CHAR 变长数据类型，用来指明数据的长度。对于其他定长数据类型，忽略其长度。

threadNum(输入) 多线程调用，线程序号，单线程传0。

返回值：

true, false注释：

8． fldr_Send_Rows_ex描述：

发送行数。

格式：

boolean fldr_Send_Rows_ex(

## 第9 章 DM FLDR JNI 编程指南

long rows,int threadNum,int seqNo);

参数：

rows (输入) 在多行绑定的情况，指明绑定的行数。

threadNum(输入) 多线程调用，线程序号，单线程传0。

seqNo(输入) 数据批次，从1 开始自增，保证数据有序。

返回值：

true, false 9． finish描述：

结束一次批量操作。

格式：

bollean finish();

参数：无返回值：

true, false

## 9.3 DM FLDR JNI 编程实例

package com.dameng;

import java.io.File;

import com.dameng.floader.DataTypes;

import com.dameng.floader.Instance;

import com.dameng.floader.Properties;

public class TestFloder{public static void main(String[] args){Instance instance = new Instance();

int threadNum = 1;

TestFloder floder = new TestFloder();

/* ***************************初始化******************************* *//* create table sysdba.test1(c1 int ,c2 varchar(50)); */String tableName = "SYSDBA.TEST1";

boolean success = floder.init(instance, threadNum, tableName);

## 第9 章 DM FLDR JNI 编程指南

if (success){try{int c1[] = {1,2,3,4,5,6,7,8,9}; //数据int c1_ind[] = {4,4,4,4,4,4,4,4,4}; //长度指示符 -1表示空byte[] byteArray = new byte[9];

for (int i = 0; i < 9; i++){byteArray[i] = ((Integer)c1[i]).byteValue();

}String c2[] ={"a1","a12","a123","a1234","a12345","a123456","a1234567","a12345678","a123456789"};

int c2_ind[] = {2,3,4,5,6,7,8,9,10}; //长度指示符 -1表示空byte[][] byteArray2 = new byte[9][];

for (int i = 0; i < 9; i++){byteArray2[i] = c2[i].getBytes();

}/*fldr_Bind_Columns_ex(int colNumber, // 列号从1开始int type, // 列类型从DataTypes取String datefmt, // 时间类型格式范式：默认yyyy-mm-dd hh-mm-ss，为空的话，按默认处理Object data, // 数值类型直接使数值类型数组，字符串类型是byte数组int maxcollen, // 数值类型值无效，fldr里面自己按sizeof取长度。，// xxxxxxxxxxxxx注意字符串类型是所有数据总长度xxxxxxxxxxxxxxxxxxx。

// fldr里面要按这个总长度申请类型int[] ind_len, // 长度指示符，int数组，-1标示空// 数值类型无效，字符串类型标示数据长度。

int threadNum // 多线程下有效，单线程传1)*//*fldr_Send_Rows_ex(long rows, // 行数

## 第9 章 DM FLDR JNI 编程指南

int threadNum, // 多线程下有效，单线程传1 int seqNo // 数据批次号，从1开始，必须连续，否则fldr会卡住。

)*/for (int i = 1; i < 10; i++){instance.fldr_Bind_Columns_ex(1, DataTypes.FLDR_C_INT, null, c1, 4, c1_ind, 1);

instance.fldr_Bind_Columns_ex(2, DataTypes.FLDR_C_CHAR, null, byteArray2, 54,c2_ind, 1);

instance.fldr_Send_Rows_ex(9, 1, i);

}}catch (Exception e){e.printStackTrace();

}}/* ***************************释放******************************* */if (!success){String message = instance.getErrorMsg();

System.out.println("出错信息:" + message);

instance.free();

}else{instance.finish();

// 返回实际插入的行数long rowHaveCopied =Long.parseLong(instance.getAttribute(Properties.FLDR_ATTR_COMMIT_ROWS));

System.out.println("已复制行数:" + rowHaveCopied);

instance.unitialize();

instance.free();

}}// 初始化

## 第9 章 DM FLDR JNI 编程指南

public boolean init(Instance instance, int threadNum, String tableName){// 分配句柄instance.allocInstance();

// 设置属性String host = "localhost";

String port = "5236";

String userName = "SYSDBA";

String password = "SYSDBA";

instance.setAttribute(Properties.FLDR_ATTR_SERVER, host);

instance.setAttribute(Properties.FLDR_ATTR_PORT, port);

instance.setAttribute(Properties.FLDR_ATTR_UID, userName);

instance.setAttribute(Properties.FLDR_ATTR_PWD, password);

// 编码// instance.setAttribute(Properties.FLDR_ATTR_DATA_CHAR_SET,System.getProperty("file.encoding"));

// 是否有自增量// instance.setAttribute(Properties.FLDR_ATTR_SET_INDENTITY, "0");

// fldr task线程默认为cpu个数，如果客户端线程数大于cpu个数，则必须设置该参数// instance.setAttribute(Properties.FLDR_ATTR_TASK_THREAD_NUM, String.valueOf(threadNum));

// 一次提交记录数// instance.setAttribute(Properties.FLDR_ATTR_DATA_SIZE, "5000");

// 记录出错的信息String dmHome = System.getProperty("DM_HOME");

if (dmHome != null && !dmHome.equals("")){if (dmHome.endsWith("/") || dmHome.endsWith("\\")){instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + "BADFILE.TXT");

}else{instance.setAttribute(Properties.FLDR_ATTR_BAD_FILE, dmHome + File.separator +"BADFILE.TXT");

}}// 装载日志if (dmHome != null && !dmHome.equals(""))

## 第9 章 DM FLDR JNI 编程指南

{if (dmHome.endsWith("/") || dmHome.endsWith("\\")){instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + "FLDR_LOG.TXT");

}else{instance.setAttribute(Properties.FLDR_ATTR_LOG_FILE, dmHome + File.separator +"FLDR_LOG.TXT");

}}// 最大容错个数// instance.setAttribute(Properties.FLDR_ATTR_ERRORS_PERMIT,String.valueOf(Integer.MAX_VALUE));

// 是否为mpp// instance.setAttribute(Properties.FLDR_ATTR_MPP_CLIENT, "0");

// 如果是txt到dm7// instance.setAttribute(Properties.FLDR_ATTR_COMMPRESS_FLAG, "0");

// instance.setAttribute(Properties.FLDR_ATTR_DIRECT_MODE,"0");

// instance.setAttribute(Properties.FLDR_ATTR_DATA_SORTED, "0");

// instance.setAttribute(Properties.FLDR_ATTR_LOCAL_CODE, "GBK");

// instance.setAttribute(Properties.FLDR_ATTR_BLOB_TYPE, "0");

// instance.setAttribute(Properties.FLDR_ATTR_INDEX_OPTION,"1");

// instance.setAttribute(Properties.FLDR_ATTR_LOB_DIRECTORY, "");

// instance.setAttribute(Properties.FLDR_ATTR_ERRORS_PERMIT,"1000");

// instance.setAttribute(Properties.FLDR_ATTR_SKIP_ROWS,"0");

// instance.setAttribute(Properties.FLDR_ATTR_BUFFER_SIZE,"512");

// instance.setAttribute(Properties.FLDR_ATTR_SERVER_BLDR_NUM,"512");

// instance.setAttribute(Properties.FLDR_ATTR_READ_ROWS,"512");

// instance.setAttribute(Properties.FLDR_ATTR_ROWS_COMMIT,"512");

// instance.setAttribute(Properties.FLDR_ATTR_BDTA_SIZE,"512");

boolean success = instance.initializeInstance(null, null, null, tableName);

return success;

}

}

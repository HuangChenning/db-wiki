---
title: "数据库(V9)常见问题（应用开发类-C++）"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree2.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

## 数据库(V9)常见问题（应用开发类-C++）

## C++（ODBC 方式连接 V9 数据库）

本文档详细介绍 C++ 语言通过 ODBC 方式连接 V9 数据库的完整流程，包括环境依赖安装、配置文件设置、连接验证及示例代码实现，适用于 Linux 环境下的 C++ 应用开发。

## 1.1 安装 unixODBC 依赖

ODBC 连接需依赖 unixODBC 工具，以下是具体安装步骤：

1. 下载源码包：推荐版本 unixODBC-2.3.12（可从官方渠道获取）
2. 解压并编译安装（需提前安装 gcc 编译环境）：
```
tar -zxvf unixODBC-2.3.12.tar.gz

cd unixODBC-2.3.12

./configure

make

make install
```
3. 验证安装结果：
```
isql --version  # 成功安装后输出：unixODBC 2.3.12
```

## 1.2 查找 ODBC 配置文件路径

通过命令查询系统中 ODBC 配置文件的默认存放路径，后续配置需基于此路径操作：

```
odbcinst -j
```

输出示例（实际路径以系统查询结果为准）：

```
DRIVERS.....: /usr/local/etc/odbcinst.ini

SYSTEM DATA SOURCES: /usr/local/etc/odbc.ini

USER DATA SOURCES..: /home/highgo/.odbc.ini
```

## 1.3 配置 ODBC 相关文件

需配置 odbcinst.ini（驱动配置）和 odbc.ini（数据源配置）两个核心文件，确保驱动与 V9 数据库适配。

### 1.3.1 配置 odbcinst.ini（驱动配置文件）

编辑 odbcinst.ini 文件，添加 V9 数据库驱动信息，内容如下：

```
[HGDB_v9]

Description=HGDB driver for Linux

Driver=/home/highgo/hgdb-v9.0/interfaces/odbc/lib/psqlodbcw.so

Setup=/home/highgo/hgdb-v9.0/interfaces/odbc/lib/psqlodbcw.so

UsageCount=1
```

说明：Driver 和 Setup 路径为 V9 数据库安装后自带的 ODBC 驱动路径，需根据实际安装目录调整。

### 1.3.2 配置 odbc.ini（数据源配置文件）

编辑 odbc.ini 文件，添加 V9 数据库数据源信息，内容如下：

```
[HGDB]

Description=HGDB ODBC Connection

Driver=HGDB_v9  # 需与 odbcinst.ini 中配置的驱动名称一致

Trace=Yes

TraceFile=/home/highgo/hgdb-v9.0/interfaces/odbc/sql.log

Database=highgo  # 数据库名称

Servername=172.21.154.22  # 数据库服务器 IP

UserName=highgo  # 数据库用户名

Password=Hello@123  # 数据库密码

Port=5866  # 数据库端口

Protocol=6.4

ReadOnly=No

RowVersioning=No

ShowSystemTables=No

ShowOidColumn=No

FakeOidIndex=No
```

### 1.3.3 配置环境变量

设置环境变量指定配置文件路径和驱动依赖库路径，确保系统能正确识别：

```
export ODBCINI=/etc/odbc.ini

export ODBCSYSINI=/etc/odbcinst.ini

export LD_LIBRARY_PATH=/home/highgo/hgdb-v9.0/lib:/home/highgo/hgdb-v9.0/interfaces/odbc/lib:$LD_LIBRARY_PATH
```

## 1.4 验证 ODBC 配置有效性

通过以下命令验证配置是否正确，确保能正常连接 V9 数据库：

4. 查看数据源：
```
odbcinst -q -s  # 输出 [HGDB] 即为数据源配置成功
```
5. 测试连接：
```
isql -v HGDB  # 显示 Connected! 即为连接成功
```

## 1.5 C++ 连接 V9 数据库示例代码

```cpp
#include <iostream>

#include <sql.h>

#include <sqlext.h>

using namespace std;

int main() {

SQLHENV henv;  // 环境句柄

SQLHDBC hdbc;  // 连接句柄

SQLHSTMT hstmt;  // 语句句柄

SQLRETURN ret;  // 函数返回状态

// 1. 分配环境句柄

ret = SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);

ret = SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (SQLPOINTER)SQL_OV_ODBC3, 0);

// 2. 分配连接句柄

ret = SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);

// 3. 连接 V9 数据库（数据源名称、用户名、密码需与 odbc.ini 配置一致）

ret = SQLConnect(hdbc, (SQLCHAR*)"HGDB", SQL_NTS, (SQLCHAR*)"highgo", SQL_NTS, (SQLCHAR*)"Hello@123", SQL_NTS);

if (ret == SQL_SUCCESS || ret == SQL_SUCCESS_WITH_INFO) {

cout << "成功连接到 V9 数据库!" << endl;

// 获取数据库版本信息

SQLCHAR ver[1024];

SQLINTEGER len;

ret = SQLGetInfo(hdbc, SQL_DBMS_VER, ver, sizeof(ver), &len);

cout << "V9 数据库版本: " << ver << endl;

// 关闭数据库连接

SQLDisconnect(hdbc);

} else {

cout << "连接 V9 数据库失败!" << endl;

}

// 4. 释放资源

SQLFreeHandle(SQL_HANDLE_DBC, hdbc);

SQLFreeHandle(SQL_HANDLE_ENV, henv);

return 0;

}
```

## 1.6 编译与运行

使用 g++ 编译器编译示例代码，链接 odbc 库，具体命令如下：

```
g++ -o hgdb_odbc_demo hgdb_odbc_demo.cpp -lodbc

./hgdb_odbc_demo
```

## 1.7 运行结果

连接成功后输出如下：

```
成功连接到 V9 数据库!

V9 数据库版本: PostgreSQL 14.15 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 10.4.0, 64-bit
```
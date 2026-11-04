---
title: "数据库(V9)常见问题（应用开发类-Qt）"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree5.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

## 数据库(V9)常见问题（应用开发类-Qt）

## Qt 连接 V9 数据库

本文档详细介绍 Qt 框架连接 V9 数据库的两种常用方式（libpq 方式、ODBC 方式），包含环境配置、项目设置、代码实现及运行验证，适用于 Qt Creator 开发环境，适配 Linux 系统。

## 2.1 libpq 方式连接

libpq 是 PostgreSQL 官方提供的 C 语言客户端库，Qt 可通过链接该库直接连接 V9 数据库，步骤如下：

### 2.1.1 配置环境变量

在 Qt Creator 中配置环境变量，指定 V9 数据库库文件路径：

1. 点击「项目」→ 「Build Environment」（构建环境）
2. 点击「添加」，新增环境变量 `LD_LIBRARY_PATH` ，值设为 V9 数据库 lib 目录路径：
```
LD_LIBRARY_PATH=/home/highgo/hgdb-v9.0/lib
```

### 2.1.2 配置 Qt 项目文件（.pro）

在项目的.pro 文件中添加头文件路径和链接库配置，确保 Qt 能找到 libpq 相关资源：

```
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
TARGET = hgdb_libpq_demo
TEMPLATE = app
DEFINES += QT_DEPRECATED_WARNINGS

# 配置 V9 数据库头文件路径
INCLUDEPATH += /home/highgo/hgdb-v9.0/include

# 配置链接 libpq 库（V9 数据库自带）
LIBS += /home/highgo/hgdb-v9.0/lib/libpq.so.5

# 项目源文件、头文件、界面文件配置
SOURCES += main.cpp \
           mainwindow.cpp
HEADERS  += mainwindow.h
FORMS    += mainwindow.ui
```

### 2.1.3 连接 V9 数据库代码示例

实现 Qt 程序通过 libpq 连接 V9 数据库，包含连接建立、数据查询、资源释放完整流程：

```
#include <QCoreApplication>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlRecord>
#include <QDebug>

int main(int argc, char *argv[]) {
    QCoreApplication a(argc, argv);

    // 1. 创建数据库连接（驱动指定为 QPSQL，对应 libpq 驱动）
    QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
    // 2. 配置连接参数（根据实际环境调整）
    db.setHostName("192.168.1.7");  // 数据库服务器 IP
    db.setPort(5866);                // 数据库端口
    db.setUserName("highgo");        // 数据库用户名
    db.setPassword("Hello@123");     // 数据库密码
    db.setDatabaseName("highgo");    // 要连接的数据库名称

    // 3. 打开数据库连接并执行查询
    if (db.open()) {
        qDebug() << "连接 V9 数据库成功: " << db.isOpen();
        // 执行查询语句
        QSqlQuery query;
        query.prepare("select * from test");  // test 为示例表名
        if (query.exec()) {
            // 遍历查询结果
            while (query.next()) {
                QSqlRecord record = query.record();
                qDebug() << "id:" << record.value("id").toInt()
                         << "name:" << record.value("name").toString()
                         << "age:" << record.value("age").toInt()
                         << "address:" << record.value("address").toString()
                         << "salary:" << record.value("salary").toFloat();
            }
        } else {
            qDebug() << "查询失败: " << query.lastError().text();
        }
        // 4. 关闭连接
        db.close();
    } else {
        qDebug() << "连接 V9 数据库失败: " << db.lastError().text();
    }

    return a.exec();
}
```

### 2.1.4 运行结果

连接成功并查询到数据后，输出如下：

```
连接 V9 数据库成功:  true
id: 1 name: "test_1" age: 25 address: "北京" salary: 12
id: 2 name: "test_2" age: 22 address: "西宁" salary: 22
id: 3 name: "test_3" age: 26 address: "济南" salary: 33
```

## 2.2 ODBC 方式连接

Qt 也可通过 ODBC 方式连接 V9 数据库，需先完成 ODBC 环境配置（参考 C++ 章节的 1.1-1.4 节），具体步骤如下：

### 2.2.1 前置条件

已完成 unixODBC 安装、V9 数据库 ODBC 驱动配置（odbcinst.ini 和 odbc.ini），且通过 `isql -v HGDB` 验证连接成功。

### 2.2.2 配置环境变量

在 Qt Creator 中添加环境变量，指定 ODBC 配置文件路径和驱动库路径：

```
LD_LIBRARY_PATH=/home/highgo/hgdb-v9.0/lib:/home/highgo/hgdb-v9.0/interfaces/odbc/lib:$LD_LIBRARY_PATH
ODBCSYSINI=/etc/odbcinst.ini
```

### 2.2.3 连接 V9 数据库代码示例

```
#include <QApplication>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QDebug>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    // 1. 配置连接信息（根据 odbc.ini 配置调整）
    QString strHost = "192.168.1.21";    // 数据库服务器 IP
    int port = 5866;                     // 数据库端口
    QString strDbName = "highgo";        // 数据库名称
    QString strUserName = "highgo";      // 用户名
    QString strUserPwd = "Hello@123";    // 密码

    // 2. 创建 ODBC 连接（驱动指定为 QODBC）
    QSqlDatabase db = QSqlDatabase::addDatabase("QODBC");
    // 3. 构造 ODBC 连接字符串（Driver 名称需与 odbcinst.ini 一致）
    QString strConn = QString(
        "Driver={HGDB_v9};"
        "SERVER=%1;"
        "PORT=%2;"
        "DATABASE=%3;"
        "UID=%4;"
        "PWD=%5;"
    ).arg(strHost).arg(port).arg(strDbName).arg(strUserName).arg(strUserPwd);
    db.setDatabaseName(strConn);

    // 4. 打开连接并验证
    if (db.open()) {
        qDebug() << "Connection V9 database successful";
        db.close();
    } else {
        qDebug() << "Connection failed: " << db.lastError().text();
    }

    return a.exec();
}
```

### 2.2.4 运行结果

连接成功后输出如下：

```
Connection V9 database successful
```
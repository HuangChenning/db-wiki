---
title: "数据库(V9)常见问题（应用开发类-Python-psycopg2）"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree4.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

## 数据库(V9)常见问题（应用开发类-Python-psycopg2）

## Python（psycopg2）

## 1.1 psycopg2 概述

psycopg2 是 Python 访问 PostgreSQL 数据库的第三方库，核心特点：

• 简单易用：提供简洁 API，易于学习和上手

• 高性能：基于 C 语言实现，数据库操作效率高

• 完全兼容：支持大多数 PostgreSQL 数据库特性

• 安全性：内置防 SQL 注入功能，保障数据安全

注意：Python 版本与 psycopg2 版本需匹配，本文档示例版本仅作参考

### 1.1.1 安装 Python

1. 下载源码：推荐 Python 3.7.0 版本
2. 解压并编译安装：
```bash
tar -zxvf python.tar.gz
cd python安装目录
./configure --prefix=/opt/Python3.7
make
make install
```
3. 替换系统旧版本 Python（可选）：
```bash
rm -rf /usr/bin/python
ln -s /opt/Python3.7/bin/python3.7 /usr/bin/python
```
4. 验证安装结果：
```bash
python --version  # 成功输出：Python 3.7.0 即为安装完成
```

### 1.1.2 安装 psycopg2

5. 下载源码：推荐 psycopg2 2.9.5 版本

注意：psycopg2 2.9.9 及以上版本需 Python 3.8 及更高版本支持

6. 解压并编译安装：
```bash
tar -zxvf psycopg2.tar.gz
cd psycopg2安装目录
python setup.py build
python setup.py install
```
7. 验证安装路径（示例，需根据实际安装目录调整）：
```bash
/opt/Python3.7/lib/python3.7/site-packages/psycopg2-2.9.5-py3.7-linux-x86_64.egg/psycopg2
```

### 1.1.3 连接 V9 数据库代码示例

```python
import psycopg2
try:
    # 数据库连接配置信息
    host = "172.20.18.140"
    port = 5866
    account = "highgo"
    password = "Hello@123"
    dbname = "highgo"
    
    # 建立数据库连接
    conn = psycopg2.connect(
        host=host,
        port=int(port),
        user=account,
        password=password,
        dbname=dbname
    )
    cursor = conn.cursor()  # 创建游标对象，用于执行SQL语句
    
    # 执行查询语句
    cursor.execute("select * from test")
    result = cursor.fetchall()  # 获取所有查询结果
    print(result)  # 预期输出：[(1,'test_1'),(2,'test_2'),(3,'test_3')]
except Exception as e:
    print("数据库操作异常：", e)
```
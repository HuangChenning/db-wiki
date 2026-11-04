---
title: "2、ODBC连接报错-Could not SQLConnect"
book: "连接使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/ODBC_connect_error.html"
tags:
  - highgo
  - highgo-v45
  - faq-connections
---

## ODBC连接报错Could not SQLConnect

## 1、问题现象

Centos7环境下ODBC连接HGDB报错Could not SQLConnect。

## 2、解决方案

### （1）配置ODBC

/opt/HighGo4.5-see/etc/drivers/ODBC/unixODBC/etc/目录，修改odbcinst.ini和odbc.ini文件。

odbcinst.ini文件内容如下：

![clip_image002](img/clip_image002.jpg)

odbc.ini文件内容如下：

![clip_image004](img/clip_image004.jpg)

### （2）测试连接

/opt/HighGo4.5-see/etc/drivers/ODBC/unixODBC/bin/目录，执行测试程序./isql -v see4odbc，执行结果如下：

![clip_image006](img/clip_image006.jpg)

报Could not SQLConnect错。

### （3）解决方法

添加环境变量：

```
export ODBCSYSINI=/opt/HighGo4.5-see/etc/drivers/ODBC/unixODBC/etc
```

再次执行测试程序./isql -v see4odbc，执行结果如下：

![clip_image008](img/clip_image008.jpg)

执行查询语句：

```
select * from student;
```

执行结果如下：

![5.png](img/clip_image010.jpg)

总结：需要添加环境变量：

```
ODBCSYSINI=/opt/HighGo4.5-see/etc/drivers/ODBC/unixODBC/etc
```
---
title: "13、如何使用BenchmarkSQL工具测试HGDB"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/BenchmarkSQL.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 如何使用BenchmarkSQL工具测试HGDB

## 一、测试前的准备

① 确认数据库可以正常启动并连接。

② 解压BenchmarkSQL工具。

③ 创建好测试数据库，通常使用benchmarksql数据库名。

创建命令：

```
highgo=# create database benchmarksql;
CREATE DATABASE
```

④ 安装ant进行编译。

常用安装方式有： yum install ant

## 二、安装BenchmarkSQL工具

### 1、解压并编译

在解压后一级目录编译并出现BUILD SUCCESSFUL字样：

```
[root@localhost benchmarksql-5.0]# ant
cd run/

cp props.pg highgo.p
```

### 2、修改配置文件

```
[postgres@localhost benchmarksql] $ cd run 
[postgres@localhost run] $ cp props.pg my_postgres.properties 
[postgres@localhost run] $ vi my_postgres.properties
```

关于驱动，如果工具自身驱动可用则驱动连接字符串如下：

```
conn=jdbc:postgresql://localhost:5866/benchmarksql
```

【注意修改端口号和数据库并提前将数据库创建好】

如果工具驱动无法使用，则：  
将该路径（/home/highgo/highgo/database/4.3.4/hgdbadmin/lib/lib 此为默认路径）下的驱动包复制到工具lib目录下  
/upload/benchmarksql-5.0/lib/postgres \* **一定要确保该路径下有且只有一个驱动jar包\***

```
db=postgres
driver=com.highgo.jdbc.Driver
conn=jdbc:highgo://localhost:5886/benchmarksql
```

用户名和密码，确保数据库中的用户存在且密码无误。

```
user=sysdba
password=highgo123

warehouses=1 //对应数据量，比如10代表约1G数据量
loadWorkers=4 // 看看核心数是多少就设置成多少

terminals=1  //代表数据库连接数
//To run specified transactions per terminal- runMins must equal zero
runTxnsPerTerminal=0  // 设置为0
//To run for specified minutes- runTxnsPerTerminal must equal zero
runMins=100 //看看需要测试多长时间，单位为分钟
//Number of total transactions per minute
limitTxnsPerMin=0 //设置为0
```

### 3、构建模式和初始数据库加载

```
[postgres@localhost run]$ ./runDatabaseBuild.sh my_postgres.properties
```

4、测试过程

```
[postgres@localhost run]$ ./runBenchmark.sh my_postgres.properties 
 The benchmark should run for the number of configured concurrent 
  connections (terminals) and the duration or number of transactions. 

  The end result of the benchmark will be reported like this: 

  01:58:09,081 [Thread-1] INFO  jTPCC : Term-00, 
  01:58:09,082 [Thread-1] INFO  jTPCC : Term-00, Measured tpmC (NewOrders) = 179.55 
  01:58:09,082 [Thread-1] INFO  jTPCC : Term-00, Measured tpmTOTAL = 329.17 
  01:58:09,082 [Thread-1] INFO  jTPCC : Term-00, Session Start   = 2016-05-25 01:58:07 
  01:58:09,082 [Thread-1] INFO  jTPCC : Term-00, Session End    = 2016-05-25 01:58:09 
  01:58:09,082 [Thread-1] INFO  jTPCC : Term-00, Transaction Count = 10
```

到这一步已经安装完成了，只要修改my\_postgres.properties的参数就可以进行不同并发的压力测试了

### 5、快速重建数据模型

有时候测试崩溃或者不动数据库量对等测试需要快速重来，如果你修改了配置文件中的warehouse或者load的值都需要重建数据库，快速重建方法如下：

```
[postgres@localhost run]$ ./runDatabaseDestroy.sh my_postgres.properties   
[postgres@localhost run]$ ./runDatabaseBuild.sh my_postgres.properties
```
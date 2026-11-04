---
title: "6、hgdbdeveloper无法使用调试功能"
book: "连接使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/hgdbdeveloper.html"
tags:
  - highgo
  - highgo-v45
  - faq-connections
---

## hgdbdeveloper无法使用调试功能

## 1、 问题描述：

使用hgdbdeveloper工具无法使用函数调试功能

## 2、 解决过程

\_\_原因\_\_：缺少插件pldebugger

### （1）移动、解压：

将下载好的压缩包（pldebugger.zip)移动到数据库安装目录contrib。

```
mv pldebugger.zip  /opt/HighGo5.6.5/share/contrib unzip pldebugger.zip
```

### （2）编译安装pldebugger

```
cd /opt/HighGo5.6.5/share/contrib/pldebugger/
```

执行命令：make

如果报错，加USE\_PGXS=1，原因可以自行搜索。make: \*\*\* 没有规则可以创建目标 “/contrib/contrib-global.mk”。 停止则使用命令：make USE\_PGXS=1 install。

如果报错/opt/HighGoDB-4.3.4.6/include/server/libpq/libpq-be.h:25:25: 致命错误：openssl/ssl.h：没有那个文件或目录。则安装openssl。

```
yum install openssl-devel 
make USE_PGXS=1 instal
```

安装完后在postgresql目录的Lib文件夹可以看到plugin\_debugger.so文件 cd /opt/HighGo5.6.5/lib/postgresql

### （3）postgresql配置文件配置

```
vi /opt/HighGo5.6.5/data/postgresql.conf 修改配置文件参数如下，如果多个参数逗号分开 
shared_preload_libraries = '/opt/HighGoDB5.6.5/lib/plugin_debugger.so'
```

### （4）重启数据库

```
pg_ctl restart -m fast
```

### （5）创建扩展模块

```
使用highgo用户登录数据库 
psql -U highgo -d highgo 
执行语句创建扩展模块 
create extension pldbgapi; 
查看插件是否安装成功 
select * from pg_extension;
```

### (6)安装完成。

附：客户环境为内网环境无法从网络上获取依赖包。Pldebugger的依赖包只有openssl，客户环境可能没有，实施时建议携带openssl的依赖包。
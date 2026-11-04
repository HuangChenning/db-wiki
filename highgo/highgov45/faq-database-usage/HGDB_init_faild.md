---
title: "9、关于HGDB安全版初始化失败的常见原因列举(权限、用户)"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/HGDB_init_faild.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 关于HGDB安全版初始化失败的常见原因列举（权限、用户）

当安装完安全版数据库，手动初始化数据库时提示失败。

权限、用户、环境变量等因素都可能导致此问题发生。

## 1、环境变量因素

### （1）环境变量文件未配置

```
[root@mode2 ~]# initdb -D $PGDATA  -e sm4 -c "echo 12345678" > /opt/HighGo4.5.5-see/bin/initdb.log
bash: initdb: 未找到命令...解决方法
```

①将数据库环境变量文件添加到.bashrc或.bash\_profile中

```
[root@mode2 ~]# vi ~/.bash_profile 添加以下信息
source /opt/HighGo4.5.5-see/etc/highgodb.env 
[root@mode2 ~]# source ~/.bash_profile
```

②将具体的环境变量信息填写到.bashrc或.bash\_profile中

```
[root@mode2 ~]# vi ~/.bash_profile 添加以下信息
export HG_BASE=/opt/HighGo4.5.5-see
export HGDB_HOME=/opt/HighGo4.5.5-see
export PGPORT=5866
export PGDATABASE=highgo
export PGDATA=$HGDB_HOME/data
export PATH=$HGDB_HOME/bin:$PATH
[root@mode2 ~]# source ~/.bash_profile
```

## 2、用户权限问题

执行初始化命令的用户没有创建data目录的权限

```
[highgo@mode2 ~]$ initdb -D /opt/data1
属于此数据库系统的文件宿主为用户 "highgo".
此用户也必须为服务器进程的宿主.
数据库簇将使用本地化语言 "zh_CN.UTF-8"进行初始化.
默认的数据库编码已经相应的设置为 "UTF8".
initdb: 无法为本地化语言环境"zh_CN.UTF-8"找到合适的文本搜索配置
缺省的文本搜索配置将会被设置到"simple"
禁止为数据页生成校验和.
Data encryption is disabled.
创建目录 /opt/data1 ... initdb: 无法创建目录 "/opt/data1": 权限不够
```

**解决方法**

使用root用户将data目录上级目录权限赋予初始化用户，或者直接创建data空目录，将data空目录权限授予初始化用户

```
[root@mode2 etc]# mkdir /opt/data1
[root@mode2 etc]# chown -R highgo:highgo /opt/data1
[root@mode2 etc]# su - highgo
[highgo@mode2 ~]$ initdb -D /opt/data1
属于此数据库系统的文件宿主为用户 "highgo".
此用户也必须为服务器进程的宿主.
数据库簇将使用本地化语言 "zh_CN.UTF-8"进行初始化.
默认的数据库编码已经相应的设置为 "UTF8".
initdb: 无法为本地化语言环境"zh_CN.UTF-8"找到合适的文本搜索配置
缺省的文本搜索配置将会被设置到"simple"
禁止为数据页生成校验和.
Data encryption is disabled.
修复已存在目录 /opt/data1 的权限 ... 成功
正在创建子目录 ... 成功
选择默认最大联接数 (max_connections) ... 100
选择默认共享缓冲区大小 (shared_buffers) ... 128MB
选择动态共享内存实现 ......posix
创建配置文件 ... 成功
正在运行自举脚本 ...成功
正在执行自举后初始化 ...成功
同步数据到磁盘...成功
警告:为本地连接启动了 "trust" 认证.
你可以通过编辑 pg_hba.conf 更改或你下次
行 initdb 时使用 -A或者--auth-local和--auth-host选项.
Success. You can now start the database server using:
    pg_ctl -D /opt/data1 -l logfile start
```
---
title: "7、添加postgis报cannot open shared object file No such file or directory"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/postgis.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## 添加postgis报cannot open shared object file: No such file or directory

安装完瀚高数据库后，客户要求添加postgis，语句执行情况如下

## 1、问题原因

检查该文件的库文件：

```
[highgo@dbtest lib]$ ldd /opt/HighGo6.0.4-cluster/lib/postgresql/postgis-3.so
  linux-vdso.so.1 =>  (0x00007ffecc157000)
  libm.so.6 => /lib64/libm.so.6 (0x00007f4f6f1f6000)
  libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007f4f6eeef000)
  libgeos_c.so.1 => /highgo/lib/libgeos_c.so.1 (0x00007f4f6ecb2000)
  libproj.so.12 => /highgo/lib/libproj.so.12 (0x00007f4f6ea49000)
  libjson-c.so.5 => /highgo/lib/libjson-c.so.5 (0x00007f4f6e835000)
  libprotobuf-c.so.1 => /highgo/lib/libprotobuf-c.so.1 (0x00007f4f6e62c000)
  libxml2.so.2 => /lib64/libxml2.so.2 (0x00007f4f6e2c2000)
  libz.so.1 => /lib64/libz.so.1 (0x00007f4f6e0ac000)
  libdl.so.2 => /lib64/libdl.so.2 (0x00007f4f6dea8000)
  libSFCGAL.so.1 => /highgo/lib/libSFCGAL.so.1 (0x00007f4f6d36a000)
  libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f4f6d154000)
  libc.so.6 => /lib64/libc.so.6 (0x00007f4f6cd87000)
  /lib64/ld-linux-x86-64.so.2 (0x00007f4f6f864000)
  libgeos-3.8.0.so => not found
  libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f4f6cb6b000)
  liblzma.so.5 => /lib64/liblzma.so.5 (0x00007f4f6c945000)
  libCGAL_Core.so.13 => not found
  libboost_thread.so.1.72.0 => not found
  libboost_system.so.1.72.0 => not found
  libboost_serialization.so.1.72.0 => not found
  libCGAL.so.13 => not found
  libgmp.so.10 => /lib64/libgmp.so.10 (0x00007f4f6c6cd000)
  libmpfr.so.6 => not found
```

部分库文件没有加载

## 2、解决方案

一般有两种方法加载库文件：

建议使用第一种方法：

### （1）默认的环境变量中未设置LD\_LIBRARY\_PATH

```
vi .bash_profile
source /opt/HighGo6.0.4-cluster/etc/highgodb.env
export LD_LIBRARY_PATH=/opt/HighGo6.0.4-cluster/lib:/usr/lib64:$LD_LIBRARY_PATH
source .bash_profile
psql
create extension postgis;
ERROR:  could not load library "/opt/HighGo6.0.4-cluster/lib/postgresql/postgis-3.so": libgeos_c.so.1: cannot open shared object file: No such file or directory
exit
```

检查ldd /opt/HighGo6.0.4-cluster/lib/postgresql/postgis-3.so

```
ldd /opt/HighGo6.0.4-cluster/lib/postgresql/postgis-3.so
linux-vdso.so.1 =>  (0x00007fff128f8000)
libm.so.6 => /usr/lib64/libm.so.6 (0x00007f9bba42b000)
libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007f9bba124000)
libgeos_c.so.1 => /opt/HighGo6.0.4-cluster/lib/libgeos_c.so.1 (0x00007f9bb9ee7000)
libproj.so.12 => /opt/HighGo6.0.4-cluster/lib/libproj.so.12 (0x00007f9bb9c7e000)
libjson-c.so.5 => /opt/HighGo6.0.4-cluster/lib/libjson-c.so.5 (0x00007f9bb9a6a000)
libprotobuf-c.so.1 => /opt/HighGo6.0.4-cluster/lib/libprotobuf-c.so.1 (0x00007f9bb9861000)
libxml2.so.2 => /opt/HighGo6.0.4-cluster/lib/libxml2.so.2 (0x00007f9bb94f7000)
libz.so.1 => /usr/lib64/libz.so.1 (0x00007f9bb92e1000)
libdl.so.2 => /usr/lib64/libdl.so.2 (0x00007f9bb90dd000)
libSFCGAL.so.1 => /opt/HighGo6.0.4-cluster/lib/libSFCGAL.so.1 (0x00007f9bb859f000)
libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007f9bb8389000)
libc.so.6 => /usr/lib64/libc.so.6 (0x00007f9bb7fbc000)
/lib64/ld-linux-x86-64.so.2 (0x00007f9bbaa99000)
libgeos-3.8.0.so => /opt/HighGo6.0.4-cluster/lib/libgeos-3.8.0.so (0x00007f9bb7bf4000)
libpthread.so.0 => /usr/lib64/libpthread.so.0 (0x00007f9bb79d8000)
liblzma.so.5 => /usr/lib64/liblzma.so.5 (0x00007f9bb77b2000)
libCGAL_Core.so.13 => /opt/HighGo6.0.4-cluster/lib/libCGAL_Core.so.13 (0x00007f9bb7508000)
libboost_thread.so.1.72.0 => /opt/HighGo6.0.4-cluster/lib/libboost_thread.so.1.72.0 (0x00007f9bb72e8000)
libboost_system.so.1.72.0 => /opt/HighGo6.0.4-cluster/lib/libboost_system.so.1.72.0 (0x00007f9bb70e6000)
libboost_serialization.so.1.72.0 => /opt/HighGo6.0.4-cluster/lib/libboost_serialization.so.1.72.0 (0x00007f9bb6ea3000)
libCGAL.so.13 => /opt/HighGo6.0.4-cluster/lib/libCGAL.so.13 (0x00007f9bb6c6e000)
libgmp.so.10 => /usr/lib64/libgmp.so.10 (0x00007f9bb69f6000)
libmpfr.so.6 => /opt/HighGo6.0.4-cluster/lib/libmpfr.so.6 (0x00007f9bb6780000)
librt.so.1 => /usr/lib64/librt.so.1 (0x00007f9bb6578000)
```
  
pg\_ctl reload执行后报错不变，需要重启数据库
```
pg_ctl restart
```

添加postgis成功。

### （2）在/etc/ld.so.conf添加库文件位置

```
vi /etc/ld.so.conf
/opt/HighGo6.0.4-cluster/lib/
ldconfig
```

添加postgis成功

这种方法不需要重启数据库，但ldconfig后有可能导致操作系统崩溃，可尝试切换用户su - highgo，如果报段错误，不要重启服务器，删除在ld.so.conf添加的内容，重新执行ldconfig，在报段错误时重启服务器，操作系统将无法启动。
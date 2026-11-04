---
title: "16、rpm安装包在银河麒麟上安装失败的解决办法"
book: "数据库使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/rpm_solution.html"
tags:
  - highgo
  - highgo-v45
  - faq-database-usage
---

## rpm安装包在银河麒麟上安装失败的解决办法

## 1、问题描述

安装包：hgdb4.3.4.8-see-kyl-server10sp1-phytium-64-20210315.rpm

执行安装的语句：rpm -ivh hgdb4.3.4.8-see-kyl-server10sp1-phytium-64-20210315.rpm

报错信息：

```
rpm -ivh hgdb4.3.4.8-see-kyl-server10sp1-phytium-64-20210315.rpm
[root@1e73e510-8614-11eb-bae1-00073e92aae0 suntao]# rpm -ivh hgdb4.3.4.8-see-kyl-server10sp1-phytium-64-20210315.rpm 

Verifying...                        ################################# [100%]

准备中...                          ################################# [100%]

        file /usr/lib/.build-id/97/0ce62eca94dbbbbe0a47185ee9b368a417da73 from install of hgdb-see-4.3.4.8-1.ky10.ky10.aarch64 conflicts with file from package readline-7.0-13.ky10.aarch64

        file /usr/lib/.build-id/22/0d2cb69732c04b577b9f6e5fc4c0f89665dc41 from install of hgdb-see-4.3.4.8-1.ky10.ky10.aarch64 conflicts with file from package libxcrypt-4.4.8-4.ky10.aarch64

        file /usr/lib/.build-id/a5/a99059c2ca3f128f8780e825ba4632e999a651 from install of hgdb-see-4.3.4.8-1.ky10.ky10.aarch64 conflicts with file from package libxml2-2.9.8-9.ky10.aarch64

        file /usr/lib/.build-id/32/dfd0f96823def572c25596fd35c5258665f3c1 from install of hgdb-see-4.3.4.8-1.ky10.ky10.aarch64 conflicts with file from package json-c-0.13.1-6.ky10.aarch64

        file /usr/lib/.build-id/65/cccff1be07e4fea5359f2e70f565c8adcb4701 from install of hgdb-see-4.3.4.8-1.ky10.ky10.aarch64 conflicts with file from package libxslt-1.1.32-7.ky10.aarch64
```

如上，rpm执行安装后，未正确安装完成，而且未报明确错误。

## 2、问题原因

数据库自带了所需的依赖，但是在操作系统中也存在，导致冲突，强制安装使用自带的依赖。

## 3、解决方案

增加–force选项，进行强制安装。

```
rpm -ivh -hgdb4.3.4.8-see-kyl-server10sp1-phytium-64-20210315.rpm --force
```
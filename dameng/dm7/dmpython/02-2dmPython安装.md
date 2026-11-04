---
title: "2 dmPython安装"
book: "DM7 dmPython使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmPython使用手册.htm"
tags:
  - dameng
  - dm7
  - dmpython
---

`dmPython`可以运行在任何安装了`python`的平台上。可以使用安装包安装，另外需要保证`dpi`和`dmPython`版本一致，都是32位或都是64位。

`dmPython`的运行需要使用`dpi`动态库，用户应将`dpi`所在目录（一般为`DM`安装目录中的`bin`目录）加入系统环境变量。

在`Windows`操作系统下安装`dmPython`只需要直接执行`exe`文件即可。

在`Linux`操作系统下使用`rpm`包安装`dmPython`。安装和卸载命令参考如下：

```
安装：rpm -ivh dmPython-2.1-7.1-py33-1.x86_64.rpm --nodeps
卸载：rpm -e dmPython-2.1-1.x86_64
```

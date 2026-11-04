---
title: "1 dmPython简介"
book: "DM7 dmPython使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmPython使用手册.htm"
tags:
  - dameng
  - dm7
  - dmpython
---

`dmPython`是`DM`提供的依据`Python DB API version 2.0`中`API`使用规定而开发的数据库访问接口。`dmPython`实现这些`API`，使`Python`应用程序能够对`DM`数据库进行访问。

`dmPython`通过调用`DM DPI`接口完成`python`模块扩展。在其使用过程中，除`Python`标准库以外，还需要`DPI`的运行环境。

`dmPython`接口当前版本号为`2.3`，下表指明了`dmPython`接口的版本与服务器版本和`python`的版本之间的对应情况。

表`1.1 dmPython`版本对照表

| dmPython版本 | DM Server版本 | Python版本 |
| --- | --- | --- |
| 2.3 | 7.0.0.9以上 | 2.6及以上 |

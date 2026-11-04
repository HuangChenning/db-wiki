---
title: "2 使用dmdbchk"
book: "DM7 dmdbchk使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmdbchk使用手册.htm"
tags:
  - dameng
  - dm7
  - dmdbchk
---

`dmdbchk`工具需要从命令行启动。找到`dmdbchk`所在安装目录`/dmdbms/bin`，输入`dmdbchk`和参数后回车。参数在下一节详细介绍。

语法如下：

```
dmdbchk ini_file_path
```

`ini_file_path`：`dm.ini`绝对路径或者当前目录的`dm.ini`。

> 经过初始化，且正常关闭的数据库，才能被dmdbchk工具校验， 否则dmdbchk会报错退出。

例如，正常关闭`/home/test/dmdbms`目录下数据库后，使用`dmdbchk`对数据库进行校验。

```
./dmdbchk PATH=/home/test/dmdbms/dm.ini
```

如果`dm.ini`在`dmdbchk`当前目录，也可以写成这样：

```
./dmdbchk PATH=dm.ini
```

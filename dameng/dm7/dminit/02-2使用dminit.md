---
title: "2 使用dminit"
book: "DM7 dminit使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dminit使用手册.htm"
tags:
  - dameng
  - dm7
  - dminit
---

`dminit`工具需要从命令行启动。找到`dminit`所在安装目录`/dmdbms/bin`，输入`dminit`和参数后回车。参数在下一节详细介绍。

语法如下：

```
dminit KEYWORD=value { KEYWORD=value }
```

`KEYWORD`：`dminit`参数关键字。多个参数之间排列顺序无影响，参数之间使用空格间隔。

`value`：参数取值。

> dminit如果没有带参数，系统会引导用户进行设置。 参数、等号和值之间不能有空格，例如PAGE_SIZE=16。 HELP参数的后面不用添加“=”号。

例如，初始化一个数据库，放在`/home/test/dmdbms`目录下，数据页`PAGE_SIZE`大小为`16K`。

```
./dminit PATH=/home/test/dmdbms PAGE_SIZE=16
```

如果创建成功，则屏幕显示如下：

```
initdb V7.1.5.22-Build(2015.11.17-62910trunc)
db version: 0x70009
create dm database success. 2015-12-21 15:46:27
```

此时在`/home/test/dmdbms`目录下会出现一个`DAMENG`文件夹，内容包含初始数据库`DAMENG`的相关文件和`DM`数据库启动所必须的配置文件`dm.ini`。

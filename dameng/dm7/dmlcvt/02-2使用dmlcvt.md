---
title: "2 使用dmlcvt"
book: "DM7 dmlcvt使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmlcvt使用手册.htm"
tags:
  - dameng
  - dm7
  - dmlcvt
---

`dmlcvt`工具需要从命令行启动。找到`dmlcvt`所在安装目录`/dmdbms/bin`，输入`dmlcvt`和参数后回车。参数在下一节详细介绍。

语法如下：

```
dmlcvt KEYWORD=value { KEYWORD=value }
```

`KEYWORD`：`dmlcvt`参数关键字。多个参数之间排列顺序无影响，参数之间使用空格间隔。

`value`：参数取值。

例如，通过解析控制文件`/opt/DAMENG/dm.ctl`，进而解析出所有日志文件。

```
./dmlcvt F_TYPE=1 F_PATH=/opt/DAMENG/dm.ctl out_path=/emc_2/temp
```

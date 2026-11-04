---
title: "4 dmdbchk报告解读"
book: "DM7 dmdbchk使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmdbchk使用手册.htm"
tags:
  - dameng
  - dm7
  - dmdbchk
---

dmdbchk校验的过程对用户不可见，校验的结果以报告的形式呈现给用户。

dmdbchk报告内容分为七部分：一 dmdbchk版本信息；二 开始标志；三 数据文件校验结果；四 索引校验结果；五 对象ID校验结果；六 结束标志；七 错误总数。

图4.1 dmdbchk报告内容

数据文件校验结果、索引校验结果、对象ID校验结果三部分内容伸缩性较大，内容多少由数据库大小决定。对于数据文件校验结果和索引校验结果，如果校验成功，直接打印出具体校验的对象；如果校验失败，则打印出具体错误信息。对于对象ID校验结果，如果校验成功，不打印出具体校验的对象；如果校验失败，则打印出具体错误信息。

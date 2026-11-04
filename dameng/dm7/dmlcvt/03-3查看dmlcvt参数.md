---
title: "3 查看dmlcvt参数"
book: "DM7 dmlcvt使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmlcvt使用手册.htm"
tags:
  - dameng
  - dm7
  - dmlcvt
---

`dmlcvt`使用简单灵活。用户可使用`“dmlcvt HELP”`快速查看参数用法。

```
./dmlcvt HELP
格式: dmlcvt.exe KEYWORD=value
例子: dmlcvt.exe F_TYPE=1 F_PATH=c:\dmdbms\data\DAMENG\dm.ctl OUT_PATH=d:\temp
关键字 说明(默认值)
-----------------------------------------------------------------------------
F_TYPE 必选，表示读入的日志文件类型,与F_PATH配合使用，可选值为1, 2, 3, 4, 5
1 F_TYPE 必须指向控制文件 dm.ctl
2 F_TYPE 必须指向归档目录
3 F_TYPE 必须指向单个日志文件
4 F_TYPE 必须指向控制文件 dm.ctl，调整ckpt_file/ckpt_offset到上一个合法位置（向后扫描）
5 F_TYPE 必须指向控制文件 dm.ctl，从系统当前ckpt_file/ckpt_offset向前扫描找到联机日志文件中有效的最小lsn及其偏移作为新的ckpt信息，调整ckpt_lsn/ckpt_file /ckpt_offset
F_PATH 必选，对应F_TYPE的路径
LOG_PATH 可选，是否依赖控制文件中的日志路径 bool型，可选值 1/0
仅当F_TYPE为1时有效；默认为1，值为0时日志文件必须与控制文件同目录
REC_LEVEL 可选，打印rec信息级别，可选值为1， 2， 3，默认为3
1 仅打印ptx信息
2 仅打印rec信息
3 打印ptx和rec信息
REC_DATA 可选，是否打印rec数据（以16进制显示）bool型，默认为 0
PAGE_INFO 可选，是否打印页信息，bool型，默认为1
OUT_PATH 必选，输出文件路径，默认包含以下文件: rec_info.txt, page_info.txt, file_info.txt, warn_info.txt
OUT_SIZE 可选，输出文件最大大小，单位（M），默认为 10
LSN_START 可选，从该lsn开始打印，
LSN_END 可选，直到该lsn结束打印
PTX_COUNT 可选，总共打印多少ptx
F_OFFSET 可选，文件偏移，仅对单个日志文件有效，即当F_TYPE=3时有效
DB_MAGIC 可选，db_magic值, 仅对归档模式有效，即当F_TYPE=2时有效
CALC_OFF 可选，在指定了F_OFFSET时，是否再计算有效rpag偏移，默认为1
TS_ID 可选，指定表空间id
FILE_ID 可选，指定文件id
PAGE_NO 可选，指定页号
REC_TYPE 可选，指定记录类型
ENC_FLAG 可选，日志文件是否加密
SYSTEM_PATH 可选，日志加密时指定system.dbf路径，供获取db_key
```

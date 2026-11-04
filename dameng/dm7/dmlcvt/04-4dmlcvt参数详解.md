---
title: "4 dmlcvt参数详解"
book: "DM7 dmlcvt使用手册"
version: "DM7"
source: "temp/doc/special/DM7°ïÖúÎÄµµ.chm#~htm/dmlcvt使用手册.htm"
tags:
  - dameng
  - dm7
  - dmlcvt
---

## 4.1 F_TYPE

```
必选参数，表示读入的日志文件类型。与F_PATH配合使用，可选值为1、2、3、4、5。
- 1：表示F_PATH指向控制文件dm.ctl。分析的是dm.ctl中指定的联机日志；
- 2：表示F_PATH 指向归档目录。分析的是归档目录下的归档日志；
- 3：表示F_PATH 指向单个日志文件。分析的是指定的联机或归档日志；
- 4：表示F_PATH指向控制文件dm.ctl，调整当前日志的ckpt_file/ckpt_offset到上一个合法位置（向后扫描）。合法位置是指一个完整的ptx起始位置。分析的是dm.ctl中指定的联机日志；
- 5：表示F_PATH 指向控制文件 dm.ctl，从系统当前ckpt_file&ckpt_offset向前扫描找到联机日志文件中有效的最小lsn及其偏移作为新的ckpt信息（ckpt_lsn/ckpt_file/ckpt_offset）。分析的是dm.ctl中指定的联机日志。
```

## 4.2 F_PATH

必选参数，对应`F_TYPE`的绝对路径。

## 4.3 LOG_PATH

可选参数，是否依赖控制文件中的日志路径。布尔类型，可选值 `1/0`，默认为1。仅当`F_TYPE`为1时有效。值为1时，依赖；值为0时，不依赖，为0时要求日志文件必须与控制文件的目录相同。

## 4.4 REC_LEVEL

可选参数，打印`rec`信息级别。可选值为1，2，3，默认为3。

- 1：表示仅打印`ptx`信息。`ptx`信息是物理事务信息；
- 2：表示仅打印`rec`信息。`rec`信息是物理事务对应的记录信息；
- 3：表示打印`ptx`和`rec`信息。

打印的结果存储在`rec_info000.txt`报告中。

## 4.5 REC_DATA

可选参数，是否打印`rec`数据（以16进制显示）。布尔类型，可选值：1是，0否。默认为0。

一条完整的日志记录包含`rec`信息和`rec`数据两部分。`rec`信息是指表空间号、文件号、页号等；`rec`数据指的是实际日志数据。

## 4.6 PAGE_INFO

可选参数，是否打印页信息。页信息存储在`page_info000.txt`报告中。布尔类型，可选值：1是，0否。默认为1。

## 4.7 OUT_PATH

必选参数，输出文件绝对路径。输出文件夹中包含以下文件:

- `rec_info000.txt`：记录物理事务信息和事务对应的记录信息；
- `page_info000.txt`：记录日志页信息；
- `file_info.txt`：记录日志文件信息；
- `warn_info.txt`：记录警告信息和错误信息。

## 4.8 OUT_SIZE

可选参数，单个输出文件最大大小。取值范围：`1~100`，单位M，默认为10。

当一个文件大小达到`OUT_SIZE`指定大小后，继续生成下一个。例如，`page_info000.txt`、`page_info001.txt......`以此类推。

## 4.9 LSN_START

可选参数，从该`lsn`开始打印。默认从第一个`lsn`开始打印。

## 4.10 LSN_END

可选参数，直到该`lsn`结束打印。默认直到最后一个`lsn`结束打印。

## 4.11 PTX_COUNT

可选参数，总共打印多少`ptx`。

## 4.12 F_OFFSET

可选参数，文件偏移，仅对单个日志文件有效，即当`F_TYPE=3`时有效。只解析指定文件偏移之后的日志。

## 4.13 DB_MAGIC

可选参数，`db_magic`值，仅对归档模式有效，即当`F_TYPE=2`时有效。只解析指定`db_magic`之后的日志。

## 4.14 CALC_OFF

可选参数，在指定了`F_OFFSET`时，是否再计算有效日志页（`rpag`）偏移。可选值：1是，0否。默认1。

因为指定的`F_OFFSET`并不一定是有效的`redo`日志页偏移，指定了`CALC_OFF`参数后，工具会根据指定的`F_OFFSET`计算出有效的`rpag`偏移。

如果指定了`CALC_OFF = 0`，那么用户一定要保证指定的`F_OFFSET`是一个有效的`rpag`偏移，否则报错。

## 4.15 TS_ID

可选参数，指定表空间`id`。

不使用此参数时，默认解析所有表空间的日志；当使用此参数时，只能指定一个表空间`id`，只解析此表空间日志。

## 4.16 FILE_ID

可选参数，指定文件`id`。

不使用此参数时，默认解析所有文件的日志；当使用此参数时，只能指定一个文件`id`，只解析文件`id`为指定值的文件的日志。

## 4.17 PAGE_NO

可选参数，指定页号。

不使用此参数时，默认解析数据库中所有页的日志；当使用此参数时，只能指定一个页号，只解析页号为指定值的页的日志。

> 当同时指定参数TS_ID、FILE_ID和PAGE_NO中的两个或三个时，解析内容由指定的参数值共同决定： 如仅指定PAGE_NO=10，则解析所有表空间的所有文件中页号为10 的页的日志； 若指定TS_ID=2 PAGE_NO=10，则解析指定表空间id为2的表空 间中所有文件中页号为10 的页的日志。

## 4.18 REC_TYPE

可选参数，指定记录类型，只打印指定的记录类型。

当不指定此参数时，打印全部记录类型；若指定此参数，则只能指定某一种记录类型。

日志共有15种记录类型。如下表所示：

表`4.1` 日志的记录类型

| 宏定义 | 记录类型 |
| --- | --- |
| RREC_TYPE_PTX_END | 0 |
| RREC_TYPE_BYTE | 1 |
| RREC_TYPE_WORD | 2 |
| RREC_TYPE_DWORD_0 | 3 |
| RREC_TYPE_DWORD | 4 |
| RREC_TYPE_TRXID_H0 | 5 |
| RREC_TYPE_TRXID | 6 |
| RREC_TYPE_LINT64 | 7 |
| RREC_TYPE_DDWORD | 8 |
| RREC_TYPE_ANY | 9 |
| RREC_TYPE_TIME | 10 |
| RREC_TYPE_PAGE_CREATE | 11 |
| RREC_TYPE_FSM_PAGE_INIT | 12 |
| RREC_TYPE_DW | 13 |
| RREC_TYPE_INC_BYTE6 | 14 |
| RREC_TYPE_LOGICAL | 15 |

## 4.19 ENC_FLAG、SYSTEM_PATH

`ENC_FLAG`和`SYSTEM_PATH`，日志被加密的时候使用。

`ENC_FLAG`，可选参数，日志文件是否被加密。可选参数：1是，0否。默认0。

`SYSTEM_PATH`，可选参数，如果日志被加密了（`ENC_FLAG=1`），那么一定要指定`system.dbf`路径，供获取`db_key`。因为`db_key`保存在`system.dbf`中。如果不指定，会在`F_PATH`指定的路径下找`system.dbf`。

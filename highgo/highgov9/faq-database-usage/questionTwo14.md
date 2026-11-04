---
title: "无法把类型 timestamp with time zone 转换为 timestamp"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo14.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

## 无法把类型 timestamp with time zone 转换为 timestamp

## 环境

- CPU：Hygon C86 7380 32-core Processor
- 操作系统：BigCloud Enterprise Linux For Euler 22.10 LTS
- 数据库版本：9.0.3.2
- 兼容模式：Oracle

## 问题描述及解决方法

**问题描述** ：

在执行插入数据时，出现如下错误：

```
### SQL: INSERT INTO RMS_WORK_ORDER         (TASKID, SERIALNUMBER, PROJECTCODE, PROJECTNAME, AENDNAME,          BENDNAME, OCCPNUM, DIVERGENCESTRETCHNUM, INVESTMENT,          DESIGNER, TASKTOTALDAY, TEMPLATETYPE, SYNCHTYPE,          CONSTRUCTUNITID, CONSTRUCTUNITNAME, COMPLETEDATE, PREFECTURENAME,          COUNTYNAME, ROADNAME, PORESEGMENTNUM, PIPEDUCTLENGTH,          PORESEGMENTLENGTH, WELLNUM, MEMO, BUILDUNIT,          MANAGEMENTUNIT, ODPNUM, POLENUM, TERMINALPOLENUM,          EMBEDJOINTPITNUM, JOINTSNUM, OPTICALCONNECTEDNUM, OVERHEADOPTICALLENGTH,          FOPTICALLENGTH, BOPTICALLENGTH, GOPTICALLENGTH, ZOPTICALLENGTH,          QOPTICALLENGTH, OPTICALROUTELENGTH, OPTICALDESIGNLENGTH, OPTICALCOILERLENGTH,          WORKORDERTHEME, WORKORDERNO, URGENCY, WORKORDERCATEGORY,          WORKORDERPERSON, WORKORDERSOURCE, CITY_NAME, CITY_ID,          COUNTY_NAME, COUNTY_ID, TIME_STAMP, CREATOR,          CREAT_TIME, MODIFIER, MODIFY_TIME, STATEFLAG,          AUTOPASS, INT_ID, TASKNO, TASKNAME,          TASKDESCRIPTION, PROJECTLABEL, EXECUTOR, PROVINCE)         VALUES         (?, ?, ?, ?, ?,          ?, ?, ?, ?,          ?, ?, ?, 1,          ?, ?,now()::timestamp + '1 month',null,          null,?, ?, ?,          ?,?, ?, ?,          ?, ?, ?, ?,          ?,?, ?,  ?,          ?,?, ?, ?,          ?,?, ?, ?,          ?, ?, ?, ?,          ?, ?, ?, ?,          ?, ?, current_timestamp, ?,          current_timestamp, ?, ?, 0,          0, ?, ?, ?,          ?, ?, ?, ?)
### Cause: org.postgresql.util.PSQLException: 错误: 无法把类型 timestamp with time zone 转换为 timestamp
  位置：1170
; bad SQL grammar []; nested exception is org.postgresql.util.PSQLException: 错误: 无法把类型 timestamp with time zone 转换为 timestamp
  位置：1170
```

**解决方法** ：

```
在 oracle 兼容中，时间类型数据的计算要使用 oracle 的方式。把里面的\`now()::timestamp + '1 month'\`改成 oracle 的写法\`sysdate + interval '1' month\`。
```
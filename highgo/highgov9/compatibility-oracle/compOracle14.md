---
title: "序列"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle14.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 序列

## 说明

- SHARING

该子句仅应用于应用程序根中。这种序列称为应用程序公共对象，要确定如何共享序列，请指定一下共享属性之一：

METADATA:元数据链接共享序列的元数据，但其数据对每个容器都是唯一的，这种序列称为元数据链接的应用程序公共对象。

DATA:数据链接共享该序列，其数据对应应用程序容器中的所有容器都是相同的。其数据仅存储在应用程序根目录中。这种类型的序列被称为数据链接应用程序公共对象

NONE:序列不共享

仅支持语法。

- INCREMENT BY

指定两个序列号之间的间隔。可以指定正整数或负整数，但是不能指定为0，不指定则默认间隔为1

- START WITH

指定序列的起始值

- MAXVALUE/NOMAXVALUE

指定序列的最大值，默认为NOMAXVALUE,为NOMAVALUE时，最大值为9223372036854775807或者降序时为-1

- MINVALUE/NOMINVALUE

指定序列的最小值，默认为NOMINVALUE，为NOMINVALUE时，最小值为1或者降序时为-9223372036854775808

- CYCLE/NOCYCLE

当到达了序列的最大或最小值时能继续生从最小序列值开始生成序列，默认为NOCYCLE

- CACHE/NOCACHE

指定数据库预先生成多少个序列值，为了加快序列的访问，NOCACHE指定数据库不缓存序列值，当都不指定时，默认CHACEH值为20，指定cache值必须大于1.

- ORDER/NOORDER

该选项用于数据库集群获取有序序列，指定ORDER以确保序列号按照请求顺序生成，默认为NOORDER

仅支持语法。

- KEEP/NOKEEP

如果希望NEXTVAL在重放应用程序连续性期间保持其原始值则指定KEEP,默认为NOKEEP

仅支持语法。

- SCALE/NOSCALE

使用SCALE启用序列的可伸缩性，当指定SCALE时，将在序列的开头附加一个数字偏移量，以删除生成值中所有重复项，默认为NOSCALE

EXTEND: 生成序列值都是长度(x+y),其中x是可伸缩放偏移的长度(默认值为6)，y则是序列中的最大位数。且使用SCALE时，不建议在序列上同时使用ORDER

NOEXTEND:SCALE的默认设置。使用NOEXTEND时，生成的序列值最多与序列中的最大位数一样宽。此设置对于使用序列填充固定宽度列的现有应用程序集成非常有用

- SHARD/NOSHARD

使用SHARD可以跨越分片生成唯一的序列号。序列对象被创建为一个全局的、所有分片的分片对象，它在所有分片上返回唯一的序列值。序列对象也在目录数据库中创建，该数据库返回相对于碎片数据库的唯一序列值,默认为NOSHARD.

EXTEND:生成序列的值都是长度(x+y),其中x是大小为4的偏移长度。大小为4对应与最大碎片数的宽度。即1000个分片固定在序列值的开头。y是序列maxvalue/minvalue中的最大位数

NOEXTEND:默认选项，生成的序列值最多与序列maxvalue/minvalue中最大位数一样宽，如果指定了SHARD NOEXTEND的序列调用了NEXTVAL。如果生成的值超出序列的最大值/最小值，则会引发用户错误。

仅支持语法。

- SESSION/GLOBAL

当指定SESSION创建序列时，这是一种特殊类型的序列，专门用于具有会话可见性的全局临时表，会话序列只在会话内返回唯一的序列范围，而不在会话间返回。另一个区别是会话序列不是持久的，如果会话退出，会话期间访问的会话序列的状态也会退出，但会话序列还存在。GLOBAL为全局普通序列，默认为GLOBAL.

- RESTART

该选项用于 **ALTER SEQUENCE** 中，将NEXTVAL重置为升序的MINVALUE，对于降序，RESTART将NEXTVAL重置为MAXVALUE，如果要重置不同起始值需要和START WITH一起使用。

使用伪列 **NEXTVAL** 和 **CURRVAL** 来引用序列值。对NEXTVAL的第一次引用返回序列的初始值，后续对NEXTVAL的引用按定义的增量递增序列值，并返回新值。对CURRVAL的任何引用都会返回序列的当前值，即最后一次对NEXTVAL的引用返回的值。

在会话中对序列使用CURRVAL之前，必须先使用NEXTVAL初始化序列。

## 示例

- 创建正常序列

create sequence seq1 sharing=metadata increment by 2 start with 30 minvalue 10 maxvalue 50 cycle cache 2 order keep noscale global;

初始化序列

select seq1.nextval from dual;

获取当前值

select seq1.currval from dual;

获取下一个值

select seq1.nextval from dual;
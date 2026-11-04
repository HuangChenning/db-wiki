---
title: "3、HG数据库恢复表中被删除的列"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/recover_colum.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HG数据库恢复表中被删除的列

在PG和瀚高数据库中当一个表的列被删除时，其实并没有真正的删除而是在系统表中将该列标记为删除，在表不经过VACUUM FULL和UPDATE操作的情况下，通过修该pg\_attribute表的attname、atttypid、attisdropped列的值是可以对被删除的列的值进行恢复。其中数据库自动的VACUUM不是VACUUM FULL。

## pg\_attribute表字段的信息：

| 名字 | 类型 | 引用 | 描述 |
| --- | --- | --- | --- |
| attrelid | oid | pg\_class.oid | 此字段所属的表。 |
| atttypid | oid | pg\_type.oid | 字段的数据类型。 |
| attstattarget | int4 |  | attstattarget控制ANALYZE为这个字段设置的统计细节的级别。零值表示不收集统计信息，负数表示使用系统缺省的统计对象。正数值的确切信息是和数据类型相关的。 |
| attlen | int2 |  | 该字段所属类型的长度。(pg\_type.typlen的拷贝) |
| attnum | int2 |  | 字段的编号，普通字段是从1开始计数的。系统字段，如oid，是任意的负数。 |
| attndims | int4 |  | 如果该字段是数组，该值表示数组的维数，否则是0。 |
| attcacheoff | int4 |  | 在磁盘上总是-1，但是如果装载入内存中的行描述器中， 它可能会被更新为缓冲在行中字段的偏移量。 |
| atttypmod | int4 |  | 表示数据表在创建时提供的类型相关的数据(比如，varchar字段的最大长度)。其值对那些不需要atttypmod的类型而言通常为-1。 |
| attbyval | bool |  | pg\_type.typbyval字段值的拷贝。 |
| attstorage | char |  | pg\_type.typstorage字段值的拷贝。 |
| attalign | char |  | pg\_type.typalign字段值的拷贝。 |
| attnotnull | bool |  | 如果该字段带有非空约束，则为真，否则为假。 |
| atthasdef | bool |  | 该字段是否存在缺省值，此时它对应pg\_attrdef表里实际定义此值的记录。 |
| attisdropped | bool |  | 该字段是否已经被删除。如果被删除，该字段在物理上仍然存在表中，但会被分析器忽略，因此不能再通过SQL访问。 |
| attislocal | bool |  | 该字段是否局部定义在对象中的。 |
| attinhcount | int4 |  | 该字段所拥有的直接祖先的个数。如果一个字段的祖先个数非零，那么它就不能被删除或重命名。 |

## 1、删除表列

创建测试表并查询pg\_attribute：

```
create table test1(id int,name varchar(32),    address varchar(30));
insert into test1 values(1,'张三','北京');
insert into test1 values(2,'李四','上海');

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 北京
  2 | 李四 | 上海
(2 rows)

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test2'::regclass and attnum >0;
 attrelid | attname | atttypid | attnum | attisdropped 
----------+---------+----------+--------+--------------
    57355 | id      |       23 |      1 | f 
    57355 | name    |     1043 |      2 | f
    57355 | address |     1043 |      3 | f
(3 rows)
```

通过使用::regclass, 我们就不需要通过查询pg\_class表来获取对象与oid的对应关系了,也可以通过pg\_class获取到oid，语句如下。

```
select oid from pg_class where relname='test1';
select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='查询到的oid' and attnum >0;
```

查询结果中attnum是字段的编号，普通字段是从1开始计数的。系统字段，如oid，是任意的负数。

删除列后，查看到这个

列对应的行的attname变为了 ……..pg.dropped.3……..，且字段类型也从原有数值变为了0，attisdropped也从f变为了空，被打上了删除标记。

注意：atttypid字段类型需要和原来的相对应，否则尽管数据恢复了，数据也是错的，可能原来相应的存储的字母变为数字等等。

```
alter table test1 drop column address;

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test1'::regclass and attnum >0;
 attrelid |           attname            | atttypid | attnum | attisdropped 
----------+------------------------------+----------+--------+--------------

    57355 | id                           |       23 |      1 | f
    
    57355 | name                         |     1043 |      2 | f
    
    57355 | ........pg.dropped.3........ |        0 |      3 | t

update pg_attribute set attname='address',atttypid=1043,attisdropped='f' where attrelid='test1'::regclass and attnum=3;

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 北京
  2 | 李四 | 上海
(2 rows)
```

结论：数据可以正常恢复。其中

attname：表示表中列的名字。

atttypid：表示表中列的字段类型。

attisdropped：表示表中的列是否被删除；

f表示未被删除；

t表示被删除。

## 2、表列删除后，执行VACUUM FULL操作

```
select * from test1;

alter table test1 drop column address;

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test1'::regclass and attnum >0;

vacuum full test1;

update pg_attribute set attname='address',atttypid=1043,attisdropped='f' where attrelid='test1'::regclass and attnum=3;

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 
  2 | 李四 |
```

结论：被删除的列不会恢复

## 3、表列被删除后，执行VACUUM操作

恢复数据

```
select * from test1;

alter table test1 drop column address;

select * from test1;

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test1'::regclass and attnum >0;

vacuum  test1;

update pg_attribute set attname='address',atttypid=1043,attisdropped='f' where attrelid='test1'::regclass and attnum=3;

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 北京
  2 | 李四 | 上海
(2 rows)
```

结论：数据可以正常恢复。

## 4、删除列后，执行INSERT

```
alter table test1 drop column address;

insert into test1 values(1,'王二');

select * from test1;

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test1'::regclass and attnum >0;

update pg_attribute set attname='address',atttypid=1043,attisdropped='f' where attrelid='test1'::regclass and attnum=3;

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 北京
  2 | 李四 | 上海
  1 | 王二 | 

(3 rows)
```

结论：表在删除列后新增的列，在删除的列恢复后，新增列无值，原始行该列的值被恢复。删除列上的若原有非空约束也会消失

## 5、删除列后，执行UPDATE

```
alter table test1 drop column address;

select * from test1;

update test1 set name='王名' where name='李四';

select * from test1;

select attrelid,attname,atttypid,attnum,attisdropped from pg_attribute where attrelid='test1'::regclass and attnum >0;

update pg_attribute set attname='address',atttypid=1043,attisdropped='f' where attrelid='test1'::regclass and attnum=3;

highgo=# select * from test1;
 id | name | address 
----+------+---------
  1 | 张三 | 北京
  2 | 王名 | 
(2 rows)
```

结论：表在删除列后UPDATE，在删除的列恢复后，被UPDATE的行的列的值无法恢复。
---
title: "数组类型"
book: "数据类型"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/array.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-types
---

## 数组类型

### 数组类型定义和插入

HGDB 允许一个表中的列定义为变长多维数组，可以创建任何内建或用户定义的基类、枚举类型、组合类型或者域类型的数组。

一个数组数据类型可以通过在数组元素的数据类型名称后面加上方括号（\[\]）来命名。 `CREATE TABLE` 的语法允许指定数组的确切大小，如果不进行指定，那么数据的长度和维度都不受限制。实际上， `CREATE TABLE` 中声明数组的尺寸或维度仅仅只是文档而已，它并不影响运行时的行为。

例如在创建表 grape 时将 taste 定义为长度为1的数组，将 info 定义为长度不限制的数组：

```sql
CREATE TABLE grape (taste text[1],info int[][]);

INSERT INTO grape VALUES ('{sweet}','{1,2,3}'),('{sour}','{4,5,6}');
INSERT INTO grape VALUES ('{sweet,sour,sweet_and_sour}');
INSERT INTO grape VALUES('{sweet}','{{1},{2}}');
INSERT INTO grape VALUES('{bad}','{0,0,0}');
```

还可以用关键词 `ARRAY` 定义一维数组。同前面一样，数组可以不指定尺寸，并且 HGDB 在任何情况下都不会强制尺寸限制。

```sql
CREATE TABLE grape_(info int ARRAY[4]);

INSERT INTO grape_ VALUES(ARRAY[10,20]);
INSERT INTO grape_ VALUES('{12,6}');
```

注意，插入多条多维数组时，多维数组的每一维都必须有相匹配的长度，不匹配会造成错误。

### 访问数组

访问数组中的元素时，可以将数组下标写在方括号内，HGDB 默认数组下标从1开始。

```sql
highgo=# SELECT taste FROM grape WHERE info[1]=1;
  taste  
---------
 {sweet}
(1 行记录)
```

如果数组本身为空或者任何一个下标表达式为空，访问数组下标表达式将会返回空值。如果下标超过了数组边界，下标表达式也会返回空值（这种情况不会抛出错误）。相似地，使用错误的下标号引用一个数组会得到空值而不是错误。

### 修改数组

数组可以作为一个数组值被整个替换，也可以在某一个元素上被更新。

```sql
UPDATE grape SET taste='{sweet_and_sour}' where taste='{sweet,sour,sweet_and_sour}';
UPDATE grape SET info='{100,0,0}' WHERE taste='{sweet}';
UPDATE grape SET info=ARRAY[0,100,0] WHERE taste='{sour}';
UPDATE grape SET info[1]=50,info[2]=50 WHERE taste='{sweet_and_sour}';
```

### 在数组中搜索

要搜索数组中值的”存在“情况，可以用关键字 `ANY` 来实现。例如搜索 info 数组里面所有出现元素100的数据：

```sql
highgo=# SELECT* FROM grape WHERE '100'= ANY(info);
  taste  |   info    
---------+-----------
 {sweet} | {100,0,0}
 {sweet} | {100,0,0}
 {sour}  | {0,100,0}
(3 行记录)
```

如果存在一个数组的所有元素值都相同，可以用关键字 `ALL` 来进行搜索。例如搜索info数组中所有元素的值都为0的数据：

```sql
highgo=# SELECT* FROM grape WHERE '0'= ALL(info);
 taste |  info   
-------+---------
 {bad} | {0,0,0}
(1 行记录)
```
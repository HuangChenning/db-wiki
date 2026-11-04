---
title: "其他类型"
book: "数据类型"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/other.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-types
---

## 其他类型

### 几何类型

几何数据类型表示二维的空间物体。

| 名字 | 存储尺寸 | 表示 | 描述 |
| --- | --- | --- | --- |
| point | 16字节 | 平面上的点 | (x,y) |
| line | 32字节 | 无限长的线 | {A,B,C}（A、B都不为0） |
| lseg | 32字节 | 有限线段 | ((x1,y1),(x2,y2)) |
| box | 32字节 | 矩形框 | ((x1,y1),(x2,y2)) |
| path | 16+16n 字节 | 封闭路径（类似于多边形） | ((x1,y1),…) |
| path | 16+16n 字节 | 开放路径 | \[(x1,y1),…\] |
| polygon | 40+16n 字节 | 多边形（类似于封闭路径） | ((x1,y1),…) |
| circle | 24字节 | 圆 | <(x,y),r>（中心点和半径） |

### 网络地址类型

HGDB 提供用于存储 IPv4、IPv6 和 MAC 地址的数据类型。 用这些数据类型存储网络地址比用纯文本类型好，因为这些类型提供输入错误检查以及特殊的操作符和函数。

| 名字 | 存储尺寸 | 描述 |
| --- | --- | --- |
| cidr | 7或19字节 | IPv4 和 IPv6 网络 |
| inet | 7或19字节 | IPv4 和 IPv6 主机以及网络 |
| macaddr | 6字节 | MAC 地址 |
| macaddr8 | 8 byte | MAC 地址（EUI-64 格式） |

在对 inet 或者 cidr 数据类型进行排序的时候， IPv4 地址将总是排在 IPv6 地址前面，包括那些封装或者是映射在 IPv6 地址里 的 IPv4 地址，例如::10.2.3.4 或者::ffff::10.4.3.2。

### 位串类型

位串就是一串 1 和 0 的串，它们可以用于存储和可视化位掩码。

| 名字 | 描述 |
| --- | --- |
| bit(n) | 定长 |
| bit varying(n) | 变长 |

n 是一个正整数，bit 类型的数据必须准确匹配长度 n，更短或更长的位串都会被拒绝；bit varying 数据是最长位数为 n 的变长类型。写一个没有长度的 bit 等效于 bit(1)，没有长度的 bit varying 意味着没有长度限制。位串类型在输入时也需要用单引号包围。

### 文本搜索类型

HGDB 提供两种数据类型：tsvector 和 tsquery，它们被设计用来支持全文搜索，全文搜索是一种在自然语言的文档集合中搜索以定位那些最匹配一个查询的文档的活动。

| 名字 | 描述 |
| --- | --- |
| tsvector | tsvector 类型表示一个为文本搜索优化的形式下的文档，tsvector 的值是一个排序的可区分词位的列表。 |
| tsquery | tsquery 类型表示一个文本查询，一个 tsquery 值存储用于搜索的词位，并且使用布尔操作符 &(AND)，\|(OR) 和!(NOT) 来组合它们。 |

### UUID类型

数据类型 uuid 存储由 RFC 4122、ISO/IEC 9834-8:2005 以及相关标准定义的通用唯一标识符（UUID），这种标识符是一个 128 位的量。

一个 UUID 被写成一个小写十六进制位的序列，该序列被连字符分隔成多个组：首先是一个 8 位组，接下来是三个 4 位组，最后是一个 12 位组。总共的 32 位（十六进制位）表示了 128 个二进制位，这是 UUID 类型的标准形式。

瀚高数据库也接受另一种输入形式：使用大写位、标准格式被花括号包围、忽略某些或者全部连字符、在任意 4 位组后面增加一个连字符。

| 格式 | 示例 |
| --- | --- |
| 标准形式 | a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11 |
| 非标准形式 | A0EEBC99-9C0B-4EF8-BB6D-6BB9BD380A11   {a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11}   a0eebc999c0b4ef8bb6d6bb9bd380a11   a0ee-bc99-9c0b-4ef8-bb6d-6bb9-bd38-0a11   {a0eebc99-9c0b4ef8-bb6d6bb9-bd380a11} |

### XML类型

xml 数据类型可以被用来存储 XML 数据。它比直接在一个 text 域中存储 XML 数据的优势在于，它会检查输入值的结构是否良好，并且有支持函数用于在其上执行类型安全的操作。

创建xml值：

要从字符数据中生成一个 xml 类型的值，可以使用函数 xmlparse。

```sql
XMLPARSE({DOCUMENT|CONTENT}value)
```

例如：

```sql
XMLPARSE (DOCUMENT '<?xml version="1.0"?><book><title>Manual</ 
title><chapter>...</chapter></book>') 
XMLPARSE (CONTENT 'abc<foo>bar</foo><bar>foo</bar>')
```

然而根据 SQL 标准这是唯一将字符串转换为 XML 值的方法，HGDB 还有特有的语法：

```sql
xml'<foo>bar</foo>'
'<foo>bar</foo>'::xml
```

从 xml 产生一个字符串的逆操作可以使用函数 xmlserialize:

```sql
XMLSERIALIZE ( { DUCUMENT | CONTENT } value AS type )
```

type 可以是 character、character varying 或 text（或者其中之一的一个别名）。

### JSON类型

JSON 数据类型是用来存储 JSON（JavaScript Object Notation）数据的。这种数据也可以被存储为 text，但是 JSON 数据类型的优势在于能强制要求每个被存储的值符合 JSON 规则，也有很多 JSON 相关的函数和操作符可以用于存储在这些数据类型中的数据。

HGDB 提供存储 JSON 数据的两种类型：json 和 jsonb。json 和 jsonb 数据类型接受几乎完全相同的值集合作为输入，主要的实际区别之一是效率。json 数据类型存储输入文本的精准拷贝，执行时需重新解析数据。jsonb 数据被存储在一种分解好的二进制格式中，输入慢，处理快，因为输入时需要做附加的转换，而在处理时不需要解析，jsonb 也支持索引，这也是一个令人瞩目的优势。除非特别需要，大多数应用应该更愿意把 JSON 数据存储为 jsonb。

JSON 输出简单标量和数组如下所示：

```sql
SELECT '5'::json;
SELECT '[1,2,"foo",null]'::json;
```

### 组合类型

一个组合类型表示一行或一个记录的结构，它本质上就是一个域名和它们数据类型的列表。HGDB 允许把组合类型用在很多能用简单类型的地方。例如，一个表的一列可以被声明为一种组合类型。

#### 组合类型的定义

创建一个组合类型通过 `CREATE TYPE` 来完成，例如创建一个 complex 组合类型。

```sql
CREATE TYPE complex AS ( 
    r double precision, 
    i double precision 
);
```

该语法堪比 `CREATE TABLE` ，不过只能指定域名和类型，不能包括约束，注意 `AS` 关键字这里不能省略。

下面用创建的组合类型来创建表：

```sql
CREATE TABLE complex_(co complex);
INSERT INTO complex_ VALUES ('(3.1415926,2.71828)');
```

#### 组合类型的输入

要把一个组合值写作一个文字常量，将该域值封闭在圆括号中并且用逗号分隔他们。可以在任何域值周围放上双引号，并且如果该值域包含逗号或圆括号则必须这样做。

一个组合常量的一般格式如下：

```sql
'(val1,val2,...)'
```

例如 inventory\_item 复合类型的一个合法值是这样的：

```sql
CREATE TYPE inventory_item AS ( 
    name text, 
    supplier_id integer, 
    price numeric 
);

'("fuzzy dice",42,1.99)'
```

#### 访问组合类型

要访问一个组合列的一个域，可以写成一个点和域的名称，为避免被认为是从一个表中选择一个域，因此需要用圆括号将组合列括起来。

假设用上面创建的 iventory\_item 复合类型在表 on\_hand 中创建了一个名为 item 的属性，可以写一个这样的查询语句：

```sql
SELECT (item).name FROM on_hand WHERE (item).price>9.99;
```

也可以将表名也表示到圆括号里面：

```sql
SELECT (on_hand.item).name FROM on_hand WHERE (on_hand.item).price>9.99;
```

### 范围类型

范围类型是表达某种元素类型（称为范围的 subtype）的一个值的范围的数据类型。例如，timestamp 的范围可以被用来表达一个会议室被保留的时间范围，在这种情况下，数据类型是 tsrange（“timestamp range”的简写）而 timestamp 是 subtype。

HGDB 中带有以下内建范围类型：

• int4range — integer 的范围

• int8range — bigint 的范围

• numrange — numeric 的范围

• tsrange — 不带时区的 timestamp 的范围

• tstzrange — 带时区的 timestamp 的范围

• daterange — date 的范围

也可以通过 `CREATE TYPE` 来定义自己的范围类型。

范围类型的使用可以通过下面的例子来实现：

```sql
CREATE TABLE reservation (room int, during tsrange);
INSERT INTO reservation VALUES (1108,'[2010-01-01 14:30,2010-01-01 15:30]');

--包含
SELECT int4range(10,20)@>3;
--重叠
SELECT numrange(11.1,22.2)&&numrange(20.0,30.0);
--抽取上届
SELECT upper(int8range(15,25));
--计算交集
SELECT int4range(10,20)*int4range(15,25);
--范围为空吗？
SELECT isempty(numrange(1,5));
```

一个范围值的输入必须遵循下列模式之一：

- (lower-bound,upper-bound)
- (lower-bound,upper-bound\]
- \[lower-bound,upper-bound)
- \[lower-bound,upper-bound\]
- empty

圆括号或方括号指示上下界是否为排除的或者包含的，圆括号 ’()‘ 为不包含，方括号 ‘\[\]’ 为包含。注意最后一个模式是 empty，它表示一个空范围（一个不包含点的范围）。

lower-bound 可以是作为 subtype 的合法输入的一个字符串，或者是空表示没有下界。同样，upper-bound 可以是作为 subtype 的合法输入的一个字符串，或者是空表示没有上界。一个范围的下界被忽略意味着所有小于上界的值都被包括在范围中，例如(,3\]。 同样，如果范围的上界被忽略，那么所有比上界大的值都被包括在范围中。如果上下界都被忽略，该元素类型的所有值都被认为在该范围中。

### 域类型

域是一种用户定义的数据类型，它基于另一种底层类型。根据需要，它可以有约束来限制其有效值为底层类型所允许值的一个子集。如果没有约束，它的行为就和底层类型一样——例如，任何适用于底层类型的操作符或函数都对该域类型有效。底层类型可以是任何内建或者用户定义的基础类型、枚举类型、数组类型、组合类型、范围类型或者另一个域。

例如，我们可以在整数之上创建一个域，它只接受正整数：

```sql
CREATE DOMAIN posint AS integer CHECK(VALUE>0);
CREATE TABLE mytable(id posint);
INSERT INTO mytable VALUES(1);
INSERT INTO mytable VALUES(-1);
```

如此第一条数据插入成功，第二条数据插入失败。

当底层类型的一个操作符或函数适用于一个域值时，域会被自动向下造型为底层类型。因此， `mytable.id - 1` 的结果会被认为是类型 integer 而不是 posint。

### 对象标识符类型

对象标识符（OID）被 HGDB 用来在内部作为多个系统表的主键。 类型 oid 表示一个对象标识符。 也有多个 oid 的别名类型：regproc，regprocedure，regoper，regoperator，regclass，regtype，regrole，regnamespace，regconfig 和 regdictionary。

| 名字 | 引用 | 描述 | 值示例 |
| --- | --- | --- | --- |
| oid | 任意 | 数字形式的对象标识符 | 564182 |
| regproc | pg\_proc | 函数名字 | sum |
| regprocedure | pg\_proc | 带参数类型的函数 | sum(int4) |
| regoper | pg\_operator | 操作符名字 | + |
| regoperator | pg\_operator | 带参数类型的操作符 | \*(integer,integer) or -(NONE,integer) |
| regclass | pg\_class | 关系名字 | pg\_type |
| regtype | pg\_type | 数据类型名字 | integer |
| regrole | pg\_authid | 角色名 | smithee |
| regnamespace | pg\_namespace | 名字空间名称 | pg\_catalog |
| regconfig | pg\_ts\_config | 文本搜索配置 | english |
| regdictionary | pg\_ts\_dict | 文本搜索字典 | simple |

### pg\_lsn类型

pg\_lsn 数据类型可以被用来存储 LSN（日志序列号）数据，LSN 是一个指向 WAL 中的位置的指针。这个类型是 XLogRecPtr 的一种表达并且是 HGDB 的一种内部系统类型。

在内部，一个 LSN 是一个 64 位整数，表示在预写式日志流中的一个字节位置。它被打印成两个最高 8 位的十六进制数，中间用斜线分隔，例如 16/B374D848。pg\_lsn 类型支持标准的比较操作符，如 = 和 >。两个 LSN 可以用 - 操作符做减法， 结果将是分隔两个预写式日志位置的字节数。

### 伪类型

HGDB 类型系统包含了一些特殊目的的项，它们被统称为伪类型。一个伪类型不能被用作一个列的数据类型，但是它可以被用来定义一个函数的参数或者结果类型。每一种可用的伪类型都有其可以发挥作用的情况，这些情况的特点是一个函数的行为并不能符合于简单使用或者返回一种特定 SQL 数据类型的值。下表列出了现有的伪类型。

| 名字 | 描述 |
| --- | --- |
| any | 表示一个函数可以接受任意输入数据类型 |
| anyelement | 表示一个函数可以接受任意数据类型 |
| anyarray | 表示一个函数可以接受任意数组数据类型 |
| anynonarray | 表示一个函数可以接受任意非数组数据类型 |
| anyenum | 表示一个函数可以接受任意枚举数据类型 |
| anyrange | 表示一个函数可以接受任意范围数据类型 |
| cstring | 表示一个函数接受或者返回一个非空结尾的C字符 |
| internal | 表示一个函数接受或返回一个服务器内部数据类型 |
| language\_handler | 一个被声明为返回 language\_handler 的过程语言调用处理器 |
| fdw\_handler | 一个被声明为返回 fdw\_handler 的外部数据包装器处理器 |
| index\_am\_handler | 一个被声明为返回 index\_am\_handler 索引访问方法处理器 |
| tsm\_handler | 一个被声明为返回 tsm\_handler 的表采样方法处理器 |
| record | 表示一个接受或者返回一个为未指定的行类型的函数 |
| trigger | 一个被声明为返回 trigger 的触发器函数 |
| event\_trigger | 一个被声明为返回 event\_trigger 的事件触发器函数 |
| pg\_ddl\_command | 表示一种对事件触发器可用的 DDL 命令的表达 |
| void | 表示一个函数不返回值 |
| unknown | 表示一种还未被解析的类型，例如一个未修饰的字符文本 |
| opaque | 一种已被废弃的类型名称，以前它用于实现以上的很多种目的 |
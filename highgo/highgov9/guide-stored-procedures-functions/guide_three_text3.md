---
title: "函数定义"
book: "存储过程&函数"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_three_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-stored-procedures-functions
---

## 函数定义

PL/pgSQL 是一种可载入的过程语言，可以被用来创建函数和触发器过程等，如果数据库内置函数无法满足需求，可以通过 PL/pgSQL 来定义新的函数，本节将介绍如何通过 `CREATE FUNCTION` 来创建自定义函数。

自定义函数的语法如下：

```sql
CREATE [ OR REPLACE ] FUNCTION funcname([IN parameters,OUT parameters]) RETURNS return_value_type AS
$body$
DECLARE
    declaration;
BEGIN
    statement   --逻辑块（pl/pgsql代码块）
    [ RETURN return_value;]
END;
$body$
LANGUAGE plpgsql;
```

funcname 是函数名，IN / OUT表示输入/输出参数，可以有多个输入/输出参数，参数由参数名+数据类型组成，如 v\_id int。return\_value\_type 返回值类型，无返回值使用 void。DECLARE 定义变量列表，declaration 为函数变量列表，变量写成变量名+类型的格式。$body$ 表示里面引用的内容的函数逻辑块，return\_value 表示返回值变量，LANGUAGE 指定编程语言，如 plpgsql。

函数参数中使用 OUT 标明返回参数，return\_value\_type 为 void 时，函数逻辑块中不需要使用 RETURN 进行值返回，如果没有使用 OUT 且 return\_value\_type 不为 void 时，必须在逻辑块中使用 RETURN 表明返回值，无返回值可写成 RETURN NULL。OUT 指定的返回值类型或者 RETURN指定的返回值类型必须与 RETURNS 后指定的类型一致。

如果不需要接收执行结果，需使用 PERFORM 替换 SELECT（BEGIN里面）。否则有执行结果返回会报错。

例如创建一个 p\_function 的函数，返回参数相对应的 p\_name 的值：

```sql
CREATE OR REPLACE FUNCTION p_func(in p_no int)
RETURNS varchar AS  --定义返回的结果类型为varchar类型
$$
DECLARE
    p_name varchar;  --定义结果变量
BEGIN 
    SELECT name INTO p_name FROM products WHERE product_no=p_no;
    RETURN p_name;
END
$$
LANGUAGE plpgsql;
```

函数调用：

```sql
highgo=# SELECT p_func(1);
 p_func 
--------
 a
(1 行记录)
```
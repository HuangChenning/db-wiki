---
title: EXCEPTION
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle25.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## EXCEPTION

## 说明

在PL/SQL中，异常处理是控制程序运行中错误的一种重要机制。异常可以分为两大类：预定义异常和用户自定义异常。

例如：

NO\_DATA\_FOUND：在查询中没有找到任何数据时引发。

TOO\_MANY\_ROWS：在查询中返回了多于一条的结果行时引发。

ZERO\_DIVIDE：试图用零进行除法时引发。

这些异常为预定义异常，可以在程序中直接使用，而无需显式声明。

用户自定义异常允许开发者根据特定的需求定义新的异常。例如可以根据业务逻辑错误定义一个异常，以便在遇到特定条件时提供清晰的错误信息。

在PL/SQL中，也可以将用户自定义异常与Oracle内部预定义异常关联起来，给预定义异常一个新的名字。通过这种方式可以在程序中使用更具描述性或更符合您业务逻辑的名称来处理这些异常。

在处理异常时，EXCEPTION块捕获异常并执行相应的处理程序。处理程序可以是默认的异常处理或者是用户自定义异常处理。

通过合理使用预定义异常、用户自定义异常和异常关联，我们可以构建出更加健壮和易于维护的PL/SQL程序，提高了对错误的处理能力，使得程序在面对异常情况时能够优雅地应对。

## 示例

DECLARE

\-- 声明一个变量来保存可能的错误代码

err\_code NUMBER;

err\_msg VARCHAR2(4000);

result int;

BEGIN

\-- 这里可以放置你的PL/SQL逻辑

\-- 示例可能会产生异常的操作，例如除以零

\-- 这可以被替换为实际的逻辑

result:= 1/0;

EXCEPTION

WHEN OTHERS THEN

\-- 捕获异常

err\_code:= SQLCODE;

err\_msg:= SQLERRM;

\-- 打印异常码和异常消息

raise notice ‘错误代码: %’, err\_code;

raise notice ‘错误消息: %’, err\_msg;

END;

/
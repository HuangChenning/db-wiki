---
title: ORA_DST_ERROR
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions123.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''ora\_dst\_error.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/ora_dst_error.htm)  
  

Purpose

`ORA_DST_ERROR` is useful when you are changing the time zone data file for your database. The function takes as an argument a datetime expression that resolves to a `TIMESTAMP` `WITH` `TIME` `ZONE` value or a `VARRAY` object that contains `TIMESTAMP` `WITH` `TIME` `ZONE` values, and indicates whether the datetime value will result in an error with the new time zone data. The return values are:

- `0`: the datetime value does not result in an error with the new time zone data.
- `1878`: the datetime value results in a "nonexisting time" error.
- `1883`: the datetime value results in a "duplicate time" error.

This function can be issued only when changing the time zone data file of the database and upgrading the timestamp with the time zone data, and only between the execution of the `DBMS_DST`.`BEGIN_PREPARE` and the `DBMS_DST`.`END_PREPARE` procedures or between the execution of the `DBMS_DST`.`BEGIN_UPGRADE` and the `DBMS_DST`.`END_UPGRADE` procedures.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG259) for more information on time zone datafiles and on how Oracle Database handles daylight saving time, and [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_dst.htm#ARPLS234) for information on the `DBMS_DST` package
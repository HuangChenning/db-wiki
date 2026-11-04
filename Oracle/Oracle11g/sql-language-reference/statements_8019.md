---
title: DROP JAVA
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8019.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `JAVA` statement to drop a Java source, class, or resource schema object.

See Also:

- [CREATE JAVA](statements_5014.md) for information on creating Java objects
- [Oracle Database Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10588/toc.htm) for more information on resolving Java sources, classes, and resources

Prerequisites

The Java source, class, or resource must be in your own schema or you must have the `DROP` `ANY` `PROCEDURE` system privilege. You also must have the `EXECUTE` object privilege on Java classes to use this command.

Syntax

drop\_java::=

![drop_java](img/drop_java.gif)

> ```
> DROP JAVA { SOURCE | CLASS | RESOURCE }
>   [ schema. ] object_name ;
> ```
  

Semantics

JAVA SOURCE

Specify `SOURCE` to drop a Java source schema object and all Java class schema objects derived from it.

JAVA CLASS

Specify `CLASS` to drop a Java class schema object.

JAVA RESOURCE

Specify `RESOURCE` to drop a Java resource schema object.

object\_name

Specify the name of an existing Java class, source, or resource schema object. Enclose the `object_name` in double quotation marks to preserve lower- or mixed-case names.

Examples

Dropping a Java Class Object: Example The following statement drops the Java class `Agent`, created in ["Creating a Java Class Object: Example"](statements_5014.md):

```
DROP JAVA CLASS "Agent";
```
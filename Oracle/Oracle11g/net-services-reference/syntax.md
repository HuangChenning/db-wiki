---
title: Syntax Rules for Configuration Files
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/syntax.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 3 Syntax Rules for Configuration Files

This chapter describes the syntax rules for Oracle Net Services configuration files.

This chapter contains the following topics:

## Configuration File Syntax Overview

The Oracle Net Services configuration files consist of parameters which include keyword-value pairs. Keyword-value pairs are surrounded by parentheses:

```
parameter=(keyword=value)
```

Some keywords have other keyword-value pairs as their values:

```
(keyword=
    (keyword=value)
    (keyword=value))
```

For example, the address portion of a local naming configuration file (`tnsnames.ora`) might include the following lines:

```
(ADDRESS=
   (PROTOCOL=tcp)
   (HOST=sales-server)
   (PORT=1521))
```

Set up configuration files so that indentation reflects what keyword is the parent or owner of other keyword-value pairs. If you do not choose to indent your files in this way, you must still indent a wrapped line by at least one space, or it will be misread as a new parameter. The following syntax is acceptable:

```
(ADDRESS=(PROTOCOL=tcp)
  (HOST=sales-server)(PORT=1521))
```

The following syntax is not acceptable:

```
(ADDRESS=(PROTOCOL=tcp)
(HOST=sales-server)(PORT=1521))
```

## Syntax Rules for Configuration Files

The following rules apply to the syntax of configuration files:

- Any keyword in a configuration file that begins a parameter that includes one or more keyword-value pairs must be in the far left column of a line. If it is indented by one or more spaces, then it is interpreted as a continuation of the previous line.
- All characters must belong to the network character set.
- Keywords are not case sensitive. However, values may be case sensitive, depending on the operating system and protocol.
- Spaces around the equal sign (=) are optional in keyword-value pairs.
- There is a hierarchy of keywords such that some keywords are always followed by others. At any level of the hierarchy, keywords can be listed in any order. For example, the following entries are equally valid:
	```
	(ADDRESS=
	   (PROTOCOL=TCP)
	   (HOST=sales-server)
	   (PORT=1521))
	(ADDRESS=
	   (PROTOCOL=tcp)
	   (PORT=1521)
	   (HOST=sales-server))
	```
- Keywords cannot contain spaces.
- Values must not contain spaces unless enclosed within double quotation marks (`"`) or single quotation marks (`'`).
- If the keyword-value pair consists of a single word or a concatenation of words on either side of the equal sign, then no parentheses are needed.
- The maximum length of a connect descriptor is 4 KB
- Comments can be included using the number sign (#) at the beginning of a line. Anything following the number sign to the end of the line is considered a comment.

## Network Character Set for Keywords

The network character set for keyword values consists of the following characters. Connect descriptors must be made up of single-byte characters.

```
A-Z, a-z
0-9
( ) < > / \
, . : ; ' "=- _
$ + * # & ! % ? @
```

Within this character set, the following symbols are reserved:

```
( ) = \ " ' #
```

Reserved symbols are used as delimiters, not as part of a keyword or a value unless the keyword or value has quotation marks. Either single or double quotation marks can be used to enclose a value containing reserved symbols. To include a quotation marks within a value that is surrounded by quotation marks, use different quotation marks. The backslash (`\`) is used as an escape character.

The following characters may be used within a connect descriptor, but not in a keyword or value:

- Space
- Tab
- Carriage return
- Newline

## Character Set for Listener and Net Service Names

The listener name and net service name are limited to the following character set:

```
[a...z] [A...Z] [0...9] _
```

The first character must be an alphanumeric character. In general, up to 64 characters is acceptable. A database service name must match the global database name defined by the database administrator, which consists of a database name, and the database domain. Net service names and global database names are not case sensitive.
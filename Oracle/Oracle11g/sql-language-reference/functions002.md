---
title: Single-Row Functions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions002.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Single-row functions return a single result row for every row of a queried table or view. These functions can appear in select lists, `WHERE` clauses, `START` `WITH` and `CONNECT` `BY` clauses, and `HAVING` clauses.

## Numeric Functions

Numeric functions accept numeric input and return numeric values. Most numeric functions return `NUMBER` values that are accurate to 38 decimal digits. The transcendental functions `COS`, `COSH`, `EXP`, `LN`, `LOG`, `SIN`, `SINH`, `SQRT`, `TAN`, and `TANH` are accurate to 36 decimal digits. The transcendental functions `ACOS`, `ASIN`, `ATAN`, and `ATAN2` are accurate to 30 decimal digits. The numeric functions are:

  
[ABS](functions009.md)  
[ACOS](functions010.md)  
[ASIN](functions015.md)  
[ATAN](functions016.md)  
[ATAN2](functions017.md)  
[BITAND](functions021.md)  
[CEIL](functions024.md)  
[COS](functions037.md)  
[COSH](functions038.md)  
[EXP](functions058.md)  
[FLOOR](functions067.md)  
[LN](functions090.md)  
[LOG](functions093.md)  
[MOD](functions101.md)  
[NANVL](functions103.md)  
[POWER](functions129.md)  
[REMAINDER](functions152.md)  
[ROUND (number)](functions155.md)  
[SIGN](functions164.md)  
[SIN](functions165.md)  
[SINH](functions166.md)  
[SQRT](functions168.md)  
[TAN](functions193.md)  
[TANH](functions194.md)  
[TRUNC (number)](functions221.md)  
[WIDTH\_BUCKET](functions234.md)

## Character Functions Returning Character Values

Character functions that return character values return values of the following data types unless otherwise documented:

- If the input argument is `CHAR` or `VARCHAR2`, then the value returned is `VARCHAR2`.
- If the input argument is `NCHAR` or `NVARCHAR2`, then the value returned is `NVARCHAR2`.

The length of the value returned by the function is limited by the maximum length of the data type returned.

- For functions that return `CHAR` or `VARCHAR2`, if the length of the return value exceeds the limit, then Oracle Database truncates it and returns the result without an error message.
- For functions that return `CLOB` values, if the length of the return values exceeds the limit, then Oracle raises an error and returns no data.

The character functions that return character values are:

  
[CHR](functions026.md)  
[CONCAT](functions033.md)  
[INITCAP](functions074.md)  
[LOWER](functions094.md)  
[LPAD](functions095.md)  
[LTRIM](functions096.md)  
[NCHR](functions104.md)  
[NLS\_INITCAP](functions110.md)  
[NLS\_LOWER](functions111.md)  
[NLS\_UPPER](functions112.md)  
[NLSSORT](functions113.md)  
[REGEXP\_REPLACE](functions149.md)  
[REGEXP\_SUBSTR](functions150.md)  
[REPLACE](functions153.md)  
[RPAD](functions159.md)  
[RTRIM](functions160.md)  
[SOUNDEX](functions167.md)  
[SUBSTR](functions181.md)  
[TRANSLATE](functions216.md)  
[TRANSLATE... USING](functions217.md)  
[TRIM](functions219.md)  
[UPPER](functions226.md)

## Character Functions Returning Number Values

Character functions that return number values can take as their argument any character data type. The character functions that return number values are:

  
[ASCII](functions013.md)  
[INSTR](functions080.md)  
[LENGTH](functions088.md)  
[REGEXP\_COUNT](functions147.md)  
[REGEXP\_INSTR](functions148.md)

## Character Set Functions

The character set functions return information about the character set. The character set functions are:

  
[NLS\_CHARSET\_DECL\_LEN](functions107.md)  
[NLS\_CHARSET\_ID](functions108.md)  
[NLS\_CHARSET\_NAME](functions109.md)

## Datetime Functions

Datetime functions operate on date (`DATE`), timestamp (`TIMESTAMP`, `TIMESTAMP` `WITH` `TIME` `ZONE`, and `TIMESTAMP` `WITH` `LOCAL` `TIME` `ZONE`), and interval (`INTERVAL` `DAY` `TO` `SECOND`, `INTERVAL` `YEAR` `TO` `MONTH`) values.

Some of the datetime functions were designed for the Oracle `DATE` data type (`ADD_MONTHS`, `CURRENT_DATE`, `LAST_DAY`, `NEW_TIME`, and `NEXT_DAY`). If you provide a timestamp value as their argument, then Oracle Database internally converts the input type to a `DATE` value and returns a `DATE` value. The exceptions are the `MONTHS_BETWEEN` function, which returns a number, and the `ROUND` and `TRUNC` functions, which do not accept timestamp or interval values at all.

The remaining datetime functions were designed to accept any of the three types of data (date, timestamp, and interval) and to return a value of one of these types.

All of the datetime functions that return current system datetime information, such as `SYSDATE`, `SYSTIMESTAMP`, `CURRENT_TIMESTAMP`, and so forth, are evaluated once for each SQL statement, regardless how many times they are referenced in that statement.

The datetime functions are:

  
[ADD\_MONTHS](functions011.md)  
[CURRENT\_DATE](functions044.md)  
[CURRENT\_TIMESTAMP](functions045.md)  
[DBTIMEZONE](functions048.md)  
[EXTRACT (datetime)](functions059.md)  
[FROM\_TZ](functions068.md)  
[LAST\_DAY](functions084.md)  
[LOCALTIMESTAMP](functions092.md)  
[MONTHS\_BETWEEN](functions102.md)  
[NEW\_TIME](functions105.md)  
[NEXT\_DAY](functions106.md)  
[NUMTODSINTERVAL](functions117.md)  
[NUMTOYMINTERVAL](functions118.md)  
[ORA\_DST\_AFFECTED](functions121.md)  
[ORA\_DST\_CONVERT](functions122.md)  
[ORA\_DST\_ERROR](functions123.md)  
[ROUND (date)](functions154.md)  
[SESSIONTIMEZONE](functions162.md)  
[SYS\_EXTRACT\_UTC](functions186.md)  
[SYSDATE](functions191.md)  
[SYSTIMESTAMP](functions192.md)  
[TO\_CHAR (datetime)](functions200.md)  
[TO\_DSINTERVAL](functions204.md)  
[TO\_TIMESTAMP](functions213.md)  
[TO\_TIMESTAMP\_TZ](functions214.md)  
[TO\_YMINTERVAL](functions215.md)  
[TRUNC (date)](functions220.md)  
[TZ\_OFFSET](functions222.md)

## General Comparison Functions

The general comparison functions determine the greatest and or least value from a set of values. The general comparison functions are:

  
[GREATEST](functions069.md)  
[LEAST](functions087.md)

## Conversion Functions

Conversion functions convert a value from one data type to another. Generally, the form of the function names follows the convention `datatype` `TO` `datatype`. The first data type is the input data type. The second data type is the output data type. The SQL conversion functions are:

  
[ASCIISTR](functions014.md)  
[BIN\_TO\_NUM](functions020.md)  
[CAST](functions023.md)  
[CHARTOROWID](functions025.md)  
[COMPOSE](functions032.md)  
[CONVERT](functions034.md)  
[DECOMPOSE](functions050.md)  
[HEXTORAW](functions073.md)  
[NUMTODSINTERVAL](functions117.md)  
[NUMTOYMINTERVAL](functions118.md)  
[RAWTOHEX](functions143.md)  
[RAWTONHEX](functions144.md)  
[ROWIDTOCHAR](functions157.md)  
[ROWIDTONCHAR](functions158.md)  
[SCN\_TO\_TIMESTAMP](functions161.md)  
[TIMESTAMP\_TO\_SCN](functions195.md)  
[TO\_BINARY\_DOUBLE](functions196.md)  
[TO\_BINARY\_FLOAT](functions197.md)  
[TO\_BLOB](functions198.md)  
[TO\_CHAR (character)](functions199.md)  
[TO\_CHAR (datetime)](functions200.md)  
[TO\_CHAR (number)](functions201.md)  
[TO\_CLOB](functions202.md)  
[TO\_DATE](functions203.md)  
[TO\_DSINTERVAL](functions204.md)  
[TO\_LOB](functions205.md)  
[TO\_MULTI\_BYTE](functions206.md)  
[TO\_NCHAR (character)](functions207.md)  
[TO\_NCHAR (datetime)](functions208.md)  
[TO\_NCHAR (number)](functions209.md)  
[TO\_NCLOB](functions210.md)  
[TO\_NUMBER](functions211.md)  
[TO\_SINGLE\_BYTE](functions212.md)  
[TO\_TIMESTAMP](functions213.md)  
[TO\_TIMESTAMP\_TZ](functions214.md)  
[TO\_YMINTERVAL](functions215.md)  
[TREAT](functions218.md)  
[UNISTR](functions224.md)

## Large Object Functions

The large object functions operate on LOBs. The large object functions are:

  
[BFILENAME](functions019.md)  
[EMPTY\_BLOB, EMPTY\_CLOB](functions056.md)

## Collection Functions

The collection functions operate on nested tables and varrays. The SQL collection functions are:

  
[CARDINALITY](functions022.md)  
[COLLECT](functions031.md)  
[POWERMULTISET](functions130.md)  
[POWERMULTISET\_BY\_CARDINALITY](functions131.md)  
[SET](functions163.md)

## Hierarchical Functions

Hierarchical functions applies hierarchical path information to a result set. The hierarchical function is:

  
[SYS\_CONNECT\_BY\_PATH](functions183.md)

## Data Mining Functions

The data mining functions operate on models that have been built using the `DBMS_DATA_MINING` package or the Oracle Data Mining Java API. The SQL data mining functions are:

  
[CLUSTER\_ID](functions027.md)  
[CLUSTER\_PROBABILITY](functions028.md)  
[CLUSTER\_SET](functions029.md)  
[FEATURE\_ID](functions062.md)  
[FEATURE\_SET](functions063.md)  
[FEATURE\_VALUE](functions064.md)  
[PREDICTION](functions132.md)  
[PREDICTION\_BOUNDS](functions133.md)  
[PREDICTION\_COST](functions134.md)  
[PREDICTION\_DETAILS](functions135.md)  
[PREDICTION\_PROBABILITY](functions136.md)  
[PREDICTION\_SET](functions137.md)

See Also:

[Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_deploying.htm#DMPRG004) for information on SQL data mining functions

## XML Functions

The XML functions operate on or return XML documents or fragments. These functions use arguments that are not defined as part of the ANSI/ISO/IEC SQL Standard but are defined as part of the World Wide Web Consortium (W3C) standards. The processing and operations that the functions perform are defined by the relevant W3C standards. The table below provides a link to the appropriate section of the W3C standard for the rules and guidelines that apply to each of these XML-related arguments. A SQL statement that uses one of these XML functions, where any of the arguments does not conform to the relevant W3C syntax, will result in an error. Of special note is the fact that not every character that is allowed in the value of a database column is considered legal in XML.

| Syntax Element | W3C Standard URL |
| --- | --- |
| `value_expr` | `http://www.w3.org/TR/2006/REC-xml-20060816` |
| `Xpath_string` | `http://www.w3.org/TR/1999/REC-xpath-19991116` |
| `XQuery_string` | `http://www.w3.org/TR/2007/REC-xquery-semantics-20070123/` |
| `namespace_string` | `http://www.w3.org/TR/2006/REC-xml-names-20060816/` |
| `identifier` | `http://www.w3.org/TR/2006/REC-xml-20060816/#NT-Nmtoken` |

For more information about selecting and querying XML data using these functions, including information on formatting output, refer to [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb04cre.htm#ADXDB0400).

The SQL XML functions are:

  
[APPENDCHILDXML](functions012.md)  
[DELETEXML](functions051.md)  
[DEPTH](functions053.md)  
[EXISTSNODE](functions057.md)  
[EXTRACT (XML)](functions060.md)  
[EXTRACTVALUE](functions061.md)  
[INSERTCHILDXML](functions075.md)  
[INSERTCHILDXMLAFTER](functions076.md)  
[INSERTCHILDXMLBEFORE](functions077.md)  
[INSERTXMLAFTER](functions078.md)  
[INSERTXMLBEFORE](functions079.md)  
[PATH](functions125.md)  
[SYS\_DBURIGEN](functions185.md)  
[SYS\_XMLAGG](functions189.md)  
[SYS\_XMLGEN](functions190.md)  
[UPDATEXML](functions225.md)  
[XMLAGG](functions235.md)  
[XMLCAST](functions236.md)  
[XMLCDATA](functions237.md)  
[XMLCOLATTVAL](functions238.md)  
[XMLCOMMENT](functions239.md)  
[XMLCONCAT](functions240.md)  
[XMLDIFF](functions241.md)  
[XMLELEMENT](functions242.md)  
[XMLEXISTS](functions243.md)  
[XMLFOREST](functions244.md)  
[XMLISVALID](functions245.md)  
[XMLPARSE](functions246.md)  
[XMLPATCH](functions247.md)  
[XMLPI](functions248.md)  
[XMLQUERY](functions249.md)  
[XMLROOT](functions250.md)  
[XMLSEQUENCE](functions251.md)  
[XMLSERIALIZE](functions252.md)  
[XMLTABLE](functions253.md)  
[XMLTRANSFORM](functions254.md)

## Encoding and Decoding Functions

The encoding and decoding functions let you inspect and decode data in the database. The encoding and decoding functions are:

  
[DECODE](functions049.md)  
[DUMP](functions055.md)  
[ORA\_HASH](functions124.md)  
[VSIZE](functions233.md)

## Environment and Identifier Functions

The environment and identifier functions provide information about the instance and session. The environment and identifier functions are:

  
[SYS\_CONTEXT](functions184.md)  
[SYS\_GUID](functions187.md)  
[SYS\_TYPEID](functions188.md)  
[UID](functions223.md)  
[USER](functions227.md)  
[USERENV](functions228.md)
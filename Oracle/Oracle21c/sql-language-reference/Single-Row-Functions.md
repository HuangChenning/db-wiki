---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Single-Row-Functions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## Single-Row Functions

Single-row functions return a single result row for every row of a queried table or view. These functions can appear in select lists, `WHERE` clauses, `START` `WITH` and `CONNECT` `BY` clauses, and `HAVING` clauses.

### Numeric Functions

Numeric functions accept numeric input and return numeric values. Most numeric functions return `NUMBER` values that are accurate to 38 decimal digits. The transcendental functions `COS`, `COSH`, `EXP`, `LN`, `LOG`, `SIN`, `SINH`, `SQRT`, `TAN`, and `TANH` are accurate to 36 decimal digits. The transcendental functions `ACOS`, `ASIN`, `ATAN`, and `ATAN2` are accurate to 30 decimal digits. The numeric functions are:

- [ABS](ABS.md)
- [ACOS](ACOS.md)
- [ASIN](ASIN.md)
- [ATAN](ATAN.md)
- [ATAN2](ATAN2.md)
- [BITAND](BITAND.md)
- [CEIL](CEIL.md)
- [COS](COS.md)
- [COSH](COSH.md)
- [EXP](EXP.md)
- [FLOOR](FLOOR.md)
- [LN](LN.md)
- [LOG](LOG.md)
- [MOD](MOD.md)
- [NANVL](NANVL.md)
- [POWER](POWER.md)
- [REMAINDER](REMAINDER.md)
- [ROUND (number)](ROUND-number.md)
- [SIGN](SIGN.md)
- [SIN](SIN.md)
- [SINH](SINH.md)
- [SQRT](SQRT.md)
- [TAN](TAN.md)
- [TANH](TANH.md)
- [TRUNC (number)](TRUNC-number.md)
- [WIDTH\_BUCKET](WIDTH_BUCKET.md)

### Character Functions Returning Character Values

Character functions that return character values return values of the following data types unless otherwise documented:

- If the input argument is `CHAR` or `VARCHAR2`, then the value returned is `VARCHAR2`.
- If the input argument is `NCHAR` or `NVARCHAR2`, then the value returned is `NVARCHAR2`.

The length of the value returned by the function is limited by the maximum length of the data type returned.

- For functions that return `CHAR` or `VARCHAR2`, if the length of the return value exceeds the limit, then Oracle Database truncates it and returns the result without an error message.
- For functions that return `CLOB` values, if the length of the return values exceeds the limit, then Oracle raises an error and returns no data.

The character functions that return character values are:

- [CHR](CHR.md)
- [CONCAT](CONCAT.md)
- [INITCAP](INITCAP.md)
- [LOWER](LOWER.md)
- [LPAD](LPAD.md)
- [LTRIM](LTRIM.md)
- [NCHR](NCHR.md)
- [NLS\_INITCAP](NLS_INITCAP.md)
- [NLS\_LOWER](NLS_LOWER.md)
- [NLS\_UPPER](NLS_UPPER.md)
- [NLSSORT](NLSSORT.md)
- [REGEXP\_REPLACE](REGEXP_REPLACE.md)
- [REGEXP\_SUBSTR](REGEXP_SUBSTR.md)
- [REPLACE](REPLACE.md)
- [RPAD](RPAD.md)
- [RTRIM](RTRIM.md)
- [SOUNDEX](SOUNDEX.md)
- [SUBSTR](SUBSTR.md)
- [TRANSLATE](TRANSLATE.md)
- [TRANSLATE... USING](TRANSLATE-USING.md)
- [TRIM](TRIM.md)
- [UPPER](UPPER.md)

### Character Functions Returning Number Values

### Datetime Functions

Datetime functions operate on date (`DATE`), timestamp (`TIMESTAMP`, `TIMESTAMP` `WITH` `TIME` `ZONE`, and `TIMESTAMP` `WITH` `LOCAL` `TIME` `ZONE`), and interval (`INTERVAL` `DAY` `TO` `SECOND`, `INTERVAL` `YEAR` `TO` `MONTH`) values.

Some of the datetime functions were designed for the Oracle `DATE` data type (`ADD_MONTHS`, `CURRENT_DATE`, `LAST_DAY`, `NEW_TIME`, and `NEXT_DAY`). If you provide a timestamp value as their argument, then Oracle Database internally converts the input type to a `DATE` value and returns a `DATE` value. The exceptions are the `MONTHS_BETWEEN` function, which returns a number, and the `ROUND` and `TRUNC` functions, which do not accept timestamp or interval values at all.

The remaining datetime functions were designed to accept any of the three types of data (date, timestamp, and interval) and to return a value of one of these types.

All of the datetime functions that return current system datetime information, such as `SYSDATE`, `SYSTIMESTAMP`, `CURRENT_TIMESTAMP`, and so forth, are evaluated once for each SQL statement, regardless how many times they are referenced in that statement.

The datetime functions are:

- [ADD\_MONTHS](ADD_MONTHS.md)
- [CURRENT\_DATE](CURRENT_DATE.md)
- [CURRENT\_TIMESTAMP](CURRENT_TIMESTAMP.md)
- [DBTIMEZONE](DBTIMEZONE.md)
- [EXTRACT (datetime)](EXTRACT-datetime.md)
- [FROM\_TZ](FROM_TZ.md)
- [LAST\_DAY](LAST_DAY.md)
- [LOCALTIMESTAMP](LOCALTIMESTAMP.md)
- [MONTHS\_BETWEEN](MONTHS_BETWEEN.md)
- [NEW\_TIME](NEW_TIME.md)
- [NEXT\_DAY](NEXT_DAY.md)
- [NUMTODSINTERVAL](NUMTODSINTERVAL.md)
- [NUMTOYMINTERVAL](NUMTOYMINTERVAL.md)
- [ORA\_DST\_AFFECTED](ORA_DST_AFFECTED.md)
- [ORA\_DST\_CONVERT](ORA_DST_CONVERT.md)
- [ORA\_DST\_ERROR](ORA_DST_ERROR.md)
- [ROUND (date)](ROUND-date.md)
- [SESSIONTIMEZONE](SESSIONTIMEZONE.md)
- [SYS\_EXTRACT\_UTC](SYS_EXTRACT_UTC.md)
- [SYSDATE](SYSDATE.md)
- [SYSTIMESTAMP](SYSTIMESTAMP.md)
- [TO\_CHAR (datetime)](TO_CHAR-datetime.md)
- [TO\_DSINTERVAL](TO_DSINTERVAL.md)
- [TO\_TIMESTAMP](TO_TIMESTAMP.md)
- [TO\_TIMESTAMP\_TZ](TO_TIMESTAMP_TZ.md)
- [TO\_YMINTERVAL](TO_YMINTERVAL.md)
- [TRUNC (date)](TRUNC-date.md)
- [TZ\_OFFSET](TZ_OFFSET.md)

### General Comparison Functions

The general comparison functions determine the greatest and or least value from a set of values. The general comparison functions are:

- [GREATEST](GREATEST.md)
- [LEAST](LEAST.md)

### Conversion Functions

Conversion functions convert a value from one data type to another. Generally, the form of the function names follows the convention `datatype` `TO` `datatype`. The first data type is the input data type. The second data type is the output data type. The SQL conversion functions are:

- [ASCIISTR](ASCIISTR.md)
- [BIN\_TO\_NUM](BIN_TO_NUM.md)
- [CAST](CAST.md)
- [CHARTOROWID](CHARTOROWID.md)
- [COMPOSE](COMPOSE.md)
- [CONVERT](CONVERT.md)
- [DECOMPOSE](DECOMPOSE.md)
- [HEXTORAW](HEXTORAW.md)
- [NUMTODSINTERVAL](NUMTODSINTERVAL.md)
- [NUMTOYMINTERVAL](NUMTOYMINTERVAL.md)
- [RAWTOHEX](RAWTOHEX.md)
- [RAWTONHEX](RAWTONHEX.md)
- [ROWIDTOCHAR](ROWIDTOCHAR.md)
- [ROWIDTONCHAR](ROWIDTONCHAR.md)
- [SCN\_TO\_TIMESTAMP](SCN_TO_TIMESTAMP.md)
- [TIMESTAMP\_TO\_SCN](TIMESTAMP_TO_SCN.md)
- [TO\_BINARY\_DOUBLE](TO_BINARY_DOUBLE.md)
- [TO\_BINARY\_FLOAT](TO_BINARY_FLOAT.md)
- [TO\_BLOB (bfile)](TO_BLOB-bfile.md)
- [TO\_BLOB (raw)](TO_BLOB-raw.md)
- [TO\_CHAR (bfile|blob)](TO_CHAR-bfile-blob.md)
- [TO\_CHAR (character)](TO_CHAR-character.md)
- [TO\_CHAR (datetime)](TO_CHAR-datetime.md)
- [TO\_CHAR (number)](TO_CHAR-number.md)
- [TO\_CLOB (bfile|blob)](TO_CLOB-bfile-blob.md)
- [TO\_CLOB (character)](TO_CLOB-character.md)
- [TO\_DATE](TO_DATE.md)
- [TO\_DSINTERVAL](TO_DSINTERVAL.md)
- [TO\_LOB](TO_LOB.md)
- [TO\_MULTI\_BYTE](TO_MULTI_BYTE.md)
- [TO\_NCHAR (character)](TO_NCHAR-character.md)
- [TO\_NCHAR (datetime)](TO_NCHAR-datetime.md)
- [TO\_NCHAR (number)](TO_NCHAR-number.md)
- [TO\_NCLOB](TO_NCLOB.md)
- [TO\_NUMBER](TO_NUMBER.md)
- [TO\_SINGLE\_BYTE](TO_SINGLE_BYTE.md)
- [TO\_TIMESTAMP](TO_TIMESTAMP.md)
- [TO\_TIMESTAMP\_TZ](TO_TIMESTAMP_TZ.md)
- [TO\_YMINTERVAL](TO_YMINTERVAL.md)
- [TREAT](TREAT.md)
- [UNISTR](UNISTR.md)
- [VALIDATE\_CONVERSION](VALIDATE_CONVERSION.md)

### Large Object Functions

The large object functions operate on LOBs. The large object functions are:

- [BFILENAME](BFILENAME.md)
- [EMPTY\_BLOB, EMPTY\_CLOB](EMPTY_BLOB-EMPTY_CLOB.md)

### Hierarchical Functions

Hierarchical functions applies hierarchical path information to a result set. The hierarchical function is:

- [SYS\_CONNECT\_BY\_PATH](SYS_CONNECT_BY_PATH.md)

### Oracle Machine Learning for SQL Functions

The Oracle Machine Learning for SQL functions use analytics to score data. The functions can apply a mining model schema object to the data, or they can dynamically mine the data by executing an analytic clause. The OML4SQL functions can be applied to models built using the native algorithms of Oracle, as well as those built using R through the extensibility mechanism.

The Oracle Machine Learning for SQL functions are:

- [CLUSTER\_DETAILS](CLUSTER_DETAILS.md)
- [CLUSTER\_DISTANCE](CLUSTER_DISTANCE.md)
- [CLUSTER\_ID](CLUSTER_ID.md)
- [CLUSTER\_PROBABILITY](CLUSTER_PROBABILITY.md)
- [CLUSTER\_SET](CLUSTER_SET.md)
- [FEATURE\_COMPARE](FEATURE_COMPARE.md)
- [FEATURE\_DETAILS](FEATURE_DETAILS.md)
- [FEATURE\_ID](FEATURE_ID.md)
- [FEATURE\_SET](FEATURE_SET.md)
- [FEATURE\_VALUE](FEATURE_VALUE.md)
- [ORA\_DM\_PARTITION\_NAME](ORA_DM_PARTITION_NAME.md)
- [PREDICTION](PREDICTION.md)
- [PREDICTION\_BOUNDS](PREDICTION_BOUNDS.md)
- [PREDICTION\_COST](PREDICTION_COST.md)
- [PREDICTION\_DETAILS](PREDICTION_DETAILS.md)
- [PREDICTION\_PROBABILITY](PREDICTION_PROBABILITY.md)
- [PREDICTION\_SET](PREDICTION_SET.md)

See Also:

- [Oracle Machine Learning for SQL Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=DMCON) to learn about Oracle Machine Learning for SQL
- [Oracle Machine Learning for SQL User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=DMPRG004) for information about scoring

### XML Functions

The XML functions operate on or return XML documents or fragments. These functions use arguments that are not defined as part of the ANSI/ISO/IEC SQL Standard but are defined as part of the World Wide Web Consortium (W3C) standards. The processing and operations that the functions perform are defined by the relevant W3C standards. The table below provides a link to the appropriate section of the W3C standard for the rules and guidelines that apply to each of these XML-related arguments. A SQL statement that uses one of these XML functions, where any of the arguments does not conform to the relevant W3C syntax, will result in an error. Of special note is the fact that not every character that is allowed in the value of a database column is considered legal in XML.

| Syntax Element | W3C Standard URL |
| --- | --- |
| `value_expr` | [`http://www.w3.org/TR/2006/REC-xml-20060816`](http://www.w3.org/TR/2006/REC-xml-20060816) |
| `Xpath_string` | [`http://www.w3.org/TR/1999/REC-xpath-19991116`](http://www.w3.org/TR/1999/REC-xpath-19991116) |
| `XQuery_string` | [`http://www.w3.org/TR/2007/REC-xquery-semantics-20070123/`](http://www.w3.org/TR/2007/REC-xquery-semantics-20070123/)  [`http://www.w3.org/TR/xquery-update-10/`](http://www.w3.org/TR/xquery-update-10/) |
| `namespace_string` | [`http://www.w3.org/TR/2006/REC-xml-names-20060816/`](http://www.w3.org/TR/2006/REC-xml-names-20060816/) |
| `identifier` | [`http://www.w3.org/TR/2006/REC-xml-20060816/#NT-Nmtoken`](http://www.w3.org/TR/2006/REC-xml-20060816/#NT-Nmtoken) |

For more information about selecting and querying XML data using these functions, including information on formatting output, refer to [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADXDB0400)

The SQL XML functions are:

- [DEPTH](DEPTH.md)
- [EXISTSNODE](EXISTSNODE.md)
- [EXTRACT (XML)](EXTRACT-XML.md)
- [EXTRACTVALUE](EXTRACTVALUE.md)
- [PATH](PATH.md)
- [SYS\_DBURIGEN](SYS_DBURIGEN.md)
- [SYS\_XMLAGG](SYS_XMLAGG.md)
- [SYS\_XMLGEN](SYS_XMLGEN.md)
- [XMLAGG](XMLAGG.md)
- [XMLCAST](XMLCAST.md)
- [XMLCDATA](XMLCDATA.md)
- [XMLCOLATTVAL](XMLCOLATTVAL.md)
- [XMLCOMMENT](XMLCOMMENT.md)
- [XMLCONCAT](XMLCONCAT.md)
- [XMLDIFF](XMLDIFF.md)
- [XMLELEMENT](XMLELEMENT.md)
- [XMLEXISTS](XMLEXISTS.md)
- [XMLFOREST](XMLFOREST.md)
- [XMLISVALID](XMLISVALID.md)
- [XMLPARSE](XMLPARSE.md)
- [XMLPATCH](XMLPATCH.md)
- [XMLPI](XMLPI.md)
- [XMLQUERY](XMLQUERY.md)
- [XMLSEQUENCE](XMLSEQUENCE.md)
- [XMLSERIALIZE](XMLSERIALIZE.md)
- [XMLTABLE](XMLTABLE.md)
- [XMLTRANSFORM](XMLTRANSFORM.md)

### JSON Functions

JavaScript Object Notation (JSON) functions allow you to query and generate JSON data.

The following SQL/JSON functions allow you to query JSON data:

- [JSON\_QUERY](JSON_QUERY.md)
- [JSON\_TABLE](JSON_TABLE.md)
- [JSON\_VALUE](JSON_VALUE.md)

The following SQL/JSON functions allow you to generate JSON data:

- [JSON\_ARRAY](JSON_ARRAY.md)
- [JSON\_ARRAYAGG](JSON_ARRAYAGG.md)
- [JSON\_OBJECT](JSON_OBJECT.md)
- [JSON\_OBJECTAGG](JSON_OBJECTAGG.md)
- [JSON Type Constructor](json-type-constructor.md)
- [JSON\_SCALAR](json_scalar.md)
- [JSON\_SERIALIZE](JSON_SERIALIZE.md)
- [JSON\_TRANSFORM](JSON_TRANSFORM.md)

The following Oracle SQL function creates a JSON data guide:

- [JSON\_DATAGUIDE](JSON_DATAGUIDE.md)
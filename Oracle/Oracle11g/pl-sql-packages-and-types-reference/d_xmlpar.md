---
title: DBMS_XMLPARSER
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xmlpar.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 174 DBMS\_XMLPARSER

Using `DBMS_XMLPARSER`, you can access the contents and structure of XML documents. XML describes a class of data XML document objects. It partially describes the behavior of computer programs which process them. By construction, XML documents are conforming SGML documents.

XML documents are made up of storage units called entities, which contain either parsed or unparsed data. Parsed data is made up of characters, some of which form character data, and some of which form markup. Markup encodes a description of the document's storage layout and logical structure. XML provides a mechanism to impose constraints on the storage layout and logical structure.

A software module called an XML processor is used to read XML documents and provide access to their content and structure. It is assumed that an XML processor is doing its work on behalf of another module, called the application. This PL/SQL implementation of the XML processor (or parser) follows the W3C XML specification REC-xml-19980210 and includes the required behavior of an XML processor in terms of how it must read XML data and the information it must provide to the application.

The default behavior for this PL/SQL XML parser is to build a parse tree that can be accessed by DOM APIs, validate it if a DTD is found (otherwise, it is non-validating), and record errors if an error log is specified. If parsing fails, an application error is raised.

This chapter contains the following topics:

- Using DBMS\_XMLPARSER
- Summary of DBMS\_XMLPARSER Subprograms

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

---

## Using DBMS\_XMLPARSER

- Security Model

---

### Security Model

Owned by `XDB`, the `DBMS_XDB_XMLPARSER` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

## Summary of DBMS\_XMLPARSER Subprograms

Table 174-1 DBMS\_XMLPARSER Package Subprograms

| Method | Description |
| --- | --- |
| FREEPARSER | Frees a parser object. |
| GETDOCTYPE | Gets parsed DTD. |
| GETDOCUMENT | Gets DOM document. |
| GETRELEASEVERSION | Returns the release version of Oracle XML Parser for PL/SQL. |
| GETVALIDATIONMODE | Returns validation mode. |
| NEWPARSER | Returns a new parser instance |
| PARSE | Parses XML stored in the given url/file. |
| PARSEBUFFER | Parses XML stored in the given buffer |
| PARSECLOB | Parses XML stored in the given clob |
| PARSEDTD | Parses DTD stored in the given url/file |
| PARSEDTDBUFFER | Parses DTD stored in the given buffer |
| PARSEDTDCLOB | Parses DTD stored in the given clob |
| SETBASEDIR | Sets base directory used to resolve relative URLs. |
| SETDOCTYPE | Sets DTD. |
| SETERRORLOG | Sets errors to be sent to the specified file |
| SETPRESERVEWHITESPACE | Sets white space preserve mode |
| SETVALIDATIONMODE | Sets validation mode. |
| SHOWWARNINGS | Turns warnings on or off. |

---

### FREEPARSER

Frees a parser object.

Syntax

```
PROCEDURE freeParser(
    p Parser);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |

---

### GETDOCTYPE

Returns the parsed DTD; this function must be called only after a DTD is parsed.

Syntax

```
FUNCTION getDoctype(
p Parser)
RETURN DOMDocumentType;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |

---

### GETDOCUMENT

Returns the document node of a DOM tree document built by the parser; this function must be called only after a document is parsed.

Syntax

```
FUNCTION GETDOCUMENT(
p Parser)
RETURN DOMDocument;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |

---

### GETRELEASEVERSION

Returns the release version of the Oracle XML parser for PL/SQL.

Syntax

```
FUNCTION getReleaseVersion
RETURN VARCHAR2;
```

---

### GETVALIDATIONMODE

Retrieves validation mode; `TRUE` for validating, `FALSE` otherwise.

Syntax

```
FUNCTION GETVALIDATIONMODE(
p Parser)
RETURN BOOLEAN;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |

---

### NEWPARSER

Returns a new parser instance. This function must be called before the default behavior of Parser can be changed and if other parse methods need to be used.

Syntax

```
FUNCTION newParser 
RETURN Parser;
```

---

### PARSE

Parses XML stored in the given URL or file. An application error is raised if parsing fails. There are several versions of this method.

| Syntax | Description |
| --- | --- |
| `FUNCTION parse(`  `   url VARCHAR2)`  `RETURN DOMDocument;` | Returns the built DOM Document. This is meant to be used when the default parser behavior is acceptable and just a url/file needs to be parsed. |
| `PROCEDURE parse(`  `   p Parser,`  `   url VARCHAR2);` | Any changes to the default parser behavior should be effected before calling this procedure. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | Complete path of the url/file to be parsed. |
| `p` | `(IN)` | Parser instance. |

---

### PARSEBUFFER

Parses XML stored in the given buffer. Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails.

Syntax

```
PROCEDURE PARSEBUFFER(
p   Parser,
doc VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `doc` | `(IN)` | XML document buffer to parse. |

---

### PARSECLOB

Parses XML stored in the given clob. Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails.

Syntax

```
PROCEDURE PARSECLOB(
p   Parser,
doc CLOB);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `doc` | `(IN)` | XML document buffer to parse. |

---

### PARSEDTD

Parses the DTD stored in the given URL or file. Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails.

Syntax

```
PROCEDURE PARSEDTD(
p     Parser,
url   VARCHAR2,
root  VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `url` | `(IN)` | Complete path of the URL or file to be parsed. |
| `root` | `(IN)` | Name of the root element. |

---

### PARSEDTDBUFFER

Parses the DTD stored in the given buffer. Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails.

Syntax

```
PROCEDURE PARSEDTDBUFFER(
p    Parser,
dtd  VARCHAR2,
root VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `dtd` | `(IN)` | DTD buffer to parse. |
| `root` | `(IN)` | Name of the root element. |

---

### PARSEDTDCLOB

Parses the DTD stored in the given clob. Any changes to the default parser behavior should be effected before calling this procedure. An application error is raised if parsing fails.

Syntax

```
PROCEDURE PARSEDTDCLOB(
p    Parser,
dtd  CLOB,
root VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `dtd` | `(IN)` | DTD Clob to parse. |
| `root` | `(IN)` | Name of the root element. |

---

### SETBASEDIR

Sets base directory used to resolve relative URLs. An application error is raised if parsing fails.

Syntax

```
PROCEDURE setBaseDir(
p   Parser,
dir VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `dir` | (IN) | Directory used as a base directory. |

---

### SETDOCTYPE

Sets a DTD to be used by the parser for validation. This call should be made before the document is parsed.

Syntax

```
PROCEDURE setDoctype(
p   Parser,
dtd DOMDocumentType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `dtd` | `(IN)` | DTD to set. |

---

### SETERRORLOG

Sets errors to be sent to the specified file.

Syntax

```
PROCEDURE setErrorLog(
p        Parser,
fileName VARCHAR2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `fileName` | `(IN)` | Complete path of the file to use as the error log. |

---

### SETPRESERVEWHITESPACE

Sets whitespace preserving mode.

Syntax

```
PROCEDURE setPreserveWhitespace(
p   Parser,
yes BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `yes` | `(IN)` | Mode to set: `TRUE` - preserve, `FALSE` - don't preserve. |

---

### SETVALIDATIONMODE

Sets validation mode.

Syntax

```
PROCEDURE setValidationMode(
p   Parser,
yes BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `yes` | `(IN)` | Mode to set: `TRUE` - validate, `FALSE` - don't validate. |

---

### SHOWWARNINGS

Turns warnings on or off.

Syntax

```
PROCEDURE showWarnings(
p   Parser,
yes BOOLEAN);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `p` | `(IN)` | Parser instance. |
| `yes` | `(IN)` | Mode to set: `TRUE` - show warnings, `FALSE` - don't show warnings. |
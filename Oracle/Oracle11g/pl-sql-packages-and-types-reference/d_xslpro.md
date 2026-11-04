---
title: DBMS_XSLPROCESSOR
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xslpro.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 181 DBMS\_XSLPROCESSOR

The DBMS\_XSLPROCESSOR package provides an interface to manage the contents and structure of XML documents.

This chapter contains the following topics:

- Using DBMS\_XSLPROCESSOR
- Summary of DBMS\_XSLPROCESSOR Subprograms
	See Also:
	- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

---

## Using DBMS\_XSLPROCESSOR

This section contains topics which relate to using the `DBMS_XSLPROCESSOR` package.

---

### Overview

The `DBMS_XSLPROCESSOR` package provides an interface to manage the contents and structure of XML documents.

Standards

This PL/SQL implementation of the XSL processor follows the W3C XSLT working draft rev WD-xslt-19990813 and includes the required behavior of an XSL processor in terms of how it must read XSLT stylesheets and the transformation it must effect.

Concepts

The Extensible Stylesheet Language Transformation (XSLT) describes rules for transforming a source tree into a result tree. A transformation expressed in XSLT is called a stylesheet. The transformation specified is achieved by associating patterns with templates defined in the stylesheet. A template is instantiated to create part of the result tree.

Implementation

The following is the default behavior for this PL/SQL XSL Processor:

- A result tree which can be accessed by DOM programmatic interface
- Errors are not recorded unless an error log is specified; however, an application error will be raised if parsing fails

---

### Security Model

Owned by `XDB`, the `DBMS_XSLPROCESSOR` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

## Summary of DBMS\_XSLPROCESSOR Subprograms

Table 181-1 DBMS\_XSLPROCESSOR Package Subprograms

| Method | Description |
| --- | --- |
| CLOB2FILE Procedure | Writes content of a `CLOB` into a file |
| FREEPROCESSOR Procedure | Frees a processor object |
| FREESTYLESHEET Procedure | Frees a stylesheet object |
| NEWPROCESSOR Function | Returns a new processor instance |
| NEWSTYLESHEET Functions | Creates a new stylesheet from input and reference URLs |
| PROCESSXSL Functions and Procedures | Transforms an input XML document |
| READ2CLOB Function | Reads content of the file into a `CLOB` |
| REMOVEPARAM Procedure | Removes a top-level stylesheet parameter |
| RESETPARAMS Procedure | Resets the top-level stylesheet parameters |
| SELECTNODES Function | Selects nodes from a DOM tree that match a pattern |
| SELECTSINGLENODE Function | Selects the first node from the tree that matches a pattern |
| SETERRORLOG Procedure | Sets errors to be sent to the specified file |
| SETPARAM Procedure | Sets a top-level parameter in the stylesheet |
| SHOWWARNINGS Procedure | Turns warnings on or off |
| TRANSFORMNODE Function | Transforms a node in a DOM tree using a stylesheet |
| VALUEOF Function and Procedure | Gets the value of the first node that matches a pattern |

---

### CLOB2FILE Procedure

This procedure writes content of a `CLOB` into a file.

Syntax

```
DBMS_XSLPROCESSOR.CLOB2FILE(
  cl          IN  CLOB;
  flocation   IN  VARCHAR2,
  fname       IN  VARCHAR2,
  csid        IN  NUMBER:=0);
```

Parameters

Table 181-2 CLOB2FILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `CLOB` | File directory |
| `flocation` | File directory |
| `fname` | File name |
| `csid` | Character set id of the file  - Must be a valid Oracle id; otherwise returns an error - If `0`, content of the output file will be in the database character set |

---

### FREEPROCESSOR Procedure

This procedure Frees a `Processor` object.

Syntax

```
DBMS_XSLPROCESSOR.FREEPROCESSOR(
  p  IN  Processor);
```

Parameters

Table 181-3 FREEPROCESSOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | Processor |

---

### FREESTYLESHEET Procedure

This procedure frees a `Stylesheet` object.

Syntax

```
DBMS_XSLPROCESSOR.FREESTYLESHEET(
  ss  IN  Stylesheet);
```

Parameters

Table 181-4 FREESTYLESHEET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | Stylesheet |

---

### NEWPROCESSOR Function

This function returns a new `Processor` instance. The function must be called before the default behavior of `Processor` can be changed and if other processor methods need to be used.

Syntax

```
DBMS_XSLPROCESSOR.NEWPROCESSOR
 RETURN Processor;
```

---

### NEWSTYLESHEET Functions

This function creates and returns a new `Stylesheet` instance. The options are described in the following table.

Syntax

Creates and returns a new stylesheet instance using the given `DOMDOCUMENT` and reference URLs:

```
DBMS_XSLPROCESSOR.NEWSTYLESHEET(
   xmldoc  IN   DOMDOCUMENT,
   ref     IN   VARCHAR2) 
 RETURN Stylesheet;
```

Creates and returns a new `Stylesheet` instance using the given input and reference URLs:

```
DBMS_XSLPROCESSOR.NEWSTYLESHEET(
   inp    IN   VARCHAR2,
   ref    IN   VARCHAR2) 
 RETURN Stylesheet;
```

Parameters

Table 181-5 NEWSTYLESHEET Function Parameters

| Parameter | Description |
| --- | --- |
| `xmldoc` | `DOMDocument` to use for construction |
| `inp` | Input URL to use for construction |
| `ref` | Reference URL |

---

### PROCESSXSL Functions and Procedures

This function transforms input `XMLDocument`. Any changes to the default processor behavior should be effected before calling this procedure. An application error is raised if processing fails.

Syntax

Transforms input `XMLDocument` using given `DOMDocument` and stylesheet, and returns the resultant document fragment:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p      IN   Processor,
   ss     IN   Stylesheet,
   xmldoc IN   DOMDOCUMENT), 
 RETURN DOMDOCUMENTFRAGMENT;
```

Transforms input `XMLDocument` using given document as URL and the `Stylesheet`, and returns the resultant document fragment:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p     IN   Processor,
   ss    IN   Stylesheet,
   url   IN   VARCHAR2, 
 RETURN DOMDOCUMENTFRAGMENT;
```

Transforms input `XMLDocument` using given document as `CLOB` and the `Stylesheet`, and returns the resultant document fragment:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p     IN   Processor,
   ss    IN  Stylesheet,
   clb   IN  CLOB)
 RETURN DOMDOCUMENTFRAGMENT;
```

Transforms input `XMLDocument` using given `DOMDOCUMENT` and the stylesheet, and writes the output to the specified file:

```
DBMS_XSLPROCESSOR.DBMS_XSLPROCESSOR.(
   p           IN    Processor,
   ss          IN    Stylesheet,
   xmldoc      IN    DOMDOCUMENT,
   dir         IN    VARCHAR2,
   fileName    IN    VARCHAR2);
```

Transforms input `XMLDocument` using given URL and the stylesheet, and writes the output to the specified file in a specified directory:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p          IN    Processor,
   ss         IN    Stylesheet,
   url        IN    VARCHAR2,
   dir        IN    VARCHAR2,
   fileName   IN    VARCHAR2);
```

Transforms input `XMLDocument` using given `DOMDOCUMENT` and the stylesheet, and writes the output to a `CLOB`:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p          IN      Processor,
   ss         IN      Stylesheet,
   xmldoc     IN      DOMDOCUMENT,
   cl         IN OUT  CLOB);
```

Transforms input `XMLDocument` using given `DOMDOCUMENTFRAGMENT` and the stylesheet, and returns the resultant document fragment:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p         IN    Processor,
   ss        IN    Stylesheet,
   xmldf     IN    DOMDOCUMENTFRAGMENT)
 RETURN DOMDOCUMENTFRAGMENT;
```

Transforms input `XMLDocumentFragment` using given `DOMDocumentFragment` and the stylesheet, and writes the output to the specified file in a specified directory:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p         IN    Processor,
   ss        IN    Stylesheet,
   xmldf     IN    DOMDOCUMENTFRAGMENT,
   dir       IN    VARCHAR2,
   filename  IN    VARCHAR2);
```

Transforms input `XMLDocumentFragment` using given `DOMDOCUMENTFRAGMENT` and the stylesheet, and writes the output to a buffer:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p          IN       Processor,
   ss         IN       Stylesheet,
   xmldf      IN       DOMDOCUMENTFRAGMENT,
   buf        IN OUT   VARCHAR2);
```

Transforms input `XMLDocumentFragment` using given `DOMDOCUMENTFRAGMENT` and the stylesheet, and writes the output to a `CLOB`:

```
DBMS_XSLPROCESSOR.PROCESSXSL(
   p          IN      Processor,
   ss         IN      Stylesheet,
   xmldf      IN      DOMDOCUMENTFRAGMENT,
   cl         IN OUT  CLOB);
```

Parameters

Table 181-6 PROCESSXSL Function and Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | `Processor` instance |
| `ss` | `Stylesheet` instance |
| `xmldoc` | XML document being transformed |
| `url` | URL for the information being transformed |
| `clb` | `CLOB` containing information to be transformed |
| `dir` | Directory where processing output file is saved |
| `filename` | Processing output file |
| `cl` | `CLOB` to which the processing output is saved |
| `xmldf` | `XMLDocumentFragment` being transformed |

---

### READ2CLOB Function

This function reads content of a file into a `CLOB`.

Syntax

```
DBMS_XSLPROCESSOR.READ2CLOB(
   flocation     IN   VARCHAR2,
   fname         IN   VARCHAR2,
   csid          IN   NUMBER:=0)
 RETURN CLOB;
```

Parameters

Table 181-7 READ2CLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `flocation` | File directory |
| `fname` | File name |
| `csid` | Character set id of the file  - Must be a valid Oracle id; otherwise returns an error - If `0`, input file is assumed to be in the database character set |

---

### REMOVEPARAM Procedure

This procedure removes a top level stylesheet parameter.

Syntax

```
DBMS_XSLPROCESSOR.REMOVEPARAM(
   ss     IN  Stylesheet,
   name   IN  VARCHAR2);
```

Parameters

Table 181-8 REMOVEPARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |
| `name` | Name of the parameter |

---

### RESETPARAMS Procedure

This procedure resets the top-level stylesheet parameters.

Syntax

```
DBMS_XSLPROCESSOR.RESETPARAMS(
   ss  IN   Stylesheet);
```

Parameters

Table 181-9 RESETPARAMS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |

---

### SELECTNODES Function

This function selects nodes which match the suplied path expression from a DOM tree, and returns the result of the selection.

Syntax

```
DBMS_XSLPROCESSOR.SELECTNODES( 
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODELIST;
```

Parameters

Table 181-10 SELECTNODES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | Root `DOMNode` of the tree |
| `pattern` | Pattern to use |
| `namespace` | Namespace declared |

---

### SELECTSINGLENODE Function

This function selects the first node from the tree that match the suplied path expression, and returns that node.

Syntax

```
DBMS_XSLPROCESSOR.SELECTSINGLENODE(
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODE;
```

Parameters

Table 181-11 SELECTSINGLENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | Root `DOMNode` of the tree |
| `pattern` | Pattern to use |
| `namespace` | Namespace declared |

---

### SETERRORLOG Procedure

This procedure sets errors to be sent to the specified file.

Note:

This subprogram has been deprecated, and is included only for reasons of backward compatibility.

Syntax

```
DBMS_XSLPROCESSOR.SETERRORLOG(
   p         IN   Processor,
   fileName  IN   VARCHAR2);
```

Parameters

Table 181-12 SETERRORLOG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | `Processor` instance |
| `fileName` | Complete path of the file to use as the error log |

---

### SETPARAM Procedure

This procedure sets a top level parameter in the stylesheet. The parameter value must be a valid `XPath` expression. Literal string values must be quoted.

Syntax

```
DBMS_XSLPROCESSOR.SETPARAM(
   ss      IN   Stylesheet,
   name    IN   VARCHAR2,
   value   IN   VARCHAR2);
```

Parameters

Table 181-13 SETPARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |
| `name` | Name of the parameter |
| `value` | Value of the parameter |

---

### SHOWWARNINGS Procedure

This procedure turns warnings on `(TRUE)` or off `(FALSE)`.

Syntax

```
DBMS_XSLPROCESSOR.SHOWWARNINGS(
   p     IN   Processor,
   yes   IN   BOOLEAN);
```

Parameters

Table 181-14 SHOWWARNINGS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | `Processor` instance |
| `yes` | Mode to set: `TRUE` to show warnings, `FALSE` otherwise |

---

### TRANSFORMNODE Function

This function transforms a node in a DOM tree using the given stylesheet, and returns the result of the transformation as a `DOMDocumentFragment`.

Syntax

```
DBMS_XSLPROCESSOR.TRANSFORMNODE(
   n    IN  DOMNODE,
   ss   IN  Stylesheet)
 RETURN DOMDocumentFragment;
```

Parameters

Table 181-15 TRANSFORMNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` to transform |
| `ss` | Stylesheet to use |

---

### VALUEOF Function and Procedure

This subprogram retrieves the value of the first node from the tree that matches the given pattern. You can use either a function or a procedure.

Syntax

```
DBMS_XSLPROCESSOR.VALUEOF(
  n           IN    DBMS_XMLDOM.DOMNODE,
  pattern     IN    VARCHAR2,
  namespace   IN    VARCHAR2 := NULL)
 RETURN VARCHAR2;
```

```
DBMS_XSLPROCESSOR.VALUEOF(
  n           IN    DBMS_XMLDOM.DOMNODE,
  pattern     IN    VARCHAR2,
  val         OUT   VARCHAR2,
  namespace   IN    VARCHAR2 := NULL);
```

Parameters

Table 181-16 VALUEOF Function and Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | Node whose value is being retrieved |
| `pattern` | Pattern to use |
| `val` | Retrieved value |
| namespace | Namespace to use |
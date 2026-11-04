---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XSLPROCESSOR.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 220 DBMS\_XSLPROCESSOR

The `DBMS_XSLPROCESSOR` package provides an interface to manage the contents and structure of XML documents.

This chapter contains the following topics:

- DBMS\_XSLPROCESSOR Overview
- DBMS\_XSLPROCESSOR Security Model
- Summary of DBMS\_XSLPROCESSOR Subprograms
	See Also:
	- [Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB-GUID-8611495B-A091-4B11-9E65-E8AD20D50D97)

### 220.1 DBMS\_XSLPROCESSOR Overview

The `DBMS_XSLPROCESSOR` package provides an interface to manage the contents and structure of XML documents.

Standards

This PL/SQL implementation of the XSL processor follows the W3C XSLT working draft rev WD-xslt-19990813 and includes the required behavior of an XSL processor in terms of how it must read XSLT stylesheets and the transformation it must effect.

Concepts

The Extensible Stylesheet Language Transformation (XSLT) describes rules for transforming a source tree into a result tree. A transformation expressed in XSLT is called a stylesheet. The transformation specified is achieved by associating patterns with templates defined in the stylesheet. A template is instantiated to create part of the result tree.

Implementation

The following is the default behavior for this PL/SQL XSL Processor:

- A result tree which can be accessed by DOM programmatic interface
- Errors are not recorded unless an error log is specified; however, an application error will be raised if parsing fails

### 220.2 DBMS\_XSLPROCESSOR Security Model

Owned by `XDB`, the `DBMS_XSLPROCESSOR` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### 220.3 Summary of DBMS\_XSLPROCESSOR Subprograms

This table lists the `DBMS_XSLPROCESSOR` subprograms and briefly describes them.

Table 220-1 DBMS\_XSLPROCESSOR Package Subprograms

| Method | Description |
| --- | --- |
| FREEPROCESSOR Procedure | Frees a processor object |
| FREESTYLESHEET Procedure | Frees a stylesheet object |
| NEWPROCESSOR Function | Returns a new processor instance |
| NEWSTYLESHEET Functions | Creates a new stylesheet from input and reference URLs |
| PROCESSXSL Functions and Procedures | Transforms an input XML document |
| REMOVEPARAM Procedure | Removes a top-level stylesheet parameter |
| RESETPARAMS Procedure | Resets the top-level stylesheet parameters |
| SELECTNODES Function | Selects nodes from a DOM tree that match a pattern |
| SELECTSINGLENODE Function | Selects the first node from the tree that matches a pattern |
| SETERRORLOG Procedure | Sets errors to be sent to the specified file |
| SETPARAM Procedure | Sets a top-level parameter in the stylesheet |
| SHOWWARNINGS Procedure | Turns warnings on or off |
| TRANSFORMNODE Function | Transforms a node in a DOM tree using a stylesheet |
| VALUEOF Function and Procedure | Gets the value of the first node that matches a pattern |

#### 220.3.1 FREEPROCESSOR Procedure

This procedure frees a `Processor` object.

Syntax

```
DBMS_XSLPROCESSOR.FREEPROCESSOR(
  p  IN  Processor);
```

Parameters

Table 220-2 FREEPROCESSOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | Processor |

#### 220.3.2 FREESTYLESHEET Procedure

This procedure frees a `Stylesheet` object.

Syntax

```
DBMS_XSLPROCESSOR.FREESTYLESHEET(
  ss  IN  Stylesheet);
```

Parameters

Table 220-3 FREESTYLESHEET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | Stylesheet |

#### 220.3.3 NEWPROCESSOR Function

This function returns a new `Processor` instance.

The function must be called before the default behavior of `Processor` can be changed and if other processor methods need to be used.

Syntax

```
DBMS_XSLPROCESSOR.NEWPROCESSOR
 RETURN Processor;
```

#### 220.3.4 NEWSTYLESHEET Functions

This function creates and returns a new `Stylesheet` instance.

The options are described in the following table.

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

Table 220-4 NEWSTYLESHEET Function Parameters

| Parameter | Description |
| --- | --- |
| `xmldoc` | `DOMDocument` to use for construction |
| `inp` | Input URL to use for construction |
| `ref` | Reference URL |

#### 220.3.5 PROCESSXSL Functions and Procedures

This function transforms input `XMLDocument`.

Any changes to the default processor behavior should be effected before calling this procedure. An application error is raised if processing fails.

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

Transforms input `XMLDocument` using given document as `CLOB ` and the `Stylesheet`, and returns the resultant document fragment:

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

Table 220-5 PROCESSXSL Function and Procedure Parameters

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

#### 220.3.6 REMOVEPARAM Procedure

This procedure removes a top level stylesheet parameter.

Syntax

```
DBMS_XSLPROCESSOR.REMOVEPARAM(
   ss     IN  Stylesheet,
   name   IN  VARCHAR2);
```

Parameters

Table 220-6 REMOVEPARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |
| `name` | Name of the parameter |

#### 220.3.7 RESETPARAMS Procedure

This procedure resets the top-level stylesheet parameters.

Syntax

```
DBMS_XSLPROCESSOR.RESETPARAMS(
   ss  IN   Stylesheet);
```

Parameters

Table 220-7 RESETPARAMS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |

#### 220.3.8 SELECTNODES Function

This function selects nodes which match the supplied path expression from a DOM tree, and returns the result of the selection.

Syntax

```
DBMS_XSLPROCESSOR.SELECTNODES( 
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODELIST;
```

Parameters

Table 220-8 SELECTNODES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | Root `DOMNode` of the tree |
| `pattern` | Pattern to use |
| `namespace` | Namespace declared |

#### 220.3.9 SELECTSINGLENODE Function

This function selects the first node from the tree that match the supplied path expression, and returns that node.

Syntax

```
DBMS_XSLPROCESSOR.SELECTSINGLENODE(
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODE;
```

Parameters

Table 220-9 SELECTSINGLENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | Root `DOMNode` of the tree |
| `pattern` | Pattern to use |
| `namespace` | Namespace declared |

#### 220.3.10 SETERRORLOG Procedure

This deprecated procedure sets errors to be sent to the specified file.

Note:

This subprogram has been deprecated, and is included only for reasons of backward compatibility.

Syntax

```
DBMS_XSLPROCESSOR.SETERRORLOG(
   p         IN   Processor,
   fileName  IN   VARCHAR2);
```

Parameters

Table 220-10 SETERRORLOG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | `Processor` instance |
| `fileName` | Complete path of the file to use as the error log |

#### 220.3.11 SETPARAM Procedure

This procedure sets a top level parameter in the stylesheet.

The parameter value must be a valid `XPath` expression. Literal string values must be quoted.

Syntax

```
DBMS_XSLPROCESSOR.SETPARAM(
   ss      IN   Stylesheet,
   name    IN   VARCHAR2,
   value   IN   VARCHAR2);
```

Parameters

Table 220-11 SETPARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ss` | `Stylesheet` instance |
| `name` | Name of the parameter |
| `value` | Value of the parameter |

#### 220.3.12 SHOWWARNINGS Procedure

This procedure turns warnings on `(TRUE)` or off `(FALSE)`.

Syntax

```
DBMS_XSLPROCESSOR.SHOWWARNINGS(
   p     IN   Processor,
   yes   IN   BOOLEAN);
```

Parameters

Table 220-12 SHOWWARNINGS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p` | `Processor` instance |
| `yes` | Mode to set: `TRUE ` to show warnings, `FALSE` otherwise |

#### 220.3.13 TRANSFORMNODE Function

This function transforms a node in a DOM tree using the given stylesheet, and returns the result of the transformation as a `DOMDocumentFragment`.

Syntax

```
DBMS_XSLPROCESSOR.TRANSFORMNODE(
   n    IN  DOMNODE,
   ss   IN  Stylesheet)
 RETURN DOMDocumentFragment;
```

Parameters

Table 220-13 TRANSFORMNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` to transform |
| `ss` | Stylesheet to use |

#### 220.3.14 VALUEOF Function and Procedure

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

Table 220-14 VALUEOF Function and Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | Node whose value is being retrieved |
| `pattern` | Pattern to use |
| `val` | Retrieved value |
| namespace | Namespace to use |
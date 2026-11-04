---
title: XMLTYPE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/t_xml.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 260 XMLTYPE

`XMLType` is a system-defined opaque type for handling XML data. It as predefined member functions on it to extract XML nodes and fragments.

You can create columns of `XMLType` and insert XML documents into it. You can also generate XML documents as `XMLType` instances dynamically using the `SYS_XMLGEN` and `SYS_XMLAGG SQL` functions.

This chapter contains the following topics:

- Summary of XMLType Subprograms
	See Also:
	- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

---

## Summary of XMLType Subprograms

Table 260-1 summarizes functions and procedures of the `XMLType`.

Table 260-1 XMLTYPE Subprograms

| Method | Description |
| --- | --- |
| CREATENONSCHEMABASEDXML | Creates a non schema based XML from the input schema based instance. |
| CREATESCHEMABASEDXML | Creates a schema based `XMLType` instance from the non-schema based instance using the input schema URL. |
| CREATEXML | Static function for creating and returning an `XMLType` instance. |
| EXISTSNODE | Takes a `XMLType` instance and a `XPath` and returns 1 or 0 indicating if applying the `XPath` returns a non-empty set of nodes. |
| EXTRACT | Takes a `XMLType` instance and an `XPath`, applies the XPath expression and returns the results as an `XMLType`. |
| GETBLOBVAL | Returns the value of the `XMLType` instance as a `BLOB` |
| GETCLOBVAL | Returns the value of the `XMLType` instance as a `CLOB`. |
| GETNAMESPACE | Returns the namespace for the top level element in a schema based document. |
| GETNUMBERVAL | Returns the value of the `XMLType` instance as a `NUMBER`. This is only valid if the input `XMLType` instance contains a simple text node and is convertible to a number. |
| GETROOTELEMENT | Returns the root element of the input instance. Returns `NULL` if the instance is a fragment |
| GETSCHEMAURL | Returns the XML schema URL if the input is an XML Schema based. |
| GETSTRINGVAL | Returns the value of the `XMLType` instance as a string. |
| ISFRAGMENT | Checks if the input `XMLType` instance is a fragment or not. A fragment is a XML instance, which has more than one root element. |
| ISSCHEMABASED | Returns 1 or 0 indicating if the input `XMLType` instance is a schema based one or not. |
| ISSCHEMAVALID | Checks if the input instance is schema valid according to the given schema URL. |
| ISSCHEMAVALIDATED | Checks if the instance has been validated against the schema. |
| SCHEMAVALIDATE | Validates the input instance according to the XML Schema. Raises error if the input instance is non-schema based. |
| SETSCHEMAVALIDATED | Sets the schema valid flag to avoid costly schema validation. |
| TOOBJECT | Converts the `XMLType` instance to an object type. |
| TRANSFORM | Takes an `XMLType` instance and an associated stylesheet (which is also an `XMLType` instance), applies the stylesheet and returns the result as XML. |
| XMLTYPE | Constructs an instance of the `XMLType` datatype. The constructor can take in the XML as a `CLOB`, `VARCHAR2` or take in a object type. |

---

### CREATENONSCHEMABASEDXML

Member function. Creates a non-schema based XML document from a schema based instance.

Syntax

```
MEMBER FUNCTION CREATENONSCHEMABASEDXML
return XMLType deterministic;
```

---

### CREATESCHEMABASEDXML

Member function. Creates a schema based `XMLType` instance from a non-schema based `XMLType` value. It uses either the supplied `SCHEMA` URL, or the `SCHEMALOCATION` attribute of the instance.

Syntax

```
MEMBER FUNCTION createSchemaBasedXML(
schema IN varchar2 := NULL)
return XMLType deterministic;
```

| Parameter | Description |
| --- | --- |
| `schema` | Optional XMLSchema URL used to convert the value to the specified schema.. |

---

### CREATEXML

Static function for creating and returning an `XMLType` instance. The string and clob parameters used to pass in the date must contain well-formed and valid XML documents. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `STATIC FUNCTION createXML(`  `   xmlData IN varchar2)`  `RETURN XMLType deterministic;` | Creates the `XMLType` instance from a string. |
| `STATIC FUNCTION createXML(`  `   xmlData IN clob)`  `RETURN XMLType deterministic;` | Creates the `XMLType` instance from a `CLOB`. |
| `STATIC FUNCTION createXML (`  `   xmlData IN clob,`  `   schema IN varchar2,`  `   validated IN number := 0,`  `   wellformed IN number := 0 )`  `RETURN XMLType deterministic;` | This static function creates a schema-based `XMLType` instance using the specified schema and xml data parameters. |
| `STATIC FUNCTION createXML (`  `   xmlData IN varchar2,`  `   schema IN varchar2,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `RETURN XMLType deterministic;` | This static function creates a schema-based `XMLType` instance using the specified schema and xml data parameters. |
| `STATIC FUNCTION createXML (`  `   xmlData IN "<ADT_1>",`  `   schema IN varchar2 := NULL,`  `   element IN varchar2 := NULL,`  `   validated IN NUMBER := 0)`  `RETURN XMLType deterministic;` | Creates an XML instance from an instance of an user-defined type. |
| `STATIC FUNCTION createXML (`  `   xmlData IN SYS_REFCURSOR,`  `   schema in varchar2 := NULL,`  `   element in varchar2 := NULL,`  `   validated in number := 0)`  `RETURN XMLType deterministic;` | Creates an XML instance from a cursor reference. You can pass in any arbitrary SQL query as a `CURSOR`. |
| `STATIC FUNCTION createXML (`  `   xmlData IN AnyData,`  `   schema in varchar2 := NULL,`  `   element in varchar2 := NULL,`  `   validated in number := 0)`  `RETURN sys.XMLType deterministic`  `   parallel_enable` | Creates an XML instance from `ANYDATA`.If the `ANYDATA` instance contains an ADT, the `XMLType` returned is the same as would be returned for a call directly on the ADT. If the `ANYDATA` contains a scalar, the `XMLType` contains a leaf node with the scalar value. The element name for this node is taken from the optional element string if present, and is " `ANYDATA` " if it is not. |
| `STATIC FUNCTION createXML (`  `   xmlData IN blob,`  `   csid IN number,`  `   schema IN varchar2,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `return sys.XMLType deterministic` | Creates an XML instance from a `BLOB`. |
| `STATIC FUNCTION createXML (`  `   xmlData IN bfile,`  `   csid IN number,`  `   Schema IN varchar2,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `return sys.XMLType deterministic` | Creates an XML instance from a `BFILE`. |

| Parameter | Description |
| --- | --- |
| `xmlData` | The actual data in the form of a `BFILE`, `BLOB`, `CLOB`, `REF` cursor, `VARCHAR2` or object type. |
| `schema` | Optional Schema URL to be used to make the input conform to the given schema. |
| `validated` | Flag to indicate that the instance is valid according to the given XML Schema. (Default is `0`) |
| `wellformed` | Flag to indicate that the input is well formed. If set, then the database would not do well formed check on the input instance. (Default is `0`) |
| `element` | Optional element name in the case of the `ADT_1` or `REF CURSOR` constructors. (Default is `NULL`) |
| `CSID` | The character set id of input XML data. |

---

### EXISTSNODE

Member function. Checks if the node exists. If the XPath string is `NULL` or the document is empty, then a value of 0 is returned, otherwise returns 1. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION existsNode(`  `   xpath IN varchar2)`  `RETURN number deterministic;` | Given an XPath expression, checks if the XPath applied over the document can return any valid nodes. |
| `MEMBER FUNCTION existsNode(`  `   xpath in varchar2,`  `   nsmap in varchar2)`  `RETURN number deterministic;` | This member function uses the XPath expression with the namespace information and checks if applying the XPath returns any nodes or not. |

| Parameter | Description |
| --- | --- |
| `xpath` | The XPath expression to test. |
| `nsmap` | Optional namespace mapping. |

---

### EXTRACT

Member function. Extracts an `XMLType` fragment and returns an `XMLType` instance containing the result node(s). If the XPath does not result in any nodes, then returns `NULL`. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION extract(`  `   xpath IN varchar2)`  `RETURN XMLType deterministic;` | Given an XPath expression, applies the XPath to the document and returns the fragment as an `XMLType`. |
| `MEMBER FUNCTION extract(`  `   xpath IN varchar2,`  `   nsmap IN varchar2)`  `RETURN XMLType deterministic;` | This member function applies the XPath expression and namespace mapping, over the XML data to return a `XMLType` instance containing the resultant fragment. |

| Parameter | Description |
| --- | --- |
| `xpath` | The XPath expression to apply. |
| `nsmap` | Optional prefix to namespace mapping information. |

---

### GETBLOBVAL

Member function. Returns a `BLOB` containing the serialized XML representation; if the `BLOB` returned is temporary, it must be freed after use.

Syntax

```
MEMBER FUNCTION getBlobVal(
   csid   IN   NUMBER)
 RETURN Blob deterministic;
```

| Parameter | Description |
| --- | --- |
| `csid` | The character set id of input XML data |

---

### GETCLOBVAL

Member function. Returns a `CLOB` containing the serialized XML representation; if the `CLOB` returned is temporary, it must be freed after use.

Syntax

```
MEMBER FUNCTION getClobVal()
RETURN clob deterministic;
```

---

### GETNAMESPACE

Member function. Returns the namespace of the top level element in the instance. Returns `NULL` if the input is a fragment or is a non-schema based instance.

Syntax

```
MEMBER FUNCTION getNamespace
return varchar2 deterministic;
```

---

### GETNUMBERVAL

Member function. Returns a numeric value, formatted from the text value pointed to by the `XMLType` instance. The `XMLType` must point to a valid text node that contains a numerical value. The options are described in the following table.

Syntax

```
MEMBER FUNCTION getNumberVal()
RETURN number deterministic;
```

---

### GETROOTELEMENT

Member function. Gets the root element of the `XMLType` instance. Returns `NULL` if the instance is a fragment.

Syntax

```
MEMBER FUNCTION getRootElement
return varchar2 deterministic;
```

---

### GETSCHEMAURL

Member function. Returns the XML Schema URL corresponding to the `XMLType` instance, if the `XMLType` instance is a schema-based document. Otherwise returns `NULL`.

Syntax

```
MEMBER FUNCTION getSchemaURL
return varchar2 deterministic;
```

---

### GETSTRINGVAL

Member function. Returns the document as a string. Returns s string containing the seralized XML representation, or in case of text nodes, the text itself. If the XML document is bigger than the maximum size of the `VARCHAR2`, which is 4000, then an error is raised at run time.

Syntax

```
MEMBER FUNCTION getStringVal()
RETURN varchar2 deterministic;
```

---

### ISFRAGMENT

Determines if the `XMLType` instance corresponds to a well-formed document, or a fragment. Returns 1 or 0 indicating if the `XMLType` instance contains a fragment or a well-formed document.

Syntax

```
MEMBER FUNCTION isFragment()
RETURN number deterministic;
```

---

### ISSCHEMABASED

Member function. Determines whether the `XMLType` instance is schema-based or not. Returns 1 or 0 depending on whether the `XMLType` instance is schema-based.

Syntax

```
MEMBER FUNCTION isSchemaBased
return number deterministic;
```

---

### ISSCHEMAVALID

Member function. Checks if the input instance is conformant to a specified schema. Does not change the validation status of the XML instance. If a XML Schema URL is not specified and the xml document is schema based, the conformance is checked against the `XMLType` instance's own schema.

Syntax

```
member function isSchemaValid(
schurl IN VARCHAR2 := NULL,
elem IN VARCHAR2 := NULL)
return NUMBER deterministic;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `schurl` | `(IN)` | The URL of the XML Schema against which to check conformance. |
| `elem` | `(IN)` | Element of a specified schema, against which to validate. This is useful when we have a XML Schema which defines more than one top level element, and we want to check conformance against a specific one of these elements. |

---

### ISSCHEMAVALIDATED

Member function. Returns the validation status of the `XMLType` instance -- tells if a schema based instance has been actually validated against its schema. Returns 1 if the instance has been validated against the schema, 0 otherwise.

Syntax

```
MEMBER FUNCTION isSchemaValidated
return NUMBER deterministic;
```

---

### SCHEMAVALIDATE

Member procedure. Validates the XML instance against its schema if it hasn't already been done. For non-schema based documents an error is raised. If validation fails an error is raised; else, the document's status is changed to validated.

Syntax

```
MEMBER PROCEDURE schemaValidate(
   self IF OUT NOCOPY XMLType);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `self` | `(OUT)` | XML instance being validated against the schema. |

---

### SETSCHEMAVALIDATED

Member function. Sets the `VALIDATION` state of the input XML instance.

Syntax

```
MEMBER PROCEDURE setSchemaValidated(
self IF OUT NOCOPY XMLType,
   flag IN BINARY_INTEGER := 1);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `self` | `(OUT)` | XML instance. |
| `flag` | `(IN)` | 0 - `NOT VALIDATED`; 1 - `VALIDATED` (Default) |

---

### TOOBJECT

Member procedure. Converts the XML value to an object type using the `XMLSCHEMA` mapping, if available. If a `SCHEMA` is not supplied or the input is a non-schema based XML, the procedure uses cannonical mapping between elements and object type attributes.

Syntax

```
MEMBER PROCEDURE toObject(
SELF in XMLType,
object OUT "<ADT_1>",
schema in varchar2 := NULL,
element in varchar2 := NULL);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `SELF` | `(IN)` | Instance to be converted. Implicit if used as a member procedure. |
| `object` | `(IN)` | Converted object. An object instance of the required type may be passed in to this function |
| `schema` | `(IN)` | Schema URL. The mapping of the `XMLType` instance to the converted object instance may be specified using a schema. |
| `element` | `(IN)` | Top-level element name. An XML Schema document does not specify the top-level element for a conforming XML instance document without this parameter. |

---

### TRANSFORM

Member function. This member function transforms the XML data using the XSL stylesheet argument and the top-level parameters passed as a string of name=value pairs. If any of the arguments other than the parammap is `NULL`, then a `NULL` is returned.

Syntax

```
MEMBER FUNCTION transform(
xsl IN XMLType,
parammap in varchar2 := NULL)
RETURN XMLType deterministic;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `xsl` | `(IN)` | The XSL stylesheet describing the transformation |
| `parammap` | `(IN)` | Top level parameters to the XSL - string of name=value pairs |

---

### XMLTYPE

`XMLType` constructor. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `constructor function XMLType(`  `   xmlData IN clob,`  `   schema IN varchar2 := NULL,`  `   validated IN number := 0,`  `   wellformed IN Number := 0)`  `return self as result deterministic;` | This constructor function creates an optionally schema-based `XMLType` instance using the specified schema and xml data parameters. |
| `constructor function XMLType(`  `   xmlData IN varchar2,`  `   schema IN varchar2 := NULL,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `return self as result deterministic;` | This constructor function creates an optionally schema-based `XMLType` instance using the specified schema and xml data parameters. |
| `constructor function XMLType (`  `   xmlData IN "w<ADT_1>",`  `   schema IN varchar2 := NULL,`  `   element IN varchar2 := NULL,`  `   validated IN number := 0)`  `return self as result deterministic;` | This constructor function creates an optionally schema-based `XMLType` instance from the specified object type parameter. |
| `constructor function XMLType(`  `   xmlData IN SYS_REFCURSOR,`  `   schema in varchar2 := NULL,`  `   element in varchar2 := NULL,`  `   validated in number := 0)`  `return self as result deterministic;` | This constructor function creates an optionally schema-based `XMLType` instance from the specified `REF CURSOR` parameter. |
| `constructor function XMLType(`  `   xmlData IN AnyData,`  `   schema IN varchar2 := NULL,`  `   element IN varchar2 := NULL,`  `   validated IN number := 0)`  `return self as result deterministic`  `   parallel_enable` | This constructor function creates an optionally schema-based `XMLType` instance from the specified `ANYDATA` parameter.If the `ANYDATA` instance contains an ADT, the `XMLType` returned is the same as would be returned for a call directly on the ADT. If the `ANYDATA` contains a scalar, the `XMLType` contains a leaf node with the scalar value. The element name for this node is taken from the optional element string if present, and is " `ANYDATA` " if it is not. |
| `constructor function XMLType(`  `   xmlData IN blob, csid IN number,`  `   schema IN varchar2 := NULL,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `return self as result deterministic` | This constructor function creates an optionally schema-based `XMLType` instance from the specified `BLOB` parameter. |
| `constructor function XMLType(`  `   xmlData IN bfile,`  `   csid IN number,`  `   schema IN varchar2 := NULL,`  `   validated IN number := 0,`  `   wellformed IN number := 0)`  `return self as result deterministic` | This constructor function creates an optionally schema-based `XMLType` instance from the specified `BFILE` parameter. |

| Parameter | Description |
| --- | --- |
| `xmlData` | The data in the form of a `BFILE`, `BLOB`, `CLOB`, `REF` s, `VARCHAR2` or object type. |
| `schema` | Optional Schema URL to be used to make the input conform to the given schema. |
| `validated` | Indicates that the instance is valid to the given XML Schema. |
| `wellformed` | Indicates that the input is well formed. If set, then the database would not do well formed check on the input instance. |
| `element` | Optional element name in the case of the `ADT_1` or `REF CURSOR` constructors. (Default is `NULL`) |
| `CSID` | The character set id of input XML data. |
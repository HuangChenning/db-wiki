---
title: Database URI TYPEs
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/t_dburi.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 246 Database URI TYPEs

Oracle supports the `UriType` family of types that can be used to store and query Uri-refs inside the database. The `UriType` itself is an abstract object type and the `HTTPURITYPE`, `XDBURITYPE` and `DBURITYPE` are subtypes of it.

You can create a `UriType` column and store instances of the `DBURITYPE, XDBURITYPE` or the `HTTPURITYPE` inside of it. You can also define your own subtypes of the `UriType` to handle different URL protocols.

Oracle also provides a `UriFactory` package that can be used as a factory method to automatically generate various instances of these `UriTypes` by scanning the prefix, such as `http://` or `/oradb`. You can also register your subtype and provide the prefix that you support. For instance, if you have written a subtype to handle the gopher protocol, you can register the prefix `gopher://` to be handled by your subtype. The `UriFactory` will then generate your subtype instance for any URL starting with that prefix.

This chapter contains the following topics:

---

## Summary of URITYPE Supertype Subprograms

The `UriType` is the abstract super type. It provides a standard set of functions to get the value pointed to by the URI. The actual implementation of the protocol must be defined by the subtypes of this type.

Instances of this type cannot be created directly. However, you can create columns of this type and store subtype instances in it, and also select from columns without knowing the instance of the URL stored.

Table 246-1 URITYPE Type Subprograms

| Method | Description |
| --- | --- |
| GETBLOB | Returns the `BLOB` located at the address specified by the URL. |
| GETCLOB | Returns the `CLOB` located at the address specified by the URL. |
| GETCONTENTTYPE | Returns the URL, in escaped format, stored inside the `UriType` instance. |
| GETEXTERNALURL | Returns the URL, in escaped format, stored inside the `UriType` instance. |
| GETURL | Returns the URL, in non-escaped format, stored inside the `UriType` instance. |
| GETXML | Returns the `XMLType` located at the address specified by the URL. |

---

### GETBLOB

This function returns the `BLOB` located at the address specified by the URL. This function can be overridden in the subtype instances. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getBlob()`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL. |
| `MEMBER FUNCTION getBlob(`  `   content OUT VARCHAR2)`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL and the content type. |
| `FUNCTION getBlob(`  `   csid IN NUMBER)`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL in the specified character set. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |
| `csid` | `(IN)` | Character set id of the document. Must be a valid Oracle id and greater than `0`; otherwise returns an error |

---

### GETCLOB

This function returns the `CLOB` located at the address specified by the URL. This function can be overridden in the subtype instances. This function returns either a permanent `CLOB` or a temporary `CLOB`. If a temporary `CLOB` is returned, it must be freed. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getClob()`  `RETURN clob;` | This function returns the `CLOB` located at the address specified by the URL. |
| `MEMBER FUNCTION getClob(`  `   content OUT VARCHAR2)`  `RETURN clob;` | This function returns the `CLOB` located at the address specified by the URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### GETCONTENTTYPE

This function returns the content type of the document pointed to by the URI. This function can be overridden in the subtype instances. This function returns the content type as `VARCHAR2`.

Syntax

```
MEMBER FUNCTION getContentType()
RETURN VARCHAR2;
```

---

### GETEXTERNALURL

This function returns the URL, in escaped format, stored inside the `UriType` instance. The subtype instances override this member function to provide additional semantics. For instance, the `HTTPURITYPE` function does not store the prefix `http://` in the URL itself. When generating the external URL, it appends the prefix and generates it. For this reason, use the `getExternalUrl` function or the `getUrl` function to get to the URL value instead of using the attribute present in the `UriType` instance.

Syntax

```
MEMBER FUNCTION getExternalUrl()
RETURN varchar2;
```

---

### GETURL

This function returns the URL, in non-escaped format, stored inside the `UriType` instance. The subtype instances override this member function to provide additional semantics. For instance, the `HTTPURITYPE` function does not store the prefix `http://` in the URL itself. When generating the external URL, it appends the prefix and generates it. For this reason, use the `getExternalUrl` function or the `getUrl` function to get to the URL value instead of using the attribute present in the `UriType` instance.

Syntax

```
MEMBER FUNCTION getUrl()
RETURN varchar2;
```

---

### GETXML

This function returns the `XMLType` located at the address specified by the URL. This function can be overridden in the subtype instances. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getXML()`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL. |
| `MEMBER FUNCTION getXML(`  `   content OUT VARCHAR2)`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

## Summary of HTTPURITYPE Subtype Subprograms

The `HTTPURITYPE` is a subtype of the `UriType` that provides support for the HTTP protocol. This uses the `UTL_HTTP` package underneath to access the HTTP URLs. Proxy and secure wallets are not supported in this release.

Table 246-2 HTTPURITYPE Type Subprorgams

| Method | Description |
| --- | --- |
| CREATEURI | Creates an instance of `HTTPURITYPE` from the given URI. |
| GETBLOB | Returns the `BLOB` located at the address specified by the URL. |
| GETCLOB | Returns the `CLOB` located at the address specified by the URL. |
| GETCONTENTTYPE | Returns the content type of the document pointed to by the URI. |
| GETEXTERNALURL | Returns the URL, in escaped format, stored inside the `UriType` instance. |
| GETURL | Returns the URL, in non-escaped format, stored inside the `UriType` instance. |
| GETXML | Returns the `XMLType` located at the address specified by the URL |
| HTTPURITYPE | Creates an instance of `HTTPURITYPE` from the given URI. |

---

### CREATEURI

This static function constructs a `HTTPURITYPE` instance. The `HTTPURITYPE` instance does not contain the prefix `http://` in the stored URL.

Syntax

```
STATIC FUNCTION createUri(
   url IN varchar2)
RETURN HTTPURITYPE;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string containing a valid HTTP URL; escaped format. |

---

### GETBLOB

This function returns the `BLOB` located at the address specified by the HTTP URL.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getBlob()`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the HTTP URL. |
| `MEMBER FUNCTION getBlob(`  `   content OUT VARCHAR2)`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the HTTP URL and the content type. |
| `FUNCTION getBlob(`  `   csid IN NUMBER)`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL in the specified character set. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |
| `csid` | `(IN)` | Character set id of the document. Must be a valid Oracle id and greater than `0`; otherwise returns an error. |

---

### GETCLOB

This function returns the `CLOB` located by the HTTP URL address. If a temporary `CLOB` is returned, it must be freed.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getClob()`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the HTTP URL. |
| `MEMBER FUNCTION getClob(`  `   content OUT VARCHAR2)`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the HTTP URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### GETCONTENTTYPE

Returns the content type of the document pointed to by the URI.

Syntax

```
MEMBER FUNCTION getContentType()
RETURN VARCHAR2;
```

---

### GETEXTERNALURL

This function returns the URL, in escaped format, stored inside the `HTTPURITYPE` instance. The subtype instances override this member function. The `HTTPURITYPE` function does not store the prefix `http://`, but generates it for the external URL.

Syntax

```
MEMBER FUNCTION getExternalUrl()
RETURN varchar2;
```

---

### GETURL

This function returns the URL, in non-escaped format, stored inside the `HTTPURITYPE` instance.

Syntax

```
MEMBER FUNCTION getUrl()
RETURN varchar2;
```

---

### GETXML

This function returns the `XMLType` located at the address specified by the URL. An error is thrown if the address does not point to a valid XML document.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getXML()`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL. |
| `MEMBER FUNCTION getXML(`  `   content OUT VARCHAR2)`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### HTTPURITYPE

This constructs a `HTTPURITYPE` instance. The `HTTPURITYPE` instance does not contain the prefix `http://` in the stored URL.

Syntax

```
CONSTRUCTOR FUNCTION HTTPURITYPE(
   url IN varchar2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string containing a valid HTTP URL. The URL string is expected in escaped format. For example, non-url characters are represented as the hexadecimal value for the UTF-8 encoding of those characters. |

---

## Summary of DBURITYPE Subtype Subprogams

The `DBURITYPE` is a subtype of the UriType that provides support for DBUri-refs. A DBUri-ref is an intra-database URL that can be used to reference any row or row-column data in the database. The URL is specified as an XPath expression over a XML visualization of the database. The schemas become elements which contain tables and views. These tables and view further contain the rows and columns inside them.

Table 246-3 DBURITYPE Type Subprograms

| Method | Description |
| --- | --- |
| CREATEURI | Constructs a `DBURITYPE` instance. |
| DBURITYPE | Creates an instance of `DBURITYPE` from the given URI. |
| GETBLOB | Returns the `BLOB` located at the address specified by the `DBURITYPE` instance. |
| GETCLOB | Returns the `CLOB` located at the address specified by the `DBURITYPE` instance. |
| GETCONTENTTYPE | Returns the content type of the document pointed to by the URI. |
| GETEXTERNALURL | Returns the URL, in escaped format, stored inside the `DBURITYPE` instance. |
| GETURL | Returns the URL, in non-escaped format, stored inside the `DBURITYPE` instance. |
| GETXML | Returns the `XMLType` located at the address specified by the URL |

---

### CREATEURI

This static function constructs a `DBURITYPE` instance. Parses the URL given and creates a `DBURITYPE` instance.

Syntax

```
STATIC FUNCTION createUri(
   url IN varchar2)
RETURN DBURITYPE;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string, in escaped format, containing a valid `DBURITYPE`. |

---

### DBURITYPE

This constructs a `DBURITYPE` instance.

Syntax

```
CONSTRUCTOR FUNCTION DBURITYPE(
   url IN varchar2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string containing a valid `DBURITYPE`. The URL string is expected in escaped format. For example, non-URL characters are represented as the hexadecimal value for the UTF-8 encoding of those characters. |

---

### GETBLOB

This function returns the `BLOB` located at the address specified by the URL. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getBlob()`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the URL. |
| `MEMBER FUNCTION getBlob(`  `   content OUT VARCHAR2)`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the URL and the content type. |
| `FUNCTION getBlob(`  `   csid IN NUMBER)`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL in the specified character set. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |
| `csid` | `(IN)` | Character set id of the document. Must be a valid Oracle id and greater than `0`; otherwise returns an error. |

---

### GETCLOB

This function returns the `CLOB` located at the address specified by the `DBURITYPE` instance. If a temporary `CLOB` is returned, it must be freed. The document returned may be an XML document or a text document. When the DBUri-ref identifies an element in the XPath, the result is a well-formed XML document. On the other hand, if it identifies a text node, then what is returned is only the text content of the column or attribute. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getClob()`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the `DBURITYPE` instance. |
| `MEMBER FUNCTION getClob(`  `   content OUT VARCHAR2)`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the `DBURITYPE` instance and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### GETCONTENTTYPE

This function returns the content type of the document pointed to by the URI.

Syntax

```
MEMBER FUNCTION getContentType()
RETURN VARCHAR2;
```

---

### GETEXTERNALURL

This function returns the URL, in escaped format, stored inside the `DBURITYPE` instance. The `DBUri` servlet URL that processes the `DBURITYPE` has to be appended before using the escaped URL in Web pages.

Syntax

```
MEMBER FUNCTION getExternalUrl()
RETURN varchar2;
```

---

### GETURL

This function returns the URL, in non-escaped format, stored inside the `DBURITYPE` instance.

Syntax

```
MEMBER FUNCTION getUrl()
RETURN varchar2;
```

---

### GETXML

This function returns the `XMLType` located at the address specified by the URL. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getXML()`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL. |
| `MEMBER FUNCTION getXML(`  `   content OUT VARCHAR2)`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

## Summary of XDBURITYPE Subtype Subprograms

`XDBURITYPE` is a new subtype of URIType. It provides a way to expose documents in the Oracle XML DB hierarchy as URIs that can be embedded in any URIType column in a table. The URL part of the URI is the hierarchical name of the XML document it refers to. The optional fragment part uses the XPath syntax, and is separated from the URL part by '#'. The more general XPointer syntax for specifying a fragment is not currently supported.

Table 246-4 XDBURITYPE Type Subprograms

| Method | Description |
| --- | --- |
| CREATEURI | Returns the `UriType` corresponding to the specified URL. |
| GETBLOB | Returns the `BLOB` corresponding to the contents of the document specified by the `XDBURITYPE` instance. |
| GETCLOB | Returns the `CLOB` corresponding to the contents of the document specified by the `XDBURITYPE` instance. |
| GETCONTENTTYPE | Returns the content type of the document pointed to by the URI. |
| GETEXTERNALURL | Returns the URL, in escaped format, stored inside the `XDBURITYPE` instance. |
| GETURL | Returns the URL, in non-escaped format, stored inside the `XDBURITYPE` instance. |
| GETXML | Returns the `XMLType` corresponding to the contents of the document specified by the URL. |
| XDBURITYPE | Creates an instance of `XDBURITYPE` from the given URI. |

---

### CREATEURI

This static function constructs a `XDBURITYPE` instance. Parses the URL given and creates a `XDBURITYPE` instance.

Syntax

```
STATIC FUNCTION createUri(
   url IN varchar2)
RETURN XDBURITYPE
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string, in escaped format, containing a valid `XDBURITYPE`. |

---

### GETBLOB

This function returns the `BLOB` located at the address specified by the `XDBURITYPE` instance. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getBlob()`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the URL. |
| `MEMBER FUNCTION getBlob(`  `   content OUT VARCHAR2)`  `RETURN blob;` | This function returns the `BLOB` located at the address specified by the URL and the content type. |
| `FUNCTION getBlob(`  `   csid IN NUMBER)`  `RETURN BLOB;` | This function returns the `BLOB` located at the address specified by the URL in the specified character set. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |
| `csid` | `(IN)` | Character set id of the document. Must be a valid Oracle id and greater than `0`; otherwise returns an error. |

---

### GETCLOB

This function returns the `CLOB` located at the address specified by the `XDBURITYPE` instance. If a temporary `CLOB` is returned, it must be freed. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getClob()`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the `XDBUriType` instance. |
| `MEMBER FUNCTION getClob(`  `   content OUT VARCHAR2)`  `RETURN clob;` | Returns the `CLOB` located at the address specified by the `XDBUriType` instance and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### GETCONTENTTYPE

This function returns the content type of the document pointed to by the URI. This function returns the content type as `VARCHAR2`.

Syntax

```
MEMBER FUNCTION getContentType()
RETURN VARCHAR2;
```

---

### GETEXTERNALURL

This function returns the URL, in escaped format, stored inside the `XDBURITYPE` instance.

Syntax

```
MEMBER FUNCTION getExternalUrl()
RETURN varchar2;
```

---

### GETURL

This function returns the URL, in non-escaped format, stored inside the `XDBURITYPE` instance.

Syntax

```
MEMBER FUNCTION getUrl()
RETURN varchar2;
```

---

### GETXML

This function returns the `XMLType` located at the address specified by the URL. The options are described in the following table.

| Syntax | Description |
| --- | --- |
| `MEMBER FUNCTION getXML()`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL. |
| `MEMBER FUNCTION getXML(`  `   content OUT VARCHAR2)`  `RETURN XMLType;` | This function returns the `XMLType` located at the address specified by the URL and the content type. |

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `content` | `(OUT)` | Content type of the document to which URI is pointing. |

---

### XDBURITYPE

This constructs a `XDBURITYPE` instance.

Syntax

```
CONSTRUCTOR FUNCTION XDBURITYPE(
   url     IN   VARCHAR2,
   flags   IN   RAW := NULL)
 RETURN self AS RESULT;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string containing a valid `XDBUriType`. The URL string is expected in escaped format. For example, non-URL characters are represented as the hexadecimal value for the UTF-8 encoding of those characters. |
| `flags` | `(IN)` | Possible values are: - `1` - Expand all `XInclude` elements before returning the result contents. If any `XInclude` element cannot be successfully resolved according to the `XInclude` fallback semantics, then an error is raised. - `2` - Indicates that any errors during document retrieval should be suppressed - `3` - Both flag bits (`1`, `2`) are enabled |

---

## Summary of URIFACTORY Package Subprograms

The `UriFactory` package contains factory methods that can be used to generate the appropriate instance of the URI types without having to hard code the implementation in the program.

The `UriFactory` package also provides the ability to register new subtypes of the `UriType` to handle various other protocols. For example, you can invent a new protocol `ecom://` and define a subtype of the `UriType` to handle that protocol and register it with `UriFactory`. After that any factory method would generate the new subtype instance if it sees the `ecom://` prefix.

Table 246-5 URIFACTORY Type Subprograms

| Method | Description |
| --- | --- |
| GETURI | Returns the correct URL handler for the given URL string. |
| ESCAPEURI | Returns a URL in escaped format. |
| UNESCAPEURI | Returns a URL in unescaped format. |
| REGISTERURLHANDLER | Registers a particular type name for handling a particular URL. |
| UNREGISTERURLHANDLER | Unregisters a URL handler. |

---

### GETURI

This factory method returns the correct URI handler for the given URI string. It returns a subtype instance of the `UriType` that can handle the protocol. By default, it always creates an `XDBURITYPE` instance, if it cannot resolve the URL. A URL handler can be registered for a particular prefix using the REGISTERURLHANDLER function. If the prefix matches, GETURI would then use that subtype.

Syntax

```
FUNCTION getUri(
   url IN Varchar2)
RETURN UriType;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `uri` | `(IN)` | The URL string, in escaped format, containing a valid HTTP URL. |

---

### ESCAPEURI

This function returns a URL in escaped format. The subtype instances override this member function to provide additional semantics. For instance, the `HTTPURITYPE` does not store the prefix `http://` in the URL itself. When generating the external URL, it appends the prefix and generates it. For this reason, use the GETEXTERNALURL function or the GETURI function to get to the URL value instead of using the attribute present in the `UriType`.

Syntax

```
MEMBER FUNCTION escapeUri()
RETURN varchar2;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string to be returned in escaped format. |

---

### UNESCAPEURI

This function returns a URL in unescaped format. This function is the reverse of the ESCAPEURI function. This function scans the string and converts any non-URL hexadecimal characters into the equivalent UTF-8 characters. Since the return type is a `VARCHAR2`, the characters would be converted into the equivalent characters as defined by the database character set.

Syntax

```
FUNCTION unescapeUri()
RETURN varchar2;
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `url` | `(IN)` | The URL string to be returned in unescaped format. |

---

### REGISTERURLHANDLER

Registers a particular type name for handling a particular URL. The type specified must be valid and must be a subtype of the `UriType` or one of its subtypes. It must also implement the `createUri` static member function. This function is called by the GETURI function to generate an instance of the type. The `stripprefix` parameter indicates that the prefix must be stripped off before calling this function.

Syntax

```
PROCEDURE registerUrlHandler(
   prefix IN varchar2,
   schemaName IN varchar2,
   typename IN varchar2,
   ignoreCase IN boolean := true,
   stripprefix IN boolean := true);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `prefix` | `(IN)` | The prefix to handle; for example, `http://`. |
| `schemaName` | `(IN)` | Name of the schema where the type resides; case sensitive. |
| `typename` | `(IN)` | The name of the type to handle the URL; case sensitive. |
| `ignoreCase` | `(IN)` | Ignore case when matching prefixes. |
| `stripprefix` | `(IN)` | Strip prefix before generating the instance of the type. |

---

### UNREGISTERURLHANDLER

This procedure unregisters a URL handler. This only unregisters user registered handler prefixes and not predefined system prefixes such as `http://.`

Syntax

```
PROCEDURE unregisterUrlHandler(
   prefix IN varchar2);
```

| Parameter | IN / OUT | Description |
| --- | --- | --- |
| `prefix` | `(IN)` | The prefix to be unregistered. |
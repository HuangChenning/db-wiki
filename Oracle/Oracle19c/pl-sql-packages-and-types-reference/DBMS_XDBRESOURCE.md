---
title: DBMS_XDBRESOURCE
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_XDBRESOURCE.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_XDBRESOURCE` package provides the interface to operate on the resource’s metadata and contents.

This chapter contains the following topics:

**See Also:** Oracle XML DB Developer’s Guide for examples of [“Using `DBMS_XDBRESOURCE` ”](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADXDB2580)

### DBMS\_XDBRESOURCE Overview

The `DBMS_XDBRESOURCE` package provides routines to get and set the resource’s metadata and contents. To take advantage of the DOM traversal facility, provided in `DBMS_XMLDOM` package, an `XDBResource` instance could be converted to a `DOMDocument` type by using `DBMS_XDBRESOURCE`.`MAKEDOCUMENT` routine.

### DBMS\_XDBRESOURCE Security Model

Owned by `XDB`, the `DBMS_XDBRESOURCE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### Summary of DBMS\_XDBRESOURCE Subprograms

This table lists the `DBMS_XDBRESOURCE` subprograms and briefly describes them.

Table 1 *DBMS\_XDBRESOURCE Package Subprograms*

| Subprogram | Description |
| --- | --- |
| FREERESOURCE Procedure | Frees any memory associated with an XDBResource |
| GETACL Function | Given an XDBResource, returns its ACL as string |
| GETACLDOCFROMRES Function | Returns the ACL Document for the given resource as `XMLType` |
| GETAUTHOR Function | Given an XDBResource, returns its author |
| GETCHARACTERSET Function | Given an XDBResource, returns its character set |
| GETCOMMENT Function | Given an XDBResource, returns its comment |
| GETCONTENTBLOB Function | Returns the contents of the resource as a `BLOB` |
| GETCONTENTCLOB Function | Returns the contents of the resource as a `CLOB` |
| GETCONTENTREF Function | Returns the contents of the resource as an `XMLTypeRef` |
| GETCONTENTTYPE Function | Given an XDBResource, returns its content-type |
| GETCONTENTXML Function | Returns the contents of the resource as XML |
| GETCONTENTVARCHAR2 Function | Returns the contents of the resource as a string |
| GETCREATIONDATE Function | Given an XDBResource, returns its creation date |
| GETCREATOR Function | Given an XDBResource, returns its creator |
| GETCUSTOMMETADATA Function | Returns the requested custom metadata given the xpath and namespace to the metadata |
| GETDISPLAYNAME Function | Given an XDBResource, returns its display name |
| GETLANGUAGE Function | Given an XDBResource, returns its language |
| GETLASTMODIFIER Function | Given an XDBResource, returns its last modifier |
| GETMODIFICATIONDATE Function | Given an XDBResource, returns its modification date |
| GETOWNER Function | Given an XDBResource, returns its owner. |
| GETREFCOUNT Function | Given an XDBResource, returns its reference count |
| GETVERSIONID Function | Given an XDBResource, returns its version ID. |
| HASACLCHANGED Function | Returns `TRUE` if the ACL of the given resource has changed, `FALSE` otherwise |
| HASAUTHORCHANGED Function | Returns `TRUE` if the ACL of the given resource has changed `FALSE` otherwise |
| HASCHANGED Function | Returns `TRUE` if the element or attribute represented by the given XPath has changed, `FALSE` otherwise |
| HASCHARACTERSETCHANGED Function | Returns `TRUE` if the character set of the given resource has changed, `FALSE` otherwise |
| HASCOMMENTCHANGED Function | Returns `TRUE` if the comment of the given resource has changed, `FALSE` otherwise |
| HASCONTENTCHANGED Function | Returns `TRUE` if the contents of the given resource has changed, `FALSE` otherwise |
| HASCONTENTTYPECHANGED Function | Returns `TRUE` if the content-type of the given resource has changed, `FALSE` otherwise |
| HASCREATIONDATECHANGED Function | Returns `TRUE` if the creation date of the given resource has changed, `FALSE` otherwise |
| HASCREATORCHANGED Function | Returns `TRUE` if the creator of the given resource has changed, `FALSE` otherwise |
| HASCUSTOMMETADATACHANGED Function | Returns `TRUE` if custom-metadata for this XPath has changed, `FALSE` otherwise |
| HASDISPLAYNAMECHANGED Function | Returns `TRUE` if the display name of the given resource has changed, `FALSE` otherwise |
| HASLANGUAGECHANGED Function | Returns `TRUE` if the language of the given resource has changed, `FALSE` otherwise |
| HASLASTMODIFIERCHANGED Function | Returns `TRUE` if the last modifier of the given resource has changed, `FALSE` otherwise |
| HASMODIFICATIONDATECHANGED Function | Returns `TRUE` if the modification date of the given resource has changed, `FALSE` otherwise |
| HASOWNERCHANGED Function | Returns `TRUE` if the owner of the given resource has changed, `FALSE` otherwise |
| HASREFCOUNTCHANGED Function | Returns `TRUE` if the reference count of the given resource has changed, `FALSE` otherwise |
| HASVERSIONIDCHANGED Function | Returns `TRUE` if the version ID of the given resource has changed, `FALSE` otherwise |
| ISFOLDER Function | Returns `TRUE` if the given resource is a folder, `FALSE` otherwise |
| ISNULL Function | Returns `TRUE` if input resource is `NULL`, `FALSE` otherwise |
| MAKEDOCUMENT Function | Converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface |
| SAVE Procedure | Updates the resource with any modifications |
| SETACL Procedure | Sets the ACL of the given XDBResource to the path specified |
| SETAUTHOR Procedure | Sets the author of the given XDBResource to the specified string |
| SETCHARACTERSET Procedure | Sets the character set of the given XDBResource to a specified character set |
| SETCOMMENT Procedure | Sets a comment associated with the given XDBResource |
| SETCONTENT Procedures | Replaces the contents of the given resource with the given `CLOB` |
| SETCONTENTTYPE Procedure | Sets the content-type of the given XDBResource |
| SETCUSTOMMETADATA Procedure | Sets the custom metadata specified by the XPath and namespace to new data |
| SETDISPLAYNAME Procedure | Sets the display name of the given XDBResource |
| SETLANGUAGE Procedure | Sets the language of the given XDBResource |
| SETOWNER Procedure | Sets the owner of the given XDBResource |

### FREERESOURCE Procedure

This procedure frees any memory associated with an XDBResource.

**Syntax**

```md
DBMS_XDBRESOURCE.FREERESOURCE (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 2 FREERESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource to free |

### GETACL Function

Given an XDBResource, this function returns its ACL as string.

**Syntax**

```md
DBMS_XDBRESOURCE.GETACL (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 3 GETACL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETACLDOCFROMRES Function

This function returns the ACL Document for the given resource as `XMLType`.

**Syntax**

```md
DBMS_XDBRESOURCE.GETACLDOCFROMRES (
   res   IN    XDBResource)
 RETURN SYS.XMLTYPE;
```

**Parameters**

Table 4 GETACLDOCFROMRES Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETAUTHOR Function

Given an XDBResource, this function returns its author.

**Syntax**

```md
DBMS_XDBRESOURCE.GETAUTHOR (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 5 GETAUTHOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCHARACTERSET Function

Given an XDBResource, this function returns its characterset.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCHARACTERSET (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 6 GETCHARACTERSET Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCOMMENT Function

Given an XDBResource, this function returns its comment.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCOMMENT (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 7 GETCOMMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCONTENTBLOB Function

This function returns the contents of the resource as a `BLOB`.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTBLOB (
   res    IN     XDBResource,
   csid   OUT    PLS_INTEGER)
 RETURN BLOB;
```

**Parameters**

Table 8 GETCONTENTBLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `csid` | Character set ID of the `BLOB` returned |

### GETCONTENTCLOB Function

This function returns the contents of the resource as a `CLOB`.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTCLOB (
   res   IN    XDBResource)
 RETURN CLOB;
```

**Parameters**

Table 9 GETCONTENTCLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCONTENTREF Function

This function returns the contents of the resource as an `XMLTypeRef`.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTREF (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 10 GETCONTENTREF Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCONTENTTYPE Function

Given an XDBResource, this function returns its content-type.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTTYPE (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 11 GETCONTENTTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCONTENTXML Function

This function returns the contents of the resource as an `XMLTypeRef`.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTXML (
   res   IN    XDBResource)
 RETURN XMLType;
```

**Parameters**

Table 12 GETCONTENTXML Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCONTENTVARCHAR2 Function

This function returns the contents of the resource as a string.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCONTENTVARCHAR2 (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 13 GETCONTENTVARCHAR2 Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCREATIONDATE Function

Given an XDBResource, this function returns its creation date.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCREATIONDATE (
   res   IN    XDBResource)
 RETURN TIMESTAMP;
```

**Parameters**

Table 14 GETCREATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCREATOR Function

Given an XDBResource, this function returns its creator.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCREATOR (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 15 GETCREATOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETCUSTOMMETADATA Function

This function returns the requested custom metadata given the xpath and namespace to the metadata.

**Syntax**

```md
DBMS_XDBRESOURCE.GETCUSTOMMETADATA (
   res        IN    XDBResource,
   xpath      IN    VARCHAR2,    namespace  IN    VARCHAR2)
 RETURN XMLType;
```

**Parameters**

Table 16 GETCUSTOMMETADATA Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath for custom metadata |
| `namespace` | Namespace |

**Usage Notes**

The first component of the XPath expression must be “Resource”.

### GETDISPLAYNAME Function

Given an XDBResource, this function returns its display name.

**Syntax**

```md
DBMS_XDBRESOURCE.GETDISPLAYNAME (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 17 GETDISPLAYNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETLANGUAGE Function

Given an XDBResource, this function returns its language.

**Syntax**

```md
DBMS_XDBRESOURCE.GETLANGUAGE (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 18 GETLANGUAGE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETLASTMODIFIER Function

Given an XDBResource, this function returns its last modifier.

**Syntax**

```md
DBMS_XDBRESOURCE.GETLASTMODIFIER (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 19 GETLASTMODIFIER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETMODIFICATIONDATE Function

Given an XDBResource, this function returns its modification date.

**Syntax**

```md
DBMS_XDBRESOURCE.GETMODIFICATIONDATE (
   res   IN    XDBResource)
 RETURN TIMESTAMP;
```

**Parameters**

Table 20 GETMODIFICATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETOWNER Function

Given an XDBResource, this function returns its owner.

**Syntax**

```md
DBMS_XDBRESOURCE.GETOWNER (
   res   IN    XDBResource)
 RETURN VARCHAR2;
```

**Parameters**

Table 21 GETOWNER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETREFCOUNT Function

Given an XDBResource, this function returns its reference count.

**Syntax**

```md
DBMS_XDBRESOURCE.GETREFCOUNT (
   res   IN    XDBResource)
 RETURN PLS_INTEGER;
```

**Parameters**

Table 22 GETREFCOUNT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### GETVERSIONID Function

Given an XDBResource, this function returns its version ID.

**Syntax**

```md
DBMS_XDBRESOURCE.GETVERSIONID (
   res   IN    XDBResource)
 RETURN PLS_INTEGER;
```

**Parameters**

Table 23 GETVERSIONID Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASACLCHANGED Function

This function returns `TRUE` if the ACL of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASACLCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 24 HASACLCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASAUTHORCHANGED Function

This function returns `TRUE` if the author of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASAUTHORCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 25 HASAUTHORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCHANGED Function

Given an XPath, this function determines whether the element or attribute represented by the XPath has changed.

**Syntax**

```md
DBMS_XDBRESOURCE.HASCHANGED (
   res         IN    XDBResource,
   xpath       IN    VARCHAR2,
   namespace   IN    VARCHAR2)
 RETURN BOOLEAN;
```

**Parameters**

Table 26 HASCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath to check |
| `bnamespace` | Namespace to use |

### HASCHARACTERSETCHANGED Function

This function returns `TRUE` if the character set of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASCHARACTERSETCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 27 HASCHARACTERSETCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCOMMENTCHANGED Function

This function returns `TRUE` if the comment of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASCOMMENTCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 28 HASCOMMENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCONTENTCHANGED Function

This function returns `TRUE` if the contents of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASCONTENTCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 29 HASCONTENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCONTENTTYPECHANGED Function

This function returns `TRUE` if the content-type of the given resource has changed, `FALSE` otherwise

**Syntax**

```md
DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 30 HASCONTENTTYPECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCREATIONDATECHANGED Function

This function returns `TRUE` if the creation date of the given resource has changed, `FALSE` otherwise

**Syntax**

```md
DBMS_XDBRESOURCE.HASCREATIONDATECHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 31 HASCREATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCREATORCHANGED Function

This function returns `TRUE` if the creator of the given resource has changed, `FALSE` otherwise

**Syntax**

```md
DBMS_XDBRESOURCE.HASCREATORCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 32 HASCREATORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASCUSTOMMETADATACHANGED Function

This function checks whether the custom-metadata for a given resource has changed.

**Syntax**

```md
DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 33 HASCUSTOMMETADATACHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASDISPLAYNAMECHANGED Function

This function returns `TRUE` if the display name of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASDISPLAYNAMECHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 34 HASDISPLAYNAMECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASLANGUAGECHANGED Function

This function returns `TRUE` if the language of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASLANGUAGECHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 35 HASLANGUAGECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASLASTMODIFIERCHANGED Function

This function returns `TRUE` if the last modifier of the given resource has changed, `FALSE` otherwise

**Syntax**

```md
DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 36 HASLASTMODIFIERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASMODIFICATIONDATECHANGED Function

This function returns `TRUE` if the modification date of the given resource has changed, `FALSE` otherwise

**Syntax**

```md
DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 37 HASMODIFICATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASOWNERCHANGED Function

This function returns `TRUE` if the owner of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASOWNERCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 38 HASOWNERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASREFCOUNTCHANGED Function

This function returns `TRUE` if the reference count of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASREFCOUNTCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 39 HASREFCOUNTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### HASVERSIONIDCHANGED Function

This function returns `TRUE` if the version ID of the given resource has changed, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.HASVERSIONIDCHANGED (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 40 HASVERSIONIDCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### ISFOLDER Function

This function returns `TRUE` if the given resource is a folder, `FALSE` otherwise.

**Syntax**

```md
DBMS_XDBRESOURCE.ISFOLDER (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 41 ISFOLDER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### ISNULL Function

This function returns `TRUE` if input resource is `NULL`.

**Syntax**

```md
DBMS_XDBRESOURCE.ISNULL (
   res   IN    XDBResource)
 RETURN BOOLEAN;
```

**Parameters**

Table 42 ISNULL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | Input resource |

### MAKEDOCUMENT Function

This function converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface.

**See Also:** The [DBMS\_XMLDOM](DBMS_XMLDOM.md) package

**Syntax**

```md
DBMS_XDBRESOURCE.MAKEDOCUMENT (
   res   IN    XDBResource)
 RETURN DBMS_XMLDOM.DOMDocument;
```

**Parameters**

Table 43 MAKEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### SAVE Procedure

This procedures updates the resource with any modifications.

**Syntax**

```md
DBMS_XDBRESOURCE.SAVE (
   res   IN    XDBResource);
```

**Parameters**

Table 44 SAVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

### SETACL Procedure

This procedure sets the ACL of the given XDBResource to the path specified.

**Syntax**

```md
DBMS_XDBRESOURCE.SETACL (
   res      IN OUT  XDBResource,
   ACLPath  IN      VARCHAR2);
```

**Parameters**

Table 45 SETACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `ACLPath` | Absolute path of the new ACL |

### SETAUTHOR Procedure

This procedure sets the author of the given XDBResource to the specified string.

**Syntax**

```md
DBMS_XDBRESOURCE.SETAUTHOR (
   res     IN OUT  XDBResource,
   author  IN      VARCHAR2);
```

**Parameters**

Table 46 SETAUTHOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `author` | Author |

### SETCHARACTERSET Procedure

This procedure sets the character set of the given XDBResource to a specified character set.

**Syntax**

```md
DBMS_XDBRESOURCE.SETCHARACTERSET (
   res      IN OUT  XDBResource,
   charSet  IN      VARCHAR2);
```

**Parameters**

Table 47 SETCHARACTERSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `charset` | New character set |

### SETCOMMENT Procedure

This procedure sets a comment associated with the given XDBResource.

**Syntax**

```md
DBMS_XDBRESOURCE.SETCOMMENT (
   res      IN OUT  XDBResource,
   comment  IN      VARCHAR2);
```

**Parameters**

Table 48 SETCOMMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `comment` | New comment |

### SETCONTENT Procedures

This procedure replaces the contents of the given resource with the given datatype.

**Syntax**

```md
DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      BFILE,
   csid     IN      NUMBER);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      BLOB,
   csid     IN      PLS_INTEGER);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      CLOB);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      REF SYS.XMLType,
   sticky   IN      BOOLEAN := TRUE);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      VARCHAR2);

DBMS_XDBRESOURCE.SETCONTENT (
   res      IN OUT  XDBResource,
   data     IN      SYS.XMLType);
```

**Parameters**

Table 49 SETCONTENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `data` | Data input as `BFILE`, `BLOB`, `CLOB`, string, `XMLType` |
| `csid` | Character set ID of the `BFILE`, `BLOB` |
| `sticky` | If `TRUE` creates a sticky `REF`, otherwise non-sticky |

### SETCONTENTTYPE Procedure

This procedure sets the content-type of the given XDBResource.

**Syntax**

```md
DBMS_XDBRESOURCE.SETCONTENTTYPE (
   res         IN OUT  XDBResource,
   conttype    IN      VARCHAR2);
```

**Parameters**

Table 50 SETCONTENTTYPE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `conttype` | New content-type |

### SETCUSTOMMETADATA Procedure

This procedure sets the custom metadata specified by the xpath and namespace to new data.

**Syntax**

```md
DBMS_XDBRESOURCE.SETCUSTOMMETADATA (
   res          IN OUT  XDBResource,
   xpath        IN      VARCHAR2,
   namespace    IN      VARCHAR2,
   newMetadata  IN      XMLType);
```

**Parameters**

Table 51 SETCUSTOMMETADATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath to change |
| `namespace` | Namespace to use |
| `newMetadata` | New data that should replace the metadata at the given XPath |

**Usage Notes**

The first component of the XPath expression must be “Resource”.

### SETDISPLAYNAME Procedure

This procedure sets the display name of the given XDBResource.

**Syntax**

```md
DBMS_XDBRESOURCE.SETDISPLAYNAME (
   res      IN OUT  XDBResource,
   name     IN      VARCHAR2);
```

**Parameters**

Table 52 SETDISPLAYNAME Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `name` | New display name |

### SETLANGUAGE Procedure

This procedure sets the language of the given `XDBResource`.

**Syntax**

```md
DBMS_XDBRESOURCE.SETLANGUAGE (
   res      IN OUT  XDBResource,
   ACLPath  IN      VARCHAR2);
```

**Parameters**

Table 53 SETLANGUAGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `ACLPath` | New path |

### SETOWNER Procedure

This procedure sets the owner of the given XDBResource.

**Syntax**

```md
DBMS_XDBRESOURCE.SETOWNER (
   res      IN OUT  XDBResource,
   owner    IN      VARCHAR2);
```

**Parameters**

Table 54 SETOWNER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `owner` | New owner |

**Usage Notes**

The user must have the `XDBADMIN` privilege to call this subprogram.
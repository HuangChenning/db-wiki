---
title: DBMS_XMLTRANSLATIONS
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xmltranslations.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 179 DBMS\_XMLTRANSLATIONS

The DBMS\_XMLTRANSLATIONS package provides an interface to perform translations so that strings can be searched or displayed in various languages.

See Also:

For more information, see the [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

This chapter contains the following sections:

- Using DBMS\_XMLTRANSLATIONS
	- Security Model
- Summary of DBMS\_XMLTRANSLATIONS Subprograms

---

## Using DBMS\_XMLTRANSLATIONS

- Security Model

---

### Security Model

Owned by `XDB`, the `DBMS_XMLTRANSLATIONS` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

## Summary of DBMS\_XMLTRANSLATIONS Subprograms

Table 179-1 DBMS\_XMLSTORE Package Subprograms

| Method | Description |
| --- | --- |
| DISABLETRANSLATION Procedure | Disables translations in the current session so that query or retrieval will take place on the base document ignoring session language values |
| ENABLETRANSLATION Procedure | Enables translations in the current session |
| EXTRACTXLIFF Function & Procedure | Extracts the translations in `XLIFF` format from either an `XMLTYPE` or a resource in the XDB Repository |
| GETBASEDOCUMENT Function | Returns the base document with all the translations |
| MERGEXLIFF Functions | Merges the translations in `XLIFF` format into either an `XMLTYPE` or a resource in the XDB Repository |
| SETSOURCELANG Function | Sets the source language to a particular language at the specified XPATH |
| TRANSLATEXML Function | Returns the document in the specified language |
| UPDATETRANSLATION Function | Updates the translation in a particular language at the specified `XPATH` |

---

### DISABLETRANSLATION Procedure

This procedure disables translations in the current session so that query or retrieval will take place on the base document ignoring session language values.

Syntax

```
DBMS_XMLTRANSLATIONS.DISABLETRANSLATION;
```

---

### ENABLETRANSLATION Procedure

This procedure enables translations in the current session. This is the default behavior.

Syntax

```
DBMS_XMLTRANSLATIONS.ENABLETRANSLATION;
```

---

### EXTRACTXLIFF Function & Procedure

This function and procedure extracts the translations in `XLIFF` format from either an `XMLTYPE` or a resource in the XDB Repository.

Syntax

```
DBMS_XMLTRANSLATIONS.EXTRACTXLIFF(
   doc       IN  XMLTYPE,
   xpath     IN  VARCHAR2,
   namespace IN  VARCHAR2 := NULL) 
 RETURN XMLTYPE;
```
```
DBMS_XMLTRANSLATIONS.EXTRACTXLIFF(
   abspath   IN  XMLTYPE,
   xpath     IN  VARCHAR2,
   namespace IN  VARCHAR2 := NULL) 
 RETURN XMLTYPE;
```

Parameters

Table 179-2 EXTRACTXLIFF Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `XMLTYPE` from which the `XLIFF` is to be extracted |
| `xpath` | `XPATH` at which specifies the location of the element that needs to be translated. If no `XPATH` is specified, the entire document is processed. |
| `namespace` | Namespace |
| `abspath` | Absolute path of the resource from which the `XLIFF` is to be extracted |

Return Values

The translations in the `XLIFF` format

Examples

Extracting the Translation from an XMLTYPE

Let doc =

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - FR
    </title>
    <title>
        Security Class Example - ES
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

Let the xpath = `'/securityClass/title'`. The output of `EXTRACTXLIFF` will be as follows:

```
<xliff version='1.1'>
  <file original='' source-language='en' datatype='xml'>
    <body>
      <trans-unit id='/securityClass/title'>
        <source>Security Class Example</source>
        <alt-trans>
          <target xml:lang='fr'>Security Class Example - FR</target>
          <target xml:lang='es'>Security Class Example - ES</target>
        </alt-trans>
      </trans-unit>
    </body>
  </file>
</xliff>
```

Extracting the Translation from a Resource

Let the resource ' `/public/security.xml'` =

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - ES
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
    <privlist>
    <privilege name="privilege1"/>
    <aggregatePrivilege name="iStorePOApprover">
        <title>
            iStore Purchase Order Approver
        </title>
        <privilegeRef name="is:privilege1"/>
        <privilegeRef name="oa:submitPO"/>
        <privilegeRef name="oa:privilege3"/>
    </aggregatePrivilege>
    <privilege name="privilege2">
        <title>
            secondary privilege
        </title>
        <title xdb:srclang="true">
            secondary privilege - FR
        </title>
        <columnRef schema="APPS" table="PurchaseOrder" column="POId"/>
        <columnRef schema="APPS" table="PurchaseOrder" column="Amount"/>
    </privilege>
    </privlist>
</securityClass>
```

And let `XPATH` = '', then the extracted `XLIFF` is

```
<xliff version='1.1'>
  <file original='/public/security.xml' source-language='en' datatype='xml'>
    <body>
      <trans-unit id='/securityClass/title'>
        <source>Security Class Example</source>
        <alt-trans>
          <target xml:lang='fr'>Security Class Example - FR</target>
          <target xml:lang='es'>Security Class Example - ES</target>
        </alt-trans>
      </trans-unit>
    </body>
  </file>
  <file original='/public/security.xml' source-language='fr' datatype='xml'>
    <body>
      <trans-unit id='/securityClass/privilege[@name="privilege2"/title'>
        <source>secondary privilege - FR</source>
        <alt-trans>
          <target xml:lang='en'>secondary privilege</target>
        </alt-trans>
      </trans-unit>
    </body>
  </file>
</xliff>
```

---

### GETBASEDOCUMENT Function

This function returns the base document with all the translations.

Syntax

```
DBMS_XMLTRANSLATIONS.GETBASEDOCUMENT(
   doc    IN  XMLTYPE)
 RETURN XMLTYPE;
```

Parameters

Table 179-3 GETBASEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | Input `XMLTYPE` |

Return Values

The `XMLTYPE` which contains the base document with all the translations

Examples

For example, for doc =

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

For the above document, this subprogram will return:

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

---

### MERGEXLIFF Functions

This function merges the translations in `XLIFF` format into either an `XMLTYPE` or a resource in the XDB Repository.

Syntax

```
DBMS_XMLTRANSLATIONS.MERGEXLIFF(
   doc       IN  XMLTYPE,
   xliff     IN  XMLTYPE)
 RETURN XMLTYPE;
```
```
DBMS_XMLTRANSLATIONS.MERGEXLIFF(
   xliff     IN  XMLTYPE);
```

Parameters

Table 179-4 MERGEXLIFF Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `XMLTYPE` from which the `XLIFF` is to be merged |
| `xliff` | Translations in the `XLIFF` format |

Return Values

The result of merging `'xliff'` into `'doc'` at `'xpath'`

Examples

Merge Translations into an XMLTYPE

Consider the following input `XMLTYPE`:

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - ES
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
    <privlist>
    <privilege name="privilege1"/>
    <aggregatePrivilege name="iStorePOApprover">
        <title>
            iStore Purchase Order Approver
        </title>
        <privilegeRef name="is:privilege1"/>
        <privilegeRef name="oa:submitPO"/>
        <privilegeRef name="oa:privilege3"/>
    </aggregatePrivilege>
    <privilege name="privilege2">
        <title>
            secondary privilege
        </title>
        <title xdb:srclang="true">
            secondary privilege - FR
        </title>
        <columnRef schema="APPS" table="PurchaseOrder" column="POId"/>
        <columnRef schema="APPS" table="PurchaseOrder" column="Amount"/>
    </privilege>
    </privlist>
</securityClass>
```

Let the input `XLIFF` be as follows:

```
<xliff version='1.1'>
  <file original='/public/security.xml' source-language='en' datatype='xml'>
    <body>
      <trans-unit id='/securityClass/title'>
        <source>Security Class Example Modified</source>
        <alt-trans>
          <target xml:lang='fr'>Security Class Example Mod - FR</target>
          <target xml:lang='es'>Security Class Example Mod - ES</target>
        </alt-trans>
      </trans-unit>
      <trans-unit id='/securityClass/privilege[@name="privilege2"/title'>
        <source>secondary privilege modified</source>
        <alt-trans>
          <target xml:lang='fr'>secondary privilege mod - FR</target>
        </alt-trans>
      </trans-unit>
    </body>
</xliff>
```

The output of merge will be as follows:

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example Modified
    </title>
    <title>
        Security Class Example Mod - ES
    </title>
    <title>
        Security Class Example Mod - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
    <privlist>
    <privilege name="privilege1"/>
    <aggregatePrivilege name="iStorePOApprover">
        <title>
            iStore Purchase Order Approver
        </title>
        <privilegeRef name="is:privilege1"/>
        <privilegeRef name="oa:submitPO"/>
        <privilegeRef name="oa:privilege3"/>
    </aggregatePrivilege>
    <privilege name="privilege2">
        <title xdb:srclang="true">
            secondary privilege modified
        </title>
        <title>
            secondary privilege mod - FR
        </title>
        <columnRef schema="APPS" table="PurchaseOrder" column="POId"/>
        <columnRef schema="APPS" table="PurchaseOrder" column="Amount"/>
    </privilege>
    </privlist>
</securityClass>
```

Merge XLIFF Translations into a Resource

If the input document in the above example were to be stored in the repository at `'/public/security.xml'`, then merging the above `XLIFF` will have the same effect.

---

### SETSOURCELANG Function

This function sets the source language to a particular language at the specified XPATH.

Syntax

```
DBMS_XMLTRANSLATIONS.SETSOURCELANG (
   doc       IN  XMLTYPE,
   xpath     IN  VARCHAR2,
   lang      IN  VARCHAR2, 
   namespace IN  VARCHAR2 := NULL) 
 RETURN XMLTYPE;
```

Parameters

Table 179-5 SETSOURCELANG Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `XMLTYPE` for which the source language is to be set |
| `xpath` | `XPATH` at which the source language is to be set |
| `lang` | Source language |
| `namespace` | Namespace |

Return Values

The updated document

Examples

For example, if doc =

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

the statement

```
setSourceLang ( doc, '/securityClass/title', 'fr' )
```

produces

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title>
        Security Class Example
    </title>
    <title xdb:srclang="true">
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

---

### TRANSLATEXML Function

This function returns the document in the specified language.

Syntax

```
DBMS_XMLTRANSLATIONS.TRANSLATEXML(
   doc    IN  XMLTYPE,
   lang   IN  VARCHAR2) 
 RETURN XMLTYPE;
```

Parameters

Table 179-6 TRANSLATEXML Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | Input `XMLTYPE` |
| `lang` | Language |

Return Values

The `XMLTYPE` which contains the document in the specified language

Examples

For example, for doc =

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

`TRANSLATEXML` (`doc`, ' `fr` ') will return:

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title>
        Security Class Example - FR
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```

---

### UPDATETRANSLATION Function

This function updates the translation in a particular language at the specified `XPATH`.

Syntax

```
DBMS_XMLTRANSLATIONS.UPDATETRANSLATION(
   doc       IN  XMLTYPE,
   xpath     IN  VARCHAR2,
   lang      IN  VARCHAR2, 
   value     IN  VARCHAR2,
   namespace IN  VARCHAR2 := NULL) 
 RETURN XMLTYPE;
```

Parameters

Table 179-7 UPDATETRANSLATION Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `XMLTYPE` for which the translation is to be updated |
| `xpath` | `XPATH` at which the translation is to be updated |
| `lang` | Language for which the translation is to be updated |
| `value` | New translation |
| `namespace` | Namespace |

Return Values

The updated document

Examples

For example,

```
updateTranslation ( doc, '/securityClass/title/text()', 'fr', 'Oracle' );
```

produces

```
<securityClass xmlns="http://xmlns.oracle.com/xdb/security.xsd"
               xmlns:is="xmlns.oracle.com/iStore"
               xmlns:oa="xmlns.oracle.com/OracleApps"
               targetNamespace="xmlns.oracle.com/example">
    <name>
        securityClassExample
    </name>
    <title xdb:srclang="true">
        Security Class Example
    </title>
    <title>
        Oracle
    </title>
    <inherits-from>is:iStorePurchaseOrder</inherits-from>
</securityClass>
```
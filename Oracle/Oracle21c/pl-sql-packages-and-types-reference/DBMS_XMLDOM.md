---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XMLDOM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 210 DBMS\_XMLDOM

The `DBMS_XMLDOM` package is used to access `XMLType` objects, and implements the Document Object Model (DOM), an application programming interface for HTML and XML documents.

This chapter contains the following topics:

See Also:

[Oracle XML Developer's Kit Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDK-GUID-48EA5544-C75E-43DF-BAC1-2740D7002F07)

### 210.1 DBMS\_XMLDOM Overview

The Document Object Model (DOM) is an application programming interface (API) for HTML and XML documents. It defines the logical structure of documents, and the manner in which they are accessed and manipulated

In the DOM specification, the term "document" is used in the broad sense. XML is being increasingly used to represent many different kinds of information that may be stored in diverse systems. This information has been traditionally be seen as "data"; nevertheless, XML presents this data as documents, and the `DBMS_XMLDOM` package allows you access to both schema-based and non schema-based documents.

Note:

Read-from and write-to files must be on the server file system.

With DOM, anything found in an HTML or XML document can be accessed, changed, deleted, or added using the Document Object Model, with a few exceptions. In particular, the DOM interfaces for the XML internal and external subsets have not yet been specified.

One important objective of the W3C DOM specification is to provide a standard programming interface that can be used in a wide variety of environments, programming languages, and applications. Because the DOM standard is object-oriented while PL/SQL is essentially a procedural language, some changes had to be made:

- Various DOM interfaces such as `Node`, `Element`, and others have equivalent PL/SQL types `DOMNode`, `DOMElement`, respectively.
- Various `DOMException` codes such as `WRONG_DOCUMENT_ERR`, `HIERARCHY_REQUEST_ERR`, and others, have similarly named PL/SQL exceptions.
- Various DOM Node type codes such as `ELEMENT_NODE`, `ATTRIBUTE_NODE`, and others, have similarly named PL/SQL constants.
- Subprograms defined on a DOM type become functions or procedures that accept it as a parameter. For example, to perform APPENDCHILD Function on a `DOMNode` `n`, the APPENDCHILD Function PL/SQL function is provided.
- To perform `setAttribute` on a `DOMElement elem` SETATTRIBUTE Procedures, use PL/SQL procedure.

DOM defines an inheritance hierarchy. For example, `Document`, `Element`, and `Attr` are defined to be subtypes of `Node` (see Figure 210-1). Thus, a method defined in the `Node` interface should be available in these as well. Since such inheritance is not supported in PL/SQL, it is implemented through direct invocation of the `MAKENODE` function. Calling `MAKENODE` on various DOM types converts these types into a `DOMNode`. The appropriate functions or procedures that accept `DOMNode` s can then be called to operate on these types. If, subsequently, type specific functionality is desired, the `DOMNode` can be converted back into the original type by the ` make` `XXX` functions, where `DOM` `XXX` is the desired DOM type.

Figure 210-1 Inheritance Diagram for DOM Types

![Figure 210-1 Inheritance Diagram for DOM Types](img/arpls010.gif)

> This figure provides a graphical representation of inheritance-type relationship between DOM types; methods defined on the supertype should be available on the subtype.
>
> Description of the inheritance structure follows:
>
> 1. Attr, CharacterData, Document, DocumentFragment, DocumentType, Element, Entity, EntityReference, Notation, and ProcessingInstruction are all subtypes of Node
> 2. Text is a subtype of CharacterData
> 3. CDATASection and Comment are subtypes of Text


The implementation of this interface follows the REC-DOM-Level-1-19981001.

### 210.2 DBMS\_XMLDOM Security Model

Owned by `XDB`, the `DBMS_XMLDOM` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`.

Subprograms in this package are executed using the privileges of the current user.

### 210.3 DBMS\_XMLDOM Constants

The `DBMS_XMLDOM` package defines several constants that can be used for specifying parameter values.

These constants are listed in the following table.

Table 210-1 Defined Constants for DBMS\_XMLDOM

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `ELEMENT_NODE` | `PLS_INTEGER` | 1 | The Node is an Element. |
| `ATTRIBUTE_NODE` | `PLS_INTEGER` | 2 | The Node is an Attribute. |
| `TEXT_NODE` | `PLS_INTEGER` | 3 | The Node is a Text node. |
| `CDATA_SECTION_NODE` | `PLS_INTEGER` | 4 | The Node is a CDataSection. |
| `ENTITY_REFERENCE_NODE` | `PLS_INTEGER` | 5 | The Node is an Entity Reference. |
| `ENTITY_NODE` | `PLS_INTEGER` | 6 | The Node is an Entity. |
| `PROCESSING_INSTRUCTION_NODE` | `PLS_INTEGER` | 7 | The Node is a Processing Instruction. |
| `COMMENT_NODE` | `PLS_INTEGER` | 8 | The Node is a Comment. |
| `DOCUMENT_NODE` | `PLS_INTEGER` | 9 | The Node is a Document. |
| `DOCUMENT_TYPE_NODE` | `PLS_INTEGER` | 10 | The Node is a Document Type Definition. |
| `DOCUMENT_FRAGMENT_NODE` | `PLS_INTEGER` | 11 | The Node is a Document fragment. |
| `NOTATION_NODE` | `PLS_INTEGER` | 12 | The Node is a Notation. |

### 210.4 DBMS\_XMLDOM Types

This table lists and briefly describes the types for the `DBMS_XMLDOM.DOMTYPE` package.

Table 210-2 XDB\_XMLDOM Types

| Type | Description |
| --- | --- |
| `DOMATTR ` | Implements the DOM Attribute interface. |
| `DOMCDATASECTION ` | Implements the DOM CDataSection interface. |
| `DOMCHARACTERDATA ` | Implements the DOM Character Data interface. |
| `DOMCOMMENT ` | Implements the DOM Comment interface. |
| `DOMDOCUMENT ` | Implements the DOM Document interface. |
| `DOMDOCUMENTFRAGMENT ` | Implements the DOM DocumentFragment interface. |
| `DOMDOCUMENTTYPE ` | Implements the DOM Document Type interface. |
| `DOMELEMENT ` | Implements the DOM Element interface. |
| `DOMENTITY ` | Implements the DOM Entity interface. |
| `DOMENTITYREFERENCE ` | Implements the DOM EntityReference interface. |
| `DOMIMPLEMENTATION ` | Implements the DOM Implementation interface. |
| `DOMNAMEDNODEMAP ` | Implements the DOM Named Node Map interface. |
| `DOMNODE ` | Implements the DOM Node interface. |
| `DOMNODELIST ` | Implements the DOM NodeList interface. |
| `DOMNOTATION ` | Implements the DOM Notation interface. |
| `DOMPROCESSINGINSTRUCTION` | Implements the DOM Processing instruction interface. |
| `DOMTEXT ` | Implements the DOM Text interface. |

### 210.5 DBMS\_XMLDOM Exceptions

`DBMS_XMLDOM` generates an exception when it encounters an issue.

This table lists the exceptions defined for `DBMS_XMLDOM`:

Table 210-3 Exceptions for DBMS\_XMLDOM

| Exception | Description |
| --- | --- |
| `DOMSTRING_SIZE_ERR` | If the specified range of text does not fit into a `DOMString`. |
| `HIERARCHY_REQUEST_ERR` | If any node is inserted somewhere it doesn't belong. |
| `INDEX_SIZE_ERR` | If index or size is negative, or greater than the allowed value. |
| `INUSE_ATTRIBUTE_ERR` | If an attempt is made to add an attribute that is already in use elsewhere. |
| `INVALID_CHARACTER_ERR` | If an invalid or illegal character is specified, such as in a name. See production 2 in the XML specification for the definition of a legal character, and production 5 for the definition of a legal name character. |
| `NO_DATA_ALLOWED_ERROR` | If data is specified for a node that does not support data. |
| `NOT_FOUND_ERR` | If an attempt is made to reference a node in a context where it does not exist. |
| `NO_MODIFICATION_ALLOWED_ERR` | If an attempt is made to modify an object where modifications are not allowed. |
| `NOT_SUPPORTED_ERR` | If the implementation does not support the requested type of object or operation. |
| `WRONG_DOCUMENT_ERR` | If a node is used in a different document than the one that created it (that doesn't support it). |

### 210.6 DBMS\_XMLDOM Subprogram Groups

`DBMS_XMLDOM` subprograms are divided into groups according to W3C Interfaces.

- DOMNode Subprograms
- DOMAttr Subprograms
- DOMCDataSection Subprograms
- DOMCharacterData Subprograms
- DOMComment Subprograms
- DOMDocument Subprograms
- DOMDocumentFragment Subprograms
- DOMDocumentType Subprograms
- DOMElement Subprograms
- DOMEntity Subprograms
- DOMEntityReference Subprograms
- DOMImplementation Subprograms
- DOMNamedNodeMap Subprograms
- DOMNodeList Subprograms
- DOMNotation Subprograms
- DOMProcessingInstruction Subprograms
- DOMText Subprograms

#### 210.6.1 DBMS\_XMLDOM DOMNode Subprograms

This table lists and briefly describes the `DOMNode` subprograms of `DBMS_XMLDOM`.

Table 210-4 Summary of DOMNode Subprograms; DBMS\_XMLDOM

| Subprogram | Description |
| --- | --- |
| ADOPTNODE Function | Adopts a node from another document |
| APPENDCHILD Function | Appends a new child to the node |
| CLONENODE Function | Clones the node |
| FREENODE Procedure | Frees all resources associated with the node |
| GETATTRIBUTES Function | Retrieves the attributes of the node |
| GETCHILDNODES Function | Retrieves the children of the node |
| GETEXPANDEDNAME Procedure and Functions | Retrieves the expanded name of the node |
| GETFIRSTCHILD Function | Retrieves the first child of the node |
| GETLASTCHILD Function | Retrieves the last child of the node |
| GETLOCALNAME Procedure and Functions | Retrieves the local part of the qualified name |
| GETNAMESPACE Procedure and Functions | Retrieves the node's namespace URI |
| GETNEXTSIBLING Function | Retrieves the next sibling of the node |
| GETNODENAME Function | Retrieves the Name of the Node |
| GETNODETYPE Function | Retrieves the Type of the node |
| GETNODEVALUE Function | Retrieves the Value of the Node |
| GETNODEVALUEASBINARYSTREAM Function & Procedure | Retrieves Node Value as binary stream |
| GETNODEVALUEASCHARACTERSTREAM Function & Procedure | Retrieves Node Value as character stream |
| GETOWNERDOCUMENT Function | Retrieves the owner document of the node |
| GETPARENTNODE Function | Retrieves the parent of this node |
| GETPREFIX Function | Retrieves the namespace prefix |
| GETPREVIOUSSIBLING Function | Retrieves the previous sibling of the node |
| GETSCHEMANODE Function | Retrieves the associated schema URI |
| HASATTRIBUTES Function | Tests if the node has attributes |
| HASCHILDNODES Function | Tests if the node has child nodes |
| IMPORTNODE Function | Imports a node from another document |
| INSERTBEFORE Function | Inserts a child before the reference child |
| ISNULL Functions | Tests if the node is `NULL` |
| MAKEATTR Function | Casts the node to an Attribute |
| MAKECDATASECTION Function | Casts the node to a CData Section |
| MAKECHARACTERDATA Function | Casts the node to Character Data |
| MAKECOMMENT Function | Casts the node to a Comment |
| MAKEDOCUMENT Function | Casts the node to a DOM Document |
| MAKEDOCUMENTFRAGMENT Function | Casts the node to a DOM Document Fragment |
| MAKEDOCUMENTTYPE Function | Casts the node to a DOM Document Type |
| MAKEELEMENT Function | Casts the node to a DOM Element |
| MAKEENTITY Function | Casts the node to a DOM Entity |
| MAKEENTITYREFERENCE Function | Casts the node to a DOM Entity Reference |
| MAKENOTATION Function | Casts the node to a DOM Notation |
| MAKEPROCESSINGINSTRUCTION Function | Casts the node to a DOM Processing Instruction |
| MAKETEXT Function | Casts the node to a DOM Text |
| REMOVECHILD Function | Removes a specified child from a node |
| REPLACECHILD Function | Replaces the old child with a new child |
| SETNODEVALUE Procedure | Sets the Value of the node |
| SETNODEVALUEASBINARYSTREAM Function & Procedure | Sets the Node Value as binary stream |
| SETNODEVALUEASCHARACTERSTREAM Function & Procedure | Sets the Node Value as a character stream |
| SETPREFIX Procedure | Sets the namespace prefix |
| USEBINARYSTREAM Function | Establishes that the stream is valid |
| WRITETOBUFFER Procedures | Writes the contents of the node to a buffer |
| WRITETOCLOB Procedures | Writes the contents of the node to a `CLOB` |
| WRITETOFILE Procedures | Writes the contents of the node to a file |

#### 210.6.2 DBMS\_XMLDOM DOMAttr Subprograms

This table lists the DOMAttr subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-5 Summary of DOMAttr Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| GETEXPANDEDNAME Procedure and Functions | Retrieves the expanded name of the attribute |
| GETLOCALNAME Procedure and Functions | Retrieves the local name of the attribute |
| GETNAME Functions | Retrieves the name of the attribute |
| GETNAMESPACE Procedure and Functions | Retrieves the NS URI of the attribute |
| GETOWNERELEMENT Function | Retrieves the Element node, parent of the attribute |
| GETQUALIFIEDNAME Functions | Retrieves the Qualified Name of the attribute |
| GETSPECIFIED Function | Tests if attribute was specified in the element |
| GETVALUE Function | Retrieves the value of the attribute |
| ISNULL Functions | Tests if the Attribute node is `NULL` |
| MAKENODE Functions | Casts the Attribute to a node |
| SETVALUE Procedure | Sets the value of the attribute |

#### 210.6.3 DBMS\_XMLDOM DOMCDataSection Subprograms

This table lists the DOMCdata subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-6 Summary of DOMCdata Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| ISNULL Functions | Tests if the `CDataSection` is `NULL` |
| MAKENODE Functions | Casts the `CDatasection` to a node |

#### 210.6.4 DBMS\_XMLDOM DOMCharacterData Subprograms

This table lists the DOMCharacterData subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-7 Summary of DOMCharacterData Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| APPENDDATA Procedure | Appends the specified data to the node data |
| DELETEDATA Procedure | Deletes the data from the specified offSets |
| GETDATA Functions | Retrieves the data of the node |
| GETLENGTH Functions | Retrieves the length of the data |
| INSERTDATA Procedure | Inserts the data in the node at the specified offSets |
| ISNULL Functions | Tests if the CharacterData is `NULL` |
| MAKENODE Functions | Casts the CharacterData to a node |
| REPLACEDATA Procedure | Changes a range of characters in the node |
| SETDATA Procedures | Sets the data to the node |
| SUBSTRINGDATA Function | Retrieves the substring of the data |

#### 210.6.5 DBMS\_XMLDOM DOMComment Subprograms

The table lists the DOMComment subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-8 Summary of DOMComment Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| ISNULL Functions | Tests if the comment is `NULL` |
| MAKENODE Functions | Casts the Comment to a node |

#### 210.6.6 DBMS\_XMLDOM DOMDocument Subprograms

This table lists the DOMDocument subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-9 Summary of DOMDocument Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| CREATEATTRIBUTE Functions | Creates an Attribute |
| CREATECDATASECTION Function | Creates a ` CDataSection` node |
| CREATECOMMENT Function | Creates a Comment node |
| CREATEDOCUMENT Function | Creates a new Document |
| CREATEDOCUMENTFRAGMENT Function | Creates a new Document Fragment |
| CREATEELEMENT Functions | Creates a new Element |
| CREATEENTITYREFERENCE Function | Creates an Entity reference |
| CREATEPROCESSINGINSTRUCTION Function | Creates a Processing Instruction |
| CREATETEXTNODE Function | Creates a Text node |
| FREEDOCFRAG Procedure | Frees the document fragment |
| FREEDOCUMENT Procedure | Frees the document |
| GETCHARSET Function | Retrieves the characterset of the `DOM` document |
| GETDOCTYPE Function | Retrieves the DTD of the document |
| GETDOCUMENTELEMENT Function | Retrieves the root element of the document |
| GETELEMENTSBYTAGNAME Functions | Retrieves  - the elements in the DOMNODELIST by tag name - elements in the subtree of a DOMNODELIST by tagname |
| GETIMPLEMENTATION Function | Retrieves the DOM implementation |
| GETSTANDALONE Function | Retrieves the standalone property of the document |
| GETVERSION Function | Retrieves the version of the document |
| GETXMLTYPE Function | Retrieves the `XMLType` associated with the DOM Document |
| ISNULL Functions | Tests if the document is `NULL` |
| MAKENODE Functions | Casts the document to a node |
| NEWDOMDOCUMENT Functions | Creates a new document |
| SETCHARSET Procedure | Sets the characterset of the `DOM` document |
| SETDOCTYPE Procedure | Sets the DTD of the document |
| SETSTANDALONE Procedure | Sets the standalone property of the document |
| SETVERSION Procedure | Sets the version of the document |
| WRITETOBUFFER Procedures | Writes the document to a buffer |
| WRITETOCLOB Procedures | Writes the document to a `CLOB` |
| WRITETOFILE Procedures | Writes the document to a file |

#### 210.6.7 DBMS\_XMLDOM DOMDocumentFragment Subprograms

This table lists the DOMDocumentFragment subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-10 Summary of DOMDocumentFragment Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| FREEDOCFRAG Procedure | Frees the specified document fragment |
| ISNULL Functions | Tests if the DocumentFragment is `NULL` |
| MAKENODE Functions | Casts the Document Fragment to a node |
| WRITETOBUFFER Procedures | Writes the contents of a document fragment into a buffer |

#### 210.6.8 DBMS\_XMLDOM DOMDocumentType Subprograms

This table lists the DOMDocumentType subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-11 Summary of DOMDocumentType Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| FINDENTITY Function | Finds the specified entity in the document type |
| FINDNOTATION Function | Finds the specified notation in the document type |
| GETENTITIES Function | Retrieves the nodemap of entities in the Document type |
| GETNAME Functions | Retrieves the name of the Document type |
| GETNOTATIONS Function | Retrieves the nodemap of the notations in the Document type |
| GETPUBLICID Functions | Retrieves the public ID of the document type |
| GETSYSTEMID Functions | Retrieves the system ID of the document type |
| ISNULL Functions | Tests if the Document Type is ` NULL` |
| MAKENODE Functions | Casts the document type to a node |

#### 210.6.9 DBMS\_XMLDOM DOMElement Subprograms

This table lists the DOMElement subprograms of DBMS\_XMLDOM in alphabetical order and briefly describes them.

Table 210-12 Summary of DOMElement Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| FREEELEMENT Procedure | Frees memory allocated to a DOMElement handle |
| GETATTRIBUTE Functions | Retrieves the attribute node by name |
| GETATTRIBUTENODE Functions | Retrieves the attribute node by name |
| GETCHILDRENBYTAGNAME Functions | Retrieves children of the element by tag name |
| GETELEMENTSBYTAGNAME Functions | Retrieves  - the elements in the DOMNODELIST by tag name - elements in the subtree of a DOMNODELIST by tagname |
| GETEXPANDEDNAME Procedure and Functions | Retrieves the expanded name of the element |
| GETLOCALNAME Procedure and Functions | Retrieves the local name of the element |
| GETNAMESPACE Procedure and Functions | Retrieves the NS URI of the element |
| GETQUALIFIEDNAME Functions | Retrieves the qualified name of the element |
| GETTAGNAME Function | Retrieves the Tag name of the element |
| HASATTRIBUTE Functions | Tests if an attribute exists |
| ISNULL Functions | Tests if the Element is `NULL` |
| MAKENODE Functions | Casts the Element to a node |
| NORMALIZE Procedure | Normalizes the text children of the element |
| REMOVEATTRIBUTE Procedures | Removes the attribute specified by the name |
| REMOVEATTRIBUTENODE Function | Removes the attribute node in the element |
| RESOLVENAMESPACEPREFIX Function | Resolve the prefix to a namespace URI |
| SETATTRIBUTE Procedures | Sets the attribute specified by the name |
| SETATTRIBUTENODE Functions | Sets the attribute node in the element |

#### 210.6.10 DBMS\_XMLDOM DOMEntity Subprograms

This table lists and briefly describes the `DOMEntity` subprograms of `DBMS_XMLDOM`.

Table 210-13 Summary of DOMEntity Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| GETNOTATIONNAME Function | Retrieves the notation name of the entity |
| GETPUBLICID Functions | Retrieves the public Id of the entity |
| GETSYSTEMID Functions | Retrieves the system Id of the entity |
| ISNULL Functions | Tests if the Entity is `NULL` |
| MAKENODE Functions | Casts the Entity to a node |

#### 210.6.11 DBMS\_XMLDOM DOMEntityReference Subprograms

This table lists and briefly describes the `DOMEntityReference` subprograms of `DBMS_XMLDOM`.

Table 210-14 Summary of DOMEntityReference Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| ISNULL Functions | Tests if the `DOMEntityReference` is `NULL` |
| MAKENODE Functions | Casts the `DOMEntityReference` to `NULL` |

#### 210.6.12 DBMS\_XMLDOM DOMImplementation Subprograms

This table lists and briefly describes the `DOMImplementation` subprograms of `DBMS_XMLDOM`.

Table 210-15 Summary of DOMImplementation Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| ISNULL Functions | Tests if the `DOMImplementation` node is `NULL` |
| HASFEATURE Function | Tests if the `DOMImplementation` implements a feature |

#### 210.6.13 DBMS\_XMLDOM DOMNamedNodeMap Subprograms

This table lists and briefly describes the `DOMNamedNodeMap` subprograms of `DBMS_XMLDOM`.

Table 210-16 Summary of DOMNamedNodeMap Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| GETLENGTH Functions | Retrieves the number of items in the map |
| GETNAMEDITEM Function | Retrieves the item specified by the name |
| ISNULL Functions | Tests if the `NamedNodeMap` is `NULL` |
| ITEM Functions | Retrieves the item given the index in the map |
| REMOVENAMEDITEM Function | Removes the item specified by name |
| SETNAMEDITEM Function | Sets the item in the map specified by the name |

#### 210.6.14 DBMS\_XMLDOM DOMNodeList Subprograms

This table lists and briefly describes the `DOMNodeList` subprograms of `DBMS_XMLDOM`.

Table 210-17 Summary of DOMNodeList Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| FREENODELIST Procedure | Frees all resources associated with a nodelist |
| GETLENGTH Functions | Retrieves the number of items in the list |
| ISNULL Functions | Tests if the ` NodeList` is `NULL` |
| ITEM Functions | Retrieves the item given the index in the list |

#### 210.6.15 DBMS\_XMLDOM DOMNotation Subprograms

This table lists and briefly describes the `DOMNotation` subprograms of `DBMS_XMLDOM`.

Table 210-18 Summary of DOMNotation Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| GETPUBLICID Functions | Retrieves the public Id of the notation |
| GETSYSTEMID Functions | Retrieves the system Id of the notation |
| ISNULL Functions | Tests if the Notation is `NULL` |
| MAKENODE Functions | Casts the notation to a node |

#### 210.6.16 DBMS\_XMLDOM DOMProcessingInstruction Subprograms

This table lists and briefly describes the `DOMProcessingInstruction` subprograms of `DBMS_XMLDOM`.

Table 210-19 Summary of DOMProcessingInstruction Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| GETDATA Functions | Retrieves the data of the processing instruction |
| GETTARGET Function | Retrieves the target of the processing instruction |
| ISNULL Functions | Tests if the Processing Instruction is `NULL` |
| MAKENODE Functions | Casts the Processing Instruction to a node |
| SETDATA Procedures | Sets the data of the processing instruction |

#### 210.6.17 DBMS\_XMLDOM DOMText Subprograms

This table lists and briefly describes the `DOMText` subprograms of `DBMS_XMLDOM`.

Table 210-20 Summary of DOMText Subprograms; DBMS\_XMLDOM

| Method | Description |
| --- | --- |
| ISNULL Functions | Tests if the text is `NULL` |
| MAKENODE Functions | Casts the text to a node |
| SPLITTEXT Function | Splits the contents of the text node into 2 text nodes |

### 210.7 Summary of DBMS\_XMLDOM Subprograms

This table lists the DBMS\_XMLDOM subprograms and briefly describes them.

Table 210-21 Summary of DBMS\_XMLDOM Package Subprogram

| Subprogram | Description | Group |
| --- | --- | --- |
| ADOPTNODE Function | Adopts a node from another document | DOMNode Subprograms |
| APPENDCHILD Function | Appends a new child to the node | DOMNode Subprograms |
| APPENDDATA Procedure | Appends the specified data to the node data | DOMCharacterData Subprograms |
| CLONENODE Function | Clones the node | DOMNode Subprograms |
| CREATEATTRIBUTE Functions | Creates an Attribute | DOMDocument Subprograms |
| CREATECDATASECTION Function | Creates a ` CDataSection` node | DOMDocument Subprograms |
| CREATECOMMENT Function | Creates a Comment node | DOMDocument Subprograms |
| CREATEDOCUMENT Function | Creates a new Document | DOMDocument Subprograms |
| CREATEDOCUMENTFRAGMENT Function | Creates a new Document Fragment | DOMDocument Subprograms |
| CREATEELEMENT Functions | Creates a new Element | DOMDocument Subprograms |
| CREATEENTITYREFERENCE Function | Creates an Entity reference | DOMDocument Subprograms |
| CREATEPROCESSINGINSTRUCTION Function | Creates a Processing Instruction | DOMDocument Subprograms |
| CREATETEXTNODE Function | Creates a Text node | DOMDocument Subprograms |
| DELETEDATA Procedure | Deletes the data from the specified offSets | DOMCharacterData Subprograms |
| FINDENTITY Function | Finds the specified entity in the document type | DOMDocumentType Subprograms |
| FINDNOTATION Function | Finds the specified notation in the document type | DOMDocumentType Subprograms |
| FREEDOCFRAG Procedure | Frees the document fragment | DOMDocument Subprograms and DOMDocumentFragment Subprograms |
| FREEDOCUMENT Procedure | Frees the document | DOMDocument Subprograms |
| FREEELEMENT Procedure | Frees memory allocated to a DOMElement handle | DOMElement Subprograms |
| FREENODE Procedure | Frees all resources associated with the node | DOMNode Subprograms |
| FREENODELIST Procedure | Frees all resources associated with a nodelist | DOMNodeList Subprograms |
| GETATTRIBUTE Functions | Retrieves the attribute node by name | DOMElement Subprograms |
| GETATTRIBUTENODE Functions | Retrieves the attribute node by name | DOMElement Subprograms |
| GETATTRIBUTES Function | Retrieves the attributes of the node | DOMNode Subprograms |
| GETCHARSET Function | Retrieves the characterset of the `DOM` document | DOMDocument Subprograms |
| GETCHILDNODES Function | Retrieves the children of the node | DOMNode Subprograms |
| GETCHILDRENBYTAGNAME Functions | Retrieves children of the element by tag name | DOMCharacterData Subprograms |
| GETDATA Functions | Retrieves  - the data of the node - the data of the processing instruction | - DOMCharacterData Subprograms - DOMProcessingInstruction Subprograms |
| GETDOCTYPE Function | Retrieves the DTD of the document | DOMDocument Subprograms |
| GETDOCUMENTELEMENT Function | Retrieves the root element of the document | DOMDocument Subprograms |
| GETELEMENTSBYTAGNAME Functions | Retrieves  - the elements in the DOMNODELIST by tag name - elements in the subtree of a DOMNODELIST by tagname | - DOMDocument Subprograms - DOMElement Subprograms |
| GETENTITIES Function | Retrieves the nodemap of entities in the Document type | DOMDocumentType Subprograms |
| GETEXPANDEDNAME Procedure and Functions | Retrieves  - the expanded name of the node - the expanded name of the attribute - the expanded name of the element | - DOMNode Subprograms - DOMAttr Subprograms - DOMElement Subprograms |
| GETFIRSTCHILD Function | Retrieves the first child of the node | DOMNode Subprograms |
| GETIMPLEMENTATION Function | Retrieves the DOM implementation | DOMDocument Subprograms |
| GETLASTCHILD Function | Retrieves the last child of the node | DOMNode Subprograms |
| GETLENGTH Functions | Retrieves  - the length of the data - the number of items in the map - the number of items in the list | - DOMCharacterData Subprograms - DOMNamedNodeMap Subprograms - DOMNodeList Subprograms |
| GETLOCALNAME Procedure and Functions | Retrieves  - the local part of the qualified name - the local name of the attribute - the local name of the element | - DOMNode Subprograms - DOMAttr Subprograms - DOMElement Subprograms |
| GETNAME Functions | Retrieves  - the name of the attribute - the name of the Document type | - DOMAttr Subprograms - DOMDocumentType Subprograms |
| GETNAMEDITEM Function | Retrieves  - an item specified by name - and namespace URI ) | - DOMNamedNodeMap Subprograms - DOMNamedNodeMap Subprograms |
| GETNAMESPACE Procedure and Functions | Retrieves  - the node's namespace URI - the NS URI of the attribute - the NS URI of the element | - DOMNode Subprograms - DOMAttr Subprograms - DOMElement Subprograms |
| GETNEXTSIBLING Function | Retrieves the next sibling of the node | DOMNode Subprograms |
| GETNODENAME Function | Retrieves the Name of the Node | DOMNode Subprograms |
| GETNODETYPE Function | Retrieves the Type of the node | DOMNode Subprograms |
| GETNODEVALUE Function | Retrieves the Value of the Node | DOMNode Subprograms |
| GETNODEVALUEASBINARYSTREAM Function & Procedure | Retrieves the Node Value as binary stream | DOMNode Subprograms |
| GETNODEVALUEASCHARACTERSTREAM Function & Procedure | Retrieves the Node Value as character stream | DOMNode Subprograms |
| GETNOTATIONNAME Function | Retrieves the notation name of the entity | DOMEntity Subprograms |
| GETNOTATIONS Function | Retrieves the nodemap of the notations in the Document type | DOMDocumentType Subprograms |
| GETTARGET Function | Retrieves the target of the processing instruction | DOMProcessingInstruction Subprograms |
| GETOWNERDOCUMENT Function | Retrieves the owner document of the node | DOMNode Subprograms |
| GETOWNERELEMENT Function | Retrieves the Element node, parent of the attribute | DOMAttr Subprograms |
| GETPARENTNODE Function | Retrieves the parent of this node | DOMNode Subprograms |
| GETPREFIX Function | Retrieves the namespace prefix  ) | DOMNode Subprograms |
| GETPREVIOUSSIBLING Function | Retrieves the previous sibling of the node | DOMNode Subprograms |
| GETPUBLICID Functions | Retrieves  - the public ID of the document type - the public Id of the entity - the public Id of the notation | - DOMDocumentType Subprograms - DOMEntity Subprograms - DOMNotation Subprograms |
| GETQUALIFIEDNAME Functions | Retrieves  - the Qualified Name of the attribute - the qualified name of the element | - DOMAttr Subprograms - DOMElement Subprograms |
| GETSCHEMANODE Function | Retrieves the associated schema URI | DOMNode Subprograms |
| GETSPECIFIED Function | Tests if attribute was specified in the element. | DOMAttr Subprograms |
| GETSTANDALONE Function | Retrieves the standalone property of the document | DOMDocument Subprograms |
| GETSYSTEMID Functions | Retrieves  - the system ID of the document type - the system Id of the entity - the system Id of the notation | - DOMDocumentType Subprograms - DOMEntity Subprograms - DOMNotation Subprograms |
| GETTAGNAME Function | Retrieves the Tag name of the element | DOMElement Subprograms |
| GETVALUE Function | Retrieves the value of the attribute | DOMAttr Subprograms |
| GETVERSION Function | Retrieves the version of the document | DOMDocument Subprograms) |
| GETXMLTYPE Function | Retrieves the `XMLType` associated with the DOM Document | DOMDocument Subprograms |
| HASATTRIBUTES Function | Tests if the node has attributes | DOMNode Subprograms |
| HASATTRIBUTE Functions | Tests if an attribute exists | DOMElement Subprograms |
| HASCHILDNODES Function | Tests if the node has child nodes | DOMNode Subprograms |
| HASFEATURE Function | Tests if the `DOMImplementation` implements a feature | DOMImplementation Subprograms |
| IMPORTNODE Function | Imports a node from another document | DOMNode Subprograms |
| INSERTBEFORE Function | Inserts a child before the reference child | DOMNode Subprograms |
| INSERTDATA Procedure | Inserts the data in the node at the specified offSets | DOMCharacterData Subprograms |
| ISNULL Functions | Tests  - if the node is `NULL` - if the Attribute node is `NULL` - if the `CDataSection` is `NULL` - if the CharacterData is `NULL` - if the comment is `NULL` - if the document is `NULL` - if the DocumentFragment is `NULL` - if the Document Type is `NULL` - if the Element is `NULL` - if the Entity is `NULL` - if the `DOMEntityReference` is `NULL` - if the `DOMImplementation` node is `NULL` - if the `NamedNodeMap` is `NULL` - if the ` NodeList` is `NULL` - if the Notation is `NULL` - if the Processing Instruction is `NULL` - if the text is `NULL` | - DOMNode Subprograms - DOMAttr Subprograms - DOMCDataSection Subprograms - DOMCharacterData Subprograms - DOMComment Subprograms - DOMDocument Subprograms - DOMDocumentFragment Subprograms - DOMDocumentType Subprograms - DOMElement Subprograms - DOMEntity Subprograms - DOMEntityReference Subprograms - DOMImplementation Subprograms - DOMNamedNodeMap Subprograms - DOMNodeList Subprograms - DOMNotation Subprograms - DOMProcessingInstruction Subprograms - DOMText Subprograms |
| ITEM Functions | Retrieves  - the item given the index in the map - the item given the index in the ` NodeList` | - DOMNamedNodeMap Subprograms - DOMNodeList Subprograms |
| MAKEATTR Function | Casts the node to an Attribute | DOMNode Subprograms |
| MAKECDATASECTION Function | Casts the node to a CData Section | DOMNode Subprograms |
| MAKECHARACTERDATA Function | Casts the node to Character Data | DOMNode Subprograms |
| MAKECOMMENT Function | Casts the node to a Comment | DOMNode Subprograms |
| MAKEDOCUMENT Function | Casts the node to a DOM Document | DOMNode Subprograms |
| MAKEDOCUMENTFRAGMENT Function | Casts the node to a DOM Document Fragment | DOMNode Subprograms) |
| MAKEDOCUMENTTYPE Function | Casts the node to a DOM Document Type | DOMNode Subprograms |
| MAKEELEMENT Function | Casts the node to a DOM ElemenT | DOMNode Subprograms |
| MAKEENTITY Function | Casts the node to a DOM Entity | DOMNode Subprograms |
| MAKEENTITYREFERENCE Function | Casts the node to a DOM Entity Reference | DOMNode Subprograms |
| MAKENODE Functions | Casts  - the Attribute to a node - the `CDatasection` to a node - the CharacterData to a node - the Comment to a node - the document to a node - the Document Fragment to a node - the document type to a node - the Element to a node - the Entity to a node - the `DOMEntityReference` to `NULL` - the notation to a node - the Processing Instruction to a node - the text to a node | - DOMAttr Subprograms - DOMCDataSection Subprograms - DOMCharacterData Subprograms - DOMComment Subprograms - DOMDocument Subprograms - DOMDocumentFragment Subprograms - DOMDocumentType Subprograms - DOMElement Subprograms - DOMEntity Subprograms - DOMEntityReference Subprograms - DOMNotation Subprograms - DOMProcessingInstruction Subprograms - DOMText Subprograms |
| MAKENOTATION Function | Casts the node to a DOM Notation | DOMNode Subprograms |
| MAKEPROCESSINGINSTRUCTION Function | Casts the node to a DOM Processing Instruction | DOMNode Subprograms |
| MAKETEXT Function | Casts the node to a DOM Text | DOMNode Subprograms |
| NEWDOMDOCUMENT Functions | Creates a new document | DOMDocument Subprograms |
| NORMALIZE Procedure | Normalizes the text children of the element | DOMElement Subprograms |
| REMOVEATTRIBUTE Procedures | Removes the attribute specified by the name | DOMElement Subprograms |
| REMOVEATTRIBUTENODE Function | Removes the attribute node in the element | DOMElement Subprograms |
| REMOVECHILD Function | Removes a specified child from a node | DOMNode Subprograms |
| REMOVENAMEDITEM Function | Removes the item specified by name | DOMNamedNodeMap Subprograms |
| REPLACECHILD Function | Replaces the old child with a new child | DOMNode Subprograms |
| REPLACEDATA Procedure | Changes a range of characters in the node | DOMCharacterData Subprograms |
| RESOLVENAMESPACEPREFIX Function | Resolve the prefix to a namespace URI | DOMElement Subprograms |
| SETATTRIBUTE Procedures | Sets the attribute specified by the name | DOMElement Subprograms |
| SETATTRIBUTENODE Functions | Sets the attribute node in the element | DOMElement Subprograms |
| SETCHARSET Procedure | Sets the characterset of the `DOM` document | DOMDocument Subprograms |
| SETDATA Procedures | Sets  - the data to the node - the data of the processing instruction | - DOMCharacterData Subprograms - DOMProcessingInstruction Subprograms |
| SETDOCTYPE Procedure | Sets the DTD of the document. | DOMDocument Subprograms |
| SETNAMEDITEM Function | Sets the item in the map specified by the name | DOMNamedNodeMap Subprograms |
| SETNODEVALUE Procedure | Sets the Value of the node | DOMNode Subprograms |
| SETNODEVALUEASBINARYSTREAM Function & Procedure | Sets the Node Value as a binary stream | DOMNode Subprograms |
| SETNODEVALUEASCHARACTERSTREAM Function & Procedure | Sets the Node Value as a character stream | DOMNode Subprograms |
| SETPREFIX Procedure | Sets the namespace prefix | DOMNode Subprograms |
| SETSTANDALONE Procedure | Sets the standalone property of the document | DOMDocument Subprograms |
| SETVALUE Procedure | Sets the value of the attribute | DOMAttr Subprograms |
| SETVERSION Procedure | Sets the version of the document | DOMDocument Subprograms |
| SPLITTEXT Function | Splits the contents of the text node into 2 text nodes | DOMText Subprograms |
| SUBSTRINGDATA Function | Retrieves the substring of the data | DOMCharacterData Subprograms |
| USEBINARYSTREAM Function | Strabismus that the stream is valid for use | DOMNode Subprograms |
| WRITETOBUFFER Procedures | Writes  - the contents of the node to a buffer - the document to a buffer - the contents of a document fragment into a buffer | - DOMNode Subprograms - DOMDocument Subprograms - DOMDocumentFragment Subprograms |
| WRITETOCLOB Procedures | Writes  - the contents of the node to a `CLOB` - the document to a `CLOB` | - DOMNode Subprograms - DOMDocument Subprograms |
| WRITETOFILE Procedures | Writes  - the contents of the node to a file - the document to a file | - DOMNode Subprograms - DOMDocument Subprograms |

#### 210.7.1 ADOPTNODE Function

This function adopts a node from another document, and returns this new node.

See Also:

DOMNode Subprograms for other subprograms in this group

Syntax

```
DBMS_XMLDOM.ADOPTNODE(
   doc            IN   DOMDocument,
   importedNode   IN   DOMNode)
 RETURN DOMNODE;
```

Parameters

Table 210-22 ADOPTNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | Document that is adopting the node |
| `importedNode` | Node to adopt |

Usage Notes

Note that the ADOPTNODE Function removes the node from the source document while the IMPORTNODE Function clones the node in the source document.

#### 210.7.2 APPENDCHILD Function

This function adds the node `newchild` to the end of the list of children of this node, and returns the newly added node. If the `newchild` is already in the tree, it is first removed.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.APPENDCHILD(
   n          IN    DOMNode,
   newchild   IN    DOMNode)
 RETURN DOMNODE;
```

Parameters

Table 210-23 APPENDCHILD Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` |
| `newchild` | The child to be appended to the list of children of node `n` |

#### 210.7.3 APPENDDATA Procedure

This procedure appends the string to the end of the character data of the node. Upon success, data provides access to the concatenation of data and the specified string argument.

See Also:

DOMCharacterData Subprograms

Syntax

```
DBMS_XMLDOM.APPENDDATA(
   cd      IN    DOMCHARACTERDATA, 
   arg     IN    VARCHAR2);
```

Parameters

Table 210-24 APPENDDATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `arg` | The data to append to the existing data |

#### 210.7.4 CLONENODE Function

This function returns a duplicate of this node, and serves as a generic copy constructor for nodes. The duplicate node has no parent, its parent node is `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.CLONENODE(
   n       IN    DOMNODE,
   deep    IN    BOOLEAN)
 RETURN DOMNODE;
```

Parameters

Table 210-25 CLONENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `deep` | Determines if children are to be cloned |

Usage Notes

- Cloning an Element copies all attributes and their values, including those generated by the XML processor to represent defaulted attributes, but this method does not copy any text it contains unless it is a deep clone, since the text is contained in a child Text node.
- Cloning an Attribute directly, as opposed to be cloned as part of an Element cloning operation, returns a specified attribute (specified is `TRUE`).
- Cloning any other type of node simply returns a copy of this node.

#### 210.7.5 CREATEATTRIBUTE Functions

This function creates a `DOMATTR` node.

See Also:

DOMDocument Subprograms

Syntax

Creates a `DOMATTR ` with the specified name:

```
DBMS_XMLDOM.CREATEATTRIBUTE(
   doc     IN    DOMDOCUMENT,
   name    IN    VARCHAR2)
 RETURN DOMATTR;
```

Creates a `DOMATTR` with the specified name and namespace URI:

```
DBMS_XMLDOM.CREATEATTRIBUTE(
   doc     IN    DOMDOCUMENT,
   qname    IN    VARCHAR2,
   ns      IN     VARCHAR2)
RETURN DOMATTR;
```

Parameters

Table 210-26 CREATEATTRIBUTE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `qname` | New attribute qualified name |
| `ns` | Namespace |

#### 210.7.6 CREATECDATASECTION Function

This function creates a `DOMCDATASECTION` node.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATECDATASECTION(
   doc     IN      DOMDOCUMENT,
   data    IN      VARCHAR2)
 RETURN DOMCDATASECTION;
```

Parameters

Table 210-27 CREATECDATASECTION Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `data` | Content of the `DOMCDATASECTION` node |

#### 210.7.7 CREATECOMMENT Function

This function creates a `DOMCOMMENT` node.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATECOMMENT(
   doc      IN      DOMDOCUMENT,
   data     IN      VARCHAR2)
 RETURN DOMCOMMENT;
```

Parameters

Table 210-28 CREATECOMMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `data` | Content of the `DOMComment` node |

#### 210.7.8 CREATEDOCUMENT Function

This function creates a `DOMDOCUMENT` with specified namespace URI, root element name, DTD.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATEDOCUMENT(
   namespaceURI      IN     VARCHAR2,
   qualifiedName     IN     VARCHAR2,
   doctype           IN     DOMTYPE := NULL)
 RETURN DOMDOCUMENT;
```

Parameters

Table 210-29 CREATEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `namespaceURI` | Namespace URI |
| `qualifiedName` | Root element name |
| `doctype` | Document type |

#### 210.7.9 CREATEDOCUMENTFRAGMENT Function

This function creates a `DOMDOCUMENTFRAGMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATEDOCUMENTFRAGMENT(
   doc      IN     DOMDOCUMENT)
 RETURN DOMDOCUMENTFRAGMENT;
```

Parameters

Table 210-30 CREATEDOCUMENTFRAGMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDocument` |

#### 210.7.10 CREATEELEMENT Functions

This function creates a `DOMELEMENT`.

See Also:

DOMDocument Subprograms

Syntax

Creates a `DOMElement` with specified name:

```
DBMS_XMLDOM.CREATEELEMENT(
   doc        IN      DOMDOCUMENT,
   tagName    IN      VARCHAR2)
 RETURN DOMELEMENT;
```

Creates a `DOMElement` with specified name and namespace URI:

```
DBMS_XMLDOM.CREATEELEMENT(
   doc        IN     DOMDOCUMENT,
   tagName    IN     VARCHAR2,
   ns         IN     VARCHAR2)
 RETURN DOMELEMENT;
```

Parameters

Table 210-31 CREATEELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `tagName` | Tagname for new `DOMELEMENT` |
| `ns` | Namespace |

#### 210.7.11 CREATEENTITYREFERENCE Function

This function creates a `DOMENTITYREFERENCE` node.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATEENTITYREFERENCE(
   doc        IN     DOMDOCUMENT,
   name       IN     VARCHAR2)
 RETURN DOMENTITYREFERENCE;
```

Parameters

Table 210-32 CREATEENTITYREFERENCE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `name` | New entity reference name |

#### 210.7.12 CREATEPROCESSINGINSTRUCTION Function

This function creates a `DOMPROCESSINGINSTRUCTION` node.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION(
   doc       IN      DOMDocument,
   target    IN      VARCHAR2,
   data      IN      VARCHAR2)
 RETURN DOMPROCESSINGINSTRUCTION;
```

Parameters

Table 210-33 CREATEPROCESSINGINSTRUCTION Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `target` | Target of the new processing instruction |
| `data` | Content data of the new processing instruction |

#### 210.7.13 CREATETEXTNODE Function

This function creates a `DOMTEXT` node.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.CREATETEXTNODE(
   doc      IN     DOMDocument,
   data     IN     VARCHAR2)
 RETURN DOMTEXT;
```

Parameters

Table 210-34 CREATETEXTNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `data` | Content of the `DOMText` node |

#### 210.7.14 DELETEDATA Procedure

This procedure removes a range of characters from the node. Upon success, data and length reflect the change.

See Also:

DOMCharacterData Subprograms

Syntax

```
DBMS_XMLDOM.DELETEDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER);
```

Parameters

Table 210-35 DELETEDATA PROCEDURE Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `offset` | The offset from which to delete the data |
| `cnt` | The number of characters (starting from offset) to delete |

#### 210.7.15 FINDENTITY Function

This function finds an entity in the specified DTD, and returns that entity if found.

See Also:

DOMDocumentType Subprograms

Syntax

```
DBMS_XMLDOM.FINDENTITY(
   dt     IN     DOMDOCUMENTTYPE,
   name   IN     VARCHAR2,
   par    IN     BOOLEAN) 
 RETURN  DOMENTITY;
```

Parameters

Table 210-36 FINDENTITY Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | The DTD |
| `name` | Entity to find |
| `par` | Flag to indicate type of entity; `TRUE` for parameter entity and `FALSE` for normal entity |

#### 210.7.16 FINDNOTATION Function

This function finds the notation in the specified DTD, and returns it, if found.

See Also:

DOMDocumentType Subprograms

Syntax

```
DBMS_XMLDOM.FINDNOTATION(
   dt        IN     DOMDocumentType,
   name      IN     VARCHAR2) 
 RETURN DOMNOTATION;
```

Parameters

Table 210-37 FINDNOTATION Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | The DTD |
| `name` | The notation to find |

#### 210.7.17 FREEDOCFRAG Procedure

This procedure frees the specified document fragment.

See Also:

DOMDocument Subprograms and DOMDocumentFragment Subprograms

Syntax

```
DBMS_XMLDOM.FREEDOCFRAG(
   df    IN    DOMDOCUMENTFRAGMENT);
```

Parameters

Table 210-38 FREEDOCFRAG Procedure Parameters

| Parameter | Description |
| --- | --- |
| `df` | DOM document fragment |

#### 210.7.18 FREEDOCUMENT Procedure

This procedure frees `DOMDOCUMENT` object.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.FREEDOCUMENT(
   doc     IN     DOMDOCUMENT);
```

Parameters

Table 210-39 FREEDOCUMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.19 FREEELEMENT Procedure

This procedure frees memory allocated to a DOMElement handle.

See Also:

DBMS\_XMLDOM DOMElement Subprograms

Syntax

```
DBMS_XMLDOM.FREEELEMENT(
    elem IN DOMELEMENT);
```

Parameters

Table 210-40 FREEELEMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| elem | Of type `DOMELEMENT` |

#### 210.7.20 FREENODE Procedure

This procedure frees all resources associated with a `DOMNODE`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.FREENODE(
   n      IN     DOMNODE);
```

Parameters

Table 210-41 FREENODE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.21 FREENODELIST Procedure

This procedure frees all resources associated with a nodelist.

See Also:

DBMS\_XMLDOM DOMNodeList Subprograms

Syntax

```
DBMS_XMLDOM.FREENODELIST(
   nl IN DOMNodeList);
```

Parameters

Table 210-42 FREENODELIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` l | Of type `DOMNODELIST` |

#### 210.7.22 GETATTRIBUTE Functions

This function returns the value of an attribute of an `DOMELEMENT` by name.

Syntax

Returns the value of a `DOMELEMENT` 's attribute by name:

```
DBMS_XMLDOM.GETATTRIBUTE(
   elem       IN      DOMELEMENT,
   name       IN      VARCHAR2)
 RETURN VARCHAR2;
```

Returns the value of a `DOMELEMENT` 's attribute by name and namespace URI:

```
DBMS_XMLDOM.GETATTRIBUTE(
   elem      IN     DOMELEMENT,
   name      IN     VARCHAR2,
   ns        IN     VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 210-43 GETATTRIBUTE Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `name` | Attribute name |
| `ns` | Namespace |

#### 210.7.23 GETATTRIBUTENODE Functions

This function returns an attribute node from the `DOMELEMENT` by name. The function is overloaded. The specific forms of functionality are described along with the syntax declarations.

See Also:

DOMElement Subprograms

Syntax

Returns an attribute node from the `DOMELEMENT` by name:

```
DBMS_XMLDOM.GETATTRIBUTENODE(
   elem      IN     DOMElement,
   name      IN     VARCHAR2)
 RETURN DOMATTR;
```

Returns an attribute node from the `DOMELEMENT` by name and namespace URI:

```
DBMS_XMLDOM.GETATTRIBUTENODE(
   elem      IN     DOMElement,
   name      IN     VARCHAR2,
   ns        IN     VARCHAR2)
RETURN DOMATTR;
```

Parameters

Table 210-44 GETATTRIBUTENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `name` | Attribute name; \* matches any attribute |
| `ns` | Namespace |

#### 210.7.24 GETATTRIBUTES Function

This function retrieves a `NAMEDNODEMAP` containing the attributes of this node (if it is an Element) or `NULL` otherwise.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETATTRIBUTES(
   n      IN      DOMNode)
 RETURN DOMNAMEDNODEMAP;
```

Parameters

Table 210-45 GETATTRIBUTES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.25 GETCHARSET Function

This function retrieves the characterset of the DOM document.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETCHARSET(
   doc IN    DOMDocument)
 RETURN VARCHAR2;
```

Parameters

Table 210-46 GETCHARSET Function Parameters

| Parameter | Description |
| --- | --- |
| doc | `DOM` document |

Usage Notes

For a newly parsed document, we return the database characterset. Once the `SETCHARSET` Procedure is called with a non- `NULL` value for `charset`, that `charset` is returned.

#### 210.7.26 GETCHILDNODES Function

This function retrieves a `DOMNODELIST` that contains all children of this node. If there are no children, this is a `DOMNODELIST` containing no nodes.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETCHILDNODES(
   n      IN    DOMNode)
 RETURN DOMNodeList;
```

Parameters

Table 210-47 GETCHILDNODES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.27 GETCHILDRENBYTAGNAME Functions

This function returns the children of the `DOMELEMENT`.

See Also:

DOMElement Subprograms

Syntax

Returns children of the `DOMELEMENT` given the tag name:

```
DBMS_XMLDOM.GETCHILDRENBYTAGNAME(
   elem      IN      DOMElement, 
   name      IN      VARCHAR2) 
 RETURN DOMNODELIST;
```

Returns children of the `DOMELEMENT` given the tag name and namespace:

```
DBMS_XMLDOM.GETCHILDRENBYTAGNAME(
   elem      IN      DOMElement, 
   name      IN      VARCHAR2, 
   ns        IN      VARCHAR2) 
RETURN DOMNODELIST;
```

Parameters

Table 210-48 GETCHILDRENBYTAGNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | `DOMELEMENT` |
| `name` | Tag name |
| `ns` | Namespace |

#### 210.7.28 GETDATA Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Gets the character data of the node that implements this interface (See Also: DOMCharacterData Subprograms):

```
DBMS_XMLDOM.GETDATA(
   cd      IN    DOMCHARACTERDATA)
 RETURN VARCHAR2;
```

Returns the content data of the `DOMProcessingInstruction` (See Also: DOMProcessingInstruction Subprograms):

```
DBMS_XMLDOM.GETDATA(
   pi      IN    DOMPROCESSINGINSTRUCTION)
 RETURN VARCHAR2;
```

Parameters

Table 210-49 GETDATA Function Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `pi` | The `DOMPROCESSINGINSTRUCTION` |

#### 210.7.29 GETDOCTYPE Function

This function returns the DTD associated to the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETDOCTYPE(
   doc      IN     DOMDOCUMENT)
RETURN DOMDOCUMENTTYPE;
```

Parameters

Table 210-50 GETDOCTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.30 GETDOCUMENTELEMENT Function

This function returns the root element of the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETDOCUMENTELEMENT(
   doc      IN      DOMDOCUMENT)
 RETURN DOMELEMENT;
```

Parameters

Table 210-51 GETDOCUMENTELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.31 GETELEMENTSBYTAGNAME Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Returns a `DOMNODELIST` of all the elements with a specified tagname (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.GETELEMENTSBYTAGNAME(
   doc         IN      DOMDOCUMENT,
   tagname     IN      VARCHAR2)
 RETURN DOMNODELIST;
```

Returns the element children of the `DOMELEMENT` given the tag name (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.GETELEMENTSBYTAGNAME(
   elem      IN     DOMELEMENT,
   name      IN     VARCHAR2) 
 RETURN DOMNODELIST;
```

Returns the element children of the `DOMELEMENT` given the tag name and namespace (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.GETELEMENTSBYTAGNAME(
   elem      IN     DOMELEMENT,
   name      IN     VARCHAR2, 
   ns        IN     VARCHAR2) 
 RETURN DOMNODELIST;
```

Parameters

Table 210-52 GETELEMENTSBYTAGNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `tagname` | Name of the tag to match on |
| `elem` | The `DOMELEMENT` |
| `name` | Tag name; using a wildcard(\*) would match any tag |
| `ns` | Namespace |

#### 210.7.32 GETENTITIES Function

This function retrieves a `DOMNAMEDNODEMAP` containing the general entities, both external and internal, declared in the DTD.

See Also:

DOMDocumentType Subprograms

Syntax

```
DBMS_XMLDOM.GETENTITIES(
   dt      IN     DOMDocumentType)
 RETURN DOMNAMEDNODEMAP;
```

Parameters

Table 210-53 GETENTITIES Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | `DOMDOCUMENTTYPE` |

#### 210.7.33 GETEXPANDEDNAME Procedure and Functions

This subprogram is overloaded as a procedure and two functions. The specific forms of functionality are described along with the syntax declarations.

Syntax

Retrieves the expanded name of the `Node` if is in an `Element` or `Attribute ` type; otherwise, returns `NULL` (See Also: DOMNode Subprograms)

```
DBMS_XMLDOM.GETEXPANDEDNAME(
   n       IN      DOMNODE
   data    OUT     VARCHAR);
```

Returns the expanded name of the `DOMAttr` (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.GETEXPANDEDNAME(
   a       IN     DOMAttr)
 RETURN VARCHAR2;
```

Returns the expanded name of the `DOMElement` (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.GETEXPANDEDNAME(
   elem      IN    DOMELEMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-54 GETEXPANDEDNAME Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `data` | Returned expanded name of the `Node` |
| `a` | `DOMATTR` |
| `elem` | `DOMELEMENT` |

#### 210.7.34 GETFIRSTCHILD Function

This function retrieves the first child of this node. If there is no such node, this returns `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETFIRSTCHILD(
   n      IN      DOMNODE)
 RETURN DOMNODE;
```

Parameters

Table 210-55 GETFIRSTCHILD Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.35 GETIMPLEMENTATION Function

This function returns the `DOMIMPLEMENTATION` object that handles this `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETIMPLEMENTATION(
   doc      IN     DOMDOCUMENT)
 RETURN DOMIMPLEMENTATION;
```

Parameters

Table 210-56 GETIMPLEMENTATION Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.36 GETLASTCHILD Function

This function retrieves the last child of this node. If there is no such node, this returns `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETLASTCHILD(
   n     IN   DOMNODE)
 RETURN DOMNODE;
```

Parameters

Table 210-57 GETLASTCHILD Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.37 GETLENGTH Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Gets the number of characters in the data. This may have the value zero, because CharacterData nodes may be empty (See Also: DOMCharacterData Subprograms):

```
DBMS_XMLDOM.GETLENGTH(
   cd     IN     DOMCHARACTERDATA)
 RETURN NUMBER;
```

Gets the number of nodes in this map. The range of valid child node indexes is `0` to `length-1`, inclusive (See Also: DOMNamedNodeMap Subprograms):

```
DBMS_XMLDOM.GETLENGTH(
   nnm      IN     DOMNAMEDNODEMAP)
 RETURN NUMBER;
```

Gets the number of nodes in the list. The range of valid child node indexes is `0` to `length-1`, inclusive (See Also: DOMNodeList Subprograms):

```
DBMS_XMLDOM.GETLENGTH(
   nl     IN    DOMNODELIST)
 RETURN NUMBER;
```

Parameters

Table 210-58 GETLENGTH Function Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `nnm` | `DOMNAMEDNODEMAP` |
| `nl` | `DOMNODELIST` |

#### 210.7.38 GETLOCALNAME Procedure and Functions

This function is overloaded as a procedure and two functions. The specific forms of functionality are described alongside the syntax declarations.

Syntax

Retrieves the local part of the node's qualified name (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.GETLOCALNAME(
   n       IN     DOMNODE,
   data    OUT    VARCHAR2);
```

Returns the local name of the `DOMAttr` (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.GETLOCALNAME(
   a       IN     DOMATTR)
 RETURN VARCHAR2;
```

Returns the local name of the `DOMElement` (See Also: DOMElement Subprograms)

```
DBMS_XMLDOM.GETLOCALNAME(
   elem       IN     DOMELEMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-59 GETLOCALNAME Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` |
| `data` | Returned local name. |
| `a` | `DOMAttr`. |
| `elem` | `DOMElement`. |

#### 210.7.39 GETNAME Functions

This function is overloaded. The specific forms of functionality are described with the syntax declarations.

Syntax

Returns the name of this attribute (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.GETNAME(
   a       IN     DOMATTR)
 RETURN VARCHAR2;
```

Retrieves the name of DTD, or the name immediately following the `DOCTYPE` keyword (See Also: DOMDocumentType Subprograms):

```
DBMS_XMLDOM.GETNAME(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN VARCHAR2;
```

Parameters

Table 210-60 GETNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` |
| `dt` | `DOMDOCUMENTTYPE` |

#### 210.7.40 GETNAMEDITEM Function

`GETNAMEDITEM` retrieves a node specified by name.

See Also:

DOMNamedNodeMap Subprograms

Syntax

Retrieves a node specified by name:

```
DBMS_XMLDOM.GETNAMEDITEM(
   nnm    IN  DOMNAMEDNODEMAP,
   name   IN  VARCHAR2)
 RETURN DOMNODE;
```

Retrieves a node specified by name and namespace URI:

```
DBMS_XMLDOM.GETNAMEDITEM(
   nnm    IN  DOMNAMEDNODEMAP,
   name   IN  VARCHAR2,
   ns     IN  VARCHAR2)
 RETURN DOMNODE;
```

Parameters

Table 210-61 GETNAMEDITEM Function Parameters

| Parameter | Description |
| --- | --- |
| `nnm` | `DOMNAMEDNODEMAP` |
| `name` | Name of the item to be retrieved |
| `ns` | Namespace |

#### 210.7.41 GETNAMESPACE Procedure and Functions

This subprogram is overloaded as a procedure and two functions. The specific forms of functionality are described alongside the syntax declarations.

Syntax

Retrieves the namespace URI associated with the node (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.GETNAMESPACE(
   n       IN     DOMNODE,
   data    OUT    VARCHAR2);
```

Retrieves the namespace of the `DOMATTR` (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.GETNAMESPACE(
   a       IN     DOMATTR)
 RETURN VARCHAR2;
```

Retrieves the namespace of the `DOMELEMENT` (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.GETNAMESPACE(
   elem       IN     DOMELEMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-62 GETNAMESPACE Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `data` | Returned namespace URI |
| `a` | `DOMATTR` |
| `elem` | `DOMELEMENT` |

#### 210.7.42 GETNEXTSIBLING Function

This function retrieves the node immediately following this node. If there is no such node, this returns `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETNEXTSIBLING(
   n       IN     DOMNODE)
 RETURN DOMNode;
```

Parameters

Table 210-63 GETNEXTSIBLING Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.43 GETNODETYPE Function

This function retrieves a code representing the type of the underlying object.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETNODETYPE(
   n       IN     DOMNODE)
 RETURN NUMBER;
```

Parameters

Table 210-64 GETNODETYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.44 GETNODENAME Function

This function gets the name of the node depending on its type.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETNODENAME(
   n       IN     DOMNODE)
 RETURN VARCHAR2;
```

Parameters

Table 210-65 GETNODENAME Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.45 GETNODEVALUE Function

This function gets the value of this node, depending on its type.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETNODEVALUE(
   n       IN     DOMNODE)
 RETURN VARCHAR2;*
```

Parameters

Table 210-66 GETNODEVALUE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.46 GETNODEVALUEASBINARYSTREAM Function & Procedure

The operation of these subprograms is described with each syntax implementation.

Syntax

This function returns an instance of the PL/SQL `XMLBinaryInputStream`. The node datatype must be `RAW` or `BLOB` – if not an exception is raised.

```
DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM (
   n      IN     DOMNODE)
 RETURN SYS.UTL_BINARYINPUTSTREAM;
```

Using this procedure, the application passes an implementation of `SYS`.`UTL_BINARYOUTPUTSTREAM` into which XDB writes the contents of the node. The datatype of the node must be `RAW` or `CLOB` – if not an exception is raised.

```
DBMS_XMLDOM.GETNODEVALUEASBINARYSTREAM (
   n        in   DOMNODE, 
   value    in   SYS.UTL_BINARYOUTPUTSTREAM);
```

Parameters

Table 210-67 GETNODEVALUEASBINARYSTREAM Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| value | `BINARYOUTPUTSTREAM` |

#### 210.7.47 GETNODEVALUEASCHARACTERSTREAM Function & Procedure

The operation of these subprograms is described with each syntax implementation.

See Also:

DOMNode Subprograms

Syntax

This function returns an instance of the PL/SQL `XMLCharacterInputStream`. If the node data is character it is converted to the current session character set. If the node data is not character data, it is first converted to character data.

```
DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM  (
   n        IN     DOMNODE)
 RETURN SYS.UTL_CHARACTERINPUTSTREAM;
```

Using this procedure, the node data is converted, as necessary, to the session character set and then "pushed" into the `SYS`.`UTL_CHARACTEROUTPUTSTREAM`.

```
DBMS_XMLDOM.GETNODEVALUEASCHARACTERSTREAM  (
   n        IN   DOMNODE,
   value    IN   SYS.UTL_CHARACTEROUTPUTSTREAM);
```

Parameters

Table 210-68 GETNODEVALUEASCHARACTERSTREAM Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| value | `CHARACTEROUTPUTSTREAM` |

#### 210.7.48 GETNOTATIONNAME Function

This function returns the notation name of the `DOMENTITY`.

See Also:

DOMEntity Subprograms

Syntax

```
DBMS_XMLDOM.GETNOTATIONNAME(
   ent       IN     DOMENTITY)
 RETURN VARCHAR2;
```

Parameters

Table 210-69 GETNOTATIONNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `ent` | `DOMENTITY` |

#### 210.7.49 GETNOTATIONS Function

This function retrieves a `DOMNAMEDNODEMAP` containing the notations declared in the DTD.

See Also:

DOMDocumentType Subprograms

Syntax

```
DBMS_XMLDOM.GETNOTATIONS(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN DOMNAMEDNODEMAP;
```

Parameters

Table 210-70 GETNOTATIONS Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | `DOMDOCUMENTTYPE` |

#### 210.7.50 GETTARGET Function

This function returns the target of the `DOMPROCESSINGINSTRUCTION`.

See Also:

DOMProcessingInstruction Subprograms

Syntax

```
DBMS_XMLDOM.GETTARGET(
   pi       IN     DOMPROCESSINGINSTRUCTION)
 RETURN VARCHAR2;
```

Parameters

Table 210-71 GETTARGET Function Parameters

| Parameter | Description |
| --- | --- |
| `pi` | `DOMPROCESSINGINSTRUCTION` |

#### 210.7.51 GETOWNERDOCUMENT Function

This function retrieves the Document object associated with this node. This is also the Document object used to create new nodes. When this node is a Document or a Document Type that is not used with any Document yet, this is `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETOWNERDOCUMENT(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENT;
```

Parameters

Table 210-72 GETOWNERDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.52 GETOWNERELEMENT Function

This function retrieves the Element node to which the specified Attribute is attached.

Syntax

```
DBMS_XMLDOM.GETOWNERELEMENT(
   a       IN     DOMATTR)
 RETURN DOMElement;
```

Parameters

Table 210-73 GETOWNERELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `a` | Attribute |

#### 210.7.53 GETPARENTNODE Function

This function retrieves the parent of this node. All nodes, except `Attr`, `Document`, `DocumentFragment`, `Entity`, and `Notation` may have a parent. However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETPARENTNODE(
   n       IN     DOMNODE)
 RETURN DOMNODE;
```

Parameters

Table 210-74 GETPARENTNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.54 GETPREFIX Function

This function retrieves the namespace prefix of the node.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETPREFIX(
   n       IN     DOMNODE)
 RETURN VARCHAR2;
```

Parameters

Table 210-75 GETPREFIX Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.55 GETPREVIOUSSIBLING Function

This function retrieves the node immediately preceding this node. If there is no such node, this returns `NULL`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETPREVIOUSSIBLING(
   n       IN     DOMNODE)
 RETURN DOMNODE;
```

Parameters

Table 210-76 GETPREVIOUSSIBLING Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.56 GETPUBLICID Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Returns the public identifier of the specified DTD (See Also: DOMDocumentType Subprograms):

```
DBMS_XMLDOM.GETPUBLICID(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN VARCHAR2;
```

Returns the public identifier of the `DOMENTITY` (See Also: DOMEntity Subprograms):

```
DBMS_XMLDOM.GETPUBLICID(
   ent      IN     DOMENTITY)
 RETURN VARCHAR2;
```

Returns the public identifier of the `DOMNOTATION` (See Also: DOMNotation Subprograms):

```
DBMS_XMLDOM.GETPUBLICID(
   n        IN     DOMNOTATION)
 RETURN VARCHAR2;
```

Parameters

Table 210-77 GETPUBLICID Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | The DTD |
| `ent` | `DOMENTITY` |
| `n` | `DOMNOTATION` |

#### 210.7.57 GETQUALIFIEDNAME Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Returns the qualified name of the `DOMATTR` (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.GETQUALIFIEDNAME(
   a        IN     DOMATTR)
 RETURN VARCHAR2;
```

Returns the qualified name of the `DOMElement` (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.GETQUALIFIEDNAME(
   elem     IN     DOMELEMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-78 GETQUALIFIEDNAME Functions Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` |
| `elem` | `DOMELEMENT` |

#### 210.7.58 GETSCHEMANODE Function

This function retrieves the schema URI associated with the node.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.GETSCHEMANODE(
   n       IN     DOMNODE)
 RETURN DOMNODE;
```

Parameters

Table 210-79 GETSCHEMANODE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.59 GETSPECIFIED Function

If this attribute was explicitly specified, a value in the original document, this is true; otherwise, it is false.

See Also:

DOMAttr Subprograms

Syntax

```
DBMS_XMLDOM.GETSPECIFIED(
   a       IN     DOMATTR)
 RETURN BOOLEAN;
```

Parameters

Table 210-80 GETSPECIFIED Function Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` |

#### 210.7.60 GETSTANDALONE Function

This function returns the standalone property associated with the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETSTANDALONE(
   doc       IN     DOMDOCUMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-81 GETSTANDALONE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT`. |

#### 210.7.61 GETSYSTEMID Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Returns the system id of the specified DTD (See Also: DOMDocumentType Subprograms):

```
DBMS_XMLDOM.GETSYSTEMID(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN VARCHAR2;
```

Returns the system identifier of the `DOMENTITY` (See Also: DOMEntity Subprograms):

```
DBMS_XMLDOM.GETSYSTEMID(
   ent      IN     DOMENTITY)
 RETURN VARCHAR2;
```

Returns the system identifier of the `DOMNOTATION` (See Also: DOMNotation Subprograms):

```
DBMS_XMLDOM.GETSYSTEMID(
   n        IN     DOMNOTATION)
 RETURN VARCHAR2;
```

Parameters

Table 210-82 GETSYSTEMID Function Parameters

| Parameter | Description |
| --- | --- |
| `dt` | The DTD. |
| `ent` | `DOMEntity`. |
| `n` | `DOMNotation`. |

#### 210.7.62 GETTAGNAME Function

This function returns the name of the `DOMELEMENT`.

See Also:

DOMElement Subprograms

Syntax

```
DBMS_XMLDOM.GETTAGNAME(
   elem       IN     DOMELEMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-83 GETTAGNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |

#### 210.7.63 GETVALUE Function

This function retrieves the value of the attribute.

See Also:

DOMAttr Subprograms

Syntax

```
DBMS_XMLDOM.GETVALUE(
   a       IN     DOMATTR)
 RETURN VARCHAR2;
```

Parameters

Table 210-84 GETVALUE Function Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` |

#### 210.7.64 GETVERSION Function

This function returns the version of the `DOMDOCUMENT`.

Syntax

```
DBMS_XMLDOM.GETVERSION(
   doc       IN     DOMDOCUMENT)
 RETURN VARCHAR2;
```

Parameters

Table 210-85 GETVERSION Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.65 GETXMLTYPE Function

This function returns the `XMLType ` associated with the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.GETXMLTYPE(
   doc       IN     DOMDOCUMENT)
 RETURN SYS.XMLTYPE;
```

Parameters

Table 210-86 GETXMLTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |

#### 210.7.66 HASATTRIBUTE Functions

Verifies whether an attribute has been defined for `DOMELEMENT`, or has a default value.

See Also:

DOMElement Subprograms

Syntax

Verifies whether an attribute with the specified name has been defined for `DOMElement`:

```
DBMS_XMLDOM.HASATTRIBUTE(
   elem     IN  DOMELEMENT,
   name     IN  VARCHAR2)
 RETURN VARCHAR2;
```

Verifies whether an attribute with specified name and namespace URI has been defined for `DOMELEMENT`; namespace enabled:

```
DBMS_XMLDOM.HASATTRIBUTE(
   elem     IN  DOMELEMENT,
   name     IN  VARCHAR2,
   ns       IN  VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 210-87 HASATTRIBUTE Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `name` | Attribute name; \* matches any attribute |
| `ns` | Namespace |

#### 210.7.67 HASATTRIBUTES Function

This function returns whether this node has any attributes.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.HASATTRIBUTES(
   n       IN     DOMNODE)
 RETURN BOOLEAN;
```

Parameters

Table 210-88 HASATTRIBUTES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.68 HASCHILDNODES Function

This function determines whether this node has any children.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.HASCHILDNODES(
   n       IN     DOMNODE)
 RETURN BOOLEAN;
```

Parameters

Table 210-89 HASCHILDNODES Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.69 HASFEATURE Function

This function tests if the `DOMIMPLEMENTATION` implements a specific feature.

See Also:

DOMImplementation Subprograms

Syntax

```
DBMS_XMLDOM.HASFEATURE(
   di       IN     DOMIMPLEMENTATION,
   feature  IN     VARCHAR2,
   version  IN     VARCHAR2)
 RETURN BOOLEAN;
```

Parameters

Table 210-90 HASFEATURE Function Parameters

| Parameter | Description |
| --- | --- |
| `di` | `DOMIMPLEMENTATION` |
| `feature` | The feature to check for |
| `version` | The version of the DOM to check in |

#### 210.7.70 IMPORTNODE Function

This function imports a node from an external document and returns this new node.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.IMPORTNODE(
   doc            IN  DOMDOCUMENT,
   importedNode   IN  DOMNODE,
   deep           IN  BOOLEAN)
  RETURN DOMNODE;
```

Parameters

Table 210-91 IMPORTNODE Function Parameters

| Parameter | Description |
| --- | --- |
| `doc` | Document from which the node is imported |
| `importedNode` | Node to import |
| `deep` | Setting for recursive import.  - If this value is `TRUE,` the entire subtree of the node will be imported with the node. - If this value is `FALSE`, only the node itself will be imported. |

Usage Notes

Note that the ADOPTNODE Function removes the node from the source document while the IMPORTNODE Function clones the node in the source document.

#### 210.7.71 INSERTBEFORE Function

This function inserts the node `newchild` before the existing child node `refchild`. If `refchild` is `NULL`, insert `newchild` at the end of the list of children.

If `newchild` is a `DOCUMENTFRAGMENT` object, all of its children are inserted, in the same order, before `refchild`. If the `newchild` is already in the tree, it is first removed.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.INSERTBEFORE(
   n          IN     DOMNODE,
   newchild   IN     DOMNODE,
   refchild   IN     DOMNODE)
  RETURN DOMNode;
```

Parameters

Table 210-92 INSERTBEFORE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `newChild` | The child to be inserted in the `DOMNODE` |
| `refChild` | The reference node before which the `newchild` is to be inserted |

#### 210.7.72 INSERTDATA Procedure

This procedure inserts a string at the specified character offset.

See Also:

DOMCharacterData Subprograms

Syntax

```
DBMS_XMLDOM.INSERTDATA(
   cd       IN     DOMCHARACTERDATA,
   offset   IN     NUMBER,
   arg      IN     VARCHAR2);
```

Parameters

Table 210-93 INSERTDATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `offset` | The offset at which to insert the data |
| `arg` | The value to be inserted |

#### 210.7.73 ISNULL Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Checks if the specified `DOMNODE` is `NULL`. Returns `TRUE` if it is `NULL`, `FALSE ` otherwise (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.ISNULL(
  n        IN     DOMNODE) 
 RETURN BOOLEAN;
```

Checks that the specified `DOMATTR` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.ISNULL(
   a       IN     DOMATTR)
 RETURN BOOLEAN;
```

Checks that the specified `DOMCDATASECTION` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMCDataSection Subprograms):

```
DBMS_XMLDOM.ISNULL(
   cds      IN     DOMCDATASECTION)
 RETURN BOOLEAN;
```

Checks that the specified `DOMCHARACTERDATA` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMCharacterData Subprograms):

```
DBMS_XMLDOM.ISNULL(
   cd       IN     DOMCHARACTERDATA)
 RETURN BOOLEAN;
```

Checks that the specified `DOMCOMMENT` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMComment Subprograms):

```
DBMS_XMLDOM.ISNULL(
   com       IN     DOMCOMMENT)
 RETURN BOOLEAN;
```

Checks that the specified `DOMDOCUMENT` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.ISNULL(
   doc       IN     DOMDOCUMENT)
 RETURN BOOLEAN;
```

Checks that the specified `DOMDOCUMENTFRAGMENT` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE ` otherwise (See Also: DOMDocumentFragment Subprograms):

```
DBMS_XMLDOM.ISNULL(
   df       IN     DOMDOCUMENTFRAGMENT)
 RETURN BOOLEAN;
```

Checks that the specified `DOMDOCUMENTTYPE` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMDocumentType Subprograms):

```
DBMS_XMLDOM.ISNULL(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN BOOLEAN;
```

Checks that the specified `DOMELEMENT` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.ISNULL(
   elem     IN     DOMELEMENT)
 RETURN BOOLEAN;
```

Checks that the specified `DOMENTITY ` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMEntity Subprograms):

```
DBMS_XMLDOM.ISNULL(
   ent       IN     DOMENTITY)
 RETURN BOOLEAN;
```

Checks that the specified `DOMENTITYREFERENCE` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMEntityReference Subprograms):

```
DBMS_XMLDOM.ISNULL(
   EREF       IN     DOMENTITYREFERENCE)
 RETURN BOOLEAN;
```

Checks that the specified `DOMIMPLEMENTATION` is `NULL`; returns `TRUE` if it is `NULL` (See Also: DOMImplementation Subprograms):

```
DBMS_XMLDOM.ISNULL(
   di       IN     DOMIMPLEMENTATION)
 RETURN BOOLEAN;
```

Checks that the specified `DOMNAMEDNODEMAP` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMNamedNodeMap Subprograms):

```
DBMS_XMLDOM.ISNULL(
   nnm       IN     DOMNAMEDNODEMAP)
 RETURN BOOLEAN;
```

Checks that the specified `DOMNODELIST` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMNodeList Subprograms):

```
DBMS_XMLDOM.ISNULL(
   nl       IN     DOMNODELIST)
 RETURN BOOLEAN;
```

Checks that the specified `DOMNOTATION` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMNotation Subprograms):

```
DBMS_XMLDOM.ISNULL(
   n       IN     DOMNOTATION)
 RETURN BOOLEAN;
```

Checks that the specified `DOMPROCESSINGINSTRUCTION` is `NULL`; returns `TRUE` if it is NULL, `FALSE` otherwise (See Also: DOMProcessingInstruction Subprograms):

```
DBMS_XMLDOM.ISNULL(
   pi       IN     DOMPROCESSINGINSTRUCTION)
 RETURN BOOLEAN;
```

Checks that the specified `DOMTEXT` is `NULL`; returns `TRUE` if it is `NULL`, `FALSE` otherwise (See Also: DOMText Subprograms):

```
DBMS_XMLDOM.ISNULL(
   t       IN     DOMTEXT)
 RETURN BOOLEAN;
```

Parameters

Table 210-94 ISNULL Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to check |
| `a` | `DOMATTR` to check |
| `cds` | `DOMCDATASECTION` to check |
| `cd` | `DOMCHARACTERDATA` to check |
| `com` | `DOMCOMMENT` to check |
| `doc` | `DOMDOCUMENT ` to check |
| `dF` | `DOMDOCUMENTFRAGMENT` to check |
| `dt` | `DOMDOCUMENTTYPE` to check |
| `elem` | `DOMELEMENT` to check |
| `ent` | `DOMENTITY ` to check |
| `eref` | `DOMENTITYREFERENCE` to check |
| `di` | `DOMIMPLEMENTATION` to check |
| `nnm` | `DOMNAMENODEMAP` to check |
| `nl` | `DOMNODELIST ` to check |
| `n` | `DOMNOTATION` to check |
| `pi` | `DOMPROCESSINGINSTRUCTION` to check |
| `t` | `DOMTEXT` to check |

#### 210.7.74 ITEM Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Returns the item in the map which corresponds to the ` INDEX` parameter. If `INDEX` is greater than or equal to the number of nodes in this map, this returns `NULL` (See Also: DOMNamedNodeMap Subprograms):

```
DBMS_XMLDOM.ITEM(
   nnm       IN     DOMNAMEDNODEMAP,
   index     IN     NUMBER)
 RETURN DOMNODE;
```

Returns the item in the collection which corresponds to the `INDEX ` parameter. If index is greater than or equal to the number of nodes in the list, this returns `NULL` (See Also: DOMNodeList Subprograms):

```
DBMS_XMLDOM.ITEM(
   nl       IN     DOMNODELIST,
   index    IN     NUMBER)
 RETURN DOMNODE;
```

Parameters

Table 210-95 ITEM Function Parameters

| Parameter | Description |
| --- | --- |
| `nnm` | `DOMNAMEDNODEMAP` |
| `index` | The index in the node map at which the item is to be retrieved |
| `nl` | `DOMNODELIST` |
| `index` | The index in the ` NodeList` used to retrieve the item |

#### 210.7.75 MAKEATTR Function

This function casts a specified `DOMNODE` to a `DOMATTR`, and returns the `DOMATTR`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEATTR(
   n       IN     DOMNODE)
 RETURN DOMATTR;
```

Parameters

Table 210-96 MAKEATTR Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.76 MAKECDATASECTION Function

This function casts a specified `DOMNODE` to a `DOMCDATASECTION`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKECDATASECTION(
   n       IN     DOMNODE)
 RETURN DOMCDATASECTION;
```

Parameters

Table 210-97 MAKECDATASECTION Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.77 MAKECHARACTERDATA Function

This function casts a specified `DOMNODE` to a `DOMCHARACTERDATA`, and returns the `DOMCHARACTERDATA`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKECHARACTERDATA(
   n       IN     DOMNode)
 RETURN DOMCharacterData;
```

Parameters

Table 210-98 MAKECHARACTERDATA Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.78 MAKECOMMENT Function

This function casts a specified `DOMNODE` to a `DOMCOMMENT`, and returns the `DOMCOMMENT`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKECOMMENT(
   n       IN     DOMNODE)
 RETURN DOMCOMMENT;
```

Parameters

Table 210-99 MAKECOMMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.79 MAKEDOCUMENT Function

This function casts a specified `DOMNODE` to a `DOMDOCUMENT`, and returns the `DOMDOCUMENT`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEDOCUMENT(
   n       IN     DOMNODE)
 RETURN DOMDocument;
```

Parameters

Table 210-100 MAKEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.80 MAKEDOCUMENTFRAGMENT Function

This function casts a specified `DOMNODE` to a `DOMDOCUMENTFRAGMENT`, and returns the `DOMDOCUMENTFRAGMENT`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENTFRAGMENT;
```

Parameters

Table 210-101 MAKEDOCUMENTFRAGMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.81 MAKEDOCUMENTTYPE Function

This function casts a specified `DOMNODE` to a `DOMDOCUMENTTYPE` and returns the `DOMDOCUMENTTYPE`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEDOCUMENTTYPE(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENTTYPE;
```

Parameters

Table 210-102 MAKEDOCUMENTTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast. |

#### 210.7.82 MAKEELEMENT Function

This function casts a specified `DOMNODE` to a `DOMELEMENT`, and returns the `DOMELEMENT`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEELEMENT(
   n       IN     DOMNODE)
 RETURN DOMELEMENT;
```

Parameters

Table 210-103 MAKEELEMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.83 MAKEENTITY Function

This function casts a specified `DOMNODE` to a `DOMENTITY`, and returns the `DOMENTITY`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEENTITY(
   n       IN     DOMNODE)
 RETURN DOMENTITY;
```

Parameters

Table 210-104 MAKEENTITY Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.84 MAKEENTITYREFERENCE Function

This function casts a specified `DOMNODE` to a `DOMENTITYREFERENCE`, and returns the `DOMENTITYREFERENCE`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEENTITYREFERENCE(
   n       IN     DOMNODE)
 RETURN DOMENTITYREFERENCE;
```

Parameters

Table 210-105 MAKEENTITYREFERENCE Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.85 MAKENODE Functions

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Casts specified `DOMATTR` to a `DOMNODE`, and returns the `DOMNODE` (See Also: DOMAttr Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   a        IN     DOMATTR)
 RETURN DOMNODE;
```

Casts the `DOMCDATASECTION` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMCDataSection Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   cds      IN     DOMCDATASECTION)
 RETURN DOMNODE;
```

Casts the specified `DOMCHARACTERDATA` as a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMCharacterData Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   cd       IN     DOMCHARACTERDATA)
 RETURN DOMNODE;
```

Casts the specified `DOMCOMMENT` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMComment Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   com      IN     DOMCOMMENT)
 RETURN DOMNODE;
```

Casts the `DOMDOCUMENT ` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   doc      IN     DOMDOCUMENT)
 RETURN DOMNODE;
```

Casts the specified `DOMDOCUMENTFRAGMENT` to a `DOMNODE`, and returns that `DOMNODE ` (See Also: DOMDocumentFragment Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   df       IN     DOMDOCUMENTFRAGMENT)
 RETURN DOMNode;
```

Casts the specified `DOMDOCUMENTTYPE` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMDocumentType Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN DOMNODE;
```

Casts the specified `DOMELEMENT` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMElement Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   elem       IN     DOMELEMENT)
 RETURN DOMNODE;
```

Casts specified `DOMENTITY ` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMEntity Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   ent       IN     DOMENTITY)
 RETURN DOMNODE;
```

Casts the `DOMENTITYREFERENCE` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMEntityReference Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   eref       IN     DOMENTITYREFERENCE)
 RETURN DOMNODE;
```

Casts the `DOMNOTATION` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMNotation Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   n       IN     DOMNOTATION)
 RETURN DOMNODE;
```

Casts the `DOMPROCESSINGINSTRUCTION` to a `DOMNODE`, and returns the `DOMNODE` (See Also: DOMProcessingInstruction Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   pi       IN     DOMPROCESSINGINSTRUCTION)
 RETURN DOMNODE;
```

Casts the `DOMTEXT` to a `DOMNODE`, and returns that `DOMNODE` (See Also: DOMText Subprograms):

```
DBMS_XMLDOM.MAKENODE(
   t       IN     DOMTEXT)
 RETURN DOMNODE;
```

Parameters

Table 210-106 MAKENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` to cast |
| `cds` | `DOMCDATASECTION` to cast |
| `cd` | `DOMCHARACTERDATA` to cast |
| `com` | `DOMCOMMENT` to cast |
| `doc` | `DOMDOCUMENT` to cast |
| `df` | `DOMDOCUMENTFRAGMENT` to cast |
| `dt` | `DOMDOCUMENTTYPE` to cast |
| `elem` | `DOMELEMENT` to cast |
| `ent` | `DOMENTITY ` to cast |
| `eref` | `DOMENTITYREFERENCE` to cast |
| `n` | `DOMNOTATION` to cast |
| `pi` | `DOMPROCESSINGINSTRUCTION` to cast |
| t | `DOMTEXT` to cast |

#### 210.7.86 MAKENOTATION Function

This function casts a specified `DOMNODE` to a `DOMNOTATION`, and returns the `DOMNOTATION`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKENOTATION(
   n       IN     DOMNODE)
 RETURN DOMNOTATION;
```

Parameters

Table 210-107 MAKENOTATION Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.87 MAKEPROCESSINGINSTRUCTION Function

This function casts a specified `DOMNODE` to a `DOMPROCESSINGINSTRUCTION`, and returns the `Domprocessinginstruction`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION(
   n       IN     DOMNODE)
 RETURN DOMPROCESSINGINSTRUCTION;
```

Parameters

Table 210-108 MAKEPROCESSINGINSTRUCTION Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.88 MAKETEXT Function

This function casts a specified `DOMNODE` to a `DOMTEXT`, and returns the `DOMTEXT`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.MAKETEXT(
   n       IN     DOMNODE)
 RETURN DOMTEXT;
```

Parameters

Table 210-109 MAKETEXT Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` to cast |

#### 210.7.89 NEWDOMDOCUMENT Functions

This function returns a new `DOMDOCUMENT` instance.

See Also:

DOMDocument Subprograms

Syntax

Returns a new `DOMDOCUMENT` instance:

```
DBMS_XMLDOM.NEWDOMDOCUMENT
 RETURN DOMDOCUMENT;
```

Returns a new `DOMDOCUMENT` instance created from the specified `XMLType` object:

```
DBMS_XMLDOM.NEWDOMDOCUMENT(
   xmldoc    IN SYS.XMLTYPE)
 RETURN DOMDOCUMENT;
```

Returns a new `DOMDOCUMENT` instance created from the specified `CLOB`:

```
DBMS_XMLDOM.NEWDOMDOCUMENT(
   cl       IN    CLOB)
 RETURN DOMDOCUMENT;
```

Parameters

Table 210-110 NEWDOMDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `xmldoc` | `XMLType` source for the `DOMDOCUMENT` |
| `cl` | `CLOB` source for the `DOMDOCUMENT` |

#### 210.7.90 NORMALIZE Procedure

This procedure normalizes the text children of the `DOMELEMENT`.

See Also:

DOMElement Subprograms

Syntax

```
DBMS_XMLDOM.NORMALIZE(
   elem       IN     DOMELEMENT);
```

Parameters

Table 210-111 NORMALIZE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |

#### 210.7.91 REMOVEATTRIBUTE Procedures

This procedure removes an attribute from the `DOMELEMENT` by name.

See Also:

DOMElement Subprograms

Syntax

Removes the value of a `DOMELEMENT` 's attribute by name:

```
DBMS_XMLDOM.REMOVEATTRIBUTE(
   elem     IN    DOMELEMENT,
   name     IN    VARCHAR2);
```

Removes the value of a `DOMELEMENT` 's attribute by name and namespace URI.

```
DBMS_XMLDOM.REMOVEATTRIBUTE(
   elem     IN    DOMELEMENT,
   name     IN    VARCHAR2,
   ns       IN    VARCHAR2);
```

Parameters

Table 210-112 REMOVEATTRIBUTE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `name` | Attribute name |
| `ns` | Namespace |

#### 210.7.92 REMOVEATTRIBUTENODE Function

This function removes the specified attribute node from the `DOMELEMENT`. The method returns the removed node.

See Also:

DOMElement Subprograms

Syntax

```
DBMS_XMLDOM.REMOVEATTRIBUTENODE(
   elem       IN     DOMELEMENT,
   oldAttr    IN     DOMATTR)
  RETURN DOMAttr;
```

Parameters

Table 210-113 REMOVEATTRIBUTENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT`. |
| `oldAttr` | The old `DOMATTR`. |

#### 210.7.93 REMOVECHILD Function

This function removes the child node indicated by `oldchild` from the list of children, and returns it.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.REMOVECHILD(
   n          IN     DOMNode,
   oldchild   IN     DOMNode)
 RETURN DOMNODE;
```

Parameters

Table 210-114 REMOVECHILD Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `oldCHild` | The child of the node `n` to be removed |

#### 210.7.94 REMOVENAMEDITEM Function

This function removes a node, specified by name, from the map and returns this node.

When this map contains the attributes attached to an element, if the removed attribute is known to have a default value, an attribute immediately appears containing the default value as well as the corresponding namespace URI, local name, and prefix when applicable.

See Also:

DOMNamedNodeMap Subprograms

Syntax

Removes a node specified by name:

```
DBMS_XMLDOM.REMOVENAMEDITEM(
   nnm      IN     DOMNamedNodeMap,
   name     IN     VARCHAR2)
 RETURN DOMNode;
```

Removes a node specified by name and namespace URI:

```
DBMS_XMLDOM.REMOVENAMEDITEM(
   nnm      IN     DOMNamedNodeMap,
   name     IN     VARCHAR2,
   ns       IN     VARCHAR2)
 RETURN DOMNode;
```

Parameters

Table 210-115 REMOVENAMEDITEM Function Parameters

| Parameter | Description |
| --- | --- |
| `nnm` | `DOMNamedNodeMap` |
| `name` | The name of the item to be removed from the map |
| `ns` | Namespace |

#### 210.7.95 REPLACECHILD Function

This function replaces the child node `oldchild` with `newchild` in the list of children, and returns the `oldchild` node.

If `newchild` is a `DocumentFragment` object, `oldchild` is replaced by all of the `DocumentFragment` children, which are inserted in the same order. If the `newchild` is already in the tree, it is first removed.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.REPLACECHILD(
   n           IN     DOMNode,
   newchild    IN     DOMNode,
   oldchild    IN     DOMNode)
 RETURN DOMNode;
```

Parameters

Table 210-116 REPLACECHILD Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` |
| `newchild` | The new child which is to replace the old child |
| `oldchild` | The child of the node n which is to be replaced |

#### 210.7.96 REPLACEDATA Procedure

This procedure changes a range of characters in the node. Upon success, data and length reflect the change.

See Also:

DOMCharacterData Subprograms

Syntax

```
DBMS_XMLDOM.REPLACEDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER,
   arg       IN     VARCHAR2);
```

Parameters

Table 210-117 REPLACEDATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `offset` | The offset at which to replace |
| `cnt` | The number of characters to replace |
| `arg` | The value to replace with |

#### 210.7.97 RESOLVENAMESPACEPREFIX Function

This function resolves the specified namespace prefix, and returns the resolved namespace.

See Also:

DOMElement Subprograms

Syntax

```
DBMS_XMLDOM.RESOLVENAMESPACEPREFIX(
   elem       IN     DOMELEMENT,
   prefix     IN     VARCHAR2) 
 RETURN VARCHAR2;
```

Parameters

Table 210-118 RESOLVENAMESPACEPREFIX Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `prefix` | Namespace prefix |

#### 210.7.98 SETATTRIBUTE Procedures

This procedure sets the value of a `DOMELEMENT` 's attribute by name.

See Also:

DOMElement Subprograms

Syntax

Sets the value of a `DOMELEMENT` 's attribute by name:

```
DBMS_XMLDOM.SETATTRIBUTE(
   elem       IN  DOMELEMENT,
   name       IN  VARCHAR2,
   newvalue   IN  VARCHAR2);
```

Sets the value of a `DOMElement` 's attribute by name and namespace URI:

```
DBMS_XMLDOM.SETATTRIBUTE(
   elem       IN  DOMELEMENT,
   name       IN  VARCHAR2,
   newvalue   IN  VARCHAR2,
   ns         IN  VARCHAR2);
```

Parameters

Table 210-119 SETATTRIBUTE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `name` | Attribute name |
| `newvalue` | Attribute value |
| `ns` | Namespace |

#### 210.7.99 SETATTRIBUTENODE Functions

This function adds a new attribute node to the `DOMELEMENT`.

See Also:

DOMElement Subprograms

Syntax

Adds a new attribute node to the `DOMELEMENT`:

```
DBMS_XMLDOM.SETATTRIBUTENODE(
   elem      IN  DOMELEMENT,
   newAttr   IN  DOMATTR)
 RETURN DOMATTR;
```

Adds a new attribute node to the `DOMElement`; namespace enabled:

```
DBMS_XMLDOM.SETATTRIBUTENODE(
   elem      IN  DOMELEMENT,
   newAttr   IN  DOMATTR,
   ns        IN  VARCHAR2)
 RETURN DOMATTR;
```

Parameters

Table 210-120 SETATTRIBUTENODE Function Parameters

| Parameter | Description |
| --- | --- |
| `elem` | The `DOMELEMENT` |
| `newAttr` | The new `DOMATTR` |
| `ns` | The namespace |

#### 210.7.100 SETCHARSET Procedure

This function sets the characterset of the DOM document.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.SETCHARSET(
   doc      IN    DOMDocument,
   charset  IN    VARCHAR2);
```

Parameters

Table 210-121 SETCHARSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| doc | `DOM` document |
| charset | Characterset |

Usage Notes

This is used for WRITETOFILE Procedures if not explicitly specified at that time.

#### 210.7.101 SETDATA Procedures

This overloaded procedure sets character data or `DOMPROCESSINGINSTRUCTION` content data. The specific functionality is described in the syntax declarations.

Syntax

Sets the character data of the node that implements this interface (See Also: DOMCharacterData Subprograms):

```
DBMS_XMLDOM.SETDATA(
   cd       IN     DOMCHARACTERDATA,
   data     IN     VARCHAR2);
```

Sets the content data of the `DOMPROCESSINGINSTRUCTION` (See Also: DOMProcessingInstruction Subprograms):

```
DBMS_XMLDOM.SETDATA(
   pi       IN     DOMPROCESSINGINSTRUCTION,
   data     IN     VARCHAR2);
```

Parameters

Table 210-122 SETDATA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `data` | The data to which the node is set |
| `pi` | `DOMPROCESSINGINSTRUCTION` |
| `data` | New processing instruction content data |

#### 210.7.102 SETDOCTYPE Procedure

Given a DOM document, this procedure creates a new DTD with the specified name, system id and public id and sets it in the document.

This DTD can later be retrieved using the GETDOCTYPE Function.

Syntax

```
DBMS_XMLDOM.SETDOCTYPE(
  doc     IN   DOMDocument, 
  name    IN   VARCHAR2,
  sysid   IN   VARCHAR2, 
  pubid   IN   VARCHAR2);
```

Parameters

Table 210-123 SETDOCTYPE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | The document whose DTD has to be set |
| `name` | The name that the doctype needs to be initialized with |
| `sysid` | The system ID that the doctype needs to be initialized with |
| `pubid` | The public ID that the doctype needs to be initialized with |

#### 210.7.103 SETNAMEDITEM Function

This function adds a node using its `NodeName` attribute.

If a node with that name is already present in this map, it is replaced by the new one. The old node is returned on replacement; if no replacement is made, `NULL` is returned.

As the `NodeName` attribute is used to derive the name under which the node must be stored, multiple nodes of certain types, those that have a "special" string value, cannot be stored because the names would clash. This is seen as preferable to allowing nodes to be aliased.

See Also:

DOMNamedNodeMap Subprograms

Syntax

Adds a node using its `NodeName` attribute:

```
DBMS_XMLDOM.SETNAMEDITEM(
   nnm     IN     DOMNAMEDNODEMAP,
   arg     IN     DOMNODE)
 RETURN DOMNode;
```

Adds a node using its `NodeName` attribute and namespace URI:

```
DBMS_XMLDOM.SETNAMEDITEM(
   nnm     IN     DOMNAMEDNODEMAP,
   arg      IN    DOMNODE,
   ns      IN     VARCHAR2)
 RETURN DOMNode;
```

Parameters

Table 210-124 SETNAMEDITEM Function Parameters

| Parameter | Description |
| --- | --- |
| `nnm` | `DOMNAMEDNODEMAP` |
| `arg` | The Node to be added using its `NodeName` attribute |
| `ns` | Namespace |

#### 210.7.104 SETNODEVALUE Procedure

This procedure sets the value of this node, depending on its type. When it is defined to be `NULL`, setting it has no effect.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.SETNODEVALUE(
   n         IN     DOMNODE,
   nodeValue IN     VARCHAR2);
```

Parameters

Table 210-125 SETNODEVALUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNode` |
| `nodeValue` | The value to which node is set |

#### 210.7.105 SETNODEVALUEASBINARYSTREAM Function & Procedure

The operation of these subprograms is described in the syntax section.

See Also:

DOMNode Subprograms

Syntax

This function returns an instance of the PL/SQL `XMLBINARYOUTPUTSTREAM` into which the caller can write the node value. The datatype of the node must be `RAW` or `BLOB` – if not, an exception is raised.

```
DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM (
   n      IN     DOMNODE)
 RETURN SYS.UTL_BINARYOUTPUTSTREAM;
```

Using this procedure, the application passes in an implementation of `sys`.`utl_BinaryInputStream` from which XDB reads data to populate the node. The datatype of the node must be `RAW` or BLOB – if not an exception is raised.

```
DBMS_XMLDOM.SETNODEVALUEASBINARYSTREAM (
   n        in   DOMNODE, 
   value    in   SYS.UTL_BINARYINPUTSTREAM);
```

Parameters

Table 210-126 SETNODEVALUEASBINARYSTREAM Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| value | `BINARYINPUTSTREAM` |

#### 210.7.106 SETNODEVALUEASCHARACTERSTREAM Function & Procedure

The operation of these subprograms is described in the syntax section.

See Also:

DOMNode Subprograms

Syntax

This function returns an instance of the PL/SQL `XMLCHARACTEROUTPUTSTREAM` type into which the caller can write the node value. The datatype of the node can be any valid XDB datatype. If the type is not character or `CLOB`, the character data written to the stream is converted to the node datatype. If the datatype of the node is character or `CLOB`, then the character data written to the stream is converted from PL/SQL session character set to the character set of the node.

```
DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM  (
   n        IN     DOMNODE)
 RETURN SYS.UTL_CHARACTEROUTPUTSTREAM;
```

Using this procedure, the application passes in an implementation of `SYS`.`UTL_CHARACTERINPUTSTREAM` from which XDB reads to populate the node. The datatype of the node may be any valid type supported by XDB. If a non-character datatype, the character data read from the stream is converted to the datatype of the node. If the datatype of the node is either character or `CLOB`, then no conversion occurs and the character set of the node becomes the character set of the PL/SQL session.

```
DBMS_XMLDOM.SETNODEVALUEASCHARACTERSTREAM  (
   n        IN   DOMNODE,
   value    IN   SYS.UTL_CHARACTERINPUTSTREAM);
```

Parameters

Table 210-127 SETNODEVALUEASCHARACTERSTREAM Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| value | `CHARACTERINPUTSTREAM` |

#### 210.7.107 SETPREFIX Procedure

This procedure sets the namespace prefix for this node to the specified value.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.SETPREFIX(
   n       IN     DOMNODE,
   prefix  IN     VARCHAR2);
```

Parameters

Table 210-128 SETPREFIX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `prefix` | The value for the namespace prefix of the node |

#### 210.7.108 SETSTANDALONE Procedure

This procedure sets the standalone property of the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.SETSTANDALONE(
   doc         IN     DOMDOCUMENT,
   newvalue    IN     VARCHAR2);
```

Parameters

Table 210-129 SETSTANDALONE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `newvalue` | Value of the standalone property of the document |

#### 210.7.109 SETVALUE Procedure

This procedure sets the value of the attribute.

See Also:

DOMAttr Subprograms

Syntax

```
DBMS_XMLDOM.SETVALUE(
   a       IN     DOMATTR,
   value   IN     VARCHAR2);
```

Parameters

Table 210-130 SETVALUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `a` | `DOMATTR` |
| `value` | The value to which to set the attribute |

#### 210.7.110 SETVERSION Procedure

This procedure sets the version of the `DOMDOCUMENT`.

See Also:

DOMDocument Subprograms

Syntax

```
DBMS_XMLDOM.SETVERSION(
   doc        IN     DOMDOCUMENT,
   version    IN     VARCHAR2);
```

Parameters

Table 210-131 SETVERSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `doc` | `DOMDOCUMENT` |
| `version` | The version of the document |

#### 210.7.111 SPLITTEXT Function

This function breaks this `DOMTEXT` node into two `DOMTEXT` nodes at the specified offset.

See Also:

DBMS\_XMLDOM DOMText Subprograms

Syntax

```
DBMS_XMLDOM.SPLITTEXT(
   t        IN     DOMTEXT,
   offset   IN     NUMBER)
 RETURN DOMText;
```

Parameters

Table 210-132 SPLITTEXT Function Parameters

| Parameter | Description |
| --- | --- |
| `t` | `DOMTEXT` |
| `offset` | Offset at which to split |

#### 210.7.112 SUBSTRINGDATA Function

This function extracts a range of data from the node.

See Also:

DOMCharacterData Subprograms

Syntax

```
DBMS_XMLDOM.SUBSTRINGDATA(
   cd        IN     DOMCHARACTERDATA,
   offset    IN     NUMBER,
   cnt       IN     NUMBER)
 RETURN VARCHAR2;
```

Parameters

Table 210-133 SUBSTRINGDATA Function Parameters

| Parameter | Description |
| --- | --- |
| `cd` | `DOMCHARACTERDATA` |
| `offset` | The starting offset of the data from which to get the data |
| `cnt` | The number of characters (from the offset) of the data to get |

#### 210.7.113 USEBINARYSTREAM Function

This function returns `TRUE` if the datatype of the node is `RAW` or `BLOB`, so that the node value may be read or written using an `UTL_BINARYINPUTSTREAM` or `UTL_BINARYOUTPUTSTREAM`.

If a value of `FALSE` is returned, the node value may only be accessed through an `UTL_CHARACTERINPUTSTREAM` or `UTL_CHARACTEROUTPUTSTREAM`.

See Also:

DOMNode Subprograms

Syntax

```
DBMS_XMLDOM.USEBINARYSTREAM   (
   n        IN     DOMNODE)
 RETURN BOOLEAN;
```

Parameters

Table 210-134 USEBINARYSTREAM Function Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |

#### 210.7.114 WRITETOBUFFER Procedures

`WRITETOBUFFER` is an overloaded procedure that writes an XML node, XML document, or a document fragment to a specified buffer.

This procedure is overloaded. The specific forms of functionality are described along with the syntax declarations.

Syntax

Writes XML node to specified buffer using the database character set (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.WRITETOBUFFER( 
   n        IN      DOMNODE, 
   buffer   IN OUT  VARCHAR2);
```

Writes XML document to a specified buffer using database character set (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.WRITETOBUFFER( 
   doc       IN      DOMDOCUMENT, 
   buffer    IN OUT  VARCHAR2);
```

Writes the contents of the specified document fragment into a buffer using the database character set (See Also: DOMDocumentFragment Subprograms):

```
DBMS_XMLDOM.WRITETOBUFFER(
   df        IN      DOMDOCUMENTFRAGMENT,
   buffer    IN OUT  VARCHAR2);
```

Parameters

Table 210-135 WRITETOBUFFER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `buffer` | Buffer to which to write |
| `doc` | `DOMDOCUMENT` |
| `df` | DOM document fragment |

#### 210.7.115 WRITETOCLOB Procedures

`WRITETOCLOB` is an overloaded procedure that writes an XML node or document to a specified `CLOB`.

The specific forms of functionality are described along with the syntax declarations.

Syntax

Writes XML node to specified `CLOB` using the database character set (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.WRITETOCLOB(
   n       IN      DOMNODE, 
   cl      IN OUT  CLOB);
```

Writes XML document to a specified `CLOB` using database character set (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.WRITETOCLOB(
   doc     IN      DOMDOCUMENT, 
   cl      IN OUT  CLOB);
```

Parameters

Table 210-136 WRITETOCLOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `cl` | `CLOB` to which to write |
| `doc` | `DOMDOCUMENT` |

#### 210.7.116 WRITETOFILE Procedures

This overloaded procedure writes an XML node or XML document to a specified node.

The specific forms of functionality are described along with the syntax declarations.

Syntax

Writes XML node to specified file using the database character set (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.WRITETOFILE(
   n          IN      DOMNODE,
   fileName   IN      VARCHAR2);
```

Writes XML node to specified file using the specified character set, which is passed in as a separate parameter (See Also: DOMNode Subprograms):

```
DBMS_XMLDOM.WRITETOFILE(
   n          IN      DOMNODE,
   fileName   IN      VARCHAR2,
   charset    IN      VARCHAR2);
```

Writes an XML document to a specified file using database character set (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.WRITETOFILE(
   doc        IN   DOMDOCUMENT,
   filename   IN   VARCHAR2);
```

Writes an XML document to a specified file using specified character set (See Also: DOMDocument Subprograms):

```
DBMS_XMLDOM.WRITETOFILE(
   doc       IN   DOMDOCUMENT,
   fileName  IN   VARCHAR2,
   charset   IN   VARCHAR2);
```

Parameters

Table 210-137 WRITETOFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `n` | `DOMNODE` |
| `fileName` | File to which to write. The filename should be in the format of `database_directory_object_name/filename`, for example `mydir/filename` (on windows, use `\` instead of ` /`). |
| `charset` | specified character set |
| `doc` | `DOMDOCUMENT` |
| `charset` | Character set |
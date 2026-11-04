---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/references-identifiers.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## References to Identifiers

When referencing an identifier, you use a name that is either simple, qualified, remote, or both qualified and remote.

The simple name of an identifier is the name in its declaration. For example:

```
DECLARE
  a INTEGER;  -- Declaration
BEGIN
  a := 1;     -- Reference with simple name
END;
/
```

If an identifier is declared in a named PL/SQL unit, you can (and sometimes must) reference it with its qualified name. The syntax (called dot notation) is:

```
unit_name.simple_identifier_name
```

For example, if package `p` declares identifier `a`, you can reference the identifier with the qualified name `p`.`a`. The unit name also can (and sometimes must) be qualified. You must qualify an identifier when it is not visible (see " [Scope and Visibility of Identifiers](scope-and-visibility-identifiers.md) ").

If the identifier names an object on a remote database, you must reference it with its remote name. The syntax is:

```
simple_identifier_name@link_to_remote_database
```

If the identifier is declared in a PL/SQL unit on a remote database, you must reference it with its qualified remote name. The syntax is:

```
unit_name.simple_identifier_name@link_to_remote_database
```

You can create synonyms for remote schema objects, but you cannot create synonyms for objects declared in PL/SQL subprograms or packages. To create a synonym, use the SQL statement `CREATE` `SYNONYM`, explained in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01401).

For information about how PL/SQL resolves ambiguous names, see [PL/SQL Name Resolution](plsql-name-resolution.md).

Note:

You can reference identifiers declared in the packages `STANDARD` and `DBMS_STANDARD` without qualifying them with the package names, unless you have declared a local identifier with the same name (see " [Scope and Visibility of Identifiers](scope-and-visibility-identifiers.md) ").
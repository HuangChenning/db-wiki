---
title: Directory Usage Parameters (ldap.ora)
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/ldap.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 9 Directory Usage Parameters (ldap.ora)

This chapter provides a complete listing of the `ldap.ora` file configuration parameters.

This chapter contains the following topics:

- Overview of Directory Server Usage File
- Directory Usage Parameters

## Overview of Directory Server Usage File

The `ldap.ora` file contains directory usage configuration parameters created by [Oracle Internet Directory](glossary.md) Configuration Assistant or [Oracle Net Configuration Assistant](glossary.md). Do not modify these parameters or their settings.

When created with Oracle Internet Directory Configuration Assistant, `ldap.ora` is located in the `ORACLE_HOME/ldap/admin` directory. When created with Oracle Net Configuration Assistant, the `ldap.ora` file is located in the `ORACLE_HOME/network/admin` directory. The `ldap.ora` file can also be stored in the directory specified by the `LDAP_ADMIN` or `TNS_ADMIN` environment variable.

## Directory Usage Parameters

This section lists and describes the following `ldap.ora` file configuration parameters:

- DIRECTORY\_SERVERS
- DIRECTORY\_SERVER\_TYPE
- DEFAULT\_ADMIN\_CONTEXT

### DIRECTORY\_SERVERS

Purpose

To list the host names and port number of the primary and alternate LDAP [directory server](glossary.md) s.

Values

```
host:port[:sslport]
```

Example

```
DIRECTORY_SERVERS=(ldap-server:389, raffles:400:636)
```

### DIRECTORY\_SERVER\_TYPE

Purpose

To specify the type of directory server that is being used.

Values

Example

```
DIRECTORY_SERVER_TYPE=oid
```

### DEFAULT\_ADMIN\_CONTEXT

Purpose

To specify the default directory entry that contains an [Oracle Context](glossary.md) from which connect identifiers can be created, modified, or looked up.

Values

Valid [distinguished name (DN)](glossary.md)

Example

```
DEFAULT_ADMIN_CONTEXT="o=OracleSoftware,c=US"
```
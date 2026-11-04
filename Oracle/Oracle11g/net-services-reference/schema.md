---
title: LDAP Schema for Oracle Net Services
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/schema.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## C LDAP Schema for Oracle Net Services

This appendix describes the [Oracle schema](glossary.md) object classes and [attribute](glossary.md) s defined in the [directory server](glossary.md) for Oracle Net Services objects. It does not describe object classes and attributes reserved for future functionality or used by other Oracle products.

This appendix contains the following topics:

- Structural Object Classes
- Attributes

## Structural Object Classes

The Oracle schema supports the structural object classes for Oracle Net [directory naming](glossary.md) lookups. Table C-1 lists the structural object classes for Oracle Connection Manager.

Table C-1 Oracle Net Structural Object Classes

| Object Class | Attributes | Description |
| --- | --- | --- |
| orclDBServer | - `orclNetDescName` - `orclVersion` | Defines the attributes for database service entries. |
| orclNetService | - `orclNetDescName` - `orclVersion` | Defines the attributes for [net service name](glossary.md) entries. |
| orclNetServiceAlias | - `orclNetDescName` - `orclVersion` | Defines the attributes for [net service alias](glossary.md) entries. |
| orclNetDescription | - `orclNetAddrList` - `orclNetInstanceName` - `orclNetConnParamList` - `orclNetFailover` - `orclNetLoadBalance` - `orclNetSdu` - `orclNetServiceName` - `orclNetSourceRoute` - `orclSid` - `orclVersion` | Specifies a [connect descriptor](glossary.md) containing the [protocol address](glossary.md) of the [listener](glossary.md) and the connect information to the service |
| orclNetDescriptionList | - `orclNetDescList` - `orclVersion` | Specifies a list of connect descriptors. |
| orclNetAddress | - `orclNetAddressString` - `orclNetProtocol` - `orclVersion` | Specifies a listener protocol address. |
| orclNetAddressList | - `orclNetAddrList` - `orclNetFailover` - `orclNetLoadBalance` - `orclNetSourceRoute` - `orclVersion` | Specifies a list of protocol addresses. |
| orclNetDescriptionAux1 | - `orclNetSendBufSize` - `orclNetReceiveBufSize` - `orclNetFailoverModeString` - `orclNetInstanceRole` | Specifies auxiliary object class to add attributes to an orclNetDescription entry. |
| orclNetAddressAux1 | - `orclNetHostname` | Specifies an auxiliary object class to add attributes to an orclNetAddress entry. |

## Attributes

Table C-2 lists the attributes used for the object classes. This list is subject to change.

Table C-2 LDAP Schema Attributes for Oracle Net Services

| Attribute | Description |
| --- | --- |
| `orclCommonContextMap` | Allows the mapping of more than one default oracleContext in the directory server. |
| `orclNetAddrList` | Identifies one or more listener protocol addresses. |
| `orclNetAddressString` | Defines a listener protocol address. |
| `orclNetConnParamList` | Placeholder for connect data parameters. |
| `orclNetDescList` | Identifies one or more connect descriptors. |
| `orclNetDescName` | Identifies a connect descriptor or a list of connect descriptors. |
| `orclNetFailover` | Turns connect-time failover on for a protocol address list. |
| `orclNetFailoverModeString` | Instructs Oracle Net to fail over to a different listener if the first listener fails during run-time. Depending on the configuration, session or any `SELECT` statements that were in progress are automatically failed over. |
| `orclNetHostname` | Specifies the host name. |
| `orclNetInstanceName` | Specifies the instance name to access. |
| `orclNetInstanceRole` | Specifies a connection to the primary or secondary instance of an Oracle RAC configuration. |
| `orclNetLoadBalance` | Turns client load balancing on for a protocol address list. |
| `orclNetProtocol` | Identifies the protocol used in the `orclAddressString` attribute. |
| `orclNetReceiveBufSize` | Specifies the buffer space limit for receive operations of sessions. |
| `orclNetSdu` | Specifies the [session data unit (SDU)](glossary.md) size. |
| `orclNetSendBufSize` | Specifies the buffer space limit for send operations of sessions. |
| `orclNetServiceName` | Specifies the database service name in the `CONNECT_DATA` portion. |
| `orclNetSourceRoute` | Instructs Oracle Net to use each address in order until the destination is reached. |
| `orclSid` | Specifies the [Oracle System Identifier (SID)](glossary.md) in the `CONNECT_DATA` portion of a connection descriptor. |
| `orclVersion` | Specifies the version of software used to create the entry. |
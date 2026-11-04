---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/CLSDNSSD-00000.html
tags:
  - oracle
  - 21c
  - error-messages
---

CLSDNSSD-00000: no error.

Cause: Operation was successful.

Action: No action needed.

CLSDNSSD-00001: unknown error has occurred.

Cause: an unknown error has occurred.

Action: Contact Oracle Support Services.

CLSDNSSD-00002: no such name.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00003: memory allocation failed.

Cause: The DNS service discovery component was unable to allocate enough memory.

Action: If memory is low on the system, terminate other processes and/or threads and try the operation again. Otherwise, this is an internal error and Oracle Support Services should be contacted.

CLSDNSSD-00004: invalid parameter.

Cause: An parameter which had an invalid value was passed by the caller to the DNS service discovery library. This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00005: invalid reference.

Cause: An unknown DNS record reference was encountered.

Action: Contact Oracle Support Services.

CLSDNSSD-00006: invalid state.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00007: invalid flags.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00008: unsupported operation.

Cause: The DNS service discovery component attempted to perform an operation not supported by the library.

Action: Contact Oracle Support Services.

CLSDNSSD-00009: uninitialized.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00010: service already registered.

Cause: The user attempted to register a service that was already registered.

Action: A service should only be registered once.

CLSDNSSD-00011: service name conflict.

Cause: The user attempted to register a service whose name already exists.

Action: A different service name needs to be used.

CLSDNSSD-00012: invalid data in record.

Cause: The DNS service discovery component attempted to use a record with invalid data. This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00013: firewall.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00014: client software incompatible with server.

Cause: The version of the client software used by the DNS service discovery interface is not compatible with the version of the server software.

Action: Contact Oracle Support Services.

CLSDNSSD-00015: bad interface index.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00016: update refused.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00017: no such record.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00018: no auth.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00019: no such key.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00020: NAT Traversal.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00021: Double NAT traversal.

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00022: invalid time stamp in record

Cause: A DNS record contained an invalid time stamp. This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00023: invalid service type: "string".

Cause: The user specified a service type which does not conform to the standard specifed by RFC's 1034 and RFC 1123. The service type must be one or more characters and must start and end with a letter or digit. The interior characters may be letters, digits, or hyphens.

Action: Specify a service type which conforms to the RFC.

CLSDNSSD-00024: internal error: bad key

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00025: internal error: transient

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00026: service not running

Cause: The background daemon was not running.

Action: Contact Oracle Support Services.

CLSDNSSD-00027: internal error: NAT port mapping unsupported

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00028: internal error: NAT port mapping disabled

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00029: No Router

Cause: Either a router was not configured or there was no network connectivity.

Action: Contact Oracle Support Services.

CLSDNSSD-00030: internal error: polling mode

Cause: This is an internal error.

Action: Contact Oracle Support Services.

CLSDNSSD-00031: Query Time Out

Cause: The query timed out. Either the external DNS server sent a negative response or the select call timed out.

Action: Contact Oracle Support Services.

CLSDNSSD-03999: unknown error: number.

Cause: A DNS error code was returned that is not known to the system. This is an internal error.

Action: Contact Oracle Support Services.
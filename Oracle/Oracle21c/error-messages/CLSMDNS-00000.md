---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/CLSMDNS-00000.html
tags:
  - oracle
  - 21c
  - error-messages
---

CLSMDNS-00000: no error

Cause: A command completely successfully.

Action: No action is needed.

CLSMDNS-00001: GIPC endpoint creation failed.

Cause: An attempt to create a GIPC endpoint for use multicast operations failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00002: bind failed.

Cause: An attempt to bind an address to a GIPC endpoint failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00003: address creation failed.

Cause: An attempt to create a GIPC address failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00004: attribute setting failed.

Cause: An attempt to set an attribute on a GIPC endpoint or address failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00005: interface registration failed.

Cause: The registration of an interface with mDNS failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00006: failed to get name server list.

Cause: An attempt to get the list of available name servers failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00007: mDNS initialization failed.

Cause: The initialization of the mDNS subsystem failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00008: start of host query failed.

Cause: The query for hosts from mDNS failed to start.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00009: stop of host query failed.

Cause: Termination of the query for hosts from mDNS failed.

Action: Examine the accompanying error (if any) and the log file for details as to why the operation failed.

CLSMDNS-00010: Initialization of name server name retrieval failed.

Cause: The initialization of the retrieval of the names of the name servers used by multicast DNS failed.

Action: Examine the accompanying messages(s) that detail the platform error(s) for details about the exception.

CLSMDNS-00011: retrieval of name server name failed.

Cause: The retrieval of the name of a name server to be used by multicast DNS failed.

Action: Examine the accompanying messages(s) that detail the platform error(s) for details about the exception.

CLSMDNS-00012: no name servers found.

Cause: No name servers were found that could be used by multicast DNS.

Action: Check the system configuration and ensure that or more DNS name servers are configured, operating and accessible.

CLSMDNS-00013: Send of response to DNS server failed.

Cause: An attempt to send a response to a query from the DNS server failed.

Action: Examine accompanying exceptions for details about the exact error.

CLSMDNS-00015: invalid record type: number

Cause: The DNS server sent a record whose type is unknown.

Action: This is a warning message which can be ignored because the error should occur very infrequently. If the error occurs frequently, Oracle Customer Support should be contacted.

CLSMDNS-02000: unknown error.

Cause: An unknown error occurred. This error can occur when the multicast DNS server is not running.

Action: If the multicast server is not running, start it and try the operation again. If it is running, this is an internal error and Oracle Customer Support should be contacted with details about how and when the error occurred.

CLSMDNS-02001: no such name exists.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02002: memory allocation failure.

Cause: The allocation of process memory failed.

Action: If memory is low on the system, terminate other processes and/or threads and try the operation again. Otherwise, this is an internal error and Oracle Customer Support should be contacted.

CLSMDNS-02003: invalid parameter.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02004: invalid reference.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02005: invalid state.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02006: invalid flags.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02007: operation is unsupported.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02008: uninitialized.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02009: no cache.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02010: record or service is already registered.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02011: name conflict found.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02012: Invalid.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02013: Firewall.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02014: Incompatible.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02015: invalid interface.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02016: Refused.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02017: no such record.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02018: no authentication.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02019: no such key.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02020: error occurred while passing through NAT.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02021: double NAT encountered.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02022: invalid time.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02023: invalid signature.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02024: invalid key.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02025: transient error.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02250: connection pending.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02251: connection failed.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02252: connection established.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02253: more memory needed for cache.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02254: configuration changed.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.

CLSMDNS-02255: memory free needed.

Cause: This error is internal and should not ordinarily be seen by the user.

Action: Contact Oracle Customer Support.
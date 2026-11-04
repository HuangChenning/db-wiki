---
title: OS_AUTHENT_PREFIX
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams176.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OS_AUTHENT_PREFIX =` `authentication_prefix` |
| Default value | `OPS$` |
| Modifiable | No |

`OS_AUTHENT_PREFIX` specifies a prefix that Oracle uses to authenticate users attempting to connect to the server. Oracle concatenates the value of this parameter to the beginning of the user's operating system account name. When a connection request is attempted, Oracle compares the prefixed username with Oracle usernames in the database.

The default value of this parameter is `OPS$` for backward compatibility with previous versions. However, you might prefer to set the prefix value to "" (a null string), thereby eliminating the addition of any prefix to operating system account names.

Note:

The text of the `OS_AUTHENT_PREFIX` parameter is case sensitive on some operating systems.

See Also:

- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoauth.htm#ASOAG9770) for more information on setting this parameter
- Your operating system-specific Oracle documentation for the default value
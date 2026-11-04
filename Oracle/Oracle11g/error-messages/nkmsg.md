---
title: NDFN-00020 to NDFN-00025
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/nkmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 54 NDFN-00020 to NDFN-00025

NDFN-00020: missing IPMI userid

Cause: Required user name argument was not specified.

Action: Reissue command with correct arguments.

NDFN-00021: missing node list

Cause: Required node list was not supplied.

Action: Re-issue command with correct arguments.

NDFN-00022: unrecognized command option: 'string'

Cause: Operation type missing or mis-spelled.

Action: Re-issue command with correct arguments.

NDFN-00023: no password read. Re-issue request

Cause: Required administrator password was not read in response to the password prompt before finding end-of-line.

Action: Re-issue command and be sure to type the password immediately following the prompt.

NDFN-00024: caught I/O exception: string

Cause:.

Action: Re-issue command after repairing root cause.

NDFN-00025: string failed for node string

Cause: The indicated operation could not be completed for the specified node. The lower-level error messages attached should indicate the root cause.

Action: Re-issue command after repairing the condition indicated.
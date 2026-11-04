---
title: GIPC-00000 to GIPC-00020
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/gipcus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 66 GIPC-00000 to GIPC-00020

GIPC-00000: general success.

Cause: The operation succeeded.

Action: No action is required.

GIPC-00001: general failure.

Cause: A GIPC operation failed.

Action: Examine the trace and log files for the specific cause.

GIPC-00002: GIPC needs to be initialized.

Cause: The application failed to initialize GIPC prior to performing an operation.

Action: Initialize GIPC.

GIPC-00014: buffer not large enough to hold data.

Cause: The buffer provided by the application was not big enough to hold the data received.

Action: Use a larger buffer.

GIPC-00016: timeout waiting on request.

Cause: A wait call returned because the time expired.

Action: This error happens normally in most cases. If this error was not expected, examine the trace and log files for the reason.

GIPC-00017: waiting call has been posted.

Cause: A wait was interrupted by another thread posting it.

Action: This error happens normally in most cases. If this error was not expected, examine the trace and log files for the reason.

GIPC-00020: bind address already in use.

Cause: The application attempt to bind an endpoint to an address which has already been bound.

Action: Specify another address.
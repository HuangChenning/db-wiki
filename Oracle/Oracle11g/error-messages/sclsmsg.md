---
title: SCLS-01000 to SCLS-01005
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/sclsmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 90 SCLS-01000 to SCLS-01005

SCLS-01000: Failed to create super cluster representative server for tier {0}, {1}

Cause: Failed to create super cluster representative server for the given tier.

Action: Retry after resolving cause stated in message.

SCLS-01001: Failed to get ONS runtime of {0}

Cause: Failed to get ONS runtime of the given server.

Action: Retry after resolving cause stated in message.

SCLS-01002: Failed to get current member list of tier {0}

Cause: Failed to get current member list of the given tier.

Action: Retry after resolving cause stated in message.

SCLS-01003: eONS runtime was not running for tier {0}

Cause: eONS runtime was stopped abnormally.

Action: In cluster environment, try srvctl stop nodeapps -n \<node> and srvctl start nodeapps -n \<node>. In Oracle Restart environment, try srvctl stop eons and srvctl start eons.

SCLS-01004: Failed to set listening port to {0} for {1}

Cause: Failed to update listening port of the eONS runtime for this tier.

Action: Make sure that user has permission to update resource attribute. In cluster environment make sure that the clusterware stack is up.

SCLS-01005: Invalid listening port {0} specified for eONS

Cause: The specified eONS listening port number is invalid.

Action: Valid port numbers on Unix are from 1025 to 65535. Provide a valid port number for eONS to listen on.
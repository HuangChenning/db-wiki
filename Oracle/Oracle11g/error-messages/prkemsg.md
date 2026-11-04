---
title: PRKE-01008 to PRKE-01011
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prkemsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 72 PRKE-01008 to PRKE-01011

PRKE-01008: Failed to get list of active nodes from Clusterware

Cause: Possible causes: 1) Not operating in cluster mode. 2) Failed to load SRVM libraries. 3) Failed to initialize clusterware context.

Action: Check for the health of clusterware using "lsnodes" utility to get the list of active nodes in the cluster. Also, check for the presence of srvm libraries in the load library path. If these two checks get cleared, please contact Oracle Support Services.

PRKE-01009: Failed to start GSD on local node

Cause: GSD is already running on the local node, or GSD could not be started because of some other reason.

Action: Run "gsdctl stat" to check if a daemon is already running on the local node. If a daemon is not running on local node, please contact Oracle Support Services to check for the other reasons for failure.

PRKE-01010: Failed to stop GSD on local node

Cause: GSD is not running on the local node, or GSD could not shut down gracefully.

Action: Run "gsdctl stat" to check if a GSD is running on the local node. If a GSD is running, please contact Oracle Support Services to check for other reasons for failure.

PRKE-01011: Failed to get status of GSD on local node

Cause: Failure to get the list of active nodes from the cluster, or failure to query the list of live daemons from the clusterware.

Action: Run "lsnodes" to check the health of the clusterware. If the clusterware is working fine, check for the presence of SRVM libraries in the load library path. If the libraries are present, please contact Oracle Support Services for further assistance.
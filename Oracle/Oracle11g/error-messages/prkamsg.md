---
title: PRKA-02001 to PRKA-02005
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prkamsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 70 PRKA-02001 to PRKA-02005

PRKA-02001: GSD already exists

Cause: An attempt was made to create the Global Services Daemon (GSD) application while there was a running GSD application.

Action: Stop and remove the GSD and create the GSD application again using 'srvctl add nodeapps'.

PRKA-02002: Listener already exists

Cause: An attempt was made to create a Listener application while there was a running Listener application.

Action: Stop and remove the running Listener and create the Listener application again using 'srvctl add nodeapps'.

PRKA-02003: EM Agent already exists

Cause: An attempt was made to create an Agent application while there was a running Agent application.

Action: Stop the running Agent and create the Agent application again using 'srvctl add nodeapps'.

PRKA-02005: Netmasks are different for starting and ending IP addresses

Cause: An invalid range of VIP addresses was specified for the cluster

Action: Check if the starting and ending addresses in the VIP range belong to the same netmask.
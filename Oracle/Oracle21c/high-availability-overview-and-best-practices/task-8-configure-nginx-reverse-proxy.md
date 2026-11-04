---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-8-configure-nginx-reverse-proxy.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 8: Configure NGINX Reverse Proxy

Follow the instructions provided in [My Oracle Support note 2826001.1](https://support.oracle.com/rs?type=doc&id=2826001.1) to install and configure NGINX Reverse Proxy with SSL connection, and to ensure all external communication is completely secure.

Note:

When using CA Signed Certificates with NGINX, make sure the NGINX `ssl_certificate` parameter points to a certificate file that contains the certificates in the correct order of CA signed certificate, intermediate certificate and root certificate.

Oracle Clusterware needs to have control over starting the NGINX reverse proxy so that it can be started automatically before the GoldenGate deployments are started.

The NGINX resource is created with a dependency on the underlying network CRS resource, the name of which can be determined using the following command:

```
$ $GRID_HOME/bin/crsctl stat res -w "TYPE == ora.network.type"|grep NAME

NAME=ora.net1.network
```

As the `root` user, use the following example command to create a Clusterware resource to manage NGINX.

```
# $GRID_HOME/bin/crsctl add resource nginx -type generic_application -attr
 "ACL='owner:root:rwx,pgrp:root:rwx,other::r--,group:oinstall:r-x,user:oracle:rwx',
EXECUTABLE_NAMES=nginx,START_PROGRAM='/bin/systemctl
 start -f nginx',STOP_PROGRAM='/bin/systemctl
 stop -f nginx',CHECK_PROGRAMS='/bin/systemctl
 status nginx' ,START_DEPENDENCIES='hard(ora.net1.network)
 pullup(ora.net1.network)', STOP_DEPENDENCIES='hard(intermediate:ora.net1.network)',
 RESTART_ATTEMPTS=0, HOSTING_MEMBERS='dc1north01,dc1north02', CARDINALITY=2"
```

The NGINX resource created in this example run on the named cluster nodes at the same time, specified by `HOSTING_MEMBERS`. This is recommended when multiple GoldenGate Service Manager deployments are configured, and they can independently move between cluster nodes.

Once the NGINX Clusterware resource is created, alter the GoldenGate XAG resources so that NGINX must be started before the GoldenGate deployments are started.

As the `oracle` user, modify the XAG resources using the following example commands.

Determine the current `--filesystems` parameter:

```
$ agctl config goldengate SOURCE|grep "File System"

File System resources needed: ora.datac1.acfs_gg.acfs
```

Modify the `--filesystems` parameter:

```
$ agctl modify goldengate SOURCE --filesystems ora.datac1.acfs_gg.acfs,nginx
```

Repeat the above commands for each of the XAG GoldenGate registrations relying on NGINX.
---
title: "MySQL :: MySQL 26.7 Reference Manual :: 20.2.1 Deploying Group Replication in Single-Primary Mode"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/group-replication-deploying-in-single-primary-mode.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 20.2.1 Deploying Group Replication in Single-Primary Mode

Each of the MySQL server instances in a group can run on an independent physical host machine, which is the recommended way to deploy Group Replication. This section explains how to create a replication group with three MySQL Server instances, each running on a different host machine. See [Section 20.2.2, “Deploying Group Replication Locally”](group-replication-deploying-locally.md) for information about deploying multiple MySQL server instances running Group Replication on the same host machine, for example for testing purposes.

**Figure 20.7 Group Architecture**

![Three server instances, S1, S2, and S3, are deployed as an interconnected group, and clients communicate with each of the server instances.](img/gr-3-server-group.png)  

This tutorial explains how to get and deploy MySQL Server with the Group Replication plugin, how to configure each server instance before creating a group, and how to use Performance Schema monitoring to verify that everything is working correctly.
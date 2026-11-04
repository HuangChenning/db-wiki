---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/software-maintenance-tools-and-capabilities.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Software Maintenance Tools and Capabilities

Oracle continues to evolve software update tools and capabilities based on customer requirements. The primary tools used to evaluate, obtain, and apply Oracle software updates are summarized here.

Software Maintenance Capabilities

Definitions

Rolling orchestration to maximize database uptime— Coordinating software maintenance, typically offline patching, across one node or server at a time. For Database, Grid, and Exadata database servers rolling orchestration includes connection draining before each node is taken offline, so clustered database services remain available for the duration of the orchestration. For Exadata storage servers rolling orchestration includes handling storage offline and online actions while database availability remains unaffected.

Non-rolling orchestration to minimize maintenance time- Coordinating software maintenance, typically offline patching, across all nodes or servers at the same time to minimize maintenance time, requiring clustered database and/or storage service downtime for the duration of the orchestration.

Data Guard orchestration — Coordinating maintenance across primary and standby databases in a Data Guard configuration, often using standby-first patching.

Fleet orchestration — Managing and sequencing software maintenance actions across many Oracle databases, homes, clusters, or servers as a controlled fleet-level operation.

Database online hot patching — Applying online-eligible patches to an Oracle database instance while it remains running. See MOS KB140524.

Grid Zero-Downtime patching - Applying Grid home patches without bringing down Oracle RAC database instances.

Exadata Live Update - An Exadata update method that applies supported database server software updates online, using technologies such as RPM and Ksplice, to reduce or avoid database instance interruption and server reboots.

Upgrade — Moving from one major release to a newer major release.

Oracle Update Advisor integration — Integration with Oracle Update Advisor capabilities to provide software health, recommendation, and gold image based on Oracle's official recommendation.

Vertical stack update — Coordinated updating of multiple dependent layers in the Oracle technology stack, such as Grid Infrastructure software, Database software, and Exadata System Software, one node at a time across a cluster to minimize application disruption.

Database Home Software

| Product | Database patching | Database online hot patching | Database rolling orchestration | Database non-rolling orchestration | Data Guard orchestration | Fleet orchestration | Database upgrade | Oracle Update Advisor integration | Vertical stack update |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OPatch/OPatchAuto (in place) | Yes | Yes | No | No | No | No | No | No | No |
| Database Configuration Assistant (DBCA/DBCACTL) | Yes | No | Yes | Yes | No | No | No | Yes | No |
| Fleet Patching and Provisioning (FPP) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| AutoUpgrade | Yes | No | Yes | Yes | No | No | Yes | Yes | No |
| Enterprise Manager (EM) with Database Lifecycle Management (DBLM) | Yes | No | Yes | Yes | Yes | Yes | Yes | No | No |
| Cloud Console Automation | Yes | No | Yes | No | No | No | Yes | No | No |
| Cloud Exadata Fleet Update | Yes | No | Yes | Yes | No | Yes | Yes | No | No |

Grid Infrastructure Home Software

| Product | Grid patching | Grid Zero-Downtime patching | Grid rolling orchestration | Grid non-rolling orchestration | Fleet orchestration | Grid upgrade | Oracle Update Advisor Integration | Vertical Stack Update |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OPatch/OPatchAuto (in place) | Yes | No | No | No | No | No | No | No |
| gridSetup.sh | Yes | Yes | Yes | No | No | Yes | No | No |
| Fleet Patching and Provisioning (FPP) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Enterprise Manager (EM) with Database Lifecycle Management (DBLM) | Yes | Yes | Yes | Yes | Yes | Yes | No | No |
| Cloud Console Automation | Yes | No | Yes | No | No | Yes | No | No |
| Cloud Exadata Fleet Update | Yes | No | Yes | No | Yes | Yes | No | Yes |
|  |  |  |  |  |  |  |  |  |

Exadata Software

| Product | Exadata patching | Exadata Live Update | Exadata rolling orchestration | Exadata non-rolling orchestration | Fleet orchestration | Vertical Stack Update |
| --- | --- | --- | --- | --- | --- | --- |
| Patchmgr | Yes | Yes | Yes | Yes | No | No |
| Fleet Patching and Provisioning (FPP) | Yes | Yes | Yes | Yes | Yes | Yes |
| Enterprise Manager (EM) with Exadata Management pack | Yes | No | Yes | Yes | Yes | No |
| Cloud Console Automation | Yes | No | Yes | No | No | No |
| Cloud Exadata Fleet Update | Yes | No | No | Yes | Yes | Yes |

Software Maintenance Tool Recommendations

| Oracle Software Update Solution | Primary Use | Documentation/ References | Licensing |
| --- | --- | --- | --- |
| Fleet Patching and Provisioning (FPP) | Fleet-scale out-of-place, gold image-based provisioning, patching, and upgrade orchestration. | [Fleet Patching and Provisioning Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/26/fppad/fleet-patching-provisioning.html)  - [Fleet Patching and Provisioning (FPP](https://docs.oracle.com/en/database/oracle/oracle-database/26/fppad/fleet-patching-provisioning.html?utm_source=chatgpt.com)) - [Fleet Patching and Provisioning (FPP) – Local Mode](https://docs.oracle.com/en/database/oracle/oracle-database/26/fppad/oracle-fpp-local-mode.html) | Included with supported Oracle Database/Oracle RAC environments |
| Enterprise Manager with Database Lifecycle Management | Fleet-wide lifecycle orchestration across hybrid and multicloud environments with audit reporting | [Enterprise Manager Lifecycle Management Guide](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/24.1/emlcm/database-maintenance-updates-patching-upgrades.html)  - [Database Lifecycle Management](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/24.1/lifecycle.html) - [Exadata Management](http://enterprise-manager/cloud-control/enterprise-manager-cloud-control/24.1/engineered.html) - [Real Application Testing](https://docs.oracle.com/en/database/oracle/oracle-database/26/ratug/index.html?source=%3Aow%3Alp%3Acpo%3A%3Arc_bumk180724p00001%3Alpd100743723&source=%3Aow%3Alp%3Acpo%3A%3Arc_bumk180724p00001%3Alpd100743723) | Requires Database Lifecycle Management (DBLM) Pack |
| AutoUpgrade | Database upgrade and single-instance database patching | - [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/26/upgrd/autoupgrade-patching.html) [AutoUpgrade](https://docs.oracle.com/en/database/oracle/oracle-database/26/upgrd/autoupgrade-patching.html) [Patching](https://docs.oracle.com/en/database/oracle/oracle-database/26/upgrd/autoupgrade-patching.html) | Included with Oracle Database |
| Database Configuration Assistant (DBCA/DBCACTL) | Single-instance database patching | [Using Oracle Update Advisor with DBCA](https://docs.oracle.com/en/database/oracle/oracle-database/26/dbptc/index.html#GUID-8FF368BB-736A-49F1-AC8E-8ADA9A30FDB0) | Included with Oracle Database |
| OPatch | Database online hot patching | - OPatch - [RDBMS Online Patching (“Hot Patching”) – KB140524](https://fa-etmi-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/redwood/myknowledge/content/container/main/article?stripeCode=ORA_SVC_CRM&answerId=761111) | Included with Oracle Database |
| Patchmgr | Exadata System Software maintenance | [Exadata Database Machine Maintenance Guide](https://docs.oracle.com/en/engineered-systems/exadata-database-machine/dbmmn/index.html) | Included with Oracle Exadata Systems |
| Cloud Console Automation | Database, Grid Infrastructure, and Exadata software maintenance for Oracle Cloud Database services. | Refer to the applicable Oracle Cloud Database Service documentation | Included with Oracle Cloud Services |
| Cloud Exadata Fleet Update | Fleet-scale Database, Grid Infrastructure, and Exadata software maintenance for Oracle Cloud Database services. | Refer to the applicable Oracle Cloud Database Service documentation | Included with Oracle Cloud Services |
---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/software-security-recommendations.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Software Security Recommendations

Software Security Recommendations

Oracle environments can be high-value targets because they often support mission-critical business processes and may include broad database, middleware, application, and infrastructure footprints. In addition to maintaining strong security practices, such as network isolation, least-privilege access controls, secure configuration, and regular validation, timely software maintenance is a core security control and an MAA best practice.

Patch management is critical because many incidents exploit vulnerabilities for which fixes are already available. To help protect Oracle Database environments, Oracle recommends that you:

- Oracle Database and Grid Infrastructure Software
	- Upgrade to a Long Term Support Database release, such as Oracle Database 19c or Oracle AI Database 26ai.
		- Apply the latest quarterly Database Release Updates (RUs) for Oracle Database, Oracle Grid Infrastructure, and related software components. RUs contain the latest critical fixes, security fixes, and reliability improvements.
		- Apply the latest monthly Database Critical Security Patch Update (CSPU) when available and applicable to your platform and release. Monthly Critical Security Patch Updates (CSPUs) begin May 2026 and provide targeted fixes for critical vulnerabilities in a smaller, focused format, enabling customers to address high-priority issues without waiting for the next quarterly release update. Database and Grid Infrastructure on Linux x86-64 receive CSPU content in the existing Monthly Recommended Patch (MRP) update.
		- Update client libraries and drivers to supported Long Term Support release versions, such as 19c or 26ai.
- Exadata System Software
	- Update to an Exadata Release still receiving monthly maintenance releases.
		- Apply the latest monthly Exadata System Software maintenance release when available.

For more information see My Oracle Support article [PNEWS3015 Recommendations to Help Protect Oracle Databases from Emerging AI-enabled Security Threats](https://support.oracle.com/support/?documentId=PNEWS3015).

For the latest software recommendations, use Oracle Update Advisor (OUA) or reference the Oracle Support knowledge articles applicable to your environment.

OUA evaluates and reports Oracle Database and Grid Infrastructure software health, and provides recommendations aligned with Oracle update policies and software images matching the recommendation. Many Oracle software maintenance tools integrate with OUA to deliver software health and recommendation. See Software Maintenance Tools and Capabilities section below. In addition, OUA can be integrated into existing custom software maintenance orchestration. See Oracle Update Advisor (OUA) API Reference and Integration Guide [KB886700](https://support.oracle.com/support/?documentId=KB886700).

The following table summarizes Oracle's general recommendation:

| Software Component | General Recommendation | Documentation References |
| --- | --- | --- |
| Oracle Database software  Oracle Grid Infrastructure software | - Use release 19c or 26ai - Apply the latest RU - Apply the latest MRP or CSPU - Use OUA to evaluate software health and provide recommendations | Primary Note for Database Quarterly Release Updates [KB106822](https://support.oracle.com/support/?documentId=KB106822)  Exadata Database Machine and Exadata Storage Server Supported Versions [KB153930](https://support.oracle.com/support/?documentId=KB153930)  Exadata Database Service Software Versions [KB114881](https://support.oracle.com/support/?documentId=KB114881) |
| Exadata System Software | - Use an Exadata release receiving monthly updates - Apply the latest monthly Exadata maintenance release | Exadata Database Machine and Exadata Storage Server Supported Versions [KB153930](https://support.oracle.com/support/?documentId=KB153930)  Exadata Database Service Software Versions [KB114881](https://support.oracle.com/support/?documentId=KB114881) |

Staying current with upgrades and patches reduces risk and helps maintain a secure, supportable environment over time. Oracle provides different levels of automation and assistance depending on the deployment model:

- Oracle-managed services: Oracle Autonomous Database services are automatically updated to current software levels by Oracle.
- Co-managed cloud services: Exadata Database Service and Oracle Database services in supported multicloud environments provide automation to help customers apply updates across their database fleets.
- Customer-managed environments: For on-premises and highly integrated environments, Oracle provides resources through [Oracle Platinum Services](https://www.oracle.com/assets/oracle-platinum-services-ds-1653256.pdf) for engineered systems, [My Oracle Support](http://support.oracle.com/), and [Oracle Customer Success Services](https://www.oracle.com/customer-success/) to assist with planning, testing, and execution.
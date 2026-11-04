---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/security-considerations-gghub-onprem-gghub.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Security Considerations for GGHub

For detailed guidance on implementing security features and best practices in Oracle GoldenGate Microservices Architecture, see [Oracle GoldenGate Security Feature: Implementation](https://docs.oracle.com/en/database/goldengate/core/26/coredoc/security-feature-implementation.html).

When configuring GGHub using the Ansible automation steps in the topics that follow, the security guidelines described at the link above are implemented as follows:

- Security guideline 1 is met by providing the latest Oracle GoldenGate software version in Step 2.3 - "Download the required Oracle GoldenGate Software to the Ansible Orchestration Host" for Ansible automation to install.
- Security guideline 2 is met when Ansible automation configures NGINX reverse proxy with SSL to ensure all external communication is secure. The Ansible automation initially uses a self signed certificate for NGINX configuration. The certificate and key file can be replaced as per your security standards following the process in Step 3.5 - "Replace NGINX SSL Certificate".
- Security guideline 3 is met by providing a strong password for Ansible automation in Step 3.1 - "Create GGHub Ansible Inventory File".
- The remaining security guidelines can be implemented after Ansible automation during GoldenGate configuration.
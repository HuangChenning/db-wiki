---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-10-create-new-profile.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 10 - Create a New Profile

Create a new profile to automatically start the Extract and Replicat processes when the Oracle GoldenGate Administration Server is started.

Then, restart if any Extract or Replicat processes are abandoned. With GoldenGate Microservices, auto start and restart is managed by Profiles.

Using the Oracle GoldenGate Administration Server GUI, create a new profile that can be assigned to each of the Oracle GoldenGate processes:

1. Log in to the Administration Service on the Source and Target GoldenGate.
2. Click on Profile under Administration Service.
3. Click the plus (+) sign next to Profiles on the Managed Process Settings home page. The Add Profile page is displayed.
4. Enter the details.
5. Click Submit.
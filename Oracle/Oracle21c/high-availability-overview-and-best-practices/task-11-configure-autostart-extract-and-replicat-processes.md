---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-11-configure-autostart-extract-and-replicat-processes.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 11: Configure Autostart of Extract and Replicat Processes

Configure the Extract and Replicat processes to automatically start when the Oracle GoldenGate Administration Server is started, and then to restart if any Extract or Replicat processes abend. With GoldenGate Microservices auto start and restart is managed by Profiles.

Using the Oracle GoldenGate Administration Server GUI, create a new profile which can be assigned to each of the Oracle GoldenGate processes.

| Profile Configuration Option | Recommended Setting |
| --- | --- |
| Default Profile | Enabled |
| Auto Start | Enabled |
| Startup Delay | 1 minute |
| Auto Restart | Enabled |
| Max Retries | 5 |
| Retry Delay | 30 seconds |
| Retries Window | 30 minutes |
| Restart on Failure only | Enabled |
| Disable Task After Retries Exhausted | Enabled |

After the profile has been created, and set as the default profile, all new GoldenGate processes created are assigned this profile. For all existing processes, the profile must be assigned to each process.

In the Overview pane, on the Process Information tab, select the Profile Name under Managed Options.

Note:

When using Oracle GoldenGate Microservices with XAG, it is strongly recommended not to enable the ‘Critical to deployment health’ flag for any Extract or Replicat processes. Doing so can cause an entire GoldenGate deployment outage from a single Extract or Replicat failure, and also prevents XAG from being able to restart GoldenGate. Refer to [Troubleshooting Oracle GoldenGate on Oracle RAC](troubleshooting-oracle-goldengate-oracle-rac.md) for an example of troubleshooting an outage caused by setting a Replicat to critical.
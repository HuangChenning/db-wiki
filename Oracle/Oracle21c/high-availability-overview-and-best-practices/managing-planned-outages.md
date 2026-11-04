---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/managing-planned-outages.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Managing Planned Outages

When there is a requirement to perform planned maintenance on the GGHub, some of the CRS resources should be stopped and disabled to prevent them from restarting, or from causing undesirable results when incorrectly instigating a file system failover, or stopping GoldenGate from running.

Use the following recommendations in the event of a planned outage of the primary or standby hub clusters.

For all planned maintenance events:

- Operating system software or hardware updates and patches
- Oracle Grid Infrastructure interim or diagnostic patches
- Oracle Grid Infrastructure quarterly updates under the Critical Patch Update (CPU) program, or Oracle Grid Infrastructure release upgrades
- GGHub software life cycle, including:
	- Oracle GoldenGate
		- Oracle Grid Infrastructure Agent
		- NGINX

High Availability Solutions with Target Outage Time:

Seconds to minutes where GoldenGate replication is temporarily suspended

Step 1: Software update of idle GGHub node

Step 2: GGHub Node Relocate

Step 3: Software update of the remaining inactive GGHub node

GGHub Node Relocate

As the `grid` OS user on the primary GGHub system, relocate the Oracle GoldenGate Instance:

```
[grid@gghub_prim1 ~]$ agctl status goldengate

Goldengate instance 'gghub' is running on gghub_prim1

[grid@gghub_prim1 ~]$ time agctl relocate goldengate gghub

real    0m43.984s
user    0m0.156s
sys     0m0.049s
```

As the `grid` OS user on the primary GGHub system, check the status of the Oracle GoldenGate Instance:

```
[grid@gghub_prim1 ~]$ agctl status goldengate

Goldengate instance 'gghub' is running on gghub_prim2
```

GGHub Role Reversal for DR events or to move GGHub in the same region as the target database

GGHub role reversal performs an ACFS role reversal so that the standby becomes the new primary. With both the primary and standby file systems online, the `acfsutil repl failover` command ensures that all outstanding primary file system changes are transferred and applied to the standby before the role reversal completes.

When to use GGHub role reversal:

- To move the GGHub deployment close to the target database for replication performance
- To support site outage
- To support site maintenance

As the `grid` OS user on the current standby GGHub node, create the script to perform the ACFS role reversal:

```
[grid@gghub_stby1]$ export ACFS_MOUNT_POINT=/mnt/acfs_gg1
[grid@gghub_stby1]$ export GG_DEPLOYMENT_NAME=gghub
[grid@gghub_stby1]$ ssh \`/sbin/acfsutil repl info -c -v $ACFS_MOUNT_POINT| grep
 'Primary hostname' | awk '{print $3}'| cut -d "@" -f2\`
 "agctl stop goldengate $GG_DEPLOYMENT_NAME"
[grid@gghub_stby1]$ /sbin/acfsutil repl failover $ACFS_MOUNT_POINT
[grid@gghub_stby1]$ agctl start goldengate $GG_DEPLOYMENT_NAME
[grid@gghub_stby1]$ agctl status goldengate $GG_DEPLOYMENT_NAME
Goldengate  instance 'gghub' is running on gghub_stby1
```

Alternatively, as the `grid` OS user on any GGHub node, run the script `acfs_role_reversal.sh` to perform the ACFS role reversal:

```
[grid@gghub_stby1]$ sh /u01/oracle/scripts/acfs_role_reversal.sh
 /mnt/acfs_gg1 gghub

################################################################################
ACFS Primary Site: gghub_prim_vip1.frankfurt.goldengate.com
ACFS Standby Site: gghub_stby_vip1.frankfurt.goldengate.com
################################################################################
Thu Nov 30 17:28:37 UTC 2023 - Begin Stop  GoldenGate gghub
Thu Nov 30 17:28:38 UTC 2023 - End   Stop  GoldenGate gghub
################################################################################
Thu Nov 30 17:28:38 UTC 2023 - Begin ACFS replication sync /mnt/acfs_gg1
Thu Nov 30 17:28:59 UTC 2023 - End   ACFS replication sync /mnt/acfs_gg1
################################################################################
Site:                                Primary
Primary status:                      Running
Status:                              Send Completed
Lag Time:                            00:00:00
Retries made:                        0
Last send started at:                Thu Nov 30 17:28:45 2023
Last send completed at:              Thu Nov 30 17:28:55 2023
################################################################################
Site:                                Standby
Last sync time with primary:         Thu Nov 30 17:28:45 2023
Status:                              Receive Completed
Last receive started at:             Thu Nov 30 17:28:46 2023
Last receive completed at:           Thu Nov 30 17:28:52 2023
################################################################################
Thu Nov 30 17:29:00 UTC 2023 - Begin Role Reversal
Thu Nov 30 17:30:02 UTC 2023 - End Role Reversal
################################################################################
ACFS Primary Site: gghub_stby_vip1.frankfurt.goldengate.com
ACFS Standby Site: gghub_prim_vip1.frankfurt.goldengate.com
################################################################################
Site:                                Primary
Primary status:                      Running
Status:                              Send Completed
Lag Time:                            00:00:00
Retries made:                        0
Last send started at:                Thu Nov 30 17:29:45 2023
Last send completed at:              Thu Nov 30 17:29:56 2023
################################################################################
Site:                                Standby
Last sync time with primary:         Thu Nov 30 17:29:45 2023
Status:                              Receive Completed
Last receive started at:             Thu Nov 30 17:29:50 2023
Last receive completed at:           Thu Nov 30 17:29:50 2023
################################################################################
Thu Nov 30 17:30:03 UTC 2023 - Begin Start GoldenGate gghub
Thu Nov 30 17:30:10 UTC 2023 - End   Start GoldenGate gghub
################################################################################
```
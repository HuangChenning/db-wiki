---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/managing-unplanned-outages.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Managing Unplanned Outages

Expected Impact with Unplanned Outages

When an unplanned outage occurs on either the primary or standby GGHub clusters, there are some instructions to ensure the continuous operation of GoldenGate. Use the following GGHUB failure use cases to guide you in the event of an unplanned outage of the primary and standby GGHUB systems.

Use case #1 – Standby Hub Failure or Primary GGHub Cannot Communicate with the Standby GGHub

If the primary GGhub cannot communicate with the standby GGhub, the following messages will be output into the primary CRS trace file (crsd\_scriptagent\_grid.trc) on the active cluster node:

```
2023-06-21 12:06:59.506 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] Executing action script: /u01/oracle/scripts/acfs_primary.scr[check]
2023-06-21 12:07:05.666 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] WARNING: STANDBY not accessible (attempt 1 of 3))
2023-06-21 12:07:18.683 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] WARNING: STANDBY not accessible (attempt 2 of 3))
2023-06-21 12:07:31.751 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] WARNING: STANDBY not accessible (attempt 3 of 3))
2023-06-21 12:07:31.751 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] WARNING: Problem with STANDBY file system (error: 222)
```

At this time, the standby file system is no longer receiving the primary file system changes. The primary file system and Oracle GoldenGate will continue to function unimpeded.

Use the following action plan with this scenario.

- Check the standby file system, using the command ‘acfsutil repl util verifystandby /mnt/acfs\_gg –v’ to determine why the standby hub is inaccessible.
- After fixing the cause of the communication errors, the standby will automaitically catch up applying the outstanding primary file system changes. The warning messages will no longer be reported into the CRS trace file, being replaced with the following message:
```
2023-06-21 12:15:01.720 :CLSDYNAM:1427187456: [acfs_primary]{1:8532:12141} [check] SUCCESS: STANDBY file system /mnt/acfs_gg is ONLINE
```

Use case #2 – Primary GGHub Failure or Standby GGHub Cannot Communicate with the Primary GGHub

If the standby GGhub cannot communicate with the primary GGhub, the the following messages will be output into the standby CRS trace file (crsd\_scriptagent\_grid.trc) on the active cluster node:

```
2023-06-21 12:24:03.823 :CLSDYNAM:4156544768: [acfs_standby]{1:10141:2} [check] Executing action script: /u01/oracle/scripts/acfs_standby.scr[check]
2023-06-21 12:24:06.928 :CLSDYNAM:4156544768: [acfs_standby]{1:10141:2} [check] WARNING: PRIMARY not accessible (attempt 1 of 3)
2023-06-21 12:24:19.945 :CLSDYNAM:4156544768: [acfs_standby]{1:10141:2} [check] WARNING: PRIMARY not accessible (attempt 2 of 3)
2023-06-21 12:24:32.962 :CLSDYNAM:4156544768: [acfs_standby]{1:10141:2} [check] WARNING: PRIMARY not accessible (attempt 3 of 3)
2023-06-21 12:24:32.962 :CLSDYNAM:4156544768: [acfs_standby]{1:10141:2} [check] WARNING: Problem with PRIMARY file system (error: 222)
```

At this time, it is unlikely that the standby file system is receiving file system changes from the primary file system.

Use the following action plan with this scenario.

- Check the primary file system, using the command ‘acfsutil repl util verifyprimary /mnt/acfs\_gg -v’ to determine why the primary hub is inaccessible.
- If the primary file system cluster is down and cannot be restarted, issue an ACFS failover on the standby GGhub:
	```
	[grid@gghub_stby1]$ /sbin/acfsutil repl failover /mnt/acfs_gg        # Specify the correct mount point
	[grid@gghub_stby1]$ acfsutil repl info -c -v /mnt/acfs_gg |egrep 'Site:|Primary status|Background Resources:'
	Site:                                Primary
	Primary status:                      Running
	Background Resources:                Active
	```
- Run the following commands to prepare the acfs\_primary resource to start on the new primary hub, and then restart GoldenGate:
	```
	[grid@gghub_stby1]$ echo "RESTART" > /mnt/acfs_gg/status/acfs_primary
	[grid@gghub_stby1]$ agctl start goldengate <instance_name>              # Specify the GoldenGate instance name
	[grid@gghub_stby1]$ agctl status goldengate
	Goldengate  instance '<instance_name>' is running on gghubstby-node1
	```
- When the old primary file system comes back online, if connectivity is resumed between the new primary and old primary, the old primary file system will automatically convert to the standby.
- If the old primary file system comes back online, but connectivity cannot be established between the primary and standby file systems the acfs\_primary resource will detect that node had crashed, and because connectivity to the standby cannot be confirmed, GoldenGate will not be started. This avoids a ‘split-brain’ where two file systems think they are both the primary because they cannot commnunicate with each other.

Use case #3 – Double Failure Case: Primary GGHub Failure and Standby GGHub Connectivity Failure

If the primary GGhub crashes and communication cannot be established with the standby file system when it comes back online, the following messages will be output into the primary CRS trace file (crsd\_scriptagent\_grid.trc) on the active cluster node:

```
2023-06-21 17:08:52.621:[acfs_primary]{1:40360:36312} [start] WARNING: PRIMARY file system /mnt/acfs_gg previously crashed
2023-06-21 17:08:55.678:[acfs_primary]{1:40360:36312} [start] WARNING: STANDBY not accessible - disabling acfs_primary
```

If an attempt is made to manually restart the primary file system, an additional message will be output into the CRS trace file:

```
2023-06-21 17:25:54.224:[acfs_primary]{1:40360:37687} [start] WARNING:
    PRIMARY /mnt/acfs_gg disabled to prevent split brain
```

Use the following action plan with this scenario.

- Check the standby file system, using the command ‘acfsutil repl util verifystandby /mnt/acfs\_gg -v’ to determine why the standby hub is inaccessible.
- If communication with the the standby file system can re-established, restart GoldenGate on the primary hub:
	```
	[grid@gghub_prim1]$ agctl start goldengate <instance_name> # Specify the GoldenGate instance name
	[grid@gghub_prim1]$ agctl status goldengate
	Goldengate  instance '<instance_name>' is running on gghub_prim1
	```
- If communication with the standby file system cannot be re-established, use the following commands to restart GoldenGate on the primary hub:
	```
	[grid@gghub_prim1]$ echo "RESTART" > /mnt/acfs_gg/status/acfs_primary
	[grid@gghub_prim1]$ agctl start goldengate <instance_name>              # Specify the GoldenGate instance name
	[grid@gghub_prim1]$ agctl status goldengate
	Goldengate  instance '<instance_name>' is running on gghub_prim1
	```
- When communication with the standby file system is restored, ACFS Replication will continue to replicate primary file system changes.
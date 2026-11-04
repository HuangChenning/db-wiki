---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-9-create-oracle-net-tns-aliases-oracle-goldengate-database-connections.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 9: Create Oracle Net TNS Aliases for Oracle GoldenGate Database Connections

The same TNS aliases created on the primary cluster for the primary database using the IPC protocol must be created with the same alias names on each node of the standby cluster, using the IPC communication protocol as specified in [Task 9: Create Oracle Net TNS Alias for Oracle GoldenGate Database Connections](task-9-create-oracle-net-tns-alias-oracle-goldengate-database-connections.md).

The location of `tnsnames.ora` used by the Oracle GoldenGate deployment must be the same on the standby cluster nodes as it is on the primary cluster.

Use the following query REST API call to query the `TNS_ADMIN` location on the primary cluster.

```
$ curl -s -u OGG_admin_username
 https://vip_name/services/v2/deployments/deployment_name
 -XGET|python -m json.tool|grep TNS_ADMIN -A1
```

You will be prompted to enter the Oracle GoldenGate Service Manager administrator user password.

For example:

```
$ curl -s -u oggadmin https://dc1north01-vip1/services/v2/deployments/ggnorth
 -XGET|python -m json.tool|grep TNS_ADMIN -A1

                "name": "TNS_ADMIN",
                "value": "/u01/goldengate/network/admin"
```

Make sure the `tnsnames.ora` is located in this same directory on all standby cluster nodes.

Example TNS alias for the GoldenGate database:

```
ggnorth_pdb =
    (DESCRIPTION =
      (SDU = 2097152)
      (ADDRESS = (PROTOCOL = IPC)(KEY=LISTENER))
      (CONNECT_DATA =
        (SERVICE_NAME = oggserv_pdb.example.com)
       )
    )
```
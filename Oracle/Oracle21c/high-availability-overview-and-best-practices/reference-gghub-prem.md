---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/reference-gghub-prem.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Reference

### Alternate Method to Generate Ansible Inventory File for Deployment

The Ansible playbook `oracle.gghub.onboarding` can generate the Ansible inventory file for deployment using an alternate method.

The alternate method uses a response file instead of user prompts for all the required values. A template response file is provided in the GGHub collection directory which must be updated and used with the playbook `oracle.gghub.onboarding`.

Make a copy of the provided template response file from the collection directory and fill in all the parameter values.

Note:

A space is required before the parameter value in the response file following the YAML syntax. As per YAML specification, the key-value pairs are marked with a colon and space. For example, `gg_deployment_name: maahub`

```
(gghub) [~]$ cd /u01/maagghub
(gghub) [~]$ cp gghub-ansible-collection/gghub_deploy.yml
 gghub-ansible-collection/gghub_maahub.yml
(gghub) [~]$ vi gghub-ansible-collection/gghub_maahub.yml
```

Execute the playbook `oracle.gghub.onboarding` using the response file as follows to generate the Ansible inventory file.

```
(gghub) [~]$ ansible-playbook oracle.gghub.onboarding
 -i /u01/maagghub/collections/ansible_collections/oracle/gghub/inventory/localhost
 -e @/u01/maagghub/gghub-ansible-collection/gghub_maahub.yml
```

When the playbook `oracle.gghub.onboarding` is executed using a response file it will only prompt for the Ansible vault and GoldenGate admin user passwords.

### Alternate Deployment Option to Configure Only Primary or Standby GGHub

If there is a requirement to deploy only the primary GGHub or the standby GGHub initially, use the `limit` option and specify the primary or standby group name from the Ansible inventory file. The `limit` option restricts the execution of a playbook to a specific subset of hosts within the inventory.

In the following example, Ansible automation only deploys GGHub resources on the primary GGHub cluster using the `limit` option. ACFS file system will be created.

```
(gghub) [~]$ ansible-playbook oracle.gghub.deploy
 -i /u01/maagghub/inventory/maahub.yml --limit maahuba -e @/u01/maagghub/inventory/maahub.key
 --ask-vault-pass
```

Continuing with the example above where just the primary GGHub is deployed, to proceed with standby GGHub deployment and ACFS replication setup, run the deploy playbook without the `limit` option. Ansible skips the actions already performed for the primary GGHub and configures only the standby GGHub and AFCS replication.

```
(gghub) [~]$ ansible-playbook oracle.gghub.deploy
 -i /u01/maagghub/inventory/maahub.yml -e @/u01/maagghub/inventory/maahub.key
 --ask-vault-pass
```

### Validate GGHub Deployment

After the deployment is complete, playbook `oracle.gghub.verify` can be executed to display the GGHub configuration information and status of some of the GGHub clusterware resources.

```
(gghub) [~] $ ansible-playbook oracle.gghub.verify
 -i /u01/maagghub/inventory/maahub.yml --ask-vault-password
```

Example output:

```
TASK [Display GoldeGate status] ************************************************
ok: [maahuba1] => {
    "msg": [
        {
            "grid": {
                "activeVersion": "19.0.0.0.0",
                "cluster_nodes": "maahuba1,maahuba2",
                "homePath": "/u01/app/19.0.0.0/grid",
                "master_node": "maahuba1",
                "orabase": "/u01/app/grid",
                "patchVersion": "19.26.0.0.0",
                "scanListenerTCPPorts": "1521",
                "state": "NORMAL",
                "user": "grid"
            },
            "system": {
                "crs": true,
                "inst_group": "oinstall",
                "inventory_loc": "/u01/app/oraInventory",
                "oracle_ahf_loc": "/u01/app/oracle.ahf",
                "scan_name": "maahuba-scan.clientsubnet.vcnfraans1.oraclevcn.com"
            }
        },
        {
            "acfs": {
                "device": "/dev/asm/maahub-207",
                "diskgroup": "data",
                "primary_hostname": "maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com",
                "primary_path": "/opt/oracle/gghub/maahub",
                "retries_made": "0",
                "site": "primary",
                "standby_connect_string": "grid@maahubb-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com",
                "standby_path": "/opt/oracle/gghub/maahub",
                "status": "running",
                "volume": "maahub"
            },
            "appvip": {
                "name": "maahuba-app-vip1"
            },
            "crs_status": {
                "acfs_primary": true,
                "acfs_standby": true,
                "ora_acfs": true,
                "sshd_restart": true,
                "xag_goldengate": true
            },
            "goldengate": {
                "admin_user": "oggadmin",
                "file_system": "acfs_primary,nginx",
                "homePath": "/u01/app/oracle/goldengate/gg23ai",
                "name": "maahub",
                "service_manager_port": "9100",
                "xag_home": " /u01/app/grid/xag"
            }
        },
        "",
        ""
    ]
}
```

### GGHub Ansible Playbook oracle.gghub.maa\_ha Functions

Playbook `oracle.gghub.maa_ha` provides multiple functions to perform different tasks.

These additional functions are available in the form of tags in the playbook `oracle.gghub.maa_ha`. List the available tags in the playbook as shown below.

```
(gghub) [~] $ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --list-tags
```

The following section describes some of the functions in the playbook `oracle.gghub.maa_ha` which are invoked using the specific tag names.

Relocate GGHub Clusterware Resources

It is highly recommended that you validate the GGHub clusterware resources high availability and successful role reversal functionality before configuring the GoldenGate extract and replicat processes.

Playbook `oracle.gghub.maa_ha` provides the functionality to relocate GGHub clusterware resources from the active node of the GGHub cluster to the available node.

The relocate feature of the playbook `oracle.gghub.maa_ha` can also facilitate the rolling planned maintenance of GGHub cluster nodes.

Perform the following steps to relocate the GGHub clusterware resources from the active node to the available node in the cluster:

Step 1. Relocate Primary GGHub Clusterware Resources

Validate the status of the primary GGHub clusterware resources before relocating to the available node using the example command in the "Check the Primary and Standby GGHub Clusterware Resources Status" section of [Troubleshooting GGHub Deployment Using Ansible](troubleshooting-maa-gghub.md).

Execute the Ansible playbook `oracle.gghub.maa_ha` with tag `acfs_relocate_primary` to relocate the primary GGHub clusterware resources from the active node to the available node in the primary cluster.

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags acfs_relocate_primary
```

Check the status of the GGHub clusterware resources after the relocate task is complete. Notice that all the resources should be online on the available node.

Step 2. Relocate Standby GGHub Clusterware Resources

Validate the status of the standby GGHub clusterware resources before relocating to the available node using the example command in the "Standby GGHub Clusterware Resources Status" section of [Troubleshooting GGHub Deployment Using Ansible](troubleshooting-maa-gghub.md).

Execute the Ansible playbook `oracle.gghub.maa_ha` with tag `acfs_relocate_standby` to relocate the standby GGHub clusterware resources from the active node to the available node in the standby cluster.

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags acfs_relocate_standby
```

Check the status of the GGHub clusterware resources after the relocate task is complete. Notice that all of the resources should be online on the available node.

GGHub Role Reversal

The role of Primary GGHub can be reversed to a standby GGHub for planned or unplanned outages and disaster recovery. ACFS replication direction is reversed during this process. Ansible playbook `oracle.gghub.maa_ha` with tag `acfs_role_reversal` can be used to perform GGHub role reversal.

To perform a role reversal execute the playbook `oracle.gghub.maa_ha` as follows:

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags acfs_role_reversal
```

Validate the status of the resources on the new primary and standby GGHub clusters using the example commands in the "Check the Primary and Standby GGHub Clusterware Resources Status" section of [Troubleshooting GGHub Deployment Using Ansible](troubleshooting-maa-gghub.md).

The new primary GGHub should show the `acfs_primary` CRS resource state as ONLINE after the role reversal is complete.

Validate the ACFS replication status on the new primary and standby GGHub cluster using the example commands in the "Check the GGHub ACFS Mount Replication Status" section of [Troubleshooting GGHub Deployment Using Ansible](troubleshooting-maa-gghub.md).

Stopping and Starting GGHub Clusterware Resources

GGHub clusterware resources can be stopped and started on the primary and standby GGHub clusters using specific tags provided in Ansible playbook `oracle.gghub.maa_ha`.

Execute the playbook `oracle.gghub.maa_ha` to accomplish this task as below:

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags gghub_stop

(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags gghub_start
```

To stop just the primary or the standby GGHub cluster resources use the below tags.

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags gghub_stop_primary

(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags gghub_stop_standby
```

If one of the GGHub cluster resources are stopped use the `gghub_start` tag to restart. Ansible automation will detect and only start the GGHub clusterware resources where it is stopped.

### Change GoldenGate Microservices Deployment Password Using Ansible

To update the GoldenGate Microservices deployment password execute the Ansible playbook `oracle.gghub.change_password` from the GGHub Ansible collection.

The playbook will prompt for the Ansible vault password and then prompt for the new GoldenGate Microservices deployment password.

The playbook uses the existing GoldenGate Microservices deployment password from the Ansible vault, and after successful change the GoldenGate Microservices deployment password will be updated in the Ansible vault.

```
(gghub) [~]$ ansible-playbook oracle.gghub.change_password
 -i /u01/maagghub/inventory/maahub.yml --ask-vault-password
```

### Understanding NGINX Reverse Proxy and Certificate Configuration

This section explains the NGINX reverse proxy configuration and certificate usage in GGHub clusters.

The GoldenGate reverse proxy feature allows a single point of contact for all the GoldenGate microservices associated with a GoldenGate deployment. Without a reverse proxy, the GoldenGate deployment microservices are contacted using a URL consisting of a hostname or IP address and separate port numbers, one for each of the services. For example, to contact the Service Manager, you could use http://gghub.example.com:9100, then the Administration Server is http://gghub.example.com:9101, the second Service Manager may be accessed using http://gghub.example.com:9110, and so on.

When running Oracle GoldenGate in a High Availability (HA) configuration with the Grid Infrastructure agent (XAG), there is a limitation preventing more than one deployment from being managed by a GoldenGate Service Manager. Because of this limitation, creating a separate virtual IP address (VIP) for each Service Manager/deployment pair is recommended. This way, the microservices can be accessed directly using this VIP.

With a reverse proxy, port numbers are not required to connect to the microservices because they are replaced with the deployment name and the hostname's VIP. For example, to connect to the console via a web browser, use the URLs:

| GoldenGate Service | URL |
| --- | --- |
| Service Manager | https://gghub.example.com:443 |
| Administration Server | https://gghub.example.com:443/<deployment\_name>/adminsrvr |
| Distribution Server | https://gghub.example.com:443/<deployment\_name>/distsrvr |
| Performance Metric Server | https://gghub.example.com:443/<deployment\_name>/pmsrvr |
| Receiver Server | https://gghub.example.com:443/<deployment\_name>/recvsrvr |

When running multiple Service Managers, the following instructions will provide configuration using a separate VIP for each Service Manager. NGINX uses the VIP to determine which Service Manager an HTTPS connection request is routed to.

An SSL certificate is required for clients to authenticate the server they connect to through NGINX. Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.

The Ansible automation configures NGINX reverse proxy with an SSL connection and ensures all external communication is secure. The Ansible automation initially uses a self signed certificate for NGINX configuration. The certificate and key file can be replaced as per corporate security standards for production deployments following the process in

For more details on the NGINX HTTPS configuration that the Ansible automation will deploy refer to NGINX documentation at [https://nginx.org/en/docs/http/configuring\_https\_servers.html](https://nginx.org/en/docs/http/configuring_https_servers.html).

Note:

The common name in the CA-signed certificate must match the target hostname/VIP used by NGINX.
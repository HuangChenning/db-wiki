---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-3-configure-primary-and-standby-gghub-clusters-using-ansible-automation-prem.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 3: Configure Primary and Standby GGHub Clusters Using Ansible Automation

Perform the following steps to complete this task:

- Step 3.1 - Create GGHub Ansible Inventory File
- Step 3.2 - Validate SSH Connectivity and sudo Access for GGHub Nodes Using Ansible
- Step 3.3 - Deploy and Configure GGHub Using Ansible
- Step 3.4 - Validate GoldenGate Microservices Connectivity
- Step 3.5 - Replace NGINX SSL Certificate

Step 3.1 - Create GGHub Ansible Inventory File

GGHub deployment using Ansible automation requires an inventory file that contains all of the target GGHub node names and required parameters for the GGHub configuration.

Ansible playbook `oracle.gghub.onboarding` is executed to generate the Ansible inventory file.

The `oracle.gghub.onboarding` playbook configures an Ansible vault to securely store the encrypted GoldenGate admin user password, so that the password can be used securely and seamlessly during Ansible orchestration steps, as needed.

- The `oracle.gghub.onboarding` playbook requires and prompts for the Ansible vault password and the GoldenGate admin user password.
- The Ansible deployment orchestration uses a system-generated GoldenGate admin password for initial GoldenGate installation, and then changes the GoldenGate admin password to the user-supplied password at the end of the deployment.
- Both system-generated and user-supplied GoldenGate admin passwords are stored in the Ansible vault in an encrypted format.
- The Ansible vault is accessed using the Ansible vault password.

Table 3.1-1 Explanation of Ansible inventory file parameters and values

Table 26-3 Ansible inventory file parameters and values

| Ansible inventory file prompts and parameters | Description |
| --- | --- |
| GoldenGate deployment name | Deployment name which is also used in ACFS and XAG clusterware resource names. Name must begin with a character and cannot be the GoldenGate Service Manager name. Special characters that are allowed in the name include \[ - \_ /. \]. |
| GoldenGate oracle home | GoldenGate software home on the GGHub cluster nodes. |
| GoldenGate primary group | Ansible group name to identify the primary GGHub cluster nodes and associated variables. This name will be part of the primary App VIP clusterware resource name. |
| GoldenGate primary group node 1 | Primary cluster node 1 host name. Ansible orchestration host uses this name to login. |
| GoldenGate primary group node 2 | Primary cluster node 2 host name. Ansible orchestration host uses this name to login. |
| GoldenGate primary AppVIP IP address | App VIP for the primary cluster. App VIP needs to be on the public network and registered in DNS. |
| Primary ASM diskgroup name | Disk group name for the primary cluster which is used to create ACFS file system. File system size is defined by Ansible inventory file parameter ASM\_vol\_size (see ASM\_vol\_size row at the bottom of this table). |
| GoldenGate standby group | Ansible group name to identify the standby GGHub cluster nodes and associated variables. This name will be part of the standby App VIP clusterware resource name. |
| GoldenGate standby group node 1 | Standby cluster node 1 host name. Ansible orchestration host uses this name to login. |
| GoldenGate standby group node 2 | Standby cluster node 2 host name. Ansible orchestration host uses this name to login. |
| GoldenGate standby AppVIP IP address | App VIP for the standby cluster. App VIP needs to be on the public network and registered in DNS. |
| Standby ASM diskgroup name | Disk group name for the GGHub cluster which will be used to create ACFS file system. |
| ACFS mount point | Full path of the ACFS mount point. This directory is created if does not exist. The same path is used on both primary and standby GGHub clusters. |
| Local software repository directory | Full path of the software repository directory on the Ansible orchestration host. |
| Remote directory in target machines | Full path of the software staging directory on the GGHub cluster nodes. Ansible automation creates this directory if it does not exist during deployment process, and copies the required software. |
| GoldenGate patch file name | GoldenGate software complete install patch file name which is copied to the Ansible orchestration host software repository directory. |
| XAG patch file name | Oracle Grid Infrastructure standalone agent patch file name which is copied to the Ansible orchestration host software repository directory. |
| Login user for the target machines | GGHub orchestration OS user name on the GGHub cluster nodes with sudo privileges. Ansible orchestration host logs in to GGHub cluster nodes using this OS user. |
| ansible\_python\_interpreter for the target machines | Full path of the python interpreter that exists on the GGHub cluster nodes (for example, /usr/bin/python3.12 or /u01/app/oracle.ahf/common/venv/bin/python3.12).GGHub target nodes python interpreter must be 3.12 or higher version. Python version 3.12 is recommended. |
| Ansible inventory full path | Full path of the Ansible inventory directory on the Ansible orchestration host.  Ansible vault files and Ansible inventory file are created in this directory during onboarding Ansible playbook execution. |
| Password for Ansible Vault | Password which will be used to configure and access Ansible vault. Password needs to be between 8 and 30 characters with at least one lowercase character, one uppercase character and one number. See the description of Ansible vault at the beginning of this section for details. |
| Password for GoldenGate deployment | GoldenGate admin password set after initial GoldenGate installation and deployment. Password needs to be between 8 and 30 characters. Password needs to have at least one lowercase character, one uppercase character, one number and one special character from the list \[-! @ % & \*. # \_\]. |
| `GG_deployment_number` | Deployment number used if more than one GGHub deployments are managed by Ansible  Default: 1 |
| `GG_deployment_service_manager_port` | The port for the Oracle GoldenGate Service Manager, which is used for accessing the Service Manager in a web browser  Default: 9100 |
| `GG_deployment_admin_user` | Admin user for the GGHub deployment  Default: oggadmin |
| `ASM_vol_size` | Size of the ASM volume which will be used for ACFS file system  Default: 100GB |

There are two methods to generate the Ansible inventory file using the Ansible playbook `oracle.gghub.onboarding`. The recommended method is to run the Ansible onboarding playbook and answer prompts which are explained in this section.

The alternate method--to use a response file as input--is discussed in [Alternate Method to Generate Ansible Inventory File for Deployment](reference-gghub-prem.md).

Execute the `oracle.gghub.onboarding` playbook using the supplied localhost Ansible inventory file from the collections directory on the Ansible orchestration host, as shown in the following example.

```
$ source /u01/maagghub/venv/bin/activate
(gghub) [~]$ cd /u01/maagghub
(gghub) [~]$ ansible-playbook oracle.gghub.onboarding
 -i /u01/maagghub/collections/ansible_collections/oracle/gghub/inventory/localhost
```
```
Example output:

GoldenGate - Enter the GoldenGate deployment name: maahub
GoldenGate - Enter the GoldenGate ORACLE_HOME: /u01/app/oracle/goldengate/gg23ai
Primary - Enter the GoldenGate primary group: maahuba
Primary - Enter the GoldenGate primary group node 1 (Ansible will ssh using this name):
 maahuba1
Primary - Enter the GoldenGate primary group node 2 (Ansible will ssh using this name):
 maahuba2
Primary - Enter the GoldenGate primary APPVIP IP address: 10.53.240.11
Primary - Enter the ASM DiskGroup name: DATA
Standby - Enter the GoldenGate standby group: maahubb
Standby - Enter the GoldenGate standby group node 1 (Ansible will ssh using this name):
 maahubb1
Standby - Enter the GoldenGate standby group node 2 (Ansible will ssh using this name):
 maahubb2
Standby - Enter the GoldenGate standby APPVIP IP address: 10.53.240.12
Standby - Enter the ASM DiskGroup name: DATA
GGHUB - Enter the path for acfs mount point: /opt/oracle/gghub/maahub
Patch File - Enter the local software repository directory that stores software patches:
 /u01/maagghub/stage
Patch File - Enter the remote directory in target machines for staging files:
 /u01/oracle/stage
Patch File - Enter the GoldenGate patch file name:
 p37777817_23802504OGGRU_Linux-x86-64.zip
Patch File - Enter the XAG patch file name: p31215432_190000_Generic.zip
Ansible - Sets the login user for the target machines: opc
Ansible - Sets the ansible_python_interpreter for the target machines: /usr/bin/python3.12
Ansible - Enter the Ansible inventory full path directory: /u01/maagghub/inventory
Password - Enter the password for Ansible Vault ([8=>length<=30][A-Z][a-z][0-9]):
confirm Password - Enter the password for Ansible Vault ([8=>length<=30][A-Z][a-z][0-9]):
Password - Enter the password for GoldenGate deployment ''
 ([8=>length<=30][A-Z][a-z][0-9][-!@%&*.#]):
confirm Password - Enter the password for GoldenGate deployment ''
 ([8=>length<=30][A-Z][a-z][0-9][-!@%&*.#]):
```

The onboarding playbook configures the Ansible vault, creates the inventory directory and Ansible inventory file when executed using either of the two methods specified above.

The Ansible inventory file can be updated to adjust any parameter values before executing the GGHub deployment using Ansible.

Validate the Ansible vault and deployment Ansible inventory files in the `/u01/maagghub/inventory/` directory.

```
(gghub) [~]$ ls /u01/maagghub/inventory/

maahub.yml
vault_pass
maahub.key
```

GGHub inventory configuration file example:

```
(gghub) [~]$ cat /u01/maagghub/inventory/maahub.yml 

gghservers:
  children:
    maahuba:
      hosts:
        maahuba1:
        maahuba2:
      vars:
        appvip_ip_address: 10.53.240.11
        asm_diskgroup: DATA
        ansible_python_interpreter: /u01/app/oracle.ahf/common/venv/bin/python3.12
        ansible_user: opc
    maahubb:
      hosts:
        maahubb1:
        maahubb2:
      vars:
        appvip_ip_address: 10.53.240.12
        asm_diskgroup: DATA
        ansible_python_interpreter: /u01/app/oracle.ahf/common/venv/bin/python3.12
        ansible_user: opc
  vars:
    gg_deployment_name: maahub
    gg_deployment_number: 1
    gg_deployment_service_manager_port: 9100
    gg_deployment_admin_user: oggadmin
    gg_hub_groups: maahuba,maahubb
    acfs_name: maahub
    acfs_mount_point: /opt/oracle/gghub/maahub
    asm_vol_size: 100G
    gg_oracle_home: /u01/app/oracle/goldengate/gg23ai
    gg_patch_file: p37777817_23802504OGGRU_Linux-x86-64.zip
    xag_patch_file: p31215432_190000_Generic.zip
    stage_dir_local: /u01/maagghub/stage
    stage_dir_remote: /u01/oracle/stage
    ansible_inventory_dir: /u01/maagghub/inventory
```
Step 3.2 - Configure and Validate SSH Connectivity and sudo Access for GGHub Cluster Nodes Using Ansible

Configure the following passwordless ssh access:

| SSH from | SSH to | Purpose |
| --- | --- | --- |
| Ansible orchestration user (for example, `ansible`) on Ansible orchestration host | GGHub orchestration user (for example, `opc`) on each GGHub cluster node  This user must have privileged access (`su/sudo`) to `root` user. It is specified in the Ansible inventory file as `parameteransible_user`. | For Ansible to connect to GGHub nodes to perform installation, setup, and administration commands run as `root`, `grid`, or `oracle`, as required. |

Execute the below Ansible command to test the ssh connectivity from the Ansible orchestration host to GGHub nodes, and also validate `sudo` privileges on the GGHub nodes.

```
(gghub) [~]$ ansible gghservers -i /u01/maagghub/inventory/maahub.yml -m command
 -a 'sudo date'
```

The above Ansible command should return date output and return code 0 from all of the GGHub hosts specified under the gghservers group in the inventory file `maahub.yml` in this example.

Step 3.3 - Deploy GGHub on the Primary and Standby Clusters Using Ansible

To configure and deploy the MAA GoldenGate Hub on the primary and standby clusters execute the `oracle.gghub.deploy` Ansible playbook. The Ansible deploy playbook configures one VIP and service manager pair on each GGHub cluster.

The `oracle.gghub.deploy` playbook performs the following tasks on the primary and standby GGHub clusters:

- Executes prerequisite checks
- Installs Oracle GoldenGate software
- Configures ACFS file system and ACFS replication between primary and standby GGHub clusters
- Creates clusterware resources for APP VIPs
- Creates the Oracle GoldenGate Deployment
- Configures Oracle Grid Infrastructure Agent (XAG)
- Configures NGINX Reverse Proxy and creates NGINX clusterware resource
- Secures GoldenGate Microservices to restrict non-secure direct access

Execute the `oracle.gghub.deploy` playbook using the Ansible inventory file as follows:

```
(gghub) [~]$ ansible-playbook oracle.gghub.deploy
 -i /u01/maagghub/inventory/maahub.yml -e @/u01/maagghub/inventory/maahub.key
 --ask-vault-pass
```

The `oracle.gghub.deploy` playbook prompts for the Ansible vault password, displays all of the configuration information, and then asks for confirmation to continue with the deployment.

GGHub deployment playbook example output

```
Vault password:

PLAY [Play for deploying GGHUB] *******************************************************

TASK [Gather server default minimum amount of facts] **********************************
ok: [maahuba1]

TASK [oracle.gghub.oracle_meta : Assert GoldenGate deployment password] ***************
ok: [maahuba1] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Show GoldenGate Deployment] *****************************************************
<snip>

[Confirm GGHUB deployment variables]

Are you sure you want to continue with the GGHUB deployment (yes/no):

<snip>

PLAY RECAP *******************************************************************************************************
maahuba1                   : ok=233  changed=121  unreachable=0    failed=0    skipped=65   rescued=0    ignored=0
maahuba2                   : ok=139  changed=47   unreachable=0    failed=0    skipped=145  rescued=0    ignored=0
maahubb1                   : ok=180  changed=85   unreachable=0    failed=0    skipped=104  rescued=0    ignored=0
maahubb2                   : ok=139  changed=48   unreachable=0    failed=0    skipped=145  rescued=0    ignored=0
```

GGHub deployment playbook execution should not have any "failed" tasks in the Ansible PLAY RECAP summary, which is displayed at the end of the playbook execution. The "ok, changed" and "skipped" number of tasks could vary based on the environment and retry attempts.

After deployment is complete, the `oracle.gghub.verify` playbook runs automatically to display the GGHub deployment configuration information.

If issues occur during deployment, or if the configuration needs to be removed, see [Troubleshooting GGHub Deployment Using Ansible](troubleshooting-maa-gghub.md).

Step 3.4 - Validate GoldenGate Microservices Connectivity

As the `root` OS user on the first GGHub node, use the below curl command to validate the Microservices connectivity. The command will prompt for the `oggadmin` deployment password.

```
[root@gghub_prim1 ~]# vi access.cfg
user = "oggadmin"

[root@gghub_prim1 ~]# curl --insecure --user oggadmin -svf
 -K access.cfg https://<vip_name.FQDN>:<port#>/services/v2/config/health
 -XGET && echo -e "\n*** Success"

Sample output:
Enter host password for user 'oggadmin':

* Connected to maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com (10.53.240.11)
 port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
...
* Server certificate:
*  subject: C=GE; ST=San Francisco; L=California; O=Oracle; OU=Oracle MAA;
 CN=maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
*  start date: Nov 16 14:04:18 2025 GMT
*  expire date: Nov 16 14:04:18 2026 GMT
*  issuer: C=US; L=San Francisco; O=Oracle; OU=Oracle MAA;
 CN=maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com; basicConstraints=CA:true
*  SSL certificate verify result: self signed certificate in certificate chain (19),
 continuing anyway.
* Server auth using Basic with user 'oggadmin'
* TLSv1.3 (OUT), TLS app data, [no content] (0):
> GET /services/v2/config/health HTTP/1.1
> Host: maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
> Authorization: Basic b2dnYWRtaW46V0VsY29tZTEyM19f
> User-Agent: curl/7.61.1
> Accept: */*
...
<
{"$schema":"api:standardResponse","links":[{"rel":"canonical","href":
"https://maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com/services/v2/config/health",
"mediaType":"application/json"},{"rel":"self","href":
"https://maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com/services/v2/config/health",
"mediaType":"application/json"},{"rel":"describedby","href":
"https://maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com/services/ServiceManager/v2/metadata-catalog/health",
"mediaType":"application/schema+json"}],"messages":[],"response":{"$schema":"ogg:health",
"deploymentName":"ServiceManager","serviceName":"ServiceManager","started":
"2025-11-13T20:25:30.321Z","healthy":true,"criticalResources":[{"deploymentName":
"ServiceManager","name":"ServiceManager","type":"service","status":"running",
"healthy":true},{"deploymentName":"ServiceManager","name":"pluginsrvr","type":"service",
"status":"stopped","healthy":true},{"deploymentName":"maahub","name":"adminsrvr","type":
"service","status":"running","healthy":true},{* Connection #0 to host 
maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com left intact
"deploymentName":"maahub","name":"distsrvr","type":"service","status":"running","healthy":
true},{"deploymentName":"maahub","name":"recvsrvr","type":"service","status":"running",
"healthy":true}]}}
*** Success
```

Note:

If the environment is using self-signed SSL certificates, add the flag `--insecure` to the curl command to avoid the error "NSS error -8172 (SEC\_ERROR\_UNTRUSTED\_ISSUER)".

Step 3.5 - Replace NGINX SSL Certificate

Follow the below sub-steps to replace the NGINX SSL certificate and key file for your deployment orchestrated by Ansible automation.

- Step 3.5.1 - Validate NGINX configuration
- Step 3.5.2 - Identify the NGINX configuration file for the deployment
- Step 3.5.3 - Copy the certificate and key files
- Step 3.5.4 - Update the NGINX configuration file
- Step 3.5.5 - Reload and validate NGINX configuration

Note:

NGINX commands need to be run as a privileged user on the GGHub cluster nodes. Step 3.5.1 - Validate NGINX configuration

Validate the NGINX configuration using the below command:

```
# nginx -t

nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
Step 3.5.2 - Identify the NGINX configuration file for the deployment

For GGHub deployment the NGINX configuration files are located under the directory `/etc/nginx/conf.d/` and the configuration file name follows the standard `ogg_<GG_DEPLOYMENT_NAME>.conf`.

The location of the NGINX configuration files is also specified in the `/etc/nginx/nginx.conf` file.

In this example the GGHub deployment NGINX configuration file name is `ogg_maahub.conf`.

```
# ls /etc/nginx/conf.d/

ogg_maahub.conf
```
Step 3.5.3 - Copy the certificate and key files

View the GGHub NGINX configuration file and note the `ssl_certificate` and `ssl_certificate_key` parameter values in the server block:

```
# view /etc/nginx/conf.d/ogg_maahub.conf

server {
    listen                  443 ssl;
    listen             [::]:443 ssl;
    proxy_read_timeout      600s;
    proxy_buffer_size       16k;
    proxy_buffers           8 16k;
    server_name             maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com;
    ssl_certificate      /etc/nginx/ssl/maahuba-app-vip1.chained.pem;
    ssl_certificate_key  /etc/nginx/ssl/maahuba-app-vip1.key;
```

You should receive a certificate file and corresponding private key file from a Certificate Authority (CA) (for example: `your_domain.crt` and `your_domain.key`). If your CA provided a CA bundle or intermediate certificates make sure to create a chained certificate following the below guideline.

When using CA-signed certificates, the certificate named with the `ssl_certificate` NGINX parameter must include the 1) CA signed, 2) intermediate, and 3) root certificates in a single file. The order is significant; otherwise, NGINX fails to start and displays the error message:

(SSL: error:0B080074:x509 certificate routines: X509\_check\_private\_key:key values mismatch)

When using chained certificate use.pem as the file extension. This extension is commonly used when adding multiple certificates into a single file and referenced in the GoldenGate user guide.

Copy the certificate (chained certificate) and private key file to the `/etc/nginx/ssl/` directory identified from the NGINX configuration file.

Step 3.5.4 - Update the NGINX configuration file

Edit the NGINX configuration file and update the `ssl_certificate` and `ssl_certificate_key` parameter values to use the new certificate and key files.

Step 3.5.5 - Validate NGINX configuration and reload service

Validate the NGINX configuration and reload the NGINX service on the GGHub cluster nodes.

```
# nginx -t

nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

# systemctl reload nginx
# systemctl status nginx.service
```

Repeat the steps on the second node of the GGHub cluster.

Do Step 3.4 to validate GoldenGate Microservices connectivity after the change.
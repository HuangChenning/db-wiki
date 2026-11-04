---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-6-configure-network.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 6 - Configure the Network

The way you configure the network depends on your Exadata platform. The first method described in Step 6a applies to ExaDB-D only, and the second method described in Step 6b applies to ExaDB-C@C only.

Perform one of the following steps to complete this task:

- Step 6a - (ExaDB-D only) Configure Oracle Cloud Infrastructure Networking
- Step 6b - (ExaDB-C@C only) Prepare for Application Virtual IP Address Creation

Step 6a - (ExaDB-D only) Configure Oracle Cloud Infrastructure Networking

You must configure virtual cloud network (VCN) components such as private DNS zones, VIP, bastion, security lists, and firewalls for Oracle GoldenGate to function correctly.

To learn more about VCNs and security lists, including instructions for creating them, see [Oracle Cloud Infrastructure Networking](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm).

Perform the following sub-steps to complete this step:

- Step 6a.1 - Connect to GoldenGate Microservices Web Interface Using a Private IP
- Step 6a.2 - Create an Application Virtual IP Address (VIP)
- Step 6a.3 - Add Ingress Rule
- Step 6a.4 - Open Port 443 in the Firewall
- Step 6a.5 - Connecting your Source and Target VIP
- Step 6a.5 - Configuring Network Connectivity Between GoldenGate Source and Target
- Step 6a.6 - Configure Private DNS Zones Views and Resolvers
Step 6a.1 - Connect to GoldenGate Microservices Web Interface Using a Private IP

GoldenGate Microservices web interface is only accessible using a private endpoint from within the OCI network or through a bastion host that secures access to OCI resources.

If OCI Bastion service is unavailable in your region, you can use your OCI Compute Instance as a bastion. Follow the steps in [OCI Bastion As A Service](https://www.ateam-oracle.com/post/oci-bastion-as-a-service) to create your bastion. You will need one bastion for each region where Oracle GoldenGate Microservices is running.

Note:

After creating a bastion or using a compute instance as a bastion, you need to create an SSH port forwarding session to use `https://localhost:local_port` to connect to Oracle GoldenGate Microservices.

Step 6a.2 - Create an Application Virtual IP Address (VIP)

A dedicated application VIP is required to allow access to the Oracle GoldenGate Microservices using the same host name, regardless of which Oracle RAC node is hosting the services. An application VIP will also ensure the Oracle GoldenGate Distribution Server can communicate with the Distribution Receiver running the current Oracle RAC node.

The VIP is a cluster resource that Oracle Clusterware manages. The VIP is assigned to a database node and is automatically migrated to another node in the event of a node failure.

Using the Console, assign the VIP to the Oracle Exadata Database Service:

1. Open the navigation menu. Click Oracle Database, then click Exadata on Oracle Public Cloud.
2. Choose your compartment.
3. Click Exadata VM Cluster under Oracle Exadata Database Service on Dedicated Infrastructure.
4. Navigate to the Exadata VM Cluster you want to create the new VIP.
5. Under Resources, click Virtual IP Address.
6. Click Attach Virtual IP Address.
7. In the Attach Virtual IP Address dialog, enter the following mandatory information:
	- Subnet: The client subnet
		- Virtual IP address hostname: Use the SCAN DNS Name and replace the SCAN word for Oracle GoldenGate (Example: `exadb-xxxx-ggN`)
8. Click Create.

When the Virtual IP Address creation is complete, the status changes from Provisioning to Available, and the assigned IP will be shown in the Virtual IP Address. Make a note of the fully qualified domain name; this is the host name required to connect the source with the target Oracle GoldenGate deployment.

Note:

Adding a new VIP is available in most tenancies; log a Service Request if you have any issues.

Step 6a.3 - Add an Ingress Rule

Using the Console, open ingress port 443 to connect the Oracle GoldenGate service using NGINX as a reverse proxy. For more information, see [Working with Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm).

After you update the security list, it will have an entry with values similar to the following:

- Source Type: CIDR
- Source CIDR: 0.0.0.0/0
- IP Protocol: TCP
- Source Port Range: All
- Destination Port Range: 443
- Allows: TCP traffic for ports: 443 HTTPS
- Description: Oracle GoldenGate 443

Step 6a.4 - Open Port 443 in the Firewall

As the `opc` OS user, validate if the chains are currently figured to accept traffic:

```
[opc@exadb-node1 ~]$ sudo iptables --list |grep policy
 
Chain INPUT (policy ACCEPT)
Chain FORWARD (policy ACCEPT)
Chain OUTPUT (policy ACCEPT)
```

If the policy is `ACCEPT`, you can skip this step and proceed with Task 7. Otherwise, contact your network administrator to update the firewall to open port 443 for ingress activity.

Step 6a.5 - Configuring Network Connectivity Between the GoldenGate Source and Target

You can set up your VCN to access the internet if you like. You can also privately connect your VCN to public Oracle Cloud Infrastructure services such as Object Storage, your on-premises network, or another VCN.

To learn more about whether subnets are public or private, including instructions for creating the connection, see [Connectivity Choices](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#connectivity) in the Oracle Cloud Infrastructure Networking documentation.

Step 6a.6 - Configure Private DNS Zones Views and Resolvers

If the source and target Oracle GoldenGate deployments are in different regions, you must create a private DNS view in the source region with a private zone. This is required for the source Oracle GoldenGate Distribution Path to reach the target Oracle GoldenGate deployment VIP host name.

Follow the steps in [Configure private DNS zones views and resolvers](https://docs.oracle.com/en/learn/oci_private_dns/index.html#introduction) to create your private DNS view and zone.

As the `opc` OS user on the source system, use the command `nslookup` to resolve the Fully qualified domain name (from Step 6.2) of the target Oracle GoldenGate deployment:

```
[opc@exadb-node1 ~]$ nslookup <target_vip_fully_qualified_domain_name>
Server:         <DNS_IP>
Address:        <DNS_IP>#53

Non-authoritative answer:
Name:   <target_vip_fully_qualified_domain_name>
Address: <target_vip_ip>
```

Step 6b - (ExaDB-C@C only) Prepare for Application Virtual IP Address Creation

A dedicated application VIP is required to allow access to the Oracle GoldenGate Microservices using the same host name, regardless of which Oracle RAC node is hosting the services. An application VIP will also ensure that the Oracle GoldenGate Distribution Server can communicate with the Distribution Receiver running the current Oracle RAC node.

The VIP is a cluster resource that Oracle Clusterware manages. The VIP is assigned to a database node and is automatically migrated to another node in the event of a node failure.

Your system administrator must provide the IP address for the new Application VIP. This IP address must be in the same subnet as the system environment as determined above.

The VIP will be created in the next Task when you configure the Oracle Grid Infrastructure Agent.
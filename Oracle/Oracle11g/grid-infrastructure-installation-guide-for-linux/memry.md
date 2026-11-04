---
title: Configuring Large Memory Optimization
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/memry.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## C Configuring Large Memory Optimization

This appendix provides information for configuring memory optimization with large page tables on the Linux operating system, using Hugepages. It contains the following topics:

## C.1 Overview of HugePages

You can choose to configure HugePages. For some uses, HugePages can provide enhanced performance. However, this feature is an advanced configuration option. It is not a requirement for Oracle RAC.

The following is an overview of HugePages. It does not provide RPM or configuration information. The tasks you must perform for configuration depend on kernel distribution and hardware on your system. If you decide to configure your cluster nodes to use HugePages, then refer to your distribution documentation and to Oracle Technology Network (OTN) and My Oracle Support for further information.

### C.1.1 What HugePages Provides

HugePages is a feature integrated into the Linux kernel with release 2.6. It is a method to have larger pages where it is useful for working with very large memory. It can be useful for both 32-bit and 64-bit configurations. HugePage sizes vary from 2MB to 256MB, depending on the kernel version and the hardware architecture. For Oracle Databases, using HugePages reduces the operating system maintenance of page states, and increases TLB (Translation Lookaside Buffer) hit ratio.

Without HugePages, the operating system keeps each 4 KB of memory as a page, and when it is allocated to the SGA, then the lifecycle of that page (dirty, free, mapped to a process, and so on) must be kept up to date by the operating system kernel.

With HugePages, the operating system page table (virtual memory to physical memory mapping) is smaller, since each page table entry is pointing to pages from 2 MB to 256 MB. Also, the kernel has fewer pages whose lifecyle must be monitored.

For example, if you use HugePages with 64-bit hardware, and you want to map 256 MB of memory, you may need one page table entry (PTE). If you do not use HugePages, and you want to map 256 MB of memory, then you must have 256 MB \* 1024 KB/4 KB = 65536 PTEs.

## C.2 Restrictions for HugePage Configurations

To use HugePages, you must configure Grub to allocate memory for HugePages during system startup. After paging space is reserved, HugePages can be used as needed. However, if the space they require is not reserved in memory during system startup, then a HugePages allocation may fail.

HugePages are not subject to allocation or release after system startup, unless a system administrator changes the hugepages configuration by modifying the number of pages available, or the pool size.

## C.3 Disabling Transparent HugePages

Transparent HugePages memory is enabled by default with Red Hat Enterprise Linux 6, SUSE Linux Enterprise Server 11, and Oracle Linux 6 with earlier releases of Oracle Linux Unbreakable Enterprise Kernel 2 (UEK2) kernels. Transparent HugePages memory is disabled in later releases of Oracle Linux UEK2 kernels.

Transparent HugePages can cause memory allocation delays during runtime. To avoid performance issues, Oracle recommends that you disable Transparent HugePages on all Oracle Database servers. Oracle recommends that you instead use standard HugePages for enhanced performance.

Transparent HugePages memory differs from standard HugePages memory because the kernel khugepaged thread allocates memory dynamically during runtime. Standard HugePages memory is pre-allocated at startup, and does not change during runtime.

See Also:

[Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/appi_vlm.htm#UNXAR391) for information about HugePages

To check if Transparent HugePages memory is enabled, run one of the following commands as the `root` user:

Red Hat Enterprise Linux kernels:

```
# cat /sys/kernel/mm/redhat_transparent_hugepage/enabled
```

Other kernels:

```
# cat /sys/kernel/mm/transparent_hugepage/enabled
```

The following is a sample output that shows Transparent HugePages memory being used as the `[always]` flag is enabled.

```
[always] never
```

Note:

If Transparent HugePages is removed from the kernel, then the `/sys/kernel/mm/transparent_hugepage` or `/sys/kernel/mm/redhat_transparent_hugepage` files do not exist.

To disable Transparent HugePages, perform the following steps:

1. Add the following entry to the kernel boot line in the `/etc/grub.conf` file:
	```
	transparent_hugepage=never
	```
	For example:
	```
	title Oracle Linux Server (2.6.32-300.25.1.el6uek.x86_64)
	        root (hd0,0)
	        kernel /vmlinuz-2.6.32-300.25.1.el6uek.x86_64 ro root=LABEL=/   transparent_hugepage=never
	        initrd /initramfs-2.6.32-300.25.1.el6uek.x86_64.img
	```
2. Restart the system to make the changes permanent.
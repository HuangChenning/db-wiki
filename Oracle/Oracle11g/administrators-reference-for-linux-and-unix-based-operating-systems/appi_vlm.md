---
title: Very Large Memory and HugePages
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/appi_vlm.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## G Very Large Memory and HugePages

This chapter guides Linux system administrators to configure very large memory configurations and HugePages on Linux systems.

This chapter contains the following sections:

- Very Large Memory on Linux x86
- Overview of HugePages

## G.1 Very Large Memory on Linux x86

Very Large Memory (VLM) configurations allow a 32-bit Oracle Database to access more than 4GB RAM that is traditionally available to Linux applications. The Oracle VLM option for 32-bit creates a large database buffer cache using an in-memory file system (`/dev/shm`). Other parts of the SGA are allocated from regular memory. VLM configurations improve database performance by caching more database buffers in memory, which significantly reduces the disk I/O compared to configurations without VLM. This chapter shows how to increase the SGA memory using VLM on a 32-bit computer.

Note:

The contents documented in this section apply only to 32-bit Linux operating system. With a 64-bit architecture, VLM support is available natively. All 64-bit Linux operating systems use the physical memory directly, as the maximum available virtual address space is 16 EB (exabyte = 2^60 bytes.)

This section includes the following topics:

### G.1.1 Implementing VLM on 32-bit Linux

With 32-bit architectures, VLM is accessed through a VLM window of a specific size. The VLM window is a data structure in the process address space that provides access to the whole virtual address space from a window of a specific size. On 32-bit Linux, you must set the parameter `USE_INDIRECT_DATA_BUFFERS=TRUE`, and mount a `shmfs` or `tmpfs` or `ramfs` type of in-memory filesystem over `/dev/shm` to increase the usable address space.

### G.1.2 Prerequisites for Implementing VLM

The following are some of the prerequisites for implementing VLM on a 32-bit operating system:

- The computer on which Oracle Database is installed must have more than 4GB of memory.
- The computer must be configured to use a kernel with PAE support upon startup.
- The `USE_INDIRECT_DATA_BUFFERS=TRUE` must be present in the initialization parameter file for the database instance that uses VLM support.
- Initialization parameters `DB_BLOCK_BUFFERS` and `DB_BLOCK_SIZE` must be set to values you have chosen for the Oracle Database.

### G.1.3 Methods To Increase SGA Limits

In a typical 32-bit Linux kernel, one can create an SGA of up to 2.4GB size. Using a Linux Hugemem kernel enables the creation of an SGA of upto 3.2GB size. To go beyond 3.2GB on a 32-bit kernel, you must use the VLM feature.

The following are the methods to increase SGA limits on a 32-bit computer:

- Hugemem Kernel
- Hugemem Kernel with Very Large Memory

#### G.1.3.1 Hugemem Kernel

Red Hat Enterprise Linux 4 and Oracle Linux 4 include a new kernel known as the Hugemem kernel. The Hugemem kernel feature is also called a 4GB-4GB Split Kernel as it supports a 4GB per process user space (versus 3GB for the other kernels), and a 4GB direct kernel space. Using this kernel enables RHEL 4/Oracle Linux 4 to run on systems with up to 64GB of main memory. The Hugemem kernel is required to use all the memory in system configurations containing more than 16GB of memory. The Hugemem kernel can run configurations with less memory.

A classic 32-bit 4GB virtual address space is split 3GB for user processes and 1GB for the kernel. The new scheme (4GB/4GB) permits 4GB of virtual address space for the kernel and almost 4GB for each user process. Due to this scheme with hugemem kernel, 3.2GB of SGA can be created without using the indirect data buffer method.

Note:

Red Hat Enterprise Linux 5/ Oracle Linux 5 and Red Hat Enterprise Linux 6/ Oracle Linux 6 on 32-bit does not have the hugemem kernel. It supports only the 3GB user process/ 1GB kernel split. It has a PAE kernel that supports systems with more than 4GB of RAM and reliably upto 16GB. Since this has a 3GB/1GB kernel split, the system may run out of lowmem if the system's load consumes lots of lowmem. There is no equivalent kernel for hugemem in Enterprise Linux 5 and one is recommended to either use Enterprise Linux 4 with hugemem or go for 64-bit.

The Hugemem kernel on large computers ensures better stability as compared to the performance overhead of address space switching.

Run the following command to determine if you are using the `Hugemem` kernel:

```
$ uname -r
2.6.9-5.0.3.ELhugemem
```

#### G.1.3.2 Hugemem Kernel with Very Large Memory

If you use only Hugemem kernels on 32-bit systems, then the SGA size can be increased but not significantly. Refer to section "Hugemem Kernel", for more information.

Note:

Red Hat Enterprise Linux 5/ Oracle Linux 5 and Red Hat Enterprise Linux 6/ Oracle Linux 6 does not support the hugemem kernel. It supports a PAE kernel that can be used to implement Very Large Memory (VLM) as long as the physical memory does not exceed 16GB.

This section shows how the SGA can be significantly increased by using Hugemem kernel with VLM on 32-bit systems.

The SGA can be increased to about 62GB (depending on block size) on a 32-bit system with 64GB RAM. A processor feature called Page Address Extension (PAE) permits you to physically address 64GB of RAM. Since PAE does not enable a process or program to either address more than 4GB directly, or have a virtual address space larger than 4GB, a process cannot attach to shared memory directly. To address this issue, a shared memory filesystem (memory-based filesystem) must be created which can be as large as the maximum allowable virtual memory supported by the kernel. With a shared memory filesystem processes can dynamically attach to regions of the filesystem allowing applications like Oracle to have virtually a much larger shared memory on 32-bit operating systems. This is not an issue on 64-bit operating systems.

VLM moves the database buffer cache part of the SGA from the System V shared memory to the shared memory filesystem. It is still considered one large SGA but it consists now of two different operating system shared memory entities. VLM uses 512MB of the non-buffer cache SGA to manage VLM. This memory area is needed for mapping the indirect data buffers (shared memory filesystem buffers) into the process address space since a process cannot attach to more than 4GB directly on a 32-bit system.

Note:

`USE_INDIRECT_DATA_BUFFERS` = `TRUE` must be present in the initialization parameter file for the database instance that use Very Large Memory support. If this parameter is not set, then Oracle Database 11g Release 2 (11.2) or later behaves in the same way as previous releases.

You must also manually set the initialization parameters `DB_BLOCK_BUFFERS` and `SHARED_POOL_SIZE` to values you have chosen for an Oracle Database. Automatic Memory Management (AMM) cannot be used. The initialization parameter `DB_BLOCK_SIZE` sets the block size and in combination with `DB_BLOCK_BUFFERS` determines the buffer cache size for an instance

For example, if the non-buffer cache SGA is 2.5GB, then you will only have 2GB of non-buffer cache SGA for shared pool, large pool, and redo log buffer since 512MB is used for managing VLM. It is not recommended to use VLM if buffer cache size is less than 512MB.

In RHEL 4/ Oracle Linux 4 there are two different memory file systems that can be used for VLM:

- `tmpfs or shmfs`: mount a `shmfs` with a certain size to `/dev/shm`, and set the correct permissions. For `tmpfs` you do not need to specify a size. `Tmpfs or` `shmfs` allocated memory is pageable.
	For example:
	```
	Example Mount shmfs:
	# mount -t shm shmfs -o size=20g /dev/shm
	Edit /etc/fstab:
	shmfs /dev/shm shm size=20g 0 0
	OR
	Example Mount tmpfs:
	# mount –t tmpfs tmpfs /dev/shm
	Edit /etc/fstab:
	none /dev/shm tmpfs defaults 0 0
	```
- `ramfs`: `ramfs` is similar to `shmfs`, except that pages are not pageable or swappable. This approach provides the commonly desired effect. `ramfs` is created by:
	```
	umount /dev/shm
	mount -t ramfs ramfs /dev/shm
	```

### G.1.4 Configuring Very Large Memory for Oracle Database

Complete the following procedure to configure Very Large Memory on Red Hat Enterprise Linux 4/ Oracle Linux 4 using `ramfs`:

1. Log in as a `root` user:
	```
	sudo -sh
	Password:
	```
2. Edit the `/etc/rc.local` file and add the following entries to it to configure the computer to mount `ramfs` over the `/dev/shm` directory, whenever you start the computer:
	```
	umount /dev/shm
	mount -t ramfs ramfs /dev/shm
	chown oracle:oinstall /dev/shm
	```
	In the preceding commands, `oracle` is the owner of Oracle software files and `oinstall` is the group for Oracle owner account. If the new configuration disables `/etc/rc.local` file or you start an instance of Oracle database using a Linux service script present under the `/etc/init.d` file, then you can add those entries in the service script too.
	Note, this configuration will make `ramfs` ready even before your system autostarts crucial Oracle Database instances. The commands can also be included in your startup scripts. It is important that you test the commands extensively by repeated restart action, after you complete configuring the computer using the following steps:
3. Restart the server.
4. Log in as a `root` user.
5. Run the following command to check if the `/dev/shm` directory is mounted with the ramfs type:
	```
	/dev/shm directory is mounted with the ramfs type:
	# mount | grep shm
	ramfs on /dev/shm type ramfs (rw)
	```
6. Run the following command to check the permissions on the `/dev/shm` directory:
	```
	# ls -ld /dev/shm
	drwxr-xr-x  3 oracle oinstall 0 Jan 13 12:12 /dev/shm
	```
7. Edit the `/etc/security/limits.conf` file and add the following entries to it to increase the max locked memory limit:
	```
	soft    memlock        3145728
	hard    memlock        3145728
	```
8. Switch to the `oracle` user:
	```
	# sudo - oracle
	Password:
	```
9. Run the following command to check the max locked memory limit:
	```
	$ ulimit -l
	3145728
	```
10. Complete the following procedure to configure instance parameters for Very Large Memory:
	1. Replace the `DB_CACHE_SIZE`, `DB_xK_CACHE_SIZE`, `sga_target`, and `memory_target` parameters with `DB_BLOCK_BUFFERS` parameter.
		2. Add the `USE_INDIRECT_DATA_BUFFERS=TRUE` parameter.
		3. Configure SGA size according to the SGA requirements.
		4. Remove `SGA_TARGET`, `MEMORY_TARGET`, or `MEMORY_MAX_TARGET` parameters, if set.
11. Start the database instance.
12. Run the following commands to check the memory allocation:
	```
	$ ls -l /dev/shm
	$ ipcs -m
	```

See Also:

"Configuring HugePages on Linux" section for more information about HugePages.

### G.1.5 Restrictions Involved in Implementing Very Large Memory

Following are the limitations of running a computer in the Very Large Memory mode:

- You cannot use Automatic Memory Management (AMM) while implementing VLM using `ramfs`, because AMM works on dynamic SGA tuning. With AMM swapping is possible. For example, you can unmap the unused SGA space and map it to PGA. Dynamic SGA and multiple block size are not supported with Very Large Memory because `ramfs` is not swappable. To enable Very Large Memory, you must ensure that you set the value of `MEMORY_TARGET` to zero.
- VLM can be implemented only if Database Buffer Cache size is greater than 512MB.

## G.2 Overview of HugePages

HugePages is a feature integrated into the Linux kernel 2.6. Enabling HugePages makes it possible for the operating system to support memory pages greater than the default (usually 4KB). Using very large page sizes can improve system performance by reducing the amount of system resources required to access page table entries. HugePages is useful for both 32-bit and 64-bit configurations. HugePage sizes vary from 2MB to 256MB, depending on the kernel version and the hardware architecture. For Oracle Databases, using HugePages reduces the operating system maintenance of page states, and increases Translation Lookaside Buffer (TLB) hit ratio.

This section includes the following topics:

- Tuning SGA With HugePages
- Configuring HugePages on Linux
- Restrictions for HugePages Configurations
- Disabling Transparent HugePages

### G.2.1 Tuning SGA With HugePages

Without HugePages, the operating system keeps each 4KB of memory as a page, and when it is allocated to the SGA, then the lifecycle of that page (dirty, free, mapped to a process, and so on) is kept up to date by the operating system kernel.

With HugePages, the operating system page table (virtual memory to physical memory mapping) is smaller, since each page table entry is pointing to pages from 2MB to 256MB. Also, the kernel has fewer pages whose lifecyle must be monitored.

Note:

2MB size of HugePages is available with Linux x86-64, Linux x86, and IBM: Linux on System z.

The following are the advantages of using HugePages:

- Increased performance through increased TLB hits.
- Pages are locked in memory and are never swapped out which guarantees that shared memory like SGA remains in RAM.
- Contiguous pages are preallocated and cannot be used for anything else but for System V shared memory (for example, SGA)
- Less bookkeeping work for the kernel for that part of virtual memory due to larger page sizes

### G.2.2 Configuring HugePages on Linux

Complete the following steps to configure HugePages on the computer:

1. Edit the `memlock` setting in the `/etc/security/limits.conf` file. The `memlock` setting is specified in KB and set slightly lesser than the installed RAM. For example, if you have 64GB RAM installed, add the following entries to increase the max locked memory limit:
	```
	*   soft   memlock    60397977
	*   hard   memlock    60397977
	```
	You can also set the `memlock` value higher than your SGA requirements.
2. Login as the `oracle` user again and run the `ulimit -l` command to verify the new `memlock` setting:
	```
	$ ulimit -l
	60397977
	```
3. Run the following command to display the value of `Hugepagesize` variable:
	```
	$ grep Hugepagesize /proc/meminfo
	```
4. Complete the following procedure to create a script that computes recommended values for `hugepages` configuration for the current shared memory segments:
	Note:
	Following is an example that may require modifications.
	1. Create a text file named `hugepages_settings.sh`.
		2. Add the following content in the file:
		```
		#!/bin/bash
		#
		# hugepages_settings.sh
		#
		# Linux bash script to compute values for the
		# recommended HugePages/HugeTLB configuration
		#
		# Note: This script does calculation for all shared memory
		# segments available when the script is run, no matter it
		# is an Oracle RDBMS shared memory segment or not.
		# Check for the kernel version
		KERN=\`uname -r | awk -F. '{ printf("%d.%d\n",$1,$2); }'\`
		# Find out the HugePage size
		HPG_SZ=\`grep Hugepagesize /proc/meminfo | awk {'print $2'}\`
		# Start from 1 pages to be on the safe side and guarantee 1 free HugePage
		NUM_PG=1
		# Cumulative number of pages required to handle the running shared memory segments
		for SEG_BYTES in \`ipcs -m | awk {'print $5'} | grep "[0-9][0-9]*"\`
		do
		   MIN_PG=\`echo "$SEG_BYTES/($HPG_SZ*1024)" | bc -q\`
		   if [ $MIN_PG -gt 0 ]; then
		      NUM_PG=\`echo "$NUM_PG+$MIN_PG+1" | bc -q\`
		   fi
		done
		# Finish with results
		case $KERN in
		   '2.4') HUGETLB_POOL=\`echo "$NUM_PG*$HPG_SZ/1024" | bc -q\`;
		          echo "Recommended setting: vm.hugetlb_pool = $HUGETLB_POOL" ;;
		   '2.6'|'3.8') echo "Recommended setting: vm.nr_hugepages = $NUM_PG" ;;
		    *) echo "Unrecognized kernel version $KERN. Exiting." ;;
		esac
		# End
		```
		3. Run the following command to change the permission of the file:
		```
		$ chmod +x hugepages_settings.sh
		```
5. Run the `hugepages_settings.sh` script to compute the values for `hugepages` configuration:
	```
	$ ./hugepages_settings.sh
	```
6. Set the following kernel parameter:
	```
	# sysctl -w vm.nr_hugepages=value_displayed_in_step_5
	```
7. To make the value of the parameter available for every time you restart the computer, edit the `/etc/sysctl.conf` file and add the following entry:
	```
	vm.nr_hugepages=value_displayed_in_step_5
	```
8. Restart the server.
	Note:
	To check the available `hugepages`, run the following command:
	```
	$ grep Huge /proc/meminfo
	```

### G.2.3 Restrictions for HugePages Configurations

Following are the limitations of using HugePages:

- Automatic Memory Management (AMM) and HugePages are not compatible. When you use AMM, the entire SGA memory is allocated by creating files under `/dev/shm`. When Oracle Database allocates SGA with AMM, HugePages are not reserved. To use HugePages on Oracle Database 12c, You must disable AMM.
- If you are using VLM in a 32-bit environment, then you cannot use HugePages for the Database Buffer cache. You can use HugePages for other parts of the SGA, such as `shared_pool`, `large_pool`, and so on. Memory allocation for VLM (buffer cache) is done using shared memory file systems (`ramfs/tmpfs/shmfs`). Memory file systems do not reserve or use HugePages.
- HugePages are not subject to allocation or release after system startup, unless a system administrator changes the HugePages configuration, either by modifying the number of pages available, or by modifying the pool size. If the space required is not reserved in memory during system startup, then HugePages allocation fails.

### G.2.4 Disabling Transparent HugePages

Transparent HugePages memory is enabled by default with Red Hat Enterprise Linux 6, SUSE 11, and Oracle Linux 6 with earlier releases of Oracle Linux Unbreakable Enterprise Kernel 2 (UEK2) kernels. Transparent HugePages memory is disabled by default in later releases of UEK2 kernels.

Transparent HugePages can cause memory allocation delays at runtime. To avoid performance issues, Oracle recommends that you disable Transparent HugePages on all Oracle Database servers. Oracle recommends that you instead use standard HugePages for enhanced performance.

Transparent HugePages memory differs from standard HugePages memory because the kernel `khugepaged` thread allocates memory dynamically during runtime. Standard HugePages memory is pre-allocated at startup, and does not change during runtime.

To check if Transparent HugePages is enabled run one of the following commands as the `root` user:

Red Hat Enterprise Linux kernels:

```
# cat /sys/kernel/mm/redhat_transparent_hugepage/enabled
```

Other kernels:

```
# cat /sys/kernel/mm/transparent_hugepage/enabled
```

The following is a sample output that shows Transparent HugePages is being used as the `[always]` flag is enabled.

```
[always] never
```

Note:

If Transparent HugePages is removed from the kernel then the `/sys/kernel/mm/transparent_hugepage` or `/sys/kernel/mm/redhat_transparent_hugepage` files do not exist.

To disable Transparent HugePages perform the following steps:

1. Add the following entry to the kernel boot line in the `/etc/grub.conf` file:
	```
	transparent_hugepage=never
	```
	For example:
	```
	title Oracle Linux Server (2.6.32-300.25.1.el6uek.x86_64)
	        root (hd0,0)
	        kernel /vmlinuz-2.6.32-300.25.1.el6uek.x86_64 ro root=LABEL=/ transparent_hugepage=never
	        initrd /initramfs-2.6.32-300.25.1.el6uek.x86_64.img
	```
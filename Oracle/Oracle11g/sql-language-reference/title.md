---
title: "Oracle Database SQL Language Reference, 11g Release 2 (11.2)"
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/title.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

## Oracle® Database

SQL Language Reference

11g Release 2 (11.2)

E41084-04

---

Oracle Database SQL Language Reference, 11g Release 2 (11.2)

E41084-04

Copyright © 1996, 2016, Oracle and/or its affiliates. All rights reserved.

Primary Authors: Diana Lorentz, Mary Beth Roeser

Contributors: Sundeep Abraham, Angela Amor, Geeta Arora, Vikas Arora, Lance Ashdown, Hermann Baer, Shrikanth Bellamkonda, Donna Carver, Dan Chiba, Timothy Chien, Alan Choi, Thierry Cruanes, George Eadon, Amit Ganesh, Barb Glover, Naveen Gopal, Mike Hallas, Min-Hank Ho, Chandrasekharan Iyer, Mark Jaeger, Vikram Kapoor, Peter Knaggs, Srinath Krishnaswamy, Andre Kruglikov, Paul Lane, Huagang Li, Yunrui Li, Vince Liang, Bryn Llewellyn, Rich Long, Scott Lynn, Vineet Marwah, Jun Matsuzawa, Robert McGuirk, Rahil Mir, Gopal Mulagund, Sujatha Muthulingam, Hanlin Qian, Ashish Ray, John Russell, Laurent Schneider, Vivian Schupmann, Jia Shi, Ajeet Singh, Wayne Smith, Shanshan Song, Vinay Srihari, Jim Stenoish, Sankar Subramanian, Seema Sundara, Mark van de Wiel, Badhri Varanasi, William Waddington, Peter Wahl, Charles Wetherell, Sergiusz Wolicki, Daniel Wong, Tsae-feng Yu, Mohamed Zait, Fred Zemke, Wei Zhang, Weiran Zhang

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, then the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, delivered to U.S. Government end users are "commercial computer software" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, use, duplication, disclosure, modification, and adaptation of the programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, shall be subject to license terms and license restrictions applicable to the programs. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information about content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services unless otherwise set forth in an applicable agreement between you and Oracle. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services, except as set forth in an applicable agreement between you and Oracle.
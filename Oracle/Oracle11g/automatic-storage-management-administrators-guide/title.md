---
title: "Oracle Automatic Storage Management Administrator's Guide, 11g Release 2 (11.2)"
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/title.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## Oracle® Automatic Storage Management

Administrator's Guide

11g Release 2 (11.2)

E18951-03

---

Oracle Automatic Storage Management Administrator's Guide, 11g Release 2 (11.2)

E18951-03

Copyright © 2007, 2012, Oracle and/or its affiliates. All rights reserved.

Contributing Authors: Jerry Abraham, Prasad Bagal, Mark Bauer, Eric Belden, Bill Bridge, Chan Chan, Xiaobin Chen, Hanlin Chien, Jonathan Creighton, Steve Fogel, Dave Friedman, Barb Glover, Fred Glover, Allan Graves, Shie-rei Huang, Rekha Iyer, Diane Lebel, Rich Long, Colin McGregor, Gregory Mengel, Harendra Mishra, Valarie Moore, Nitin Munjal, Darshan Nagarajappa, Harish Nandyala, Bob Nelson, Balaji Pagadala, Satish Panchumarthy, Soma Prasad, Kathy Rich, Harshavardhan Sabbineni, Francisco Sanchez, Santhosh Selvaraj, Ara Shakian, Duane Smith, Joshua Smith, Malai Stalin, Amar Subba, Yaser Suleiman, Elisabeth Thibault, Michael Timpanaro-Perrotta, Samarjeet Tomar, Brian Tsao, Nitin Vengurlekar, P Venkatraman, Anton Verhulst, Radek Vingralek, Ron Weiss, Ric Werme, Rajiv Wickremesinghe, Jim A. Williams, Sivakumar Yarlagadda, Song Ye, Krishnan Yegnashankaran, Hector Yuen, Jon Zolla

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, the following notice is applicable:

U.S. GOVERNMENT RIGHTS Programs, software, databases, and related documentation and technical data delivered to U.S. Government customers are "commercial computer software" or "commercial technical data" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, the use, duplication, disclosure, modification, and adaptation shall be subject to the restrictions and license terms set forth in the applicable Government contract, and, to the extent applicable by the terms of the Government contract, the additional rights set forth in FAR 52.227-19, Commercial Computer Software License (December 2007). Oracle America, Inc., 500 Oracle Parkway, Redwood City, CA 94065.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information on content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services.
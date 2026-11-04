---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/index.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

12c Release 2 (12.2)

E85760-09

---

Oracle Database Database Administrator’s Guide, 12c Release 2 (12.2)

E85760-09

Copyright © 2001, 2020, Oracle and/or its affiliates.

Primary Author: Rajesh Bhatiya, Padmaja Potineni

Contributing Author: Randy Urbano, Virginia Beecher, Leo Cloutier, Steve Fogel, Chuck Murray

Contributor: A. Agrawal, L. Ashdown, P. Avril, D. Austin, T. Baby, H. Baer, S. Ball, S. Battula, M. Bauer, T. Bednar, E. Belden, J. Byun, L. Carpenter, A. Chaudhry, C. Chang, B. Cheng, H. Chien, T. Chien, G. Christman, C. C. Chui, L. Clarke, D. Colello, C. Colrain, K. Cook, J. Creighton, A. Dadhich, S. Datta, S. Davidson, M. Dilman, S. Doraiswamy, J. Draaijer, M. Fallen, M. Fuller, D. Gagne, A. Ganesh, GP Gongloor, J. Gonzalez, V. Goorah, S. Gopalan, S. Gupta, B. Habeck, S. Hase, W. Hu, P. Huey, K. Inoue, M. Ito, C. Iyer, K. Itikarlapalli, P. Jaganath, S. Jain, C. Jones, S. Joshi, B. Khaladkar, F. Kobylanski, B. Krishnan, V. Krishnaswamy, A. Kruglikov, B. Kuchibhotla, V. Kuhr, R. Kumar, S. Kumar, V. Kumar, H. Lakshmanan, A. Lee, B. Lee, J. Lee, S. K. Lee, T. Lee, C. Lei, B. Leung, Y. Li, I. Listvinsky, B. Llewellyn, H. Lombera, B. Lundhild, S. Lynn, R. Mani, V. Marwah, C. McGregor, J. McDonnell, J. McHugh, B. McGuirk, J. Meeks, K. Mensah, M. Minhas, K. Mohan, H. Mohankumar, A. Munnolimath, G. Mulagund, P. Murguia, P. Murthy, A. Mylavarapu, V. Moore, N. Muthukrishnan, S. Muthulingam, L. Nim, S. Panchumarthy, R. Pang, V. Panteleenko, R. Pingte, K. Rajamani, A. Raghavan, M. Ramacher, R. Ramkissoon, S. Ravindhran, G. Ravipati, A. Ray, W. Ren, K. Rich, J. Rivera, C. A. L. Rueda, R. Rungta, S. Sahu, P. Shanthaveerappa, S. Sonawane, Y. Sarig, M. Savanur, S. Shankar, D. Sharma, A. Shen, B. Sinha, J. Spiller, D. Steiner, J. Stern, M. Stewart, S. Stoian, R. Swonger, M. Subramaniam, N. Sundarappa, M. Susairaj, A. Tran, A. Tsukerman, C. Tuzla, T. Ueda, K. Umamageswaran, D. Utzig, E. Voss, N. Wagner, X. Wang, M. Wei, S. Wertheimer, P. Wheeler, D. Williams, A. Witkowski, S. Wolicki, D. M. Wong, Z. Yang, T. F. Yu, W. Zhang

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, then the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs (including any operating system, integrated software, any programs embedded, installed or activated on delivered hardware, and modifications of such programs) and Oracle computer documentation or other Oracle data delivered to or accessed by U.S. Government end users are "commercial computer software" or “commercial computer software documentation” pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, the use, reproduction, duplication, release, display, disclosure, modification, preparation of derivative works, and/or adaptation of i) Oracle programs (including any operating system, integrated software, any programs embedded, installed or activated on delivered hardware, and modifications of such programs), ii) Oracle computer documentation and/or iii) other Oracle data, is subject to the rights and limitations specified in the license contained in the applicable contract. The terms governing the U.S. Government’s use of Oracle cloud services are defined by the applicable contract for such services. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Inside are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Epyc, and the AMD logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information about content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services unless otherwise set forth in an applicable agreement between you and Oracle. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services, except as set forth in an applicable agreement between you and Oracle.
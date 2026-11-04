---
title: "26、如何查看当前数据库的安全策略"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/security_policy.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 如何查看当前数据库的安全策略

使用psql命令或客户端工具，通过管理员用户(企业版V6：默认highgo。安全版：syssso)连接数据库执行select show\_secure\_param();即可查看当前数据库的安全策略。

## 1、企业版数据库V6：

```
psql -d highgo -U highgo  
highgo=# select show_secure_param();
           show_secure_param           
---------------------------------------
 hg_idcheck.pwdlock = 5 time(s),      +
 hg_idcheck.pwdlocktime = 24 hour(s), +
 hg_idcheck.pwdvaliduntil = 7 day(s), +
```

安全策略参数包括hg\_idcheck.pwdlock、hg\_idcheck.pwdlocktime 和hg\_idcheck.pwdvaliduntil。通过调用sql函数show\_secure\_param()可查看当前安全策略参数的配置值。

sql函数set\_secure\_param()可设定某一配置，例如selcet set\_secure\_param(‘hg\_idcheck.pwdlock’,’3’)可将hg\_idcheck.pwdlock的值设为3。另外，只有管理员用户才有权限查看和设置安全策略参数。

参数名称及其对应功能如下：

hg\_idcheck.pwdlock：可以输错密码的次数，当密码输错次数超过此限定值时用户会被锁定，须通过管理员用户调用user\_unlock(‘username’)进行解锁。默认值为5。取值范围0~10。开关参数Passwordlock。

hg\_idcheck.pwdlocktime：密码锁定后自动解锁需要经过的时间，单位为Dd/Hh/Mm/Ss（天/小时/分钟/秒），默认值为24hours。

hg\_idcheck.pwdvaliduntil：当创建用户或修改用户密码且缺省validuntil时密码经过多长时间后过期，单位天，默认值7，取值范围0~365。开关参数Passwordvaliduntil。

## 2、安全版数据库V4.5：

```
psql -d highgo -U syssso
highgo=> select show_secure_param();
            show_secure_param            
-----------------------------------------
   hg_sepofpowers = on,                 +
   hg_macontrol = on,                   +
   hg_rowsecure = on,                   +
   hg_showlogininfo = on,               +
   hg_clientnoinput = 30 min(s),        +
   hg_idcheck.enable = on,              +
   hg_idcheck.pwdlock = 5 time(s),      +
   hg_idcheck.pwdlocktime = 24 hour(s), +
   hg_idcheck.pwdvaliduntil = 10 day(s), +
   hg_idcheck.pwdpolicy = highest,      +
```

安全参数的显示：

登录syssso用户，执行select show\_secure\_param(); 可以显示所有的安全参数。

安全参数的设置：

登录syssso用户，执行select set\_secure\_param(‘参数名’,’参数值’);来设置某个安全参数的值。

注：参数名和参数值都需要用西文单引号包括。

例如：select set\_secure\_param(‘hg\_showlogininfo’,’off’);

则会关闭登录信息的显示。

有些安全参数还拥有子参数，这时在安全参数和子参数之间加一个.即可例如：select set\_secure\_param(‘hg\_idcheck.pwdlocktime’,’3’);

有些安全参数是即时生效，有些安全参数是重启数据库后生效。例如设置hg\_clientnoinput参数后，需要重启才能生效。

每个参数的说明如下：

hg\_idcheck.子参数名：

enable：该参数相当于以下四个子参数的总开关。默认值为on，开启身份鉴别，其他子参数以默认值显示;off为关闭身份鉴别，所有身份鉴别相关参数均不生效。参数值重启生效。

pwdlock：密码连续输入错误多少次后账户被锁，默认5次。参数范围值为0-10次,设置为0表示不限制密码错误次数，重启后密码连续错误次数重新计算。参数值动态（不重启）生效。

pwdlocktime：密码连续错误次数超限被锁定的时间，默认24小时，参数范围值为0-240小时。设置为0则表示一直被锁定，但可以通过syssso解锁。参数值动态（不重启）生效。

pwdvaliduntil：参数功能为密码有效期，参数范围值为0-365天，默认7天，设置值为0表示不限制天数。参数值动态（不重启）生效。

pwdpolicy：参数有low、medium、high、highest四个参数值，设置为low时表示密码不受限制，与原生PG保持一致；设置为medium表示密码长度至少为8位，必须包含字母和数字；设置为high表示密码长度至少为8位，必须包含字母、数字和特殊字符。highest,包含常用密码、保留字、关键字等所有密码规则。默认为highest参数值动态（不重启）生效。

hg\_sepofpowers：三权分立开关，默认on，off为关闭三权分立，关闭后即无安全功能。参数值重启生效。

hg\_macontrol：默认on，开启强制访问控制；参数值为min，表示强访功能最小化，即只有自主访问控制功能。参数值重启生效。

hg\_rowsecure：用来开关行级强制访问控制，该参数只在hg\_macontrol为on时生效。参数值为on|off，on为开启行级访问控制，off为关闭行级访问控制，开启表级访问控制。默认为off。参数值重启生效。

hg\_showlogininfo：参数功能为显示登入信息（管理工具和psql客户端，参数值为on|off，on为开启功能，off为关闭功能，默认on。参数值动态生效。

hg\_clientnoinput：参数表示session不活动无操作自动断开的时间(有事务运行则不会断开)，参数范围值为0-1440分钟；默认30分钟，设置为0则不限制。参数值重启生效。

## 3、安全版数据库V4：

```
psql -d highgo -U syssso
highgo=> select show_secure_param();
      show_secure_param      
-----------------------------
 Secure level = on,        +
   hg_SepOfPowers = on,    +
   hg_MAControl = on,      +
   hg_RowSecure = on,      +
 hg_PwdValidUntil = 350,    +
 hg_PwdErrorLock = 5,       +
 hg_ShowLoginInfo = on,     +
 hg_ClientNoInput = 30 min, +
 hg_PwdRule = on,           +
```

安全管理员可以通过select show\_secure\_param();来随时查看当前的安全策略。每个参数的说明如下：

hg\_SepOfPowers，三权分立开关。

hg\_MAControl，强制访问控制开关。

hg\_RowSecure，行安全开关。

hg\_PwdValidUntil，密码有效期设置参数。

hg\_PwdErrorLock，密码错误次数设置参数。

hg\_ShowLoginInfo，用户登录信息开关。

hg\_ClientNoInput，超时断开设置参数。

hg\_PwdRule，密码复杂度开关。

安全管理员可以通过，select set\_secure\_param(‘parm’, ‘value’);进行设置，第一个参数是要配置的参数名称，后边是要设置的值，两个参数全部都是字符串类型。
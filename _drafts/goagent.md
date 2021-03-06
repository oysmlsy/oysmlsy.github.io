---
layout: post
title:  "利用 GoAgent、gogotester 翻墙"
---
## 注册 Google 账户

建议为翻墙专门注册一个 Google 账户，本文写作时注册 Google 账户可以不验证手机号。

## 在 GAE 上建立工程

Google App Engine，简称 GAE，地址是 https://appengine.google.com。

用 Google 账户登录 GAE，找到 Google Developers Console 的链接，进入 Google Developers Console 页面。

点击 Create Project 按钮，弹出 New Project 对话框。

在 Project name 处填写工程名字，大小写、数字随意，但注意 Project ID 自动全部是小写。勾选 I agree that ...... 复选框，点击 Create 按钮，工程建立完成。

如此反复多建立几个工程。

## 下载 GoAgent

GoAgent 托管在 GitHub 上，地址是 https://github.com/goagent/goagent，本文写作时的版本是 3.2.3。

## 修改 proxy.ini 文件

将下载的 GoAgent 压缩包解压缩，里面有 local 文件夹、server 文件夹和 README.md 文件。

进入 local 文件夹，打开 proxy.ini 文件，将 appid = goagent 处的 goagent 改成 GAE 上的 Project ID，可以输入一个，也可以输入多个，多个 appid 用 | 隔开。

## 上传应用到 GAE

进入 server 文件夹，运行 uploader 脚本。这时需要区分操作系统。

Windows 系统：

    双击 uploader.bat

Linux 系统：

    $ python server/uploader.py

Mac 系统：

    $ python server/uploader.py

在打开的命令行中提示输入 APPID。这里输入的 appid 就是在 GAE 中建立的 project 名称，可以输入一个，也可以输入多个，多个 appid 用 | 隔开。

输入 appid，点击回车，提示输入 Email。这里的 Email 就是 Google 账户名。

输入 Email，点击回车，提示输入密码。

## 利用 gogotester 寻找可用的 Google IP

这段时间 Google IP 大量被封，GoAgent 受到严重影响，黑窗口中会出现大量的黄色警告，导致网页打开速度慢甚至根本打不开。

我们利用 gogotester 来解决这个问题。

gogotester 这个软件项目托管在 GitHub 上，地址是 https://github.com/azzvx/gogotester，本文写作时的版本是 2.3。

如果在 GitHub 上搜索 gogotester，会得到多个结果。一定要认准 azzvx 的 gogotester 才是官方仓储。

gogotester 在 Google Code 上也有个家，地址是 https://code.google.com/p/gogo-tester。这里说明的比较详细，而且是汉语。但鉴于大量开源项目逐渐搬离 Google Code 前往 GitHub 的趋势，我们还是将重点放在 GitHub。

从 GitHub 的项目主页下载项目 zip 压缩包，或者使用 git 软件直接 clone。

gogotester 是个 C# 项目，下载得到工程源代码。不要急，尽管是源代码，但里面包含了编译装配好的 .exe 文件：GoGo Tester.exe，在 GoGo Tester\bin\Release\ 目录下。

运行 .exe 文件前需要先安装 [Microsoft .NET Framework 4（独立安装程序）](http://www.microsoft.com/zh-cn/download/details.aspx?id=17718)。

双击运行 .exe 文件，点击“随机测试”菜单，弹出窗口，要求你指定要获取的 IP 数量，默认是 20 个。默认值 20 个就可以，因为 20 个完全够用了，而且要寻找的 IP 数量越多，耗费的时间就越长。

点击“确定”，软件开始寻找 IP ，找到的会列出来。耗费的时间因时因地而异，几分钟或几小时。

已找到的 IP 表格中有一列叫“证书”，这一列里面的字母含义如下：

* G：可直连 Google
* A：可连接 AppSpot，即 GAE
* NN：无效 IP

我们需要带有 A 标记的 IP，右键点击 IP 表格，可以导出到剪切板。

找到的有效 IP 会用 | 符号连接成如下形式 IP 串：

    173.194.201.123|208.117.244.39|209.85.145.138|64.233.190.101|64.233.190.196|173.194.201.176|209.85.145.118|208.117.244.41|173.194.200.91|64.233.190.156|209.85.145.113|208.117.243.111|208.117.243.101|209.85.147.82|64.233.190.166|209.85.147.116|192.119.20.245|173.194.200.117|209.85.145.83

打开 GoAgent 的 proxy.ini 文件，找到 [iplist] 段落，如下所示：

    [iplist]
    *google_cn* = www.google.cn|www.g.cn
    *google_hk* = www.google.com|mail.google.com|www.google.com.hk|www.google.com.tw|www.l.google.com|www2.l.google.com|www3.l.google.com|www4.l.google.com|www5.l.google.com|mail.l.google.com|googleapis.l.google.com|googlecode.l.googleusercontent.com|maps.l.google.com|code.l.google.com|cert-test.sandbox.google.com
    *google_talk* = talk.google.com|talk.l.google.com|talkx.l.google.com

将 google_cn 和 google_hk 等号后面的字符串删掉或注释掉（proxy.ini 文件的注释是在行首加一个英文分号 ; ）。

在 google_cn 和 google_hk 等号后面填入上述 IP 串（注意不要把 google_talk 那部分删去），如下所示：

    [iplist]
    *google_cn* = 173.194.201.123|208.117.244.39|209.85.145.138|64.233.190.101|64.233.190.196|173.194.201.176|209.85.145.118|208.117.244.41|173.194.200.91|64.233.190.156|209.85.145.113|208.117.243.111|208.117.243.101|209.85.147.82|64.233.190.166|209.85.147.116|192.119.20.245|173.194.200.117|209.85.145.83
    *google_hk* = 173.194.201.123|208.117.244.39|209.85.145.138|64.233.190.101|64.233.190.196|173.194.201.176|209.85.145.118|208.117.244.41|173.194.200.91|64.233.190.156|209.85.145.113|208.117.243.111|208.117.243.101|209.85.147.82|64.233.190.166|209.85.147.116|192.119.20.245|173.194.200.117|209.85.145.83
    *google_talk* = talk.google.com|talk.l.google.com|talkx.l.google.com

利用 gogotester 寻找可用的 Google IP 需要不时的搞一搞。

## 运行 GoAgent

    $ python local/proxy.py // linux & mac
    双击 local/goagent.exe // windows

Firefox 和 Opera 需要导入证书。

对于 CentOS 6.x：

    $ yum install centos-release-SCL
    $ yum install python27

在 /etc/ld.so.conf.d/ 文件夹中建立文件 python27.conf，内容为 /opt/rh/python27/root/usr/lib64。

    $ ldconfig // 加载配置
    $ /opt/rh/python27/root/usr/bin/python proxy.py

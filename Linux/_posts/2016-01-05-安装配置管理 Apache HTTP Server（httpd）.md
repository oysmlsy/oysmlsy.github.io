---
title: 安装配置管理 Apache HTTP Server（httpd）
---

## 安装

    $ yum install httpd

## 管理

在 Windows 下，httpd 以系统服务的形式运行，在 Unix（Linux）下，httpd 作为 daemon（守护进程）运行。

httpd 官方文档推荐用 apachectl 这个 script 来调用 httpd 可执行程序，原因是：apachectl 首先会设置一些为保证 httpd 正确运行所必要的环境变量，然后再去调用 httpd 可执行程序，而且 apachectl 会把命令行参数原封不动的传递给 httpd。

apachectl 是 httpd daemon 的 front end，所以**管理员应该用 apachectl 来管理 httpd daemon**。

    $ apachectl start
    $ apachectl stop 或 graceful-stop
    $ apachectl restart 或 graceful
    $ apachectl status

如果不使用 apachectl 这个 script，也可以使用 service 这个管理 daemon 的命令。

    $ service httpd start
    $ service httpd stop
    $ service httpd restart
    $ service httpd status

如果系统支持 systemd（CentOS 7.x 开始支持 systemd），既可以用 service 命令，也可以用 systemd。

    $ systemctl start httpd.service
    $ systemctl stop httpd.service
    $ systemctl restart httpd.service
    $ systemctl status httpd.service
    $ systemctl is-active httpd.service

## 设置开机自动启动

如果操作系统有 systemd：

    $ systemctl enable httpd.service
    $ systemctl disable httpd.service

如果没有 systemd，修改 `/etc/rc.d/rc.local` 这个文件。

    $ vi /etc/rc.d/rc.local

添加以下命令：

    /usr/sbin/apachectl start

## 理解并设置虚拟主机

httpd 的主配置文件是 `/etc/httpd/conf/httpd.conf`。目录 `/etc/httpd/conf.d/` 下的文件只要以 `.conf` 作为扩展名，其内容就能被集成到主配置文件中。所以尽量不直接修改主配置文件，而是在目录 `/etc/httpd/conf.d/` 下面增加新的配置文件。

httpd 官方文档把 Virtual Host（虚拟主机）分为了2种：IP-based 和 Name-based。

可以这样理解：

在配置文件里放一个 `<VirtualHost></VirtualHost>` block，就代表配置了一个 Virtual Host，放2个就代表配置了2个。起始标签 `<VirtualHost>` 里需要说明IP地址和端口，即这个样子：`<VirtualHost 192.168.1.1:80>`，IP 可以是 `*`，端口可以不写。

一个 request 进来之后，会根据 IP 地址和端口按照配置文件中的顺序来一个个匹配 `<VirtualHost></VirtualHost>` block。如果所有的 `<VirtualHost></VirtualHost>` block 都没匹配上，那么就去咨询主配置文件里的指示。而一旦某些 `<VirtualHost></VirtualHost>` block 匹配上了，那么只有这些匹配上的 block 才能成为 request 的候选者，其它的 `<VirtualHost></VirtualHost>` block 包括主配置文件就都没有机会了。

如果候选者只有1个，那么没的挑了，就是它了。而如果候选者有多个，怎么选？

这时就得看 `<VirtualHost></VirtualHost>` block 里面的 `ServerName` 和 `ServerAlias` 指示，谁的 `ServerName`、`ServerAlias` 与 request 的 HTTP 报文的 header 的 Host相匹配，那么谁就胜出。如果多个 block 都匹配，那么先来后到，谁在前边谁胜出。如果都不匹配，那么还是先来后到。

示例如下：

    Listen 80
    <VirtualHost *:80>
        DocumentRoot /var/www/html
        ServerName www.example.com
        ServerAlias example.com
    </VirtualHost>
    <Directory "/var/www/html">
        AllowOverride All
    </Directory>

`AllowOverride All` 的作用是使 web 目录内的 .htaccess 文件起作用，常用于开启 Drupal 的简洁 URL。

如果 VirtualHost 指定了端口，需要写上 `Listen` 指示，因为只有先告诉 httpd 监听某个端口，request 才能从这个端口进来，进而进入某个 VirtualHost。httpd 主配置文件默认已经配置了 `Listen 80`，所以 VirtualHost 如果指定80端口，就不需要再此指示监听80端口了，配置文件里重复的指示不符合语法。

## SELinux 搞鬼，造成 httpd 无法监听自定义端口

我们知道在 Linux 系统里，0-1023是公认端口号，即已经公认定义或为将要公认定义的软件保留的，而1024-65535是并没有公认定义的端口号，用户可以自己定义这些端口的作用。

那么我们配置 VirtualHost 时，任意指定1024-65535范围内的端口号就可以了吗？

理论上是正确的。但 CentOS 默认开启了 SELinux，SELinux 会约束使用 http 协议的端口范围。使用下面的命令查看一下支持 http 的端口有哪些：

    $ semanage port -l | grep http

stdout 输出的结果中有这么一行：`http_port_t tcp 80, 81, 443, 488, 8008, 8009, 8443, 9000`，原来只有这几个端口可以用在 http 上。

所以在配置 VirtualHost 时，把端口号约束在 SELinux 允许的范围内就 OK 了。

如果你强烈需要 VirtualHost 监听某一个自定义端口，比如10000，那么你可以告知 SELinux 为 http 添加新的端口号：

    $ semanage port -a -t http_port_t -p tcp 10000

SELinux 的配置文件在 `/etc/selinux/config`，里面的注释说的很清楚，你可以使安全策略强制施行，也可以仅生成警告，也可以 disable 安全策略。

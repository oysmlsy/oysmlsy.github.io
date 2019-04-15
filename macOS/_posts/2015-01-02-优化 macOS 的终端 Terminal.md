---
title: 优化 macOS 的终端 Terminal
---

## 支持 ll 命令

类 Unix 系统中，`ll`命令是`ls -l`的别名。

终端默认没有`ll`命令，在 Bash 配置文件中添加别名：

    $ echo 'alias ll="ls -l"' >> ~/.bash_profile

## ls 命令区分文件夹和文件的颜色

终端默认`ls`命令输出中的文件夹、各种文件类型没有颜色区分。

在 Bash 配置文件中暴露两个环境变量即可：

    $ echo 'export CLICOLOR=1' >> ~/.bash_profile
    $ echo 'export LSCOLORS=gxfxaxdxcxegedabagacad' >> ~/.bash_profile

CLICOLOR 用来设置是否进行颜色的显示；LSCOLORS 用来设置当 CLICOLOR 被启用后，各种文件类型的颜色。

LSCOLORS 的值中每两个字母为一组，分别设置某个文件类型的文字颜色和背景颜色。

LSCOLORS 中一共11组颜色设置，按照先后顺序，分别对以下的文件类型进行设置：

* 1 directory
* 2 symbolic link
* 3 socket
* 4 pipe
* 5 executable
* 6 block special
* 7 character special
* 8 executable with setuid bit set
* 9 executable with setgid bit set
* 10 directory writable to others, with sticky bit
* 11 directory writable to others, without sticky bit

LSCOLORS 中，字母代表的颜色如下：

* a 黑色
* b 红色
* c 绿色
* d 棕色
* e 蓝色
* f 洋红色
* g 青色
* h 浅灰色
* A 黑色粗体
* B 红色粗体
* C 绿色粗体
* D 棕色粗体
* E 蓝色粗体
* F 洋红色粗体
* G 青色粗体
* H 浅灰色粗体

## 设置终端输入 exit 或 CTRL+D 自动关闭终端窗口

终端默认输入 exit 或 CTRL+D 之后 只是结束了进程，窗口并没有关闭。

选取“终端”>“偏好设置”，点按“描述文件”，然后在“当 shell 退出时”下拉框处选择“关闭窗口”。

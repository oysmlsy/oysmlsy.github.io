---
title: macOS 软件包管理器 Homebrew
---

在 macOS 中安装软件，我遵循的原则：尽可能使用 App Store、Homebrew 和 Homebrew Cask 进行安装。因为软件的安装、更新、卸载可以被管理起来，只有像 Microsoft Office、Adobe 全家桶这类软件才手动安装。

## 安装 Homebrew

大概步骤：Command Line Tools -> Homebrew -> Homebrew Cask

Homebrew 依赖于 Command Line Tools，首先安装之：

    $ xcode-select --install

安装完成后，再次运行`xcode-select --install`，如果出现下述输出，则说明安装成功。

    $ xcode-select --install
    xcode-select: error: command line tools are already installed, use "Software Update" to install updates

访问 Homebrew 官网 [https://brew.sh](https://brew.sh)，首页清楚的告知安装只需一条命令：

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

这条命令的意思：

* 复制粘贴 URL`https://raw.githubusercontent.com/Homebrew/install/master/install`至浏览器，可知其指向的是一个 Ruby 脚本文件。
* 用`curl`命令把文件取下来。
* 我们知道`curl`命令默认会将结果输出至 stdout，那么再用`$( )`将其扩起来，会导致`curl`命令的输出被填充至命令中的双引号`""`之间。
* macOS 自带 Ruby，即`/usr/bin/ruby`，加上 `-e` 选项，就是用 Ruby 解释器执行命令参数部分的 Ruby 代码。

验证安装是否成功：

    $ brew doctor
    Your system is ready to brew.

## Homebrew 安装目录详解

Homebrew 主要涉及`/usr/local/`目录下的3个子目录：`Homebrew/`、`Cellar/`和`Caskroom/`。

`/usr/local/Homebrew/`是 Homebrew 的程序安装目录。

Homebrew 的 GitHub 地址是 Homebrew/brew，安装脚本把 Homebrew 的 GitHub 仓库克隆至`/usr/local/Homebrew/`目录，并把里面的可执行文件`/usr/local/Homebrew/bin/brew`软链接至`/usr/local/bin/brew`。

而`/usr/local/bin/`目录是 PATH 环境变量的一部分。

`/usr/local/Cellar/`目录是通过`brew install <formula>`命令安装的软件包的安装所在路径，里面的每个子目录都是一个包，目录名即为包名，按照`Cellar/包名/版本号/`的形式来安放，包括可执行程序、文档和配置文件。

Homebrew 把软件包称为 formula（formula 的复数是 formulae）。

每个软件包的可执行程序被软链接至`/usr/local/bin/`，例如：

    // 查看一下在命令行里直接输入`python`命令到底执行的是哪个可执行文件
    $ type python
    python is /usr/bin/python
    // /usr/bin/python 是 macOS 预装的 Python

    // 通过 Homebrew 安装 Python 2.x
    $ brew install python@2

    // 再看一下，变成了刚刚 Homebrew 安装的
    $ type python
    python is /usr/local/bin/python

    // /usr/local/bin/python 是个软链接
    $ ls -l /usr/local/bin/python
    lrwxr-xr-x  1 oysmlsy  admin  38  4 26 20:21 /usr/local/bin/python -> ../Cellar/python@2/2.7.14_3/bin/python

通常`/usr/bin/`存放的是系统预装的可执行程序，会随着系统升级而改变。

`/usr/local/bin/`目录是给用户放置自己的可执行程序的地方，不会被系统升级而覆盖同名文件。

如果两个目录下有相同的可执行程序，谁优先执行受到 PATH 环境变量的影响。

看一下 PATH 环境变量：

    $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

`/usr/local/bin/`通常在`/usr/bin/`之前，所以`/usr/local/bin/`优先于`/usr/bin/`。

`/usr/local/Caskroom/`用于存放通过`brew cask install <cask>`命令安装的软件包，里面的每个子目录都是一个包，目录名即为包名，按照`Caskroom/包名/版本号/`的形式来安放。

Homebrew Cask 将下载安装好的二进制程序`XXX.app`文件放到`/Applications/`目录下。

Homebrew Cask 把软件包称为 cask。

## 安装常用软件

    $ brew cask install google-chrome   // Google Chrome 浏览器，前端开发必备
    $ brew cask install vmware-fusion   // macOS 版本的 VMware 非常优秀
    $ brew cask install go2shell        // 一个可以快速在 Finder 当前目录打开 Shell 的工具，小巧好用
    $ brew cask install ccleaner        // CCleaner，用来清理系统、卸载手动安装的软件
    $ brew cask install sublime         // Sublime Text 3，开发必备
    $ brew cask install pycharm         // PyCharm，Python 开发必备 IDE
    $ brew cask install docker          // Docker CE for Mac
    $ brew cask install quicklook-json  // Finder 中通过按下空格快速预览 JSON 文件的小工具
    $ brew cask install iina            // macOS 上非常优秀的视频播放器
    $ brew install wget                 // macOS 自带 curl，不能少了 wget
    $ brew install unrar                // 用来解压来自 Windows 平台的 .rar 文件
    $ brew install p7zip                // p7zip，是 Windows 平台的 7-Zip 的 Linux 版本

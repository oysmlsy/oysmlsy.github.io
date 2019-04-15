---
title: 打造自己的 Sublime Text 3
---

## 优化 User Settings

选取菜单“Sublime Text”>“Preferences”>“Settings”，或输入`CMD+,`，打开“Default/Preferences.sublime-settings”和“Packages/User/Preferences.sublime-settings”配置文件。

“Default/Preferences.sublime-settings”文件只起示范作用，不应作修改。

自定义的 settings 应写进“Packages/User/Preferences.sublime-settings”文件。

特定语法（syntax-specific）的配置文件，如 Python 的配置文件“Packages/User/Python.sublime-settings”也可以用来承载自定义的 settings。

优先级：“Packages/User/Python.sublime-settings”>“Packages/User/Preferences.sublime-settings”>“Default/Preferences.sublime-settings”

在“Packages/User/Preferences.sublime-settings”配置文件里写入：

    {
        // 定义插入符号（光标）caret 如何闪烁的样式
        "caret_style": "phase",

        // 使空白字符，如空格、Tab 制表符等永久可见
        "draw_white_space": "all",

        // 保存文件时，保证文件末尾至少有一个空行
        "ensure_newline_at_eof_on_save": true,

        // 设置默认字体大小
        "font_size": 12,

        // 设置插入符号（光标）所在的行被高亮显示，以便轻松定位当前光标位置
        "highlight_line": true,

        // 使被修改但尚未保存的文件的标签（Tab）更明显
        "highlight_modified_tabs": true,

        // 1个 Tab 制表符相当于4个空格的宽度
        "tab_size": 4,

        // 设置将插入的 Tab 制表符自动转换为空格
        "translate_tabs_to_spaces": true,

        // 保存文件时，保证行末没有空白字符
        "trim_trailing_white_space_on_save": true
    }

## 安装 Package Control

访问 [Package Control](https://packagecontrol.io) 官网，按照官方最新方法进行安装。

## 常用插件

#### Sublime Tutor

类似 vimtutor 的快捷键起步教程，打开方式：选取菜单“Help”>“Sublime Tutor”。

> I always believed that the best way to learn anything is by doing it.

#### Emmet

大名鼎鼎的前端利器，因为依赖于PyV8，所以最好翻墙安装。

#### Side​Bar​Enhancements

增强了默认的 Sidebar。

#### Expand Tabs on Save

保存时，自动将“Tab缩进”转换为“空格”。`Packages/User/Preferences.sublime-settings`文件中需配置：`"convert_tabspaces_on_save": true`。

#### Terminal

实现了 Sublime Text 中在当前文件或文件夹的位置直接打开终端（Terminal），使用方法：右键。

#### Git

通过 Command Palette 使用 Git。

#### jQuery

jQuery 代码片段（Code Snippets）。

#### Bootstrap 3 Snippets

Bootstrap 3 代码片段（Code Snippets）。`Packages/User/Preferences.sublime-settings`文件中需配置：`"auto_complete_triggers": [{"selector": "text.html", "characters": "bs3"}]`。

#### Bootstrap 3 Autocomplete

Bootstrap 3 智能提示。

#### Bootstrap 4 Snippets

Bootstrap 4 代码片段（Code Snippets）。`Packages/User/Preferences.sublime-settings`文件中需配置：`"auto_complete_triggers": [{"selector": "text.html", "characters": "bs4"}]`。

#### Bootstrap 4 Autocomplete

Bootstrap 4 智能提示。

#### Color Highlighter

颜色代码处直观显示颜色，并提供拾色器（Color Picker）。

#### BracketHighlighter

Highlight 各种配对的括号和标签。

#### HTML-CSS-JS Prettify

HTML，CSS，JavaScript，JSON code formatter，依赖于 Node.js。

#### Anaconda

Python IDE。

#### Go​Sublime

Golang IDE。

#### Markdown​Highlighting

高亮 Markdown 语法。

#### LESS

编写 .less 文件必备，高亮 LESS 语法（syntax highlighting）。

## 常用快捷键

* `super + ,` - Edit settings
* `ctrl + backquote` - Show Console

* `super + n` - New file
* `super + shift + n` - New window

* `super + w` - Close
* `super + shift + w` - Close window

* `super + s` - Save
* `super + shift + s` - Prompt save as
* `super + alt + s` - Save all

* `super + o` - Prompt open
* `super + shift + t` - Reopen last file

* `super + z` - Undo
* `super + shift + z` - Redo
* `super + u` - Soft undo
* `super + shift + u` - Soft redo

* `super + x` - Cut
* `super + c` - Copy
* `super + v` - Paste
* `super + a` - Select all
* `super + l` - Expand selection to line
* `super + j` - Join lines
* `super + b` - Build
* `super + ]` - Indent
* `super + [` - Unindent
* `super + equals` - Increase font size
* `super + plus` - Increase font size
* `super + minus` - Decrease font size

* `super + f` - Show panel find
* `super + alt + f` - Show panel replace
* `super + shift + f` - Show panel find_in_files
* `super + e` - Slurp find string
* `super + g` - Find next
* `super + shift + g` - Find prev

* `super + k, super + b` - Toggle side bar
* `super + k, super + v` - Paste from history
* `super + k, super + up` - New pane
* `super + k, super + down` - Close pane
* `super + k, super + u` - Upper case
* `super + k, super + l` - Lower case

* `super + t` - Show goto overlay (Goto Anything)
* `super + p` - Show goto overlay (Goto Anything)
* `super + shift + p` - Show command palette overlay
* `super + r` - Show goto @ overlay (Goto Symbol)
* `ctrl + g` - Show goto : overlay (Goto Line)

* `super + ctrl + f` - Toggle full screen
* `ctrl + tab` - Next view in stack
* `ctrl + shift + tab` - Prev view in stack
* `super + shift + space` - Expand selection to scope
* `ctrl + shift + m` - Expand selection to brackets
* `f5` - Sort lines

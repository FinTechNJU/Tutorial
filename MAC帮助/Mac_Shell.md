##### Mac配置环境变量的地方

 1./etc/profile   （建议不修改这个文件 ）
 全局（公有）配置，不管是哪个用户，登录时都会读取该文件。

 2./etc/bashrc    （一般在这个文件中添加系统级环境变量）
 全局（公有）配置，bash shell执行时，不管是何种方式，都会读取此文件。

 3.~/.bash_profile  （一般在这个文件中添加用户级环境变量）

 每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该文件仅仅执行一次!

less 浏览文件内容

- 选项，--长选项

在Unix系统中，一切皆文件。

less is more less 是Unix程序more的改进版本。

列出目录内容 ls -l

| 目录           | 评论                                                         |
| :------------- | :----------------------------------------------------------- |
| /              | 根目录，万物起源。                                           |
| /bin           | 包含系统启动和运行所必须的二进制程序。                       |
| /boot          | 包含 Linux 内核、初始 RAM 磁盘映像（用于启动时所需的驱动）和 启动加载程序。有趣的文件：/boot/grub/grub.conf or menu.lst， 被用来配置启动加载程序。/boot/vmlinuz，Linux 内核。 |
| /dev           | 这是一个包含设备结点的特殊目录。“一切都是文件”，也适用于设备。 在这个目录里，内核维护着所有设备的列表。 |
| /etc           | 这个目录包含所有系统层面的配置文件。它也包含一系列的 shell 脚本， 在系统启动时，这些脚本会开启每个系统服务。这个目录中的任何文件应该是可读的文本文件。有趣的文件：虽然/etc 目录中的任何文件都有趣，但这里只列出了一些我一直喜欢的文件：/etc/crontab， 定义自动运行的任务。/etc/fstab，包含存储设备的列表，以及与他们相关的挂载点。/etc/passwd，包含用户帐号列表。 |
| /home          | 在通常的配置环境下，系统会在/home 下，给每个用户分配一个目录。普通用户只能 在自己的目录下写文件。这个限制保护系统免受错误的用户活动破坏。 |
| /lib           | 包含核心系统程序所使用的共享库文件。这些文件与 Windows 中的动态链接库相似。 |
| /lost+found    | 每个使用 Linux 文件系统的格式化分区或设备，例如 ext3文件系统， 都会有这个目录。当部分恢复一个损坏的文件系统时，会用到这个目录。这个目录应该是空的，除非文件系统 真正的损坏了。 |
| /media         | 在现在的 Linux 系统中，/media 目录会包含可移动介质的挂载点， 例如 USB 驱动器，CD-ROMs 等等。这些介质连接到计算机之后，会自动地挂载到这个目录结点下。 |
| /mnt           | 在早些的 Linux 系统中，/mnt 目录包含可移动介质的挂载点。     |
| /opt           | 这个/opt 目录被用来安装“可选的”软件。这个主要用来存储可能 安装在系统中的商业软件产品。 |
| /proc          | 这个/proc 目录很特殊。从存储在硬盘上的文件的意义上说，它不是真正的文件系统。 相反，它是一个由 Linux 内核维护的虚拟文件系统。它所包含的文件是内核的窥视孔。这些文件是可读的， 它们会告诉你内核是怎样监管计算机的。 |
| /root          | root 帐户的家目录。                                          |
| /sbin          | 这个目录包含“系统”二进制文件。它们是完成重大系统任务的程序，通常为超级用户保留。 |
| /tmp           | 这个/tmp 目录，是用来存储由各种程序创建的临时文件的地方。一些配置导致系统每次 重新启动时，都会清空这个目录。 |
| /usr           | 在 Linux 系统中，/usr 目录可能是最大的一个。它包含普通用户所需要的所有程序和文件。 |
| /usr/bin       | /usr/bin 目录包含系统安装的可执行程序。通常，这个目录会包含许多程序。 |
| /usr/lib       | 包含由/usr/bin 目录中的程序所用的共享库。                    |
| /usr/local     | 这个/usr/local 目录，是非系统发行版自带程序的安装目录。 通常，由源码编译的程序会安装在/usr/local/bin 目录下。新安装的 Linux 系统中会存在这个目录， 并且在管理员安装程序之前，这个目录是空的。 |
| /usr/sbin      | 包含许多系统管理程序。                                       |
| /usr/share     | /usr/share 目录包含许多由/usr/bin 目录中的程序使用的共享数据。 其中包括像默认的配置文件、图标、桌面背景、音频文件等等。 |
| /usr/share/doc | 大多数安装在系统中的软件包会包含一些文档。在/usr/share/doc 目录下， 我们可以找到按照软件包分类的文档。 |
| /var           | 除了/tmp 和/home 目录之外，相对来说，目前我们看到的目录是静态的，这是说， 它们的内容不会改变。/var 目录存放的是动态文件。各种数据库，假脱机文件， 用户邮件等等，都位于在这里。 |
| /var/log       | 这个/var/log 目录包含日志文件、各种系统活动的记录。这些文件非常重要，并且 应该时时监测它们。其中最重要的一个文件是/var/log/messages。注意，为了系统安全，在一些系统中， 你必须是超级用户才能查看这些日志文件。 |

| 按键                | 移动光标                                          |
| :------------------ | :------------------------------------------------ |
| l or 右箭头         | 向右移动一个字符                                  |
| h or 左箭头         | 向左移动一个字符                                  |
| j or 下箭头         | 向下移动一行                                      |
| k or 上箭头         | 向上移动一行                                      |
| 0 (零按键)          | 移动到当前行的行首。                              |
| ^                   | 移动到当前行的第一个非空字符。                    |
| $                   | 移动到当前行的末尾。                              |
| w                   | 移动到下一个单词或标点符号的开头。                |
| W                   | 移动到下一个单词的开头，忽略标点符号。            |
| b                   | 移动到上一个单词或标点符号的开头。                |
| B                   | 移动到上一个单词的开头，忽略标点符号。            |
| Ctrl-f or Page Down | 向下翻一页                                        |
| Ctrl-b or Page Up   | 向上翻一页                                        |
| numberG             | 移动到第 number 行。例如，1G 移动到文件的第一行。 |
| G                   | 移动到文件末尾。                                  |

| 命令 | 删除的文本                               |
| :--- | :--------------------------------------- |
| x    | 当前字符                                 |
| 3x   | 当前字符及其后的两个字符。               |
| dd   | 当前行。                                 |
| 5dd  | 当前行及随后的四行文本。                 |
| dW   | 从光标位置开始到下一个单词的开头。       |
| d$   | 从光标位置开始到当前行的行尾。           |
| d0   | 从光标位置开始到当前行的行首。           |
| d^   | 从光标位置开始到文本行的第一个非空字符。 |
| dG   | 从当前行到文件的末尾。                   |
| d20G | 从当前行到文件的第20行。                 |

| 命令 | 删除的文本                               |
| :--- | :--------------------------------------- |
| x    | 当前字符                                 |
| 3x   | 当前字符及其后的两个字符。               |
| dd   | 当前行。                                 |
| 5dd  | 当前行及随后的四行文本。                 |
| dW   | 从光标位置开始到下一个单词的开头。       |
| d$   | 从光标位置开始到当前行的行尾。           |
| d0   | 从光标位置开始到当前行的行首。           |
| d^   | 从光标位置开始到文本行的第一个非空字符。 |
| dG   | 从当前行到文件的末尾。                   |
| d20G | 从当前行到文件的第20行。                 |

| !!       | 重复最后一次执行的命令。可能按下上箭头按键和 enter 键更容易些。 |
| -------- | ------------------------------------------------------------ |
| !number  | 重复历史列表中第 number 行的命令。                           |
| !string  | 重复最近历史列表中，以这个字符串开头的命令。                 |
| !?string | 重复最近历史列表中，包含这个字符串的命令。                   |

属于 GNU 项目的程序，还有其它许多程序都会，提供文档文件 README，INSTALL，NEWS，和 COPYING。

*登录 shell 会话的启动文件*

| 文件            | 内容                                                         |
| :-------------- | :----------------------------------------------------------- |
| /etc/profile    | 应用于所有用户的全局配置脚本。                               |
| ~/.bash_profile | 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。 |
| ~/.bash_login   | 如果文件 ~/.bash_profile 没有找到，bash 会尝试读取这个脚本。 |
| ~/.profile      | 如果文件 ~/.bash_profile 或文件 ~/.bash_login 都没有找到，bash 会试图读取这个文件。 这是基于 Debian 发行版的默认设置，比方说 Ubuntu。 |

*非登录 shell 会话的启动文件*

| 文件             | 内容                                                         |
| :--------------- | :----------------------------------------------------------- |
| /etc/bash.bashrc | 应用于所有用户的全局配置文件。                               |
| ~/.bashrc        | 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。 |

```
export PATH
```

这个 export 命令告诉 shell 让这个 shell 的子进程可以使用 PATH 变量的内容。

备份文件的名字无关紧要，只要选择一个容易理解的文件名。扩展名 “.bak”、”.sav”、 “.old”和 “.orig” 都是用来指示备份文件的流行方法。哦，记住 cp 命令会默默地覆盖已经存在的同名文件。

```
apple key code list
```

```
0 0x00 ANSI_A
1 0x01 ANSI_S
2 0x02 ANSI_D
3 0x03 ANSI_F
4 0x04 ANSI_H
5 0x05 ANSI_G
6 0x06 ANSI_Z
7 0x07 ANSI_X
8 0x08 ANSI_C
9 0x09 ANSI_V
10 0x0A ISO_Section
11 0x0B ANSI_B
12 0x0C ANSI_Q
13 0x0D ANSI_W
14 0x0E ANSI_E
15 0x0F ANSI_R
16 0x10 ANSI_Y
17 0x11 ANSI_T
18 0x12 ANSI_1
19 0x13 ANSI_2
20 0x14 ANSI_3
21 0x15 ANSI_4
22 0x16 ANSI_6
23 0x17 ANSI_5
24 0x18 ANSI_Equal
25 0x19 ANSI_9
26 0x1A ANSI_7
27 0x1B ANSI_Minus
28 0x1C ANSI_8
29 0x1D ANSI_0
30 0x1E ANSI_RightBracket
31 0x1F ANSI_O
32 0x20 ANSI_U
33 0x21 ANSI_LeftBracket
34 0x22 ANSI_I
35 0x23 ANSI_P
36 0x24 Return
37 0x25 ANSI_L
38 0x26 ANSI_J
39 0x27 ANSI_Quote
40 0x28 ANSI_K
41 0x29 ANSI_Semicolon
42 0x2A ANSI_Backslash
43 0x2B ANSI_Comma
44 0x2C ANSI_Slash
45 0x2D ANSI_N
46 0x2E ANSI_M
47 0x2F ANSI_Period
48 0x30 Tab
49 0x31 Space
50 0x32 ANSI_Grave
51 0x33 Delete
53 0x35 Escape
55 0x37 Command
56 0x38 Shift
57 0x39 CapsLock
58 0x3A Option
59 0x3B Control
60 0x3C RightShift
61 0x3D RightOption
62 0x3E RightControl
63 0x3F Function
64 0x40 F17
65 0x41 ANSI_KeypadDecimal
67 0x43 ANSI_KeypadMultiply
69 0x45 ANSI_KeypadPlus
71 0x47 ANSI_KeypadClear
72 0x48 VolumeUp
73 0x49 VolumeDown
74 0x4A Mute
75 0x4B ANSI_KeypadDivide
76 0x4C ANSI_KeypadEnter
78 0x4E ANSI_KeypadMinus
79 0x4F F18
80 0x50 F19
81 0x51 ANSI_KeypadEquals
82 0x52 ANSI_Keypad0
83 0x53 ANSI_Keypad1
84 0x54 ANSI_Keypad2
85 0x55 ANSI_Keypad3
86 0x56 ANSI_Keypad4
87 0x57 ANSI_Keypad5
88 0x58 ANSI_Keypad6
89 0x59 ANSI_Keypad7
90 0x5A F20
91 0x5B ANSI_Keypad8
92 0x5C ANSI_Keypad9
93 0x5D JIS_Yen
94 0x5E JIS_Underscore
95 0x5F JIS_KeypadComma
96 0x60 F5
97 0x61 F6
98 0x62 F7
99 0x63 F3
100 0x64 F8
101 0x65 F9
102 0x66 JIS_Eisu
103 0x67 F11
104 0x68 JIS_Kana
105 0x69 F13
106 0x6A F16
107 0x6B F14
109 0x6D F10
111 0x6F F12
113 0x71 F15
114 0x72 Help
115 0x73 Home
116 0x74 PageUp
117 0x75 ForwardDelete
118 0x76 F4
119 0x77 End
120 0x78 F2
121 0x79 PageDown
122 0x7A F1
123 0x7B LeftArrow
124 0x7C RightArrow
125 0x7D DownArrow
126 0x7E UpArrow
```

参考文档：https://en.wikibooks.org/wiki/Category:Book:AppleScript_Programming

sascript was designed for use with AppleScript, but will work with any Open Scripting Architecture (OSA) language.

###### An A-Z Index of the **Apple macOS** command line (macOS bash)

https://ss64.com/osx/

Info.plist中添加

```
<key>LSUIElement</key>
<string>1</string>
```

```
ps aux | grep YOUR_SCRIPT_NAME` and `kill PROCESS_ID
```




